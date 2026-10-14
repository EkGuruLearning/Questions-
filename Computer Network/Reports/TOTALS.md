# Grand Totals — EkGuru CN Question Bank (R2 wave)

**Release:** R2 (wave-5 import + near-dup merge) • 2026-10-14 • branch `arena/2151f846-questions`
**Master bank:** `Computer Network/data/cn_questions.json` — **817 questions** (spec §6 schema)

## 1. Per topic

| Topic | Questions | Practice booklet | Quiz HTML |
|---|---|---|---|
| 1 — Data Communications & Networks | 150 | 150Q / 17pp | Topic 1 (243 KB) |
| 2 — OSI & TCP/IP Models | 100 | 100Q / 10pp | Topic 2 (146 KB) |
| 3 — Internetworking & Addressing | 122 | 122Q / 12pp | Topic 3 (173 KB) |
| 4 — Connecting LANs & WANs | 52 | 52Q / 5pp | Topic 4 (99 KB) |
| 5 — Telephony, TV, Cable, Wireless | 73 | 73Q / 7pp | Topic 5 (123 KB) |
| 6 — Transport, Routing & Application | 247 | 247Q / 24pp | Topic 6 (333 KB) |
| 7 — Network Security | 73 | 73Q / 7pp | Topic 7 (119 KB) |
| **Total** | **817** | **817Q / 82pp** | **7 HTMLs** |

## 2. Per difficulty (audit classifier)

| Level | Count |
|---|---|
| Easy | 86 |
| Medium | 475 |
| Hard | 256 |

## 3. Per source status (spec §7)

| source_type | Count | Meaning |
|---|---|---|
| repository_internal | 466 | repo unit tests / OCR / web banks — answer_checked |
| original_practice | 197 | self-authored (Practice — original) — answer_checked |
| claimed_pyq_unverified | 86 | claimed previous-exam recall, no primary evidence |
| textbook_paraphrase | 42 | Forouzan-concept paraphrases |
| verified_official_pyq | 26 | RPSC Programmer 2024 paper + official key |

| verification_status | Count |
|---|---|
| paper_and_key_checked | 26 |
| answer_checked | 791 |

## 4. Question style / language

- 4 options per question (100%); correct answer cross-checked at authoring (pipeline-solved, `answer_checked`)
- Bilingual EN + HI stems/options/nukte on every record; explanation language follows the question language rule
- Mix: recall / reasoning / numeric / assertion-statement / match-the-following / list-match / ordering / case-study (RPSC-style column-matching retained)

## 5. Deliverable files (R2)

| Deliverable | Location | Size/Count |
|---|---|---|
| Master JSON bank | `Computer Network/data/cn_questions.json` | 817 records |
| 7 topic books (MCQ + nukte + explanations) | `Computer Network/Topic N - …pdf` | 627 legacy + wave updates |
| Complete book | `Complete Book - CN …pdf` | 216pp (rebuild on demand) |
| 7 practice booklets (2-col, no solutions) | `Computer Network/Practice/` | 817Q / 82pp |
| 7 quiz & exam apps (mobile, filters, mock presets) | `Computer Network/Online Quiz/` | 7 single-file HTML |
| Audit reports | `Computer Network/Reports/` | INVENTORY, DUPLICATE_AUDIT, ANSWER_VERIFICATION, SOURCE_REGISTER, EXAM_BLUEPRINTS, QA_REPORT, RELEASE_NOTES, TOTALS |
| Release package R1 | `EkGuru_CN_Release_2026-10-14.zip` | 548 KB (JSON+reports+HTMLs) |

## 6. Exam coverage (source labels across the bank)

RPSC Programmer/ACP-DD • SSC MTS/CHSL/CGL/GD/Selection Post • RSMSSB IA/LDC/Informatics Assistant • GATE CS/IT • UGC NET CS • KVS PGT/EMRS/DSSSB/JNV/Lecturer • UPSC/State PSC (BPSC/TNPSC/Kerala PSC/UPPSC/MPPSC/WBPSC/APPSC/OPSC/JPSC/CGPSC/Mahagenco/BSNL JTO/JSSC/UPRVNL/UPHESC/BSF/Indian Air Force/Indian Navy/DRDO) • ISRO/NIC/CDAC • Banking (SBI/IBPS/RBI/IDBI/NABARD/Canara) • TCS/Wipro/Infosys/Cognizant/HCL/Tech Mahindra/L&T/IBM/Capgemini • BCI/SCI • NTSE/REET • CCNA/Network+/N10-009.

