# राजस्थान — सीमावर्ती ज़िला एटलस
## Rajasthan Border District Atlas

A reproducible, source-documented, geographically validated district map of
Rajasthan and every district that shares a boundary with it across the
international border with Pakistan and the interstate borders with Punjab,
Haryana, Uttar Pradesh, Madhya Pradesh and Gujarat.

**District count is 41, not 33 and not 50.** Rajasthan went 33 → 50 (Aug 2023)
→ **41** (cabinet decision of 28 Dec 2024, which annulled 9 of the 17 districts
created in 2023 and all three new divisions). The subtitle on the sheet is
generated from the layer at render time, so it can never drift out of date.

---

## 1. What was actually built

| | |
|---|---|
| Geometry | 431 district polygons, 0 invalid, none simplified or moved |
| Rajasthan | **41 districts**, 7 divisions |
| Border-sharing neighbours | **36** (6 Gujarat, 7 Haryana, 10 MP, 2 Punjab, 2 UP, 9 Pakistan) |
| Labels drawn | 237, all anchored inside their own polygon, 0 duplicates |
| Sheets | A1 841×594, A2 594×420, A3 420×297 mm — identical layout, scaled |
| Adjacency evidence | 3 independent methods converge on the same answer |
| Automated tests | 27 PASS / 1 REVIEW / 2 NOT TESTED / 0 FAIL |

---

## 2. Directory layout

```
Rajasthan Geography Maps/
├── INPUT_AUDIT.md            audit of user-supplied material (none arrived)
├── SOURCE_AUDIT.md           honest source count + evidence hierarchy
├── SOURCES_REGISTER.csv      16 registered sources
├── BOUNDARY_RELATIONS.csv    89 machine-generated border relationships
├── UNRESOLVED_DISCREPANCIES.md   7 OPEN items, none hidden
├── QA_REPORT.md              acceptance-test battery
├── README.md                 this file
├── reports/
│   ├── REVIEW_ROUND_1.md     source & geometry audit
│   ├── REVIEW_ROUND_2.md     label & cartography audit
│   └── REVIEW_ROUND_3.md     blind final verification
├── data/
│   ├── raw/                  original downloads, never modified (gitignored)
│   │   ├── india_soi/        Survey-of-India-derived district GeoJSON
│   │   ├── pakistan_opencarto/  WFP/OCHA COD-AB v01
│   │   └── reference_uploads/   EMPTY — for your files
│   ├── processed/            master GeoPackage (gitignored, regenerable)
│   └── metadata/             inventories, validation, label manifests, hashes
├── scripts/                  01 → 04 build, 05 → 07 review, 99 validate
├── fonts/                    Noto Sans Devanagari (OFL 1.1)
├── gis_project/              editable QGIS project (.qgz)
├── exports/                  A1/A2/A3 PDF + PNG  (PDFs gitignored)
└── previews/                 viewable preview sheet
```

---

## 3. Reproduce from scratch

```bash
cd "Rajasthan Geography Maps"

python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt

# 0. (optional) drop reference files into data/raw/reference_uploads/ then
.venv/bin/python scripts/00_audit_uploads.py

# 1. fetch sources (needs network to github.com)
bash scripts/00_fetch_sources.sh

# 2. build the master GeoPackage + validation battery
.venv/bin/python scripts/01_build_master.py

# 3. derive the border-sharing table from geometry
.venv/bin/python scripts/02_adjacency.py

# 4. render A1 / A2 / A3 PDFs + PNGs + preview
.venv/bin/python scripts/03_render.py

# 5. write the QGIS project
.venv/bin/python scripts/04_make_qgis_project.py

# 6. three review rounds
.venv/bin/python scripts/05_review_round1.py
.venv/bin/python scripts/06_review_round2.py
.venv/bin/python scripts/07_review_round3.py

# 7. acceptance tests → reports/QA_REPORT.md
.venv/bin/python scripts/99_validate.py
```

Every script is idempotent and independent of any manual edit. **No step
involves opening an image editor.**

---

## 4. Projections and measurement conventions

| Purpose | CRS |
|---|---|
| Master storage | EPSG:4326 (WGS 84) — retained for traceability |
| Map rendering | `+proj=lcc +lat_1=25 +lat_2=30 +lat_0=27 +lon_0=71 +datum=WGS84 +units=m` — conformal, standard parallels bracket the 23 N–31 N mapped band |
| Locator inset | EPSG:32644 |
| Lengths | geodesic on the WGS 84 ellipsoid (`pyproj.Geod`) — free of projection scale error |
| Areas | geodesic (`Geod.geometry_area_perimeter`) |

**Adjacency method.** The Indian and Pakistani layers are independent sources,
so `A.boundary ∩ B.boundary` undercounts badly. Instead, for each pair:

```
l1 = geodesic length of A's boundary within 1000 m of B
l2 = geodesic length of B's boundary within 1000 m of A
shared = (l1 + l2) / 2
```

