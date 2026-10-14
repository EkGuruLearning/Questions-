#!/usr/bin/env python3
"""Regenerate the CN report set from the canonical bank and generated manifest."""
from __future__ import annotations

import collections
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from audit_duplicates import audit, write_outputs  # noqa: E402
import audit_legacy_apps  # noqa: E402

BANK = ROOT / "Computer Network/data/cn_questions.json"
REPORTS = ROOT / "Computer Network/Reports"
BUILD_MANIFEST = ROOT / "data/reports/build_manifest.json"
QA_RESULTS = ROOT / "data/reports/qa_results.json"
BROWSER_QA = ROOT / "data/reports/browser_visual_qa.json"
PDF_QA = ROOT / "data/reports/pdf_rendering_qa.json"
EVIDENCE = ROOT / "data/sources/official_paper_key_evidence.json"
EXAMS = ROOT / "data/catalog/exams.json"

TOPIC_NAMES = {
    "T01": "Introduction of Data Communication",
    "T02": "Network Models (OSI & TCP/IP)",
    "T03": "Addressing (MAC, IPv4, IPv6, Port, DNS)",
    "T04": "Networking Devices",
    "T05": "Transmission Medium",
    "T06": "OSI Layers in Detail",
    "T07": "Network Security",
}
SOURCES = (
    "verified_official_pyq",
    "claimed_pyq_unverified",
    "repository_internal",
    "textbook_paraphrase",
    "original_practice",
)
STATUSES = (
    "paper_and_key_checked",
    "answer_checked",
    "claimed_answer_unverified",
    "disputed",
    "pending_review",
)


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ui_fingerprint():
    value = hashlib.sha256()
    for relative in ("index.html", "assets/css/portal.css", "assets/js/app.mjs", "assets/js/engine.mjs"):
        value.update(relative.encode("utf-8"))
        value.update(bytes((0,)))
        value.update((ROOT / relative).read_bytes())
        value.update(bytes((0,)))
    return value.hexdigest()


def current_pdf_qa(report):
    if not report:
        return None
    try:
        output = subprocess.run(
            ["git", "ls-files", "-z", "--", "*.pdf"],
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
        ).stdout
        current_paths = {item.decode("utf-8") for item in output.split(bytes((0,))) if item}
        entries = report.get("files", [])
        expected = {item["path"]: item["sha256_after"] for item in entries}
        if not current_paths or current_paths != set(expected):
            return None
        for relative, sha256 in expected.items():
            path = ROOT / relative
            if not path.is_file() or digest(path) != sha256:
                return None
        return report
    except (KeyError, OSError, subprocess.CalledProcessError):
        return None


def md_header(title, build_id, canonical_sha, date):
    return (
        f"# {title}\n\n"
        f"**Bank build ID:** `{build_id}`<br>\n"
        f"**Canonical SHA-256:** `{canonical_sha}`<br>\n"
        f"**Snapshot date:** {date}\n\n"
    )


def md_table(counter, keys):
    lines = ["| Category | Records |", "|---|---:|"]
    for key in keys:
        lines.append(f"| `{key}` | {counter.get(key, 0)} |")
    return "\n".join(lines) + "\n"


def get_duplicate_data(bank):
    exact_groups, near = audit(bank["questions"])
    write_outputs(bank["questions"], exact_groups, near)
    return exact_groups, near


