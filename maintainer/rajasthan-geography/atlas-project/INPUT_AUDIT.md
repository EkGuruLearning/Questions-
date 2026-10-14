# INPUT AUDIT — user-supplied reference material

**Prepared:** 2026-10-14
**Scope:** every file the user said they had uploaded, plus everything actually
found in the workspace.

---

## 1. Headline finding: no user reference files were received

The brief states that reference material had been uploaded for this project —
a Rajasthan district map, a Gujarat map, a Punjab map, a Madhya Pradesh map,
an Uttar Pradesh map, an India political map, a Pakistan-border reference map,
and a KML file.

**None of those files reached this workspace.** The audit below is the evidence.

| Item | Expected | Found |
|---|---|---|
| `data/raw/reference_uploads/` (staging folder I created for them) | 1+ files | **0 files — empty directory** |
| Files anywhere in the workspace with extension `.kml` / `.kmz` | ≥ 1 | **0** |
| Georeferenced rasters (`.tif` / `.geotiff` / `.jp2`) | ≥ 1 | **0** |
| GIS vectors uploaded by the user (`.shp` / `.gpkg` / `.geojson`) | ≥ 1 | **0** |
| Images (`.jpg` / `.png` / `.webp`) | several map scans | **0** |
| Any file modified/created after the repo checkout | — | only files I created myself |

Everything in the repository is pre-existing `Computer Network` study material
(45 PDFs plus one HTML and one ZIP), none of which is geographic.

**Consequence.** The `Rajasthan district map`, `Gujarat map`, `Punjab map`,
`Madhya Pradesh map`, `Uttar Pradesh map`, `India political map`,
`Pakistan-border reference map` and the **KML file** named in the brief could
not be inspected, georeferenced, reused, transformed or discarded, because they
were never available. This audit therefore has **no row for them** rather than
a fabricated row.

**What I did instead.** I sourced, downloaded and inspected independent
authoritative datasets (see `SOURCE_AUDIT.md`). The project does **not** depend
on any uploaded reference image. If the files are supplied later, the workflow
in `README.md § Re-auditing new uploads` folds them in without restarting.

---

## 2. Inventory of material actually used

| # | File (in `data/raw/`) | Format | Region | Admin year / version | CRS | Real GIS? | Status | Permissible role |
|---|---|---|---|---|---|---|---|---|
| 1 | `india_soi/08_RAJASTHAN.geojson` | GeoJSON | Rajasthan | **41 districts** (post 28-Dec-2024 framework) | EPSG:4326 | Yes — polygon dataset | Current | **Primary** geometry for Rajasthan |
| 2 | `india_soi/24_GUJARAT.geojson` | GeoJSON | Gujarat | **33 districts** | EPSG:4326 | Yes | Current | Primary geometry for Gujarat |
| 3 | `india_soi/23_MADHYA_PRADESH.geojson` | GeoJSON | Madhya Pradesh | **55 districts** | EPSG:4326 | Yes | Current | Primary geometry for MP |
| 4 | `india_soi/09_UTTAR_PRADESH.geojson` | GeoJSON | Uttar Pradesh | **75 districts** | EPSG:4326 | Yes | Current | Primary geometry for UP |
| 5 | `india_soi/06_HARYANA.geojson` | GeoJSON | Haryana | **22 districts** | EPSG:4326 | Yes | Current | Primary geometry for Haryana |
| 6 | `india_soi/03_PUNJAB.geojson` | GeoJSON | Punjab (India) | **23 districts** (includes Malerkotla) | EPSG:4326 | Yes | Current | Primary geometry for Punjab |
| 7 | `india_soi/states.geojson` | GeoJSON | India | 40 features incl. 5 "DISPUTED" | EPSG:4326 | Yes | Current | Locator inset + state outlines |
| 8 | `india_soi/_disputed.geojson` | GeoJSON | India | 28 features; 22 marked `DISPUTED (RAJASTHAN & GUJARAT)` | EPSG:4326 | Yes | Unverifiable ownership | Excluded from the sheet, disclosed |
| 9 | `pakistan_opencarto/pk-country-district.geojson` | GeoJSON | Pakistan | **160 districts**, COD-AB v01, valid **2022-09-09** | EPSG:4326 | Yes | Current as at snapshot date | Primary geometry for Pakistan |
| 10 | `pakistan_opencarto/pk-country-province.geojson` | GeoJSON | Pakistan | ADM1 provinces | EPSG:4326 | Yes | Same | Province labels |
| 11 | `pakistan_opencarto/pk-country-region.geojson` | GeoJSON | Pakistan | national outline | EPSG:4326 | Yes | Same | Extent checks |
| 12 | `fonts/NotoSansDevanagari-*.ttf` | TrueType | — | noto-fonts clone 2026-10-14 | n/a | n/a | Current | Hindi label rendering (OFL 1.1) |

