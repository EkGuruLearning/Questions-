#!/usr/bin/env python3
"""
03_render.py
============
Renders the master GeoPackage to print-ready PDFs (A1 / A2 / A3) and a
high-resolution preview PNG.

Everything is drawn from the same master project: no geometry is simplified,
moved or re-drawn here.  The only geometric operations are:
  * projection to the documented Lambert Conformal Conic CRS,
  * clipping the drawing extent to the sheet frame (never re-shaping a line),
  * deriving the boundary *lines* that are already implied by the polygons.

The three paper sizes are produced by scaling the identical layout, so the
geographic proportions are identical on every sheet.
"""
from __future__ import annotations

import sys
from pathlib import Path
from datetime import date

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.text import Text
from shapely.geometry import MultiPolygon
from shapely.ops import unary_union

sys.path.insert(0, str(Path(__file__).resolve().parent))
from atlas_lib import (PROCESSED, METADATA, ROOT, MAP_PROJ, WGS84,  # noqa: E402
                      MAX_SCALE_ERROR_PCT)
from atlas_style import (  # noqa: E402
    PAGES, FRAME, BG, PAGE_BG, INTL_RED, INTER_YELLOW, DIST_EDGE,
    NEIGH_EDGE, TEXT_HI, LEADER, RAJASTHAN_DIVISIONS, DIVISION_ORDER,
    DIVISION_FILL, DIVISION_HI, NEIGHBOUR_STYLE, PROVINCE_HI,
    CHECKLIST_NOT_TOUCHING, PK_SUFFIX, FS_RAJASTHAN, FS_TOUCHING,
    FS_OTHER, FS_REGION, FS_PROVINCE, GRATICULE_STEP, GRATICULE_COLOR,
    GRATICULE_LW, DIST_EDGE_STUDY, DIST_EDGE_LW, PANEL_COLS,
)

EXPORTS = ROOT / "exports"
PREVIEWS = ROOT / "previews"
FONT_DIR = ROOT / "fonts"
BUILD_DATE = date.today().isoformat()

# --------------------------------------------------------------------------
# fonts: Noto Sans Devanagari for Hindi, DejaVu Sans as the Latin fallback
# --------------------------------------------------------------------------
FONT_FILE = FONT_DIR / "NotoSansDevanagari-Regular.ttf"
FONT_BOLD = FONT_DIR / "NotoSansDevanagari-Bold.ttf"
FONT_SEMI = FONT_DIR / "NotoSansDevanagari-SemiBold.ttf"
FONT_MED = FONT_DIR / "NotoSansDevanagari-Medium.ttf"
for f in (FONT_FILE, FONT_BOLD, FONT_SEMI, FONT_MED):
    if f.exists():
        fontManager.addfont(str(f))

FP_HI = FontProperties(fname=str(FONT_FILE))
FP_HI_B = FontProperties(fname=str(FONT_BOLD))
plt.rcParams["pdf.fonttype"] = 42      # embed TrueType (OFL permits embedding)
plt.rcParams["ps.fonttype"] = 42
plt.rcParams["font.family"] = ["Noto Sans Devanagari", "DejaVu Sans"]
plt.rcParams["font.sans-serif"] = ["Noto Sans Devanagari", "DejaVu Sans"]


def largest_part(geom):
    if isinstance(geom, MultiPolygon):
        return max(geom.geoms, key=lambda g: g.area)
    return geom


def label_point(geom):
    """A point guaranteed to lie inside the polygon, on its largest part."""
    g = largest_part(geom)
    c = g.centroid
    return c if g.contains(c) else g.representative_point()


def build_boundaries(src_wgs):
    """Derive, from the polygons only, the three classes of line to draw."""
    rj = unary_union(src_wgs[src_wgs.state_province == "Rajasthan"]
                     .geometry.buffer(0))
    pk = unary_union(src_wgs[src_wgs.country == "Pakistan"]
                     .geometry.buffer(0))
    others = src_wgs[(src_wgs.state_province != "Rajasthan")
                     & (src_wgs.country == "India")]
    other_states = {st: unary_union(grp.geometry.buffer(0))
                    for st, grp in others.groupby("state_province")}

    rjP = gpd.GeoSeries([rj], crs=WGS84).to_crs(MAP_PROJ).iloc[0]
    pkP = gpd.GeoSeries([pk], crs=WGS84).to_crs(MAP_PROJ).iloc[0]

    # international boundary: outer edge of Rajasthan/Gujarat facing Pakistan.
    intl_parts = []
    for name in ("Rajasthan", "Gujarat"):
        A = rjP if name == "Rajasthan" else (
            gpd.GeoSeries([other_states[name]], crs=WGS84)
            .to_crs(MAP_PROJ).iloc[0] if name in other_states else None)
        if A is None:
            continue
        seg = A.boundary.intersection(pkP.buffer(1000.0))
        if not seg.is_empty:
            intl_parts.append(seg)
    intl = unary_union(intl_parts) if intl_parts else None

    # interstate boundary of Rajasthan: exact intersection, same source.
    inter_parts = []
    for st, S in other_states.items():
        SP = gpd.GeoSeries([S], crs=WGS84).to_crs(MAP_PROJ).iloc[0]
        seg = rjP.boundary.intersection(SP.boundary)
        if not seg.is_empty:
            inter_parts.append(seg)
    inter = unary_union(inter_parts) if inter_parts else None
    return rjP, pkP, other_states, intl, inter


