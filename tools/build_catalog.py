#!/usr/bin/env python3
"""Build the student-facing site data file `data/site.json`.

Inputs (all editable, all checked in):

* `data/catalog/subjects.json`  — subjects, topic titles (English + Hindi), routes.
* `data/catalog/materials.json` — every downloadable student file, one row each.
* `data/banks/cn/manifest.json` — generated question-bank manifest and topic chunks
  (produced by `tools/build_site_data.py` from the canonical bank).

Output:

* `data/site.json` — the only data file the website fetches for its pages.

Wiring rules enforced here (the build fails instead of shipping a wrong page):

1. Every file under `content/` must be registered in `materials.json`.
2. Every registered file must exist, and must live under `content/`.
3. Every registered topic must exist in the bank manifest and match its topic name.
4. Counts, byte sizes and SHA-256 values come from the real files, never hand-typed.

Run:

    python3 tools/build_catalog.py            # write data/site.json
    python3 tools/build_catalog.py --check    # fail if data/site.json is out of date
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
import urllib.parse
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "data/catalog"
CONTENT = ROOT / "content"
BANK_MANIFEST = ROOT / "data/banks/cn/manifest.json"
OUTPUT = ROOT / "data/site.json"

CONTENT_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".webp", ".svg"}
KINDS = ("theory", "practice", "test", "reference", "map")

SECTION_PREFIX = re.compile(r"^section\s+[a-z0-9]+\s*[-–—:]\s*", re.IGNORECASE)


def read_json(path: pathlib.Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def human_size(num_bytes: int) -> str:
    if num_bytes >= 1024 * 1024:
        return f"{num_bytes / (1024 * 1024):.1f} MB"
    if num_bytes >= 1024:
        return f"{num_bytes / 1024:.0f} KB"
    return f"{num_bytes} B"


def url_for(rel_path: str) -> str:
    return urllib.parse.quote(rel_path, safe="/")


def content_files() -> list[str]:
    found = []
    for path in sorted(CONTENT.rglob("*")):
        if not path.is_file():
            continue
        if path.name.startswith(".") or path.suffix.lower() not in CONTENT_SUFFIXES:
            continue
        found.append(path.relative_to(ROOT).as_posix())
    return found


def section_label(title: str) -> str:
    """Short, readable section name for buttons and chips."""
    text = SECTION_PREFIX.sub("", title or "").strip()
    part = text.split(" (", 1)[0].split(" — ", 1)[0].strip(" -–—")
    return part or text


def load_bank() -> dict:
    if not BANK_MANIFEST.is_file():
        raise SystemExit("FAIL: data/banks/cn/manifest.json missing — run tools/build_site_data.py first")
    manifest = read_json(BANK_MANIFEST)
    topics = {}
    total_questions = 0
    total_sections = 0
    for chunk in manifest.get("topics", []):
        topic_id = chunk["topic_id"]
        chunk_path = ROOT / chunk["file"]
        if not chunk_path.is_file():
            raise SystemExit(f"FAIL: bank chunk missing for {topic_id}: {chunk['file']}")
        records = read_json(chunk_path)
        seen: dict[str, dict] = {}
        for record in records:
            title = (record.get("subtopic") or "").strip()
            if not title:
                continue
            bucket = seen.setdefault(title, {"title": title, "short": section_label(title), "count": 0})
            bucket["count"] += 1
        sections = list(seen.values())
        total_sections += len(sections)
        total_questions += len(records)
        topics[topic_id] = {
            "id": topic_id,
            "title_en": chunk["topic_name"],
            "question_count": len(records),
            "sections": sections,
        }
    manifest["_topics"] = topics
    manifest["_question_total"] = total_questions
    manifest["_section_total"] = total_sections
    return manifest


def build() -> dict:
    subjects_doc = read_json(CATALOG / "subjects.json")
    materials_doc = read_json(CATALOG / "materials.json")
    bank = load_bank()

    registered = materials_doc.get("materials", [])
    registered_paths = [item["file"] for item in registered]
    duplicates = {path for path in registered_paths if registered_paths.count(path) > 1}
    if duplicates:
        raise SystemExit(f"FAIL: file registered more than once in materials.json: {sorted(duplicates)}")

    on_disk = set(content_files())
    missing_from_registry = sorted(on_disk - set(registered_paths))
    if missing_from_registry:
        raise SystemExit(
            "FAIL: these content files are not registered in data/catalog/materials.json:\n  - "
            + "\n  - ".join(missing_from_registry)
        )
    missing_on_disk = sorted(set(registered_paths) - on_disk)
    if missing_on_disk:
        raise SystemExit(
            "FAIL: these registered files do not exist:\n  - " + "\n  - ".join(missing_on_disk)
        )

    groups = {group["id"]: group for group in materials_doc.get("groups", [])}
    subject_ids = [subject["id"] for subject in subjects_doc["subjects"]]

    items: list[dict] = []
    for raw in registered:
        kind = raw.get("kind")
        if kind not in KINDS:
            raise SystemExit(f"FAIL: unknown kind {kind!r} for {raw['file']}")
        if raw["subject"] not in subject_ids:
            raise SystemExit(f"FAIL: unknown subject {raw['subject']!r} for {raw['file']}")
        path = ROOT / raw["file"]
        size = path.stat().st_size
        items.append({
            "id": raw["file"].split("/", 1)[1].replace("/", "-").rsplit(".", 1)[0],
            "subject": raw["subject"],
            "kind": kind,
            "topic_id": raw.get("topic"),
            "order": raw.get("order", 0),
            "title_en": raw["title_en"],
            "title_hi": raw["title_hi"],
            "note_en": raw.get("note_en", ""),
            "note_hi": raw.get("note_hi", ""),
            "repo_path": raw["file"],
            "url": url_for(raw["file"]),
            "file_name": path.name,
            "file_type": path.suffix.lstrip(".").upper(),
            "bytes": size,
            "size_label": human_size(size),
            "sha256": sha256(path),
        })

    subjects = []
    for subject in subjects_doc["subjects"]:
        slug = subject["slug"]
        own = [item for item in items if item["subject"] == subject["id"]]
        entry = {
            "id": subject["id"],
            "slug": slug,
            "title_en": subject["title_en"],
            "title_hi": subject["title_hi"],
            "tagline_en": subject["tagline_en"],
            "tagline_hi": subject["tagline_hi"],
            "intro_en": subject["intro_en"],
            "intro_hi": subject["intro_hi"],
            "has_material": bool(subject.get("has_material")),
            "has_test": bool(subject.get("has_test")),
            "has_maps": bool(subject.get("has_maps")),
            "route": f"subjects/{slug}/index.html",
            "material_route": f"subjects/{slug}/material/index.html" if subject.get("has_material") else None,
            "test_route": f"subjects/{slug}/test/index.html" if subject.get("has_test") else None,
            "file_count": len(own),
            "total_bytes": sum(item["bytes"] for item in own),
        }

        if subject.get("has_test"):
            bank_topics = bank["_topics"]
            topics = []
            for topic in subject["topics"]:
                topic_id = topic["id"]
                if topic_id not in bank_topics:
                    raise SystemExit(f"FAIL: topic {topic_id} has no question bank chunk")
                bank_topic = bank_topics[topic_id]
                if topic["title_en"].strip() != bank_topic["title_en"].strip():
                    raise SystemExit(
                        f"FAIL: topic {topic_id} name mismatch — bank has {bank_topic['title_en']!r}, "
                        f"catalogue has {topic['title_en']!r}"
                    )
                topics.append({
                    "id": topic_id,
                    "title_en": topic["title_en"],
                    "title_hi": topic["title_hi"],
                    "question_count": bank_topic["question_count"],
                    "section_count": len(bank_topic["sections"]),
                    "sections": bank_topic["sections"],
                    "material": {
                        kind: sorted(
                            [item for item in own if item["kind"] == kind and item["topic_id"] == topic_id],
                            key=lambda item: item["order"],
                        )
                        for kind in KINDS
                    },
                })
            entry["topics"] = topics
            entry["test"] = {
                "build_id": bank.get("bank_build_id"),
                "manifest_url": "data/banks/cn/manifest.json",
                "question_count": bank["_question_total"],
                "topic_count": len(topics),
                "section_count": bank["_section_total"],
            }
        else:
            entry["topics"] = []

        groups_out = []
        for group in sorted(groups.values(), key=lambda group: group["order"]):
            group_items = sorted(
                [item for item in own if item["kind"] == group["id"]],
                key=lambda item: (item["topic_id"] or "ZZ", item["order"]),
            )
            if group_items:
                groups_out.append({**group, "items": group_items})
        entry["groups"] = groups_out
        subjects.append(entry)

    return {
        "schema_version": 1,
        "generated_on": date.today().isoformat(),
        "brand": subjects_doc["brand"],
        "bank_build_id": bank.get("bank_build_id"),
        "subjects": subjects,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify data/site.json is current")
    args = parser.parse_args()

    payload = build()
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if not OUTPUT.is_file():
            print("FAIL: data/site.json is missing; run tools/build_catalog.py")
            return 1
        current = OUTPUT.read_text(encoding="utf-8")
        if current != text:
            print("FAIL: data/site.json is out of date; run tools/build_catalog.py")
            return 1
        print("PASS: data/site.json matches the registered content and catalogue.")
        return 0

    OUTPUT.write_text(text, encoding="utf-8")
    materials = sum(len(subject["groups"]) and sum(len(group["items"]) for group in subject["groups"]) for subject in payload["subjects"])
    print(f"wrote data/site.json — subjects: {len(payload['subjects'])}; downloads: {materials}")
    for subject in payload["subjects"]:
        count = sum(len(group["items"]) for group in subject["groups"])
        tests = subject["test"]["question_count"] if subject.get("test") else 0
        print(f"  {subject['id']}: {count} download(s), {tests} online question(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
