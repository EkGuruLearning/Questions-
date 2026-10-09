# 🛠️ tools/ — the CN question-bank system

Small, dependency-light Python tools that turn exam-paper PDFs into the 7 topic-wise
bilingual MCQ books in `Computer Network/`. Full docs: **`Computer Network/README.md`**.

| File | Role |
|------|------|
| `cn_taxonomy.py` | 7 topics + sub-topics + keywords + exam list + content-based `classify()` |
| `cn_extract.py`  | PDF → clean English MCQs (pymupdf text; RapidOCR fallback for scans) |
| `cn_pipeline.py` | **auto-update engine**: ingest → classify → dedupe → merge → rebuild |
| `cn_engine.py`   | renders a topic's data → bilingual PDF (PyMuPDF Story, HarfBuzz shaping) + Markdown |
| `cn_build_topic.py` | build one/all topic PDF+MD from `data/topicN_data.py` |
| `data/topicN_data.py` | curated, verified questions (source of truth) |
| `data/topicN_pending.py` | auto-ingested, needs-verification questions |
| `fonts/` | bundled fonts (Noto Sans Devanagari + DejaVu Sans) |

## Commands
```bash
# build a topic (or all) from curated data
python tools/cn_build_topic.py 2
python tools/cn_build_topic.py --all

# auto-update: drop PDFs in Computer Network/Incoming/, then
python tools/cn_pipeline.py ingest
python tools/cn_pipeline.py rebuild --all
python tools/cn_pipeline.py status

# ingest a specific file/folder
python tools/cn_pipeline.py ingest --pdf path/to/file.pdf
python tools/cn_pipeline.py ingest --dir path/to/folder
```

## Requirements
`pymupdf`; for OCR of scanned PDFs also `rapidocr-onnxruntime` + `opencv-python-headless`.
Fonts are bundled in `tools/fonts/`.
