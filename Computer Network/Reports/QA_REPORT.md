# QA Report — Current Portal Build

**Bank build ID:** `cn-014b0aa51c0651e7`<br>
**Canonical SHA-256:** `014b0aa51c0651e77ee8166a9f81a4daeeb0574b75b7abf6e5d72050c46feef0`<br>
**Snapshot date:** 2026-10-14

> **Scope note:** This report preserves the earlier Computer Network bank/release QA record. Its `data/reports/browser_visual_qa.json` and rendered-browser section cover the pre-catalog portal UI, not the new subject/map routes. Current portal validation is recorded separately in [`data/reports/portal_qa_report.md`](../../data/reports/portal_qa_report.md) and [`data/reports/portal_browser_visual_qa.json`](../../data/reports/portal_browser_visual_qa.json). Neither report claims a deployment check.

## Recorded automated results

| Check | Result | Command | Notes |
|---|---|---|---|
| Python syntax | **PASS** | `python3 -m py_compile tools/cn_export_json.py tools/reconcile_cn_bank.py tools/build_site_data.py tools/build_reports.py tools/audit_duplicates.py tools/audit_links.py tools/audit_blueprints.py tools/validate_question_bank.py tools/build_v6_launchers.py tools/retire_legacy_apps.py tools/audit_legacy_apps.py tools/inert_archived_html.py tools/audit_pdfs.py tools/check_whitespace.py tools/run_release_checks.py` | All release/build/audit Python scripts compile. |
| Catalog and schema JSON | **PASS** | `bash -lc 'for f in data/catalog/*.json data/sources/*.json data/schemas/*.json assets/catalog.min.json assets/banks/cn/manifest.json assets/source-register.min.json data/reports/build_manifest.json data/reports/browser_visual_qa.json data/reports/pdf_rendering_qa.json; do python3 -m json.tool "$f" >/dev/null \|\| exit 1; done'` | Catalog, evidence, schemas and generated manifests parse as JSON. |
| Canonical and generated-data validation | **PASS** | `python3 tools/validate_question_bank.py` | Canonical v2, hashes, official evidence gate, chunks and source references. |
| Exam profile and mapping audit | **PASS** | `python3 tools/audit_blueprints.py` | Profiles/mappings validated; none claims an exact simulation. |
| Legacy app provenance audit | **PASS** | `python3 tools/audit_legacy_apps.py` | Seven archived snapshots checked for embedded stale official labels; public paths must redirect. |
| Static links and new-tab safety | **PASS** | `python3 tools/audit_links.py --strict` | Root page, legacy pages, v6 launchers, catalog book files and topic chunks. |
| Duplicate scan | **PASS** | `python3 tools/audit_duplicates.py --check` | Exact and near-duplicate scan; reports candidates without auto-merging. |
| Data unit tests | **PASS** | `python3 -m unittest discover -s tests/data -p 'test_*.py' -v` | Canonical integrity, source gates, payloads, catalog and preserved files. |
| Navigation unit tests | **PASS** | `python3 -m unittest discover -s tests/navigation -p 'test_*.py' -v` | Anchors, explicit buttons, mobile navigation semantics and safe links. |
| Responsive structural tests | **PASS** | `python3 -m unittest discover -s tests/responsive -p 'test_*.py' -v` | Viewport, breakpoint and touch-target CSS checks; not rendered visual QA. |
| JavaScript syntax | **PASS** | `bash -lc 'node --check assets/js/engine.mjs && node --check assets/js/app.mjs && node --check tests/engine/engine.test.mjs && node --check tests/navigation/app_dom_smoke.cjs && node --check tests/visual/browser_visual_qa.cjs'` | Engine, application module and Node tests parse. |
| Portal interaction smoke (optional JSDOM) | **PASS** | `node tests/navigation/app_dom_smoke.cjs` | Catalog-first loading, topic-only fetch, nav, answer feedback, bookmark, source dialog, scoring/review and filters; exit 77 means jsdom is not installed. JSDOM was available in this test environment; the production portal has no npm runtime dependency. |
| Engine unit tests | **PASS** | `node --test tests/engine/engine.test.mjs` | Filtering, opt-in status, deterministic sampling, scoring and language fallbacks. |
| Rendered browser visual and accessibility QA (pre-catalog UI snapshot) | **PASS · HISTORICAL SCOPE** | Recorded in `data/reports/browser_visual_qa.json` | The 320×780, 375×812, 768×1024 and 1365×900 run predates the new subject/map routes. It is not current route QA; see `data/reports/portal_qa_report.md` for the current 15-viewport/135-route run. |
| PDF validity and rendering audit (optional PyMuPDF) | **PASS** | `python3 tools/audit_pdfs.py` | Read-only parse and render of every page in each tracked PDF with pre/post SHA-256 preservation checks; exit 77 means PyMuPDF is unavailable. PyMuPDF 1.28.2; PDFs=55; pages rendered=2029/2029; repaired=0; hashes unchanged=True. |
| Whitespace/conflict check | **PASS** | `bash -lc 'git diff --check && git diff --cached --check && python3 tools/check_whitespace.py'` | Tracked diffs and changed/untracked text files are checked; preserved archive bytes are excluded. |

## Earlier rendered-browser result — historical UI only

**Historical pass** — Chromium 153.0.8010.0 (headless) at 320×780, 375×812, 768×1024 and 1365×900. This is retained as a record for the pre-catalog UI. It is not evidence about the new subject, map, study-material or source routes; current checks are in `data/reports/portal_qa_report.md`.

The earlier screenshots were headless viewport emulations, not tests on physical devices.

## Original PDF validity and rendering QA

**PASS** — 55 tracked PDFs; 2,029/2,029 pages rendered; 0 files repaired by MuPDF; 0 failed files. Original sizes and SHA-256 hashes unchanged: **True**.

This validates file opening, page-tree loading and rendering—not question/answer correctness, source provenance, print quality, or PDF/A conformance.

## Scope and limitations

- The shared Computer Network practice app loads a small catalog and content-hashed topic chunks; the new subject catalogue is documented and checked separately.
- Legacy topic HTML snapshots were inspected separately; they are retained as historical artifacts and must not be presented as current verification-gated apps.
- The pre-change GitHub Pages source was fetched during the earlier bank audit, before this catalogue redesign. No current deployment or post-deployment live smoke test was performed.
