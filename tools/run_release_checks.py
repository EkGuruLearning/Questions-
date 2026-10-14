#!/usr/bin/env python3
"""Run the EkGuru release checks and write a machine-readable report.

Report: maintainer/reports/release_checks.json (not published on the website).
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
RESULTS_PATH = ROOT / "maintainer/reports/release_checks.json"
PY = sys.executable
PY_TOOLS = [
    "tools/build_catalog.py",
    "tools/build_site_data.py",
    "tools/validate_site.py",
    "tools/serve_site.py",
    "tools/validate_question_bank.py",
    "tools/check_whitespace.py",
    "tools/read_structure.py",
    "tools/run_release_checks.py",
    "tools/cn_export_json.py",
    "tools/cn_engine.py",
    "tools/cn_taxonomy.py",
    "tools/cn_pipeline.py",
    "tools/cn_textfix.py",
    "tools/cn_difficulty.py",
    "tools/cn_extract.py",
    "tools/cn_ingest_web.py",
    "tools/cn_ocr_cache.py",
    "tools/cn_parse_cnp3.py",
    "tools/cn_parse_ocr.py",
    "tools/cn_build_topic.py",
    "tools/cn_build_practice.py",
    "tools/cn_build_complete.py",
    "tools/cn_build_verify_key.py",
    "tools/audit_duplicates.py",
    "tools/audit_pdfs.py",
    "tools/import_w6_build.py",
    "tools/reconcile_cn_bank.py",
    "tools/read_structure.py",
]
JS_FILES = [
    "assets/js/engine.mjs",
    "assets/js/site.js",
    "assets/js/test.mjs",
    "tests/engine/engine.test.mjs",
    "tests/navigation/site_dom_smoke.cjs",
]

CHECKS = [
    ("Python syntax", [PY, "-m", "py_compile", *dict.fromkeys(PY_TOOLS)],
     "Every builder/validator script compiles."),
    ("Generated data parses as JSON",
     ["bash", "-lc", "for f in data/site.json data/banks/cn/manifest.json data/banks/cn/T0*.min.json "
                     "data/catalog/*.json data/sources/*.json data/schemas/*.json; do "
                     "[ -f \"$f\" ] || continue; python3 -m json.tool \"$f\" >/dev/null || exit 1; done"],
     "Site data, bank manifest, chunks and catalogue JSON are valid."),
    ("Question bank and evidence gate", [PY, "tools/validate_question_bank.py"],
     "Canonical schema v2, hashes, official-evidence gate and chunk coverage."),
    ("Site routes, links and downloads", [PY, "tools/validate_site.py"],
     "No broken links, no .md links, no maintainer links, download hashes match."),
    ("Site data is current", [PY, "tools/build_catalog.py", "--check"],
     "data/site.json matches the registered content and catalogue."),
    ("Bank chunks are current", [PY, "tools/build_site_data.py", "--check"],
     "Generated topic chunks and manifest match the canonical bank."),
    ("Repository structure preflight", [PY, "tools/read_structure.py", "--check"],
     "Required paths, generated data, links and whitespace in one pass."),
    ("Site tests", [PY, "-m", "unittest", "discover", "-s", "tests/site", "-p", "test_*.py", "-v"],
     "Site data integrity, registry wiring and route/anchor checks."),
    ("Navigation and content tests", [PY, "-m", "unittest", "discover", "-s", "tests/navigation", "-p", "test_*.py", "-v"],
     "Page semantics, nav targets, new-tab safety and no-audit-leak rules."),
    ("Responsive structural tests", [PY, "-m", "unittest", "discover", "-s", "tests/responsive", "-p", "test_*.py", "-v"],
     "Viewport, breakpoints and touch-target CSS checks; not rendered visual QA."),
    ("Data pipeline tests", [PY, "-m", "unittest", "discover", "-s", "tests/data", "-p", "test_*.py", "-v"],
     "Canonical bank identity, public chunk fields and preserved snapshots."),
    ("JavaScript syntax", ["bash", "-lc", "for f in " + " ".join(JS_FILES) + "; do node --check \"$f\" || exit 1; done"],
     "Site modules, test app and Node tests parse."),
    ("Engine unit tests", ["node", "--test", "tests/engine/engine.test.mjs"],
     "Filtering, sampling, scoring and language fallbacks."),
    ("Rendered DOM smoke test (optional jsdom)", ["node", "tests/navigation/site_dom_smoke.cjs"],
     "Renders the real pages and asserts topic/material/map lists; exit 77 means jsdom is not installed."),
    ("Whitespace/conflict check", ["bash", "-lc", "git diff --check && git diff --cached --check && python3 tools/check_whitespace.py"],
     "Tracked diffs and changed/untracked text files are checked."),
]


def main() -> int:
    results = []
    for name, command, note in CHECKS:
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        status = "PASS" if result.returncode == 0 else "SKIP" if result.returncode == 77 else "FAIL"
        if result.returncode == 77:
            note += " Skipped in this environment."
        output = (result.stdout + result.stderr).strip().splitlines()
        results.append({
            "name": name,
            "status": status,
            "exit_code": result.returncode,
            "note": note,
            "output_tail": output[-6:],
        })
        print(f"[{status}] {name}")
        for line in output[-4:]:
            print("    " + line)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "command": "python3 tools/run_release_checks.py",
        "summary": {
            "pass": sum(item["status"] == "PASS" for item in results),
            "skip": sum(item["status"] == "SKIP" for item in results),
            "fail": sum(item["status"] == "FAIL" for item in results),
        },
        "checks": results,
        "not_tested": [
            "Real browser rendering, device testing and the live GitHub Pages deployment.",
            "PDF page-by-page rendering (tools/audit_pdfs.py needs PyMuPDF).",
        ],
    }
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"\nsummary: {report['summary']} — report: {RESULTS_PATH.relative_to(ROOT)}")
    return 1 if report["summary"]["fail"] else 0


if __name__ == "__main__":
    sys.exit(main())
