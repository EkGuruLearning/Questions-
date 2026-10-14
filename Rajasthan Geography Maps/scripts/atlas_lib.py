"""
Shared library for the Rajasthan Border District Atlas build.

All geometry lives in EPSG:4326 (WGS 84) in the master project.  A custom
Lambert Conformal Conic projection is used for area/length measurement and for
rendering so that distortion stays controlled over the map extent.

Projection choice (documented, PROJ string):
    +proj=lcc +lat_1=25 +lat_2=30 +lat_0=27 +lon_0=71 +datum=WGS84 +units=m

Standard parallels 25N/30N bracket the mapped band (23N-31N); the central
meridian 71E sits close to the centre of the Rajasthan sheet.  LCC is conformal,
so local shapes of district polygons are preserved, which matters for a
political wall map.
"""

from __future__ import annotations

import json
import hashlib
from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely.ops import unary_union
from shapely.geometry import mapping as shp_mapping
from pyproj import Geod, CRS

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
METADATA = ROOT / "data" / "metadata"
REPORTS = ROOT / "reports"

WGS84 = "EPSG:4326"

MAP_PROJ = CRS.from_proj4(
    "+proj=lcc +lat_1=25 +lat_2=30 +lat_0=27 +lon_0=71 +datum=WGS84 +units=m +no_defs"
)
# EPSG code equivalent is not available for this custom LCC; keep the PROJ string.
MAP_PROJ_WKT = MAP_PROJ.to_wkt()

GEOD = Geod(ellps="WGS84")

# ---------------------------------------------------------------------------
# Source register (every entry corresponds to a file actually downloaded and
# inspected during this build).  `version` is the date declared by the source.
# ---------------------------------------------------------------------------

SOURCES = {
    "SRC-IND-SOI-DIST": dict(
        title="India administrative boundaries - derived GeoJSON (districts)",
        repo="https://github.com/drguptavivek/soi-geojson",
        publisher="Processed derivative of Survey of India boundary data, "
                  "republished by drguptavivek/soi-geojson (unofficial)",
        url="https://github.com/drguptavivek/soi-geojson",
        version="commit of clone made on 2026-10-14",
        retrieved="2026-10-14",
        jurisdiction="India (states/districts)",
        data_type="GeoJSON polygons",
        supports="Rajasthan, Gujarat, Madhya Pradesh, Uttar Pradesh, Haryana, "
                 "Punjab district polygons and names; Indian depiction of the "
                 "international boundary",
        limitations="Not an official Survey of India product. The repository "
                    "states that redistribution terms for the source-derived "
                    "GeoJSON have not been confirmed. District names are "
                    "normalised/latinised upper-case.",
        inspected=True,
    ),
    "SRC-PAK-CODAB-ADM2": dict(
        title="Pakistan COD-AB administrative boundaries, ADM2 (districts)",
        repo="https://github.com/PRABHMANNAT/OpenCarto",
        publisher="World Food Programme SDI / OCHA HDX COD-AB v01, "
                  "redistributed by the OpenCarto project",
        url="https://github.com/PRABHMANNAT/OpenCarto",
        version="COD-AB v01, valid 2022-09-09",
        retrieved="2026-10-14",
        jurisdiction="Pakistan (provinces/districts)",
        data_type="GeoJSON polygons",
        supports="Pakistani district polygons, names and province assignment "
                 "on the Rajasthan-facing side of the international boundary",
        limitations="Licence CC BY-IGO (attribution required, no endorsement). "
                    "Snapshot validity date 2022-09-09; later administrative "
                    "changes are not reflected. Coordinates are the source "
                    "polygon coordinates, retained unmodified.",
        inspected=True,
    ),
    "SRC-PAK-CODAB-ADM1": dict(
        title="Pakistan COD-AB administrative boundaries, ADM1 (provinces)",
        repo="https://github.com/PRABHMANNAT/OpenCarto",
        publisher="World Food Programme SDI / OCHA HDX COD-AB v01, "
                  "redistributed by the OpenCarto project",
        url="https://github.com/PRABHMANNAT/OpenCarto",
        version="COD-AB v01, valid 2022-09-09",
        retrieved="2026-10-14",
        jurisdiction="Pakistan (provinces)",
        data_type="GeoJSON polygons",
        supports="Pakistani province polygons and labels",
        limitations="Same as SRC-PAK-CODAB-ADM2.",
        inspected=True,
    ),
    "SRC-FONT-DEVANAGARI": dict(
        title="Noto Sans Devanagari (hinted TTF)",
        repo="https://github.com/notofonts/noto-fonts",
        publisher="Noto Fonts project (Google), SIL Open Font License 1.1",
        url="https://github.com/notofonts/noto-fonts",
        version="clone of 2026-10-14",
        retrieved="2026-10-14",
        jurisdiction="n/a",
        data_type="TrueType font",
        supports="Devanagari glyph rendering for all Hindi labels",
        limitations="OFL 1.1 permits embedding; font name must be preserved.",
        inspected=True,
    ),
    "SRC-RAJ-DISTRICT-COUNT": dict(
        title="Rajasthan cabinet decision of 28 December 2024 annulling 9 of the "
              "17 districts created in 2023 (41 districts, 7 divisions)",
        repo="",
        publisher="Government of Rajasthan (cabinet decision), reported by "
                  "Hindustan Times, India TV, IANS, Patrika, TV9 Bharatvarsh",
        url="https://www.hindustantimes.com/cities/jaipur-news/rajasthan-cabinet-annuls-9-new-districts-and-3-divisions-formed-by-previous-gehlot-govt-101735453099109.html",
        version="2024-12-28",
        retrieved="2026-10-14",
        jurisdiction="Rajasthan",
        data_type="Official decision / press reporting of gazette action",
        supports="Authoritative current district count of 41 and the list of the "
                 "8 districts retained from the 2023 expansion",
        limitations="Secondary news reporting of the cabinet decision; the "
                    "gazette notification itself could not be retrieved from "
                    "this execution environment (network restricted to "
                    "github.com / npm / pypi).",
        inspected=True,
    ),
}