A pair counts as a **shared boundary** only when both `l1` and `l2` exceed
1 500 m, which excludes corner/point touches. The 1 000 m tolerance is the
measured 94th percentile of the real seam error (median offset 50 m), not a
round number picked for convenience.

---

## 5. Key findings you should know before using this for exams

1. **41 districts, 7 divisions** — not 33, not 50.
2. **Pakistan touches 9 districts, but not the 9 usually listed.**
   Dera Ghazi Khan, Muzaffargarh and Rajanpur **do not** touch Rajasthan;
   Ghotki, Khairpur and Sukkur **do**. The three non-touching ones are hatched
   on the sheet with a footnote.
3. **The district counts match published lists exactly** — Punjab 2,
   Haryana 7, Uttar Pradesh 2, Madhya Pradesh 10, Gujarat 6, Pakistan 9.
4. **The border lengths do not.** See `UNRESOLVED_DISCREPANCIES.md` D-2. If an
   exam asks for a length, the published figure is what the answer key expects;
   if you are asked to defend it from a map, it does not survive measurement.
   Both are tabulated in `data/metadata/BORDER_LENGTH_CROSSCHECK.csv`.

---

## 6. Sources and licences

| Layer | Source | Licence / status |
|---|---|---|
| Indian districts | Survey-of-India-derived GeoJSON, `drguptavivek/soi-geojson` | **Not an official SoI product; redistribution terms unconfirmed.** Study use. |
| Pakistani districts | WFP / OCHA COD-AB v01 via `PRABHMANNAT/OpenCarto`, valid 2022-09-09 | **CC BY-IGO** (attribution required, no endorsement) |
| Fonts | Noto Sans Devanagari, `notofonts/noto-fonts` | **SIL OFL 1.1** (embedding permitted) |

Full register: `SOURCES_REGISTER.csv`. Evidence discussion: `SOURCE_AUDIT.md`.

**Do not publish this commercially** — the Indian layer's redistribution terms
are unresolved.

---

## 7. Re-auditing new uploads

Your reference maps and KML never reached the workspace — see
`INPUT_AUDIT.md`. If you re-upload them:

1. Put them in `data/raw/reference_uploads/`.
2. `.venv/bin/python scripts/00_audit_uploads.py`
3. Read `data/metadata/UPLOAD_AUDIT.csv` and
   `data/metadata/UPLOAD_AUDIT_DIVERGENCE.csv`.

An upload may replace primary geometry **only** if it is a genuine vector
dataset in a documented CRS **and** carries a newer administrative vintage than
the sources above. Otherwise it is a style reference. Either way, re-run
`01 → 02 → 03 → 99` end to end.

---

## 8. Making a change (the three revision passes)

1. Read `reports/REVIEW_ROUND_*.md` and `UNRESOLVED_DISCREPANCIES.md`.
2. Decide whether the change touches geometry, administrative data, labels,
   layout or exports.
3. Edit the **underlying** layer — the raw source, `data/metadata/district_names_hi.csv`,
   or `scripts/atlas_style.py`. Never patch the PNG.
4. Re-run the affected scripts from § 3.
5. Re-run `99_validate.py`; the previous manifest stays in
   `data/metadata/DELIVERED_FILE_HASHES.csv` for comparison.
6. Record the change in this file's change log below.

### Change log

| Date | Change | Files touched | Re-run |
|---|---|---|---|
| 2026-10-14 | Initial build: 41-district framework, 36 border neighbours, A1/A2/A3 + preview | all | all |
| 2026-10-14 | Round 1: fixed `Punjab` admin-name collision (Indian state vs Pakistani province were sharing one key, so Pakistani Punjab was being filled with the Indian Punjab colour and the big `पंजाब` label was anchored on a cross-country union) | `01_build_master.py`, `03_render.py`, `atlas_style.py`, `data/metadata/district_names_hi.csv`, `99_validate.py` | 01, 02, 03, 99 |
| 2026-10-14 | Round 1: removed double-scaled text metrics in label collision boxes | `03_render.py` | 03 |
| 2026-10-14 | Round 1: added DejaVu Sans as the Latin fallback (`·`, `N`, numerals were tofu) | `03_render.py`, `99_validate.py` | 03, 99 |
| 2026-10-14 | Round 2: excluded the 22 disputed Rajasthan–Gujarat slivers from the adjacency table (they are contested pockets, not districts, and only appeared at the wider tolerance) | `02_adjacency.py` | 02, 03, 99 |
| 2026-10-14 | Round 3: fixed ink-threshold (240 counted the cream background as ink) and the figure/image coordinate flip in the panel probes | `06_review_round2.py` | 06 |

---

## 9. Honest limitations

Read `UNRESOLVED_DISCREPANCIES.md` before relying on this. The three that
matter most:

1. **No gazette notification was retrievable.** The 41-district count rests on
   six corroborating contemporaneous reports. This is the weakest link.
2. **The Pakistani snapshot is dated 2022-09-09.**
3. **No human has looked at the printed sheet.** Open the A1 PDF at 100 % before
   printing.
