#!/usr/bin/env python3
"""Build subject-sharded, hash-addressed CBT banks from data/tests/<subject>/*.test.json.
50 subjects / 500+ tests need no player/API change; only the chosen subject/index/test
is fetched. No OCR/network/third-party Python dependency is used during builds.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import pathlib
import re
import sys
import struct

ROOT = pathlib.Path(__file__).resolve().parent.parent
SLUG = re.compile(r"[a-z0-9][a-z0-9_.-]{0,95}")

def dump(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n"

def text(value, label, maximum=200):
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise ValueError(f"{label}: non-empty text, at most {maximum} characters required")
    return value.strip()

def number(value, label, low=0, high=100):
    if type(value) not in (int, float) or not math.isfinite(value) or not low <= value <= high:
        raise ValueError(f"{label}: bounded finite number required")
    return value

def image_size(data):
    if data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR" and len(data) >= 24:
        size = struct.unpack(">II", data[16:24])
    elif data[:4] == b"RIFF" and data[8:12] == b"WEBP" and len(data) >= 30:
        kind = data[12:16]
        if kind == b"VP8X": size = (1 + int.from_bytes(data[24:27], "little"), 1 + int.from_bytes(data[27:30], "little"))
        elif kind == b"VP8L" and data[20] == 47:
            bits = int.from_bytes(data[21:25], "little"); size = (1 + (bits & 0x3fff), 1 + ((bits >> 14) & 0x3fff))
        elif kind == b"VP8 " and data[23:26] == b"\x9d\x01\x2a": size = (int.from_bytes(data[26:28], "little") & 0x3fff, int.from_bytes(data[28:30], "little") & 0x3fff)
        else: raise ValueError("Unsupported question WebP header")
    else: raise ValueError("Question image must be a valid PNG/WebP")
    if not all(1 <= v <= 8192 for v in size) or size[0] * size[1] > 16000000: raise ValueError("Question image exceeds phone memory bounds")
    return list(size)

def build(root=ROOT):
    files, subjects, seen = {}, {}, set()
    def hashed(directory, name, value):
        body = dump(value).rstrip("\n")
        digest = hashlib.sha256(body.encode()).hexdigest()[:12]
        file = f"data/quizzes/{directory}/{name}.{digest}.min.json"
        files[file] = body
        return file, digest
    for path in sorted((root / "data/tests").glob("*/*.test.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        subject = path.parent.name
        test = doc.get("id", path.name[:-10])
        if doc.get("schema_version") != 1 or not SLUG.fullmatch(subject) or not isinstance(test, str) or not SLUG.fullmatch(test):
            raise ValueError(f"{path.name}: invalid version / subject / test slug")
        if (subject, test) in seen: raise ValueError("Duplicate subject/test identifier")
        seen.add((subject, test))
        title, subject_title = text(doc.get("title"), "title"), text(doc.get("subject_title", subject.replace("-", " ").title()), "subject_title")
        if subject in subjects and subjects[subject]["title"] != subject_title: raise ValueError("Inconsistent subject titles")
        group = subjects.setdefault(subject, {"id": subject, "title": subject_title, "tests": []})
        minutes = doc.get("duration_minutes", 30)
        if type(minutes) is not int or not 0 <= minutes <= 360: raise ValueError("Invalid duration_minutes")
        kind = doc.get("kind", "quiz")
        if kind not in ("quiz", "paper"): raise ValueError("kind must be quiz or paper")
        source = doc.get("source", {})
        if not isinstance(source, dict): raise ValueError("source must be an object")
        if source.get("pdf"):
            pdf = root / source["pdf"]
            if not str(source["pdf"]).startswith("content/") or not pdf.resolve().is_relative_to((root / "content").resolve()) or not pdf.is_file() or pdf.suffix.lower() != ".pdf": raise ValueError("Invalid source PDF")
            if hashlib.sha256(pdf.read_bytes()).hexdigest() != source.get("sha256"): raise ValueError("Source PDF hash changed; review transcription")
        questions = doc.get("questions")
        if not isinstance(questions, list) or not 1 <= len(questions) <= (300 if kind == "paper" else 2000): raise ValueError("1..2000 questions required (papers: 300)")
        clean = []
        for index, raw in enumerate(questions, 1):
            if not isinstance(raw, dict): raise ValueError("Question must be an object")
            q = {"id": str(index), "text": text(raw.get("text"), f"Q{index}", 12000), "type": raw.get("type", "single")}
            if q["type"] not in ("single", "multiple", "numeric"): raise ValueError("Unknown question type")
            q["marks"] = number(raw.get("marks", doc.get("marks", 1)), "marks", .001)
            q["negative"] = number(raw.get("negative", doc.get("negative_marks", 0)), "negative")
            if q["type"] != "numeric":
                choices = raw.get("options")
                if not isinstance(choices, list) or not 2 <= len(choices) <= 5: raise ValueError("2..5 options required")
                q["options"] = [{"id": "ABCDE"[i], "text": text(option, f"Q{index} option", 4000)} for i, option in enumerate(choices)]
                valid = {o["id"] for o in q["options"]}
                skip = raw.get("skip_option")
                if skip is not None:
                    if q["type"] != "single" or skip not in valid: raise ValueError("Invalid skip option")
                    q["skip_option"] = skip
                answer = raw.get("answer")
                if answer is not None:
                    if not isinstance(answer, list) or not answer or len(set(answer)) != len(answer) or any(a not in valid or a == skip for a in answer): raise ValueError("Invalid answer map")
                    q["answer"] = sorted(answer)
            elif raw.get("answer_range") is not None:
                bounds = raw["answer_range"]
                if not isinstance(bounds, list) or len(bounds) != 2: raise ValueError("numeric answer_range needs [min,max]")
                bounds = [number(v, "numeric range", -1e12, 1e12) for v in bounds]
                if bounds[0] > bounds[1]: raise ValueError("numeric range reversed")
                q["answer_range"] = bounds
            for key in ("explanation", "notice"):
                if raw.get(key): q[key] = text(raw[key], key, 5000)
            if raw.get("source_page") is not None:
                if type(raw["source_page"]) is not int or raw["source_page"] < 1: raise ValueError("Invalid source page")
                q["source_page"] = raw["source_page"]
            if raw.get("image"):
                image = raw["image"]
                if not isinstance(image, str) or not re.fullmatch(r"assets/img/questions/[A-Za-z0-9_.-]+\.[a-f0-9]{12}\.(?:webp|png)", image) or not (root / image).is_file(): raise ValueError("Question image must be a hash-addressed local image")
                if hashlib.sha256((root / image).read_bytes()).hexdigest()[:12] != image.rsplit(".", 2)[1]: raise ValueError("Question image hash mismatch")
                q["image"] = image
                q["image_size"] = image_size((root / image).read_bytes()[:32])
            clean.append(q)
        if sum(q["marks"] for q in clean) > 30000 or sum(q["negative"] for q in clean) > 30000: raise ValueError("Total marking exceeds history bounds")
        bank = {"schema_version": 1, "id": test, "subject_id": subject, "title": title, "subject_title": subject_title,
                "kind": kind, "duration_minutes": minutes, "note": doc.get("note", ""), "source": source, "questions": clean}
        file, digest = hashed(subject, test, bank)
        group["tests"].append({"id": test, "title": title, "question_count": len(clean), "duration_minutes": minutes,
                              "file": file, "fingerprint": digest, "kind": kind})
    # Existing CN engine remains usable; these presets share the same history SDK.
    if (root / "data/banks/cn/manifest.json").is_file():
        group = subjects.setdefault("computer-network", {"id": "computer-network", "title": "Computer Network", "tests": []})
        for count, minutes, label in [(20, 0, "Daily warm-up"), (50, 60, "CN exam sprint"), (100, 120, "Full revision")]:
            if ("computer-network", f"cn-mixed-{count}") in seen: raise ValueError("Reserved CN preset test ID")
            group["tests"].append({"id": f"cn-mixed-{count}", "title": label, "question_count": count, "duration_minutes": minutes,
                "legacy_url": f"subjects/computer-network/test/index.html?mode=full&count={count}&pattern={'exam' if minutes else 'practice'}&minutes={minutes}"})
    manifest = {"schema_version": 1, "test_count": sum(len(s["tests"]) for s in subjects.values()), "subjects": []}
    for subject in sorted(subjects.values(), key=lambda s: s["title"].lower()):
        index, _ = hashed(subject["id"], "index", {"schema_version": 1, **subject})
        manifest["subjects"].append({"id": subject["id"], "title": subject["title"], "test_count": len(subject["tests"]), "file": index})
    files["data/quizzes/manifest.json"] = dump(manifest)
    site_path = root / "data/site.json"
    if site_path.is_file():
        cn = next((s for s in json.loads(site_path.read_text(encoding="utf-8"))["subjects"] if s["id"] == "computer-network"), None)
        if cn:
            files["data/banks/cn/topics.json"] = dump({"id": cn["id"], "topics": [{k: t[k] for k in ("id", "title_en", "title_hi", "question_count", "section_count", "sections")} for t in cn["topics"]]})
    return files

def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--check", action="store_true"); args = parser.parse_args()
    try: files = build()
    except (ValueError, TypeError, KeyError) as error: print(f"FAIL: {error}", file=sys.stderr); return 1
    stale = [name for name, body in files.items() if not (ROOT / name).is_file() or (ROOT / name).read_text(encoding="utf-8") != body]
    obsolete = [p for p in (ROOT / "data/quizzes").rglob("*.json") if p.relative_to(ROOT).as_posix() not in files]
    if args.check:
        if stale or obsolete: print("FAIL: run python3 tools/build_quizzes.py"); return 1
        print(f"PASS: {len(files)} CBT manifest/index/bank files current"); return 0
    for path in obsolete: path.unlink()
    for name, body in files.items():
        path = ROOT / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_text(body, encoding="utf-8")
    print(f"wrote {len(files)} subject-sharded CBT manifest/index/bank files")
    return 0
if __name__ == "__main__": sys.exit(main())
