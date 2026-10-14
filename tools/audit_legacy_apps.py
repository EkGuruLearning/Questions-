#!/usr/bin/env python3
"""Audit preserved legacy CBT source and verify old public paths redirect safely."""
from __future__ import annotations
import collections
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
ARCHIVE_DIR = ROOT / "archive/pre-audit-2026-10-14/Computer Network/Online Quiz"
LIVE_DIR = ROOT / "Computer Network/Online Quiz"
REPORT = ROOT / "Computer Network/Reports/LEGACY_APPS.md"
JSON_REPORT = ROOT / "data/reports/legacy_app_audit.json"
BANK = json.loads((ROOT / "Computer Network/data/cn_questions.json").read_text(encoding="utf-8"))
EVIDENCE = json.loads((ROOT / "data/sources/official_paper_key_evidence.json").read_text(encoding="utf-8"))


def main():
    pages = []
    total_records = 0
    old_official = 0
    incomplete = 0
    source_counts = collections.Counter()
    for number in range(1, 8):
        name = f"Topic {number} - Online Quiz & Exam (by PRAKASH - EkGuru).html"
        original_path = ARCHIVE_DIR / f"{name}.snapshot"
        redirect_path = LIVE_DIR / name
        original = original_path.read_text(encoding="utf-8")
        current = redirect_path.read_text(encoding="utf-8")
        match = re.search(r"(?:const|var|let)\s+QUESTIONS\s*=\s*(\[.*?\]);", original, re.S)
        if not match:
            raise SystemExit(f"Could not parse preserved question list: {original_path}")
        questions = json.loads(match.group(1))
        original_sha = hashlib.sha256(original_path.read_bytes()).hexdigest()
        current_redirect = "legacy CBT snapshot has been retired" in current and "window.location.replace" in current
        fallback_target = f"topic=T{number:02d}"
        if not current_redirect or fallback_target not in current or "../../practice/index.html" not in current:
            raise SystemExit(f"Old public path does not redirect to its topic: {redirect_path}")
        source_by_type = collections.Counter(q.get("stype", "unknown") for q in questions)
        old_official += source_by_type.get("verified_official_pyq", 0)
        total_records += len(questions)
        for q in questions:
            source_counts[q.get("stype", "unknown")] += 1
            options = q.get("opts") or []
            if len(options) != 4 or any(not (option[0] or "").strip() for option in options):
                incomplete += 1
        pages.append({
            "topic_id": f"T{number:02d}",
            "archive_file": original_path.relative_to(ROOT).as_posix(),
            "redirect_file": redirect_path.relative_to(ROOT).as_posix(),
            "sha256_preserved_original": original_sha,
            "record_count": len(questions),
            "source_type_counts": dict(sorted(source_by_type.items())),
            "stale_official_labels": source_by_type.get("verified_official_pyq", 0),
            "redirect_verified": current_redirect,
        })
    executable_archive_html = list((ROOT / "archive").rglob("*.html"))
    if executable_archive_html:
        raise SystemExit(f"Archived HTML is still directly runnable: {executable_archive_html[0]}")
    evidence_count = len(EVIDENCE.get("records", []))
    result = {
        "schema_version": 1,
        "canonical_build_id": "cn-" + hashlib.sha256((ROOT / "Computer Network/data/cn_questions.json").read_bytes()).hexdigest()[:16],
        "legacy_topic_pages": pages,
        "legacy_record_total": total_records,
        "preserved_legacy_verified_official_labels": old_official,
        "canonical_question_level_official_evidence_records": evidence_count,
        "legacy_records_with_incomplete_options": incomplete,
        "legacy_source_type_counts": dict(sorted(source_counts.items())),
        "finding": "The preserved snapshots embed historical source-status labels and standalone data; they are not the current canonical bank. Original bytes are archived and the former public paths now redirect to the shared provenance-aware portal.",
    }
    JSON_REPORT.parent.mkdir(parents=True, exist_ok=True)
    JSON_REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Legacy CBT Page Audit",
        "",
        f"**Current bank build ID:** `{result['canonical_build_id']}`",
        "",
        "The seven original standalone HTML quiz pages were inspected and preserved byte-for-byte as `.html.snapshot` files under `archive/pre-audit-2026-10-14/Computer Network/Online Quiz/`. Archived HTML snapshots use a non-runnable suffix so stale standalone apps are not republished from the archive. Their former public paths now redirect to the shared provenance-aware portal with the matching topic preselected.",
        "",
        f"The preserved snapshots embed {total_records:,} records and **{old_official} `verified_official_pyq` labels**. The current question-level official paper/final-key evidence register has {evidence_count} entries. The old embedded status labels are historical and are not used by the new portal.",
        f"The archived snapshots contain {incomplete} records with at least one blank option (including the two canonical records now marked `pending_review`). Original page data is retained; incomplete questions are not testable in the new portal.",
        "",
        "| Topic | Archived records | Archived official labels | Preserved original SHA-256 | Former path redirects? |",
        "|---|---:|---:|---|---|",
    ]
    for page in pages:
        lines.append(f"| {page['topic_id']} | {page['record_count']} | {page['stale_official_labels']} | `{page['sha256_preserved_original']}` | {page['redirect_verified']} |")
    lines += [
        "",
        "The archived pages are not current apps and must not be linked as verified tests. The current portal uses generated topic chunks and per-question status filters. No original PDF or legacy HTML archive was deleted.",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"PASS: archived pages={len(pages)} records={total_records} stale_official_labels={old_official} incomplete={incomplete} evidence={evidence_count}")


if __name__ == "__main__":
    main()