def write_inventory(bank, manifest, build_id, sha, date):
    q = bank["questions"]
    by_topic = collections.Counter(item["topic_id"] for item in q)
    by_source = collections.Counter(item["source_type"] for item in q)
    by_status = collections.Counter(item["verification_status"] for item in q)
    by_difficulty = collections.Counter(item["difficulty"] for item in q)
    by_style = collections.Counter(item["question_style"] for item in q)
    language = manifest["language_coverage"]
    text = md_header("CN Question Bank — Current Inventory", build_id, sha, date)
    text += (
        f"**Canonical records:** {len(q):,}. These are records, not proof of the same number of unique concepts or official PYQs.\n\n"
        "## By topic\n\n| Topic ID | Topic | Records |\n|---|---|---:|\n"
    )
    for tid in TOPIC_NAMES:
        text += f"| {tid} | {TOPIC_NAMES[tid]} | {by_topic.get(tid, 0)} |\n"
    text += "\n## By source type\n\n" + md_table(by_source, SOURCES)
    text += "\n## By answer-verification status\n\n" + md_table(by_status, STATUSES)
    text += "\n## Difficulty estimates (heuristic; not calibrated)\n\n" + md_table(by_difficulty, ("easy", "medium", "hard"))
    text += "\n## Question styles (heuristic labels; all current records render as single-select MCQ)\n\n" + md_table(by_style, sorted(by_style))
    text += "\n## Language coverage (actual fields, not a global bilingual claim)\n\n"
    text += "| Field coverage | Records |\n|---|---:|\n"
    for key in ("stem_en", "stem_hi", "options_en_complete", "options_hi_complete", "explanation_en", "explanation_hi", "nukta_en", "nukta_hi", "full_bilingual_records"):
        text += f"| `{key}` | {language[key]} |\n"
    text += "\nHindi display falls back to English for any missing translation; the UI labels that fallback per question.\n"
    (REPORTS / "INVENTORY.md").write_text(text, encoding="utf-8")


def write_duplicate_report(bank, build_id, sha, date, exact_groups, near):
    text = md_header("Duplicate Audit", build_id, sha, date)
    text += (
        "Method: Unicode NFKC and normalized English-stem exact scan; near candidates use a conservative token-overlap threshold "
        "(at least 3 non-filler shared tokens and at least 60% of the smaller token set). Candidates are not merged or deleted automatically.\n\n"
    )
    text += f"## Exact duplicate groups: {len(exact_groups)}\n\n"
    if exact_groups:
        for group in exact_groups:
            text += f"- `{group['normalized_stem'][:100]}` — {', '.join(group['question_ids'])}\n"
    else:
        text += "No normalized exact-stem groups were found by this scan.\n"
    text += f"\n## Near-duplicate candidates: {len(near)}\n\n"
    text += "- Concept-level review completed in this implementation: **0**\n"
    text += f"- Pending manual review: **{len(near)}**\n"
    text += "- Full queue with stable IDs, shared terms and disposition columns: `DUPLICATE_REVIEW_QUEUE.csv`\n\n"
    text += "Top candidates (triage aid only):\n\n| ID A | ID B | Shared tokens | Terms |\n|---|---|---:|---|\n"
    for row in near[:60]:
        terms = ", ".join(row["shared_terms"][:10]).replace("|", "\\|")
        text += f"| {row['question_a']} | {row['question_b']} | {row['overlap_count']} | {terms} |\n"
    text += "\nA high token overlap is not proof of a duplicate. Review stem, answer, options, objective, source and explanation before disposition.\n"
    (REPORTS / "DUPLICATE_AUDIT.md").write_text(text, encoding="utf-8")


def write_answer_report(bank, build_id, sha, date, evidence):
    statuses = collections.Counter(q["verification_status"] for q in bank["questions"])
    source_types = collections.Counter(q["source_type"] for q in bank["questions"])
    text = md_header("Answer Verification Report", build_id, sha, date)
    text += (
        "The `answer_checked` label is a curation-pipeline status, not official paper/final-key matching. "
        "A claimed PYQ source and an answer-check status are separate dimensions. No blanket ‘fully verified’ claim is made.\n\n"
        "| Verification status | Records | Meaning |\n|---|---:|---|\n"
        f"| `paper_and_key_checked` | {statuses.get('paper_and_key_checked', 0)} | Question-level official paper and final/corrected key evidence recorded in the evidence register. |\n"
        f"| `answer_checked` | {statuses.get('answer_checked', 0)} | Answer-level curation review; does not establish exam provenance or official-key match. |\n"
        f"| `claimed_answer_unverified` | {statuses.get('claimed_answer_unverified', 0)} | Source answer or claim is not independently verified for release. |\n"
        f"| `disputed` | {statuses.get('disputed', 0)} | Explicitly disputed; excluded from ordinary reviewed practice. |\n"
        f"| `pending_review` | {statuses.get('pending_review', 0)} | Awaiting review. |\n\n"
        "## Evidence-gate correction\n\n"
        "The 26 records previously labelled `paper_and_key_checked` were downgraded to `claimed_answer_unverified` and `claimed_pyq_unverified`. "
        "The checked-in `2024 Programmer Paper-1 ANSWERS.md` is a community-maintained answer table; its README says the answers are based on standard solutions and recommends checking the official key. "
        "It is not an official final/corrected key, and no stable question-to-official-key mapping is in the evidence register. The source files were preserved.\n\n"
        "## Source-type cross-check\n\n"
        f"- `verified_official_pyq`: {source_types.get('verified_official_pyq', 0)}\n"
        f"- `claimed_pyq_unverified`: {source_types.get('claimed_pyq_unverified', 0)}\n"
        "- Source type does not by itself say whether the answer was reviewed.\n\n"
        f"Evidence register entries: {len(evidence.get('records', []))}. No official record will be accepted without an exact paper, final key and stable question IDs.\n"
    )
    pending = [q for q in bank["questions"] if q["verification_status"] == "pending_review"]
    if pending:
        pending_ids = ", ".join(q["id"] for q in pending)
        text += f"\nPending content-quality records: {pending_ids}. At least one answer option is blank; source wording is retained and the records are excluded from public test chunks.\n"
    (REPORTS / "ANSWER_VERIFICATION.md").write_text(text, encoding="utf-8")


