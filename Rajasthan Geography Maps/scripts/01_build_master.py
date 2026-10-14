#!/usr/bin/env python3
"""
01_build_master.py
==================
Loads the raw, unmodified source layers, normalises the attribute schema,
runs the geometry-validation battery, and writes the master GeoPackage.

Nothing in this script moves, simplifies or re-positions a boundary.
Original downloaded files are never written to.
"""
from __future__ import annotations

import sys
import json
from datetime import date
from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely.geometry import MultiPolygon, Polygon
from shapely.validation import explain_validity

sys.path.insert(0, str(Path(__file__).resolve().parent))
from atlas_lib import (  # noqa: E402
    RAW, PROCESSED, METADATA, WGS84, MAP_PROJ, SOURCES, INDIAN_STATES,
    read_soi_districts, write_sources_csv, sha256, geodesic_area_km2,
)

BUILD_DATE = date.today().isoformat()


def keep_polygonal(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Drop any non-polygonal parts produced by a dissolve/buffer accident."""
    out = gdf.copy()
    out["geometry"] = out.geometry.apply(
        lambda g: MultiPolygon([g]) if isinstance(g, Polygon) else g
    )
    return out


def validate(gdf: gpd.GeoDataFrame, label: str) -> pd.DataFrame:
    """Geometry-validation battery.  Returns one row per finding."""
    findings = []

    def add(feat_id, name, test, status, detail):
        findings.append(
            dict(layer=label, feature_id=feat_id, name=name, test=test,
                 status=status, detail=detail)
        )

    for idx, row in gdf.iterrows():
        g = row.geometry
        fid = row.get("feat_id", idx)
        nm = row.get("district_en", idx)
        if g is None or g.is_empty:
            add(fid, nm, "empty_geometry", "FAIL", "geometry is null/empty")
            continue
        if not g.is_valid:
            add(fid, nm, "invalid_polygon", "FAIL", explain_validity(g))
        else:
            add(fid, nm, "invalid_polygon", "PASS", "")
        if isinstance(g, MultiPolygon):
            n = len(g.geoms)
            add(fid, nm, "multipart_geometry",
                "PASS" if n == 1 else "REVIEW",
                f"{n} parts - multipart district, inspect before labelling")
        elif isinstance(g, Polygon):
            add(fid, nm, "multipart_geometry", "PASS", "single part")
        else:
            add(fid, nm, "multipart_geometry", "FAIL", g.geom_type)

    # duplicates
    dup = gdf.duplicated(subset=["country", "state_province", "district_en"], keep=False)
    for idx in gdf.index[dup]:
        add(gdf.at[idx, "feat_id"], gdf.at[idx, "district_en"],
            "duplicate_feature", "FAIL", "duplicate country/state/district key")
    # missing names
    for idx, row in gdf.iterrows():
        if not str(row.get("district_en", "")).strip():
            add(row.get("feat_id", idx), "", "missing_name", "FAIL", "blank district name")

    return pd.DataFrame(findings)


def main():
    PROCESSED.mkdir(parents=True, exist_ok=True)
    METADATA.mkdir(parents=True, exist_ok=True)

    # ---------------- raw file inventory ----------------
    inv = []
    for p in sorted(RAW.rglob("*")):
        if p.is_file():
            inv.append(dict(
                path=str(p.relative_to(RAW)),
                bytes=p.stat().st_size,
                sha256=sha256(p),
            ))
    pd.DataFrame(inv).to_csv(METADATA / "RAW_FILE_INVENTORY.csv", index=False)

    # ---------------- India districts ----------------
    india_frames = []
    for code, name in INDIAN_STATES:
        gdf = read_soi_districts(code, name)
        gdf = gdf.to_crs(WGS84)
        out = gpd.GeoDataFrame({
            "feat_id": [f"IN-{code}-{d}" for d in gdf["district_lgd"].astype(str)],
            "country": "India",
            "state_province": name.title(),
            "district_en": gdf["district_name"].astype(str).str.strip(),
            "district_lgd_code": gdf["district_lgd"].astype(str),
            "admin_level": "ADM2 (district)",
            "source_id": "SRC-IND-SOI-DIST",
            "source_version": SOURCES["SRC-IND-SOI-DIST"]["version"],
        }, geometry=gdf.geometry.values, crs=WGS84)
        india_frames.append(out)
        print(f"  loaded {name}: {len(out)} districts")

    india = pd.concat(india_frames, ignore_index=True)
    india = gpd.GeoDataFrame(india, geometry="geometry", crs=WGS84)

    # ---------------- disputed slivers ----------------
    disp = gpd.read_file(RAW / "india_soi" / "_disputed.geojson").to_crs(WGS84)
    disp = disp[disp["remarks"].astype(str).str.contains("RAJ", case=False, na=False)]
    if len(disp):
        disp_out = gpd.GeoDataFrame({
            "feat_id": [f"IN-DISPUTED-{i}" for i in range(len(disp))],
            "country": "India",
            "state_province": "DISPUTED",
            "district_en": [f"DISPUTED AREA (RAJASTHAN-GUJARAT) #{i+1}"
                            for i in range(len(disp))],
            "district_lgd_code": "",
            "admin_level": "disputed",
            "source_id": "SRC-IND-SOI-DIST",
            "source_version": SOURCES["SRC-IND-SOI-DIST"]["version"],
        }, geometry=disp.geometry.values, crs=WGS84)
        india = pd.concat([india, disp_out], ignore_index=True)
        print(f"  loaded disputed slivers: {len(disp_out)}")

    # ---------------- Pakistan districts ----------------
    pk = gpd.read_file(RAW / "pakistan_opencarto" / "pk-country-district.geojson")
    pk = pk.to_crs(WGS84)
    pk_out = gpd.GeoDataFrame({
        "feat_id": pk["id"].astype(str),
        "country": "Pakistan",
        # Disambiguate: the Indian state "Punjab" and the Pakistani province
        # "Punjab" would otherwise share one key and be merged by every
        # groupby() downstream.
        "state_province": pk["province"].astype(str) + " (Pakistan)",
        "district_en": pk["name"].astype(str).str.strip(),
        "district_lgd_code": pk["sourceCode"].astype(str),
        "admin_level": "ADM2 (district)",
        "source_id": "SRC-PAK-CODAB-ADM2",
        "source_version": pk["sourceValidOn"].astype(str).iloc[0],
    }, geometry=pk.geometry.values, crs=WGS84)
    print(f"  loaded Pakistan districts: {len(pk_out)}")

    # ---------------- combine ----------------
    all_dist = pd.concat([india, pk_out], ignore_index=True)
    all_dist = gpd.GeoDataFrame(all_dist, geometry="geometry", crs=WGS84)
    all_dist["area_km2"] = all_dist.geometry.apply(geodesic_area_km2)
    all_dist["n_parts"] = all_dist.geometry.apply(
        lambda g: len(g.geoms) if isinstance(g, MultiPolygon) else 1)
    all_dist["geom_valid"] = all_dist.geometry.is_valid

    # ---------------- validation ----------------
    find = pd.concat([
        validate(all_dist, "districts_all"),
    ], ignore_index=True)
    find.to_csv(METADATA / "GEOMETRY_VALIDATION.csv", index=False)
    summ = (find.groupby(["layer", "test", "status"]).size()
            .reset_index(name="n"))
    print("\nValidation summary:")
    print(summ.to_string(index=False))

    # ---------------- write master ----------------
    gpkg = PROCESSED / "rajasthan_border_atlas.gpkg"
    if gpkg.exists():
        gpkg.unlink()

    all_dist.to_file(gpkg, layer="districts_all", driver="GPKG")
    rj = all_dist[(all_dist.state_province == "Rajasthan")].copy()
    rj.to_file(gpkg, layer="rajasthan_districts", driver="GPKG")
    all_dist[all_dist.country == "Pakistan"].to_file(
        gpkg, layer="pakistan_districts", driver="GPKG")

    # state / province outlines (dissolved, never re-drawn)
    india_only = all_dist[all_dist.country == "India"]
    states = india_only.dissolve(by="state_province", as_index=False)[
        ["state_province", "geometry"]]
    states.to_file(gpkg, layer="indian_state_outlines", driver="GPKG")
    provs = pk_out.dissolve(by="state_province", as_index=False)[
        ["state_province", "geometry"]]
    provs.to_file(gpkg, layer="pakistan_province_outlines", driver="GPKG")

    # locator layer: whole of India from the SOI state layer
    india_states = gpd.read_file(RAW / "india_soi" / "states.geojson").to_crs(WGS84)
    india_states = india_states[~india_states["state_name"].astype(str)
                                .str.startswith("DISPUTED")]
    india_states.to_file(gpkg, layer="india_locator_states", driver="GPKG")

    # ---------------- district inventory ----------------
    inv2 = all_dist.drop(columns="geometry").copy()
    inv2["in_primary_frame"] = False
    inv2.to_csv(METADATA / "DISTRICT_INVENTORY.csv", index=False, encoding="utf-8-sig")

    # ---------------- sources ----------------
    write_sources_csv(ROOT := Path(__file__).resolve().parent.parent / "SOURCES_REGISTER.csv")

    meta = dict(
        build_date=BUILD_DATE,
        master_gpkg=str(gpkg.relative_to(Path(__file__).resolve().parent.parent)),
        crs=WGS84,
        # Derived from atlas_lib.MAP_PROJ so the recorded projection can
        # never drift away from the one the renderer actually uses.
        map_projection=MAP_PROJ.to_proj4(),
        districts_total=int(len(all_dist)),
        rajasthan_districts=int((all_dist.state_province == "Rajasthan").sum()),
        pakistan_districts=int((all_dist.country == "Pakistan").sum()),
    )
    (Path(__file__).resolve().parent.parent / "data" / "metadata"
     ).mkdir(parents=True, exist_ok=True)
    with open(METADATA / "BUILD_METADATA.json", "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=2, ensure_ascii=False)
    print("\nMaster written:", gpkg)
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