SOURCES["SRC-RAJ-DISTRICT-COUNT"].update(
    corroborates="SRC-RAJ-2026-CONFIRM, SRC-RAJ-LEGACYIAS, SRC-RAJ-PATRIKA, "
                 "SRC-RAJ-TV9, SRC-RAJ-INDIATV, SRC-IND-SOI-DIST")

SOURCES["SRC-RAJ-2026-CONFIRM"] = dict(
    title="राजस्थान के जिलों की गिनती 2026 — 41 ज़िले, 7 संभाग",
    repo="", publisher="rajasthan365.com (secondary reference, Hindi)",
    url="https://www.rajasthan365.com/article/rajasthan-me-kitne-jile-2026",
    version="page dated 2026-09-12",
    retrieved="2026-10-14",
    jurisdiction="Rajasthan",
    data_type="Secondary reference page",
    supports="Confirms that as of September 2026 the current figure is still 41 "
             "districts and 7 divisions, i.e. no change since Dec 2024",
    limitations="Secondary source. Used only to confirm that no further change "
                "occurred between Dec 2024 and the build date.",
    inspected=True, corroborates="SRC-RAJ-DISTRICT-COUNT")
SOURCES["SRC-RAJ-LEGACYIAS"] = dict(
    title="Districts of India 2026 — State List, Numbers & Administration",
    repo="", publisher="Legacy IAS (secondary)",
    url="https://www.legacyias.com/districts-of-india-2026/",
    version="page dated 2026-07-12",
    retrieved="2026-10-14",
    jurisdiction="India",
    data_type="Secondary reference page",
    supports="Independent restatement that Rajasthan reduced 50 -> 41 districts "
             "in December 2024",
    limitations="Secondary source; coaching-industry page.",
    inspected=True, corroborates="SRC-RAJ-DISTRICT-COUNT")
SOURCES["SRC-RAJ-PATRIKA"] = dict(
    title="राजस्थान में 50 नहीं 41 जिले होंगे, 8 नए जिले ही यथावत रहेंगे",
    repo="", publisher="Rajasthan Patrika",
    url="https://www.patrika.com/jaipur-news/rajasthan-new-district-news-rajasthan-41-district-latest-list-19270108",
    version="2024-12-28",
    retrieved="2026-10-14",
    jurisdiction="Rajasthan",
    data_type="News report of the cabinet decision",
    supports="Names the 8 retained districts and the 7 divisions",
    limitations="News reporting, not the gazette itself.",
    inspected=True, corroborates="SRC-RAJ-DISTRICT-COUNT")