def write_source_report(bank, build_id, sha, date, evidence, source_payload):
    counts = collections.Counter(q["source_type"] for q in bank["questions"])
    tag_basis = collections.Counter(q["exam_tag_basis"] for q in bank["questions"])
    text = md_header("Source Register & Classification Rules", build_id, sha, date)
    text += (
        "## Current category counts\n\n" + md_table(counts, SOURCES) + "\n"
        "## Classification and evidence policy\n\n"
        "- `verified_official_pyq`: only when a stable question ID maps to an official paper and final/corrected key in `data/sources/official_paper_key_evidence.json`.\n"
        "- `claimed_pyq_unverified`: a source or citation claims an exam appearance, but official paper/key matching is absent.\n"
        "- `repository_internal`: repository tests, imported/coaching/OCR sources and other internal/third-party content.\n"
        "- `textbook_paraphrase`: textbook-derived practice wording; this is not a copied official exam question.\n"
        "- `original_practice`: original practice written for learning; it is not a PYQ.\n\n"
        "`paper_and_key_checked` is the only status that permits an item in Verified PYQ mock mode. `answer_checked` means answer review only.\n\n"
        "## Current official-evidence status\n\n"
        f"Accepted question-level paper+final-key evidence records: **{len(evidence.get('records', []))}**.\n\n"
        "The RPSC Programmer 2024 source transcription and answer table are community-maintained; the checked-in answer table explicitly recommends official-key verification. "
        "It is retained as a citation but does not count as an official final key.\n\n"
        "## Exam-tag provenance\n\n" + md_table(tag_basis, sorted(tag_basis)) + "\n"
        "Exam tags are practice filters, not proof of a past appearance. Some tags are source labels; others are difficulty/syllabus-fit suggestions. "
        "Exam-name/year labels are marked per question as source claims unless an official evidence record exists.\n\n"
        f"Public per-source citation records: {source_payload['source_count']} in `assets/source-register.min.json`. Each question references its source by stable `source_id`.\n"
    )
    (REPORTS / "SOURCE_REGISTER.md").write_text(text, encoding="utf-8")