## 7. Verification honesty statement (spec §7)

- Only **RPSC Programmer 2024 Paper-1 (26Q)** = paper + official key checked (evidence folder preserved).
- All other 791 = pipeline-solved, `answer_checked` — **not** official-key verified. Never claimed 100% verification.
- Exact duplicates in bank: **0** (evidence: export duplicate group scan). Near-duplicate review: 15 same-answer candidates reviewed, **9 merged**, 6 kept as distinct demands (documented in DUPLICATE_AUDIT.md §3). Remaining ≥0.65-overlap pairs are concept repetition (spec §9 allowed).

## 8. Wave-5 import log (source: `Computer Network/new/`)

- 23 PDFs extracted → 1008 usable stems (McqMate sets 1–20 + DCN_MCQ-Ashwini).
- `Computer-Network-MCQ.pdf` + `networkmcq.pdf` = **0 usable** (format not parseable — honestly not imported).
- Dedupe vs bank: 24 exact + 169 near dropped + 179 internal dups → 636 unique new stems.
- Copyright rule (spec §7): compiled-bank stems **not copied verbatim**; 26 new gap-concept questions re-authored as originals (`Practice — original (textbook-based)`), incl. hop limit, dual-stack, Teredo, coax conductors, 10Base5/2/T, DSLAM, HFC, SONET STS-1, terrestrial radio, congestion collapse, protocol field 17/1, MF flag, fragment offset, RSVP, HTTP request-line/persistent/conditional-GET/250, honeypot/shadow honeypot.

**Grand total = 817 questions across 7 topics, 82 practice pages, 7 CBT apps, 8 audit reports.**

## 9. Verification Answer Key (user QA pass)

`Practice/ANSWER KEY - Added Questions (197) (Verification).pdf` — 60pp.
Sab self-authored questions (waves 1–5 = 197) jo quiz/practice me add hue: har question ka
Q + 4 options + ✓ correct answer + why (EN/HI) + nukte + source. Part A = wave-5 NEW (26),
Part B = waves 1–4 (171). User inka answer verify karenge.
Wave-5 stems practice booklets me confirmed (26/26, PDF text extract proof).

---

# R3 — W6 bulk import (ALL new/ questions) — 2026-10-14

**Grand total = 1556 questions** (817 R2 bank + **739 newly imported** from new/ compiled banks).

## Per topic (R3)

| Topic | Q | Practice booklet | Quiz HTML |
|---|---|---|---|
| 1 | 375 | 375Q / 31pp | 431 KB |
| 2 | 144 | 144Q / 12pp | 180 KB |
| 3 | 231 | 231Q / 19pp | 259 KB |
| 4 | 99 | 99Q / 8pp | 136 KB |
| 5 | 174 | 174Q / 14pp | 202 KB |
| 6 | 387 | 387Q / 34pp | 444 KB |
| 7 | 146 | 146Q / 12pp | 178 KB |
| **Total** | **1556** | **1556Q / 130pp** | 7 HTMLs, JS check 7/7 |

## Source pool & zero-repeat evidence (W6_IMPORT_LOG.md)

- Extracted: 1008 (21 PDFs) + 178 (2nd-parser: Computer-Network-MCQ 89 + networkmcq 89) = **1185 usable**
- Dropped as REPEATS: **446** (241 exact stem + 136 near≥0.90 + 69 near≥0.75 & same answer)
- **Imported: 739 new** — 0 exact dup groups in export scan

## Answer status (honest)

| verification_status | count | meaning |
|---|---|---|
| answer_checked | 791 | curation pipeline solved/cross-checked |
| paper_and_key_checked | 26 | RPSC Programmer 2024 paper + official key |
| **claimed_answer_unverified** | **739** | W6 bulk import — source key only, ⚠ CAUTION in nukte |

- W6 records: EN stems/options (Hindi translation pass pending); every nukte carries
  "⚠ CAUTION — answer NOT verified: compiled-bank source key = (X)". Visible in quiz feedback panel.
- Agent verification pass will flip records to answer_checked + fill explanations, batch by batch.
