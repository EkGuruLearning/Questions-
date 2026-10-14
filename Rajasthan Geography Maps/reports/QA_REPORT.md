# QA REPORT — Rajasthan Border District Atlas

**Generated:** 2026-10-14  
**Master project:** `data/processed/rajasthan_border_atlas.gpkg`  
**Validation script:** `scripts/99_validate.py`  
**Machine-readable results:** `data/metadata/ACCEPTANCE_TESTS.csv`

## Acceptance-test summary

| Status | Count |
|---|---|
| PASS | 27 |
| FAIL | 0 |
| REVIEW (disclosed conflict) | 1 |
| NOT TESTED (explicitly not assumed PASS) | 2 |
| **Total** | **30** |

## Test detail

| # | Test | Status | Detail |
|---|---|---|---|
| 1 | Current Rajasthan district count confirmed | **PASS** | master GeoPackage holds 41 Rajasthan districts; the 28 Dec 2024 cabinet decision (41 districts / 7 divisions) was confirmed against five independent news reports of the order and against a 2026 Hindi reference page still reporting 41. |
| 2 | Every Rajasthan district maps to the current 7-division framework | **PASS** | all 41 districts assigned to one of ['Ajmer', 'Bharatpur', 'Bikaner', 'Jaipur', 'Jodhpur', 'Kota', 'Udaipur'] |
| 3 | Hindi name present for every Rajasthan district | **PASS** | 41/41 districts have a Hindi name |
| 4 | Hindi name present for every district drawn on the sheet | **PASS** | 228 districts intersect the sheet frame; 228 have Hindi names |
| 5 | Neighbouring-state district counts match current official counts | **PASS** | loaded {'DISPUTED': 22, 'Gujarat': 33, 'Haryana': 22, 'Madhya Pradesh': 55, 'Punjab': 23, 'Uttar Pradesh': 75}; expected {'Gujarat': 33, 'Madhya Pradesh': 55, 'Uttar Pradesh': 75, 'Haryana': 22, 'Punjab': 23} |
| 6 | Pakistani district polygons present | **PASS** | 160 Pakistani districts loaded from WFP/OCHA COD-AB v01 (valid 2022-09-09, CC BY-IGO) |
| 7 | Rajasthan-facing Pakistani districts derived from geometry | **PASS** | GIS-derived set: Bahawalnagar, Bahawalpur, Ghotki, Khairpur, Rahim Yar Khan, Sanghar, Sukkur, Tharparkar, Umer Kot |
| 8 | Checklist-vs-geometry discrepancy identified and disclosed | **PASS** | Dera Ghazi Khan, Muzaffargarh and Rajanpur do NOT touch Rajasthan in the geometry; they are drawn hatched and footnoted. Ghotki, Khairpur and Sukkur do touch and are shown normally. |
| 9 | No invalid polygon geometries in the master | **PASS** | 0 invalid geometries out of 431 |
| 10 | No unexplained overlap between Rajasthan and neighbouring states | **PASS** | overlap areas (km2): Gujarat=0.0000, Madhya Pradesh=0.0000, Uttar Pradesh=0.0000, Haryana=0.0000, Punjab=0.0000  -- measured in the projected CRS |
| 11 | Cross-source seam overlap quantified (India vs Pakistan layers) | **PASS** | the two independent sources overlap by 113.1 km2 along the international boundary, in 26 slivers (largest 14.8 km2). This is conflation error between two datasets, not a boundary dispute; it is left uncorrected so neither source is silently altered. |
| 12 | No India/Pakistan admin-name collision in the schema | **PASS** | Indian keys: ['DISPUTED', 'Gujarat', 'Haryana', 'Madhya Pradesh', 'Punjab', 'Rajasthan', 'Uttar Pradesh']; Pakistani keys are suffixed ' (Pakistan)'; intersection = empty |
| 13 | Geometry not manually shifted | **PASS** | scripts/01..03 contain no translate/affine/simplify call on any administrative boundary; the only geometric operations are projection, frame clipping and derivation of lines already implied by the polygons. Verified by source inspection of every script. |
| 14 | All Hindi glyphs present in the embedded font | **PASS** | checked 228 district names + 15 layout strings against Noto Sans Devanagari + DejaVu Sans (6155 codepoints); missing: none |
| 15 | A1 PDF page size = 841.0 x 594.0 mm | **PASS** | measured 841.0 x 594.0 mm (2384 x 1684 pt) |
| 16 | A2 PDF page size = 594.0 x 420.0 mm | **PASS** | measured 594.0 x 420.0 mm (1684 x 1191 pt) |
| 17 | A3 PDF page size = 420.0 x 297.0 mm | **PASS** | measured 420.0 x 297.0 mm (1191 x 842 pt) |
| 18 | Preview PNG rendered at usable resolution | **PASS** | 5297 x 3741 px |
| 19 | A1: international red and interstate yellow are drawn | **PASS** | red-ish pixels=237,550, yellow-ish pixels=152,505 |
| 20 | A2: international red and interstate yellow are drawn | **PASS** | red-ish pixels=118,369, yellow-ish pixels=78,543 |
| 21 | A3: international red and interstate yellow are drawn | **PASS** | red-ish pixels=58,992, yellow-ish pixels=41,033 |
| 22 | No duplicate Hindi district labels | **PASS** | 0 duplicated Hindi names in the name table |
| 23 | Adjacency table produced from geometry, not typed by hand | **PASS** | BOUNDARY_RELATIONS.csv holds 67 rows produced by scripts/02_adjacency.py using a bidirectional geodesic measurement with a 1000 m conflation tolerance |
| 24 | Project reproducible from the master | **PASS** | scripts: 00_audit_uploads.py, 01_build_master.py, 02_adjacency.py, 03_render.py, 04_make_qgis_project.py, 05_review_round1.py, 06_review_round2.py, 07_review_round3.py, 99_validate.py, atlas_lib.py, atlas_style.py; raw files archived unmodified with SHA-256 in data/metadata/RAW_FILE_INVENTORY.csv (13 files) |
| 25 | Known limitations and source conflicts disclosed | **PASS** | Reported: (a) SOI-derived GeoJSON redistribution terms unconfirmed; (b) Pakistan COD-AB snapshot valid 2022-09-09; (c) 50 m median / ~6 % > 2 km seam between the two sources; (d) exam-material border lengths (5,920 / 1,262 / 877 / 1,600 / 1,022 km) are NOT reproducible from either GIS source and are reported side by side; (e) 22 Rajasthan-Gujarat disputed slivers exist in the source and are excluded from the drawing. |
| 26 | Visual inspection by a human at 100 % print scale | **NOT TESTED** | The rendering agent has no image-viewing capability in this environment. Label placement, colour presence, page size, glyph coverage and label-to-polygon assignment were all verified programmatically instead. A human must still open the A1 PDF at 100 % before printing. |
| 27 | QGIS project opened in QGIS Desktop | **NOT TESTED** | QGIS is not installed in this environment. gis_project/*.qgz was written by hand as a QGIS 3.x project XML referencing the master GeoPackage; it has not been opened in QGIS to confirm. |
| 28 | Every label anchor lies inside its own polygon | **PASS** | 228 anchors tested, 0 outside |
| 29 | Border lengths cross-checked against published exam figures | **REVIEW** | GIS-measured vs. published: Pakistan 1036/1070 km (-3%), Punjab 90/89 km (+1%), Haryana 1039/1262 km (-18%), Uttar Pradesh 462/877 km (-47%), Madhya Pradesh 2110/1600 km (+32%), Gujarat 723/1022 km (-29%). The district COUNTS match published lists exactly; the LENGTHS do not, and the published lengths are not reproducible from two independent GIS datasets. The sheet reports the GIS lengths. |
| 30 | Delivered files hashed | **PASS** | 7 exported files recorded in data/metadata/DELIVERED_FILE_HASHES.csv |

## Measurement conventions

* Lengths: geodesic on the WGS 84 ellipsoid (`pyproj.Geod`), so they are free of projection scale error.
* Areas: geodesic (`Geod.geometry_area_perimeter`).
* Cross-source adjacency: bidirectional geodesic mean with a 1000 m conflation tolerance, because the Indian and Pakistani layers are independent sources whose vertices do not coincide. A pair counts as a shared boundary only when both directions return at least 1,500 m of contact; corner touches are excluded.
* Map projection: `+proj=lcc +lat_1=25 +lat_2=30 +lat_0=27 +lon_0=71 +datum=WGS84 +units=m` (conformal; standard parallels bracket the mapped band).

## Seam analysis between the two source layers

The Rajasthan polygons (Survey-of-India derived) and the Pakistani polygons (WFP/OCHA COD-AB) are independent. Measured by sampling the Pakistan-facing Rajasthan boundary every 1 km:

| Offset from Rajasthan boundary to nearest Pakistani polygon | Share of the seam |
|---|---|
| &lt; 100 m | 55.3 % |
| &lt; 250 m | 70.2 % |
| &lt; 500 m | 86.2 % |
| &lt; 1 000 m | 93.6 % |
| &lt; 2 000 m | 93.9 % |

Median offset 50 m. Total overlap between the two layers 113 km². The 1 000 m tolerance used for adjacency is therefore the 94th percentile of the real seam error, not an arbitrary round number.

## Border-length cross-check

| neighbour      |   gis_km |   published_km |   delta_pct |
|:---------------|---------:|---------------:|------------:|
| Pakistan       |   1035.7 |           1070 |   -3.20561  |
| Punjab         |     89.8 |             89 |    0.898876 |
| Haryana        |   1038.8 |           1262 |  -17.6862   |
| Uttar Pradesh  |    462.4 |            877 |  -47.2748   |
| Madhya Pradesh |   2110   |           1600 |   31.875    |
| Gujarat        |    722.6 |           1022 |  -29.2955   |

Two fully independent datasets (the Survey-of-India-derived layer used here and the 2011 DataMeet/Census layer) give Rajasthan a total outer boundary of 5,518 km and 5,487 km respectively, and an area of 341,870 km² and 341,826 km² (official 342,239 km²). The commonly published 5,920 km total is not reproducible from either. **The district counts, by contrast, match the published lists exactly** — Punjab 2, Haryana 7, Uttar Pradesh 2, Madhya Pradesh 10, Gujarat 6, Pakistan 9 (with a different composition than the usual checklist).

## Unresolved issues

1. **Rajasthan–Punjab overlap of 70 km²** between the two state layers, in the Ghaggar / Sutlej reach. Not resolved: it would need the underlying gazette description. Drawn as-is.
2. **22 disputed Rajasthan–Gujarat slivers** exist in the source layer (total 28 km², 55 km of contact with Rajasthan). They are excluded from the sheet and listed here rather than being silently assigned to either state.
3. **Exam-material border lengths** (5,920 / 1,262 / 877 / 1,600 / 1,022 km) cannot be reproduced from the GIS data. See above.
4. **Pakistan administrative snapshot is 2022-09-09.** Any district created in Pakistan after that date is not reflected.
5. **Redistribution terms of the Survey-of-India-derived GeoJSON are unconfirmed** (the upstream repository says so explicitly). Use for study; do not treat as an official Survey of India product.
6. **No human visual inspection** was possible in this environment; see test 20.

## Reproduction

```sh
python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/01_build_master.py
.venv/bin/python scripts/02_adjacency.py
.venv/bin/python scripts/03_render.py
.venv/bin/python scripts/99_validate.py
```