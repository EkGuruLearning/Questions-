# EkGuru Learning — repository-backed subject portal

**Work status:** feature branch `arena/cfe67f95-questions`; this change has not been merged or deployed.

**GitHub Pages project URL:** <https://ekgurulearning.github.io/Questions-/> — the live deployment was **not checked** as part of this work. All checked-in internal routes are project-base-safe for `/Questions-/`.

EkGuru presents existing study material as a source-labelled catalogue. The portal distinguishes a live resource collection from a live question bank, and does not promote unresolved source or boundary claims as verified facts.

## Portal routes

- `index.html` — subject catalogue and map preview.
- `subjects/index.html` — all published subjects.
- `subjects/computer-network/index.html` — Computer Network bank, topics, CBTs, booklets, theory, source notes and audit material.
- `subjects/rajasthan-geography/index.html` — existing map, district CSV, metadata and audit resources; **no question bank is published**.
- `maps/index.html` and `maps/rajasthan/index.html` — map catalogue, same-tab full-size PNG action, CSV data and verification notes.
- `practice/index.html` — existing shared Computer Network practice app.
- `study-material/index.html` and `sources/index.html` — resource and source/audit catalogues.
- `guides/repository-structure/index.html` — website-readable English/Hindi file map, topic folder guide and safe repository-merge checklist.

Internal links stay in the current tab. PDFs and external official-source links open a new tab only with a visible label and `rel="noopener noreferrer"`. Full-size map PNGs stay in the current tab so browser Back returns to the previous page.

## Published data snapshot

### Computer Network

- Canonical bank: **1,556** records across seven topics; **1,554** are in the current practice payload.
- Two incomplete pending-review records remain in canonical data and are excluded from practice.
- The official paper + final-key evidence count is **0**. “Answer checked” is not an official-key match; unverified claims stay separately labelled.
- Counts, build ID and SHA-256 are generated from the canonical bank and recorded in `data/reports/build_manifest.json` and the CN reports.

### Rajasthan Geography

- Published as a **resource library**, not a question bank; the catalogue intentionally contains no geography question count or practice-test button.
- `Rajasthan Geography Maps/` and `Geography/Map/Rajasthan/` are distinct source trees with separate READMEs/audits. They have not been merged, moved or rewritten.
- Existing previews, raster exports, CSVs and audit files are linked in place. Boundary, source-vintage and review conflicts stay marked **Needs verification**; see each source audit and `UNRESOLVED_DISCREPANCIES.md` before relying on a map or CSV value.
- `assets/catalog/rajasthan-border-atlas-preview.webp` is an optimized derivative; the original PNG remains unchanged. The source atlas PDFs/GeoPackage are not claimed as included when absent from the tracked repository.

## Catalogue build and validation

The catalogue builder reads real repository files and checked-in manifests. It is read-only with respect to original question banks, PDFs, maps, CSVs and CBT files.

```bash
python3 tools/build_catalog.py
python3 tools/build_catalog.py --check
python3 tools/validate_links.py       # project-base links and new-tab policy
python3 tools/validate_assets.py      # existence, SHA-256, sizes, image metadata
python3 tools/validate_subjects.py   # publication gates and required resources
```

The builder writes `assets/catalog/{subjects,resources,maps}.json`, `data/reports/portal_repository_inventory.csv`, and `Rajasthan Geography Maps/STRUCTURE_AND_ASSET_INVENTORY.md`. Review and regenerate those outputs whenever their source data or tracked resource paths change; do not hand-edit generated catalogue JSON. Editable catalog inputs and add-file examples are documented in [`data/catalog/README.md`](data/catalog/README.md).

To print the repository/site folder map or run the read-only merge preflight, use:

```bash
python3 tools/read_structure.py
python3 tools/read_structure.py --check
```

The website version of this guide is linked in the main navigation at `guides/repository-structure/index.html`.

**Quick placement rule:** new CN study PDFs go in `Computer Network/Topics/TNN/` and must be registered in `data/catalog/books.json` plus the CN `book_ids` list; question-source PDFs go to `Computer Network/Incoming/` for review and are not published automatically. Geography files stay in one of their two audited source trees and new documents/CSVs are registered through `data/catalog/portal_resources.json`. Do not hand-edit files under `assets/catalog/` or combine the geography roots.

To rebuild the existing Computer Network data pipeline after question-source changes, follow `SITE_GUIDE.md` and `Computer Network/README.md`. Do not hand-edit the generated bank chunks or compatibility catalog.

## Tests and release report

Run each Python test group explicitly (the repository does not package `tests/` as a single unittest package):

```bash
python3 -m unittest discover -s tests/data -p 'test_*.py' -v
python3 -m unittest discover -s tests/navigation -p 'test_*.py' -v
python3 -m unittest discover -s tests/responsive -p 'test_*.py' -v
python3 tools/read_structure.py --check
node --test tests/engine/engine.test.mjs
node tests/navigation/app_dom_smoke.cjs  # optional; exit 77 if jsdom is absent
```

Rendered browser QA is optional and has no production/runtime dependency. It requires temporary `playwright-core`, `@sparticuz/chromium`, and `axe-core` packages; see `tests/visual/browser_visual_qa.cjs`. The run recorded for this branch is summarized in `data/reports/portal_qa_report.md`, with machine-readable results in `data/reports/portal_browser_visual_qa.json`. It is headless viewport emulation, not a test on physical devices or a post-deployment smoke test.

The report lists actual checks, scope and anything **NOT TESTED**. This branch has not been merged, and no deployment or live-site behavior is claimed as verified.
