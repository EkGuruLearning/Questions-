# EkGuru Learning — source-labelled practice portal

**Production site:** https://ekgurulearning.github.io/Questions-/
**Branch status:** this implementation is on `arena/bc406676-questions`; it has not been merged or deployed. The production link above still serves the pre-audit site until a reviewed release is published.

EkGuru currently has one published subject bank: **Computer Networks**. The canonical bank contains 1,556 records across seven topics. The portal separates question source type from answer-verification status and does not claim that the whole bank is official, fully bilingual, or fully verified.

## Current data snapshot

- Canonical records: **1,556** — T01 375, T02 144, T03 231, T04 99, T05 174, T06 387, T07 146.
- Practice payload: **1,554**. Two incomplete records have blank options, are labelled `pending_review`, and remain in the canonical file but are omitted from test chunks.
- Official paper + final-key checked: **0**. The question-level evidence register is empty.
- Answer checked: **847** (answer review, not official-key matching).
- Claimed answer unverified: **707**; disputed: **0**; pending review: **2**.
- Source types: 112 claimed PYQs (unverified), 1,205 repository/internal, 42 textbook paraphrases, 197 original practice, 0 verified official PYQs.
- **817 records** meet the field-based full-bilingual condition. Missing Hindi fields are shown with an explicit English-fallback notice.
- Exact normalized English-stem duplicate groups: **0**. **748 near-duplicate candidates remain pending manual concept review**; none was auto-merged or deleted by this audit.

Counts and the current SHA-256 / build ID are in `Computer Network/Reports/INVENTORY.md` and `data/reports/build_manifest.json`.

## What the portal does

- Loads a small generated catalog and then only the selected, content-hashed topic chunk(s); it does not fetch the monolithic compatibility bank on page load.
- Supports topic, exam/practice-tag, answer-verification, source-type, heuristic-difficulty, question-count and language filters.
- Defaults to answer-checked records. Unverified claimed-answer practice requires an explicit opt-in filter; disputed and pending records cannot start a test.
- Provides learn feedback, user-configured timed practice, question navigation, marking, local bookmarks, answer review, retry of incorrect answers, and a local copyable result summary.
- Keeps attempt history and saved questions in browser local storage only. No sign-in, analytics, ads, cloud sync, push or email notifications are added.
- Shows planned subjects as unavailable. No unfinished subject is marked live.

Exam labels are sources or practice-fit suggestions, not proof of an exam appearance. No exact exam simulation or official timing/marking claim is enabled. The UGC-NET draft no longer uses an answer-key page as a pattern URL; current-cycle pattern verification remains open.

## Repository map

```text
index.html                              accessible data-driven portal shell
assets/css/portal.css                   responsive site styles
assets/js/app.mjs                       client UI, local state and lazy chunk loading
assets/js/engine.mjs                    pure filtering, sampling, localization and scoring
Computer Network/data/cn_questions.json canonical CN source, schema v2
assets/catalog.min.json                 generated subject/exam/library catalog
assets/banks/cn/manifest.json           generated counts and topic chunk manifest
assets/banks/cn/Tnn.<hash>.min.json     generated public topic chunks
assets/source-register.min.json         generated public citation register
assets/cn-questions.min.json             generated compatibility payload; not fetched by portal
 data/catalog/                           subject, exam, mapping and book drafts
 data/sources/official_paper_key_evidence.json  question-level official evidence gate
 data/schemas/                           canonical/public/evidence JSON schemas
tools/cn_export_json.py                 rebuild canonical bank and downstream data
 tools/build_site_data.py                generate catalog, assets and build manifest
 tools/build_reports.py                  regenerate reports and duplicate queue
tests/                                   data, engine, navigation and responsive checks
archive/pre-audit-2026-10-14/            preserved pre-change page, asset and report snapshots
```

All original PDFs remain in their original paths. The seven legacy HTML snapshots are preserved byte-for-byte as inert `.html.snapshot` files under `archive/pre-audit-2026-10-14/Computer Network/Online Quiz/`; their former public paths now redirect to the shared portal because their embedded official labels predate the evidence correction. New `Online Quiz/v6/` links are topic launchers into the shared portal.

## Rebuild and release checks

From the repository root, after editing the source question modules or catalog drafts:

```bash
python3 tools/cn_export_json.py
python3 tools/run_release_checks.py
python3 tools/build_reports.py  # refresh QA_REPORT.md from the recorded test results
```

`cn_export_json.py` regenerates the canonical JSON, topic chunks, catalog, source register, manifest and report set. Do not hand-edit generated `assets/` files. The migration tool `tools/reconcile_cn_bank.py` is for schema/provenance normalization; it is not a substitute for reviewing source content.

The published PDFs are preserved historical materials. No PDF is regenerated by the portal build. Before deployment, repeat the data/link/test checks, perform rendered phone/tablet/laptop and keyboard checks in a real browser, inspect any PDF that is intentionally changed, and verify the production site after release. See `Computer Network/Reports/QA_REPORT.md` for actual recorded results and limitations.
