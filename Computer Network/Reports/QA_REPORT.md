# QA Report — EkGuru CN release (2026-10-14)

Spec: `Computer Network/new/README.md` §14 (milestone 9–10). This report lists
what was tested, what passed, and what is **not** claimed.

## 1. Files expected by the spec — status

| Spec reference | Status |
|---|---|
| `README.md` (master spec) | present — `Computer Network/new/README.md` |
| `README_CN_QUESTION_BANK.md` | **MISSING** (not on main; recorded, not fabricated) |
| `ARENA_CN_MASTER_EXECUTION_PROMPT.md` | **MISSING** as a separate file; its text is embedded inside `new/README.md` (followed) |
| `Repeater_Ring_Topology_Correction.md` | present — correction applied to the bank |
| `EkGuru_CN_Topic1_Question_Audit.csv` | present — reviewed (151-row Topic-1 starter audit) |
| Original Topic 1 HTML files (two copies) | **MISSING** on main (only `EkGuru_CN_Online_Test_Portal_Updated.html` supplied) |
| `Pasted text (5).txt` | **MISSING** on main |
| 7 Practice Questions PDFs | present (regenerated versions; originals superseded by build pipeline) |
| `EkGuru_CN_Question_Bank_Starter_Package.zip` | present — retained read-only |

Empty placeholders noted: `Computer Network/new/.qqq.md`, `Computer Network/New CN questions`,
`Computer Network/.md` (0 bytes / whitespace) — recorded, not treated as content.

## 2. What was built and tested

| Deliverable | Result |
|---|---|
| `data/cn_questions.json` | **801 records**, spec §6 schema, stable IDs `CN-Tnn-####` |
| Exact-duplicate scan (normalised) | **0 exact groups** (4 found in the first pass were removed; canonical kept) |
| Near-duplicate candidates | 357 listed in `DUPLICATE_AUDIT.md` for manual review (NOT auto-deleted; concept repetition allowed per §9) |
| Answer verification | 26 `paper_and_key_checked` (RPSC Programmer 2024 paper+key in `Past Papers/`), 775 `answer_checked` (pipeline cross-check), **0 silent guesses**; second-pass review pending — we do NOT claim 100% official verification |
| Portal (7 topic HTMLs) | v5 filters + CBT behaviour tests below |
| Blueprints | `EXAM_BLUEPRINTS.md` — GATE-2026 / UGC-NET / RPSC Programmer / RSMSSB IA checked today; **conflicts recorded** (RPSC Q-count & negative rule; IA section split & negative rule) |
| Release ZIP | `EkGuru_CN_Release_2026-10-14.zip` |

## 3. Portal test matrix (manual + automated)

| Test | Method | Result |
|---|---|---|
| JS syntax, all 7 files | `node --check` on extracted `<script>` | PASS 7/7 |
| Metadata + filters present | JSON/HTML structure scan (exam/diff/source/type/lang/marking) | PASS 7/7 |
| Option shuffle keeps key mapped | logic test mirroring `ix.indexOf(ans)`, 2000 random trials | PASS 2000/2000 |
| Unsaved-answer warning on palette jump/prev | `confirm()` guard when `pending` exists in Exam Mode | present (manual click-through pending on device) |
| Quiz-mode feedback on revisit | `renderQ` re-shows feedback for answered questions | fixed & present |
| Timeout auto-submit once | `tickTimer` clears interval before `submitTest(true)` | PASS |
| Unattempted = Skipped, not wrong | result counters | PASS |
| Net mock score under chosen rule | `+pos/−neg` labelled **mock** | PASS |
| Mobile layout | CSS breakpoints 980/640/420 + touch targets | present (device test recommended) |
| Filter-empty handling | alert + no crash | PASS (JS guard) |

## 4. Known limits (never claimed otherwise)

1. **Not all 805→801 answers are officially verified.** 775 are pipeline-checked
   (solved + cross-checked vs Forouzan/computed numerics); official paper+key
   matching exists only for the 26 RPSC Programmer 2024 items.
2. **Near-duplicate review is partial** — 357 candidates need human concept-level
   judgement; numeric variants of the same formula are treated as different
   questions (documented rule).
3. **Exam filters use audited/heuristic tags** — default tags (for unlabelled
   sources) are syllabus-fit suggestions, not authority claims.
4. **Marking presets are mock rules** (labelled in the UI). IA negative marking
   has a three-way source conflict (⅓ vs ¼ vs none) — preset uses ⅓ + "verify".
5. **Sections 2–7 of the supplied booklets had no answer keys** — those answers
   come from the curation pipeline, not from booklet keys.
6. RPSC Programmer Q-count (100 vs 120 per paper) and negative-rule wording
   conflict across sources — verify the official notification before an exact
   simulation claim.
7. indiabix.com (named in the master README) is not reachable here — recorded in
   `SOURCE_REGISTER.md`, not imported.
