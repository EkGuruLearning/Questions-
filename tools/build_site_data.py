#!/usr/bin/env python3
"""Build deterministic, provenance-aware public CN data and subject catalog.

Canonical input: Computer Network/data/cn_questions.json
Public outputs: assets/catalog.min.json, assets/banks/cn/manifest.json,
                content-hashed topic chunks, assets/source-register.min.json,
                and the generated compatibility asset assets/cn-questions.min.json.
The portal fetches the catalog first and only fetches the selected topic chunk(s).
"""
from __future__ import annotations

import collections
import hashlib
import json
import pathlib
import re
import urllib.parse
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "Computer Network/data/cn_questions.json"
SUBJECTS_PATH = ROOT / "data/catalog/subjects.json"
EXAMS_PATH = ROOT / "data/catalog/exams.json"
MAPPINGS_PATH = ROOT / "data/catalog/syllabus_mappings.json"
BOOKS_PATH = ROOT / "data/catalog/books.json"
EVIDENCE_PATH = ROOT / "data/sources/official_paper_key_evidence.json"
ASSETS = ROOT / "assets"
BANK_DIR = ASSETS / "banks/cn"
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
        raise ValueError("canonical CN bank must be migrated to schema_version 2")
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
    exam_name_status = "none"
    if q.get("exam_name"):
        if q["verification_status"] == "paper_and_key_checked":
            exam_name_status = "official_evidence"
        elif q["source_type"] == "claimed_pyq_unverified":
            exam_name_status = "source_claim_unverified"
        else:
            exam_name_status = "source_label_unverified"
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
        "question_type": q["question_type"],
        "question_style": q["question_style"],
        "difficulty": q["difficulty"],
        "difficulty_basis": q["difficulty_basis"],
        "source_type": q["source_type"],
        "verification_status": q["verification_status"],
        "source_id": q["source_id"],
        "exam_name": q.get("exam_name") if exam_name_status != "none" else None,
        "exam_year": q.get("exam_year") if exam_name_status != "none" else None,
        "paper_or_shift": q.get("paper_or_shift") if exam_name_status != "none" else None,
        "exam_name_status": exam_name_status,
        "exam_tags": q.get("exam_tags") or [],
        "exam_tag_basis": q.get("exam_tag_basis") or "suggested_practice_fit",
        "official_evidence_id": q["id"] if q["verification_status"] == "paper_and_key_checked" else None,
    }


def safe_source_links(reference: str) -> list[dict]:
    links = []
    seen = set()
    for raw in re.findall(r"https?://[^\s)]+", reference, flags=re.I):
        parsed = urllib.parse.urlparse(raw.rstrip(".,;"))
        if parsed.scheme in ("http", "https") and parsed.netloc and not parsed.username:
            href = raw.rstrip(".,;")
            if href not in seen:
                links.append({"label": parsed.netloc, "href": href, "external": True})
                seen.add(href)
    candidates = []
    if reference.startswith("Computer Network/"):
        candidates.extend(re.findall(r"Computer Network/[^;()]+?\.(?:pdf|md|html|csv)", reference, flags=re.I))
    for match in re.findall(r"([^;|\n]+?\.(?:pdf|md|html|csv))", reference, flags=re.I):
        value = match.strip().strip(" `\"'")
        value = re.sub(r"^(?:Repo:\s*)", "", value, flags=re.I)
        candidates.append(value)
    for candidate in candidates:
        candidate = candidate.strip().strip(" `\"'")
        if candidate.startswith("Computer Network/"):
            path = (ROOT / candidate).resolve()
        else:
            path = (ROOT / "Computer Network" / candidate).resolve()
        try:
            path.relative_to(ROOT.resolve())
        except ValueError:
            continue
        if path.is_file():
            href = urllib.parse.quote(path.relative_to(ROOT).as_posix(), safe="/")
            if href not in seen:
                links.append({"label": path.name, "href": href, "external": False})
                seen.add(href)
    return links