def write_exam_report(build_id, sha, date, exam_doc, mappings_doc, bank):
    text = md_header("Exam Profiles & Syllabus Mappings", build_id, sha, date)
    text += (
        "No exam profile is published as an exact simulation in this build. Official links in the catalog are references, not a release-gate pass; "
        "timing and marking fields are deliberately not treated as verified. The UGC-NET syllabus index was checked and labels its syllabi as applicable from June 2019; "
        "the NTA homepage served June 2025 materials during this audit, so no current-cycle 2026 pattern is claimed. The draft `AnswerKey.html` URL was removed from the UGC pattern field.\n\n"
        "| Profile | Status | Scope | Pattern status | Tag records | Time / marking |\n|---|---|---|---|---:|---|\n"
    )
    for profile in exam_doc.get("profiles", []):
        tag = profile.get("exam_tag")
        tag_count = sum(tag in q.get("exam_tags", []) for q in bank["questions"]) if tag else len(bank["questions"])
        text += (
            f"| {profile['name']} | `{profile.get('status')}` | `{profile.get('simulation_level')}` | "
            f"`{profile.get('pattern_status')}` | {tag_count} | {profile.get('scoring_label', 'User-configured mock only')} |\n"
        )
    text += "\n## Official references (links are not current-cycle pattern approval)\n\n"
    for profile in exam_doc.get("profiles", []):
        links = [profile.get("official_syllabus_url"), profile.get("official_pattern_url")]
        links = [link for link in links if link]
        if links:
            text += f"- **{profile['name']}** — " + ", ".join(links) + "\n"
    text += "\n## Mapping status\n\n| Exam profile | Subject | Topics | Mapping status | Reference |\n|---|---|---|---|---|\n"
    for mapping in mappings_doc.get("mappings", []):
        topics = ", ".join(mapping.get("topic_ids", []))
        reference = mapping.get("source_ref", "").replace("|", "\\|")
        text += f"| `{mapping['exam_profile_id']}` | `{mapping['subject_id']}` | {topics} | `{mapping['mapping_status']}` | {reference} |\n"
    text += "\nGATE CN practice does not implement MSQ/NAT or a complete paper. UGC-NET, RPSC Programmer, Informatics Assistant and SSC rows are subject/segment practice only. "
    text += "Do not infer an exam's duration, section splits, negative marking or official PYQ coverage from these profiles.\n"
    (REPORTS / "EXAM_BLUEPRINTS.md").write_text(text, encoding="utf-8")


def write_totals(bank, manifest, build_id, sha, date, duplicate_summary):
    q = bank["questions"]
    by_topic = collections.Counter(item["topic_id"] for item in q)
    text = md_header("CN Question Bank — Totals & History", build_id, sha, date)
    text += f"**Current canonical total:** {len(q):,} records. Counts below are generated from the canonical file, not historical PDF cover labels.\n\n"
    text += "| Topic | Current records |\n|---|---:|\n"
    for tid, name in TOPIC_NAMES.items():
        text += f"| {tid} — {name} | {by_topic.get(tid, 0)} |\n"
    text += f"| **Total** | **{len(q)}** |\n\n"
    text += "## Current source-status split\n\n" + md_table(collections.Counter(x["source_type"] for x in q), SOURCES)
    text += "\n## Current answer-verification split\n\n" + md_table(collections.Counter(x["verification_status"] for x in q), STATUSES)
    text += "\n## Audit counts\n\n"
    text += f"- Exact normalized stem groups: {duplicate_summary['exact_duplicate_group_count']}\n"
    text += f"- Near-duplicate candidates: {duplicate_summary['near_duplicate_candidate_count']} ({duplicate_summary['near_duplicate_pending_count']} pending manual review)\n\n"
    text += "## Historical snapshots from earlier files (not current inventory)\n\n"
    text += "| Snapshot reference | Historical total | Use |\n|---|---:|---|\n"
    text += "| `Computer Network/COVERAGE.md`, early extraction diary (2026-10-09) | 593 | Historical capture/queue accounting; superseded. |\n"
    text += "| R1 notes in older report files | 801 | Historical release snapshot; superseded. |\n"
    text += "| R2 notes in older report files | 817 | Historical release snapshot; superseded. |\n"
    text += f"| Current canonical bank ({build_id}) | {len(q)} | Current source of truth. |\n\n"
    text += "Historical filenames/covers may describe partial books and must not be used as current bank totals.\n"
    (REPORTS / "TOTALS.md").write_text(text, encoding="utf-8")