def draw_line(ax, geom, **kw):
    if geom is None or geom.is_empty:
        return
    geoms = geom.geoms if hasattr(geom, "geoms") else [geom]
    for g in geoms:
        if g.is_empty:
            continue
        if g.geom_type == "LineString":
            ax.plot(*g.xy, **kw)
        elif g.geom_type == "MultiLineString":
            for l in g.geoms:
                ax.plot(*l.xy, **kw)


def draw_graticule(ax, sf):
    """1-degree graticule, projected (so the curves are geometrically true),
    with edge labels.  Lets the reader verify position and spot any
    distortion, instead of having to trust the drawing."""
    import numpy as np
    from shapely.geometry import LineString
    fx0, fy0, fx1, fy1 = FRAME
    lons = np.arange(np.ceil(fx0), np.floor(fx1) + 1e-9, GRATICULE_STEP)
    lats = np.arange(np.ceil(fy0), np.floor(fy1) + 1e-9, GRATICULE_STEP)
    kw = dict(color=GRATICULE_COLOR, lw=GRATICULE_LW * sf, zorder=4,
              solid_capstyle="butt")
    for lo in lons:
        ln = LineString([(lo, y) for y in
                         np.linspace(fy0, fy1, 241)])
        g = gpd.GeoSeries([ln], crs=WGS84).to_crs(MAP_PROJ).iloc[0]
        ax.plot(*g.xy, **kw)
        x, y = g.coords[0]
        ax.text(x, y + 0.012 * (fy1 - fy0) * 111000, f"{lo:.0f}°E",
                fontsize=5.2 * sf, color="#7C7568", ha="center", va="bottom",
                zorder=6)
    for la in lats:
        ln = LineString([(x, la) for x in
                         np.linspace(fx0, fx1, 241)])
        g = gpd.GeoSeries([ln], crs=WGS84).to_crs(MAP_PROJ).iloc[0]
        ax.plot(*g.xy, **kw)
        x, y = g.coords[0]
        ax.text(x + 0.010 * (fx1 - fx0) * 99000, y, f"{la:.0f}°N",
                fontsize=5.2 * sf, color="#7C7568", ha="left", va="center",
                zorder=6)


def wrap_hi(text, width):
    """Wrap Hindi text on spaces/commas without breaking words."""
    out, cur = [], ""
    for tok in text.replace(", ", " , ").split(" "):
        if len(cur) + len(tok) + 1 > width and cur:
            out.append(cur.strip())
            cur = tok
        else:
            cur = (cur + " " + tok).strip()
    if cur:
        out.append(cur.strip())
    return out


# --------------------------------------------------------------------------
# label placement
# --------------------------------------------------------------------------
_MEASURE_CACHE = {}


def measure_text(fig, text, fontprops, fontsize, renderer, dpi):
    """Glyph-metric text extent in device pixels (cached per string)."""
    key = (text, round(fontsize, 3), id(fontprops))
    if key in _MEASURE_CACHE:
        w_pt, h_pt = _MEASURE_CACHE[key]
        return w_pt * dpi / 72.0, h_pt * dpi / 72.0
    t = Text(0, 0, text, fontproperties=fontprops, fontsize=fontsize,
             figure=fig)
    try:
        bb = t.get_window_extent(renderer=renderer)
        w_px, h_px = float(bb.width), float(bb.height)
    except Exception:
        w_px = h_px = 0.0
    if w_px <= 0 or h_px <= 0:
        w_px = len(text) * fontsize * dpi / 72.0 * 0.62
        h_px = fontsize * dpi / 72.0 * 1.0
    _MEASURE_CACHE[key] = (w_px * 72.0 / dpi, h_px * 72.0 / dpi)
    return w_px, h_px


