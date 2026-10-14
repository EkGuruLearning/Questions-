# Answer Verification Report

**Bank build ID:** `cn-014b0aa51c0651e7`<br>
**Canonical SHA-256:** `014b0aa51c0651e77ee8166a9f81a4daeeb0574b75b7abf6e5d72050c46feef0`<br>
**Snapshot date:** 2026-10-14

The `answer_checked` label is a curation-pipeline status, not official paper/final-key matching. A claimed PYQ source and an answer-check status are separate dimensions. No blanket ‘fully verified’ claim is made.

| Verification status | Records | Meaning |
|---|---:|---|
| `paper_and_key_checked` | 0 | Question-level official paper and final/corrected key evidence recorded in the evidence register. |
| `answer_checked` | 847 | Answer-level curation review; does not establish exam provenance or official-key match. |
| `claimed_answer_unverified` | 707 | Source answer or claim is not independently verified for release. |
| `disputed` | 0 | Explicitly disputed; excluded from ordinary reviewed practice. |
| `pending_review` | 2 | Awaiting review. |

## Evidence-gate correction

The 26 records previously labelled `paper_and_key_checked` were downgraded to `claimed_answer_unverified` and `claimed_pyq_unverified`. The checked-in `2024 Programmer Paper-1 ANSWERS.md` is a community-maintained answer table; its README says the answers are based on standard solutions and recommends checking the official key. It is not an official final/corrected key, and no stable question-to-official-key mapping is in the evidence register. The source files were preserved.

## Source-type cross-check

- `verified_official_pyq`: 0
- `claimed_pyq_unverified`: 112
- Source type does not by itself say whether the answer was reviewed.

Evidence register entries: 0. No official record will be accepted without an exact paper, final key and stable question IDs.

Pending content-quality records: CN-T01-0287, CN-T06-0296. At least one answer option is blank; source wording is retained and the records are excluded from public test chunks.
