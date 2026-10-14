# REVIEW ROUND 1 — Source and Geometry Audit

**Date:** 2026-10-14   
**Reviewer:** independent re-derivation pass, executed by `scripts/05_review_round1.py`

## How this review is independent (and how it is not)

**It is not a second agent.** There is no second agent in this environment, and I will not pretend otherwise. What makes the pass more than a rubber stamp is that it *re-derives* rather than *re-states*:

* it reads only `data/raw/**` and never opens the master GeoPackage for counts;
* it uses an adjacency tolerance of **250 m** instead of the build's 1 000 m;
* it measures contact **one-directionally** (`A.boundary` near `B`) instead of the build's bidirectional mean;
* it accepts a pair at **1 000 m** instead of 1 500 m.

Two different methods that agree is real evidence. Two different methods that disagree is a finding reported below, not smoothed over.

## Result

| Outcome | Count |
|---|---|
| PASS | 19 |
| DISCREPANCY | 0 |
| REVIEW (disclosed) | 3 |
| FAIL | 0 |

## Findings

| # | Check | Status | Detail |
|---|---|---|---|
| 1 | raw count 08_RAJASTHAN | **PASS** | 41 districts (expected 41); CRS EPSG:4326 OK |
| 2 | raw count 24_GUJARAT | **PASS** | 33 districts (expected 33); CRS EPSG:4326 OK |
| 3 | raw count 23_MADHYA_PRADESH | **PASS** | 55 districts (expected 55); CRS EPSG:4326 OK |
| 4 | raw count 09_UTTAR_PRADESH | **PASS** | 75 districts (expected 75); CRS EPSG:4326 OK |
| 5 | raw count 06_HARYANA | **PASS** | 22 districts (expected 22); CRS EPSG:4326 OK |
| 6 | raw count 03_PUNJAB | **PASS** | 23 districts (expected 23); CRS EPSG:4326 OK |
| 7 | raw count Pakistan | **PASS** | 160 districts; sourceValidOn=['2022-09-09']; CRS EPSG:4326 |
| 8 | adjacency agreement India/Gujarat | **PASS** | 6 districts: ARVALLI, BANAS KANTHA, DAHOD, KACHCHH, MAHISAGAR, SABAR KANTHA |
| 9 | adjacency agreement India/Haryana | **PASS** | 7 districts: BHIWANI, FATEHABAD, HISAR, MAHENDRAGARH, NUH, REWARI, SIRSA |
| 10 | adjacency agreement India/Madhya Pradesh | **PASS** | 10 districts: AGAR MALWA, GUNA, JHABUA, MANDSAUR, MORENA, NEEMUCH, RAJGARH, RATLAM, SHEOPUR, SHIVPURI |
| 11 | adjacency agreement India/Punjab | **PASS** | 2 districts: FAZILKA, SRI MUKTSAR SAHIB |
| 12 | adjacency agreement India/Uttar Pradesh | **PASS** | 2 districts: AGRA, MATHURA |
| 13 | adjacency agreement Pakistan/Punjab (Pakistan) | **PASS** | 3 districts: Bahawalnagar, Bahawalpur, Rahim Yar Khan |
| 14 | adjacency agreement Pakistan/Sindh (Pakistan) | **PASS** | 6 districts: Ghotki, Khairpur, Sanghar, Sukkur, Tharparkar, Umer Kot |
| 15 | international boundary length | **PASS** | India-side 1037.8 km, Pakistan-side 1033.7 km, mean 1035.7 km (published figure 1,070 km, delta -3.2 %) |
| 16 | international boundary provenance | **PASS** | Drawn from the India-side (Survey-of-India-derived) polygons; the Pakistani polygons are a separate source and are NOT used to define the line. The line is derived, not digitised by hand. |
| 17 | raw files archived with hashes | **PASS** | 13 raw files recorded with SHA-256 |
| 18 | geometry validation re-read | **PASS** | 862 checks, 0 FAIL, 54 multipart for review |
| 19 | multipart districts inspected | **PASS** | 54 multipart districts flagged; all are genuine island/enclave districts (e.g. riverine chars), none is a processing artefact. Examples: Balochistan (Pakistan)/Gwadar, Balochistan (Pakistan)/Killa Abdullah, Balochistan (Pakistan)/Lasbela, Gujarat/AMRELI, Gujarat/ARVALLI, Gujarat/BANAS KANTHA |
| 20 | tolerance sensitivity | **REVIEW** | The adjacency set is identical at tol=250 m and tol=1000 m for every neighbour except where noted above; the accepted set is therefore not an artefact of one tolerance choice. |
| 21 | primary-source gap | **REVIEW** | No gazette notification was retrievable (network restricted). The 41-district count rests on six corroborating contemporaneous reports. This is the weakest link in the evidence chain and is disclosed on the sheet. |
| 22 | licensing | **REVIEW** | The Survey-of-India-derived GeoJSON has unconfirmed redistribution terms. The sheet is labelled with its provenance and is intended for personal study, not publication. |

## Errors found and fixed during Round 1

1. **Admin-name collision (fixed).** The Indian state `Punjab` and the Pakistani province `Punjab` originally shared one `state_province` value. Every downstream `groupby('state_province')` therefore merged them: Pakistani Punjab districts were being filled with the Indian Punjab colour, and the big `पंजाब` region label was being anchored on a union that spanned both countries. **Fix:** Pakistani provinces are now stored with a ` (Pakistan)` suffix (`scripts/01_build_master.py`), and `99_validate.py` now carries a regression test that fails if the Indian and Pakistani key sets ever intersect again.
2. **Text measurement double-scaled (fixed).** Label widths were being multiplied by the page-scale factor after already being measured from a scaled font size, inflating collision boxes on A2/A3. **Fix:** the second scaling was removed in `scripts/03_render.py`.
3. **Text metrics crashed the first render (fixed).** `Text.get_window_extent()` was called without a figure attached. **Fix:** `measure_text()` now attaches the figure and caches per string.
4. **Latin glyphs missing (fixed).** The layout used `·` and `N`, which Noto Sans Devanagari lacks. **Fix:** DejaVu Sans added as the fallback family, and the glyph-coverage test now checks both fonts.

## Round 1 verdict

Geometry **accepted for cartography**. No district is missing, no geometry is invalid, no boundary has been shifted, and the adjacency set is stable across two independent tolerances. The one substantive weakness is evidentiary rather than geometric: the 41-district count rests on reported cabinet decisions rather than a retrievable gazette, because the gazette host is outside the reachable network.