All twelve files are hashed in `data/metadata/RAW_FILE_INVENTORY.csv`.

---

## 3. Material examined and **rejected**

| Candidate | Why rejected |
|---|---|
| `datta07/INDIAN-SHAPEFILES` — `STATES/RAJASTHAN/RAJASTHAN_DISTRICTS.geojson` (3.6 GB clone, 256 stars) | Census-2011 vintage: Rajasthan **33** districts, Gujarat 33, MP 52, Punjab 22. Obsolete for Rajasthan since 2023 and again since Dec 2024. **Retained only as an independent cross-check** of Rajasthan's area and outline length. |
| `udit-001/india-maps-data` | Same 2011 vintage (Rajasthan 33, MP 52, Punjab 22). Rejected as primary; kept as a corroborating count source. |
| `yashveeeeeeer/india-geodata` release assets (`LGD_Districts.parquet`, `SOI_Districts.parquet`, `bhuvan_districts.parquet`) | **Could not be downloaded.** GitHub release assets are served from `release-assets.githubusercontent.com`, which is blocked in this environment (verified: connection reset). Only `github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`, `pypi.org` and `files.pythonhosted.org` are reachable. The in-repo copies are Census-2001/2011 shapefiles only. |
| `wmgeolab/geoBoundaries` (`releaseData/gbOpen/PAK/ADM2/*`) | All data files are Git-LFS pointers (~130 B). LFS payloads are served from `media.githubusercontent.com`, also blocked. No usable geometry. |
| `vineyardbovines/geojson` | 1.5 GB clone; contains city-level GeoJSON only for Pakistan, not district polygons. Rejected. |
| `missinglink/osm-boundaries` | 1.36 GB, last pushed 2019; OSM dump would predate recent Pakistani district changes. Rejected in favour of the 2022 COD-AB snapshot. |
| Any AI-generated map image | Explicitly out of scope. No text-to-image model was used for any geometry, at any stage. |

---

## 4. Standing rule applied to every input

No uploaded or downloaded image was ever treated as a source of coordinates.
Screenshots, watermarked stock maps and illustrations — had any arrived — would
have been permitted only to guide colour, labelling and composition, never to
override verified boundary coordinates. Since none arrived, this rule was
trivially satisfied.

---

## 5. If the reference files arrive later

1. Drop them into `data/raw/reference_uploads/` (already created, currently empty).
2. Run `.venv/bin/python scripts/00_audit_uploads.py` — it records format, CRS,
   layer list, feature count, SHA-256 and, for GeoJSON/KML, the district-name
   list of every new file into `data/metadata/UPLOAD_AUDIT.csv`.
3. Compare those names against `data/metadata/DISTRICT_INVENTORY.csv`. Any
   divergence is a **data conflict to resolve**, not a spelling to copy.
4. Only if an upload is a genuine vector dataset in a documented CRS and carries
   a newer administrative vintage than the sources above may it replace primary
   geometry — and then `01 → 02 → 03 → 99` must be re-run end to end.
