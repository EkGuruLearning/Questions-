#!/usr/bin/env python3
"""Validate the canonical CN bank and the generated browser test chunks."""
from __future__ import annotations

import collections
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_site_data  # noqa: E402

BANK_PATH = ROOT / "data/banks/cn/cn_questions.json"
MANIFEST_PATH = ROOT / "data/banks/cn/manifest.json"
EVIDENCE_PATH = ROOT / "data/sources/official_paper_key_evidence.json"


def fail(message: str):
    raise SystemExit("FAIL: " + message)


def main() -> int:
    bank_raw = BANK_PATH.read_bytes()
    bank = json.loads(bank_raw)
    sha = hashlib.sha256(bank_raw).hexdigest()
    build_id = "cn-" + sha[:16]
    evidence_ids = build_site_data.validate_evidence(json.loads(EVIDENCE_PATH.read_text(encoding="utf-8")), bank["questions"])
    questions = build_site_data.validate_canonical(bank, evidence_ids)

    counts = collections.Counter(q["topic_id"] for q in questions)
    source_counts = collections.Counter(q["source_type"] for q in questions)
    verification_counts = collections.Counter(q["verification_status"] for q in questions)

    if sum(counts.values()) != len(questions):
        fail("topic counts do not sum to canonical total")
    if bank.get("counts", {}).get("total") != len(questions):
        fail("canonical counts.total mismatch")
    for tid, count in counts.items():
        if bank["counts"].get("per_topic", {}).get(tid) != count:
            fail(f"canonical count mismatch for {tid}")
    if verification_counts.get("paper_and_key_checked", 0) != len(evidence_ids):
        fail("paper_and_key_checked count does not match the official evidence register")
    if source_counts.get("verified_official_pyq", 0) != len(evidence_ids):
        fail("verified_official_pyq count does not match the official evidence register")

    if not MANIFEST_PATH.exists():
        fail("data/banks/cn/manifest.json missing; run python3 tools/build_site_data.py")
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest.get("bank_build_id") != build_id or manifest.get("canonical_sha256") != sha:
        fail("bank manifest is stale for the current canonical data")

    publishable_ids = {q["id"] for q in questions if q["verification_status"] not in ("disputed", "pending_review")}
    if manifest.get("question_count") != len(questions):
        fail("manifest question_count mismatch")
    if manifest.get("published_question_count") != len(publishable_ids):
        fail("manifest published_question_count mismatch")

    seen: list[str] = []
    for chunk in manifest.get("topics", []):
        path = ROOT / chunk["file"]
        if not path.is_file():
            fail(f"missing topic chunk {chunk['file']}")
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != chunk["sha256"]:
            fail(f"topic chunk hash mismatch: {chunk['file']}")
        if not chunk["file"].startswith("data/banks/cn/"):
            fail(f"topic chunk must live under data/banks/cn/: {chunk['file']}")
        items = json.loads(raw)
        if len(items) != chunk["published_question_count"]:
            fail(f"topic chunk count mismatch: {chunk['topic_id']}")
        for question in items:
            if question["topic_id"] != chunk["topic_id"]:
                fail(f"topic chunk contains a wrong-topic record: {chunk['topic_id']}")
            if question["verification_status"] in ("disputed", "pending_review"):
                fail(f"review-only record published in a test chunk: {question['id']}")
            if len(question["options"]) != 4 or question["answer_option_id"] not in {option["id"] for option in question["options"]}:
                fail(f"option/key mismatch in a test chunk: {question['id']}")
            if not question["stem_en"].strip():
                fail(f"empty question stem in a test chunk: {question['id']}")
        seen.extend(item["id"] for item in items)

    if len(seen) != len(set(seen)) or set(seen) != publishable_ids:
        fail("generated chunks are not a one-to-one match with published canonical IDs")

    extra = sorted(path.name for path in (ROOT / "data/banks/cn").glob("T0*.min.json")
                   if path.name not in {chunk["file"].rsplit("/", 1)[-1] for chunk in manifest["topics"]})
    if extra:
        fail(f"stale topic chunks present: {extra}")

    print("PASS: canonical schema v2 bank and browser test chunks are consistent")
    print(f"bank_build_id={build_id}")
    print(f"canonical_sha256={sha}")
    print(f"question_count={len(questions)} published={len(publishable_ids)}")
    print("topic_counts=" + json.dumps(dict(sorted(counts.items())), sort_keys=True))
    print("verification_counts=" + json.dumps({key: verification_counts.get(key, 0) for key in build_site_data.STATUS_VALUES}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
