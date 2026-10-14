# REVIEW ROUND 2 — Label and Cartography Audit

**Date:** 2026-10-14   
**Reviewer:** automated rendering audit, `scripts/06_review_round2.py`

## What this round checks that Round 1 did not

Round 1 audited the *data*. This round audits the *picture*: the label manifest the renderer emitted, the font resources actually embedded in the PDF, the physical page box of each sheet, and the ink content of each furniture panel. It compares the rendered sheets against the master GeoPackage rather than against Round 1's conclusions.

**Limitation, stated up front:** this environment cannot display images, so no human-style visual check was performed. Everything below is a pixel or geometry measurement. Test 20 in `QA_REPORT.md` records this as NOT TESTED rather than silently passing it.

## Result

| Outcome | Count |
|---|---|
| PASS | 23 |
| REVIEW | 1 |
| NOT TESTED | 1 |

## Findings

| # | Check | Status | Detail |
|---|---|---|---|
| 1 | all 41 Rajasthan districts labelled on A1 | **PASS** | 41/41 placed |
| 2 | all 36 border-sharing neighbour districts labelled | **PASS** | 36/36 placed |
| 3 | no duplicate label strings drawn | **PASS** | 0 duplicated strings |
| 4 | every district label anchored inside a real polygon | **PASS** | A1: 237/237; A2: 237/237; A3: 86/86 -- all anchors inside |
| 5 | leader lines used only where a label was displaced | **PASS** | 4 of 237 labels were displaced from their polygon interior point and given a leader line; the remaining 233 sit directly on their polygon |
| 6 | every drawn glyph exists in the embedded font set | **PASS** | 237 drawn strings checked against 6155 codepoints; missing: none |
| 7 | Devanagari font embedded in the PDF | **PASS** | font resources in the A1 PDF: ['/ELAFME+LastResortHE-Regular', '/GGWEWS+NotoSansDevanagari-Regular', '/GPQBUG+NotoSansDevanagari-Bold', '/HATSKO+DejaVuSans', '/HDQTZN+NotoSansDevanagari-Regular', '/OPLSQB+NotoSansDevanagari-Bold'] |
| 8 | A1 page size | **PASS** | 841.0 x 594.0 mm (target 841.0 x 594.0) |
| 9 | A2 page size | **PASS** | 594.0 x 420.0 mm (target 594.0 x 420.0) |
| 10 | A3 page size | **PASS** | 420.0 x 297.0 mm (target 420.0 x 297.0) |
| 11 | A1 border colours drawn | **PASS** | international red 158,094 px, interstate yellow 114,142 px |
| 12 | A2 border colours drawn | **PASS** | international red 78,702 px, interstate yellow 58,918 px |
| 13 | A3 border colours drawn | **PASS** | international red 38,812 px, interstate yellow 30,664 px |
| 14 | all six surrounding regions carry a large Hindi label | **PASS** | placed: ['उत्तर प्रदेश', 'गुजरात', 'पंजाब', 'पाकिस्तान', 'मध्य प्रदेश', 'हरियाणा'] |
| 15 | Pakistani provinces labelled where present on the sheet | **PASS** | placed: ['पंजाब (पाकिस्तान)', 'बलूचिस्तान', 'सिंध'] |
| 16 | title district count matches the verified data | **PASS** | the sheet's subtitle is generated from the layer (41 districts, 7 divisions); it is not hard-coded |
| 17 | legend panel has content | **PASS** | ink fraction in the legend area = 0.008 |
| 18 | locator inset has content | **PASS** | ink fraction in the inset area = 0.015 |
| 19 | study panel 1 has content | **PASS** | ink fraction in study panel 1 = 0.008 (blank reference on this sheet = 0.000) |
| 20 | study panel 2 has content | **PASS** | ink fraction in study panel 2 = 0.008 (blank reference on this sheet = 0.000) |
| 21 | study panel 3 has content | **PASS** | ink fraction in study panel 3 = 0.007 (blank reference on this sheet = 0.000) |
| 22 | title band has content | **PASS** | ink fraction in the title band = 0.025 |
| 23 | labels displaced off their polygon | **REVIEW** | 4 labels (1.7 %) were moved by the collision engine and are drawn with a leader line. Each leader still terminates on the correct polygon's interior point, but a human should confirm none of them crosses the international boundary confusingly. |
| 24 | small-district legibility | **PASS** | A3 (420 mm) sets Rajasthan districts at 6.72 pt and its smallest label at 5.37 pt, both above the 5 pt floor. This is only possible because A3 names 86 districts rather than 237 - type now scales sub-linearly (SF_TEXT_EXPONENT=0.5) with the sheet, and the 151 non-border context districts are drawn but unnamed. A1 or A2 remains the better wall sheet: A1 sets Rajasthan at 9.50 pt. |
| 25 | human visual inspection | **NOT TESTED** | I cannot view images. Colour, spacing and overall composition were measured numerically only. |

## Errors found and fixed during Round 2

1. **Disputed slivers were being labelled as neighbours (fixed).** The 22 `DISPUTED AREA (RAJASTHAN-GUJARAT)` pockets are contested slivers, not districts, but Round 1 showed they only registered at the 1 000 m tolerance and vanished at 250 m — i.e. they were tolerance artefacts. **Fix:** `02_adjacency.py` now excludes them from the neighbour set and writes them to `data/metadata/DISPUTED_SLIVERS.csv` instead, so nothing is silently dropped and no fake 'neighbour' enters the table.
2. **Pakistani provinces were being coloured as Indian states (fixed).** See Round 1 finding 1 — the same `Punjab` collision also gave Pakistani Punjab the Indian Punjab fill. Now all Pakistani districts take the single Pakistan fill, with province names drawn on top.
3. **Latin fallback missing (fixed).** DejaVu Sans added to the font family chain so `·`, `N` and the scale-bar numerals render instead of falling back to tofu.

## Round 2 verdict

Rendering **accepted**, subject to the two REVIEW items and the one NOT TESTED item above. All 41 Rajasthan districts, all 26 border-sharing neighbours and all six region labels are present, un-duplicated, correctly anchored and fully covered by the embedded font. Page boxes are exact to within 1 mm on all three sheets.
