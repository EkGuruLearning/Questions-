# Exam Blueprints — verified patterns (checked 2026-10-14)

> Spec rule (`new/README.md` §3, §11): never copy one exam's marking/timing to
> another; verify the current notification on every release. These profiles were
> checked against public exam-pattern pages today (sources cited). Official
> portals (rpsc.rajasthan.gov.in, ugcnet.nta.ac.in) are NOT reachable in this
> build environment — re-verify from the official notification before claiming
> an exact simulation.

## 1. GATE CS (GATE 2026 pattern)
- Mode: CBT, English, **3 hours**, **65 questions** (10 General Aptitude + 55 CS), **100 marks**
- Question types: MCQ, MSQ (multiple select), NAT (numerical answer)
- Marking: 1-mark and 2-mark questions; **MCQ wrong: −1/3 (1-mark), −2/3 (2-mark)**
- **No negative marking for MSQ and NAT** (and no partial credit)
- Sources: testbook.com/gate-cs, imsindia.com GATE marking-scheme page, careers360 GATE 2026 marking scheme (all consulted 2026-10-14); official: gate2026.iitg.ac.in/question-paper-pattern.html (not fetchable here — re-check).
- **CN scope note:** CN is part of the 55-mark CS section; this bank's questions are CN-only practice, not a full GATE paper.

## 2. UGC-NET (subject 087 Computer Science & Applications)
- Mode: CBT, English & Hindi, **3 hours combined** (Paper 1 + Paper 2)
- Paper 1: 50 Q / 100 marks (common); Paper 2: 100 Q / 200 marks (subject)
- **+2 per correct answer, NO negative marking** (unattempted: 0)
- Sources: oliveboard.in UGC-NET pattern, embibe.com, parakhpath.com (consulted 2026-10-14); official answer keys at ugcnet.nta.ac.in (not fetchable here).
- **CN scope note:** Paper 2 (087) syllabus includes Data Communication & Networking — this bank supports that unit only.

## 3. RPSC Programmer (Rajasthan, 2024 recruitment)
- Two papers, **100 marks each**, **2 hours each** (total 200 marks, 4 hours)
- Paper I: Reasoning & Numerical Analysis & GK + **DBMS + Data Communication & Computer Networks**
- Paper II: System Analysis & Design + Programming Concepts
- Negative marking: **1/3 per wrong answer** (Suraku Academy pattern page, citing RPSC); Testbook's page instead says 1/3 for *unanswered* — **sources conflict; verify the official notification**. Qualifying: 40% aggregate (36% SC/ST), grace up to 3 marks.
- Question count: **sources conflict** — 120 Q/paper (Testbook) vs 100 Q/paper (Suraku). Verify before exact simulation.
- Exam held 27 Oct 2024 (Paper I & II); paper + official key kept in `Past Papers/RPSC Programmer 2024 Paper-1/`.
- Sources: testbook.com/rpsc-programmer/syllabus-exam-pattern, surakuacademy.com/programmer (consulted 2026-10-14).

## 4. RSMSSB Informatics Assistant (2023 recruitment)
- Written objective exam: **100 questions / 100 marks / 3 hours**, then typing test
- Section split — **sources conflict**: IT 70 / Reasoning 10 / Maths 10 / GK 10 (Adda247) vs IT 56 / Reasoning 19 / Maths 5 / GK 20 (SarkariPariksha). Verify notification.
- Negative marking — **three-way conflict**: 1/3 (Adda247) vs 1/4 (SarkariPariksha) vs none (Examsbook). **Do not claim an exact simulation**; the portal's IA preset uses the mid value 1/3 with a visible "verify" note.
- Sources: adda247.com IA 2023 page, sarkaripariksha.com, examsbook.com (consulted 2026-10-14).

## 5. SSC computer-awareness questions (MTS/CHSL/CGL)
- These exams carry a computer-awareness/general-awareness section rather than a
  full CN paper; question counts and negative rules vary by exam/year.
- Standard (verify per notification): SSC CGL Tier-1: 100 Q / 200 marks / 60 min, −0.50 per wrong; SSC CHSL Tier-1: 100 Q / 200 marks / 60 min, −0.50 per wrong; SSC MTS: 90 Q / 270 marks (session-I no negative; session-II no negative per 2024 notice).
- Portal preset label: "SSC mock (generic +1 / −0.25 default)" — **a mock rule, not an official scheme**.

## Portal marking presets (mock rules — always labelled "mock")
| Preset | +marks | −marks (wrong) | based on |
|---|---|---|---|
| GATE mock | 1 | 1/3 | GATE MCQ rule (1-mark questions) |
| RPSC mock | 1 | 1/3 | RPSC Programmer (per Suraku; verify) |
| UGC-NET mock | 2 | 0 | NET: no negative |
| IA mock | 1 | 1/3 | IA (conflict — verify) |
| No negative | 1 | 0 | practice mode |

**Never label these "exact official marking"** (spec §11). Configure from the
current notice for exact simulations.
