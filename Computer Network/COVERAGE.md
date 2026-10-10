# COVERAGE — Complete Question Accounting (koi question nahi chhoota)

Last updated: 2026-10-09 (after OCR of scanned PDFs + web/textbook-bank harvest).
This file proves that **every** question in every source is accounted for:
either curated into a book, staged in a queue, or dropped with a documented reason.

## Grand totals (updated after Topic 4 build)

| Bucket | Count | Where |
|---|---|---|
| Curated books (T1 + T2 + T3 + T4) | **315** | topic1_data (118) + topic2_data (81) + topic3_data (82) + topic4_data (34) |
| T1/T2 holding (awaiting next book update) | **1** | `tools/data/web_extra_t1t2.py` |
| Pending queues (T5–T7, staged for their topic builds) | **277** | topic{5-7}_pending.py (46/184/47) |
| **TOTAL items captured** | **593** | + ~50 near-dups folded into multi-source book questions |

### T1/T2 update pass (holding 53 disposed — see `tools/data/holding_dispositions.md`)
- 8 questions merged into T1/T2 books (benefits of networking, ring-break, tree topology, kbps speed, UPnP, data-link protocols, end-system app layer, physical-layer translate — answer corrected to Data link layer).
- 15 items routed to T3–T7 pending; ~30 near-dups of existing book questions dropped with notes; 2 cnp3 figure-based dropped.

### Topic 3 build pass (109 pending → 82 curated MCQs + 27 Nukte Rapid-Fire)
- 98 pending merged into 82 book questions (multi-source tags where several banks asked the same fact).
- 5 moved to correct topics (scanner tool → T7; IGMP/ICMP/LDAP/IPv4-total-length → T6).
- 1 held for T1 (Windows XP statements), 2 dropped (binary-missing question — source text layer broken; cnp3 figure question).
- Official keys used: RPSC 2024 + Rajasthan PYQ (`tools/data/answer_keys.py`).

### Topic 4 build pass (53 pending → 34 curated MCQs + 22 Nukte Rapid-Fire)
- 45 pending merged into 34 book questions (multi-source tags; recovered garbled items from source PDFs: BCI T9 statements, ST-7 router-functions, UT-4 router-statements & MUX).
- 7 moved to Topic 6 (transport multiplexing, BGP, MPLS, L7 protocols, MAC sublayer, early-ARPANET routing, dynamic routing protocols).
- 11 dropped/documented: 3 covered in Topic 3 (subnet-mask/ARP/NAT-fn), 5 near-dups merged (collision-domain & router-definition variants), 1 match-format garbled, 1 cnp3 figure, 1 Rajasthan-PYQ Q91 (option D unreadable even at 300-dpi OCR — not fabricated).
- +1 question added into Topic 3 (network ID reserved — cannot be assigned to a host).

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


## 8. India-level PYQ drive (2011–2026) — merged Oct 2026

45 new previous-year questions harvested from every accessible exam bank and
merged topic-wise at section level (books now 602 MCQs total):

- **RPSC Programmer 2011 Paper-1** (via pyqp.in text dump): TCP port numbers,
  TTL loop-prevention, not-client-server (Ping), bridge-vs-router, AAL function,
  CSMA/CD min-packet (joint key with GATE CS 2003).
- **RPSC Programmer 2024** (via Suraku Academy official-key solutions):
  Class B /21 subnet hosts=2046; DNS reverse lookup = PTR.
- **GATE CS**: 2003 (CSMA/CD 2 km min packet), 2005 (Class B 6-bit subnet 62/1022),
  2007 (CRC x³+1 → 11001001011), 2008 (slow-start exponential), 2009 (CRC odd-bit
  condition = x+1 factor), 2012 (TCP statements), 2015 Set-3 (signal speed 20000 km/s),
  symmetric-key count N(N-1)/2.
- **UGC NET CS Jan 2025 / Dec 2022** (via samagracs): CSMA/CD 20 Mbps→1000 bits;
  Nyquist 5000 Hz→10000 bps; CRC data 111111.
- **RSMSSB Informatics Assistant 2023** (via examsmantra): repeater, mesh wires,
  MAC 48-bit (merged), VoIP, digital signals.
- **SSC CHSL 2022-23 / SSC MTS / SSC CGL** (via Testbook, adda247, pendulumedu):
  DHCP dynamic IP (merged), FTP full form (merged), HTTP = WWW delivery,
  TCP/IP standard protocol.