class LabelBox:
    __slots__ = ("cx", "cy", "w", "h", "text", "fs", "prop", "color",
                 "priority", "anchor", "leader_to", "zorder", "bbox")

    def __init__(self, cx, cy, w, h, text, fs, prop, color, priority,
                 anchor, leader_to, zorder, bbox):
        self.cx, self.cy, self.w, self.h = cx, cy, w, h
        self.text, self.fs, self.prop = text, fs, prop
        self.color, self.priority = color, priority
        self.anchor, self.leader_to = anchor, leader_to
        self.zorder, self.bbox = zorder, bbox

    def overlaps(self, other, pad=1.5):
        ax0, ay0, ax1, ay1 = self.bbox
        bx0, by0, bx1, by1 = other.bbox
        return not (ax1 + pad < bx0 or bx1 + pad < ax0
                    or ay1 + pad < by0 or by1 + pad < ay0)


def place_labels(ax, candidates, fig):
    """Greedy collision-avoiding placement in device-pixel space."""
    trans = ax.transData.transform
    inv = ax.transData.inverted().transform
    renderer = fig.canvas.get_renderer()
    dpi = fig.dpi
    placed, dropped = [], []
    for c in sorted(candidates, key=lambda d: (d["priority"], -d["fs"])):
        px, py = trans((c["x"], c["y"]))
        w_px, h_px = measure_text(fig, c["text"], c["prop"], c["fs"],
                                  renderer, dpi)
        offsets = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1),
                   (1, -1), (-1, 1), (0, 2), (0, -2), (0, 3), (0, -3)]
        chosen = None
        for dx, dy in offsets:
            cx = px + dx * (w_px * 0.60 + 5)
            cy = py + dy * (h_px * 0.80 + 4)
            bb = (cx - w_px / 2, cy - h_px / 2, cx + w_px / 2, cy + h_px / 2)
            probe = LabelBox(cx, cy, w_px, h_px, c["text"], c["fs"], c["prop"],
                             c["color"], c["priority"], None, None, 0, bb)
            if not any(probe.overlaps(p) for p in placed):
                chosen = (cx, cy, bb)
                break
        if chosen is None:
            dropped.append(c)
            continue
        cx, cy, bb = chosen
        lb = LabelBox(cx, cy, w_px, h_px, c["text"], c["fs"], c["prop"],
                      c["color"], c["priority"],
                      inv((cx, cy)), (c["x"], c["y"]),
                      c.get("zorder", 10), bb)
        placed.append(lb)
    return placed, dropped


