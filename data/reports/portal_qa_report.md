# Subject Portal and Repository Structure — QA Report

**Date:** 2026-10-14 (UTC)

**Branch:** `arena/cfe67f95-questions`

**Overall local result:** **PASS** — 21 release checks passed on the feature branch, including repository-structure/merge preflight.

**Deployment status:** **NOT TESTED** — GitHub Pages production behavior after merge/deployment has not been smoke-tested.

## Scope and catalogue snapshot

The check covers the home catalogue; Computer Network and Rajasthan Geography pages; map, practice, study-material, source and bilingual repository-structure guide routes; project-base links under `/Questions-/`; topic-resource registration/rendering; the shared practice app; generated manifests; and preservation/integrity checks. Unresolved geography claims remain marked for verification. Question content was not manually re-reviewed as part of this portal/structure change.

- **Subjects:** 2 live entries — Computer Network (question bank) and Rajasthan Geography (resource library only).
- **Resources:** 173 repository files; **maps:** 2; **border-data groups:** 7.
- **Computer Network:** 1,556 canonical records, 1,554 in the practice payload, seven topics. Official paper + final-key evidence remains 0; source and answer-verification labels remain distinct.
- **Rajasthan Geography:** no quiz bank or question count is published. `Rajasthan Geography Maps/` and `Geography/Map/Rajasthan/` remain separate; map/boundary previews retain **Needs verification** status.
- **File placement:** new CN topic study PDFs have a documented `Computer Network/Topics/T01`–`T07` convention and catalogue-registration path. New geography add-on resources use `data/catalog/portal_resources.json`; originals are not moved.
- **Generated inventory:** 366 rows in the final tree. Volatile machine-generated QA result JSONs are excluded to avoid self-referential hashes.

## Automated checks

| Check | Result | Observed outcome |
|---|---|---|
| Catalogue build and reproducibility | **PASS** | `tools/build_catalog.py` and `--check`; 2 subjects, 173 resources and 2 map records. |
| Project-base links and tab behavior | **PASS** | 25 HTML pages, 324 references and 320 local links resolved under `/Questions-/`; PDF/external new-tab behavior has safe `rel` attributes and visible labels. |
| Resource/asset integrity | **PASS** | 173 resource paths and hashes checked; 8 map images had readable dimensions/alt text; responsive aspect-ratio checks passed. |
| Subject publication gates | **PASS** | Seven current CN topic routes, 7 practice PDFs, 7 theory PDFs, 7 v6 launchers, two geography map entries and seven CSV-derived border groups. |
| Repository structure merge preflight | **PASS** | `python3 tools/read_structure.py --check` checked for unresolved Git merge entries and verified catalogue freshness, routes, assets, subject gates and whitespace without modifying files. |
| Legacy links and provenance | **PASS** | Strict link audit passed. Seven archived CBT snapshots remain unchanged; current launchers route to the shared practice app. |
| Question-bank data and engine | **PASS** | Canonical/build checks passed; 13 data unit tests and 5 JavaScript engine tests passed. Duplicate audit: 0 exact groups; 748 near-duplicate candidates remain pending review. |
| Navigation and responsive structure | **PASS** | 11 navigation tests and 6 responsive structural tests passed. |
| Practice-app interaction smoke | **PASS** | JSDOM smoke passed for catalogue/topic loading, topic query, mobile navigation, answering, bookmarks, source dialog, scoring/review and filters. JSDOM was temporary; no runtime dependency was added. |
| Rendered browser and accessibility QA | **PASS** | Chromium 153.0.8010.0 headless: **15 viewport profiles × 10 routes = 150 route renders**; no horizontal overflow or browser/network errors. **10 same-tab navigation/back flows** passed. Axe scanned 11 representative states: **0 violations and 0 incomplete checks**. |
| PDF integrity and rendering | **PASS** | Read-only PyMuPDF audit rendered **2,029/2,029 pages across 55 tracked PDFs**; 0 failures, 0 repairs, all source SHA-256 hashes unchanged. |
| Syntax, JSON and whitespace | **PASS** | Python/JavaScript syntax, catalogue JSON, whitespace and `git diff --check` passed. |
| Preservation check | **PASS** | All **341** pre-work tracked paths remain present; **306** are byte-identical to baseline, 35 are intentionally modified, and 0 are missing. All 142 protected source paths (PDFs, geography inputs/audits, canonical CN data and archived CBT snapshots) remain byte-identical. |

Detailed machine results are in [`portal_qa_results.json`](portal_qa_results.json), [`portal_browser_visual_qa.json`](portal_browser_visual_qa.json) and [`portal_pdf_rendering_qa.json`](portal_pdf_rendering_qa.json). Browser screenshots were written under the ignored `.arena/portal-browser-qa/screenshots/` directory; they are not release artifacts.

## Rendered navigation flows

The browser run exercised these same-tab journeys:

1. Home → Computer Network → T01 CBT (preselected) → Back → Computer Network.
2. Home → Rajasthan Geography → full-size A1 PNG → Back → Rajasthan Geography.
3. Maps catalogue → Rajasthan map details → Back → Maps catalogue.
4. Home → Repository File Guide → Back → Home.
5. At 320 px, keyboard focus reached “Skip to content”; the mobile menu opened without overflow and closed after route navigation.

The 15 viewport profiles covered 320, 360, 390, 430, 520, 640, 720, 768, 950, 1024, 1280, 1440 and 1920 CSS pixels, plus phone and tablet landscape. The 640 CSS-pixel viewport models 200% reflow on a 1280 px baseline; browser-chrome/OS zoom controls were not automated. Axe reported zero violations and zero incomplete results in the 11 tested states; manual assistive-technology review is not automated.

## NOT TESTED / remaining limits

- **Production deployment and GitHub Pages live behavior: NOT TESTED.** The branch is not merged or deployed.
- **Physical devices, assistive technology and browser/OS zoom controls: NOT TESTED.** Rendered browser tests are headless viewport emulations.
- **External official-source availability/content: NOT TESTED.** URLs are recorded safely; external pages were not fetched during this integration.
- **Geography source validity, current district boundaries, map authority and CSV interpretation: NOT VERIFIED.** Both source trees retain their own audits and unresolved findings.
- **Manual question/answer correctness and the 748 near-duplicate concepts: NOT TESTED by this portal/structure change.** Existing evidence labels and review queues remain in force.
- PDF rendering QA checks parse/render behavior and byte preservation—not answer correctness, provenance, print quality or PDF/A conformance.

## Reproduction

From the repository root:

```bash
python3 tools/read_structure.py                 # print the folder/data-flow map
python3 tools/build_catalog.py --check
python3 tools/read_structure.py --check          # one-command read-only merge preflight
python3 tools/run_release_checks.py
```

After changing registered source/catalogue data, run the relevant builder first. Browser, JSDOM and PyMuPDF packages used for the recorded QA were temporary; the production portal has no runtime dependency on them.