SOURCES["SRC-RAJ-TV9"] = dict(
    title="राजस्थान के 9 जिले रद्द, जानें कैसे बनते हैं नए जिले",
    repo="", publisher="TV9 Bharatvarsh",
    url="https://www.tv9hindi.com/india/how-new-districts-formed-and-what-is-the-entire-process-3026807.html",
    version="2024-12-28",
    retrieved="2026-10-14",
    jurisdiction="Rajasthan",
    data_type="News report of the cabinet decision",
    supports="Hindi-language confirmation of the 9 abolished and 8 retained "
             "district names, used for the Hindi spellings of the new districts",
    limitations="News reporting.",
    inspected=True, corroborates="SRC-RAJ-DISTRICT-COUNT")
SOURCES["SRC-RAJ-INDIATV"] = dict(
    title="Rajasthan government dissolves nine districts formed under Congress "
          "regime - full list",
    repo="", publisher="India TV News",
    url="https://www.indiatvnews.com/rajasthan/rajasthan-government-dissolves-nine-districts-in-cabinet-meeting-cm-bhajan-all-sharma-decision-check-full-list-ashok-gehlot-bjp-congress-latest-update-2024-12-28-968363",
    version="2024-12-28",
    retrieved="2026-10-14",
    jurisdiction="Rajasthan",
    data_type="News report of the cabinet decision",
    supports="Full list of the 9 dissolved districts and the 8 retained",
    limitations="News reporting.",
    inspected=True, corroborates="SRC-RAJ-DISTRICT-COUNT")
SOURCES["SRC-RAJ-BORDER-LENGTHS"] = dict(
    title="International and Interstate Boundaries of Rajasthan "
          "(5,920 / 1,070 / 1,262 / 877 / 1,600 / 1,022 / 89 km)",
    repo="", publisher="RAS study material / coaching aggregators "
                       "(rasonly.com, testbook.com, iasaarthi.com)",
    url="https://rasonly.com/ras/exams/rajasthan-international-and-interstate-boundaries",
    version="retrieved 2026-10-14",
    retrieved="2026-10-14",
    jurisdiction="Rajastan borders",
    data_type="Published exam figures",
    supports="The border LENGTHS most commonly quoted in Rajasthan competitive "
             "examinations, used as the cross-check baseline",
    limitations="**These lengths could NOT be reproduced from two independent "
                "GIS datasets** (see QA_REPORT.md). The district COUNTS in the "
                "same sources do match. Reported side-by-side, not overwritten.",
    inspected=True, corroborates="")
SOURCES["SRC-DATAMEET-2011"] = dict(
    title="INDIAN-SHAPEFILES — RAJASTHAN_DISTRICTS.geojson (Census 2011)",
    repo="https://github.com/datta07/INDIAN-SHAPEFILES",
    publisher="datta07 (Census 2011 / DataMeet derived)",
    url="https://github.com/datta07/INDIAN-SHAPEFILES",
    version="Census 2011",
    retrieved="2026-10-14",
    jurisdiction="India",
    data_type="GeoJSON polygons (Census 2011)",
    supports="Independent cross-check of Rajasthan's area (341,826 km²) and "
             "total outline length (5,487 km)",
    limitations="**REJECTED as primary geometry** — only 33 Rajasthan districts, "
                "obsolete since 2023 and again since Dec 2024.",
    inspected=True, corroborates="SRC-IND-SOI-DIST")
SOURCES["SRC-UDIT-INDIAMAPS"] = dict(
    title="india-maps-data — state-wise district GeoJSON",
    repo="https://github.com/udit-001/india-maps-data",
    publisher="udit-001",
    url="https://github.com/udit-001/india-maps-data",
    version="repo pushed 2026-07-14",
    retrieved="2026-10-14",
    jurisdiction="India",
    data_type="GeoJSON polygons",
    supports="Corroboration of the neighbouring-state district COUNTS "
             "(Gujarat 34 in this layer vs 33 in the SOI layer)",
    limitations="**REJECTED as primary geometry** — Rajasthan 33, MP 52, "
                "Punjab 22 (Census-2011 vintage).",
    inspected=True, corroborates="SRC-IND-SOI-DIST")
