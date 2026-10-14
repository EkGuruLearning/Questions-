#!/usr/bin/env python3
"""Conservatively reconcile CN provenance and annotate the canonical schema.

This is intentionally a one-way safe migration: it never upgrades a verification
status. Records labelled paper_and_key_checked without a question-level entry in
`data/sources/official_paper_key_evidence.json` are downgraded, not deleted.
"""
from __future__ import annotations

import collections
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BANK_PATH = ROOT / "Computer Network/data/cn_questions.json"
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
LETTERS = "ABCD"


def source_id(value: str) -> str:
    return "src-" + hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def read_json(path: pathlib.Path):
    return json.loads(path.read_text(encoding="utf-8"))


def scrub_unsupported_key_wording(text: str) -> str:
    patterns = (
        r"(?i)matches?\s+the\s+official\s+RPSC(?:\s+2024)?\s+key(?:\s*\([a-d]\))?",
        r"(?i)official\s+RPSC(?:\s+2024)?\s+key(?:\s*\([a-d]\))?",
        r"(?i)RPSC(?:\s+2024)?\s+official\s+key(?:\s*\([a-d]\))?",
        r"(?i)official\s+key(?:\s*\([a-d]\))?",
    )
    for pattern in patterns:
        text = re.sub(pattern, "unverified supplied answer-table claim", text)
    return text


def main() -> None:
    bank = read_json(BANK_PATH)
    evidence = read_json(EVIDENCE_PATH)
    accepted_ids = set()
    for record in evidence.get("records", []):
        paper = record.get("official_paper") or {}
        key = record.get("official_final_key") or {}
        if (paper.get("url") or paper.get("file")) and (key.get("url") or key.get("file")):
            accepted_ids.update(record.get("question_ids", []))

    downgraded = []
    for q in bank["questions"]:
        source = str(q.get("source_url_or_file") or "")
        # Preserve the source trail, but correct an unsupported use of the word
        # “official”: the checked-in answer table is a community transcription.
        if q.get("verification_status") == "paper_and_key_checked" and q["id"] not in accepted_ids:
            if re.search(r"RPSC\s+Programmer\s+2024\s+Paper[- ]?1", source, re.I):
                for field in ("explanation_en", "explanation_hi", "nukte_en", "nukte_hi"):
                    q[field] = scrub_unsupported_key_wording(q.get(field) or "")
                q["source_url_or_file"] = (
                    "Computer Network/Past Papers/RPSC Programmer 2024 Paper-1/"
                    "2024 Programmer Paper-1 QUESTIONS.md; "
                    "2024 Programmer Paper-1 ANSWERS.md (community-maintained; "
                    "answer table says it is based on standard solutions and "
                    "recommends checking the official key)"
                )
                q["provenance_note"] = (
                    "The repository README identifies this as a community-maintained transcription; "
                    "the answer table is not an official final/corrected key."
                )
                q["exam_name"] = "RPSC Programmer"
                q["exam_year"] = 2024
                q["paper_or_shift"] = "Paper 1"
            q["source_type"] = "claimed_pyq_unverified"
            q["verification_status"] = "claimed_answer_unverified"
            q["answer_verified_by"] = (
                "Unverified: checked-in answer table is community-maintained, "
                "not an official final answer key; independent review pending."
            )
            downgraded.append(q["id"])

        if q.get("verification_status") == "claimed_answer_unverified" and re.search(r"RPSC\s+Programmer\s+2024\s+Paper[- ]?1", source, re.I):
            for field in ("explanation_en", "explanation_hi", "nukte_en", "nukte_hi"):
                q[field] = scrub_unsupported_key_wording(q.get(field) or "")

        # Stable option identity supplements, but does not replace, the legacy
        # options_en/options_hi/correct_option fields used by the PDF pipeline.
        options = q.get("options_en")
        if not isinstance(options, list) or len(options) != 4:
            raise ValueError(f"{q.get('id')}: expected four English options")
        if any(not isinstance(option, str) or not option.strip() for option in options):
            q["verification_status"] = "pending_review"
            q["answer_verified_by"] = "Pending review: one or more answer options are blank; source wording is preserved."
            q["provenance_note"] = "Question content is incomplete because at least one answer option is blank; do not use in practice until a source-backed correction is reviewed."
        q["subject_id"] = "cn"
        q["question_type"] = "single_select_mcq"
        q["option_ids"] = list(LETTERS)
        correct = q.get("correct_option")
        if correct not in LETTERS:
            raise ValueError(f"{q.get('id')}: invalid correct_option {correct!r}")
        q["answer_option_id"] = correct
        q["difficulty_basis"] = "heuristic_classifier_estimate"
        src_type = q.get("source_type")
        if src_type == "claimed_pyq_unverified":
            q["exam_tag_basis"] = "source_claim_unverified"
        elif q.get("exam_name") and src_type != "original_practice":
            q["exam_tag_basis"] = "source_label_unverified"
        else:
            q["exam_tag_basis"] = "suggested_practice_fit"
        q["source_id"] = source_id(str(q.get("source_url_or_file") or ""))
        if q.get("verification_status") not in STATUS_VALUES:
            raise ValueError(f"{q.get('id')}: invalid verification status")
        if src_type not in SOURCE_VALUES:
            raise ValueError(f"{q.get('id')}: invalid source type {src_type!r}")

    # No official label can survive unless an evidence entry explicitly names
    # that stable question ID and includes both an official paper and final key.
    for q in bank["questions"]:
        if q.get("verification_status") == "paper_and_key_checked" and q["id"] not in accepted_ids:
            raise ValueError(f"{q['id']}: unsupported paper_and_key_checked status")
        if q.get("source_type") == "verified_official_pyq" and q["id"] not in accepted_ids:
            raise ValueError(f"{q['id']}: unsupported verified_official_pyq source type")

    questions = bank["questions"]
    by_topic = collections.Counter(q["topic_id"] for q in questions)
    by_source = collections.Counter(q["source_type"] for q in questions)
    by_status = collections.Counter(q["verification_status"] for q in questions)
    by_difficulty = collections.Counter(q["difficulty"] for q in questions)
    by_style = collections.Counter(q["question_style"] for q in questions)
    bank["schema_version"] = 2
    bank["schema_note"] = (
        "Stable subject and option IDs supplement the original CN fields; "
        "legacy text arrays are retained for existing PDF/build tools."
    )
    bank["counts"] = {
        "total": len(questions),
        "per_topic": dict(sorted(by_topic.items())),
        "by_source_type": dict(sorted(by_source.items())),
        "by_verification": {key: by_status.get(key, 0) for key in STATUS_VALUES},
        "by_difficulty": dict(sorted(by_difficulty.items())),
        "by_style": dict(sorted(by_style.items())),
        "downgraded_unsupported_official_labels": len(downgraded),
        "official_evidence_records": len(accepted_ids),
    }
    BANK_PATH.write_text(json.dumps(bank, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Schema v2 applied: {len(questions)} records; downgraded {len(downgraded)} unsupported official labels.")
    print("Downgraded IDs:", ", ".join(downgraded) if downgraded else "none")
    print("By verification:", dict(sorted(by_status.items())))
    print("By source type:", dict(sorted(by_source.items())))
    print("Input evidence register:", EVIDENCE_PATH.relative_to(ROOT))


if __name__ == "__main__":
    main()
