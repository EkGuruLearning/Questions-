#!/usr/bin/env python3
"""
00_audit_uploads.py
===================
Run this AFTER dropping new reference files into `data/raw/reference_uploads/`.

It records, for every file it finds, whatever can be determined without
assuming the file is trustworthy:

  * name, format, byte size, SHA-256
  * whether it is a real GIS dataset, a georeferenced raster, a plain image,
    a document, or something else
  * CRS and layer list, if it is a vector dataset
  * feature count and the district-name list, if such a field exists
  * KML/KMZ structure, if applicable

It then diffs any district names it finds against
`data/metadata/DISTRICT_INVENTORY.csv` and writes the divergence to
`data/metadata/UPLOAD_AUDIT_DIVERGENCE.csv`.

A divergence is a DATA CONFLICT TO RESOLVE, not a spelling to copy.  This
script never imports an upload into the master project; that decision stays
manual and is recorded in the change log.

Usage:
    .venv/bin/python scripts/00_audit_uploads.py
"""
from __future__ import annotations

import sys
import hashlib
import zipfile
from pathlib import Path
from datetime import date

import pandas as pd
import geopandas as gpd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from atlas_lib import RAW, METADATA, ROOT  # noqa: E402

UP = RAW / "reference_uploads"
TODAY = date.today().isoformat()

VECTOR_EXT = {".geojson", ".json", ".shp", ".gpkg", ".kml", ".kmz", ".gml",
              ".gdb"}
RASTER_EXT = {".tif", ".tiff", ".geotiff", ".jp2", ".img", ".sid", ".ecw"}
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif", ".svg"}
DOC_EXT = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".txt", ".md", ".csv"}

NAME_FIELDS = ["district", "dtname", "district_name", "DISTRICT", "NAME",
               "name", "DIST_NAME", "dist_name", "dt_name", "Name"]


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def classify(p: Path) -> str:
    suf = p.suffix.lower()
    if suf in VECTOR_EXT:
        return "vector (possible GIS dataset)"
    if suf in RASTER_EXT:
        return "raster (check georeferencing)"
    if suf in IMAGE_EXT:
        return "image (NOT a coordinate source)"
    if suf in DOC_EXT:
        return "document"
    return "unknown"


def main():
    UP.mkdir(parents=True, exist_ok=True)
    (UP / ".gitkeep").touch(exist_ok=True)
    files = sorted(p for p in UP.iterdir() if p.is_file()
                   and p.name != ".gitkeep")
    if not files:
        print(f"No files in {UP}.")
        print("Nothing to audit. As of the original build, the user's")
        print("reference maps and KML never reached the workspace - see")
        print("INPUT_AUDIT.md.")
        return

    rows, all_names = [], {}
    for p in files:
        row = dict(file=p.name, bytes=p.stat().st_size, sha256=sha256(p),
                   format=classify(p), crs="", layers="", features="",
                   notes="")
        try:
            if p.suffix.lower() in {".geojson", ".json", ".shp", ".gpkg",
                                    ".gml"}:
                import fiona
                try:
                    layers = fiona.listlayers(str(p))
                except Exception:
                    layers = [None]
                row["layers"] = ", ".join(str(x) for x in layers)
                g = gpd.read_file(p)
                row["crs"] = str(g.crs)
                row["features"] = len(g)
                for fld in NAME_FIELDS:
                    if fld in g.columns:
                        all_names[p.name] = sorted(
                            set(g[fld].astype(str).str.strip()))
                        row["notes"] = f"name field '{fld}'"
                        break
            elif p.suffix.lower() == ".kml":
                txt = p.read_text(errors="ignore")
                row["features"] = txt.count("<Placemark")
                row["notes"] = ("KML: CRS assumed EPSG:4326 per spec - "
                                "VERIFY, do not assume")
            elif p.suffix.lower() == ".kmz":
                with zipfile.ZipFile(p) as z:
                    names = z.namelist()
                row["notes"] = f"KMZ contents: {', '.join(names[:8])}"
            elif p.suffix.lower() in RASTER_EXT:
                row["notes"] = ("raster - inspect for a .tfw/.aux.xml sidecar "
                                "and check CRS before any georeferencing claim")
            elif p.suffix.lower() in IMAGE_EXT:
                row["notes"] = ("image - may guide colour/labelling ONLY; "
                                "never a source of coordinates")
        except Exception as e:
            row["notes"] = f"could not parse: {type(e).__name__}: {e}"
        rows.append(row)

    df = pd.DataFrame(rows)
    out = METADATA / "UPLOAD_AUDIT.csv"
    df.to_csv(out, index=False, encoding="utf-8-sig")
    print(df.to_string(index=False))
    print(f"\nwrote {out}")

    if all_names:
        inv = pd.read_csv(METADATA / "DISTRICT_INVENTORY.csv")
        known = set(inv.district_en.astype(str).str.upper())
        div = []
        for src, names in all_names.items():
            for n in names:
                if n.upper() not in known:
                    div.append(dict(upload=src, name_in_upload=n,
                                    in_master="NO"))
        d = pd.DataFrame(div)
        dout = METADATA / "UPLOAD_AUDIT_DIVERGENCE.csv"
        d.to_csv(dout, index=False, encoding="utf-8-sig")
        print(f"{len(d)} names in uploads are absent from the master -> "
              f"{dout}")
        if len(d):
            print("Resolve each by evidence (gazette / official portal) "
                  "before adopting it.")


if __name__ == "__main__":
    main()
