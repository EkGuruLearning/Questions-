#!/usr/bin/env python3
"""Build the student-facing site data file `data/site.json`.

Everything under `content/` is published. The folder tree on the website *is*
the folder tree on disk, so adding material needs no code change:

    content/<subject>/<folder>/<subfolder>/file.pdf
      -> subject card -> folder tile -> subfolder tile -> file row

Inputs:

* `content/**`                    — the student files (PDF / pictures). Source of truth.
* `data/catalog/subjects.json`    — optional niceties: bilingual titles, folder icons,
                                    notes, ordering, which folders exist before files
                                    arrive, and whether a subject has an online test.
* `data/catalog/materials.json`   — optional per-file overrides: nicer bilingual titles,
                                    topic id, order, notes, SEO `alt_*` / `description_*`.
* `data/banks/cn/manifest.json`   — generated question-bank manifest + topic chunks
                                    (tools/build_site_data.py).
* `data/thumbs/manifest.json`     — generated picture previews (tools/build_thumbs.py).

Anything not described in the catalogue gets a sensible label derived from its
own name (`reasoning/tests/` -> "Tests"; `DSSSB-2019-Paper-1.pdf` -> "DSSSB 2019
Paper 1"; `previous-year-papers` -> "Previous Year Papers").

The build fails (instead of shipping a wrong page) when:

1. A file listed in `materials.json` does not exist on disk (typo protection).
2. A folder/`?folder=` route points somewhere that is not a real folder.
3. A folder declared in `subjects.json` does not exist on disk.
4. A picture has no up-to-date preview from `tools/build_thumbs.py`, or — when it
   is described in `materials.json` — no alt text / description for search engines.
5. A topic referenced by a file is not a topic of that subject's question bank.

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
BANKS = ROOT / "data/banks"
THUMB_MANIFEST = ROOT / "data/thumbs/manifest.json"
OUTPUT = ROOT / "data/site.json"

CONTENT_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".webp", ".svg"}
PICTURE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
# Names that must stay in capitals when a filename is turned into a label.
ACRONYMS = {
    "ia", "sci", "dsssb", "ssc", "net", "rssb", "rpsc", "pyq", "cgl", "chsl", "mts",
    "gd", "reet", "si", "upsc", "ibps", "rrb", "bci", "cn", "os", "dbms", "sad",
    "ai", "it", "cbt", "key", "mcq", "pdf", "gk", "gs", "nta", "ugc", "kvs", "nvs",
}


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


def humanize(name: str) -> str:
    """`previous-year-papers` -> "Previous Year Papers"; `DSSSB_2019.pdf` -> "DSSSB 2019"."""
    stem = name.rsplit(".", 1)[0] if "." in name else name
    words = [word for word in re.split(r"[-_\s]+", stem.strip()) if word]
    out = []
    for word in words:
        if word.isdigit():
            out.append(word)
        elif word.lower() in ACRONYMS:
            out.append(word.upper())
        elif word.isupper() and len(word) <= 6:
            out.append(word)
        else:
            out.append(word[:1].upper() + word[1:])
    return " ".join(out)


def topic_in(name: str) -> str | None:
    """`T03-Addressing-...` -> "T03" (so a filename alone can set the topic)."""
    match = re.match(r"^(T\d{2})[-_ ]", name, flags=re.IGNORECASE)
    return match.group(1).upper() if match else None


def published_files(subject_dir: pathlib.Path) -> list[str]:
    return sorted(
        path.relative_to(ROOT).as_posix()
        for path in subject_dir.rglob("*")
        if path.is_file() and not path.name.startswith(".") and path.suffix.lower() in CONTENT_SUFFIXES
    )


def folder_of(relative: str, subject_id: str) -> str:
    """`content/<subject>/a/b/file.pdf` -> `a/b`."""
    return "/".join(pathlib.PurePosixPath(relative).parts[2:-1])


def folders_with_files(relative_paths, subject_id: str) -> set[str]:
    """Every folder under content/<subject>/ that holds a file, plus its parents."""
    prefix = ("content", subject_id)
    folders: set[str] = set()
    for relative in relative_paths:
        parts = pathlib.PurePosixPath(relative).parts
        if parts[:2] != prefix:
            continue
        relative_folder = parts[2:-1]
        for depth in range(1, len(relative_folder) + 1):
            folders.add("/".join(relative_folder[:depth]))
    return folders


def section_label(title: str) -> str:
    """Short, readable section name for buttons and chips."""
    text = re.sub(r"^section\s+[a-z0-9]+\s*[-–—:]\s*", "", (title or "").strip(), flags=re.IGNORECASE)
    part = text.split(" (", 1)[0].split(" — ", 1)[0].strip(" -–—")
    return part or text


def load_thumbs() -> dict:
    if not THUMB_MANIFEST.is_file():
        raise SystemExit("FAIL: data/thumbs/manifest.json missing — run tools/build_thumbs.py first")
    return read_json(THUMB_MANIFEST).get("thumbs", {})


def load_bank() -> dict:
    """Every bank under data/banks/<subject>/manifest.json, with topics and section counts."""
    banks: dict[str, dict] = {}
    for manifest_path in sorted(BANKS.glob("*/manifest.json")):
        subject_id = manifest_path.parent.name
        manifest = read_json(manifest_path)
        topics = {}
        question_total = 0
        section_total = 0
        for chunk in manifest.get("topics", []):
            chunk_path = ROOT / chunk["file"]
            if not chunk_path.is_file():
                raise SystemExit(f"FAIL: bank chunk missing for {subject_id}/{chunk['topic_id']}: {chunk['file']}")
            records = read_json(chunk_path)
            seen: dict[str, dict] = {}
            for record in records:
                title = (record.get("subtopic") or "").strip()
                if not title:
                    continue
                bucket = seen.setdefault(title, {"title": title, "short": section_label(title), "count": 0})
                bucket["count"] += 1
            section_total += len(seen)
            question_total += len(records)
            topics[chunk["topic_id"]] = {
                "id": chunk["topic_id"],
                "title_en": chunk["topic_name"],
                "title_hi": chunk.get("topic_name_hi") or chunk["topic_name"],
                "question_count": len(records),
                "sections": list(seen.values()),
            }
        banks[subject_id] = {
            "build_id": manifest.get("bank_build_id"),
            "manifest_url": manifest_path.relative_to(ROOT).as_posix(),
            "topics": topics,
            "question_total": question_total,
            "section_total": section_total,
        }
    if "cn" not in banks:
        raise SystemExit("FAIL: data/banks/cn/manifest.json missing — run tools/build_site_data.py first")
    return banks


def discover_subjects(subjects_doc: dict) -> list[dict]:
    """One entry per folder under content/: catalogue labels win, names fill the gaps."""
    configured = {item["id"]: item for item in subjects_doc.get("subjects", [])}
    discovered: list[dict] = []
    for directory in sorted(path for path in CONTENT.iterdir() if path.is_dir()):
        subject_id = directory.name
        if subject_id.startswith("."):
            continue
        entry = dict(configured.get(subject_id) or {})
        entry.setdefault("id", subject_id)
        entry.setdefault("slug", subject_id)
        entry.setdefault("title_en", humanize(subject_id))
        entry.setdefault("title_hi", entry["title_en"])
        entry.setdefault("tagline_en", "Folder browse karo — file kholo ya download karo.")
        entry.setdefault("tagline_hi", "फोल्डर खोलें — फ़ाइल देखें या डाउनलोड करें।")
        entry.setdefault("intro_en", "")
        entry.setdefault("intro_hi", "")
        entry["auto"] = subject_id not in configured
        discovered.append(entry)
    for subject_id in configured:
        if not (CONTENT / subject_id).is_dir():
            raise SystemExit(
                f"FAIL: subjects.json describes {subject_id!r} but content/{subject_id}/ does not exist"
            )
    return discovered


def build_file_record(subject: dict, rel: str, raw: dict, thumbs: dict) -> dict:
    """One publishable file: catalogue overrides where present, real data always."""
    path = ROOT / rel
    suffix = path.suffix.lower()
    folder = folder_of(rel, subject["id"])
    if not folder:
        raise SystemExit(f"FAIL: {rel} must live in a folder, e.g. content/{subject['id']}/theory/{path.name}")

    topic_ids = {topic["id"] for topic in subject["topics"]}
    topic = raw.get("topic", topic_in(path.name))
    if topic is not None and (topic_ids or topic):
        if topic_ids and topic not in topic_ids:
            raise SystemExit(f"FAIL: {rel} has topic {topic!r}, which is not a topic of {subject['id']}")
        if not topic_ids and not raw:
            topic = None  # nothing to attach it to yet
    title_en = (raw.get("title_en") or "").strip() or humanize(path.name)
    title_hi = (raw.get("title_hi") or "").strip() or title_en

    size = path.stat().st_size
    thumb = None
    if suffix in PICTURE_SUFFIXES:
        entry = thumbs.get(rel)
        if entry is None or not (ROOT / entry["thumb"]).is_file():
            raise SystemExit(
                f"FAIL: {rel} has no site preview — run python3 tools/build_thumbs.py "
                "(it writes data/thumbs/, which is what the pages load)"
            )
        thumb = {"url": url_for(entry["thumb"]), "bytes": (ROOT / entry["thumb"]).stat().st_size}

    is_picture = suffix in PICTURE_SUFFIXES
    alt_en = (raw.get("alt_en") or "").strip()
    alt_hi = (raw.get("alt_hi") or "").strip()
    description_en = (raw.get("description_en") or "").strip()
    description_hi = (raw.get("description_hi") or "").strip()
    if is_picture:
        if raw:
            for field, value in (
                ("alt_en", alt_en), ("alt_hi", alt_hi),
                ("description_en", description_en), ("description_hi", description_hi),
            ):
                if not value:
                    raise SystemExit(
                        f"FAIL: {rel} is described in materials.json, so it needs a non-empty '{field}' "
                        "(SEO alt text / description)"
                    )
        else:
            alt_en = alt_en or title_en
            alt_hi = alt_hi or title_hi
            description_en = description_en or f"{title_en} — preview dekho ya poori file download karo."
            description_hi = description_hi or f"{title_hi} — प्रीव्यू देखें या पूरी फ़ाइल डाउनलोड करें।"

    return {
        "id": rel.split("/", 1)[1].replace("/", "-").rsplit(".", 1)[0],
        "subject": subject["id"],
        "folder": folder,
        "topic_id": topic,
        "order": raw.get("order", 0),
        "title_en": title_en,
        "title_hi": title_hi,
        "note_en": raw.get("note_en", ""),
        "note_hi": raw.get("note_hi", ""),
        "alt_en": alt_en,
        "alt_hi": alt_hi,
        "description_en": description_en,
        "description_hi": description_hi,
        "curated": bool(raw),
        "repo_path": rel,
        "url": url_for(rel),
        "file_name": path.name,
        "file_type": suffix.lstrip(".").upper(),
        "bytes": size,
        "size_label": human_size(size),
        "sha256": sha256(path),
        "thumb_url": thumb["url"] if thumb else None,
        "thumb_bytes": thumb["bytes"] if thumb else None,
    }


def build_tree(subject: dict, files: list[dict]) -> dict:
    """Nested folder tree that mirrors content/<subject>/ exactly."""
    labels = {key: value for key, value in (subject.get("folders") or {}).items() if key}
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

    for item in files:
        node_for(item["folder"])["files"].append(item)
    for folder in labels:  # declared-but-empty folders still show up on the site
        if folder not in nodes:
            on_disk = CONTENT / subject["id"] / folder
            if not on_disk.is_dir():
                raise SystemExit(
                    f"FAIL: subjects.json declares folder {folder!r} for {subject['id']}, "
                    f"but content/{subject['id']}/{folder}/ does not exist"
                )
            node_for(folder)

    def label_for(node: dict) -> dict:
        key = node["path"]
        if not key:  # subject root: the subject card itself
            return {
                "title_en": subject["title_en"], "title_hi": subject["title_hi"],
                "note_en": subject.get("intro_en", ""), "note_hi": subject.get("intro_hi", ""),
                "icon": "📁", "order": 0,
            }
        configured = labels.get(key)
        if configured:
            return configured
        name = key.rpartition("/")[2]
        return {"title_en": humanize(name), "title_hi": humanize(name), "note_en": "", "note_hi": "",
                "icon": "📁" if not name.isdigit() else "🗓️", "order": 50}

    def decorate(node: dict) -> dict:
        label = label_for(node)
        node["title_en"] = label["title_en"]
        node["title_hi"] = label["title_hi"]
        node["note_en"] = label.get("note_en", "")
        node["note_hi"] = label.get("note_hi", "")
        node["icon"] = label.get("icon", "📁")
        node["order"] = label.get("order", 50)
        node["auto"] = node["path"] not in labels and bool(node["path"])
        node["folders"].sort(key=lambda child: (label_for(child).get("order", 50), child["path"]))
        node["files"].sort(key=lambda item: (item["order"], item["file_name"]))
        for child in node["folders"]:
            decorate(child)
        all_files = list(node["files"])
        for child in node["folders"]:
            all_files.extend(child["_all_files"])
        node["folder_count"] = len(node["folders"])
        node["file_count"] = len(all_files)
        node["total_bytes"] = sum(item["bytes"] for item in all_files)
        node["file_types"] = sorted({item["file_type"] for item in all_files})
        node["topics"] = sorted({item["topic_id"] for item in all_files if item["topic_id"]})
        node["empty"] = not all_files
        node["_all_files"] = all_files
        return node

    decorate(root)
    for key in labels:
        if key not in nodes:
            raise SystemExit(f"FAIL: folder {key!r} was declared but never created in the tree")

    def clean(node: dict) -> dict:
        node.pop("_all_files", None)
        node["folders"] = [clean(child) for child in node["folders"]]
        return node

    return clean(root)


def build() -> dict:
    subjects_doc = read_json(CATALOG / "subjects.json")
    materials_doc = read_json(CATALOG / "materials.json")
    thumbs = load_thumbs()
    banks = load_bank()

    registered = materials_doc.get("materials", [])
    registered_paths = [item["file"] for item in registered]
    duplicates = {path for path in registered_paths if registered_paths.count(path) > 1}
    if duplicates:
        raise SystemExit(f"FAIL: file described more than once in materials.json: {sorted(duplicates)}")
    registered_by_path = {item["file"]: item for item in registered}

    subjects = []
    for subject in discover_subjects(subjects_doc):
        subject_id = subject["id"]
        subject_dir = CONTENT / subject_id
        if not subject_dir.is_dir():
            subject_dir.mkdir(parents=True)
        on_disk = published_files(subject_dir)
        missing = [item for item in registered if item["subject"] == subject_id and item["file"] not in on_disk]
        if missing:
            raise SystemExit(
                f"FAIL: these files are described for {subject_id} but do not exist:\n  - "
                + "\n  - ".join(sorted(item["file"] for item in missing))
            )
        for item in registered:
            if item["file"] in on_disk and item["subject"] != subject_id:
                raise SystemExit(
                    f"FAIL: {item['file']} lives under content/{subject_id}/ but materials.json says "
                    f"subject {item['subject']!r}"
                )

        bank = banks.get(subject.get("test_bank") or subject_id)
        has_test = bool(subject.get("has_test")) and bank is not None
        subject["topics"] = list(subject.get("topics") or [])
        if has_test and not subject["topics"]:
            subject["topics"] = [
                {"id": topic_id, "title_en": topic["title_en"], "title_hi": topic["title_hi"]}
                for topic_id, topic in sorted(bank["topics"].items())
            ]
        if not has_test:
            subject["topics"] = []

        files = [
            build_file_record(subject, rel, registered_by_path.get(rel, {}), thumbs)
            for rel in on_disk
        ]
        files.sort(key=lambda item: (item["folder"], item["order"], item["file_name"]))
        tree = build_tree(subject, files)

        slug = subject["slug"]
        explorer = f"subjects/index.html?subject={slug}"
        dedicated = CONTENT.parent / "subjects" / slug / "index.html"
        route = f"subjects/{slug}/index.html" if dedicated.is_file() else explorer
        entry = {
            "id": subject_id,
            "slug": slug,
            "title_en": subject["title_en"],
            "title_hi": subject["title_hi"],
            "tagline_en": subject["tagline_en"],
            "tagline_hi": subject["tagline_hi"],
            "intro_en": subject.get("intro_en", ""),
            "intro_hi": subject.get("intro_hi", ""),
            "auto": bool(subject.get("auto")),
            "has_material": bool(subject.get("has_material", True)),
            "has_test": has_test,
            "has_maps": bool(subject.get("has_maps")),
            "route": route,
            "explorer_route": explorer,
            "material_route": route if subject.get("has_material", True) else None,
            "test_route": f"subjects/{slug}/test/index.html" if has_test and (CONTENT.parent / "subjects" / slug / "test" / "index.html").is_file() else None,
            "file_count": len(files),
            "total_bytes": sum(item["bytes"] for item in files),
            "folder_count": tree["folder_count"],
            "tree": tree,
            "files": files,
        }

        if subject.get("year_folders"):
            entry["year_folders"] = subject["year_folders"]

        if has_test:
            topics = []
            for topic in subject["topics"]:
                topic_id = topic["id"]
                bank_topic = bank["topics"].get(topic_id)
                if bank_topic is None:
                    raise SystemExit(f"FAIL: topic {topic_id} has no question bank chunk in {subject_id}")
                if topic["title_en"].strip() != bank_topic["title_en"].strip():
                    raise SystemExit(
                        f"FAIL: topic {topic_id} name mismatch — bank has {bank_topic['title_en']!r}, "
                        f"catalogue has {topic['title_en']!r}"
                    )
                topics.append({
                    "id": topic_id,
                    "title_en": topic["title_en"],
                    "title_hi": topic.get("title_hi", bank_topic["title_hi"]),
                    "question_count": bank_topic["question_count"],
                    "section_count": len(bank_topic["sections"]),
                    "sections": bank_topic["sections"],
                    "material": {
                        folder: [item for item in files if item["folder"] == folder and item["topic_id"] == topic_id]
                        for folder in ("theory", "practice", "answers", "tests", "reference")
                    },
                })
            entry["topics"] = topics
            entry["test"] = {
                "build_id": bank["build_id"],
                "manifest_url": bank["manifest_url"],
                "question_count": bank["question_total"],
                "topic_count": len(topics),
                "section_count": bank["section_total"],
            }
        else:
            entry["topics"] = []

        subjects.append(entry)

    return {
        "schema_version": 1,
        "generated_on": date.today().isoformat(),
        "brand": subjects_doc["brand"],
        "bank_build_id": banks["cn"]["build_id"],
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
        print("PASS: data/site.json matches the content folders and the catalogue.")
        return 0

    OUTPUT.write_text(text, encoding="utf-8")
    print(f"wrote data/site.json — subjects: {len(payload['subjects'])}")
    for subject in payload["subjects"]:
        folders = ", ".join(
            f"{folder['title_en']}({folder['file_count']})" for folder in subject["tree"]["folders"]
        ) or "—"
        tests = subject["test"]["question_count"] if subject.get("test") else 0
        tag = "auto" if subject["auto"] else "catalogue"
        print(f"  {subject['id']} [{tag}]: {subject['file_count']} file(s) in [{folders}]; {tests} online question(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
