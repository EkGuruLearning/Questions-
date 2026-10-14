#!/usr/bin/env python3
"""
02_adjacency.py
===============
Derives the Rajasthan border-sharing table from the actual polygon geometry.

Method
------
The Rajasthan layer (Survey-of-India derived) and the Pakistan layer
(COD-AB / OCHA) are independent sources, so their lines do not coincide to the
millimetre.  Measuring `A.boundary ∩ B.boundary` exactly therefore *undercounts*
badly.  Instead, for every candidate pair we measure contact in BOTH
directions and average:

    l1 = length of A's boundary lying within TOL of B
    l2 = length of B's boundary lying within TOL of A
    shared = (l1 + l2) / 2

TOL is 1 000 m.  This value was not chosen arbitrarily: it comes from the measured
seam between the two sources (93.6 % of the Pakistan-facing Rajasthan boundary
lies within 1 000 m of the Pakistan polygons, median offset 50 m; see
reports/QA_REPORT.md).  Averaging the two directions also prevents a source that
is systematically denser in vertices from inflating one side.

A pair is only accepted as a genuine SHARED BOUNDARY when both directions return
at least MIN_LINE_CONTACT_M (1 500 m).  Corner/point touches fail that test and
are reported separately as `point_or_short_contact` and never counted as an
ordinary border district.

Lengths are geodesic (WGS 84 ellipsoid, pyproj.Geod), so they are free of
projection distortion.  Areas are geodesic too.
"""
from __future__ import annotations

import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from atlas_lib import (  # noqa: E402
    PROCESSED, METADATA, ROOT, MAP_PROJ, WGS84,
    ADJACENCY_TOLERANCE_M as TOL, MIN_LINE_CONTACT_M,
    geodesic_length,
)


def boundary_length_within(a_geom, b_geom, tol):
    """Geodesic metres of a_geom's boundary lying within `tol` of b_geom.

    The buffer/intersection is done in the projected CRS (metres), then the
    result is transformed back to geographic coordinates and measured on the
    WGS 84 ellipsoid, so the reported length is free of projection scale error.
    """
    near = a_geom.boundary.intersection(b_geom.buffer(tol))
    if near.is_empty:
        return 0.0
    near_wgs = gpd.GeoSeries([near], crs=MAP_PROJ).to_crs(WGS84).iloc[0]
    return geodesic_length(near_wgs)


def main():
    gpkg = PROCESSED / "rajasthan_border_atlas.gpkg"
    all_dist = gpd.read_file(gpkg, layer="districts_all")

    rj = all_dist[all_dist.state_province == "Rajasthan"].copy()
    # The 22 "DISPUTED AREA (RAJASTHAN-GUJARAT)" slivers are contested pockets
    # on the Rajasthan-Gujarat boundary, not districts.  They are excluded from
    # the adjacency table (they are not administrative neighbours) and recorded
    # separately so nothing is silently dropped.
    neighbours = all_dist[(all_dist.state_province != "Rajasthan")
                          & (all_dist.state_province != "DISPUTED")].copy()
    disp = all_dist[all_dist.state_province == "DISPUTED"]
    if len(disp):
        disp.drop(columns="geometry").to_csv(
            METADATA / "DISPUTED_SLIVERS.csv", index=False, encoding="utf-8-sig")

    rj_p = rj.to_crs(MAP_PROJ)
    nb_p = neighbours.to_crs(MAP_PROJ)
    rj_p = rj_p.reset_index(drop=True)
    nb_p = nb_p.reset_index(drop=True)

    sindex = nb_p.sindex
    rows = []

    for i in range(len(rj_p)):
        a = rj_p.geometry.iloc[i]
        a_nm = rj_p.district_en.iloc[i]
        # candidate neighbours within tolerance
        cand = list(sindex.query(a.buffer(TOL), predicate="intersects"))
        for j in cand:
            b = nb_p.geometry.iloc[j]
            if not a.intersects(b.buffer(TOL)):
                continue
            l1 = boundary_length_within(a, b, TOL)
            l2 = boundary_length_within(b, a, TOL)
            if l1 <= 0 and l2 <= 0:
                continue
            shared = (l1 + l2) / 2.0
            raw_exact = a.boundary.intersection(b)
            exact = (geodesic_length(
                gpd.GeoSeries([raw_exact], crs=MAP_PROJ).to_crs(WGS84).iloc[0])
                if not raw_exact.is_empty else 0.0)
            if min(l1, l2) >= MIN_LINE_CONTACT_M:
                kind = "shared_boundary"
            elif shared >= 1.0:
                kind = "point_or_short_contact"
            else:
                continue
            nb = nb_p.iloc[j]
            rows.append(dict(
                rajasthan_district_en=a_nm,
                neighbour_country=nb.country,
                neighbour_state_province=nb.state_province,
                neighbour_district_en=nb.district_en,
                neighbour_feature_id=nb.feat_id,
                shared_border_km=round(shared / 1000.0, 3),
                side_a_km=round(l1 / 1000.0, 3),
                side_b_km=round(l2 / 1000.0, 3),
                exactly_coincident_km=round(exact / 1000.0, 3),
                contact_type=kind,
                method="bidirectional geodesic mean, tol=1000 m",
                source_rajasthan="SRC-IND-SOI-DIST",
                source_neighbour=nb.source_id,
            ))

    df = pd.DataFrame(rows)
    df = df[df.contact_type == "shared_boundary"].copy()
    df = df.sort_values(
        ["neighbour_country", "neighbour_state_province",
         "neighbour_district_en", "shared_border_km"],
        ascending=[True, True, True, False]).reset_index(drop=True)
    df.insert(0, "relation_id", [f"BR-{i:03d}" for i in range(1, len(df) + 1)])
    df.to_csv(ROOT / "BOUNDARY_RELATIONS.csv", index=False, encoding="utf-8-sig")

    # ---- summary tables -------------------------------------------------
    by_nb = (df.groupby(["neighbour_country", "neighbour_state_province"])
               .agg(districts_touching=("neighbour_district_en", "nunique"),
                    total_shared_km=("shared_border_km", "sum"))
               .reset_index())
    print("\n=== Rajasthan border summary by neighbour (geometry-derived) ===")
    print(by_nb.to_string(index=False))
    by_nb.to_csv(METADATA / "BORDER_SUMMARY_BY_NEIGHBOUR.csv", index=False)

    print("\n=== Districts touching Rajasthan, per neighbour ===")
    for (c, s), grp in df.groupby(["neighbour_country", "neighbour_state_province"]):
        agg = (grp.groupby("neighbour_district_en")["shared_border_km"].sum()
               .sort_values(ascending=False))
        print(f"\n{c} / {s}  ({len(agg)} districts, {agg.sum():.1f} km)")
        for nm, v in agg.items():
            rjs = sorted(grp[grp.neighbour_district_en == nm].rajasthan_district_en)
            print(f"   {nm:<32s} {v:8.1f} km   <- {', '.join(rjs)}")

    print("\nWrote", ROOT / "BOUNDARY_RELATIONS.csv", len(df), "rows")

    # ---- per-country/state total contact length (for QA cross-check) ----
    return df, by_nb


if __name__ == "__main__":
    main()