def write_qa_report(build_id, sha, date, qa_results=None, browser_qa=None, pdf_qa=None):
    text = md_header("QA Report — Current Portal Build", build_id, sha, date)
    if qa_results:
        text += "## Recorded automated results\n\n| Check | Result | Command | Notes |\n|---|---|---|---|\n"
        for item in qa_results.get("checks", []):
            command = item.get("command", "").replace("|", "\\|")
            notes = item.get("notes", "").replace("|", "\\|")
            text += f"| {item.get('name')} | **{item.get('result')}** | `{command}` | {notes} |\n"
        text += "\n"
    else:
        text += "No `data/reports/qa_results.json` is present; do not infer automated checks from this report build.\n\n"

    text += "## Rendered-browser visual and accessibility QA\n\n"
    if browser_qa:
        viewport_sizes = ", ".join(f"{item['width']}×{item['height']}" for item in browser_qa.get("viewports", []))
        text += (
            f"**PASS** — {browser_qa.get('browser', 'headless browser')} at emulated viewports {viewport_sizes}. "
            "Landing and quiz layouts had no horizontal overflow; source dialogs fit their viewports; mobile navigation was exercised; "
            "all measured visible controls were at least 44 px high; axe reported "
            f"{browser_qa.get('total_axe_violations', 'unknown')} violations across landing, quiz and source-dialog states; "
            f"browser/runtime and failed-response errors: {len(browser_qa.get('browser_errors', []))}.\n\n"
            "Rendered screenshots were captured and visually reviewed. These are headless viewport emulations, not tests on physical devices.\n\n"
        )
    else:
        text += "**NOT PASS** — no current passing rendered-browser report is available for this UI build.\n\n"

    text += "## Original PDF validity and rendering QA\n\n"
    if pdf_qa:
        status = pdf_qa.get("status", "UNKNOWN")
        label = "PASS" if status == "PASS" else "PASS WITH WARNINGS" if status == "PASS_WITH_WARNINGS" else status
        text += (
            f"**{label}** — {pdf_qa.get('tracked_pdf_count', 0)} tracked PDFs; "
            f"{pdf_qa.get('total_pages_rendered', 0):,}/{pdf_qa.get('total_pages', 0):,} pages rendered; "
            f"{pdf_qa.get('mupdf_repaired_files', 0)} files repaired by MuPDF; "
            f"{pdf_qa.get('failed_files', 0)} failed files. "
            f"Original sizes and SHA-256 hashes unchanged: **{pdf_qa.get('all_source_hashes_unchanged', False)}**.\n\n"
            "This validates file opening, page-tree loading and rendering—not question/answer correctness, source provenance, print quality, or PDF/A conformance.\n\n"
        )
    else:
        text += "**NOT PASS** — no current PDF report matching the tracked PDF files is available.\n\n"

    text += (
        "## Scope and limitations\n\n"
        "- Current root portal data loads from a small catalog and content-hashed topic chunks.\n"
        "- Legacy topic HTML snapshots were inspected separately; they are retained as historical artifacts and must not be presented as current verification-gated apps.\n"
        "- The pre-change GitHub Pages source was fetched during this audit. This local QA run contains no post-merge or post-deployment live smoke test.\n"
    )
    (REPORTS / "QA_REPORT.md").write_text(text, encoding="utf-8")


def write_release_notes(bank, build_id, sha, date, manifest):
    text = md_header("EkGuru Portal — Implementation Release Notes", build_id, sha, date)
    text += (
        "## Current implementation snapshot\n\n"
        f"- Canonical CN bank: {manifest['question_count']:,} records across {len(manifest['topic_counts'])} topics; {manifest['published_question_count']:,} practice-payload records.\n"
        f"- {manifest['review_only_excluded_count']} record(s) marked disputed/pending are omitted from practice chunks; source records remain in the canonical bank.\n"
        "- Only the root data-driven portal is the current production candidate; other subjects remain unavailable until their review gates pass.\n"
        f"- Official paper + final-key match: {manifest['verification_counts'].get('paper_and_key_checked', 0)} records in the current evidence register.\n"
        f"- Answer checked: {manifest['verification_counts'].get('answer_checked', 0)}; claimed answer unverified: {manifest['verification_counts'].get('claimed_answer_unverified', 0)}; pending review: {manifest['verification_counts'].get('pending_review', 0)}.\n"
        "- All current exam profiles are practice or suggested-fit mappings, not exact simulations.\n\n"
        "## User-facing changes in this branch\n\n"
        "- Provenance-aware topic chunks, catalog, source register and generated counts.\n"
        "- Accessible responsive navigation and same-tab internal routes.\n"
        "- Source/verification filters, honest language fallbacks, local attempt recovery, deterministic scoring, question review and report-copy flow.\n"
        "- Legacy source files, original PDFs and historical quiz snapshots are preserved.\n\n"
        "## Deployment\n\n"
        "This report is generated on a feature branch. It is not evidence of a merge, GitHub Pages deployment or live-site smoke test.\n"
    )
    (REPORTS / "RELEASE_NOTES.md").write_text(text, encoding="utf-8")