- **HTET 2024 / BPSC TRE 2024** (via KnowledgeGate): worm resource-exhaustion,
  VPN private-over-public.
- **RRB NTPC PYQ banks** (via adda247 50-PYQ PDF, practicemock): POP3 receive,
  odd-one SNMP, firewall monitoring, spam, WLL/ISDN/Hertz-odd (selected).
- **Banking (IBPS/SBI PO & Clerk, RRB PO)** (via meritnotes, bankersadda,
  ixambee, IBT capsule, tpointtech): TCP/IP suite, broadband vs baseband,
  dial-up not broadband, bridges connect LANs, plaintext/ciphertext, time bomb,
  authentication, biometric, IPv6=128, POP3/SLIP full forms, ICMP full form.
- **Solved-drop list** (documented, not fabricated): items with missing options
  (preamble-Q option-4 bleed in RPSC 2011 dump, sliding-window numerics),
  disputed keys (MAC-vs-IP "permanent address"), 5-option papers adapted with
  notes (BPSC), figure/scenario GATE items.

All prior repo-PDF content was already fully merged (§1–§7; 15 papers + OCR
decks + web banks + cnp3 banks = 656+ items accounted; pending sets disposed).


## 9. Wave-2 GATE sweep + difficulty ordering + Material Archive (Oct 2026)

- **Wave 2 (+29):** GATE 2011–2026 full sweep (2012 Class C 2²¹, 2013 last-fragment
  2400–2759, 2014 ×3, 2015 ×2 stop-wait numerics + router NOT-modify, 2016 ×2,
  2017 FIN_WAIT_2, 2018 ×2 seq-reuse=34s + slow-start (iv), 2019 ×2 /30 + ARP,
  2020 router stmts, 2021 handshake X+1, 2022 ×2 7.08ms + 33-bits, 2024 ×3 NAT/CIDR/
  6-fragments, 2025 ×2 flags + next-hop), KVS PGT 2017 (153.6 Mbps, 1000/4000 baud),
  EMRS PGT (WWW). All complete items; zero repeats (deduped against 602 existing).
- **Difficulty ordering (user spec):** har section ke andar Easy → Medium → Hard;
  `tools/cn_difficulty.py` exam-level + content heuristics (SCI/BCI/MTS/CHSL/REET =
  easy; GATE/NET/KVS/EMRS/DSSSB/JNV/Programmer/PGT = hard; beech = medium). Books
  mein source line par chip: `· Easy / · Medium / · Hard`.
- **Material Archive/** — future subjects (DBMS, SAD, Java) ke liye saara research
  material + source registries + workflow README (2-din roadmap).
- Totals: **631 MCQs** (T1 124, T2 82, T3 93, T4 38, T5 48, T6 193, T7 53) + 165
  nukte rapid; Easy 86 / Medium 339 / Hard 206.


## 10. The Complete Book (Theory + Questions) — Oct 2026

User spec ke hisaab se nayi complete book: **"The Complete Computer Network -
Theory + 631 MCQs (Answers + Nukte).pdf/.md"** (216 pages):

- Har section mein PEHLE **समझ (Theory)** — full-width bilingual structured notes
  (intro + bullets + table) — Forouzan se; PHIR questions **Easy → Medium → Hard**.
- Question row = 2 columns: LEFT question + options | RIGHT = sirf **✔ correct
  answer + ★ Nukte** (lambi explanation nahi — theory pages woh kaam karte hain).
- Sab 7 topics, 31 sections, 631 MCQs + 165 nukte rapid-fire covered.
- No pictures; structured lining; Hindi clean Devanagari.
- Theory data: `tools/data/topic{1..7}_theory.py`; builder: `tools/cn_build_complete.py`.
- 7 topic books (detailed why-correct format) bhi repo mein hain as-is.

## 7. Open items (nothing lost — all staged)

1. **T1/T2 holding (53)** — new finds (web + OCR + banks) merge into the T1/T2
   books at the next T1/T2 update pass (after current review).
2. **T3–T7 pending (412)** — curated phase-wise per topic (answers verified
   against Forouzan + solution-slide keys + `answer_keys.py`), at correct
   syllabus positions, never appended at the end.
3. **Forouzan Ch2–7 practice sets** — converted during their topic turns.
4. Snippet-truncated web finds (§3) — pick up when a full source is available.
