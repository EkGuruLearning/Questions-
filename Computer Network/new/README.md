# EkGuru Data Communication & Computer Networks (CN) Question Bank

**Project owner / compiler:** PRAKASH  
**Brand:** EkGuru Learning  
**Reference orientation:** Behrouz A. Forouzan, *Data Communications and Networking*, plus official exam syllabi/papers/answer keys, other recognised networking texts, standards/RFCs, and original practice questions.  
**Last working review:** 13 October 2026

---

## 1. Project goal

Build a topic-wise, exam-aware, non-repeating CN practice bank for Rajasthan state recruitment and relevant Indian/national technical examinations. The portal must let a learner choose the exam profile, topic/subtopic, question style, source category, quantity, mode, time per question, and a mock negative-marking rule. It must provide reliable answers, explanations, score analysis, and a question-wise review after submission.

This is a curated question-bank project, not a claim that one static set reproduces every exam or every book. The source material must be recorded per question, duplicates must be grouped, and answer-key verification must be traceable.

## 2. Current supplied inventory

The following are the uploaded practice-booklet inventories. Counts are the numbers stated in their filenames/booklet covers; they are **not** a count of unique questions after deduplication.

| Topic | Supplied booklet | Stated questions | Current role |
|---|---|---:|---|
| 1 | Introduction of Data Communication | 151 | Existing interactive HTML bank with answers/explanations; needs a full answer/provenance audit |
| 2 | Network Models (OSI & TCP/IP) | 100 | Practice booklet; no solution key in the supplied PDF |
| 3 | Addressing (MAC, IPv4, IPv6, Port, DNS) | 122 | Practice booklet; no solution key in the supplied PDF |
| 4 | Networking Devices | 53 | Practice booklet; no solution key in the supplied PDF |
| 5 | Transmission Medium | 67 | Practice booklet; no solution key in the supplied PDF |
| 6 | OSI Layers in Detail | 240 | Practice booklet; no solution key in the supplied PDF |
| 7 | Network Security | 72 | Practice booklet; no solution key in the supplied PDF |
| **Total** | **7 booklets** | **805** | **Raw inventory; duplicates and overlap are expected** |

The two uploaded copies of the Topic 1 HTML and the pasted-text copy should be treated as duplicate representations of the same base, not separate banks.

### Present interactive HTML state

`EkGuru_CN_Online_Test_Portal_Updated.html` contains the original 151 records plus one corrected repeater/ring-topology concept-check item (152 records total). It adds exam-profile, section, question-style and source-label selectors; clearer provenance wording; configurable mock negative marking; safer unsaved-response navigation; and several review/timing fixes. **It does not yet contain all questions from Topic 2–7 PDFs.** Those PDFs currently do not include answer keys, so their questions must be answered and independently reviewed before being merged into a scored CBT test.

## 3. Official exam profiles to support

Build distinct profiles, but do not imply a single question mix fits all examinations:

### Rajasthan recruitment / computer awareness
- RPSC Programmer
- Analyst-Cum-Programmer / Deputy Director (confirm the exact post and notification)
- RSMSSB Informatics Assistant
- BCI / SCI roles (retain the exact recruitment name and year from the source paper)
- Other relevant Rajasthan technical recruitment exams and computer-awareness sections

### Technical / teaching / national profiles
- GATE Computer Science and Information Technology
- UGC-NET Computer Science and Applications (subject code 087)
- Assistant Professor / technical faculty exams, only where the relevant subject and notification match
- KVS / NVS / EMRS / DSSSB / HTET and other teacher-recruitment computer/IT sections when applicable
- SSC / RRB / IBPS / UPSC and other exams only for the computer/network content that their current syllabus actually includes

Each profile needs its own **syllabus map, source register, time/marks/negative-marking rule, supported question formats, and confidence label**. Do not copy GATE marking or timing to a Rajasthan exam or vice versa. For example, the official GATE 2026 CS pattern is a three-hour, 100-mark paper and distinguishes MCQ negative marking from MSQ/NAT treatment; always re-check the current official pattern before building an exact simulation.