def update_w6_log(build_id, sha, date, statuses):
    path = REPORTS / "W6_IMPORT_LOG.md"
    old = path.read_text(encoding="utf-8") if path.exists() else "# W6 bulk import log\n"
    marker = "\n## Current canonical status (supersedes older rolling snapshot)\n"
    if marker in old:
        old = old.split(marker, 1)[0]
    current = (
        f"{marker}\n"
        f"Bank build ID: `{build_id}`; canonical SHA-256: `{sha}`; snapshot: {date}.\n\n"
        f"- Current `answer_checked`: {statuses.get('answer_checked', 0)}\n"
        f"- Current `paper_and_key_checked`: {statuses.get('paper_and_key_checked', 0)}\n"
        f"- Current `claimed_answer_unverified`: {statuses.get('claimed_answer_unverified', 0)}\n\n"
        f"- Current `disputed`: {statuses.get('disputed', 0)}; current `pending_review`: {statuses.get('pending_review', 0)}\n\n"
        "The W6 import count of 739 is a historical import event, not a current verification count. The older `ok`/`fix` agent verdicts are not official evidence. "
        "Earlier rolling totals that included 26 official-key matches were superseded after review of the community-maintained answer table.\n"
    )
    # Keep the original import log above the historical summary; never rewrite the
    # extraction event itself when regenerating current totals.
    path.write_text(old.rstrip() + "\n" + current, encoding="utf-8")


def main():
    bank = read(BANK)
    manifest = read(BUILD_MANIFEST)
    evidence = read(EVIDENCE)
    exam_doc = read(EXAMS)
    mappings_doc = read(ROOT / "data/catalog/syllabus_mappings.json")
    source_payload = read(ROOT / "assets/source-register.min.json")
    sha = digest(BANK)
    build_id = "cn-" + sha[:16]
    if manifest.get("canonical_sha256") != sha or manifest.get("bank_build_id") != build_id:
        raise SystemExit("site build manifest is stale; run tools/build_site_data.py first")
    generated_on = str(bank.get("generated") or "unknown")
    REPORTS.mkdir(parents=True, exist_ok=True)
    audit_legacy_apps.main()
    exact_groups, near = get_duplicate_data(bank)
    duplicate_summary = {
        "exact_duplicate_group_count": len(exact_groups),
        "near_duplicate_candidate_count": len(near),
        "near_duplicate_reviewed_count": 0,
        "near_duplicate_pending_count": len(near),
    }
    write_inventory(bank, manifest, build_id, sha, generated_on)
    write_duplicate_report(bank, build_id, sha, generated_on, exact_groups, near)
    write_answer_report(bank, build_id, sha, generated_on, evidence)
    write_source_report(bank, build_id, sha, generated_on, evidence, source_payload)
    write_exam_report(build_id, sha, generated_on, exam_doc, mappings_doc, bank)
    write_totals(bank, manifest, build_id, sha, generated_on, duplicate_summary)
    qa_results = read(QA_RESULTS) if QA_RESULTS.exists() else None
    browser_qa = read(BROWSER_QA) if BROWSER_QA.exists() else None
    current_browser_qa = (
        browser_qa
        if browser_qa
        and browser_qa.get("status") == "PASS"
        and browser_qa.get("bank_build_id") == build_id
        and browser_qa.get("canonical_sha256") == sha
        and browser_qa.get("ui_sha256") == ui_fingerprint()
        else None
    )
    pdf_qa = read(PDF_QA) if PDF_QA.exists() else None
    current_pdf_report = current_pdf_qa(pdf_qa)
    write_qa_report(build_id, sha, generated_on, qa_results, current_browser_qa, current_pdf_report)
    write_release_notes(bank, build_id, sha, generated_on, manifest)
    statuses = collections.Counter(q["verification_status"] for q in bank["questions"])
    update_w6_log(build_id, sha, generated_on, statuses)
    print(f"Reports regenerated for {build_id}; total={len(bank['questions'])}; exact={len(exact_groups)}; near={len(near)}.")


if __name__ == "__main__":
    main()
