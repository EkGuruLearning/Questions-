# Catalogue source files — read before adding website content

Files in this folder are **editable source inputs**. Browser-facing catalogues under `assets/catalog/` are generated outputs; do not edit those outputs by hand.

| File | Purpose | Website reader / builder |
|---|---|---|
| `subjects.json` | Subject identity, route, status, topics and book IDs. | `tools/build_site_data.py` and `tools/build_catalog.py` |
| `books.json` | Existing and new Computer Network topic PDFs/CBT launchers. Each file needs a stable ID, exact repository path and topic ID. | `tools/build_site_data.py` and `tools/build_catalog.py` |
| `portal_resources.json` | Curated add-on resources that are not CN topic-book entries (for example, a new geography source note or CSV). | `tools/build_catalog.py` |
| `exams.json` | Practice profiles and their recorded source/evidence status. | `tools/build_site_data.py` |
| `syllabus_mappings.json` | Source-labelled exam/syllabus mapping records. | `tools/build_site_data.py` |

## Adding a topic PDF

Use `Computer Network/Topics/T01/` through `T07/` for new topic-specific study files. Add the same record to `books.json` and add its ID to the CN `book_ids` list in `subjects.json`. Example:

```json
{
  "id": "cn-t01-extra-notes",
  "subject_id": "cn",
  "topic_id": "T01",
  "kind": "theory_mcq_pdf",
  "label": "Topic 1 supplementary notes",
  "file": "Computer Network/Topics/T01/extra-notes.pdf",
  "status": "reviewed_resource",
  "note": "Describe the file and its provenance; do not claim official status without evidence."
}
```

Use a unique `id`; `file` must exist and match case exactly. The generated page groups all registered practice/theory resources under the recorded topic. PDF paths are safely encoded for the `/Questions-/` GitHub Pages base.

## Adding another website resource

For a new non-CN-book resource, first place the original under its correct subject/source folder. Add a record to `portal_resources.json`:

```json
{
  "id": "geo-new-audit-note",
  "subject_id": "rajasthan-geography",
  "title": "New source audit",
  "category": "Audit/QA",
  "repo_path": "Rajasthan Geography Maps/reports/NEW_AUDIT.md",
  "source_status": "State what the file does and what it does not prove.",
  "source_status_label": "Source audit · read caveats",
  "source_status_state": "warning",
  "notes": "Keep the source limitations visible on the site."
}
```

Supported current subject IDs are `computer-network` and `rajasthan-geography`. Use the `books.json` path for a CN topic book so it appears on the topic card. New geography map images also need an explicit map record in the map builder and a reviewed alt/caption/status; registering an image as a resource alone does not add it to the map gallery.

## Regenerate and preflight

```bash
python3 tools/build_site_data.py   # after an approved CN bank/catalog source change
python3 tools/build_catalog.py     # rebuild web catalogues and repository inventory
python3 tools/read_structure.py --check
```

Question-bank source changes have their own review/export procedure in `SITE_GUIDE.md` and `Computer Network/README.md`. Do not mark a future subject live by adding a resource row alone.
