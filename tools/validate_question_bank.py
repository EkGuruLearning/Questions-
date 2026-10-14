#!/usr/bin/env python3
"""Validate canonical CN data, official-evidence gates, and generated site payloads."""
from __future__ import annotations

import collections
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_site_data  # noqa: E402

BANK_PATH = ROOT / "Computer Network/data/cn_questions.json"
MANIFEST_PATH = ROOT / "assets/banks/cn/manifest.json"
CATALOG_PATH = ROOT / "assets/catalog.min.json"
SOURCE_PATH = ROOT / "assets/source-register.min.json"
COMPAT_PATH = ROOT / "assets/cn-questions.min.json"
EVIDENCE_PATH = ROOT / "data/sources/official_paper_key_evidence.json"


def fail(message: str):
    raise SystemExit("FAIL: " + message)


def main():
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
        fail("paper_and_key_checked count does not match question-level official evidence register")
    if source_counts.get("verified_official_pyq", 0) != len(evidence_ids):
        fail("verified_official_pyq count does not match official evidence register")

    if not MANIFEST_PATH.exists() or not CATALOG_PATH.exists() or not SOURCE_PATH.exists() or not COMPAT_PATH.exists():
        fail("generated site data missing; run python3 tools/build_site_data.py")
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    sources = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
    compat = json.loads(COMPAT_PATH.read_text(encoding="utf-8"))
    for label, data in (("manifest", manifest), ("catalog", catalog), ("source register", sources)):
        if data.get("bank_build_id") != build_id or data.get("canonical_sha256") != sha:
            fail(f"{label} is stale for current canonical data")
    publishable_ids = {q["id"] for q in questions if q["verification_status"] not in ("disputed", "pending_review")}
    if len(compat) != len(publishable_ids):
        fail("compatibility export publishable-record count mismatch")
    if manifest.get("question_count") != len(questions):
        fail("generated canonical manifest count mismatch")
    if manifest.get("published_question_count") != len(publishable_ids):
        fail("generated published-question count mismatch")
    generated_chunks = []
    for chunk in manifest.get("topics", []):
        path = ROOT / chunk["file"]
        if not path.is_file():
            fail(f"missing topic chunk {chunk['file']}")
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != chunk["sha256"]:
            fail(f"topic chunk hash mismatch: {chunk['file']}")
        items = json.loads(raw)
        if len(items) != chunk["published_question_count"]:
            fail(f"topic chunk count mismatch: {chunk['topic_id']}")
        if any(q["topic_id"] != chunk["topic_id"] for q in items):
            fail(f"topic chunk contains a wrong-topic record: {chunk['topic_id']}")
        generated_chunks.extend(items)
    canonical_ids = publishable_ids
    generated_ids = [q["id"] for q in generated_chunks]
    if len(generated_ids) != len(set(generated_ids)) or set(generated_ids) != canonical_ids:
        fail("generated chunk IDs are not a one-to-one match with publishable canonical IDs")
    if any(q["verification_status"] in ("disputed", "pending_review") for q in generated_chunks):
        fail("disputed/pending records must not be published in practice chunks")
    source_ids = {item["id"] for item in sources.get("records", [])}
    if any(q["source_id"] not in source_ids for q in generated_chunks):
        fail("public question references a missing source-register entry")
    if any(q["verification_status"] not in ("paper_and_key_checked", "answer_checked") for q in generated_chunks if q["verification_status"] == "pending_review"):
        fail("pending question found in public payload")
    for q in generated_chunks:
        if q["verification_status"] == "paper_and_key_checked" and q["id"] not in evidence_ids:
            fail(f"official question lacks evidence: {q['id']}")
        if len(q["options"]) != 4 or q["answer_option_id"] not in {o["id"] for o in q["options"]}:
            fail(f"public option/key mismatch: {q['id']}")

    print("PASS: canonical schema v2 and public exports are consistent")
    print(f"bank_build_id={build_id}")
    print(f"canonical_sha256={sha}")
    print(f"question_count={len(questions)}")
    print("topic_counts=" + json.dumps(dict(sorted(counts.items())), sort_keys=True))
    print("source_type_counts=" + json.dumps({k: source_counts.get(k, 0) for k in build_site_data.SOURCE_VALUES}, sort_keys=True))
    print("verification_counts=" + json.dumps({k: verification_counts.get(k, 0) for k in build_site_data.STATUS_VALUES}, sort_keys=True))
    print("public_source_records=" + str(sources["source_count"]))
    print("public_topic_chunks=" + str(len(manifest["topics"])))


if __name__ == "__main__":
    main()
