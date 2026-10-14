# Source Register & Classification Rules (generated 2026-10-14)

## Classification rules (applied by `tools/cn_export_json.py`)

| source_type | rule |
|---|---|
| verified_official_pyq | source names the exam paper AND `Past Papers/` holds the paper + official key (currently: RPSC Programmer 2024 Paper-1) |
| claimed_pyq_unverified | source string names an exam/year but no paper+key evidence is attached |
| repository_internal | repo unit/subject tests, OCR solutions, coaching/web banks (labels like `Repo:`, `Unit Test`, `InstrumentationTools`, blog banks) |
| textbook_paraphrase | Forouzan/Tanenbaum-style textbook concept labels |
| original_practice | `Practice — original (…)` — newly written, textbook-based |

## Exam-tag rules

Tags come from exam names found in the source string (mapped to profile names). When a source carries no exam name, syllabus-fit default tags are applied by difficulty band: hard → GATE CS / UGC-NET 087 / RPSC Programmer / RPSC ACP-DD; medium → RSMSSB IA / SSC / RPSC Programmer; easy → SSC / RSMSSB IA / JNV TAT. Default tags are a practice-fit suggestion, not an exam-authority claim.

## Primary source families

1. Repo papers in `Computer Network/` (15 Rajasthan exam PDFs — BCI/SCI/RPSC-style; classified by content) — see `Past Papers/SOURCES.md`.
2. `Past Papers/RPSC Programmer 2024 Paper-1/` — questions + official answers + syllabus (evidence for verified labels).
3. `Computer Network/new/` — audit starter pack (20 `computer-networks [set N].pdf` compilations, DCN/Computer-Network-MCQ/networkmcq PDFs, Topic-1 audit CSV, portal HTML, starter ZIP).
4. Forouzan *Data Communications and Networking* — concept verification.
5. Original practice questions (textbook-based) — waves 1–4, `tools/data/practice_new_p*.py`.

## Blocked / not auto-fetchable in this environment

rpsc.rajasthan.gov.in, rssb.rajasthan.gov.in, indiabix.com, testbook, jagranjosh, scribd and most edu sites are not reachable here (allowlist: github/pypi/npm). Papers for those sources must be dropped into `Computer Network/Incoming/` by hand. The master README's link `indiabix.com/networking/questions-and-answers/` is therefore **recorded but not imported**.