def main() -> None:
    bank = read_json(SRC)
    canonical_bytes = SRC.read_bytes()
    canonical_sha = sha256_bytes(canonical_bytes)
    build_id = "cn-" + canonical_sha[:16]
    generated_on = str(bank.get("generated") or "unknown")
    subjects_doc = read_json(SUBJECTS_PATH)
    exams_doc = read_json(EXAMS_PATH)
    mappings_doc = read_json(MAPPINGS_PATH)
    books_doc = read_json(BOOKS_PATH)
    evidence_doc = read_json(EVIDENCE_PATH)
    evidence_ids = validate_evidence(evidence_doc, bank.get("questions", []))
    questions = validate_canonical(bank, evidence_ids)

    topics = {}
    for q in questions:
        topics.setdefault(q["topic_id"], q["topic"])
    # Disputed and pending records remain in the canonical bank and report counts,
    # but incomplete/review-only items are not shipped in public test chunks.
    publishable_questions = [q for q in questions if q["verification_status"] not in ("disputed", "pending_review")]
    topic_questions = {
        topic_id: [public_question(q) for q in publishable_questions if q["topic_id"] == topic_id]
        for topic_id in sorted(topics)
    }
    total_by_source = collections.Counter(q["source_type"] for q in questions)
    total_by_verification = collections.Counter(q["verification_status"] for q in questions)
    total_by_style = collections.Counter(q["question_style"] for q in questions)
    total_by_difficulty = collections.Counter(q["difficulty"] for q in questions)
    lang = language_counts(questions)

    # Public citation register: safe per-source reference text and links only.
    source_map: dict[str, dict] = {}
    for q in questions:
        sid = q["source_id"]
        item = source_map.setdefault(sid, {
            "id": sid,
            "reference": q["source_url_or_file"],
            "source_types": collections.Counter(),
            "verification_statuses": collections.Counter(),
            "question_count": 0,
            "official_evidence_question_count": 0,
            "links": safe_source_links(q["source_url_or_file"]),
            "audit_note": q.get("provenance_note") or None,
        })
        if item["reference"] != q["source_url_or_file"]:
            raise ValueError(f"source_id collision with different references: {sid}")
        item["source_types"][q["source_type"]] += 1
        item["verification_statuses"][q["verification_status"]] += 1
        item["question_count"] += 1
        if q["verification_status"] == "paper_and_key_checked":
            item["official_evidence_question_count"] += 1
    public_sources = []
    for sid in sorted(source_map):
        item = source_map[sid]
        item["source_types"] = counter_dict(item["source_types"], SOURCE_VALUES)
        item["verification_statuses"] = counter_dict(item["verification_statuses"], STATUS_VALUES)
        public_sources.append(item)
    source_payload = {
        "schema_version": 1,
        "bank_build_id": build_id,
        "canonical_sha256": canonical_sha,
        "generated_on": generated_on,
        "source_count": len(public_sources),
        "records": public_sources,
    }
    source_bytes = write_json(ASSETS / "source-register.min.json", source_payload, compact=True)

    # Content-addressed topic chunks remain immutable. A stale catalog cached by a
    # browser therefore still points to chunks that were generated with it.
    chunk_manifest = []
    chunks_all = []
    for topic_id in sorted(topic_questions):
        canonical_topic = [q for q in questions if q["topic_id"] == topic_id]
        chunk = topic_questions[topic_id]
        chunk_bytes = compact_bytes(chunk)
        chunk_hash = sha256_bytes(chunk_bytes)
        file_name = f"{topic_id}.{chunk_hash[:12]}.min.json"
        file_path = BANK_DIR / file_name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if file_path.exists() and file_path.read_bytes() != chunk_bytes:
            raise ValueError(f"hash-named chunk collision: {file_path}")
        if not file_path.exists():
            file_path.write_bytes(chunk_bytes)
        chunks_all.extend(chunk)
        chunk_manifest.append({
            "topic_id": topic_id,
            "topic_name": topics[topic_id],
            "file": "assets/banks/cn/" + file_name,
            "sha256": chunk_hash,
            "bytes": len(chunk_bytes),
            "record_count": len(canonical_topic),
            "published_question_count": len(chunk),
            "review_only_excluded_count": len(canonical_topic) - len(chunk),
            "by_source_type": counter_dict(collections.Counter(q["source_type"] for q in canonical_topic), SOURCE_VALUES),
            "by_verification": counter_dict(collections.Counter(q["verification_status"] for q in canonical_topic), STATUS_VALUES),
            "by_style": counter_dict(collections.Counter(q["question_style"] for q in canonical_topic)),
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
    manifest_bytes = write_json(BANK_DIR / "manifest.json", manifest_payload)

    # Compatibility export for older consumers; review-only records are omitted,
    # and the new root page fetches topic chunks rather than this monolithic asset.
    compatibility_bytes = write_json(ASSETS / "cn-questions.min.json", chunks_all, compact=True)

    # Verify book links and expose only files that exist in this repository.
    books_by_id = {item["id"]: item for item in books_doc.get("books", [])}
    for book in books_doc.get("books", []):
        path = pathlib.Path(book["file"])
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"unsafe book path: {book['file']}")
        full_path = (ROOT / path).resolve()
        try:
            full_path.relative_to(ROOT.resolve())
        except ValueError as exc:
            raise ValueError(f"book escapes repository root: {book['file']}") from exc
        if not full_path.is_file():
            raise FileNotFoundError(f"catalog book missing: {book['file']}")
        book["href"] = urllib.parse.quote(path.as_posix(), safe="/")
        book["sha256"] = sha256_bytes(full_path.read_bytes())
        book["bytes"] = full_path.stat().st_size
        # PDF resources open separately with safe rel attributes; interactive CBT
        # launchers remain in the same tab by default as required by site navigation.
        book["opens_in_new_tab"] = book["kind"] in ("theory_mcq_pdf", "practice_pdf")
        book["download_available"] = book["kind"] in ("theory_mcq_pdf", "practice_pdf")
    for subject in subjects_doc.get("subjects", []):
        missing_books = set(subject.get("book_ids", [])) - books_by_id.keys()
        if missing_books:
            raise ValueError(f"subject {subject['id']} refers to missing books: {sorted(missing_books)}")

    # The CN bank is the only published subject. Planned subjects stay visible,
    # carry zero published records, and have no startable bank URL.
    subject_entries = []
    for subject in subjects_doc.get("subjects", []):
        status = subject.get("status")
        if status not in ("planned", "collecting", "ingested", "review", "verified", "live"):
            raise ValueError(f"subject {subject.get('id')}: invalid publication status {status!r}")
        entry = dict(subject)
        entry["available"] = status == "live"
        entry["question_count"] = 0
        entry["topic_count"] = 0
        entry["topics"] = []
        entry["verification_summary"] = counter_dict(collections.Counter(), STATUS_VALUES)
        entry["source_type_summary"] = counter_dict(collections.Counter(), SOURCE_VALUES)
        entry["language_coverage"] = None
        entry["bank_manifest_url"] = None
        if subject["id"] == "cn":
            if status != "live":
                raise ValueError("CN is the canonical live subject; catalog status must be `live`")
            entry["question_count"] = len(questions)
            entry["topic_count"] = len(chunk_manifest)
            entry["topics"] = [{
                "id": item["topic_id"],
                "name": item["topic_name"],
                "question_count": item["record_count"],
                "practice_question_count": item["published_question_count"],
                "chunk_url": item["file"],
            } for item in chunk_manifest]
            entry["verification_summary"] = manifest_payload["by_verification"]
            entry["source_type_summary"] = manifest_payload["by_source_type"]
            entry["language_coverage"] = lang
            entry["bank_manifest_url"] = "assets/banks/cn/manifest.json"
        elif status == "live":
            raise ValueError(f"subject {subject['id']} marked live without a configured bank")
        entry["books"] = [books_by_id[book_id] for book_id in subject.get("book_ids", [])]
        subject_entries.append(entry)

    exam_profiles = exams_doc.get("profiles", [])
    exam_ids = {profile["id"] for profile in exam_profiles}
    tag_map = {profile["id"]: profile.get("exam_tag") for profile in exam_profiles}
    for profile in exam_profiles:
        if profile.get("simulation_level") == "exact_simulation":
            raise ValueError(f"exact simulation not permitted without a current verified blueprint: {profile['id']}")
        if profile.get("status") == "live" and profile.get("simulation_level") == "exact_simulation":
            raise ValueError(f"exact profile must not be live without a release-gate audit: {profile['id']}")
    for mapping in mappings_doc.get("mappings", []):
        if mapping.get("exam_profile_id") not in exam_ids:
            raise ValueError(f"mapping references unknown exam: {mapping.get('exam_profile_id')}")
        if mapping.get("subject_id") not in {x["id"] for x in subject_entries}:
            raise ValueError(f"mapping references unknown subject: {mapping.get('subject_id')}")
        if any(topic not in topics for topic in mapping.get("topic_ids", [])) and mapping.get("subject_id") == "cn":
            raise ValueError(f"mapping references unknown CN topic: {mapping.get('exam_profile_id')}")

    # Counts per exam tag are surfaced as available pool guidance only. The
    # mappings are explicitly suggestions unless separately backed by a notice.
    for profile in exam_profiles:
        tag = profile.get("exam_tag")
        if tag:
            profile["tagged_record_count"] = sum(tag in q["exam_tags"] for q in questions)
        else:
            profile["tagged_record_count"] = len(questions)

    catalog_payload = {
        "schema_version": 1,
        "catalog_version": "ekguru-site-catalog-v1",
        "bank_build_id": build_id,
        "canonical_sha256": canonical_sha,
        "generated_on": generated_on,
        "subjects": subject_entries,
        "exam_profiles": exam_profiles,
        "syllabus_mappings": mappings_doc.get("mappings", []),
        "source_register_url": "assets/source-register.min.json",
        "cn_bank_manifest_url": "assets/banks/cn/manifest.json",
        "source_evidence_policy": evidence_doc.get("policy"),
    }
    catalog_bytes = write_json(ASSETS / "catalog.min.json", catalog_payload, compact=True)

    build_manifest = {
        "schema_version": 1,
        "bank_build_id": build_id,
        "generated_on": generated_on,
        "canonical_file": "Computer Network/data/cn_questions.json",
        "canonical_sha256": canonical_sha,
        "question_count": len(questions),
        "published_question_count": len(chunks_all),
        "review_only_excluded_count": len(questions) - len(chunks_all),
        "topic_counts": {item["topic_id"]: item["record_count"] for item in chunk_manifest},
        "published_topic_counts": {item["topic_id"]: item["published_question_count"] for item in chunk_manifest},
        "source_type_counts": manifest_payload["by_source_type"],
        "verification_counts": manifest_payload["by_verification"],
        "language_coverage": lang,
        "assets": {
            "catalog": {"file": "assets/catalog.min.json", "sha256": sha256_bytes(catalog_bytes), "bytes": len(catalog_bytes)},
            "cn_manifest": {"file": "assets/banks/cn/manifest.json", "sha256": sha256_bytes(manifest_bytes), "bytes": len(manifest_bytes)},
            "source_register": {"file": "assets/source-register.min.json", "sha256": sha256_bytes(source_bytes), "bytes": len(source_bytes)},
            "compatibility_bank": {"file": "assets/cn-questions.min.json", "sha256": sha256_bytes(compatibility_bytes), "bytes": len(compatibility_bytes)},
            "topic_chunks": [{"file": x["file"], "sha256": x["sha256"], "bytes": x["bytes"], "record_count": x["published_question_count"], "canonical_record_count": x["record_count"]} for x in chunk_manifest],
        },
        "subject_statuses": {item["id"]: item["status"] for item in subject_entries},
        "exam_blueprint_statuses": {profile["id"]: profile.get("pattern_status") for profile in exam_profiles},
    }
    write_json(ROOT / "data/reports/build_manifest.json", build_manifest)

    print(f"Canonical: {SRC.relative_to(ROOT)} sha256={canonical_sha}")
    print(f"bank_build_id: {build_id}")
    print(f"records: {len(questions)}; topics: {len(chunk_manifest)}")
    print("by topic:", build_manifest["topic_counts"])
    print("by source type:", manifest_payload["by_source_type"])
    print("by verification:", manifest_payload["by_verification"])
    print("language coverage:", lang)
    print(f"generated topic chunks: {len(chunk_manifest)}; source records: {len(public_sources)}")
    print(f"compatibility bank: assets/cn-questions.min.json ({len(compatibility_bytes)} bytes; not fetched by the live app)")
    print(f"catalog: assets/catalog.min.json ({len(catalog_bytes)} bytes)")


if __name__ == "__main__":
    main()
