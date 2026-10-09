# 📚 Source Papers & Trusted Sources — Computer Networks (CN)

All question content is **curated from the papers below** (never invented). Reference
book for verification & gap-fill: **Behrouz A. Forouzan — *Data Communications and
Networking***.

> **Network note:** this build environment can only reach `github.com` /
> `registry.npmjs.org` / `pypi.org`. Official **RSSB / RPSC** portals
> (`rssb.rajasthan.gov.in`, `rpsc.rajasthan.gov.in`) and other prep sites are
> **blocked** here, so their PDFs cannot be auto-downloaded. The repo already ships
> **15 Rajasthan exam PDFs** (the primary source). To add more official papers later,
> download them on your machine and **drop them into `Computer Network/Incoming/`** —
> the pipeline will auto-classify & merge them (see `Computer Network/README.md`).

---

## A. Source exam papers already saved in this repo (`Computer Network/`)

These 15 Rajasthan exam PDFs (BCI / SCI / RPSC-Programmer-style coaching papers) are the
**primary question source**. They are bilingual EN+HI MCQ papers; their embedded Hindi
text layer is OCR-garbled, so Hindi is **re-authored** during curation.

| # | File | Content (classified by content) | Feeds topics |
|---|------|----------------------------------|--------------|
| 1 | `CN Topic Test-01.pdf` | UNIT TEST-1 — Networking introduction | T1 (main), T2/T4/T5 |
| 2 | `CN Topic Test-02.pdf` | UNIT TEST-2 — Networking basics, OSI model | **T2 (main)**, T1/T6 |
| 3 | `CN Topic Test-03.pdf` | UNIT TEST-3 — OSI, Addressing (MAC/IP/Port) | **T3 (main)**, T2/T4 |
| 4 | `CN Topic Test-04.pdf` | UNIT TEST-4 — OSI, Physical, Data Link layer | **T5/T6**, T3 |
| 5 | `CN Topic Test 5.pdf` | UNIT TEST-5 — OSI layers detail, addressing | **T6/T3**, T1 |
| 6 | `CN Topic Test  6.pdf` | UNIT TEST-6 — OSI layers detail, devices | **T6 (main)**, T3/T4 |
| 7 | `BCI Subject Test-8.pdf` | OSI, Addressing, Transmission Media, Devices | T2/T4/T5/T6 |
| 8 | `BCI Subject Test-9.pdf` | OSI — Physical/Data Link + Security protocols | T6/T7 |
| 9 | `BCI_SCI Subject Test-01 (CN and Security).pdf` | Intro + **Security** | T1, **T7 (main)** |
| 10 | `BCI_SCI Subject Test-7.pdf` | OSI model, MAC/IP address | T2/T3 |
| 11 | `Random Test- Rajasthan PYQ.pdf` | Rajasthan PYQ (OMR, scanned → OCR) | all topics |
| 12 | `Subject Test Solution -1 (CN & Security).pdf` | **Official answer key** — BCI_SCI ST-01 Q1–25 | verification (T1/T7) |
| 13 | `Subject Test Solution -1 (CN & Security) Part-2.pdf` | **Official answer key** (part 2) | verification |
| 14 | `Unit Test -2 Solutions.pdf` | **Official answer key** — UNIT TEST-2 | verification (T2) |
| 15 | `Unit Test-4 Solution.pdf` | **Official answer key** — UNIT TEST-4 | verification (T5/T6) |

> Repo PDF **page headers are copy-pasted and unreliable** — every question is
> classified by **content** (`tools/cn_taxonomy.py`), never by header.

## B. Additional trusted source (fetched & saved)

| Source | What was captured | File |
|--------|-------------------|------|
| **RPSC Programmer (Paper-I & II) Solved Papers & Practice Book** — YCT Publications (A.K. Mahajan), source: `yctfastbook.com/upload/1726202413_RPSC Pragrammer .pdf` | RPSC Programmer **syllabus — "3. Data Communication and Computer Networks"** (Network Architecture, Circuit/Packet/Message Switching, Network Structure, Physical Layer, Data Link Layer, Framing, Retransmission algorithms, Multiple access & Aloha, CSMA/CD & Ethernet, High Speed LANs & topologies, Broadcast routing & spanning trees, TCP/IP Stack, IP Networks & Internet, DNS & Firewalls, Intrusion Detection & Prevention, Transport layer & TCP/IP, Network Management & Interoperability) + a solved PYQ (sliding-window max window size). | `RPSC Programmer - Data Communication & CN (PYQ) - source yctfastbook.md` |

## C. Exams this question bank serves

Computer Networks / Data Communication is a **common subject** across these Rajasthan
Govt. exams — the same 7-topic structure (with nukta + verification) serves all:

- **RPSC Programmer** (Paper-I: Data Communication & Computer Networks)
- **RSMSSB Informatics Assistant (IA / Suchna Sahayak)**
- **RSMSSB School Administrator (SA)**
- **RSMSSB Data Entry / Computer Operator (DD)**
- **BCI — Basic Computer Instructor**
- **SCI — Senior Computer Instructor**
- **REET (Level 1 / 2 — Computer)**
- **RAS / other Rajasthan Govt. exams**

## D. How to add more papers later

1. Download the PDF (e.g. an RSSB/RPSC previous paper) on your machine.
2. Drop it into **`Computer Network/Incoming/`**.
3. Run `python tools/cn_pipeline.py ingest` (ingests everything in `Incoming/`).
4. Run `python tools/cn_pipeline.py rebuild --all`.
5. New questions appear in each topic PDF under **"Pending Review"** (auto-classified,
   answers to be verified). Curate them into `tools/data/topicN_data.py` and rebuild.

See `Computer Network/README.md` for the full workflow.
