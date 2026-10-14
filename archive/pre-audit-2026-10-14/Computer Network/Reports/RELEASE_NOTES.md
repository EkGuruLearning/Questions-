# EkGuru CN — Release 2026-10-14

**Compiled & updated by PRAKASH • EkGuru Learning** — following the master
execution prompt in `Computer Network/new/README.md`.

## What is in this release
- **Working portal:** 7 topic-wise offline CBT apps (`Online Quiz/`), v5 —
  exam/difficulty/source-status/question-type/language/marking filters with
  audited tags, real CBT navigation (palette + hide-show, Save & Next with
  authentic save rule, mark-for-review, unsaved-answer warning), mobile-first
  layout, per-question Source (exam/year) chips, Correct/Wrong/Skipped analysis,
  net mock score, question-wise solutions.
- **Normalized bank:** `data/cn_questions.json` — 801 records (spec §6 schema),
  stable IDs; 0 exact duplicate groups (4 removed after audit; canonical kept).
- **Reports:** INVENTORY, DUPLICATE_AUDIT (357 near-candidates for review),
  ANSWER_VERIFICATION (26 paper+key checked / 775 pipeline-checked — no
  overclaims), SOURCE_REGISTER (classification rules + evidence + blocked sites),
  EXAM_BLUEPRINTS (GATE-2026 / NET / RPSC Programmer / RSMSSB IA — conflicts
  recorded), QA_REPORT (this folder).
- **Books:** 7 topic books (627 MCQ + 165 rapid), Complete Book (216 pp),
  7 practice booklets (801 Q, 80 pp) — all rebuilt after dedupe + language fixes.
- **Repeater/ring-topology correction** applied (concept-check, not a PYQ).

## Change log
### 2026-10-14 — release R1
- Imported the main-branch starter pack (`new/`) read-only; missing spec files recorded.
- Repeater question corrected (traditional-ring wording, answer Ring).
- 4 exact duplicate stems removed (ARPANET ×2; Client-Server cross-topic;
  DNS reverse-lookup claimed twin; digital-modulation twin).
- 97 Hindi-in-English-slot explanations given English (earlier round, retained).
- Portal v5 filters + net mock score + unsaved warning + quiz-feedback-on-revisit.
- Honest source-status labels; "all answers verified" startup claim removed.

## Remaining / next
- Second-pass answer review (human) for the 775 pipeline-checked items.
- Manual near-duplicate review of the 357 candidates.
- Import `computer-networks [set 1–20]` PDFs + the 3 MCQ PDFs as new source waves
  (after per-question dedupe + answer verification).
- Website build (login + real-time monitoring) — user's future plan.
