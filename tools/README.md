# Repository tools

## Computer Network question-bank tools

Small, dependency-light Python tools turn the CN source modules and exam-paper PDFs into the topic-wise question books in `Computer Network/`. Full CN workflow documentation: **`Computer Network/README.md`**.

| File | Role |
|------|------|
| `cn_taxonomy.py` | Seven topics, sub-topics, keywords, exam list and content-based `classify()` |
| `cn_extract.py` | PDF → clean English MCQs (PyMuPDF text; RapidOCR fallback for scans) |
| `cn_pipeline.py` | Ingest → classify → deduplicate → merge → rebuild |
| `cn_engine.py` | Render a topic's data → bilingual PDF (PyMuPDF Story, HarfBuzz shaping) + Markdown |
| `cn_build_topic.py` | Build one/all topic PDF+MD from `data/topicN_data.py` |
| `data/topicN_data.py` | Curated question source modules |
| `data/topicN_pending.py` | Auto-ingested questions needing verification |

```bash
python tools/cn_build_topic.py 2
python tools/cn_build_topic.py --all
python tools/cn_pipeline.py ingest
python tools/cn_pipeline.py rebuild --all
python tools/cn_pipeline.py status
python tools/cn_pipeline.py ingest --pdf path/to/file.pdf
python tools/cn_pipeline.py ingest --dir path/to/folder
```

Requirements: `pymupdf`; for OCR of scanned PDFs, `rapidocr-onnxruntime` and `opencv-python-headless`. Fonts are bundled in `tools/fonts/`.

## Subject portal catalogue and validators

- `build_catalog.py` generates `assets/catalog/{subjects,resources,maps}.json`, a repository inventory CSV, and a geography asset inventory Markdown file from existing checked-in files. It does not edit or move original source materials.
- `read_structure.py` prints the bilingual website/file map in the terminal; `--check` is a read-only merge preflight for unresolved Git conflicts, generated catalogue freshness, project-base links, assets, publication gates and whitespace.
- `data/catalog/portal_resources.json` is the editable registry for curated non-CN-book add-on resources. `data/catalog/books.json` remains the topic/PDF registration source for Computer Network.
- `validate_links.py` resolves local routes under the GitHub Pages `/Questions-/` project base and checks fragments, safe new-tab configuration and generated manifest paths.
- `validate_assets.py` checks catalogue path availability, file sizes/SHA-256, map-image dimensions/alt text and responsive aspect-ratio rules.
- `validate_subjects.py` enforces live-subject/resource publication gates, current topic routes, PDF behavior and the geography “resource library, no question bank” status.

```bash
python3 tools/build_catalog.py
python3 tools/build_catalog.py --check
python3 tools/validate_links.py
python3 tools/validate_assets.py
python3 tools/validate_subjects.py
python3 tools/read_structure.py
python3 tools/read_structure.py --check
```

The portal itself has no server-side or npm runtime dependency. See `SITE_GUIDE.md` and `data/reports/portal_qa_report.md` for data-preservation rules, tests and release scope.
