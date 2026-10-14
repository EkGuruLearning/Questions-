#!/usr/bin/env python3
"""Report exact duplicates and conservative near-duplicate candidates.

The near-duplicate output is a human-review queue, not an automatic merge/deletion
instruction. All candidate pairs retain stable question IDs and shared terms.
"""
from __future__ import annotations

import argparse
import csv
import json
import pathlib
import re
import unicodedata
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
BANK_PATH = ROOT / "Computer Network/data/cn_questions.json"
QUEUE_PATH = ROOT / "Computer Network/Reports/DUPLICATE_REVIEW_QUEUE.csv"
SUMMARY_PATH = ROOT / "data/reports/duplicate_audit.json"
FILLER = set("which of the following is a an in are and to or be its with for that it the is of a".split())


def normalize(value: str) -> str:
    text = unicodedata.normalize("NFKC", value or "").lower()
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def audit(questions: list[dict]):
    exact = defaultdict(list)
    normalized = []
    for q in questions:
        key = normalize(q["stem_en"])
        exact[key].append(q["id"])
        normalized.append((q["id"], key, set(key.split()) - FILLER))
    exact_groups = [
        {"normalized_stem": key, "question_ids": sorted(ids)}
        for key, ids in exact.items() if len(ids) > 1
    ]
    near = []
    for a in range(len(normalized)):
        ida, _, ta = normalized[a]
        if len(ta) < 3:
            continue
        for b in range(a + 1, len(normalized)):
            idb, _, tb = normalized[b]
            if len(tb) < 3:
                continue
            shared = ta & tb
            if len(shared) >= 3 and len(shared) >= 0.6 * min(len(ta), len(tb)):
                near.append({
                    "question_a": ida,
                    "question_b": idb,
                    "overlap_count": len(shared),
                    "token_count_a": len(ta),
                    "token_count_b": len(tb),
                    "shared_terms": sorted(shared),
                    "review_status": "pending_manual_concept_review",
                    "decision": "",
                    "rationale": "",
                })
    near.sort(key=lambda row: (-row["overlap_count"], row["question_a"], row["question_b"]))
    return exact_groups, near


def write_outputs(questions: list[dict], exact_groups: list[dict], near: list[dict]):
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = (
        "pair_id", "question_a", "question_b", "overlap_count", "token_count_a",
        "token_count_b", "shared_terms", "review_status", "decision", "rationale",
    )
    with QUEUE_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for index, row in enumerate(near, 1):
            writer.writerow({
                "pair_id": f"NDC-{index:04d}",
                "question_a": row["question_a"],
                "question_b": row["question_b"],
                "overlap_count": row["overlap_count"],
                "token_count_a": row["token_count_a"],
                "token_count_b": row["token_count_b"],
                "shared_terms": " ".join(row["shared_terms"]),
                "review_status": row["review_status"],
                "decision": row["decision"],
                "rationale": row["rationale"],
            })
    bank = json.loads(BANK_PATH.read_text(encoding="utf-8"))
    summary = {
        "schema_version": 1,
        "bank_build_id": "cn-" + __import__("hashlib").sha256(BANK_PATH.read_bytes()).hexdigest()[:16],
        "canonical_sha256": __import__("hashlib").sha256(BANK_PATH.read_bytes()).hexdigest(),
        "record_count": len(questions),
        "method": "Unicode NFKC + ASCII word normalization; near candidate if shared non-filler tokens >= 3 and >=60% of the smaller token set.",
        "exact_duplicate_group_count": len(exact_groups),
        "exact_duplicate_groups": exact_groups,
        "near_duplicate_candidate_count": len(near),
        "near_duplicate_reviewed_count": 0,
        "near_duplicate_pending_count": len(near),
        "queue_file": QUEUE_PATH.relative_to(ROOT).as_posix(),
        "manual_review_policy": "Candidates are not auto-deleted or merged; reviewer must compare meaning, options, answer and learning objective.",
        "near_duplicate_candidates": near,
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"records={len(questions)} exact_groups={len(exact_groups)} near_candidates={len(near)} reviewed=0 pending={len(near)}")
    print(f"queue={QUEUE_PATH.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="audit only; do not write queue artifacts")
    args = parser.parse_args()
    bank = json.loads(BANK_PATH.read_text(encoding="utf-8"))
    questions = bank["questions"]
    exact_groups, near = audit(questions)
    if args.check:
        print(f"records={len(questions)} exact_groups={len(exact_groups)} near_candidates={len(near)} reviewed=0 pending={len(near)}")
    else:
        write_outputs(questions, exact_groups, near)


if __name__ == "__main__":
    main()
