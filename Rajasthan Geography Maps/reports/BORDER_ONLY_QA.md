# QA — Rajasthan Border Districts, clean A4 map

**Script:** `scripts/10_render_border_only.py`  
**Audit:** `scripts/11_verify_border_only.py`  
**Master:** `data/processed/rajasthan_border_atlas.gpkg`

## Summary

| Status | Count |
|---|---|
| PASS | 18 |
| REVIEW | 2 |
| **Total** | **20** |

## Detail

| # | Test | Status | Detail |
|---|---|---|---|
| 1 | district set re-derived independently from the master + adjacency | **PASS** | 77 districts: 41 Rajasthan + 36 border-sharing. Per unit: Gujarat 6, Haryana 7, Madhya Pradesh 10, Punjab 2, Punjab (Pakistan) 3, Rajasthan 41, Sindh (Pakistan) 6, Uttar Pradesh 2 |
| 2 | shipped district manifest matches the re-derived set exactly | **PASS** | BORDER_ONLY_DISTRICTS.csv holds 77 rows; difference vs independent derivation: 0 |
| 3 | no non-bordering district is included | **PASS** | 354 of 431 districts in the master are deliberately NOT drawn (the atlas's context districts, graticule, panels and locator are all omitted). Spot-check absent: ['Gwalior', 'Indore', 'Lahore'] |
| 4 | projection distortion re-measured on this map's own extent | **PASS** | LCC 23.71 / 29.485 N, lat_0 26.5975, lon_0 73.516. Max scale error 0.1264 % = 0.0321 mm per inch (mean 0.0775 %), measured over a 0.25-degree lattice covering 22.503-30.692 N, 68.178-78.854 E. |
| 5 | Landscape: page is A4 landscape (297 x 210 mm) | **PASS** | PNG 3507x2480 px, aspect 1.4141 vs expected 1.4143; PDF 6562 kB |
| 6 | Landscape: both required border types are drawn | **PASS** | international red #C62828 = 21,605 px; Rajasthan interstate yellow #F2C200 = 71,945 px |
| 7 | Landscape: omitted furniture really is absent (no graticule) | **PASS** | 39,346 px near the graticule colour (antialiased district edges), but the longest straight run is 101 px. A real graticule measures 449 px on the atlas A1. No graticule is drawn here. |
| 8 | Landscape: ink coverage is sane | **PASS** | dark-pixel fraction 0.0287 |
| 9 | Landscape: every one of the 77 districts is labelled exactly once | **PASS** | manifest holds 77 labels, 77 unique districts; 77 of them belong to the re-derived 77 |
| 10 | Landscape: no label displaced off its district | **REVIEW** | 2 of 77 labels needed a nudge from the collision engine; max shift 71.7 px |
| 11 | Landscape: labels are bilingual (Hindi + English) | **PASS** | 77/77 Hindi strings contain Devanagari; 77/77 English strings contain Latin |
| 12 | Landscape: every label anchor lies inside a drawn polygon | **PASS** | 77/77 anchors fall inside one of the 77 districts |
| 13 | Portrait: page is A4 portrait (210 x 297 mm) | **PASS** | PNG 2480x3507 px, aspect 0.7072 vs expected 0.7071; PDF 6524 kB |
| 14 | Portrait: both required border types are drawn | **PASS** | international red #C62828 = 20,429 px; Rajasthan interstate yellow #F2C200 = 67,191 px |
| 15 | Portrait: omitted furniture really is absent (no graticule) | **PASS** | 36,145 px near the graticule colour (antialiased district edges), but the longest straight run is 46 px. A real graticule measures 449 px on the atlas A1. No graticule is drawn here. |
| 16 | Portrait: ink coverage is sane | **PASS** | dark-pixel fraction 0.0281 |
| 17 | Portrait: every one of the 77 districts is labelled exactly once | **PASS** | manifest holds 77 labels, 77 unique districts; 77 of them belong to the re-derived 77 |
| 18 | Portrait: no label displaced off its district | **REVIEW** | 4 of 77 labels needed a nudge from the collision engine; max shift 71.7 px |
| 19 | Portrait: labels are bilingual (Hindi + English) | **PASS** | 77/77 Hindi strings contain Devanagari; 77/77 English strings contain Latin |
| 20 | Portrait: every label anchor lies inside a drawn polygon | **PASS** | 77/77 anchors fall inside one of the 77 districts |

## Scope of this map

Only 77 districts are drawn: Rajasthan's 41, plus the 36
districts that genuinely share a border with Rajasthan.
Everything else in the master is excluded by construction.
Furniture is limited to a north arrow and a scale bar; the
graticule, legend, locator inset and study panels that appear
on the full atlas are all deliberately omitted.
