# 📥 Incoming — drop new question PDFs here

To add more questions to the topic-wise bank (e.g. an RSSB/RPSC previous paper,
a textbook question bank, any MCQ PDF):

1. **Copy the PDF into this folder** (`Computer Network/Incoming/`).
2. Run:
   ```bash
   python tools/cn_pipeline.py ingest        # ingests everything in this folder
   python tools/cn_pipeline.py rebuild --all # rebuild all topic PDFs
   ```
3. Open the rebuilt topic PDF — new questions appear under
   **"Pending Review — needs verification"** (auto-classified into the right topic by
   content, de-duplicated).
4. Verify them (correct answer + nukta + Hindi + option-wise verification) and move them
   into `tools/data/topicN_data.py`, then rebuild again.

The extractor reads clean **English** MCQs (question + 4 options) and drops the garbled
Hindi (Hindi is re-authored during curation). Scanned PDFs are handled via OCR
(RapidOCR). Supported option-label styles: `(a) (A) a) a. A) A.` and `(1) (2) 1. 2.`.

You can also ingest a specific file/folder without dropping it here:
```bash
python tools/cn_pipeline.py ingest --pdf path/to/file.pdf
python tools/cn_pipeline.py ingest --dir path/to/folder
```
