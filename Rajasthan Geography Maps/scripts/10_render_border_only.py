#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
10_render_border_only.py
========================
A deliberately stripped-down companion to the full atlas.

It draws **only**:

  * Rajasthan's 41 districts, and
  * the 36 districts of the neighbouring units that genuinely share a border
    with Rajasthan (Gujarat 6, Haryana 7, Madhya Pradesh 10, Punjab 2,
    Uttar Pradesh 2, Pakistan/Punjab 3, Pakistan/Sindh 6)

Everything else present in the atlas is gone: no non-bordering context
districts, no graticule, no study panels, no legend, no locator inset.
The only furniture besides the map is a north arrow and a scale bar.

Labels are bilingual: Hindi above, English below.

Output: A4 landscape and A4 portrait, PNG + PDF.

Run:  python scripts/10_render_border_only.py
Requires scripts/01_build_master.py and scripts/02_adjacency.py to have run.
"""

from __future__ import annotations

import sys
from pathlib import Path

import warnings
warnings.filterwarnings("ignore")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Polygon as MplPolygon
from matplotlib.text import Text
from shapely.geometry import LineString, MultiLineString
from shapely.ops import unary_union

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from atlas_lib import PROCESSED, METADATA, WGS84  # noqa: E402

EXPORTS = ROOT / "exports"

# ---------------------------------------------------------------------------
# Projection: optimised for THIS map's extent, not inherited from the atlas.
#
# The 77 drawn districts span 22.503-30.692 N.  The standard parallels below
# were found by scanning the symmetric pair about lat_0 and minimising the
# maximum scale error over a 0.25-degree lattice across the extent:
#     lat_1 = 23.71, lat_2 = 29.485, lat_0 = 26.5975, lon_0 = 73.516
#     max scale error 0.1264 %  =  0.0321 mm per inch
# (The atlas's own parallels give 0.2101 % on this extent; the old 25/30
# pair gives 0.2802 %.)
# ---------------------------------------------------------------------------
from pyproj import CRS  # noqa: E402

BORDER_MAP_PROJ = CRS.from_proj4(
    "+proj=lcc +lat_1=23.71 +lat_2=29.485 +lat_0=26.5975 "
    "+lon_0=73.516 +datum=WGS84 +units=m +no_defs"
)
MAX_SCALE_ERROR_PCT = 0.1264

# ---------------------------------------------------------------------------
# Palette.  One fill per state so the colour itself identifies the state.
# ---------------------------------------------------------------------------
FILL_RAJASTHAN = "#FDF0DC"
FILL = {
    "Punjab":            "#E4EFD3",
    "Haryana":           "#FDF1C7",
    "Uttar Pradesh":     "#FBDCDC",
    "Madhya Pradesh":    "#DCE8F7",
    "Gujarat":           "#E6DEF6",
    "Punjab (Pakistan)": "#E3E7E1",
    "Sindh (Pakistan)":  "#D9DFDB",
}
EDGE_DISTRICT = "#8E8778"   # crisp district outline (study legibility)
EDGE_STATE    = "#6E6A63"   # neighbour state outlines
INTL_RED      = "#C62828"   # India-Pakistan international boundary
INTER_YELLOW  = "#F2C200"   # Rajasthan interstate boundary
TEXT_HI       = "#241F1A"
TEXT_EN       = "#5A5348"

FS_HI_RAJ = 6.6     # Hindi, Rajasthan districts
FS_HI_NB  = 6.0     # Hindi, neighbour districts
FS_EN     = 4.6     # English, all

MEASURE_CACHE: dict = {}


def measure_text(fig, text, prop, fs, renderer, dpi):
    key = (text, round(fs, 3), id(prop))
    if key not in MEASURE_CACHE:
        t = Text(0, 0, text, fontproperties=prop, fontsize=fs, figure=fig)
        try:
            bb = t.get_window_extent(renderer=renderer)
            w, h = float(bb.width), float(bb.height)
        except Exception:
            w = h = 0.0
        if w <= 0 or h <= 0:
            w = len(text) * fs * dpi / 72.0 * 0.62
            h = fs * dpi / 72.0
        MEASURE_CACHE[key] = (w, h)
    return MEASURE_CACHE[key]


def _lines(geom):
    if geom is None or geom.is_empty:
        return []
    if isinstance(geom, (LineString, MultiLineString)):
        return [geom] if isinstance(geom, LineString) else list(geom.geoms)
    out = []
    for g in getattr(geom, "geoms", [geom]):
        if isinstance(g, LineString):
            out.append(g)
        elif isinstance(g, MultiLineString):
            out.extend(g.geoms)
    return out


def draw_line(ax, geom, color, lw, zorder=9, cap="round"):
    """Plot a (multi)linestring without letting matplotlib close polygons."""
    for ln in _lines(geom):
        if ln.is_empty or len(ln.coords) < 2:
            continue
        ax.plot(*ln.xy, color=color, linewidth=lw, zorder=zorder,
                solid_capstyle=cap, solid_joinstyle="round")


def place_bilingual(ax, fig, cands):
    """Greedy collision-avoiding placement of two-line (Hindi/English) blocks.

    Works in device pixels so the measurement is independent of the axes'
    data range.  Returns (placed_rows, dropped_rows).
    """
    trans = ax.transData.transform
    inv = ax.transData.inverted().transform
    renderer = fig.canvas.get_renderer()
    dpi = fig.dpi
    boxes = []
    placed, dropped = [], []

    def overlaps(cx, cy, w, h, pad):
        return any(not (cx + w / 2 + pad < b[0] - b[2] / 2
                        or cx - w / 2 - pad > b[0] + b[2] / 2
                        or cy + h / 2 + pad < b[1] - b[3] / 2
                        or cy - h / 2 - pad > b[1] + b[3] / 2)
                   for b in boxes)

    for c in sorted(cands, key=lambda d: (d["priority"], -d["fs_hi"])):
        px, py = trans((c["x"], c["y"]))
        w1, h1 = measure_text(fig, c["hi"], c["prop_hi"], c["fs_hi"],
                              renderer, dpi)
        w2, h2 = measure_text(fig, c["en"], c["prop_en"], c["fs_en"],
                              renderer, dpi)
        w, h = max(w1, w2), h1 + h2
        s = max(h1, h2)
        offs = [(0, 0)]
        for dy in (1, -1, 2, -2, 3, -3, 4, -4):
            offs.append((0, dy * s * 1.08))
        for dx in (0.62, -0.62, 1.15, -1.15):
            for dy in (0, 1, -1):
                offs.append((dx * w, dy * s * 1.08))

        chosen = None
        for ox, oy in offs:
            cx, cy = px + ox, py + oy
            if overlaps(cx, cy, w, h, pad=1.3):
                continue
            chosen = (cx, cy, ox, oy)
            break
        if chosen is None:
            dropped.append(c)
            continue

        cx, cy, ox, oy = chosen
        boxes.append((cx, cy, w, h))
        hx, hy = inv((cx, cy + h / 2 - h1 / 2))
        ex, ey = inv((cx, cy - h / 2 + h2 / 2))
        ax.text(hx, hy, c["hi"], fontproperties=c["prop_hi"],
                fontsize=c["fs_hi"], ha="center", va="center",
                color=c["color_hi"], zorder=c["zorder"])
        ax.text(ex, ey, c["en"], fontproperties=c["prop_en"],
                fontsize=c["fs_en"], ha="center", va="center",
                color=TEXT_EN, zorder=c["zorder"])
        if abs(ox) > 1 or abs(oy) > 1:
            ax.plot([c["x"], hx], [c["y"], hy], color="#9A938A",
                    lw=0.32, zorder=c["zorder"] - 1)
        placed.append(dict(text_hi=c["hi"], text_en=c["en"],
                           state=c["state"], district_en=c["district_en"],
                           anchor_x=c["x"], anchor_y=c["y"],
                           offset_px=round(float((ox * ox + oy * oy) ** 0.5), 1)))
    return placed, dropped


def nice_scale_km(metres_per_mm, target_mm):
    """Pick a round distance whose bar is close to target_mm long."""
    target_km = metres_per_mm * target_mm / 1000.0
    for v in (10, 20, 25, 50, 75, 100, 125, 150, 200, 250, 300, 400, 500):
        if v >= target_km * 0.75:
            return v
    return 500


def render(orientation="landscape", dpi=300):
    Wmm, Hmm = (297.0, 210.0) if orientation == "landscape" else (210.0, 297.0)
    fig = plt.figure(figsize=(Wmm / 25.4, Hmm / 25.4), dpi=dpi)
    fig.patch.set_facecolor("#FFFFFF")

    # ------------------------------------------------------------------ data
    gdf = gpd.read_file(PROCESSED / "rajasthan_border_atlas.gpkg",
                        layer="districts_all")
    names = pd.read_csv(METADATA / "district_names_hi.csv")
    gdf = gdf.merge(names[["state_province", "district_en", "district_hi"]],
                    on=["state_province", "district_en"], how="left")
    rel = pd.read_csv(ROOT / "BOUNDARY_RELATIONS.csv")
    touching = set(zip(rel.neighbour_country, rel.neighbour_state_province,
                       rel.neighbour_district_en))
    gdf["_key"] = list(zip(gdf.country, gdf.state_province, gdf.district_en))
    raj = gdf[gdf.state_province == "Rajasthan"].copy()
    nb = gdf[gdf._key.isin(touching)].copy()
    sel = pd.concat([raj, nb], ignore_index=True)
    assert len(raj) == 41 and len(nb) == 36, (len(raj), len(nb))

    src = gpd.GeoDataFrame(sel, geometry="geometry", crs=WGS84)
    P = src.to_crs(BORDER_MAP_PROJ)
    P = P.reset_index(drop=True)

    # ------------------------------------------------------- boundary lines
    rj_u = unary_union(raj.geometry.buffer(0))
    rjP = gpd.GeoSeries([rj_u], crs=WGS84).to_crs(BORDER_MAP_PROJ).iloc[0]
    pk_sel = nb[nb.country == "Pakistan"]
    pk_u = unary_union(pk_sel.geometry.buffer(0)) if len(pk_sel) else None

    intl = None
    if pk_u is not None:
        pkP = gpd.GeoSeries([pk_u], crs=WGS84).to_crs(BORDER_MAP_PROJ).iloc[0]
        intl = rjP.boundary.intersection(pkP.buffer(1000.0))

    inter_parts = []
    for st, grp in nb[nb.country == "India"].groupby("state_province"):
        S = unary_union(grp.geometry.buffer(0))
        SP = gpd.GeoSeries([S], crs=WGS84).to_crs(BORDER_MAP_PROJ).iloc[0]
        seg = rjP.boundary.intersection(SP.boundary)
        if not seg.is_empty:
            inter_parts.append(seg)
    inter = unary_union(inter_parts) if inter_parts else None

    # --------------------------------------------------------------- layout
    if orientation == "landscape":
        mbox = [0.022, 0.088, 0.956, 0.842]
        title_y, foot_y = 0.962, 0.032
    else:
        mbox = [0.028, 0.082, 0.944, 0.848]
        title_y, foot_y = 0.958, 0.028

    ax = fig.add_axes(mbox)
    ax.set_facecolor("#FFFFFF")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)

    # ------------------------------------------------------------- polygons
    rjP_df = P[P.state_province == "Rajasthan"]
    nbP_df = P[P.state_province != "Rajasthan"]

    for _, row in nbP_df.iterrows():
        fc = FILL.get(row.state_province, "#EDEAE3")
        for poly in (row.geometry.geoms if row.geometry.geom_type == "MultiPolygon"
                     else [row.geometry]):
            ax.add_patch(MplPolygon(np.asarray(poly.exterior.coords),
                                    facecolor=fc, edgecolor="none", zorder=1))
            ax.plot(*poly.exterior.xy, color=EDGE_DISTRICT, lw=0.32, zorder=3)

    for _, row in rjP_df.iterrows():
        for poly in (row.geometry.geoms if row.geometry.geom_type == "MultiPolygon"
                     else [row.geometry]):
            ax.add_patch(MplPolygon(np.asarray(poly.exterior.coords),
                                    facecolor=FILL_RAJASTHAN,
                                    edgecolor="none", zorder=2))
            ax.plot(*poly.exterior.xy, color=EDGE_DISTRICT, lw=0.34, zorder=4)

    # --------------------------------------------------------- border lines
    if inter is not None:
        draw_line(ax, inter, INTER_YELLOW, 1.9, zorder=7)
    if intl is not None and not intl.is_empty:
        draw_line(ax, intl, INTL_RED, 2.4, zorder=8)
    draw_line(ax, rjP.boundary, "#6E6A63", 0.85, zorder=6)

    xmin, ymin, xmax, ymax = P.total_bounds
    pad_x = (xmax - xmin) * 0.012
    pad_y = (ymax - ymin) * 0.012
    ax.set_xlim(xmin - pad_x, xmax + pad_x)
    ax.set_ylim(ymin - pad_y, ymax + pad_y)
    ax.set_aspect("equal", adjustable="box")

    # --------------------------------------------------------------- labels
    FP_HI_R = FontProperties(fname=str(ROOT / "fonts" /
                                       "NotoSansDevanagari-Bold.ttf"))
    FP_HI_N = FontProperties(fname=str(ROOT / "fonts" /
                                       "NotoSansDevanagari-Regular.ttf"))
    FP_EN = FontProperties(family="DejaVu Sans")

    cands = []
    for _, row in P.iterrows():
        is_raj = row.state_province == "Rajasthan"
        pt = row.geometry.representative_point()
        hi = (row.district_hi if isinstance(row.district_hi, str)
              and str(row.district_hi).strip() else row.district_en)
        cands.append(dict(
            x=pt.x, y=pt.y, hi=str(hi), en=str(row.district_en).title(),
            prop_hi=FP_HI_R if is_raj else FP_HI_N,
            prop_en=FP_EN,
            fs_hi=FS_HI_RAJ if is_raj else FS_HI_NB,
            fs_en=FS_EN,
            color_hi=TEXT_HI if is_raj else "#4A443B",
            priority=0 if is_raj else 1,
            zorder=12 if is_raj else 11,
            state=row.state_province, district_en=row.district_en))

    placed, dropped = place_bilingual(ax, fig, cands)

    # --------------------------------------------------- north arrow + scale
    nax = fig.add_axes([mbox[0] + mbox[2] - 0.072,
                        mbox[1] + mbox[3] - 0.098, 0.062, 0.086],
                       facecolor="none")
    nax.set_xlim(0, 1); nax.set_ylim(0, 1); nax.axis("off")
    nax.annotate("", xy=(0.5, 0.93), xytext=(0.5, 0.22),
                 arrowprops=dict(arrowstyle="-|>", color="#332F28", lw=1.5,
                                 mutation_scale=9))
    nax.text(0.5, 0.02, "N", ha="center", va="bottom", fontsize=8.5,
             fontproperties=FP_EN, color="#332F28")

    # metres per millimetre on paper: use the axes' rendered width
    axpos = ax.get_position()
    map_w_mm = axpos.width * Wmm
    m_per_mm = (xmax - xmin + 2 * pad_x) / map_w_mm
    skm = nice_scale_km(m_per_mm, 0.17 * map_w_mm)
    bar_mm = skm * 1000.0 / m_per_mm
    bar_frac = bar_mm / Wmm
    y0 = mbox[1] + 0.026
    ax.bar = None
    fig.patches.append(plt.Rectangle((mbox[0] + 0.004, y0), bar_frac, 0.0075,
                                     transform=fig.transFigure,
                                     facecolor="#332F28", zorder=20,
                                     figure=fig))
    fig.text(mbox[0] + 0.004 + bar_frac + 0.006, y0 + 0.0015,
             f"0        {skm} कि.मी. / km", fontproperties=FP_HI_N,
             fontsize=6.0, va="bottom", color="#332F28")

    # ----------------------------------------------------------- title/foot
    fig.text(0.5, title_y,
             "राजस्थान — सीमावर्ती ज़िले",
             ha="center", va="top", fontproperties=FP_HI_R, fontsize=14.0,
             color="#1F1B16")
    fig.text(0.5, title_y - 0.030,
             "Rajasthan — the 41 districts of Rajasthan and the 36 districts "
             "of the neighbouring states and of Pakistan that share its border",
             ha="center", va="top", fontproperties=FP_EN, fontsize=6.4,
             color="#5A5348")
    fig.text(0.5, foot_y,
             f"लांबर्ट कन्फॉर्मल कोनिक — मानक समांतर 23°43′N, 29°29′N · "
             f"अधिकतम स्केल त्रुटि {MAX_SCALE_ERROR_PCT:.3f} % "
             f"(= 1 इंच पर {25.4*MAX_SCALE_ERROR_PCT/100:.3f} mm) · "
             f"77 ज़िले: राजस्थान 41 + सीमावर्ती 36",
             ha="center", va="bottom", fontproperties=FP_HI_N, fontsize=5.6,
             color="#7A7367")

    # ----------------------------------------------------------------- save
    tag = "Landscape" if orientation == "landscape" else "Portrait"
    EXPORTS.mkdir(parents=True, exist_ok=True)
    out_png = EXPORTS / f"Rajasthan_Border_Districts_A4_{tag}.png"
    out_pdf = EXPORTS / f"Rajasthan_Border_Districts_A4_{tag}.pdf"
    # label manifest, so the rendering can be audited against the GIS layer
    METADATA.mkdir(parents=True, exist_ok=True)
    man = pd.DataFrame(placed)
    man.insert(0, "page", f"A4_{tag}")
    man.to_csv(METADATA / f"PLACED_LABELS_BORDER_ONLY_{tag}.csv",
               index=False, encoding="utf-8-sig")
    fig.savefig(out_png, dpi=dpi, facecolor="#FFFFFF")
    fig.savefig(out_pdf, dpi=dpi, facecolor="#FFFFFF")
    plt.close(fig)
    print(f"wrote {out_png}")
    print(f"wrote {out_pdf}")
    return dict(orientation=orientation, requested=len(cands),
                placed=len(placed), dropped=len(dropped),
                scale_bar_km=skm, dropped_names=[d["district_en"]
                                                 for d in dropped])


if __name__ == "__main__":
    stats = {}
    for o in ("landscape", "portrait"):
        stats[o] = render(o, dpi=300)
    # manifest of exactly what is drawn
    gdf = gpd.read_file(PROCESSED / "rajasthan_border_atlas.gpkg",
                        layer="districts_all")
    names = pd.read_csv(METADATA / "district_names_hi.csv")
    gdf = gdf.merge(names[["state_province", "district_en", "district_hi"]],
                    on=["state_province", "district_en"], how="left")
    rel = pd.read_csv(ROOT / "BOUNDARY_RELATIONS.csv")
    touch = set(zip(rel.neighbour_country, rel.neighbour_state_province,
                    rel.neighbour_district_en))
    gdf["_k"] = list(zip(gdf.country, gdf.state_province, gdf.district_en))
    sel = pd.concat([gdf[gdf.state_province == "Rajasthan"],
                     gdf[gdf._k.isin(touch)]]).copy()
    sel = sel[["country", "state_province", "district_en", "district_hi"]]
    sel = sel.sort_values(["state_province", "district_en"])
    out = METADATA / "BORDER_ONLY_DISTRICTS.csv"
    sel.to_csv(out, index=False, encoding="utf-8-sig")
    print(f"wrote {out} ({len(sel)} rows)")
    for o, s in stats.items():
        print(f"  {o:<10} requested={s['requested']} placed={s['placed']} "
              f"dropped={s['dropped']} scalebar={s['scale_bar_km']} km")
        if s["dropped_names"]:
            print(f"    dropped: {s['dropped_names']}")