def render(page="A1", dpi=200, preview=False):
    Wmm, Hmm = PAGES[page]
    sf = {"A1": 1.0, "A2": 1 / np.sqrt(2), "A3": 0.5}[page]

    gdf = gpd.read_file(PROCESSED / "rajasthan_border_atlas.gpkg",
                        layer="districts_all")
    names = pd.read_csv(METADATA / "district_names_hi.csv")
    gdf = gdf.merge(names[["state_province", "district_en", "district_hi"]],
                    on=["state_province", "district_en"], how="left")
    src_wgs = gdf.copy()
    gdf = gdf[(gdf.state_province != "DISPUTED")
              & gdf.geometry.intersects(
                  gpd.GeoSeries([__import__("shapely").geometry.box(*FRAME)],
                                crs=WGS84).iloc[0])].copy()
    gdf = gdf.to_crs(MAP_PROJ)
    gdf["division"] = gdf.district_en.map(RAJASTHAN_DIVISIONS)

    rjP, pkP, other_states, intl, inter = build_boundaries(src_wgs)

    # ------------------------------------------------------------------
    fig = plt.figure(figsize=(Wmm / 25.4, Hmm / 25.4), dpi=dpi,
                     facecolor=PAGE_BG)
    left, right, bottom, top = 0.008, 0.992, 0.250, 0.945
    # right-hand reference column and bottom study strip are
    # reserved, so the map box is narrower than the page.
    right = 0.780
    axw, axh = right - left, top - bottom
    fr = gpd.GeoSeries([__import__("shapely").geometry.box(*FRAME)],
                       crs=WGS84).to_crs(MAP_PROJ).iloc[0]
    px0, py0, px1, py1 = fr.bounds
    pw, ph = px1 - px0, py1 - py0
    box_aspect = (axw * Wmm) / (axh * Hmm)
    data_aspect = pw / ph
    if data_aspect > box_aspect:
        hh = axh * (box_aspect / data_aspect)
        ax = fig.add_axes([left, bottom + (axh - hh) / 2, axw, hh])
    else:
        ww = axw * (data_aspect / box_aspect)
        ax = fig.add_axes([left + (axw - ww) / 2, bottom, ww, axh])
    ax.set_xlim(px0, px1)
    ax.set_ylim(py0, py1)
    ax.set_aspect("equal", adjustable="box")
    ax.set_facecolor(BG)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    # ------------------------------------------------------------------ fills
    others = gdf[gdf.state_province != "Rajasthan"]
    for st, grp in others.groupby("state_province"):
        if (grp.country == "Pakistan").all():
            fill = NEIGHBOUR_STYLE["Pakistan"]["fill"]
        else:
            fill = NEIGHBOUR_STYLE.get(st, dict(fill="#EFEAE0"))["fill"]
        grp.plot(ax=ax, color=fill, edgecolor=NEIGH_EDGE,
                 linewidth=0.35 * sf, zorder=1)
    raj = gdf[gdf.state_province == "Rajasthan"]
    for div in DIVISION_ORDER:
        grp = raj[raj.division == div]
        if len(grp):
            grp.plot(ax=ax, color=DIVISION_FILL[div],
                     edgecolor=DIST_EDGE_STUDY, linewidth=DIST_EDGE_LW * sf,
                     zorder=2)
    for (c, s, d) in CHECKLIST_NOT_TOUCHING:
        row = gdf[(gdf.country == c) & (gdf.state_province == s)
                  & (gdf.district_en == d)]
        if len(row):
            row.plot(ax=ax, facecolor="none", edgecolor=INTL_RED,
                     hatch="////", linewidth=0.55 * sf, zorder=3)

    # ------------------------------------------------------------ boundaries
    draw_line(ax, inter, color=INTER_YELLOW, lw=2.6 * sf,
              solid_capstyle="round", zorder=8)
    draw_line(ax, intl, color=INTL_RED, lw=2.8 * sf,
              solid_capstyle="round", zorder=9)
    draw_line(ax, rjP.boundary, color="#6E6A63", lw=0.70 * sf, zorder=7)

    # ------------------------------------------------------------- labels
    cands = []

    def add_label(x, y, text, fs, prop, color, priority, zorder):
        cands.append(dict(x=x, y=y, text=text, fs=fs, prop=prop, color=color,
                          priority=priority, zorder=zorder))

    # (a) the six big region labels, placed first at the region's own interior
    region_geoms = {}
    for st in NEIGHBOUR_STYLE:
        if st == "Pakistan":
            u = gdf[gdf.country == "Pakistan"].geometry.unary_union
        else:
            u = gdf[gdf.state_province == st].geometry.unary_union
        if u is not None and not u.is_empty:
            region_geoms[st] = u
    for st, u in region_geoms.items():
        p = label_point(u)
        add_label(p.x, p.y, NEIGHBOUR_STYLE[st]["label"], FS_REGION * sf, FP_HI_B,
                  "#2B2620", priority=-3, zorder=16)

    # (b) Pakistani province labels
    for prov, hi in PROVINCE_HI.items():
        grp = gdf[(gdf.country == "Pakistan")
                  & (gdf.state_province == prov + PK_SUFFIX)]
        if not len(grp):
            continue
        p = label_point(unary_union(grp.geometry))
        add_label(p.x, p.y, hi, FS_PROVINCE * sf, FP_HI_B, "#5A5348",
                  priority=-2, zorder=15)

    # (c) Rajasthan districts
    for _, row in raj.iterrows():
        p = label_point(row.geometry)
        add_label(p.x, p.y, row.district_hi, FS_RAJASTHAN * sf, FP_HI_B, TEXT_HI,
                  priority=0, zorder=12)

    # (d) neighbouring districts that genuinely touch, then the rest
    rel = pd.read_csv(ROOT / "BOUNDARY_RELATIONS.csv")
    touching = set(zip(rel.neighbour_country, rel.neighbour_state_province,
                       rel.neighbour_district_en))
    for _, row in others.iterrows():
        key = (row.country, row.state_province, row.district_en)
        if key in touching:
            p = label_point(row.geometry)
            add_label(p.x, p.y, row.district_hi, FS_TOUCHING * sf, FP_HI, "#3F3A33",
                      priority=1, zorder=11)
    for _, row in others.iterrows():
        key = (row.country, row.state_province, row.district_en)
        if key not in touching:
            p = label_point(row.geometry)
            add_label(p.x, p.y, row.district_hi, FS_OTHER * sf, FP_HI, "#6D675E",
                      priority=3, zorder=10)

    placed, dropped = place_labels(ax, cands, fig)
    label_stats = dict(
        requested=len(cands), placed=len(placed), dropped=len(dropped))

    # record every label actually drawn, with the feature it belongs to, so
    # that review round 2 can audit the rendering against the GIS layer
    rec_rows = []
    inv = {(r.district_hi, r.state_province): r.district_en
           for _, r in gdf.iterrows()}
    for lb in placed:
        moved = (abs(lb.anchor[0] - lb.leader_to[0]) > 1e-6
                 or abs(lb.anchor[1] - lb.leader_to[1]) > 1e-6)
        rec_rows.append(dict(
            page=page, text=lb.text, fontsize_pt=round(lb.fs, 2),
            priority=lb.priority,
            anchor_x=round(lb.anchor[0], 1), anchor_y=round(lb.anchor[1], 1),
            polygon_x=round(lb.leader_to[0], 1),
            polygon_y=round(lb.leader_to[1], 1),
            moved_from_polygon=bool(moved) and lb.priority >= 0,
            has_leader_line=bool(moved) and lb.priority >= 0,
        ))
    METADATA.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rec_rows).to_csv(
        METADATA / f"PLACED_LABELS_{page}.csv", index=False,
        encoding="utf-8-sig")

    for lb in placed:
        if lb.priority >= 0 and (abs(lb.anchor[0] - lb.leader_to[0]) > 1e-6
                                 or abs(lb.anchor[1] - lb.leader_to[1]) > 1e-6):
            ax.plot([lb.leader_to[0], lb.anchor[0]],
                    [lb.leader_to[1], lb.anchor[1]], color=LEADER,
                    lw=0.35 * sf, zorder=lb.zorder - 1)
            ax.plot(*lb.leader_to, marker="o", ms=1.2 * sf, color=LEADER,
                    zorder=lb.zorder)
        ax.text(lb.anchor[0], lb.anchor[1], lb.text,
                fontproperties=lb.prop, fontsize=lb.fs, color=lb.color,
                ha="center", va="center", zorder=lb.zorder)

    # -------------------------------------------------------------- title
    n_raj = int((gdf.state_province == "Rajasthan").sum())
    n_div = len([d for d in DIVISION_ORDER if (raj.division == d).any()])
    fig.text(0.5, 0.980, "राजस्थान — सीमावर्ती ज़िला एटलस", ha="center",
             va="top", fontproperties=FP_HI_B, fontsize=25 * sf,
             color="#1F1B16")
    fig.text(0.5, 0.941,
             f"राजस्थान के {n_raj} ज़िले · {n_div} संभाग   |   "
             "पाकिस्तान · पंजाब · हरियाणा · उत्तर प्रदेश · "
             "मध्य प्रदेश · गुजरात — सीमावर्ती ज़िले",
             ha="center", va="top", fontproperties=FP_HI,
             fontsize=12.5 * sf, color="#4A443B")
    fig.text(0.5, 0.918,
             "ज्यामिति: Survey of India–व्युत्पन्न ज़िला सीमाएँ (भारत) · "
             "WFP / OCHA COD-AB v01 (पाकिस्तान)  |  "
             f"निर्माण तिथि {BUILD_DATE}",
             ha="center", va="top", fontproperties=FP_HI,
             fontsize=8.6 * sf, color="#7A7367")

    # ----------------------------------------------------------- graticule
    draw_graticule(ax, sf)

    # ==================================================================
    # RIGHT-HAND REFERENCE COLUMN
    # ==================================================================
    RX, RW = 0.788, 0.204

    # ---- locator inset ------------------------------------------------
    iax = fig.add_axes([RX, 0.790, RW, 0.155], facecolor="#FBF7EE")
    india = gpd.read_file(PROCESSED / "rajasthan_border_atlas.gpkg",
                          layer="india_locator_states").to_crs("EPSG:32644")
    india.plot(ax=iax, color="#EFEBE2", edgecolor="#C6BFB1", lw=0.30)
    hi = india[india.state_name.astype(str).str.contains("RAJASTHAN", na=False)]
    if len(hi):
        hi.plot(ax=iax, color=INTL_RED, edgecolor="#8E1F1F", lw=0.5)
    iax.set_xticks([])
    iax.set_yticks([])
    for sp in iax.spines.values():
        sp.set_edgecolor("#C9C2B4")
        sp.set_linewidth(0.6)
    iax.text(0.5, 1.06, "स्थान संकेत — भारत में राजस्थान",
             transform=iax.transAxes, fontproperties=FP_HI_B,
             fontsize=8.0 * sf, ha="center", va="bottom", color="#332F28")

    # ---- legend -------------------------------------------------------
    lax = fig.add_axes([RX, 0.360, RW, 0.420], facecolor="#FFFFFF")
    lax.set_xticks([])
    lax.set_yticks([])
    for sp in lax.spines.values():
        sp.set_visible(True)
        sp.set_edgecolor("#C9C2B4")
        sp.set_linewidth(0.6)
    lax.set_xlim(0, 1)
    lax.set_ylim(0, 1)
    rows = [
        ("line", "अंतरराष्ट्रीय सीमा\n(भारत–पाकिस्तान)",
         dict(color=INTL_RED, lw=2.8, solid_capstyle="round"), 0.075),
        ("line", "राजस्थान की अंतर्राज्यीय सीमा",
         dict(color=INTER_YELLOW, lw=2.6, solid_capstyle="round"), 0.075),
        ("line", "राज्य / प्रांत सीमा", dict(color="#6E6A63", lw=0.9), 0.050),
        ("line", "ज़िला सीमा", dict(color=DIST_EDGE_STUDY, lw=0.5), 0.050),
        ("line", "ग्रेटिक्यूल (1°)", dict(color=GRATICULE_COLOR, lw=0.45), 0.050),
        ("patch", "राजस्थान के ज़िले\n(7 संभाग — रंग अलग)",
         dict(facecolor=DIVISION_FILL["Jaipur"], edgecolor=DIST_EDGE_STUDY,
              lw=0.4), 0.075),
        ("patch", "पड़ोसी राज्यों के ज़िले",
         dict(facecolor=NEIGHBOUR_STYLE["Haryana"]["fill"],
              edgecolor=NEIGH_EDGE, lw=0.35), 0.050),
        ("patch", "पाकिस्तान के ज़िले",
         dict(facecolor=NEIGHBOUR_STYLE["Pakistan"]["fill"],
              edgecolor=NEIGH_EDGE, lw=0.35), 0.050),
        ("patch", "सूचीबद्ध, परंतु सीमा को\nन छूने वाले ज़िले",
         dict(facecolor="#FFFFFF", edgecolor=INTL_RED, hatch="////",
              lw=0.7), 0.075),
    ]
    y = 0.975
    for kind, lab, kw, dy in rows:
        y -= dy
        if kind == "line":
            lax.plot([0.035, 0.175], [y, y], **kw)
        else:
            lax.add_patch(Rectangle((0.035, y - 0.022), 0.140, 0.044, **kw))
        lax.text(0.215, y, lab, fontproperties=FP_HI, fontsize=7.0 * sf,
                 va="center", linespacing=1.25, color="#332F28")
    y -= 0.062
    lax.text(0.035, y, "राजस्थान के 7 संभाग:", fontproperties=FP_HI_B,
             fontsize=7.2 * sf, va="center", color="#332F28")
    for div in DIVISION_ORDER:
        y -= 0.040
        lax.add_patch(Rectangle((0.035, y - 0.013), 0.062, 0.026,
                                facecolor=DIVISION_FILL[div],
                                edgecolor=DIST_EDGE_STUDY, lw=0.3))
        n_divd = int((raj.district_en.map(RAJASTHAN_DIVISIONS) == div).sum())
        lax.text(0.115, y, f"{DIVISION_HI[div]} ({n_divd})",
                 fontproperties=FP_HI, fontsize=6.6 * sf, va="center",
                 color="#332F28")

    # ---- north arrow + scale bar --------------------------------------
    nax = fig.add_axes([RX, 0.255, RW, 0.095], facecolor="none")
    nax.set_xlim(0, 1)
    nax.set_ylim(0, 1)
    nax.axis("off")
    nax.annotate("", xy=(0.10, 0.86), xytext=(0.10, 0.16),
                 arrowprops=dict(arrowstyle="-|>", color="#332F28", lw=1.4))
    nax.text(0.10, 0.02, "N", ha="center", va="bottom",
             fontproperties=FP_HI_B, fontsize=9 * sf, color="#332F28")
    skm = min([50, 100, 150, 200, 250, 300, 400, 500],
              key=lambda v: abs(v - 0.18 * (pw / 1000.0)))
    nax.plot([0.30, 0.95], [0.30, 0.30], color="#332F28", lw=1.7 * sf,
             solid_capstyle="butt")
    for t in (0, 0.5, 1.0):
        nax.plot([0.30 + t * 0.65] * 2, [0.30, 0.38], color="#332F28",
                 lw=1.1 * sf)
    nax.text(0.30, 0.44, "0", ha="center", va="bottom", fontsize=6.4 * sf,
             color="#332F28")
    nax.text(0.95, 0.44, f"{skm} कि.मी.", ha="center", va="bottom",
             fontproperties=FP_HI, fontsize=7.2 * sf, color="#332F28")

    # ---- accuracy note -------------------------------------------------
    fig.text(RX, 0.228,
             f"प्रक्षेप: लांबर्ट कन्फॉर्मल कोनिक, मानक समांतर "
             f"24°26′N व 29°46′N\n"
             f"शीट पर अधिकतम स्केल त्रुटि {MAX_SCALE_ERROR_PCT:.3f} % "
             f"= 1 इंच पर {25.4*MAX_SCALE_ERROR_PCT/100:.3f} mm\n"
             f"लंबाई/क्षेत्रफल: WGS 84 दीर्घवृत्त पर जियोडेसिक (बिना प्रक्षेप त्रुटि)",
             ha="left", va="top", fontproperties=FP_HI,
             fontsize=6.6 * sf, color="#5A5348", linespacing=1.5)

    # ==================================================================
    # BOTTOM STUDY STRIP — three panels
    # ==================================================================
    PY0, PH = 0.026, 0.211
    PHmm = PH * Hmm
    # line advance in axes-fraction, derived from the real text
    # height (1.35 x font size) rather than a guessed fraction
    def step(F, gap=0.55):
        return (1.35 * F * 0.3528 + gap) / PHmm
    OVERFLOW = []

    # ---- panel A: districts of each neighbour that touch Rajasthan ----
    axA = fig.add_axes([PANEL_COLS[0][0], PY0,
                        PANEL_COLS[0][1] - PANEL_COLS[0][0], PH],
                       facecolor="#FFFFFF")
    for sp in axA.spines.values():
        sp.set_edgecolor("#C9C2B4")
        sp.set_linewidth(0.6)
    axA.set_xticks([])
    axA.set_yticks([])
    axA.set_xlim(0, 1)
    axA.set_ylim(0, 1)
    axA.text(0.03, 0.955, "राजस्थान की सीमा से लगे ज़िले — पड़ोसी राज्य/देश",
             fontproperties=FP_HI_B, fontsize=9.0 * sf, va="top",
             color="#1F1B16")
    yy = 1.0 - step(9.0 * sf) * 1.25
    for st in ["Pakistan", "Punjab", "Haryana", "Uttar Pradesh",
               "Madhya Pradesh", "Gujarat"]:
        sub = rel[rel.neighbour_state_province == st] \
            if st == "Pakistan" else rel[(rel.neighbour_country == "India")
                                         & (rel.neighbour_state_province == st)]
        if not len(sub):
            continue
        grp = (sub.groupby("neighbour_district_en")["shared_border_km"].sum()
               .sort_values(ascending=False))
        his = []
        for nm in grp.index:
            m = names[(names.state_province == st) & (names.district_en == nm)]
            if len(m):
                his.append(m.district_hi.iloc[0])
        label = (NEIGHBOUR_STYLE[st]["label"] if st != "Pakistan"
                 else "पाकिस्तान")
        head = f"● {label} — {len(grp)} ज़िले, {grp.sum():.0f} कि.मी."
        axA.text(0.03, yy, head, fontproperties=FP_HI_B, fontsize=7.6 * sf,
                 va="top", color="#3A352E")
        yy -= step(7.6 * sf)
        for ln in wrap_hi("    " + ", ".join(his), 58):
            if yy < 0.01:
                OVERFLOW.append(("A", st, ln))
                break
            axA.text(0.03, yy, ln, fontproperties=FP_HI, fontsize=6.8 * sf,
                     va="top", color="#4A443B")
            yy -= step(6.8 * sf)
        yy -= step(6.8 * sf) * 0.35

    # ---- panel B: the international border + length comparison --------
    axB = fig.add_axes([PANEL_COLS[1][0], PY0,
                        PANEL_COLS[1][1] - PANEL_COLS[1][0], PH],
                       facecolor="#FFFFFF")
    for sp in axB.spines.values():
        sp.set_edgecolor("#C9C2B4")
        sp.set_linewidth(0.6)
    axB.set_xticks([])
    axB.set_yticks([])
    axB.set_xlim(0, 1)
    axB.set_ylim(0, 1)
    axB.text(0.03, 0.975, "अंतरराष्ट्रीय सीमा (पाकिस्तान) — राजस्थान के ज़िले",
             fontproperties=FP_HI_B, fontsize=9.0 * sf, va="top",
             color="#1F1B16")
    pkrel = rel[rel.neighbour_country == "Pakistan"]
    yy = 1.0 - step(9.0 * sf) * 1.25
    for nm, v in (pkrel.groupby("rajasthan_district_en")["shared_border_km"]
                  .sum().sort_values(ascending=False).items()):
        m = names[(names.state_province == "Rajasthan")
                  & (names.district_en == nm)]
        hn = m.district_hi.iloc[0] if len(m) else nm
        if yy > 0.01:
            axB.text(0.03, yy, f"● {hn}", fontproperties=FP_HI,
                     fontsize=7.4 * sf, va="top", color="#3A352E")
            axB.text(0.97, yy, f"{v:.0f} कि.मी.", fontproperties=FP_HI,
                     fontsize=7.4 * sf, va="top", ha="right", color="#3A352E")
        yy -= step(7.4 * sf)
    yy -= step(7.4 * sf) * 0.8
    for txt, fsz, col in [
            ("सीमा लंबाई — GIS बनाम प्रकाशित", 7.6, "#8C2F1E"),
            ("GIS    1,036 / 90 / 1,039 / 462 / 2,110 / 723 कि.मी.", 6.6, "#4A443B"),
            ("पुस्तक 1,070 / 89 / 1,262 / 877 / 1,600 / 1,022 कि.मी.", 6.6, "#8C2F1E"),
            ("(पाकिस्तान, पंजाब, हरियाणा, उ.प्र., म.प्र., गुजरात)", 6.0, "#7A7367"),
            ("ज़िलों की गिनती प्रकाशित सूचियों से मेल खाती है;", 6.0, "#7A7367"),
            ("लंबाई नहीं मिलती — विवरण UNRESOLVED में।", 6.0, "#7A7367")]:
        if yy < 0.01:
            OVERFLOW.append(("B", "lengths", txt))
            break
        axB.text(0.03, yy, txt, fontproperties=FP_HI, fontsize=fsz * sf,
                 va="top", color=col)
        yy -= step(fsz * sf)

    # ---- panel C: 7 divisions and their districts ---------------------
    axC = fig.add_axes([PANEL_COLS[2][0], PY0,
                        PANEL_COLS[2][1] - PANEL_COLS[2][0], PH],
                       facecolor="#FFFFFF")
    for sp in axC.spines.values():
        sp.set_edgecolor("#C9C2B4")
        sp.set_linewidth(0.6)
    axC.set_xticks([])
    axC.set_yticks([])
    axC.set_xlim(0, 1)
    axC.set_ylim(0, 1)
    axC.text(0.03, 0.975, "राजस्थान के 7 संभाग और उनके ज़िले (कुल 41)",
             fontproperties=FP_HI_B, fontsize=9.0 * sf, va="top",
             color="#1F1B16")
    yy = 1.0 - step(9.0 * sf) * 1.25
    for div in DIVISION_ORDER:
        ds = raj[raj.district_en.map(RAJASTHAN_DIVISIONS) == div]
        his = []
        for nm in sorted(ds.district_en):
            m = names[(names.state_province == "Rajasthan")
                      & (names.district_en == nm)]
            if len(m):
                his.append(m.district_hi.iloc[0])
        axC.add_patch(Rectangle((0.03, yy - 0.030), 0.035, 0.030,
                                facecolor=DIVISION_FILL[div],
                                edgecolor=DIST_EDGE_STUDY, lw=0.3,
                                transform=axC.transAxes))
        axC.text(0.075, yy, f"{DIVISION_HI[div]} ({len(ds)})",
                 fontproperties=FP_HI_B, fontsize=7.2 * sf, va="top",
                 color="#3A352E")
        yy -= step(7.2 * sf)
        for ln in wrap_hi("    " + ", ".join(his), 56):
            if yy < 0.01:
                OVERFLOW.append(("C", div, ln))
                break
            axC.text(0.075, yy, ln, fontproperties=FP_HI, fontsize=6.4 * sf,
                     va="top", color="#4A443B")
            yy -= step(6.4 * sf)
        yy -= step(6.4 * sf) * 0.30

    # ---- footnote on the hatch ----------------------------------------
    fig.text(0.008, 0.006,
             "* हैच किए गए ज़िले — डेरा ग़ाज़ी ख़ान, मुज़फ़्फ़रगढ़, राजनपुर — "
             "परीक्षा-सामग्री में अक्सर राजस्थान से लगे बताए जाते हैं, किन्तु "
             "भौगोलिक ज्यामिति के अनुसार वे राजस्थान को नहीं छूते।  "
             "ज्यामिति: Survey of India–व्युत्पन्न ज़िला सीमाएँ (भारत) · "
             "WFP / OCHA COD-AB v01 (पाकिस्तान) · निर्माण " + BUILD_DATE,
             ha="left", va="bottom", fontproperties=FP_HI,
             fontsize=6.6 * sf, color="#7A3020")

    # ---------------------------------------------------------------- save
    EXPORTS.mkdir(parents=True, exist_ok=True)
    PREVIEWS.mkdir(parents=True, exist_ok=True)
    if preview:
        out_png = PREVIEWS / "Rajasthan_Border_District_Atlas_Preview.png"
        fig.savefig(out_png, dpi=dpi, facecolor=PAGE_BG)
        if OVERFLOW:
            print("!! PANEL OVERFLOW:", OVERFLOW)
        print("wrote", out_png)
    else:
        out_pdf = EXPORTS / f"Rajasthan_Border_District_Atlas_{page}.pdf"
        out_png = EXPORTS / f"Rajasthan_Border_District_Atlas_{page}.png"
        fig.savefig(out_pdf, dpi=dpi, facecolor=PAGE_BG)
        fig.savefig(out_png, dpi=dpi, facecolor=PAGE_BG)
        if OVERFLOW:
            print("!! PANEL OVERFLOW:", OVERFLOW)
        print("wrote", out_pdf, out_png)
    plt.close(fig)
    return label_stats


if __name__ == "__main__":
    stats = {}
    for pg in ("A1", "A2", "A3"):
        stats[pg] = render(pg, dpi=200)
    stats["preview"] = render("A1", dpi=160, preview=True)
    print(json.dumps(stats, indent=2) if False else stats)
