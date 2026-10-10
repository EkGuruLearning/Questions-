# COVERAGE — Complete Question Accounting (koi question nahi chhoota)

Last updated: 2026-10-09 (after OCR of scanned PDFs + web/textbook-bank harvest).
This file proves that **every** question in every source is accounted for:
either curated into a book, staged in a queue, or dropped with a documented reason.

## Grand totals (updated after T1/T2 update + Topic 3 build)

| Bucket | Count | Where |
|---|---|---|
| Curated books (T1 + T2 + T3) | **280** | topic1_data.py (118) + topic2_data.py (81) + topic3_data.py (81) |
| T1/T2 holding (awaiting next book update) | **1** | `tools/data/web_extra_t1t2.py` (Windows-XP statement) |
| Pending queues (T4–T7, staged for their topic builds) | **323** | topic{4-7}_pending.py (53/46/177/47) |
| **TOTAL items captured** | **604** | + ~50 near-dups folded into multi-source book questions (see dispositions) |

### T1/T2 update pass (holding 53 disposed — see `tools/data/holding_dispositions.md`)
- 8 questions merged into T1/T2 books (benefits of networking, ring-break, tree topology, kbps speed, UPnP, data-link protocols, end-system app layer, physical-layer translate — answer corrected to Data link layer).
- 15 items routed to T3–T7 pending; ~30 near-dups of existing book questions dropped with notes; 2 cnp3 figure-based dropped.

### Topic 3 build pass (109 pending → 81 curated MCQs + 27 Nukte Rapid-Fire)
- 98 pending merged into 81 book questions (multi-source tags where several banks asked the same fact).
- 5 moved to correct topics (scanner tool → T7; IGMP/ICMP/LDAP/IPv4-total-length → T6).
- 1 held for T1 (Windows XP statements), 2 dropped (binary-missing question — source text layer broken; cnp3 figure question).
- Official keys used: RPSC 2024 + Rajasthan PYQ (`tools/data/answer_keys.py`).

## 1. Repo source PDFs (on `main`, folder `Computer Network/`)

