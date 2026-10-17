#!/usr/bin/env python3
"""Discover uploaded old-paper PDFs and build the small Test Room manifest.

Upload: content/previous-year-papers/<exam>/<year>/Your-Paper.pdf
Optional: data/practice/papers/<exam>/<year>/Your-Paper.paper.json
(see maintainer/AUTH_AND_PRACTICE.md). Metadata stays outside student content/.
No OCR, PDF conversion, npm or database is needed to publish a scanned paper.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
from urllib.parse import urlsplit

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTPUT = pathlib.Path("data/practice/manifest.json")
KEY_NAME = re.compile(r"answer[\s_-]*key|solution|उत्तर|(?:^|[\s_-])key(?:[\s_.-]|$)", re.I)
MAX_QUESTIONS = 300


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def local_pdf(root: pathlib.Path, value: str) -> pathlib.Path:
    if not isinstance(value, str) or "\\" in value or pathlib.PurePosixPath(value).is_absolute():
        raise ValueError("key_pdf must be a repository-relative local PDF")
    path = (root / value).resolve()
    base = (root / "content/previous-year-papers").resolve()
    if not path.is_relative_to(base) or path.suffix.lower() != ".pdf" or not path.is_file():
        raise ValueError("key_pdf must exist inside content/previous-year-papers/")
    return path


def generate(root: pathlib.Path = ROOT) -> dict:
    base = root / "content/previous-year-papers"
    papers = []
    seen_ids = set()
    metadata = {}
    referenced_keys = set()
    metadata_root = root / "data/practice/papers"
    for path in sorted(metadata_root.rglob("*.paper.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict) or doc.get("schema_version") != 1:
            raise ValueError(f"{path.name}: metadata needs schema_version 1")
        relative = path.relative_to(metadata_root)
        pdf = base / relative.parent / (path.name[:-len(".paper.json")] + ".pdf")
        if not pdf.is_file():
            raise ValueError(f"{path.name}: matching paper PDF is missing")
        metadata[pdf] = doc
        if doc.get("key_pdf"):
            referenced_keys.add(local_pdf(root, doc["key_pdf"]))

    for pdf in sorted(base.rglob("*")):
        if not pdf.is_file() or pdf.suffix.lower() != ".pdf" or pdf.name.startswith("."):
            continue
        if KEY_NAME.search(pdf.stem) or pdf.resolve() in referenced_keys:
            continue
        if not pdf.resolve().is_relative_to(base.resolve()):
            raise ValueError("Paper symlinks may not escape the public paper folder")
        doc = metadata.get(pdf, {})
        rel = pdf.relative_to(root).as_posix()
        paper_id = doc.get("id") or "paper-" + hashlib.sha256(rel.encode()).hexdigest()[:16]
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,95}", paper_id) or paper_id in seen_ids:
            raise ValueError(f"{rel}: invalid/duplicate paper id")
        seen_ids.add(paper_id)
        count = doc.get("question_count")
        if count is not None and (type(count) is not int or not 1 <= count <= MAX_QUESTIONS):
            raise ValueError(f"{rel}: question_count must be 1..{MAX_QUESTIONS} or null")
        options = doc.get("options_count", 4)
        if type(options) is not int or not 2 <= options <= 5:
            raise ValueError(f"{rel}: options_count must be 2..5")
        skip = doc.get("skip_option")
        allowed = list("ABCDE"[:options])
        if skip is not None and skip not in allowed:
            raise ValueError(f"{rel}: invalid skip_option")
        minutes = doc.get("duration_minutes", 120)
        if type(minutes) is not int or not 0 <= minutes <= 360:
            raise ValueError(f"{rel}: duration_minutes must be 0..360 (0 = untimed)")
        marks, negative = doc.get("marks", 1), doc.get("negative_marks", 0)
        if (type(marks) not in (int, float) or not 0 < marks <= 100
                or type(negative) not in (int, float) or not 0 <= negative <= 100):
            raise ValueError(f"{rel}: invalid practice marking")
        key = doc.get("answer_key", {})
        if not isinstance(key, dict) or (key and count is None):
            raise ValueError(f"{rel}: answer_key needs an object and an explicit question_count")
        normalized = {}
        for number, value in key.items():
            if not re.fullmatch(r"[1-9]\d{0,2}", number) or int(number) > count:
                raise ValueError(f"{rel}: answer_key question out of range")
            if value == "DROP":
                normalized[number] = "DROP"
                continue
            values = [value] if isinstance(value, str) else value
            if not isinstance(values, list) or not values or len(set(values)) != len(values) or any(
                    option not in allowed or option == skip for option in values):
                raise ValueError(f"{rel}: answer_key must contain A..E options, lists or DROP")
            normalized[number] = sorted(values)
        key_pdf = local_pdf(root, doc["key_pdf"]) if doc.get("key_pdf") else None
        if not key_pdf and pdf.name.endswith("-Questions.pdf"):
            candidate = pdf.with_name(pdf.name.replace("-Questions.pdf", "-Answer-Key.pdf"))
            key_pdf = candidate if candidate.is_file() else None
        if doc.get("key_sha256") and (not key_pdf or sha256(key_pdf) != doc["key_sha256"]):
            raise ValueError(f"{rel}: key_pdf hash changed — review the answer map before publishing")
        paper_hash = sha256(pdf)
        if (doc.get("answer_key") or doc.get("paper_sha256")) and doc.get("paper_sha256") != paper_hash:
            raise ValueError(f"{rel}: a digital key needs the matching paper_sha256 — review before publishing")
        note = doc.get("key_note", "")
        if not isinstance(note, str) or len(note) > 1000:
            raise ValueError(f"{rel}: invalid key_note")
        title = doc.get("title") or re.sub(r"[-_]+", " ", pdf.stem)
        if not isinstance(title, str) or not title.strip() or len(title) > 200:
            raise ValueError(f"{rel}: title must be 1..200 characters")
        title_hi = doc.get("title_hi", "")
        if not isinstance(title_hi, str) or len(title_hi) > 200:
            raise ValueError(f"{rel}: invalid title_hi")
        parts = pdf.relative_to(base).parts
        entry = {
            "id": paper_id, "title": title.strip(), "title_hi": title_hi,
            "exam": parts[0] if len(parts) > 1 else "other",
            "year": next((part for part in parts[:-1] if re.fullmatch(r"(?:19|20)\d{2}", part)), ""),
            "pdf": rel, "bytes": pdf.stat().st_size, "sha256": paper_hash,
            "question_count": count, "options_count": options, "skip_option": skip,
            "duration_minutes": minutes, "marks": marks, "negative_marks": negative,
            "answer_key": normalized, "key_note": note,
            "key_pdf": key_pdf.relative_to(root).as_posix() if key_pdf else None,
            "key_label": "Provided practice key — not independently verified against the official final key" if normalized else "No digital answer key — unscored self-practice",
        }
        reader_only = doc.get("reader_only", False)
        if type(reader_only) is not bool: raise ValueError("reader_only must be boolean")
        entry["reader_only"] = reader_only
        if reader_only and normalized: raise ValueError("reader-only paper cannot have a forced digital key")
        if doc.get("source_url"):
            parsed = urlsplit(doc["source_url"])
            if parsed.scheme != "https" or parsed.netloc != "github.com" or parsed.username or parsed.password: raise ValueError("Invalid pinned source URL")
            entry["source_url"] = doc["source_url"]
        if doc.get("cbt_test") or doc.get("cbt_subject"):
            if reader_only or not re.fullmatch(r"[a-z0-9][a-z0-9_.-]{0,95}", doc.get("cbt_subject", "")) or not re.fullmatch(r"[a-z0-9][a-z0-9_.-]{0,95}", doc.get("cbt_test", "")): raise ValueError("Invalid CBT link")
            authored = root / f"data/tests/{doc['cbt_subject']}/{doc['cbt_test']}.test.json"
            if not authored.is_file() or json.loads(authored.read_text(encoding="utf-8")).get("source", {}).get("pdf") != rel: raise ValueError("CBT link needs a matching authored source PDF")
            entry.update(cbt_subject=doc["cbt_subject"], cbt_test=doc["cbt_test"])
        entry["fingerprint"] = hashlib.sha256(json.dumps(entry, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        papers.append(entry)
    papers.sort(key=lambda p: (p["year"], p["exam"], p["title"]), reverse=True)
    return {"schema_version": 1, "papers": papers}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        text = json.dumps(generate(), ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n"
    except (ValueError, TypeError, KeyError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    output = ROOT / OUTPUT
    if args.check:
        if not output.is_file() or output.read_text(encoding="utf-8") != text:
            print("FAIL: practice manifest is stale; run python3 tools/build_practice.py")
            return 1
        print("PASS: Test Room manifest matches every uploaded old-paper PDF and key.")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
        print(f"wrote {OUTPUT} — {len(json.loads(text)['papers'])} paper(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
