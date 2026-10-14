# Computer Network topic-material folders

This folder is the **recommended home for new, topic-specific study files**. Existing PDFs, papers, CBT snapshots and reports stay at their original paths; do not move them just to match this layout.

```text
Computer Network/Topics/
├── README.md
├── T01/    # Introduction of Data Communication
├── T02/    # Network Models: OSI & TCP/IP
├── T03/    # Addressing: MAC, IPv4, IPv6, Ports, DNS
├── T04/    # Networking Devices
├── T05/    # Transmission Medium
├── T06/    # OSI Layers in Detail
└── T07/    # Network Security
```

Create a `TNN/` directory only when there is reviewed material for it. Prefer clear names such as `T01-communication-notes.pdf`; exact case and the repository-relative path matter on GitHub Pages.

## How to make a new file appear on the website

Putting a file in a folder does **not** by itself publish it. For a new Computer Network PDF or notes file:

1. Keep the original file in `Computer Network/Topics/TNN/` (or leave an existing file where it already is).
2. Add a unique record to `data/catalog/books.json` with `subject_id: "cn"`, the correct `topic_id`, a supported `kind` (`theory_mcq_pdf` or `practice_pdf`), and the exact `file` path.
3. Add that record's `id` to the Computer Network `book_ids` array in `data/catalog/subjects.json`.
4. Build and validate the site catalogues from the repository root:

   ```bash
   python3 tools/build_site_data.py
   python3 tools/build_catalog.py
   python3 tools/read_structure.py --check
   ```

The generated catalogue makes the resource available to the Computer Network page and its topic card. PDF links open in a new tab with a visible label. Never hand-edit `assets/catalog/*.json`, `assets/catalog.min.json`, or `assets/banks/cn/*`.

## Question-bank sources are different

New question-source PDFs go to `Computer Network/Incoming/` for the existing ingestion/review workflow. The website does not publish an incoming PDF as approved question content. Curated question records are maintained in `tools/data/topicN_data.py` and flow through the documented CN exporter; review source and answer-verification status before release. Do not create hand-maintained per-topic JSON chunks in this folder.

See `../../guides/repository-structure/index.html` for the complete website/file map and merge preflight.