Official starting points (verify the current notification on every release):
- RPSC syllabus index: https://rpsc.rajasthan.gov.in/Syllabus.aspx
- RPSC Programmer syllabus PDF (official page): https://rpsc.rajasthan.gov.in/Static/Syllabus/7B209EAD-A262-4AE5-8387-0E53FF305A31.pdf
- GATE 2026 exam papers and syllabus: https://gate2026.iitg.ac.in/exam-papers-and-syllabus.html
- GATE 2026 question paper pattern: https://gate2026.iitg.ac.in/question-paper-pattern.html
- GATE 2026 question papers and answer keys: https://gate2026.iitg.ac.in/QPs-answer-keys.html
- UGC-NET official portal and answer keys: https://ugcnet.nta.ac.in/AnswerKey.html
- UGC-NET Computer Science & Applications (subject code 087) final key examples: https://ugcnet.nta.ac.in/images/UGC_JUNE_2025_FINALKEY/087.pdf
   and also https://www.indiabix.com/networking/questions-and-answers/.  check and add 
The official RPSC Programmer syllabus includes Data Communication and Computer Networks subjects such as network architecture, switching, network structure, physical/data-link topics, topologies, TCP/IP, DNS/firewalls and related content. Map actual profile coverage from the specific notification rather than assuming that all exams cover all seven CN booklets.

## 4. Topic map and scope control

### Topic 1 — Introduction of Data Communication
- Components: message, sender, receiver, transmission medium, protocol
- Data communication characteristics: delivery, accuracy, timeliness, jitter
- Network criteria: performance, reliability, security
- Modes: simplex, half-duplex, full-duplex
- Topology: physical vs logical; mesh, star, bus, ring and hybrid forms
- Network types: LAN, MAN, WAN, PAN, CAN, SAN
- Accessibility: Internet, intranet, extranet
- Connection/architecture: point-to-point, multipoint, client-server, peer-to-peer
- History: ARPANET and the Internet's evolution

**Scope warning:** the original Topic 1 HTML's Section G contains 20 general-network questions, such as email, WWW, ATM and switching. Some of these belong more naturally to later topics or need a syllabus mapping. Do not automatically regard all 151 as confined to the short Topic 1 outline above.

### Other supplied topics
- Topic 2: OSI and TCP/IP models
- Topic 3: MAC, IPv4/IPv6, ports and DNS
- Topic 4: network devices
- Topic 5: transmission media and signal/transmission fundamentals
- Topic 6: layer-wise functions and protocols
- Topic 7: network security

Cross-topic overlap is normal (e.g., a repeater can appear in devices and topology context). The deduplication system should preserve a shared concept tag while preventing near-duplicate stems from being presented as unique new coverage.

## 5. Repeater / ring-topology correction

### Original wording to retire
> The repeater is used in ____ topology.

Expected answer in many traditional basic-computer MCQ sets: **Ring topology**. However, the stem is too broad because a repeater is a physical-layer signal-regeneration device and is not exclusively usable in ring networks.

### Corrected question used in the updated HTML
> In a traditional ring network, repeaters are particularly associated with which topology because each station can regenerate and forward the signal?
>
> (A) Ring topology  (B) Mesh topology  (C) Bus topology  (D) Star topology

**Answer: (A) Ring topology.**  
**Explanation:** In a classic ring, each station commonly regenerates/repeats the incoming signal before passing it to the next station. The qualification “traditional ring network” preserves the intended textbook answer without falsely implying that repeaters are exclusive to rings. This is an original concept-check correction, **not a verified PYQ**.

## 6. Mandatory question record schema

Each question should be stored as one independent data object with the following fields:

