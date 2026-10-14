#!/usr/bin/env python3
"""Build the browser question chunks for the online test page.

Canonical input : `data/banks/cn/cn_questions.json` (schema v2, one record per question)
Generated output: `data/banks/cn/manifest.json` + `data/banks/cn/T0N.<hash>.min.json`

The test page fetches the manifest first and then only the topic chunk(s) it needs,
so a topic-wise test never downloads the whole bank.

Records that are still `pending_review` or `disputed` stay in the canonical bank and in
the counts, but are never shipped inside a test chunk.

Run:
    python3 tools/build_site_data.py            # write manifest + chunks
    python3 tools/build_site_data.py --check    # fail if the checked-in files are stale
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "data/banks/cn/cn_questions.json"
BANK_DIR = ROOT / "data/banks/cn"
EVIDENCE_PATH = ROOT / "data/sources/official_paper_key_evidence.json"

STATUS_VALUES = (
    "paper_and_key_checked",
    "answer_checked",
    "claimed_answer_unverified",
    "disputed",
    "pending_review",
)
SOURCE_VALUES = (
    "verified_official_pyq",
    "claimed_pyq_unverified",
    "repository_internal",
    "textbook_paraphrase",
    "original_practice",
)
QUESTION_STYLES = ("concept", "scenario", "statement", "numerical", "match")
LETTERS = "ABCD"


def read_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_id(reference: str) -> str:
    return "src-" + sha256_bytes(reference.encode("utf-8"))[:12]


def compact_bytes(payload: Any) -> bytes:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def write_json(path: pathlib.Path, payload: Any, *, compact: bool = False) -> bytes:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = compact_bytes(payload) if compact else (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    path.write_bytes(data)
    return data


def counter_dict(counter: collections.Counter, ordered_keys=None):
    if ordered_keys is None:
        return dict(sorted(counter.items()))
    return {key: counter.get(key, 0) for key in ordered_keys}


def validate_evidence(evidence: dict, questions: list[dict]) -> set[str]:
    ids = {q["id"] for q in questions}
    accepted: set[str] = set()
    for record in evidence.get("records", []):
        paper = record.get("official_paper") or {}
        final_key = record.get("official_final_key") or {}
        qids = record.get("question_ids") or []
        if not (paper.get("url") or paper.get("file")):
            raise ValueError("official evidence record has no paper URL/file")
        if not (final_key.get("url") or final_key.get("file")):
            raise ValueError("official evidence record has no final-key URL/file")
        if not qids or any(qid not in ids for qid in qids):
            raise ValueError("official evidence record must map to known stable question IDs")
        if not record.get("reviewed_at") or not record.get("reviewer"):
            raise ValueError("official evidence record needs reviewer and reviewed_at")
        accepted.update(qids)
    return accepted


def validate_canonical(bank: dict, evidence_ids: set[str]) -> list[dict]:
    if bank.get("schema_version") != 2:
        raise ValueError("canonical CN bank must be schema_version 2")
    questions = bank.get("questions")
    if not isinstance(questions, list) or not questions:
        raise ValueError("canonical `questions` must be a non-empty array")
    required = (
        "id", "subject_id", "topic_id", "subtopic", "stem_en", "stem_hi",
        "options_en", "options_hi", "option_ids", "correct_option", "answer_option_id",
        "question_type", "question_style", "difficulty", "difficulty_basis",
        "source_type", "source_url_or_file", "source_id", "verification_status",
        "exam_tags", "exam_tag_basis", "explanation_en", "explanation_hi",
        "nukte_en", "nukte_hi",
    )
    seen: set[str] = set()
    topics: dict[str, str] = {}
    for index, q in enumerate(questions):
        prefix = f"questions[{index}]"
        missing = [key for key in required if key not in q]
        if missing:
            raise ValueError(f"{prefix} missing fields: {', '.join(missing)}")
        qid = q["id"]
        if not isinstance(qid, str) or not qid.strip() or qid in seen:
            raise ValueError(f"{prefix}: empty or duplicate stable question ID {qid!r}")
        seen.add(qid)
        if q["subject_id"] != "cn":
            raise ValueError(f"{qid}: current canonical file must refer to subject_id `cn`")
        if not q["topic_id"] or not q["topic"]:
            raise ValueError(f"{qid}: missing topic id/name")
        topics[q["topic_id"]] = q["topic"]
        if not isinstance(q["stem_en"], str) or not q["stem_en"].strip():
            raise ValueError(f"{qid}: empty English stem")
        if q["question_type"] != "single_select_mcq":
            raise ValueError(f"{qid}: unsupported question type {q['question_type']!r}")
        if q["question_style"] not in QUESTION_STYLES:
            raise ValueError(f"{qid}: unsupported question style {q['question_style']!r}")
        if q["difficulty"] not in ("easy", "medium", "hard"):
            raise ValueError(f"{qid}: invalid difficulty estimate")
        if not isinstance(q["options_en"], list) or len(q["options_en"]) != 4:
            raise ValueError(f"{qid}: single-select MCQ needs exactly four English choices")
        if not isinstance(q["options_hi"], list) or len(q["options_hi"]) != 4:
            raise ValueError(f"{qid}: Hindi option array must align to the four stable option IDs")
        if q["option_ids"] != list(LETTERS) or q["correct_option"] not in LETTERS:
            raise ValueError(f"{qid}: invalid stable option IDs or correct_option")
        if q["answer_option_id"] != q["correct_option"]:
            raise ValueError(f"{qid}: answer_option_id does not match the canonical option key")
        if any(not isinstance(option, str) or not option.strip() for option in q["options_en"]):
            if q["verification_status"] != "pending_review":
                raise ValueError(f"{qid}: blank English option must be marked pending_review")
        if q["source_type"] not in SOURCE_VALUES:
            raise ValueError(f"{qid}: missing or unsupported source_type")
        if q["verification_status"] not in STATUS_VALUES:
            raise ValueError(f"{qid}: missing or unsupported verification_status")
        if not isinstance(q["source_url_or_file"], str) or not q["source_url_or_file"].strip():
            raise ValueError(f"{qid}: no source reference")
        if q["source_id"] != source_id(q["source_url_or_file"]):
            raise ValueError(f"{qid}: source_id is stale for the source reference")
        if not isinstance(q["exam_tags"], list):
            raise ValueError(f"{qid}: exam_tags must be an array")
        official = q["verification_status"] == "paper_and_key_checked" or q["source_type"] == "verified_official_pyq"
        if official and qid not in evidence_ids:
            raise ValueError(f"{qid}: official status has no question-level paper + final-key evidence")
    expected = {f"T{i:02d}" for i in range(1, 8)}
    if set(topics) != expected:
        raise ValueError(f"CN topic map mismatch: expected {sorted(expected)}, found {sorted(topics)}")
    return questions


def language_counts(questions: list[dict]) -> dict:
    return {
        "records": len(questions),
        "stem_en": sum(bool(q["stem_en"].strip()) for q in questions),
        "stem_hi": sum(bool((q.get("stem_hi") or "").strip()) for q in questions),
        "options_en_complete": sum(all(x.strip() for x in q["options_en"]) for q in questions),
        "options_hi_complete": sum(all(x.strip() for x in q["options_hi"]) for q in questions),
        "explanation_en": sum(bool((q.get("explanation_en") or "").strip()) for q in questions),
        "explanation_hi": sum(bool((q.get("explanation_hi") or "").strip()) for q in questions),
        "nukta_en": sum(bool((q.get("nukte_en") or "").strip()) for q in questions),
        "nukta_hi": sum(bool((q.get("nukte_hi") or "").strip()) for q in questions),
        "full_bilingual_records": sum(
            bool((q.get("stem_hi") or "").strip())
            and all(x.strip() for x in q["options_hi"])
            and bool((q.get("explanation_hi") or "").strip())
            and bool((q.get("nukte_hi") or "").strip())
            for q in questions
        ),
    }


def public_question(q: dict) -> dict:
    """Fields the browser needs for a test, without internal review notes."""
    return {
        "id": q["id"],
        "subject_id": q["subject_id"],
        "topic_id": q["topic_id"],
        "topic_name": q["topic"],
        "subtopic": q.get("subtopic") or "",
        "stem_en": q["stem_en"],
        "stem_hi": q.get("stem_hi") or "",
        "options": [
            {"id": option_id, "text_en": en, "text_hi": hi or ""}
            for option_id, en, hi in zip(q["option_ids"], q["options_en"], q["options_hi"])
        ],
        "answer_option_id": q["answer_option_id"],
        "explanation_en": q.get("explanation_en") or "",
        "explanation_hi": q.get("explanation_hi") or "",
        "nukta_en": q.get("nukte_en") or "",
        "nukta_hi": q.get("nukte_hi") or "",
        "question_style": q["question_style"],
        "difficulty": q["difficulty"],
        "source_type": q["source_type"],
        "verification_status": q["verification_status"],
        "exam_tags": q.get("exam_tags") or [],
    }


def generate() -> tuple[dict, str]:
    """Return (manifest payload, manifest text) plus the chunk files it needs."""
    bank = read_json(SRC)
    canonical_sha = sha256_bytes(SRC.read_bytes())
    build_id = "cn-" + canonical_sha[:16]
    generated_on = str(bank.get("generated") or "unknown")
    evidence_doc = read_json(EVIDENCE_PATH)
    evidence_ids = validate_evidence(evidence_doc, bank.get("questions", []))
    questions = validate_canonical(bank, evidence_ids)

    topics: dict[str, str] = {}
    for q in questions:
        topics.setdefault(q["topic_id"], q["topic"])
    publishable = [q for q in questions if q["verification_status"] not in ("disputed", "pending_review")]
    topic_questions = {
        topic_id: [public_question(q) for q in publishable if q["topic_id"] == topic_id]
        for topic_id in sorted(topics)
    }

    total_by_source = collections.Counter(q["source_type"] for q in questions)
    total_by_verification = collections.Counter(q["verification_status"] for q in questions)
    total_by_style = collections.Counter(q["question_style"] for q in questions)
    total_by_difficulty = collections.Counter(q["difficulty"] for q in questions)
    lang = language_counts(questions)

    # Content-addressed topic chunks stay immutable: a browser holding an older
    # manifest still finds the exact chunk it was generated with.
    chunk_manifest = []
    chunks_all = []
    live_files = {}
    for topic_id in sorted(topic_questions):
        canonical_topic = [q for q in questions if q["topic_id"] == topic_id]
        chunk = topic_questions[topic_id]
        chunk_bytes = compact_bytes(chunk)
        chunk_hash = sha256_bytes(chunk_bytes)
        file_name = f"{topic_id}.{chunk_hash[:12]}.min.json"
        live_files[file_name] = chunk_bytes
        chunks_all.extend(chunk)
        chunk_manifest.append({
            "topic_id": topic_id,
            "topic_name": topics[topic_id],
            "file": f"data/banks/cn/{file_name}",
            "sha256": chunk_hash,
            "bytes": len(chunk_bytes),
            "record_count": len(canonical_topic),
            "published_question_count": len(chunk),
            "review_only_excluded_count": len(canonical_topic) - len(chunk),
        })

    manifest_payload = {
        "schema_version": 1,
        "subject_id": "cn",
        "bank_build_id": build_id,
        "canonical_sha256": canonical_sha,
        "generated_on": generated_on,
        "question_count": len(questions),
        "published_question_count": len(chunks_all),
        "review_only_excluded_count": len(questions) - len(chunks_all),
        "topic_count": len(chunk_manifest),
        "by_source_type": counter_dict(total_by_source, SOURCE_VALUES),
        "by_verification": counter_dict(total_by_verification, STATUS_VALUES),
        "by_question_style": counter_dict(total_by_style),
        "by_provisional_difficulty": counter_dict(total_by_difficulty),
        "language_coverage": lang,
        "topics": chunk_manifest,
    }
    manifest_text = json.dumps(manifest_payload, ensure_ascii=False, indent=2) + "\n"
    generate.chunks = live_files
    return manifest_payload, manifest_text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify the checked-in manifest and chunks")
    args = parser.parse_args()

    manifest_payload, manifest_text = generate()
    chunk_files: dict[str, bytes] = generate.chunks

    if args.check:
        problems = []
        current = (BANK_DIR / "manifest.json")
        if not current.is_file() or current.read_text(encoding="utf-8") != manifest_text:
            problems.append("data/banks/cn/manifest.json is out of date; run tools/build_site_data.py")
        for name, payload in chunk_files.items():
            path = BANK_DIR / name
            if not path.is_file() or path.read_bytes() != payload:
                problems.append(f"topic chunk is out of date: data/banks/cn/{name}")
        stale = [path.name for path in sorted(BANK_DIR.glob("T0*.min.json")) if path.name not in chunk_files]
        if stale:
            problems.append(f"stale topic chunk(s) present: {stale}")
        if problems:
            for problem in problems:
                print("FAIL:", problem)
            return 1
        print("PASS: data/banks/cn manifest and topic chunks match the canonical bank.")
        return 0

    for stale in sorted(BANK_DIR.glob("T0*.min.json")):
        if stale.name not in chunk_files:
            stale.unlink()
            print("removed superseded chunk:", stale.relative_to(ROOT))
    for name, payload in chunk_files.items():
        (BANK_DIR / name).write_bytes(payload)
    write_json(BANK_DIR / "manifest.json", manifest_payload)

    print(f"Canonical: {SRC.relative_to(ROOT)} sha256={manifest_payload['canonical_sha256']}")
    print(f"bank_build_id: {manifest_payload['bank_build_id']} — records: {manifest_payload['question_count']}; "
          f"published: {manifest_payload['published_question_count']}; topics: {manifest_payload['topic_count']}")
    print("by topic:", {item["topic_id"]: item["published_question_count"] for item in manifest_payload["topics"]})
    print("by verification:", manifest_payload["by_verification"])
    print(f"manifest: data/banks/cn/manifest.json ({len(manifest_text)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
