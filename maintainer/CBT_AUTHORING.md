# All-subject CBT, results and PDF curation

## Scale model

`data/tests/<subject-id>/<test-id>.test.json` is the authoring contract. Adding subjects/tests needs **no player, API or database schema change**. `npm run build:content` generates:

- `data/quizzes/manifest.json`: subject IDs/titles, counts and index paths, **no questions**.
- One immutable `<subject>/index.<hash>.min.json` per subject: test metadata/paths only.
- One immutable `<test>.<hash>.min.json` per test. The browser loads **only the selected subject and test**, never 500 question banks at once.
- `data/banks/cn/topics.json`: 5,006 source bytes / 5,005 minified bytes, instead of fetching the roughly 400 KB full file catalogue to start CN.

The native player is `/subjects/practice/index.html?subject=reasoning&test=series-12`. The current catalogue has **7 starts**: 3 existing CN presets, native RPSC Paper 1, two existing Reasoning samples and a five-question **original practice** IT check. That is not 500 authored tests; the builder test creates **550 definitions across 50 subjects** to verify the scale contract. The Supabase rollback regression independently retains **551 distinct tests/results across 50 subjects**, with RLS and keyset paging.

Native-only subjects appear automatically in the CBT picker/Test Room. Register a subject in `data/catalog/subjects.json` and add `content/<subject>/` files as usual if it should also have a material/folder page. Do not place authoring JSON or provenance notes in the student PDF tree.

## Minimal authoring example

Create `data/tests/new-subject/my-test.test.json`:

```json
{
  "schema_version": 1,
  "id": "my-test",
  "title": "My practice test",
  "subject_title": "New Subject",
  "duration_minutes": 20,
  "note": "Original practice; not an official past-exam paper.",
  "questions": [
    { "text": "How many bits are in an IPv4 address?", "options": ["16", "32", "64", "128"], "answer": ["B"], "explanation": "Four octets of eight bits each." },
    { "text": "Select all transport protocols.", "type": "multiple", "options": ["TCP", "UDP", "HTTP"], "answer": ["A", "B"] },
    { "text": "Enter the decimal value of binary 1011.", "type": "numeric", "answer_range": [11, 11] }
  ]
}
```

Rules:

- ASCII lower-case subject/test slugs, up to 96 characters. Stable IDs should describe a test, not an individual attempt; each completed attempt gets a fresh UUID.
- `single` (default): 2–5 options, answer `['A']`; multiple listed keys are **alternative accepted single choices**, not MSQ.
- `multiple`: answer is the **exact correct set**; no partial credit. Marking is explicitly configurable, not assumed to match every examination.
- `numeric`: inclusive `[minimum, maximum]` range; zero/negative/decimal answers supported. Invalid input counts as unanswered. Bounds are finite, within ±1e12.
- Omit `answer`/`answer_range` to keep an item **ungraded**. Never generate a missing key, OCR text, or official-verification status from guesses. Partial scores exclude unkeyed questions from the denominator; an entirely unkeyed test has null marks, not a fabricated 0%.
- `skip_option: 'E'` is valid **only** for a single-choice source that explicitly defines E as not attempted. E is otherwise an ordinary option.
- `marks` / `negative` can be per question, or `marks` / `negative_marks` at test level (default +1 / −0). Maximum 2,000 questions; `kind: 'paper'` is capped at 300. Total positive/negative marking stays within the API's 30,000 bound.
- Native PDF transcriptions include `source: {pdf: 'content/...pdf', sha256: 'actual source hash', label: 'honest source status'}`. A changed PDF hash stops the build for review. `source_page`, `notice`, `explanation` are optional.
- Question images, if needed, are local `assets/img/questions/<name>.<sha256-first-12>.webp` (or `.png`). The builder checks their actual byte hash, and production caches them immutably. Text/options must still have useful accessible content; do not invent an image's transcription.
- Current RPSC reprint: **98 provided keys**, Q3 conflict/Q5 missing table ungraded. Mixed Reasoning Q6 is ungraded because the stated relationship does not establish R's gender; the old source PDF/key remain unchanged.