All 15 PDFs processed. 10 have a text layer (extracted directly); 5 are
scanned (OCR'd with RapidOCR — texts kept in `tools/data/ocr_text/`).

### Text-layer PDFs (question counts = curated + pending)

| PDF | Questions found | Accounting |
|---|---|---|
| CN Topic Test-01.pdf | 48 | T1/T2 books 38, pending T3–T7 10 |
| CN Topic Test-02.pdf | 43 | books 30, pending 13 |
| CN Topic Test-03.pdf | 40 | books 5, pending 35 |
| CN Topic Test-04.pdf | 35 | pending 35 |
| CN Topic Test 5.pdf | 40 | books 1, pending 39 |
| CN Topic Test  6.pdf | 44 | books 4, pending 40 |
| BCI_SCI Subject Test-01 (CN and Security).pdf | 47 | books 23, pending 24 |
| BCI_SCI Subject Test-7.pdf | 44 | books 19, pending 25 |
| BCI Subject Test-8.pdf | 48 | books 13, pending 35 |
| BCI Subject Test-9.pdf | 46 | books 3, pending 43 |

### Scanned PDFs (OCR'd — `tools/cn_parse_ocr.py`, texts in `tools/data/ocr_text/`)

| PDF | Pages | Accounting |
|---|---|---|
| Random Test- Rajasthan PYQ.pdf | 30 | 27 questions total: 3 earlier in books + 16 matched existing queues (dups of unit-test questions) + **11 newly staged** with verified keys (`answer_keys.py`). Cover/junk 1 page. |
| Subject Test Solution -1 (CN & Security).pdf | 25 | Solution slides (= ST-01 keys). 22 matched existing, **3 new** staged. **Official keys Q1–25 preserved in `tools/data/answer_keys.py`**. |
| Subject Test Solution -1 (CN & Security) Part-2.pdf | 25 | Security-section slides. 22 matched, **3 new** staged (security questions). |
| Unit Test -2 Solutions.pdf | 54 | 54 question pages: 10 matched Topic-Test-02 queues, **26 new CN staged**, 8 Java (out of syllabus — dropped), 10 leaderboard/junk pages. |
| Unit Test-4 Solution.pdf | 52 | 50 question pages: 10 matched, **20 new CN staged**, 19 Java (dropped), 3 junk/other. |

> **Note:** the Unit-Test *Solutions* decks contain many questions that are NOT
> on the corresponding question-paper PDFs — those are now in the pending
> queues (T4/T5/T6 especially). Java questions from the mixed tests are out of
> the CN syllabus and are intentionally not ingested (28 total).

## 2. Other trusted sources (saved in repo)

| Source | Status |
|---|---|
| RPSC Programmer 2024 Paper-1 + **official answer key** | `Past Papers/RPSC Programmer 2024 Paper-1/` — 28 CN questions ingested (books 4 + pending 24) |
| Forouzan — Data Communications and Networking 6th ed (861 pp) | `Past Papers/Reference Books/` — Ch1 practice set converted (21 MCQs in books). **Ch2–7 practice sets will be converted during T3–T7 builds.** |
| cnp3/MCQ (Olivier Bonaventure textbook MCQ bank, CC-BY) | `Past Papers/Question Banks/cnp3-MCQ…/` — 12 RST files, 65 questions: **10 clean single-answer converted** to queues, 55 multi-statement/figure-based kept as **answer-verification reference** for T3/T6 |
| Web exam banks (search-snippet harvest, complete Q+4opts+key only) | 77 questions ingested — see table below |

### Web banks ingested (all items have published/verified answers)

| Bank (exam tag) | Items | Example exams |
|---|---|---|
| Testbook solved (DSSSB TGT CS, KVS PGT CS 2018, KVS Librarian 2023) | 3 | DSSSB, KVS (official papers) |
| Sanfoundry CN MCQs (Reference Models, IPv6, Data Link) | 12 | standard bank |
| InstrumentationTools 150 CN MCQs | 11 | SSC/RRB-style |
| LMT MCQ bank (Computer Communication Networks) | 4 | slideshare bank |
| EduRev SSC CGL Internet & Networking | 8 | SSC CGL |
| Oliveboard SSC CGL Tier-2 repeated | 4 | SSC CGL |
| Medium 30 important CN MCQs | 11 | general |
| Studocu IP Addressing quiz (with keys) | 4 | university quiz |
| MQuestions / Reck.ac.in DCN banks | 7 | college banks |
| Kerala PSC repeated PYQs (pscarivukal) | 2 | Kerala PSC |
| IBPS RRB PO PYQ (Meritnotes) | 1 | IBPS RRB |
| DSSSB TGT CS (Testbook) TCP/IP | 1 | DSSSB |

## 3. Found but NOT extractable (snippets truncated / sites blocked) — user can drop PDFs into `Incoming/`

- **Studocu**: not-valid-IPv4, Class-A default mask, loopback address, multicast class — option text cut in snippet.
- **Jagranjosh KVS 2018** (200 questions): slowest internet connection, world network, modem-on-telephone-lines, repeater-extend, two-computers-network, channel-capacity — 5-option format or no key visible.
- **itexamanswers CCNA** IP addressing exam (/26 hosts, IPv6 subnetting) — 5-option format.
- **Practicemock** SSC CGL TCP-packetisation — published key conflicts with Forouzan (skipped).
- **pscarivukal** Kerala PSC: repeater-function, bridge-similar-LANs, routing-layer, router-regenerates, 2 match-the-following — no options printed in snippet.
- Blocked hosts (sandbox network policy): rssb.rajasthan.gov.in, rpsc.rajasthan.gov.in, testbook, studocu, jagranjosh, meritnotes, reck.ac.in, cetking, oliveboard, practicemock, exampundit, byjus, utkarsh, scribd. Only search snippets were usable.

## 4. Answer-key preservation (was in session memory only — now in repo)

`tools/data/answer_keys.py` contains:
- **BCI_SCI ST-01 Q1–25 official keys** (from the Solution-1 slides),
- **Random Test Rajasthan PYQ verified answers** (Q23–Q117, ~27 questions),
- **RPSC 2024 key summary** (full file in Past Papers),
- **Repo-question quirks** (23 curation notes for T3–T7),
- Forouzan Ch1 practice-set facts used for T1/T2.

## 5. Historical drops (documented disposition)

- 42 exact duplicates at first extraction (same question repeated across test PDFs).
- T1 curation: 51 pending disposed = 8 merged, 16 moved to T2–T7, 27 exact/near dups dropped.
- T2 curation: 82 pending disposed = 69 curated, 8 moved, 5 dropped (2 unparseable/ambiguous: "naming conventions", "peer-to-peer"; 2 T1 dups; 1 broken parse).
- 28 Java questions in Unit-Test solution decks — out of CN syllabus.
- Option-label normalisation + light typo cleanup applied (meaning preserved).

## 6. How to re-verify (reproducible)

```
/home/user/pdfenv/bin/python tools/cn_build_topic.py --all      # rebuild all 7
/home/user/pdfenv/bin/python tools/cn_ingest_web.py             # idempotent dedupe check
/home/user/pdfenv/bin/python tools/cn_parse_ocr.py --dry-run    # OCR queue audit
/home/user/pdfenv/bin/python tools/cn_pipeline.py status        # queue status
```

## 7. Open items (nothing lost — all staged)

1. **T1/T2 holding (53)** — new finds (web + OCR + banks) merge into the T1/T2
   books at the next T1/T2 update pass (after current review).
2. **T3–T7 pending (412)** — curated phase-wise per topic (answers verified
   against Forouzan + solution-slide keys + `answer_keys.py`), at correct
   syllabus positions, never appended at the end.
3. **Forouzan Ch2–7 practice sets** — converted during their topic turns.
4. Snippet-truncated web finds (§3) — pick up when a full source is available.
