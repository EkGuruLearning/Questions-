# Source Register & Classification Rules

**Bank build ID:** `cn-014b0aa51c0651e7`<br>
**Canonical SHA-256:** `014b0aa51c0651e77ee8166a9f81a4daeeb0574b75b7abf6e5d72050c46feef0`<br>
**Snapshot date:** 2026-10-14

## Current category counts

| Category | Records |
|---|---:|
| `verified_official_pyq` | 0 |
| `claimed_pyq_unverified` | 112 |
| `repository_internal` | 1205 |
| `textbook_paraphrase` | 42 |
| `original_practice` | 197 |

## Classification and evidence policy

- `verified_official_pyq`: only when a stable question ID maps to an official paper and final/corrected key in `data/sources/official_paper_key_evidence.json`.
- `claimed_pyq_unverified`: a source or citation claims an exam appearance, but official paper/key matching is absent.
- `repository_internal`: repository tests, imported/coaching/OCR sources and other internal/third-party content.
- `textbook_paraphrase`: textbook-derived practice wording; this is not a copied official exam question.
- `original_practice`: original practice written for learning; it is not a PYQ.

`paper_and_key_checked` is the only status that permits an item in Verified PYQ mock mode. `answer_checked` means answer review only.

## Current official-evidence status

Accepted question-level paper+final-key evidence records: **0**.

The RPSC Programmer 2024 source transcription and answer table are community-maintained; the checked-in answer table explicitly recommends official-key verification. It is retained as a citation but does not count as an official final key.

## Exam-tag provenance

| Category | Records |
|---|---:|
| `source_claim_unverified` | 112 |
| `source_label_unverified` | 11 |
| `suggested_practice_fit` | 1433 |

Exam tags are practice filters, not proof of a past appearance. Some tags are source labels; others are difficulty/syllabus-fit suggestions. Exam-name/year labels are marked per question as source claims unless an official evidence record exists.

Public per-source citation records: 279 in `assets/source-register.min.json`. Each question references its source by stable `source_id`.
