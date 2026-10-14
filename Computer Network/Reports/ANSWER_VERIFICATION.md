# Answer Verification Report (generated 2026-10-14)

This report is deliberately conservative (spec §10): **"answer_checked" means the curation pipeline solved and cross-checked each answer (Forouzan concepts + computed numerics); it is NOT the same as official paper+key matching.** A second-pass human review is still pending. We do NOT claim 100% official verification.

| verification_status | count | meaning |
|---|---|---|
| paper_and_key_checked | 26 | RPSC Programmer 2024 Paper-1 items whose paper + official key are in `Past Papers/` |
| answer_checked | 779 | solved + cross-checked in the curation pipeline; official key not attached |
| pending_review | 0 | none outstanding at export time |

## Evidence files present

- `2024 Programmer Paper-1 ANSWERS.md`
- `2024 Programmer Paper-1 QUESTIONS.md`
- `2024 Programmer Paper-1 SECTION-ANALYSIS.md`
- `README-source.md`
- `RPSC Programmer SYLLABUS.md`
- `Question Banks`
- `Reference Books`
- `RPSC Programmer - Data Communication & CN (PYQ) - source yctfastbook.md`
- `RPSC Programmer 2024 Paper-1`
- `SOURCES.md`

## Known limits

- Claimed-PYQ labels (exam+year strings in source) are exported as `claimed_pyq_unverified` unless a paper+key pair exists in `Past Papers/`.
- Third-party compilations (OCR tests, coaching banks, web banks) are `repository_internal`.
- Practice originals are `original_practice` (textbook-based; not PYQs).
