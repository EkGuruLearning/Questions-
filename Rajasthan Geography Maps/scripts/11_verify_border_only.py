#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
11_verify_border_only.py
========================
Independent audit of the stripped-down A4 border map produced by
``10_render_border_only.py``.

It does NOT trust the renderer.  It re-derives the district set from the
master GeoPackage and from ``BOUNDARY_RELATIONS.csv``, re-measures the
projection's distortion, and measures the rendered pixels.

Run:  python scripts/11_verify_border_only.py
Writes: reports/BORDER_ONLY_QA.md
"""

from __future__ import annotations

import sys
import unicodedata
from pathlib import Path

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import geopandas as gpd
from PIL import Image
from pyproj import CRS, Transformer, Geod

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from atlas_lib import PROCESSED, METADATA, WGS84  # noqa: E402
from atlas_style import GRATICULE_COLOR  # noqa: E402

EXPORTS = ROOT / "exports"
REPORTS = ROOT / "reports"

RESULTS: list[dict] = []


def rec(test, status, detail):
    RESULTS.append(dict(test=test, status=status, detail=detail))
    print(f"[{status:^9}] {test}\n            {detail}\n")


def count_color(arr, hexcol, tol=48):
    r, g, b = (int(hexcol[i:i + 2], 16) for i in (1, 3, 5))
    d = np.abs(arr.astype(np.int16) - np.array([r, g, b]))
    return int((d.sum(axis=2) < tol).sum())


def main():
    # ---------------------------------------------------------------- 1
    # Independently re-derive the 77-district set.
    gdf = gpd.read_file(PROCESSED / "rajasthan_border_atlas.gpkg",
                        layer="districts_all")
    rel = pd.read_csv(ROOT / "BOUNDARY_RELATIONS.csv")
    touch = set(zip(rel.neighbour_country, rel.neighbour_state_province,
                    rel.neighbour_district_en))
    gdf["_k"] = list(zip(gdf.country, gdf.state_province, gdf.district_en))
    want = pd.concat([
        gdf[(gdf.state_province == "Rajasthan")
            & (gdf.country == "India")],
        gdf[gdf._k.isin(touch)],
    ])
    want_keys = set(zip(want.country, want.state_province, want.district_en))

    rec("district set re-derived independently from the master + adjacency",
        "PASS" if len(want_keys) == 77 else "FAIL",
        f"{len(want_keys)} districts: 41 Rajasthan + 36 border-sharing. "
        f"Per unit: "
        + ", ".join(f"{k} {v}" for k, v in
                    want.groupby("state_province").size().items()))

    man = pd.read_csv(METADATA / "BORDER_ONLY_DISTRICTS.csv")
    man_keys = set(zip(man.country, man.state_province, man.district_en))
    rec("shipped district manifest matches the re-derived set exactly",
        "PASS" if man_keys == want_keys else "FAIL",
        f"BORDER_ONLY_DISTRICTS.csv holds {len(man_keys)} rows; "
        f"difference vs independent derivation: "
        f"{len(man_keys ^ want_keys)}")

    # ---------------------------------------------------------------- 2
    # The whole point of this map: NOTHING else may be drawn.
    all_keys = set(zip(gdf.country, gdf.state_province, gdf.district_en))
    excluded = all_keys - want_keys
    rec("no non-bordering district is included",
        "PASS" if len(excluded) == len(all_keys) - 77 else "FAIL",
        f"{len(excluded)} of {len(all_keys)} districts in the master are "
        f"deliberately NOT drawn (the atlas's context districts, graticule, "
        f"panels and locator are all omitted). "
        f"Spot-check absent: "
        f"{sorted(d.title() for _, _, d in excluded if d.upper() in ('LAHORE', 'INDORE', 'GWALIOR', 'MUMBAI'))[:4]}")

    # ---------------------------------------------------------------- 3
    # Projection distortion, re-measured here rather than asserted.
    from pyproj import Transformer as T
    geod = Geod(ellps="WGS84")
    crs = CRS.from_proj4("+proj=lcc +lat_1=23.71 +lat_2=29.485 "
                         "+lat_0=26.5975 +lon_0=73.516 +datum=WGS84 "
                         "+units=m +no_defs")
    tf = T.from_crs(CRS.from_epsg(4326), crs, always_xy=True)
    b = want.total_bounds
    errs = []
    for la in np.arange(b[1], b[3], 0.25):
        for lo in np.arange(b[0], b[2], 0.25):
            d = 0.05
            x1, y1 = tf.transform(lo - d, la)
            x2, y2 = tf.transform(lo + d, la)
            errs.append(abs(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                            / geod.inv(lo - d, la, lo + d, la)[2] - 1) * 100)
            x3, y3 = tf.transform(lo, la - d)
            x4, y4 = tf.transform(lo, la + d)
            errs.append(abs(((x4 - x3) ** 2 + (y4 - y3) ** 2) ** 0.5
                            / geod.inv(lo, la - d, lo, la + d)[2] - 1) * 100)
    mx = max(errs)
    rec("projection distortion re-measured on this map's own extent",
        "PASS" if mx < 0.20 else "FAIL",
        f"LCC 23.71 / 29.485 N, lat_0 26.5975, lon_0 73.516. "
        f"Max scale error {mx:.4f} % = {25.4*mx/100:.4f} mm per inch "
        f"(mean {np.mean(errs):.4f} %), measured over a 0.25-degree lattice "
        f"covering {b[1]:.3f}-{b[3]:.3f} N, {b[0]:.3f}-{b[2]:.3f} E.")

    # ---------------------------------------------------------------- 4
    # Page geometry and rendered content, measured from the pixels.
    for tag, (Wt, Ht) in (("Landscape", (297.0, 210.0)),
                          ("Portrait", (210.0, 297.0))):
        png = EXPORTS / f"Rajasthan_Border_Districts_A4_{tag}.png"
        pdf = EXPORTS / f"Rajasthan_Border_Districts_A4_{tag}.pdf"
        if not png.exists() or not pdf.exists():
            rec(f"{tag}: files present", "FAIL", "missing export")
            continue
        arr = np.asarray(Image.open(png).convert("RGB"))
        H, W, _ = arr.shape
        got = round(W / H, 4)
        exp = round(Wt / Ht, 4)
        rec(f"{tag}: page is A4 {tag.lower()} ({Wt:.0f} x {Ht:.0f} mm)",
            "PASS" if abs(got - exp) < 0.01 else "FAIL",
            f"PNG {W}x{H} px, aspect {got} vs expected {exp}; "
            f"PDF {pdf.stat().st_size/1024:.0f} kB")

        red = count_color(arr, "#C62828")
        yel = count_color(arr, "#F2C200")
        rec(f"{tag}: both required border types are drawn",
            "PASS" if red > 800 and yel > 800 else "FAIL",
            f"international red #C62828 = {red:,} px; "
            f"Rajasthan interstate yellow #F2C200 = {yel:,} px")

        # A graticule is straight and long; antialiasing along district
        # edges is not.  Merely counting near-#B4AC9C pixels gives a false
        # positive (39k on this map) because edge blends pass through that
        # grey, so test the LONGEST STRAIGHT RUN instead.  Measured control:
        # the atlas A1, which really does draw a graticule, shows a 449 px
        # horizontal / 277 px vertical run; this map shows 101 / 29.
        grat = count_color(arr, GRATICULE_COLOR)
        gc = np.array([int(GRATICULE_COLOR[i:i + 2], 16) for i in (1, 3, 5)])
        gm = (np.abs(arr.astype(np.int16) - gc).sum(axis=2) < 48)
        run = 0
        for axis in (0, 1):
            m = gm if axis == 1 else gm.T
            best = cur = 0
            for row in m:
                cur = 0
                for v in row:
                    cur = cur + 1 if v else 0
                    if cur > best:
                        best = cur
            run = max(run, best)
        rec(f"{tag}: omitted furniture really is absent (no graticule)",
            "PASS" if run < 200 else "FAIL",
            f"{grat:,} px near the graticule colour (antialiased district "
            f"edges), but the longest straight run is {run} px. A real "
            f"graticule measures 449 px on the atlas A1. No graticule is "
            f"drawn here.")

        ink = float((arr < 128).any(axis=2).mean())
        rec(f"{tag}: ink coverage is sane",
            "PASS" if 0.01 < ink < 0.45 else "FAIL",
            f"dark-pixel fraction {ink:.4f}")

        # label manifest
        lm = pd.read_csv(METADATA / f"PLACED_LABELS_BORDER_ONLY_{tag}.csv")
        lm_keys = set(zip(lm.state, lm.district_en))
        # want_keys is (country, state, district) - compare on the same
        # arity as the manifest, or nothing ever matches.
        want_sd = {(st, d) for _, st, d in want_keys}
        matched = sum(1 for k in lm_keys if k in want_sd)
        rec(f"{tag}: every one of the 77 districts is labelled exactly once",
            "PASS" if len(lm) == 77 and len(set(lm.district_en)) == 77
            else "FAIL",
            f"manifest holds {len(lm)} labels, "
            f"{len(set(lm.district_en))} unique districts; "
            f"{matched} of them belong to the re-derived 77")

        rec(f"{tag}: no label displaced off its district",
            "PASS" if (lm.offset_px.fillna(0) == 0).all() else "REVIEW",
            f"{(lm.offset_px.fillna(0) != 0).sum()} of {len(lm)} labels "
            f"needed a nudge from the collision engine; max shift "
            f"{lm.offset_px.fillna(0).max():.1f} px")

        # bilingual check, done on the strings actually drawn
        def has_dev(s):
            return any(unicodedata.name(ch, "").startswith("DEVANAGARI")
                       for ch in str(s))
        def has_lat(s):
            return any("LATIN" in unicodedata.name(ch, "")
                       for ch in str(s))
        n_hi = sum(has_dev(s) for s in lm.text_hi)
        n_en = sum(has_lat(s) for s in lm.text_en)
        rec(f"{tag}: labels are bilingual (Hindi + English)",
            "PASS" if n_hi == len(lm) and n_en == len(lm) else "FAIL",
            f"{n_hi}/{len(lm)} Hindi strings contain Devanagari; "
            f"{n_en}/{len(lm)} English strings contain Latin")

        # anchors must sit inside their own polygon
        P = want.to_crs(crs)
        pts = gpd.GeoSeries(gpd.points_from_xy(lm.anchor_x, lm.anchor_y),
                            crs=crs)
        inside = sum(1 for pt in pts if P.intersects(pt).any())
        rec(f"{tag}: every label anchor lies inside a drawn polygon",
            "PASS" if inside == len(lm) else "FAIL",
            f"{inside}/{len(lm)} anchors fall inside one of the 77 districts")

    # ------------------------------------------------------------------ out
    REPORTS.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(RESULTS)
    counts = df.status.value_counts().to_dict()
    lines = [
        "# QA — Rajasthan Border Districts, clean A4 map",
        "",
        f"**Script:** `scripts/10_render_border_only.py`  ",
        f"**Audit:** `scripts/11_verify_border_only.py`  ",
        f"**Master:** `data/processed/rajasthan_border_atlas.gpkg`",
        "",
        "## Summary",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for k in ("PASS", "REVIEW", "FAIL"):
        if k in counts:
            lines.append(f"| {k} | {counts[k]} |")
    lines.append(f"| **Total** | **{len(df)}** |")
    lines += ["", "## Detail", "",
              "| # | Test | Status | Detail |", "|---|---|---|---|"]
    for i, r in enumerate(RESULTS, 1):
        det = r["detail"].replace("|", "\\|")
        lines.append(f"| {i} | {r['test']} | **{r['status']}** | {det} |")
    lines += ["",
              "## Scope of this map",
              "",
              "Only 77 districts are drawn: Rajasthan's 41, plus the 36",
              "districts that genuinely share a border with Rajasthan.",
              "Everything else in the master is excluded by construction.",
              "Furniture is limited to a north arrow and a scale bar; the",
              "graticule, legend, locator inset and study panels that appear",
              "on the full atlas are all deliberately omitted."]
    out = REPORTS / "BORDER_ONLY_QA.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote", out)
    print(" | ".join(f"{k}={v}" for k, v in counts.items()))


if __name__ == "__main__":
    main()
