# REVIEW ROUND 3 — Blind Final Verification

**Date:** 2026-10-14   
**Reviewer:** blind re-derivation pass, `scripts/07_review_round3.py`

## What makes this round blind

This pass never opens the build's intermediate results. It re-derives the border-sharing sets from `data/raw/**` using a **third** method — symmetric *buffered overlap area* (grow each side by 600 m, require 1.5 km² of mutual overlap) — where the build used a bidirectional boundary *length* and Round 1 used a one-directional length at a different tolerance. It then compares its answer against the **delivered** `BOUNDARY_RELATIONS.csv` and the **delivered** label manifest, treating both as untrusted.

Three different methods (length@1000 bidirectional, length@250 one-directional, area@600 symmetric) that converge on the same answer is the strongest evidence this project can produce for the adjacency claim without a second human reviewer.

## Result

| Outcome | Count |
|---|---|
| PASS | 14 |
| OPEN | 7 |

## Findings

| # | Check | Status | Detail |
|---|---|---|---|
| 1 | blind agreement India/Gujarat | **PASS** | 6 districts: ARVALLI, BANAS KANTHA, DAHOD, KACHCHH, MAHISAGAR, SABAR KANTHA |
| 2 | blind agreement India/Haryana | **PASS** | 7 districts: BHIWANI, FATEHABAD, HISAR, MAHENDRAGARH, NUH, REWARI, SIRSA |
| 3 | blind agreement India/Madhya Pradesh | **PASS** | 10 districts: AGAR MALWA, GUNA, JHABUA, MANDSAUR, MORENA, NEEMUCH, RAJGARH, RATLAM, SHEOPUR, SHIVPURI |
| 4 | blind agreement India/Punjab | **PASS** | 2 districts: FAZILKA, SRI MUKTSAR SAHIB |
| 5 | blind agreement India/Uttar Pradesh | **PASS** | 2 districts: AGRA, MATHURA |
| 6 | blind agreement Pakistan/Punjab (Pakistan) | **PASS** | 3 districts: Bahawalnagar, Bahawalpur, Rahim Yar Khan |
| 7 | blind agreement Pakistan/Sindh (Pakistan) | **PASS** | 6 districts: Ghotki, Khairpur, Sanghar, Sukkur, Tharparkar, Umer Kot |
| 8 | every district the table says touches Rajasthan is drawn at border-district priority | **PASS** | table says 36; drawn at priority 1 = 36; symmetric difference = none |
| 9 | no district abolished in Dec 2024 appears in the master | **PASS** | checked 9 abolished names; found none |
| 10 | retained 2023 districts present | **PASS** | all 8 districts retained by the Dec 2024 order are present: Balotra, Beawar, Deeg, Didwana-Kuchaman, Kotputli-Behror, Khairthal-Tijara, Phalodi, Salumbar |
| 11 | every Rajasthan district falls inside the sheet frame | **PASS** | 41/41 districts intersect the frame |
| 12 | master build metadata matches the layer | **PASS** | BUILD_METADATA.json says 41 Rajasthan and 160 Pakistani districts; the GeoPackage holds 41 and 160 |
| 13 | delivered PNGs byte-match the recorded hashes | **PASS** | 4 PNGs byte-identical to the manifest; drift: none |
| 14 | delivered PDFs present and non-trivial | **PASS** | 3 PDFs present, each > 100 kB. NOTE: PDF bytes embed a CreationDate, so their SHA-256 changes on every re-render by design; PDF integrity is instead pinned by the page-geometry and colour tests in Rounds 1-2. |
| 15 | unresolved #1: Exam-published border lengths unreproducible | **OPEN** | Pakistan 1,070 / Punjab 89 / Haryana 1,262 / UP 877 / MP 1,600 / Gujarat 1,022 km vs. GIS 1,036 / 90 / 1,039 / 462 / 2,110 / 723 km. Two independent datasets agree with each other but not with the published figures. -> The sheet reports the GIS lengths and the discrepancy is printed in QA_REPORT.md. Not resolvable without the original measurement specification behind the published numbers. |
| 16 | unresolved #2: Gazette notification not retrievable | **OPEN** | Revenue/Rajasthan and Bhuvan hosts are outside the reachable network list for this environment. -> The 41-district count rests on six corroborating contemporaneous reports instead. Flagged as the weakest evidentiary link. |
| 17 | unresolved #3: Cross-source seam between India and Pakistan layers | **OPEN** | Median offset 50 m, 93.6 % within 1 km, 113 km² total overlap across 26 slivers (largest 14.8 km²). -> Left uncorrected on principle: correcting it would mean altering one authoritative source to match another. Disclosed instead. |
| 18 | unresolved #4: 22 disputed Rajasthan–Gujarat slivers | **OPEN** | 28 km² total, 55 km of contact with Rajasthan; ownership contested. -> Excluded from the sheet and from the adjacency table, listed in data/metadata/DISPUTED_SLIVERS.csv. |
| 19 | unresolved #5: Pakistan administrative snapshot 2022-09-09 | **OPEN** | Any Pakistani district created after that date is absent. -> Newer COD-AB release would be needed; unreachable from this environment. |
| 20 | unresolved #6: Survey-of-India derivative licensing | **OPEN** | Upstream repo states redistribution terms are unconfirmed. -> Sheet carries provenance text; intended for personal study. |
| 21 | unresolved #7: No human visual inspection | **OPEN** | The rendering environment cannot display images. -> Everything verified numerically. A human must open the A1 PDF at 100 % before printing. |

## Corrections made during Round 3

1. **Ink-threshold bug in the Round 2 measurement (fixed).** Round 2 initially counted the cream sheet background (#FBF7EE, blue channel 238) as 'ink' at a 240 threshold, which made the locator-inset content check read 0.859 and fail spuriously. Threshold lowered to 128; the inset now measures 0.023.
2. **Figure/image coordinate flip (fixed).** Panel-content probes were measuring the top of the page instead of the bottom because figure y is bottom-up while image rows are top-down. Fixed in `06_review_round2.py`.

## Round 3 verdict

**Accepted for delivery, with the seven OPEN items above.** The adjacency answer is stable across three independent methods. No obsolete district is present, no district is missing, the drawn sheet matches the table, and the exported files match their recorded hashes. The residual risk is evidentiary and visual, not geometric.

## Standing instruction for the three planned revision passes

Any future change must be made in the underlying data or design layer and re-exported through `03_render.py`, never patched into the PNG. The register of OPEN items above is the machine-readable list to work from.
