#!/usr/bin/env python3
"""Run reproducible release checks and record real exit statuses for QA_REPORT."""
from __future__ import annotations
import json
import pathlib
import shlex
import subprocess
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
RESULTS_PATH = ROOT / "data/reports/qa_results.json"
CHECKS = [
    ("Python syntax", ["python3", "-m", "py_compile", "tools/cn_export_json.py", "tools/reconcile_cn_bank.py", "tools/build_site_data.py", "tools/build_reports.py", "tools/audit_duplicates.py", "tools/audit_links.py", "tools/audit_blueprints.py", "tools/validate_question_bank.py", "tools/build_v6_launchers.py", "tools/retire_legacy_apps.py", "tools/audit_legacy_apps.py", "tools/inert_archived_html.py", "tools/audit_pdfs.py", "tools/check_whitespace.py", "tools/run_release_checks.py"], "All release/build/audit Python scripts compile."),
    ("Catalog and schema JSON", ["bash", "-lc", "for f in data/catalog/*.json data/sources/*.json data/schemas/*.json assets/catalog.min.json assets/banks/cn/manifest.json assets/source-register.min.json data/reports/build_manifest.json data/reports/browser_visual_qa.json data/reports/pdf_rendering_qa.json; do python3 -m json.tool \"$f\" >/dev/null || exit 1; done"], "Catalog, evidence, schemas and generated manifests parse as JSON."),
    ("Canonical and generated-data validation", ["python3", "tools/validate_question_bank.py"], "Canonical v2, hashes, official evidence gate, chunks and source references."),
    ("Exam profile and mapping audit", ["python3", "tools/audit_blueprints.py"], "Profiles/mappings validated; none claims an exact simulation."),
    ("Legacy app provenance audit", ["python3", "tools/audit_legacy_apps.py"], "Seven archived snapshots checked for embedded stale official labels; public paths must redirect."),
    ("Static links and new-tab safety", ["python3", "tools/audit_links.py", "--strict"], "Root page, legacy pages, v6 launchers, catalog book files and topic chunks."),
    ("Duplicate scan", ["python3", "tools/audit_duplicates.py", "--check"], "Exact and near-duplicate scan; reports candidates without auto-merging."),
    ("Data unit tests", ["python3", "-m", "unittest", "discover", "-s", "tests/data", "-p", "test_*.py", "-v"], "Canonical integrity, source gates, payloads, catalog and preserved files."),
    ("Navigation unit tests", ["python3", "-m", "unittest", "discover", "-s", "tests/navigation", "-p", "test_*.py", "-v"], "Anchors, explicit buttons, mobile navigation semantics and safe links."),
    ("Responsive structural tests", ["python3", "-m", "unittest", "discover", "-s", "tests/responsive", "-p", "test_*.py", "-v"], "Viewport, breakpoint and touch-target CSS checks; not rendered visual QA."),
    ("JavaScript syntax", ["bash", "-lc", "node --check assets/js/engine.mjs && node --check assets/js/app.mjs && node --check tests/engine/engine.test.mjs && node --check tests/navigation/app_dom_smoke.cjs && node --check tests/visual/browser_visual_qa.cjs"], "Engine, application module and Node tests parse."),
    ("Portal interaction smoke (optional JSDOM)", ["node", "tests/navigation/app_dom_smoke.cjs"], "Catalog-first loading, topic-only fetch, nav, answer feedback, bookmark, source dialog, scoring/review and filters; exit 77 means jsdom is not installed."),
    ("Engine unit tests", ["node", "--test", "tests/engine/engine.test.mjs"], "Filtering, opt-in status, deterministic sampling, scoring and language fallbacks."),
    ("Rendered browser visual and accessibility QA (optional)", ["node", "tests/visual/browser_visual_qa.cjs"], "Headless Chromium screenshots, viewport overflow, 44px controls and axe checks; exit 77 means browser packages are unavailable."),
    ("PDF validity and rendering audit (optional PyMuPDF)", ["python3", "tools/audit_pdfs.py"], "Read-only parse and render of every page in each tracked PDF with pre/post SHA-256 preservation checks; exit 77 means PyMuPDF is unavailable."),
    ("Whitespace/conflict check", ["bash", "-lc", "git diff --check && git diff --cached --check && python3 tools/check_whitespace.py"], "Tracked diffs and changed/untracked text files are checked; preserved archive bytes are excluded."),
]


def main():
    checks = []
    for name, command, note in CHECKS:
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        output = (result.stdout + result.stderr).strip()
        check_result = "PASS" if result.returncode == 0 else "SKIP" if result.returncode == 77 else "FAIL"
        check_note = note
        if name == "Portal interaction smoke (optional JSDOM)":
            if result.returncode == 0:
                check_note += " JSDOM was available in this test environment; the production portal has no npm runtime dependency."
            elif result.returncode == 77:
                check_note += " JSDOM was absent, so this interaction smoke was skipped."
        if name == "Rendered browser visual and accessibility QA (optional)":
            if result.returncode == 0:
                browser_report = json.loads((ROOT / "data/reports/browser_visual_qa.json").read_text(encoding="utf-8"))
                check_note += f" {browser_report['browser']}; viewports: " + ", ".join(f"{item['width']}×{item['height']}" for item in browser_report["viewports"]) + f"; axe violations={browser_report['total_axe_violations']}."
            elif result.returncode == 77:
                check_note += " Browser packages were absent, so rendered visual QA was skipped."
        if name == "PDF validity and rendering audit (optional PyMuPDF)":
            if result.returncode == 0:
                pdf_report = json.loads((ROOT / "data/reports/pdf_rendering_qa.json").read_text(encoding="utf-8"))
                check_note += f" {pdf_report['tool']}; PDFs={pdf_report['tracked_pdf_count']}; pages rendered={pdf_report['total_pages_rendered']}/{pdf_report['total_pages']}; repaired={pdf_report['mupdf_repaired_files']}; hashes unchanged={pdf_report['all_source_hashes_unchanged']}."
            elif result.returncode == 77:
                check_note += " PyMuPDF was absent, so PDF parse/render QA was skipped."
        checks.append({
            "name": name,
            "command": shlex.join(command),
            "exit_code": result.returncode,
            "result": check_result,
            "notes": check_note,
            "output_tail": output[-6000:],
        })
        print(f"{check_result}: {name}")
        if output:
            print(output)
    build_manifest = json.loads((ROOT / "data/reports/build_manifest.json").read_text(encoding="utf-8"))
    report = {
        "schema_version": 1,
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "bank_build_id": build_manifest["bank_build_id"],
        "canonical_sha256": build_manifest["canonical_sha256"],
        "checks": checks,
        "browser_visual_qa": next((check["notes"] for check in checks if check["name"] == "Rendered browser visual and accessibility QA (optional)"), "NOT_RUN"),
        "pdf_rendering": next((check["notes"] for check in checks if check["name"] == "PDF validity and rendering audit (optional PyMuPDF)"), "NOT_RUN"),
        "deployment": "NOT_PART_OF_LOCAL_QA_RUN: checks ran on the feature branch; this report does not include a deployment or post-deployment smoke test.",
    }
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    failed = [check for check in checks if check["exit_code"] not in (0, 77)]
    print(f"Recorded {len(checks)} check results in {RESULTS_PATH.relative_to(ROOT)}; failures={len(failed)}")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