SOURCES["SRC-INDIA-GEODATA"] = dict(
    title="india-geodata — LGD / SOI / Bhuvan district boundaries",
    repo="https://github.com/yashveeeeeeer/india-geodata",
    publisher="yashveeeeeeer (LGD, Survey of India, ISRO Bhuvan derivatives)",
    url="https://github.com/yashveeeeeeer/india-geodata",
    version="release tag admin/districts, 2026-03-08",
    retrieved="2026-10-14",
    jurisdiction="India",
    data_type="Parquet / PMTiles / 7z (release assets)",
    supports="Would have been the first-choice official source (LGD and "
             "Survey of India district polygons)",
    limitations="**COULD NOT BE DOWNLOADED.** GitHub release assets are served "
                "from release-assets.githubusercontent.com, which is blocked in "
                "this execution environment. Verified by direct connection test. "
                "No claim in this project rests on this source.",
    inspected=False, corroborates="")
SOURCES["SRC-GEOBOUNDARIES"] = dict(
    title="geoBoundaries PAK ADM2 (gbOpen)",
    repo="https://github.com/wmgeolab/geoBoundaries",
    publisher="geoBoundaries / William & Mary geoLab",
    url="https://github.com/wmgeolab/geoBoundaries",
    version="repo pushed 2026-04-15",
    retrieved="2026-10-14",
    jurisdiction="Pakistan",
    data_type="Git-LFS pointers (payload unavailable)",
    supports="Would have been a corroborating source for Pakistani districts",
    limitations="**COULD NOT BE DOWNLOADED.** All data files are Git-LFS "
                "pointers (~130 B each); LFS payloads are served from "
                "media.githubusercontent.com, which is blocked. Verified.",
    inspected=False, corroborates="")
SOURCES["SRC-USER-UPLOADS"] = dict(
    title="User-supplied reference maps and KML file",
    repo="", publisher="User upload (this task)",
    url="",
    version="", retrieved="2026-10-14",
    jurisdiction="Rajasthan and neighbours",
    data_type="Unknown — never delivered",
    supports="Nothing. The files were named in the brief but did not reach the "
             "workspace.",
    limitations="**NOT INSPECTED — never received.** Workspace search found zero "
                ".kml/.kmz/.shp/.gpkg/.geojson/.tif/.jpg/.png files other than "
                "pre-existing Computer Network study PDFs. See INPUT_AUDIT.md.",
    inspected=False, corroborates="")

INDIAN_STATES = [
    ("08", "RAJASTHAN"),
    ("24", "GUJARAT"),
    ("23", "MADHYA PRADESH"),
    ("09", "UTTAR PRADESH"),
    ("06", "HARYANA"),
    ("03", "PUNJAB"),
]

# Conflation tolerance (metres) used for cross-source adjacency detection.
# Derived from the measured seam: 93.6 % of the Rajasthan boundary facing
# Pakistan lies within 1 000 m of the Pakistan polygons, median offset 50 m.
ADJACENCY_TOLERANCE_M = 1000.0
# A pair is treated as a genuine shared boundary only when BOTH directions
# return at least this much contact, which excludes corner/point touches.
MIN_LINE_CONTACT_M = 1500.0


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def geodesic_length(geom) -> float:
    """Length in metres of a LineString / MultiLineString / GeometryCollection
    of lineal parts, measured on the WGS 84 ellipsoid."""
    total = 0.0
    if geom is None or geom.is_empty:
        return 0.0
    gt = geom.geom_type
    if gt == "LineString":
        xs, ys = geom.xy
        for i in range(len(xs) - 1):
            _, _, d = GEOD.inv(xs[i], ys[i], xs[i + 1], ys[i + 1])
            total += abs(d)
        return total
    if gt == "MultiLineString":
        for part in geom.geoms:
            total += geodesic_length(part)
        return total
    if gt == "GeometryCollection":
        for part in geom.geoms:
            total += geodesic_length(part)
        return total
    return 0.0


def geodesic_area_km2(geom) -> float:
    if geom is None or geom.is_empty:
        return 0.0
    area, _ = GEOD.geometry_area_perimeter(geom)
    return abs(area) / 1e6


def read_soi_districts(state_code: str, state_name: str) -> gpd.GeoDataFrame:
    """Source files use underscore-separated state names, e.g. 23_MADHYA_PRADESH."""
    stem = f"{state_code}_{state_name.replace(' ', '_')}"
    path = RAW / "india_soi" / f"{stem}.geojson"
    gdf = gpd.read_file(path)
    return gdf


def write_sources_csv(out_csv: Path):
    rows = []
    for sid, s in SOURCES.items():
        rows.append(dict(source_id=sid, **s))
    df = pd.DataFrame(rows)
    df.to_csv(out_csv, index=False, encoding="utf-8-sig")
    return df