Then run `npm run build:content`, `python3 tools/build_quizzes.py --check`, `npm test` and `npm run build`. Normal builds need only Python stdlib, Node 22 and the locked npm dev tools. `tools/import_existing_cbt.py` is an optional reviewable re-import helper; re-importing RPSC needs PyMuPDF, but building/deploying does not.

## Any custom subject player: shared save contract

Every generated page loads `window.EkGuruAccount`. A custom player can use the same journal/sync path:

```js
await window.EkGuruAccount.ready;
const startedOwner = window.EkGuruAccount.user?.id || null; // capture BEFORE Q1
const attemptId = crypto.randomUUID();                    // fresh per attempt
// ...run the test, preserving these values through a resume...
await window.EkGuruAccount.saveAttempt({
  id: attemptId, kind: 'quiz', subject_id: 'new-subject', test_id: 'my-test',
  label: 'My practice test', total: 20, correct: 12, wrong: 3, unanswered: 5,
  score: 12, max_score: 20, duration_seconds: 600,
  completed_at: new Date().toISOString(), details: { version: 1 }
}, startedOwner);
```

Or dispatch `ekguru:test-complete` with `detail: {attempt, owner: startedOwner}`. Do **not** look up the owner only at submission, and never upload guest/another user's old draft into the current session. Tokens/cookies must not go into a payload. The server independently validates and derives the owner from the verified session, not the caller's ID.

History is a summary timeline, not an indefinitely archived full response-sheet viewer. Full current-attempt JSON can be downloaded from the result screen; answered sets over 150 omit answer details from sync. The shared journal is IndexedDB, compound-keyed by owner/attempt UUID. Guest remains local. Pending signed-in results are retained until acknowledgement; the old 20-item outbox is migrated only for its matching signed-in owner. Logout does **not** discard queued results. Browser storage can be cleared/evicted/full; the UI warns on memory-only fallback. A shared browser is not an encrypted multi-user vault.

`GET /api/attempts` accepts `limit` (1–100, default 50), optional `subject_id` / `test_id`, and an opaque `cursor`. It returns `{attempts, next_cursor}`. Ordering is actual `completed_at DESC, id DESC`, preserving PostgreSQL timestamp precision in cursors. Delayed offline uploads do not masquerade as newly completed tests. Local/cloud views, filters, **Load older**, per-source deletion and **Export all matching results** are in My Results. There is no automatic 200-result pruning; provider storage quotas still apply.

## Curated IT PDFs — not an exhaustive archive

Six PDFs (7,965,740 bytes) were added without changing their mirror bytes:

| Exam/year | Format / limitations |
| --- | --- |
| GATE CSE 2012 | 20-page booklet; 65 questions, no digitized key |
| GATE CSE 2016 | 45-page CS-1 + CS-2 bundle with appended keys; MCQ/NAT; parent-tree repair warning |
| GATE CSE 2018 | 26 pages with GA Set-3/CS and appended MCQ/NAT keys |
| GATE CSE 2019 | 19-page scan; no OCR-derived test or invented count/key |
| GATE CSE 2022 | 43 pages, MCQ/MSQ/NAT + key; repairable source xref table |
| ISRO ICRB CSE 2023 Set A | 95 bilingual questions, printed pages **3–47 only**; cover/instructions 1–2 absent |

Exact pinned GitHub commit, blob SHA-1, SHA-256, byte/page counts and source/repair notes are in `data/catalog/imported-papers.json`. All **198 pages** rendered with MuPDF; all six files' first/last pages also rendered with self-hosted PDF.js 4.10.38. These checks establish mirror integrity/readability, **not independently authenticated official archive bytes or a redistribution license**. Rights remain with the exam/content owners; no blanket open-license claim is made.

GATE 1998/2004 candidates with missing-XObject errors, a 2020 coaching solution book, and a web-print candidate were not added. NIC/NIELIT/NET and other exam/year coverage remains incomplete. No claim of “all IT papers” or of converting every PDF to CBT is made.

Use `reader_only: true` for unreviewed scans, combined sessions or mixed-format papers. Their Test Room cards open the reader; they are excluded from the old single-choice response-sheet picker. Leave them readable until a human checks questions, figures, keys and marking. The old PDF/response-sheet tool is opt-in under **Optional tools for older scanned papers**, not the default interface.
