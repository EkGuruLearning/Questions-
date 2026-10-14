#!/usr/bin/env python3
"""Build the student-facing site data file `data/site.json`.

Inputs (all editable, all checked in):

* `data/catalog/subjects.json`  — subjects, folder labels, topic titles (English + Hindi).
* `data/catalog/materials.json` — every downloadable student file, one row each.
* `data/banks/cn/manifest.json` — generated question-bank manifest and topic chunks
  (produced by `tools/build_site_data.py` from the canonical bank).

Output:

* `data/site.json` — the only data file the website fetches for its pages.

The folder tree shown on the website is the real folder tree on disk:
`content/<subject>/<folder>/<subfolder>/file.pdf` becomes
subject → folder → subfolder → file. Folder labels come from `folders` in
`subjects.json`, so nothing on the site is hand-written twice.

Wiring rules enforced here (the build fails instead of shipping a wrong page):

1. Every file under `content/` must be registered in `materials.json`.
2. Every registered file must exist, live under `content/<subject>/<folder>/`,
   and match its declared subject.
3. Every folder that contains published files needs a label in `subjects.json`,
   and every configured label must point at a folder that really has files.
4. Every registered topic must exist in the bank manifest and match its topic name.
   Pictures must also carry alt text (`alt_en`, `alt_hi`) and a description, which
   is what a search engine reads and what the page shows under the map.
   Every picture must have an up-to-date preview from `tools/build_thumbs.py`, so a
   folder of 3 MB maps still opens instantly on a phone.
5. Counts, byte sizes and SHA-256 values come from the real files, never hand-typed.

Run:

    python3 tools/build_catalog.py            # write data/site.json
    python3 tools/build_catalog.py --check    # fail if data/site.json is out of date
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
import urllib.parse
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "data/catalog"
CONTENT = ROOT / "content"
BANK_MANIFEST = ROOT / "data/banks/cn/manifest.json"
THUMB_MANIFEST = ROOT / "data/thumbs/manifest.json"
OUTPUT = ROOT / "data/site.json"

CONTENT_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".webp", ".svg"}


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


def content_files(subject_dir: pathlib.Path) -> set[str]:
    return {
        path.relative_to(ROOT).as_posix()
        for path in subject_dir.rglob("*")
        if path.is_file() and not path.name.startswith(".") and path.suffix.lower() in CONTENT_SUFFIXES
    }


def folder_of(relative: str, subject_id: str) -> str:
    """`content/<subject>/a/b/file.pdf` -> `a/b`."""
    parts = pathlib.PurePosixPath(relative).parts
    return "/".join(parts[2:-1])


def all_folders(relative_paths, subject_id: str) -> set[str]:
    """Every folder under content/<subject>/ that holds a file, plus its parents."""
    prefix = ("content", subject_id)
    folders: set[str] = set()
    for relative in relative_paths:
        parts = pathlib.PurePosixPath(relative).parts
        if parts[:2] != prefix:
            continue
        relative_folder = parts[2:-1]  # drop "content/<subject>/" and the file name
        for depth in range(1, len(relative_folder) + 1):
            folders.add("/".join(relative_folder[:depth]))
    return folders


def section_label(title: str) -> str:
    """Short, readable section name for buttons and chips."""
    import re

    text = re.sub(r"^section\s+[a-z0-9]+\s*[-–—:]\s*", "", (title or "").strip(), flags=re.IGNORECASE)
    part = text.split(" (", 1)[0].split(" — ", 1)[0].strip(" -–—")
    return part or text


def load_thumbs() -> dict:
    """Previews built by tools/build_thumbs.py, keyed by repo path of the picture."""
    if not THUMB_MANIFEST.is_file():
        raise SystemExit("FAIL: data/thumbs/manifest.json missing — run tools/build_thumbs.py first")
    manifest = read_json(THUMB_MANIFEST)
    return manifest.get("thumbs", {})


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
        total_sections += len(seen)
        total_questions += len(records)
        topics[topic_id] = {
            "id": topic_id,
            "title_en": chunk["topic_name"],
            "question_count": len(records),
            "sections": list(seen.values()),
        }
    manifest["_topics"] = topics
    manifest["_question_total"] = total_questions
    manifest["_section_total"] = total_sections
    return manifest


def build_files(subject: dict, registered: list[dict], thumbs: dict) -> list[dict]:
    """Turn material rows into publishable file records with real sizes and hashes."""
    subject_id = subject["id"]
    topic_ids = {topic["id"] for topic in subject["topics"]}
    items: list[dict] = []
    for raw in registered:
        rel = raw["file"]
        path = ROOT / rel
        folder = folder_of(rel, subject_id)
        if not folder:
            raise SystemExit(f"FAIL: {rel} must live in a folder, e.g. content/{subject_id}/theory/{path.name}")
        if raw.get("topic") is not None and raw["topic"] not in topic_ids:
            raise SystemExit(f"FAIL: {rel} has unknown topic {raw['topic']!r} for subject {subject_id}")
        size = path.stat().st_size
        thumb = None
        if path.suffix.lower().lstrip(".") in {"png", "jpg", "jpeg", "webp"}:
            entry = thumbs.get(rel)
            if entry is None:
                raise SystemExit(
                    f"FAIL: {rel} has no site preview — run python3 tools/build_thumbs.py "
                    "(and commit the generated file under data/thumbs/)"
                )
            thumb_file = ROOT / entry["thumb"]
            if not thumb_file.is_file():
                raise SystemExit(
                    f"FAIL: the preview listed for {rel} is missing on disk: {entry['thumb']} "
                    "— run python3 tools/build_thumbs.py"
                )
            thumb = {
                "url": url_for(entry["thumb"]),
                "bytes": thumb_file.stat().st_size,
            }
        is_picture = path.suffix.lower().lstrip(".") in {"png", "jpg", "jpeg", "webp", "svg"}
        if is_picture:
            for field in ("alt_en", "alt_hi", "description_en", "description_hi"):
                if not (raw.get(field) or "").strip():
                    raise SystemExit(
                        f"FAIL: {rel} is a picture, so data/catalog/materials.json needs a "
                        f"non-empty '{field}' (SEO alt text / description)"
                    )
        items.append({
            "id": rel.split("/", 1)[1].replace("/", "-").rsplit(".", 1)[0],
            "subject": subject_id,
            "folder": folder,
            "topic_id": raw.get("topic"),
            "order": raw.get("order", 0),
            "title_en": raw["title_en"],
            "title_hi": raw["title_hi"],
            "note_en": raw.get("note_en", ""),
            "note_hi": raw.get("note_hi", ""),
            "alt_en": raw.get("alt_en", ""),
            "alt_hi": raw.get("alt_hi", ""),
            "description_en": raw.get("description_en", ""),
            "description_hi": raw.get("description_hi", ""),
            "repo_path": rel,
            "url": url_for(rel),
            "file_name": path.name,
            "file_type": path.suffix.lstrip(".").upper(),
            "bytes": size,
            "size_label": human_size(size),
            "sha256": sha256(path),
            "thumb_url": thumb["url"] if thumb else None,
            "thumb_bytes": thumb["bytes"] if thumb else None,
        })
    return sorted(items, key=lambda item: (item["folder"], item["order"], item["file_name"]))


def build_tree(subject: dict, items: list[dict]) -> dict:
    """Nested folder tree that mirrors content/<subject>/ exactly."""
    labels = subject.get("folders") or {}
    root = {"path": "", "folders": [], "files": []}
    nodes: dict[str, dict] = {"": root}

    def node_for(folder: str) -> dict:
        if folder in nodes:
            return nodes[folder]
        parent_path, _, name = folder.rpartition("/")
        parent = node_for(parent_path)
        node = {"path": folder, "name": name, "folders": [], "files": []}
        parent["folders"].append(node)
        nodes[folder] = node
        return node

    for item in items:
        node_for(item["folder"])["files"].append(item)

    def decorate(node: dict) -> dict:
        key = node["path"]
        if key:
            label = labels.get(key)
            if label is None:
                raise SystemExit(
                    "FAIL: folder has no label — add it to data/catalog/subjects.json under "
                    f"subjects[{subject['id']}].folders[{key!r}]"
                )
        else:  # the subject root: it is the subject card itself, not a folder row
            label = {
                "title_en": subject["title_en"],
                "title_hi": subject["title_hi"],
                "note_en": subject["intro_en"],
                "note_hi": subject["intro_hi"],
                "icon": "📁",
                "order": 0,
            }
        node["folders"].sort(key=lambda child: (labels.get(child["path"], {}).get("order", 99), child["path"]))
        node["files"].sort(key=lambda item: (item["order"], item["file_name"]))
        for child in node["folders"]:
            decorate(child)
        files = list(node["files"])
        for child in node["folders"]:
            files.extend(child["_all_files"])
        node["title_en"] = label["title_en"]
        node["title_hi"] = label["title_hi"]
        node["note_en"] = label.get("note_en", "")
        node["note_hi"] = label.get("note_hi", "")
        node["icon"] = label.get("icon", "📁")
        node["order"] = label.get("order", 99)
        node["folder_count"] = len(node["folders"])
        node["file_count"] = len(files)
        node["total_bytes"] = sum(item["bytes"] for item in files)
        node["file_types"] = sorted({item["file_type"] for item in files})
        node["topics"] = sorted({item["topic_id"] for item in files if item["topic_id"]})
        node["_all_files"] = files
        return node

    decorate(root)
    for key in sorted(labels):
        if key and key not in nodes:
            raise SystemExit(
                f"FAIL: subjects[{subject['id']}].folders[{key!r}] points at a folder that has no published file"
            )

    def clean(node: dict) -> dict:
        node.pop("_all_files", None)
        node["folders"] = [clean(child) for child in node["folders"]]
        return node

    return clean(root)


def build() -> dict:
    subjects_doc = read_json(CATALOG / "subjects.json")
    materials_doc = read_json(CATALOG / "materials.json")
    bank = load_bank()
    thumbs = load_thumbs()

    registered = materials_doc.get("materials", [])
    paths = [item["file"] for item in registered]
    duplicates = {path for path in paths if paths.count(path) > 1}
    if duplicates:
        raise SystemExit(f"FAIL: file registered more than once in materials.json: {sorted(duplicates)}")

    subject_ids = [subject["id"] for subject in subjects_doc["subjects"]]
    for item in registered:
        if item["subject"] not in subject_ids:
            raise SystemExit(f"FAIL: unknown subject {item['subject']!r} for {item['file']}")

    for subject in subjects_doc["subjects"]:
        subject_id = subject["id"]
        own = [item for item in registered if item["subject"] == subject_id]
        own_paths = {item["file"] for item in own}
        on_disk = content_files(CONTENT / subject_id)
        if on_disk - own_paths:
            raise SystemExit(
                f"FAIL: these {subject_id} files are not registered in data/catalog/materials.json:\n  - "
                + "\n  - ".join(sorted(on_disk - own_paths))
            )
        if own_paths - on_disk:
            raise SystemExit(
                f"FAIL: these registered {subject_id} files do not exist:\n  - "
                + "\n  - ".join(sorted(own_paths - on_disk))
            )
        for item in own:
            if folder_of(item["file"], subject_id).split("/")[0] not in (subject.get("folders") or {}):
                raise SystemExit(
                    f"FAIL: {item['file']} sits in an unknown folder — declare it in "
                    f"subjects[{subject_id}].folders"
                )
        unregistered_folders = sorted(all_folders(own_paths, subject_id) - set(subject.get("folders") or {}))
        if unregistered_folders:
            raise SystemExit(
                f"FAIL: these {subject_id} folders have no label in data/catalog/subjects.json:\n  - "
                + "\n  - ".join(unregistered_folders)
            )

    extra_dirs = sorted(
        path.name for path in CONTENT.iterdir() if path.is_dir() and path.name not in subject_ids
    )
    if extra_dirs:
        raise SystemExit(f"FAIL: content/ has folders without a subject entry in subjects.json: {extra_dirs}")

    subjects = []
    for subject in subjects_doc["subjects"]:
        subject_id = subject["id"]
        own = [item for item in registered if item["subject"] == subject_id]
        files = build_files(subject, own, thumbs)
        tree = build_tree(subject, files)
        slug = subject["slug"]
        entry = {
            "id": subject_id,
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
            "file_count": len(files),
            "total_bytes": sum(item["bytes"] for item in files),
            "folder_count": tree["folder_count"],
            "tree": tree,
            "files": files,
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
                        folder: sorted(
                            [
                                item for item in files
                                if item["folder"] == folder and item["topic_id"] == topic_id
                            ],
                            key=lambda item: item["order"],
                        )
                        for folder in ("theory", "practice", "answers", "tests", "reference")
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
        if OUTPUT.read_text(encoding="utf-8") != text:
            print("FAIL: data/site.json is out of date; run tools/build_catalog.py")
            return 1
        print("PASS: data/site.json matches the registered content and catalogue.")
        return 0

    OUTPUT.write_text(text, encoding="utf-8")
    print(f"wrote data/site.json — subjects: {len(payload['subjects'])}")
    for subject in payload["subjects"]:
        folders = ", ".join(
            f"{folder['path'] or '.'}({folder['file_count']})" for folder in subject["tree"]["folders"]
        ) or "—"
        tests = subject["test"]["question_count"] if subject.get("test") else 0
        print(f"  {subject['id']}: {subject['file_count']} file(s) in [{folders}]; {tests} online question(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