```json
{
  "id": "CN-T04-REP-0001",
  "topic_id": "T04",
  "topic": "Networking Devices",
  "subtopic": "Repeater; ring topology",
  "stem_en": "...",
  "stem_hi": "...",
  "options_en": ["A", "B", "C", "D"],
  "options_hi": ["...", "...", "...", "..."],
  "correct_option": "A",
  "explanation_en": "...",
  "explanation_hi": "...",
  "question_style": "concept | scenario | statement | numerical | match | assertion_reason | MSQ | NAT",
  "difficulty": "easy | medium | hard | pending_review",
  "exam_tags": ["RPSC Programmer", "GATE CS"],
  "source_type": "verified_official_pyq | claimed_pyq_unverified | textbook_paraphrase | original_practice",
  "exam_name": null,
  "exam_year": null,
  "paper_or_shift": null,
  "question_id_in_official_key": null,
  "source_url_or_file": "...",
  "answer_verified_by": "...",
  "verification_status": "pending | answer_checked | paper_and_key_checked | disputed",
  "duplicate_group": null,
  "concept_tags": ["signal regeneration"],
  "last_reviewed": "YYYY-MM-DD"
}
```

Use stable IDs; never identify a question only by its display order, since the portal shuffles it.

## 7. Source provenance and copyright policy

### Allowed/expected source families
1. Official syllabus, paper and answer keys from the respective exam authority.
2. Recognised networking texts for concept verification and original questions.
3. Standards and technical references (IEEE standards where accessible and relevant; IETF RFCs; other standards bodies).
4. The user's existing booklets and internal tests, treated as supplied material rather than independently verified official papers.
5. Original questions written to target a syllabus outcome, including application scenarios, calculations and conceptual contrasts.

### Books to consult by concept, not copy wholesale
- Forouzan, *Data Communications and Networking* (core reference named by the owner)
- Kurose & Ross, *Computer Networking: A Top-Down Approach*
- Tanenbaum, Wetherall and related editions of *Computer Networks*
- Stallings, *Data and Computer Communications* / relevant networking texts
- Comer, *Internetworking with TCP/IP*
- Relevant protocol RFCs and IEEE 802 references

Edition, chapter, page and licensing/access details should be recorded when a book is actually checked. Do not claim “every book worldwide” was searched; that cannot be demonstrated. A defensible process is broad source coverage plus a visible bibliography and a per-question provenance record.

Do not reproduce large copyrighted question banks or book passages verbatim. Prefer original wording and original distractors based on the underlying concepts. When a short PYQ quotation is legally and policy-appropriately included, retain its exam, year, paper/shift, question ID (if present), original source and official key reference.

## 8. Source-status rules (never blur these labels)

