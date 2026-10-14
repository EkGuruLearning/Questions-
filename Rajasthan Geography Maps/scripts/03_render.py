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
from atlas_lib import PROCESSED, METADATA, ROOT, MAP_PROJ, WGS84  # noqa: E402
from atlas_style import (  # noqa: E402
    PAGES, FRAME, BG, PAGE_BG, INTL_RED, INTER_YELLOW, DIST_EDGE,
    NEIGH_EDGE, TEXT_HI, LEADER, RAJASTHAN_DIVISIONS, DIVISION_ORDER,
    DIVISION_FILL, DIVISION_HI, NEIGHBOUR_STYLE, PROVINCE_HI,
    CHECKLIST_NOT_TOUCHING, PK_SUFFIX,
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
    left, right, bottom, top = 0.010, 0.990, 0.022, 0.950
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
            grp.plot(ax=ax, color=DIVISION_FILL[div], edgecolor=DIST_EDGE,
                     linewidth=0.40 * sf, zorder=2)
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
        add_label(p.x, p.y, NEIGHBOUR_STYLE[st]["label"], 30 * sf, FP_HI_B,
                  "#2B2620", priority=-3, zorder=16)

    # (b) Pakistani province labels
    for prov, hi in PROVINCE_HI.items():
        grp = gdf[(gdf.country == "Pakistan")
                  & (gdf.state_province == prov + PK_SUFFIX)]
        if not len(grp):
            continue
        p = label_point(unary_union(grp.geometry))
        add_label(p.x, p.y, hi, 13 * sf, FP_HI_B, "#5A5348",
                  priority=-2, zorder=15)

    # (c) Rajasthan districts
    for _, row in raj.iterrows():
        p = label_point(row.geometry)
        add_label(p.x, p.y, row.district_hi, 8.6 * sf, FP_HI_B, TEXT_HI,
                  priority=0, zorder=12)

    # (d) neighbouring districts that genuinely touch, then the rest
    rel = pd.read_csv(ROOT / "BOUNDARY_RELATIONS.csv")
    touching = set(zip(rel.neighbour_country, rel.neighbour_state_province,
                       rel.neighbour_district_en))
    for _, row in others.iterrows():
        key = (row.country, row.state_province, row.district_en)
        if key in touching:
            p = label_point(row.geometry)
            add_label(p.x, p.y, row.district_hi, 7.0 * sf, FP_HI, "#4B463E",
                      priority=1, zorder=11)
    for _, row in others.iterrows():
        key = (row.country, row.state_province, row.district_en)
        if key not in touching:
            p = label_point(row.geometry)
            add_label(p.x, p.y, row.district_hi, 5.6 * sf, FP_HI, "#6D675E",
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

    # ------------------------------------------------------------- legend
    lax = fig.add_axes([0.012, 0.026, 0.176, 0.300], facecolor="#FFFFFF")
    lax.set_xticks([])
    lax.set_yticks([])
    for s in lax.spines.values():
        s.set_visible(True)
        s.set_edgecolor("#C9C2B4")
        s.set_linewidth(0.6)
    lax.set_xlim(0, 1)
    lax.set_ylim(0, 1)
    rows = [
        ("line", "अंतरराष्ट्रीय सीमा (भारत–पाकिस्तान)",
         dict(color=INTL_RED, lw=2.8, solid_capstyle="round")),
        ("line", "राजस्थान की अंतर्राज्यीय सीमा",
         dict(color=INTER_YELLOW, lw=2.6, solid_capstyle="round")),
        ("line", "राज्य / प्रांत सीमा", dict(color="#6E6A63", lw=0.9)),
        ("line", "ज़िला सीमा (आंतरिक)", dict(color=DIST_EDGE, lw=0.5)),
        ("patch", "राजस्थान के ज़िले (7 संभाग रंग)",
         dict(facecolor=DIVISION_FILL["Jaipur"], edgecolor=DIST_EDGE, lw=0.4)),
        ("patch", "पड़ोसी राज्यों के ज़िले",
         dict(facecolor=NEIGHBOUR_STYLE["Haryana"]["fill"],
              edgecolor=NEIGH_EDGE, lw=0.35)),
        ("patch", "पाकिस्तान के ज़िले",
         dict(facecolor=NEIGHBOUR_STYLE["Pakistan"]["fill"],
              edgecolor=NEIGH_EDGE, lw=0.35)),
        ("patch", "सूचीबद्ध, परंतु सीमा को न छूने वाले",
         dict(facecolor="#FFFFFF", edgecolor=INTL_RED, hatch="////", lw=0.7)),
    ]
    y = 0.950
    for kind, lab, kw in rows:
        y -= 0.075
        if kind == "line":
            lax.plot([0.035, 0.185], [y, y], **kw)
        else:
            lax.add_patch(Rectangle((0.035, y - 0.024), 0.150, 0.048, **kw))
        lax.text(0.225, y, lab, fontproperties=FP_HI, fontsize=7.6 * sf,
                 va="center", color="#332F28")
    y -= 0.070
    lax.text(0.035, y, "राजस्थान के 7 संभाग:", fontproperties=FP_HI_B,
             fontsize=7.4 * sf, va="center", color="#332F28")
    for div in DIVISION_ORDER:
        y -= 0.042
        lax.add_patch(Rectangle((0.035, y - 0.014), 0.070, 0.028,
                                facecolor=DIVISION_FILL[div],
                                edgecolor=DIST_EDGE, lw=0.3))
        lax.text(0.120, y, DIVISION_HI[div], fontproperties=FP_HI,
                 fontsize=6.8 * sf, va="center", color="#332F28")

    # ------------------------------------------------------- locator inset
    iax = fig.add_axes([0.800, 0.030, 0.185, 0.175], facecolor="#FBF7EE")
    india = gpd.read_file(PROCESSED / "rajasthan_border_atlas.gpkg",
                          layer="india_locator_states").to_crs("EPSG:32644")
    india.plot(ax=iax, color="#EFEBE2", edgecolor="#C6BFB1", lw=0.30)
    hi = india[india.state_name.astype(str).str.contains("RAJASTHAN", na=False)]
    if len(hi):
        hi.plot(ax=iax, color=INTL_RED, edgecolor="#8E1F1F", lw=0.5)
    iax.set_xticks([])
    iax.set_yticks([])
    for s in iax.spines.values():
        s.set_edgecolor("#C9C2B4")
        s.set_linewidth(0.6)
    iax.text(0.5, 1.03, "स्थान संकेत — भारत में राजस्थान",
             transform=iax.transAxes, fontproperties=FP_HI_B,
             fontsize=7.4 * sf, ha="center", va="bottom", color="#332F28")

    # ------------------------------------------------- north arrow + scale
    nax = fig.add_axes([0.720, 0.030, 0.050, 0.070], facecolor="none")
    nax.set_xlim(0, 1)
    nax.set_ylim(0, 1)
    nax.axis("off")
    nax.annotate("", xy=(0.5, 0.86), xytext=(0.5, 0.16),
                 arrowprops=dict(arrowstyle="-|>", color="#332F28", lw=1.3))
    nax.text(0.5, 0.02, "N", ha="center", va="bottom",
             fontproperties=FP_HI_B, fontsize=9 * sf, color="#332F28")

    target_km = 0.18 * (pw / 1000.0)
    skm = min([50, 100, 150, 200, 250, 300, 400, 500],
              key=lambda v: abs(v - target_km))
    sx = px0 + 0.048 * pw
    sy = py0 + 0.048 * ph
    ax.plot([sx, sx + skm * 1000], [sy, sy], color="#332F28",
            lw=1.7 * sf, solid_capstyle="butt", zorder=17)
    for t in (0, 0.5, 1.0):
        ax.plot([sx + t * skm * 1000] * 2, [sy, sy + 0.007 * ph],
                color="#332F28", lw=1.1 * sf, zorder=17)
    ax.text(sx, sy + 0.016 * ph, "0", ha="center", va="bottom",
            fontsize=6.4 * sf, color="#332F28", zorder=17)
    ax.text(sx + skm * 1000, sy + 0.016 * ph, f"{skm} कि.मी.", ha="center",
            va="bottom", fontproperties=FP_HI, fontsize=7.2 * sf,
            color="#332F28", zorder=17)

    # ------------------------------------------------------------- footnote
    fig.text(0.012, 0.006,
             "* हैच किए गए ज़िले — डेरा ग़ाज़ी ख़ान, मुज़फ़्फ़रगढ़, राजनपुर — "
             "परीक्षा-सामग्री में अक्सर राजस्थान से लगे बताए जाते हैं, किन्तु "
             "भौगोलिक ज्यामिति के अनुसार वे राजस्थान को नहीं छूते।",
             ha="left", va="bottom", fontproperties=FP_HI,
             fontsize=7.2 * sf, color="#8C2F1E")

    # ---------------------------------------------------------------- save
    EXPORTS.mkdir(parents=True, exist_ok=True)
    PREVIEWS.mkdir(parents=True, exist_ok=True)
    if preview:
        out_png = PREVIEWS / "Rajasthan_Border_District_Atlas_Preview.png"
        fig.savefig(out_png, dpi=dpi, facecolor=PAGE_BG)
        print("wrote", out_png)
    else:
        out_pdf = EXPORTS / f"Rajasthan_Border_District_Atlas_{page}.pdf"
        out_png = EXPORTS / f"Rajasthan_Border_District_Atlas_{page}.png"
        fig.savefig(out_pdf, dpi=dpi, facecolor=PAGE_BG)
        fig.savefig(out_png, dpi=dpi, facecolor=PAGE_BG)
        print("wrote", out_pdf, out_png)
    plt.close(fig)
    return label_stats


if __name__ == "__main__":
    stats = {}
    for pg in ("A1", "A2", "A3"):
        stats[pg] = render(pg, dpi=200)
    stats["preview"] = render("A1", dpi=160, preview=True)
    print(json.dumps(stats, indent=2) if False else stats)
