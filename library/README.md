# Licensed reading source checkpoint — NOT published student pages

**Status, 2026-10-17:** source collection only. The existing website remains the previously tested CBT/results platform. The requested subject-only homepage, expanded syllabus/topic navigation, student reading renderer and additional subject tests have **not** been implemented in this checkpoint. Do not represent this collection as complete syllabus coverage or 200 independently reviewed websites.

## What is actually included

- **385 English teaching chapters from nine repositories**, 4,208,898 source-Markdown bytes.
- **669 distinct Rust listing/include files** retained as data for a future reader. Some are HTML examples; they must never be discovered/published as standalone student pages.
- Exact source bytes, reviewed commit/tree pins, Git blob SHA-1, SHA-256, byte counts, source path and preliminary subject/unit classification in `catalog.json`.
- All applicable source license/copyright notices, referenced by exact path and hash in the catalogue. The eight MIT-licensed collections (including the MIT option of Rust's dual license) and the CC0-licensed Security-101 collection are identified separately.
- No third-party image/video binaries, datasets, paid articles, login-protected material or GeeksforGeeks article copies were imported. Embedded links/captions in source text do not grant redistribution rights over their external targets.

| Source | Chapters | Notice |
| --- | ---: | --- |
| Microsoft Web Dev for Beginners | 25 | MIT |
| Microsoft ML for Beginners | 27 | MIT |
| Microsoft Data Science for Beginners | 25 | MIT |
| Microsoft AI for Beginners | 28 | MIT |
| Microsoft IoT for Beginners | 23 | MIT |
| Microsoft Generative AI for Beginners | 22 | MIT |
| Microsoft Security-101 | 24 | CC0-1.0 |
| The Rust Programming Language book | 101 | MIT option; copyright retained |
| Oleksii Trekhleb's JavaScript Algorithms | 110 | MIT |

The catalogue classifies these readings into **20 preliminary subject buckets**. This is not 40 finished subject courses, and it adds no new native quizzes yet. Optional exercises in the upstream courses may require hardware, accounts or billed cloud services; importing readable text does not activate or promise those services for free.

## Reproduce / verify

Ordinary `npm run build` does **not** fetch or execute these sources. The production export excludes `library/`; source HTML examples are explicitly excluded from published-route discovery. The dev server also denies that root.

```sh
python3 -m unittest discover -s tests/data -p 'test_open_course_import.py' -v
```

For an intentional, reviewed refresh with the already-configured GitHub connection:

```sh
python3 tools/import_open_courses.py --import-reviewed
```

The importer uses committed pins when its ignored API/blob cache is absent, rechecks tree identity, source bytes and licenses, and never runs repository scripts or source examples. No credentials belong in this directory.

## Publication still to do

1. Review the preliminary subject/unit mapping against the selected exam syllabus; identify missing topics honestly.
2. Build an offline, sanitized student reader. Preserve code and mathematical notation, resolve the pinned Rust include markers, and handle external media as clearly labelled links unless separate rights/size checks permit local copies.
3. Show attribution and the applicable notice with every published reading. Do not apply an imported license to pre-existing papers or other repository material.
4. Add subject-folder-only home navigation and a dedicated searchable test section without replacing/removing existing PDFs, CN questions, CBT or results.
5. Author and review genuinely original topic checks; distinguish short checks from complete official past papers/mocks.
6. Validate mobile layout, links, payload sizes and actual browser compression before claiming this expansion is live or complete.

## Security exclusion

One upstream IoT tutorial contained a credential-looking example connection string. It was omitted after GitHub push protection rejected it; no unblock/override was used. The filename and exclusion reason (never the value) are recorded in the catalogue/importer. All retained chapters remain byte-exact.