- **Verified official PYQ:** Original paper and official key (or an authority's official question/answer record) have been matched.
- **Claimed PYQ — verification pending:** A compilation says “PYQ” or gives an exam/year but the original paper/key has not yet been checked.
- **Repository / internal test:** Source comes from an internal test, institute repository, OCR solution, coaching bank, or third-party compilation.
- **Textbook-based practice:** Question is based on a textbook concept, not presented as an actual past-paper item.
- **Original practice:** Newly written question; not a PYQ.

A source string such as “RPSC Programmer 2024 Paper-1 (with official key)” is not by itself the official evidence. Attach the actual paper/key or downgrade the record to “claimed PYQ — verification pending.” Same principle applies to GATE, UGC-NET, SSC, RRB, KVS and all other exams.

## 9. Non-repetition system

Deduplicate at three levels:
1. **Exact duplicate:** Same stem/options with formatting changes only.
2. **Near duplicate:** Same tested fact, same cognitive demand and nearly identical options despite paraphrasing.
3. **Concept repetition for spaced practice:** Allowed only when the question asks for meaningfully different reasoning, e.g., definition, scenario, calculation, failure analysis or standards interpretation. Tag the common concept and do not count it as entirely new syllabus coverage.

Before publishing a question:
- normalise Unicode, whitespace, punctuation and option labels;
- compare question text and option sets across all seven booklets, the HTML file and future source imports;
- compare semantic meaning, not just exact text;
- check the answer and explanation independently;
- retain a duplicate-group ID when two versions must be kept for history;
- record which version is canonical and why.

Do not promise “zero similar questions” just because an exact-string duplicate scan is clean. Near-duplicate review requires concept-level analysis and a manual audit trail.

## 10. Answer verification workflow

For every item in the supplied PDFs (which are currently without solutions):
1. Extract the full question, options and source line; preserve diagrams/tables.
2. Check whether wording is complete and whether more than one option could be defensible.
3. Solve independently from a primary technical source or authoritative syllabus/source.
4. For a claimed PYQ, locate the official paper and its final/corrected key; record question ID/shift and resolve challenge/bonus questions carefully.
5. Explain why the answer is correct and why plausible distractors are wrong when needed.
6. Have a second-pass checker review the key, calculations, assumptions, units and wording.
7. Mark ambiguous/disputed items as `pending_review` or rewrite them. Never silently guess a key.
8. Run the HTML, shuffle the choices and check that the correct key remains attached to the right option.

The supplied PDFs do not contain a complete answer key. Therefore, merely extracting all 805 question stems is not equivalent to verifying all 805 answers. The Topic 1 HTML contains answer/explanation data but also requires answer-by-answer validation before it is labelled fully verified.

## 11. Exam-profile and practice-style requirements

The test setup should allow the learner to select:
- Target exam profile (profile label plus a separately verified blueprint)
- Topic and subtopic
- Source category/status
- Question type: direct concept, scenario/application, statement-based, numerical/calculation, match, assertion-reason, multi-select and numerical answer where relevant
- Difficulty (only after reviewed difficulty tags exist)
- Number of questions
- Quiz mode or timed exam mode
- Seconds per question or official time rule
- Marking scheme, positive marks and negative marks as per a verified exam blueprint
- English, Hindi or both (where verified translations are available)

The current updated HTML exposes the main filters but its target-exam choice is a **practice profile label**, not a validated exam-specific question filter. Full per-exam filtering must wait until the question records have audited exam tags. Do not show unavailable formats as if they exist in the current question bank.

### CBT behaviour required
- Question palette statuses distinguish not visited, visited/unanswered, answered, marked for review, and answered+marked.
- Save & Next persists the chosen response.
- Palette jumps warn about unsaved answers.
- Timeout auto-submits once.
- Unattempted responses count as skipped, not wrong.
- Answer/explanation is shown immediately in quiz mode and after submission in exam mode.
- Revisiting a quiz-mode answer must still show its feedback.
- The option order may shuffle, but correct answer indexing must shuffle with it.
- Results show correct, wrong, skipped, accuracy, net mock score under the chosen rule, time and per-question explanations.
- Never call generic +1 scoring an exact official marking scheme unless configured from that exam's current notice.

## 12. Audit findings from the current assets

- The original interactive HTML has 151 question records, seven internal sections (A–G), and about 99 distinct literal source labels. The labels mix internal repository tests, textbook practice, OCR-derived records and named-exam claims.
- Some existing source labels include broad phrases such as “India-level PYQ banks” and a date range without an associated question-level official source. Replace global claims with per-question evidence.
- The original startup text claims all answers are verified, but the HTML by itself does not provide the official paper/key evidence needed to establish that for every item. This claim has been removed/reworded in the updated version.
- The same concept appears multiple times in the Topic 1 bank (examples include the five data-communication components, protocol rules, and Internet/packet-switching concepts). Some repetition may be useful for practice, but it must be recorded and not counted as new unique coverage.
- Initial cross-booklet duplicate-risk examples visible in the supplied text: Topic 2 repeats introductory OSI-layer/support-layer facts; Topic 3 revisits MAC/physical-address/link-layer identification in several forms; Topic 4 repeats the physical-layer/repeater role; Topic 5 repeats the stem about discrete signals generated by digital modulation (visible as Q10 and Q16); Topic 6 revisits flow-control/layer-function definitions; Topic 7 reuses CIA-goal and attack-impact facts. These are candidates for a full exact/near-duplicate pass, not a claim that every question has already been compared.
- Section G includes broader network basics outside the tight Topic 1 outline; it should be split or re-tagged during the full question-bank integration.
- PDFs are print-ready two-column booklets without solutions, as shown on their cover text. A scored interactive merge must not invent unreviewed answer keys.
- The question “In a computer network, nodes are ... all of the mentioned” is broad and would benefit from a more precise definition of a node and examples of end systems and forwarding devices.
- The question “The capacity of a communication channel is measured in ...” should distinguish bandwidth in hertz from data rate in bits per second if the options/wording conflate them.
- The protocol timing explanation that adds “flow control” to timing should be checked against the exact Forouzan edition/chapter used; do not merge textbook terms without confirming the source wording.
- The circuit-switching explanation that every connection receives a physically separate path is oversimplified for systems that multiplex circuits over shared physical trunks. Prefer “dedicated logical circuit/resources for the connection” when describing the general principle, and use the traditional telephone model only when explicitly stated.
- The old palette navigation discarded an unsaved exam response without confirmation; the updated file now prompts before moving.
- The old HTML did not restore instant feedback when returning to an answered quiz-mode question, under-counted per-question time when rerendering, and did not submit naturally after Save & Next on the last question. These behaviours were fixed in the updated file.

These are source and code audit findings, not a claim that all 805 supplied questions have already been fully verified.

## 13. Proposed source hierarchy

Use this priority order for factual resolution:
1. Current official exam notification, official paper and official final answer key for exam-specific marking/provenance.
2. Standards, RFCs, and authoritative protocol specifications for detailed networking facts.
3. Primary reference textbook(s), with edition/chapter/page recorded, for textbook terminology.
4. Recognised academic textbooks as cross-checks.
5. High-quality secondary explanations only as a lead to better sources—not as the only proof for a disputed answer.

If sources conflict, record the conflict, edition/date and resolution. Do not hide uncertainty in a polished explanation.

## 14. Next implementation milestones

1. **Freeze baseline:** retain all seven provided PDFs and original HTML read-only; hash them and note version/date.
2. **Normalize inventory:** extract every PDF question into structured data with topic, source label, difficulty claim and answer-status fields.
3. **Deduplicate:** exact-match scan plus concept/near-duplicate review across all 805 raw questions.
4. **Answer audit:** independently solve each booklet question; attach authoritative citations and flag ambiguity.
5. **PYQ source audit:** confirm named exam/year/shift/question and official answer key before raising status to verified.
6. **Per-exam mapping:** map every syllabus item to exam profiles from current official notifications; maintain change log by exam year.
7. **Integrate interactive bank:** merge only items that have stable IDs, validated options, answer explanations, source-status metadata and topic/type tags.
8. **Build test presets:** topic-wise, exam-profile, question-type, difficulty and mixed-CN mocks; implement exam-specific marking only from verified rules.
9. **QA:** syntax check, answer-index shuffle tests, desktop/mobile layout, timer edge cases, filtering/count combinations, print/results output and keyboard access.
10. **Release:** update change log, source register, version, test counts and known limitations. Never say “all verified” until the audit reports zero unresolved records.

## 15. Version/change log

### 2026-10-13 — audit starter update
- Added this project README and the rules for source traceability, deduplication, exam profiles and answer verification.
- Updated the interactive portal to offer target-exam profile, section, question-style, source-label, quantity, time and mock marking selectors.
- Added a precisely worded repeater/ring-topology concept check.
- Reworded broad “all answers verified”/PYQ-source claims to avoid unsupported promises.
- Fixed feedback-on-revisit, unsaved response navigation, last-question submission, and per-question timing behaviour.
- Remaining: integrate Topics 2–7 into the HTML only after answer keys and source statuses are prepared; validate all 151 original HTML answers and all 805 booklet records.
