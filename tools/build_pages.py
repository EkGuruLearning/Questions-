#!/usr/bin/env python3
"""Generate the whole public website as plain HTML.

Why generated HTML instead of JavaScript rendering:

* nothing has to be fetched after the page loads, so a page opens instantly even on
  a slow phone — the list is already in the HTML;
* search engines see the real links and the real text (JavaScript lists are often
  missed);
* it keeps working with JavaScript switched off.

The pages are written straight into the folders the site already publishes:

    index.html                                     home (one card per subject)
    subjects/index.html                            all subjects
    subjects/index.html?subject=… isn't needed     every subject gets real folders:
    subjects/<slug>/index.html                     folder browser for that subject
    subjects/<slug>/<folder>/index.html            a real page per folder, so a folder
                                                   link works as a deep link and every
                                                   page has a breadcrumb back up
    subjects/previous-year-papers/exams/<id>/index.html
                                                   verified year-wise exam source pages
    subjects/computer-network/material/index.html  (kept: older links still work)
    subjects/computer-network/test/index.html      (hand-written: the online test app)

Inputs: data/site.json (tools/build_catalog.py), data/catalog/subjects.json (labels) and
`data/catalog/previous-year-papers.json` (verified exam/year source records).

Run:
    python3 tools/build_pages.py            # write the pages
    python3 tools/build_pages.py --check    # fail if a page is missing or out of date
"""
from __future__ import annotations

import argparse
import html
import json
import pathlib
import posixpath
import re
import struct
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "data/site.json"
SUBJECTS = ROOT / "data/catalog/subjects.json"
PAPER_CATALOG = ROOT / "data/catalog/previous-year-papers.json"
PAPER_KINDS = {
    "official-paper": "Official paper",
    "official-answer-key": "Official answer key",
    "official-archive": "Official archive",
    "official-notice": "Official notice",
    "candidate-login": "Candidate login / limited window",
    "practice-third-party": "Third-party / memory-based",
    "sample-paper": "Sample questions only",
    "local-paper": "Available on EkGuru",
}
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%234f46e5'/%3E%3Ctext x='32' y='44' "
           "font-size='34' font-family='Arial' font-weight='bold' fill='%23fff' "
           "text-anchor='middle'%3Ee%3C/text%3E%3C/svg%3E")
BRAND_TAGLINE = "Study material, previous year papers aur online test — sab free, koi login nahi."


# --------------------------------------------------------------------------- html
def esc(text) -> str:
    return html.escape(str(text if text is not None else ""), quote=True)


def url_for(path: str) -> str:
    return urllib.parse.quote(path, safe="/")


def rel(depth: int) -> str:
    return "../" * depth


def href_from(page: str, target_repo_path: str) -> str:
    """Shortest relative link from a published page to another repo path.

    `href_from("subjects/computer-network/answers/index.html", "content/.../a.pdf")`
    -> "../../content/.../a.pdf"  (so links stay readable and never guess depth).
    """
    page_dir = posixpath.dirname(page)
    return posixpath.relpath(target_repo_path, page_dir or ".")


def human_size(num_bytes: int) -> str:
    if num_bytes >= 1024 * 1024:
        return f"{num_bytes / (1024 * 1024):.1f} MB"
    if num_bytes >= 1024:
        return f"{num_bytes / 1024:.0f} KB"
    return f"{num_bytes} B"


def plural(count: int, one: str, many: str) -> str:
    return f"{count} {one if count == 1 else many}"


def number(value) -> str:
    try:
        return f"{int(value):,}".replace(",", ",")
    except (TypeError, ValueError):
        return str(value)


def paper_year_id(year: str) -> str:
    """Stable HTML anchor for years or year ranges such as `2007–2025`."""
    token = re.sub(r"[^A-Za-z0-9_-]+", "-", str(year)).strip("-")
    return "pyq-year-" + (token or "year")


def validate_paper_catalog(catalog: dict) -> None:
    """Fail early on a broken exam entry or an unsafe/malformed paper link."""
    if catalog.get("schema_version") != 1:
        raise SystemExit("FAIL: previous-year-papers.json must use schema_version 1")
    group_ids: set[str] = set()
    exam_ids: set[str] = set()
    for group in catalog.get("groups", []):
        group_id = group.get("id", "")
        if not group_id or group_id in group_ids:
            raise SystemExit(f"FAIL: missing or duplicate PYQ group id: {group_id!r}")
        group_ids.add(group_id)
        if not group.get("title_en") or not group.get("title_hi"):
            raise SystemExit(f"FAIL: PYQ group {group_id!r} needs bilingual titles")
        for exam in group.get("exams", []):
            exam_id = exam.get("id", "")
            if not exam_id or exam_id in exam_ids or not re.fullmatch(r"[a-z0-9-]+", exam_id):
                raise SystemExit(f"FAIL: missing, duplicate or invalid PYQ exam id: {exam_id!r}")
            exam_ids.add(exam_id)
            for field in ("title_en", "title_hi", "summary_en", "summary_hi"):
                if not (exam.get(field) or "").strip():
                    raise SystemExit(f"FAIL: PYQ exam {exam_id!r} needs {field}")
            years = exam.get("years", [])
            if not years:
                raise SystemExit(f"FAIL: PYQ exam {exam_id!r} needs at least one verified year/session")
            seen_years: set[str] = set()
            for year in years:
                year_label = str(year.get("year", "")).strip()
                if not year_label or year_label in seen_years:
                    raise SystemExit(f"FAIL: {exam_id!r} has a missing or duplicate year label")
                seen_years.add(year_label)
                for field in ("title_en", "title_hi"):
                    if not (year.get(field) or "").strip():
                        raise SystemExit(f"FAIL: {exam_id!r}/{year_label} needs {field}")
                links = year.get("links", [])
                if not links:
                    raise SystemExit(f"FAIL: {exam_id!r}/{year_label} needs at least one source link")
                for link in links:
                    for field in ("label_en", "label_hi", "url"):
                        if not (link.get(field) or "").strip():
                            raise SystemExit(f"FAIL: {exam_id!r}/{year_label} link needs {field}")
                    if link.get("kind") not in PAPER_KINDS:
                        raise SystemExit(f"FAIL: {exam_id!r}/{year_label} has unknown source kind {link.get('kind')!r}")
                    parsed = urllib.parse.urlsplit(link["url"])
                    if parsed.scheme:
                        if parsed.scheme != "https" or not parsed.netloc:
                            raise SystemExit(f"FAIL: PYQ source must use https: {link['url']}")
                    elif link["url"].startswith("/") or ".." in pathlib.PurePosixPath(link["url"]).parts:
                        raise SystemExit(f"FAIL: local PYQ source must be a repo-relative path: {link['url']}")
            for link in exam.get("sources", []):
                for field in ("label_en", "label_hi", "url"):
                    if not (link.get(field) or "").strip():
                        raise SystemExit(f"FAIL: {exam_id!r} source link needs {field}")
                if link.get("kind") not in PAPER_KINDS:
                    raise SystemExit(f"FAIL: {exam_id!r} has unknown source kind {link.get('kind')!r}")
                parsed = urllib.parse.urlsplit(link["url"])
                if parsed.scheme != "https" or not parsed.netloc:
                    raise SystemExit(f"FAIL: PYQ source must use https: {link['url']}")


# ------------------------------------------------------------------- fragments
# ---------------------------------------------------------------- subject extras
# Page copy that is specific to one subject: the map hero on the geography page
# and its search-engine block. Everything else comes from data/site.json.
SUBJECT_EXTRAS = {
    "rajasthan-geography": {
        "title": "Rajasthan Map — 41 simavarti jile, border districts A1/A2/A3/A4 | EkGuru Learning",
        "description": (
            "Rajasthan ke simavarti jile ka naksha — 41 jile aur Pakistan, Punjab, Haryana, UP, "
            "MP, Gujarat ke 36 seemavarti jile. A1 poster se A4 portrait/landscape tak, "
            "Hindi labels ke saath free download."
        ),
        "keywords": (
            "Rajasthan border districts map, राजस्थान सीमावर्ती जिले, Rajasthan 41 districts, "
            "Barmer Bikaner Sri Ganganagar Jaisalmer Phalodi border, Pakistan border Rajasthan, "
            "A4 portrait landscape map, RPSC REET Patwari map"
        ),
        "structured_data": """  {
    "@context": "https://schema.org",
    "@type": "ImageGallery",
    "name": "Rajasthan border districts map — A1, A2, A3 and A4 sheets",
    "description": "Rajasthan ke simavarti jile: all 41 districts of Rajasthan with the 36 border-sharing districts of Pakistan (Punjab and Sindh) and of Punjab, Haryana, Uttar Pradesh, Madhya Pradesh and Gujarat. Hindi labels, printable A1 poster to A4 portrait and landscape.",
    "inLanguage": "hi",
    "about": {
      "@type": "Place",
      "name": "Rajasthan, India",
      "description": "Rajasthan ke 41 jile aur unki siimavarti seemayein — Pakistan aur paanch padosi rajya."
    },
    "isFamilyFriendly": true
  }""",
        "hero_image": "assets/img/rajasthan-border-atlas-preview.webp",
        "hero_image_w": 1600,
        "hero_image_h": 1130,
        "hero_alt": "Rajasthan border-district map with Hindi district labels and highlighted state borders.",
        "hero_lead": "Folder kholo: <b>Map › Rajasthan</b>. Jitne maps aayenge, waise hi naye folders yahan dikhte jayenge.",
        "hero_caption": "Border district map — poora map A1 / A2 / A3 / A4 file me.",
        "hero_primary": ("Rajasthan ke maps kholo", "subjects/rajasthan-geography/map/rajasthan/index.html"),
        "hero_secondary": ("A1 poster download",
                           "content/rajasthan-geography/map/rajasthan/Rajasthan-Border-District-Atlas-A1.png"),
        "hero_pdf": ("PDF में नक्शा देखें", "subjects/rajasthan-geography/map/rajasthan/index.html#map-pdf-preview"),
    },
}


def image_size(rel_path: str) -> tuple[int, int] | None:
    """Pixel size of a PNG/JPG file, so <img> can reserve its box (koi layout jump nahi)."""
    path = ROOT / rel_path
    try:
        head = path.read_bytes()[:4096]
    except OSError:
        return None
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        width, height = struct.unpack(">II", head[16:24])
        return int(width), int(height)
    if head[:2] == b"\xff\xd8":  # JPEG: frame header tak segments scan karo
        index = 2
        while index + 9 < len(head):
            if head[index] != 0xFF:
                index += 1
                continue
            marker = head[index + 1]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3):
                height, width = struct.unpack(">HH", head[index + 5:index + 9])
                return int(width), int(height)
            if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
                index += 2
                continue
            index += 2 + struct.unpack(">H", head[index + 2:index + 4])[0]
    return None



def head(title: str, description: str, depth: int, extra_head: str = "", extra_body: str = "",
         keywords: str = "", structured_data: str = "") -> str:
    prefix = rel(depth)
    keyword_line = f'\n  <meta name="keywords" content="{esc(keywords)}">' if keywords else ""
    extra_head = extra_head + keyword_line
    if structured_data:
        extra_head += f'\n  <script type="application/ld+json">\n{structured_data}\n  </script>'
    return f"""<!doctype html>
<html lang="hi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#4f46e5">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <link rel="icon" href="{FAVICON}">
  <link rel="stylesheet" href="{prefix}assets/css/ekguru.css">{extra_head}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
{extra_body}"""


def header(depth: int, subject_slugs: list[tuple[str, str]], current: str = "") -> str:
    prefix = rel(depth)
    links = [("Home", f"{prefix}index.html", "")]
    for slug, title in subject_slugs:
        links.append((title, f"{prefix}subjects/{slug}/index.html", slug))
    links.append(("All Subjects", f"{prefix}subjects/index.html", "all"))
    nav_desktop = "".join(
        f'<a href="{esc(href)}"' + (' aria-current="page"' if key == current else "") + f'>{esc(label)}</a>'
        for label, href, key in links
    )
    return f"""
  <header class="site-header">
    <div class="shell header-inner">
      <a class="brand" href="{prefix}index.html">
        <span class="brand-mark" aria-hidden="true">e</span>
        <span><span class="brand-name">EkGuru Learning</span><span class="brand-caption">By PRAKASH</span></span>
      </a>
      <nav class="site-nav desktop-nav" aria-label="Main navigation">{nav_desktop}</nav>
      <details class="site-menu">
        <summary class="site-menu-toggle">Menu</summary>
        <nav class="site-nav" aria-label="Main navigation (mobile)">{nav_desktop}</nav>
      </details>
    </div>
  </header>"""


def crumbs(parts: list[tuple[str, str]]) -> str:
    """parts = [(label, href)] — the last one is the current page (rendered as text)."""
    pieces = []
    for index, (label, href) in enumerate(parts):
        if index:
            pieces.append('<span class="crumb-sep" aria-hidden="true">›</span>')
        last = index == len(parts) - 1
        if last or not href:
            pieces.append(f'<span class="crumb-current">{esc(label)}</span>')
        else:
            pieces.append(f'<a href="{esc(href)}">{esc(label)}</a>')
    back = ""
    if len(parts) > 1 and parts[-2][1]:
        back = f'<a class="crumb-up" href="{esc(parts[-2][1])}">↑ {esc(parts[-2][0])} par jao</a>'
    joined = "".join(pieces)
    return f'<nav class="crumbs" aria-label="Breadcrumb">{joined}{back}</nav>'




def file_row(item: dict, depth: int, from_page: str = "") -> str:
    prefix = rel(depth)
    href = url_for(href_from(from_page, item["repo_path"])) if from_page else prefix + url_for(item["repo_path"])
    viewer_base = href_from(from_page, "subjects/reader/index.html") if from_page else prefix + "subjects/reader/index.html"
    viewer_href = viewer_base + "?" + urllib.parse.urlencode({"file": item["repo_path"]})
    is_picture = item["file_type"] in {"PNG", "JPG", "JPEG", "WEBP", "SVG"}
    thumb = ""
    if is_picture and item.get("thumb_url"):
        thumb_src = url_for(href_from(from_page, item["thumb_url"])) if from_page else prefix + url_for(item["thumb_url"])
        size = image_size(item["thumb_url"])
        size_attrs = f' width="{size[0]}" height="{size[1]}"' if size else ""
        thumb = (f'<a class="file-thumb" href="{esc(viewer_href)}">'
                 f'<img src="{esc(thumb_src)}" alt="{esc(item["alt_en"] or item["title_en"])}"{size_attrs} '
                 f'loading="lazy" decoding="async"><span class="file-thumb-open">Poora dekho</span></a>')
    description = ""
    if is_picture and item.get("description_en"):
        description = f'<p class="file-description" lang="en">{esc(item["description_en"])}</p>'
        if item.get("description_hi"):
            description += f'<p class="file-description" lang="hi">{esc(item["description_hi"])}</p>'
    chips = []
    if item.get("topic_id"):
        chips.append(f'<span class="chip neutral">{esc(item["topic_id"])}</span>')
    chips.append(f'<span class="chip neutral">{esc(item["file_type"])}</span>')
    chips.append(f'<span class="chip neutral">{esc(human_size(item["bytes"]))}</span>')
    open_label = "Map kholo" if is_picture else "PDF kholo"
    return f"""        <li class="material-item{' is-image' if is_picture else ''}">
          {thumb}
          <div class="material-main">
            <h4>{esc(item['title_en'])}</h4>
            <p class="muted small" style="margin:0">{esc(item['title_hi'])}</p>
            {f'<p class="small" style="margin:0.2rem 0 0">{esc(item["note_en"])}</p>' if item.get('note_en') else ''}
            {description}
            <div class="material-meta">{''.join(chips)}</div>
          </div>
          <div class="material-actions">
            <a class="button secondary small" href="{esc(viewer_href)}">{open_label}</a>
            <a class="button ghost small" href="{esc(href)}" target="_blank" rel="noopener noreferrer">Original ↗</a>
            <a class="button primary small" href="{esc(href)}" download>Download</a>
          </div>
        </li>"""


# Links jo humne khud check kiye aur kaam nahi karte (HTTP error / error page).
# Key = URL ka shuru ka hissa. Har entry ke saath check ki tareekh likhi hai.
LINK_CHECKS = {
    "https://www.rrbcdg.gov.in/uploads/": (
        "2026-10-15",
        "This PDF is linked from the RRB CDG site, which returned a server error when checked. Try the official homepage link below.",
        "यह PDF RRB CDG की साइट से जुड़ा है, जाँच के समय साइट ने server error दिया। नीचे दी गई आधिकारिक homepage से खोजें।",
    ),
    "https://www.rrbcdg.gov.in/": (
        "2026-10-15",
        "The RRB CDG homepage returned a server error when checked. Try again later or use the backup search link.",
        "RRB CDG की homepage जाँच के समय server error दे रही थी। बाद में फिर कोशिश करें या backup search link use करें।",
    ),
    "https://rpsc.rajasthan.gov.in/quespapers": (
        "2026-10-15",
        "This RPSC question-paper page shows an error page when checked. Use the RPSC homepage or the backup search below.",
        "यह RPSC प्रश्न-पत्र पेज जाँच के समय error पेज दिखा रहा था। RPSC homepage या नीचे की backup search use करें।",
    ),
}


def link_check_note(url: str) -> tuple[str, str] | None:
    for prefix, (_date, note_en, note_hi) in LINK_CHECKS.items():
        if url.startswith(prefix):
            return note_en, note_hi
    return None


def official_backup_block(exam: dict) -> str:
    """Har exam ke official domains ke liye homepage aur site-search link — ek link toote to dusra kaam aaye."""
    urls = [s["url"] for s in exam.get("sources", [])]
    urls += [link["url"] for year in exam["years"] for link in year["links"]]
    hosts: list[str] = []
    for url in urls:
        parts = urllib.parse.urlsplit(url)
        if parts.scheme != "https" or not parts.netloc or parts.netloc.endswith("drive.google.com"):
            continue
        if parts.netloc not in hosts:
            hosts.append(parts.netloc)
    if not hosts:
        return ""
    rows = []
    for host in hosts[:4]:
        home = f"https://{host}/"
        query = urllib.parse.quote_plus(f"site:{host} {exam['title_en']} previous year question paper answer key")
        search = f"https://www.google.com/search?q={query}"
        rows.append(f"""<li class="pyq-link-item">
          <a class="pyq-source-link" href="{esc(home)}" target="_blank" rel="noopener noreferrer">
            <span class="pyq-source-title">{esc(host)} — official homepage <span aria-hidden="true">↗</span></span>
            <span class="pyq-source-title-hi" lang="hi">{esc(host)} — आधिकारिक homepage</span>
            <span class="pyq-source-kind">Backup · homepage</span>
          </a>
        </li>""")
        rows.append(f"""<li class="pyq-link-item">
          <a class="pyq-source-link" href="{esc(search)}" target="_blank" rel="noopener noreferrer">
            <span class="pyq-source-title">Search {esc(host)} for this exam <span aria-hidden="true">↗</span></span>
            <span class="pyq-source-title-hi" lang="hi">इस परीक्षा के लिए {esc(host)} पर खोजें</span>
            <span class="pyq-source-kind">Backup · site search</span>
          </a>
        </li>""")
    return "\n".join(rows)


def paper_link_list(links: list[dict], from_page: str) -> str:
    """Render clearly labelled official, login-only and third-party paper links."""
    rows = []
    for link in links:
        target = link["url"]
        external = urllib.parse.urlsplit(target).scheme == "https"
        if not external and target.lower().endswith(".pdf"):
            href = href_from(from_page, "subjects/reader/index.html") + "?" + urllib.parse.urlencode({"file": target})
        else:
            href = target if external else href_from(from_page, target)
        safety = ' target="_blank" rel="noopener noreferrer"' if external else ""
        marker = "↗" if external else "→"
        kind = PAPER_KINDS[link["kind"]]
        note = link_check_note(target)
        warning = (f'<span class="pyq-link-warning"><span aria-hidden="true">⚠</span> {esc(note[0])}'
                   f'<span class="pyq-link-warning-hi" lang="hi">{esc(note[1])}</span></span>') if note else ""
        rows.append(f"""<li class="pyq-link-item">
          <a class="pyq-source-link" href="{esc(href)}"{safety}>
            <span class="pyq-source-title">{esc(link['label_en'])} <span aria-hidden="true">{marker}</span></span>
            <span class="pyq-source-title-hi" lang="hi">{esc(link['label_hi'])}</span>
            <span class="pyq-source-kind">{esc(kind)}</span>
            {warning}
          </a>
        </li>""")
    return "\n".join(rows)


def available_year_chips(years: list[dict]) -> str:
    chips = []
    for year in years:
        label = str(year["year"])
        target_id = paper_year_id(label)
        chips.append(f'<a class="chip year-chip ready" href="#{esc(target_id)}">{esc(label)}</a>')
    return "".join(chips)


def year_chips(subject: dict, node: dict, from_page: str, current: str = "") -> str:
    """Only show year folders that actually contain a paper; no grey placeholder years."""
    children = [
        child for child in node["folders"]
        if child["file_count"] and child["path"].split("/")[-1].isdigit()
    ]
    children.sort(key=lambda child: int(child["path"].split("/")[-1]), reverse=True)
    chips = []
    for child in children:
        key = child["path"].split("/")[-1]
        target = f"subjects/{subject['slug']}/{child['path']}/index.html"
        href = esc(href_from(from_page, target))
        state = ' aria-current="page"' if key == current else ""
        chips.append(f'<a class="chip year-chip ready" href="{href}"{state}>{key}<span class="year-count">{child["file_count"]}</span></a>')
    return "".join(chips)


def year_section(subject: dict, node: dict, from_page: str) -> str:
    """Local PDF year folders only; external verified years live in the exam directory."""
    cfg = subject["year_folders"]
    ready = [child for child in node["folders"] if child["file_count"] and child["path"].split("/")[-1].isdigit()]
    if not ready:
        return ""
    return f"""
    <section class="section">
      <div class="section-head">
        <h2>🗓️ {esc(cfg.get('title_en', 'Available years'))}</h2>
        <span class="muted small">{len(ready)} available year(s)</span>
      </div>
      <p class="section-note">{esc(cfg.get('note_en', 'Only years with a published paper are shown.'))}</p>
      <div class="year-grid">
{year_chips(subject, node, from_page)}
      </div>
    </section>"""


def folder_tile(node: dict, href: str, compact: bool = False) -> str:
    meta = []
    if node["file_count"]:
        meta.append(plural(node["file_count"], "file", "files"))
    if node["folder_count"]:
        meta.append(plural(node["folder_count"], "subfolder", "subfolders"))
    if node["file_types"]:
        meta.append(" / ".join(node["file_types"]))
    if not meta:
        meta.append("material jald aa raha hai")
    return f"""          <a class="folder-card{' compact' if compact else ''}{' is-empty' if node['empty'] else ''}" href="{esc(href)}">
            <span class="folder-icon" aria-hidden="true">{esc(node['icon'])}</span>
            <span class="folder-body">
              <strong>{esc(node['title_en'])}</strong>
              <span class="folder-hi">{esc(node['title_hi'])}</span>
              {'' if compact or not node['note_en'] else f'<span class="folder-note">{esc(node["note_en"])}</span>'}
              <span class="folder-meta">{esc(' · '.join(meta))}</span>
            </span>
            {'' if compact else f'<span class="folder-open">{"Jald aa raha hai" if node["empty"] else "Kholo →"}</span>'}
          </a>"""


def footer(depth: int, subjects: list[dict], quick: list[tuple[str, str]]) -> str:
    prefix = rel(depth)
    total_files = sum(subject["file_count"] for subject in subjects)
    cn = next((subject for subject in subjects if subject["id"] == "computer-network"), None)
    stats = (f"{plural(len(subjects), 'subject', 'subjects')} · "
             f"{plural(total_files, 'file', 'files')}"
             + (f" · {number(cn['test']['question_count'])} online questions" if cn and cn.get("test") else ""))
    subject_links = "".join(
        f'        <p><a href="{prefix}subjects/{esc(subject["slug"])}/index.html">{esc(subject["title_en"])}'
        f'{" (" + str(subject["file_count"]) + ")" if subject["file_count"] else ""}</a></p>\n'
        for subject in subjects
    )
    quick_links = "".join(f'        <p><a href="{prefix}{esc(href)}">{esc(label)}</a></p>\n' for label, href in quick)
    return f"""  <footer class="site-footer">
    <div class="shell footer-grid">
      <div>
        <h3>EkGuru Learning</h3>
        <p>{esc(BRAND_TAGLINE)}</p>
        <p class="footer-stats">{esc(stats)}</p>
      </div>
      <div>
        <h3>Subjects</h3>
{subject_links}      </div>
      <div>
        <h3>Quick links</h3>
{quick_links}      </div>
    </div>
    <div class="shell footer-bottom">
      <span>© EkGuru Learning · By PRAKASH</span>
      <span class="footer-note">Saara material free hai — print karein, share karein.</span>
    </div>
  </footer>
</body>
</html>
"""


def breadcrumb_parts(subject: dict, node: dict, from_page: str) -> list[tuple[str, str]]:
    """Home › All Subjects › subject › folder › … for the page being written."""
    parts = [
        ("Home", href_from(from_page, "index.html")),
        ("All Subjects", href_from(from_page, "subjects/index.html")),
        (subject["title_en"], href_from(from_page, f"subjects/{subject['slug']}/index.html")),
    ]
    walked = ""
    pieces = node["path"].split("/") if node["path"] else []
    for piece in pieces:
        walked = f"{walked}/{piece}" if walked else piece
        target = next((item for item in walk_nodes(subject["tree"]) if item["path"] == walked), None)
        label = target["title_en"] if target else piece
        parts.append((label, href_from(from_page, f"subjects/{subject['slug']}/{walked}/index.html")))
    if parts:
        parts[-1] = (parts[-1][0], "")
    return parts


def walk_nodes(node: dict):
    yield node
    for child in node["folders"]:
        yield from walk_nodes(child)


# --------------------------------------------------------------------- builder
class Builder:
    def __init__(self, site: dict, subjects_doc: dict, paper_catalog: dict):
        self.site = site
        self.subjects = site["subjects"]
        self.nav = [(subject["slug"], subject["title_en"]) for subject in self.subjects]
        self.brand = subjects_doc.get("brand", {})
        self.paper_catalog = paper_catalog
        self.paper_groups = paper_catalog.get("groups", [])
        self.paper_exams = [exam for group in self.paper_groups for exam in group.get("exams", [])]
        self.written: list[tuple[pathlib.Path, str]] = []

    # ------------------------------------------------------------- utilities
    def add(self, rel_path: str, content: str) -> None:
        # keep the generated files hand-readable: no trailing blanks, one final newline
        tidy = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
        self.written.append((ROOT / rel_path, tidy))

    def folder_page_path(self, subject: dict, node: dict) -> str:
        slug = subject["slug"]
        if not node["path"]:
            return f"subjects/{slug}/index.html"
        return f"subjects/{slug}/{node['path']}/index.html"

    def folder_href_from(self, subject: dict, node: dict, depth: int, from_page: str = "") -> str:
        """Link from a page to the generated page of `node` (folder-page links stay short)."""
        slug = subject["slug"]
        target = f"subjects/{slug}/index.html" if not node["path"] else f"subjects/{slug}/{node['path']}/index.html"
        if from_page:
            return href_from(from_page, target)
        return rel(depth) + target

    # ------------------------------------------------------ previous-year pages
    @staticmethod
    def paper_exam_path(exam: dict) -> str:
        return f"subjects/previous-year-papers/exams/{exam['id']}/index.html"

    def paper_catalog_block(self, from_page: str) -> str:
        groups = []
        for group in self.paper_groups:
            cards = []
            for exam in group.get("exams", []):
                exam_page = self.paper_exam_path(exam)
                detail_href = esc(href_from(from_page, exam_page))
                chips = "".join(
                    f'<a class="chip year-chip ready" href="{detail_href}#{esc(paper_year_id(str(year["year"])))}">{esc(str(year["year"]))}</a>'
                    for year in exam["years"]
                )
                cards.append(f"""        <article class="card pyq-exam-card">
          <div class="pyq-exam-card-head">
            <div><h3>{esc(exam['title_en'])}</h3><p class="pyq-title-hi" lang="hi">{esc(exam['title_hi'])}</p></div>
            <span class="chip neutral">{len(exam['years'])} year/session records</span>
          </div>
          <p class="pyq-summary">{esc(exam['summary_en'])}</p>
          <p class="pyq-summary pyq-summary-hi" lang="hi">{esc(exam['summary_hi'])}</p>
          <nav class="pyq-year-chips" aria-label="{esc(exam['title_en'])} years">{chips}</nav>
          <a class="button primary small" href="{detail_href}">Open year-wise sources <span aria-hidden="true">→</span></a>
        </article>""")
            groups.append(f"""      <section class="pyq-group" aria-labelledby="pyq-group-{esc(group['id'])}">
        <div class="section-head"><h3 id="pyq-group-{esc(group['id'])}">{esc(group['title_en'])}</h3><span class="muted small" lang="hi">{esc(group['title_hi'])}</span></div>
        <div class="pyq-card-grid">
{chr(10).join(cards)}
        </div>
      </section>""")
        return f"""    <section class="section pyq-catalog" id="verified-paper-sources">
      <div class="section-head"><h2>Exam-wise previous-year sources</h2><span class="eyebrow">{len(self.paper_exams)} exams</span></div>
      <p class="section-note">{esc(self.paper_catalog['intro_en'])}</p>
      <p class="section-note" lang="hi">{esc(self.paper_catalog['intro_hi'])}</p>
{chr(10).join(groups)}
    </section>"""

    def paper_exam_page(self, group: dict, exam: dict) -> None:
        rel_path = self.paper_exam_path(exam)
        depth = len(pathlib.PurePosixPath(rel_path).parts) - 1
        detail_href = href_from(rel_path, "subjects/previous-year-papers/index.html")
        group_title = group["title_en"]
        year_cards = []
        for index, year in enumerate(exam["years"]):
            label = str(year["year"])
            year_id = paper_year_id(label)
            # Mobile par sab saal ek saath khule to page bahut lamba ho jata hai:
            # har saal collapsible hai, sirf sabse naya saal (pehla) shuru me khula rehta hai.
            open_attr = " open" if index == 0 else ""
            year_cards.append(f"""      <details class="card pyq-year-card" id="{esc(year_id)}"{open_attr}>
        <summary class="pyq-year-summary">
          <span class="chip green">{esc(label)}</span>
          <span class="pyq-year-summary-text">
            <strong>{esc(year['title_en'])}</strong>
            <span class="pyq-title-hi" lang="hi">{esc(year['title_hi'])}</span>
          </span>
          <span class="pyq-year-toggle" aria-hidden="true">▾</span>
        </summary>
        <div class="pyq-year-body">
        <p class="pyq-year-note">{esc(year.get('note_en', ''))}</p>
        <p class="pyq-year-note pyq-year-note-hi" lang="hi">{esc(year.get('note_hi', ''))}</p>
        <ul class="pyq-source-list">
{paper_link_list(year['links'], rel_path)}
        </ul>
        </div>
      </details>""")
        archive_links = paper_link_list(exam.get("sources", []), rel_path) or (
            '<li class="muted small">No separate archive link is listed.</li>'
        )
        year_nav = available_year_chips(exam["years"])
        title = f"{exam['title_en']} — Previous Year Papers — EkGuru Learning"
        description = (f"Year-wise previous-year paper sources for {exam['title_en']}. "
                       "Official papers, answer keys, candidate-login and third-party practice are labelled separately.")
        body = f"""{head(title, description, depth)}
{header(depth, self.nav, "previous-year-papers")}
  <main id="main" class="shell">
    <section class="section">
      {crumbs([('Home', href_from(rel_path, 'index.html')), ('Previous Year Papers', detail_href), (exam['title_en'], '')])}
      <span class="eyebrow">{esc(group_title)}</span>
      <h1>{esc(exam['title_en'])}</h1>
      <p class="pyq-title-hi" lang="hi">{esc(exam['title_hi'])}</p>
      <p class="section-note">{esc(exam['summary_en'])}</p>
      <p class="section-note" lang="hi">{esc(exam['summary_hi'])}</p>
      <div class="year-grid pyq-detail-year-nav" aria-label="Available exam years">{year_nav}</div>
    </section>
    <section class="section pyq-year-list">
      <div class="section-head"><h2>Year-wise papers and source notes</h2><a href="{esc(detail_href)}#source-archives">Exam archive links ↓</a></div>
      <div class="pyq-year-grid">
{chr(10).join(year_cards)}
      </div>
    </section>
    <section class="section" id="source-archives">
      <div class="section-head"><h2>Official archives and exam information</h2></div>
      <div class="pyq-backup">
        <h3>Agar upar ka link na khule to</h3>
        <p class="section-note">Upar ke direct link kabhi server error ya login page dikhate hain. Neeche official homepage aur site-search se wahi paper dhoondhein.</p>
        <ul class="pyq-source-list">
{official_backup_block(exam)}
        </ul>
      </div>
      <p class="section-note">Use the archive to confirm the notification, paper set, shift, discipline and answer-key status. A response sheet may require candidate login and may only remain available temporarily.</p>
      <ul class="pyq-source-list pyq-archive-list">
{archive_links}
      </ul>
    </section>
  </main>

{footer(depth, self.subjects, [('Previous year papers', 'subjects/previous-year-papers/index.html'), ('All subjects', 'subjects/index.html')])}"""
        self.add(rel_path, body)

    def paper_exam_pages(self) -> None:
        for group in self.paper_groups:
            for exam in group.get("exams", []):
                self.paper_exam_page(group, exam)

    def map_pdf_preview(self, from_page: str) -> str:
        pdf = "content/rajasthan-geography/map/rajasthan/Rajasthan-Border-Districts-A4-Portrait-Print.pdf"
        pdf_path = href_from(from_page, pdf)
        pdf_href = esc(url_for(pdf_path))
        preview = esc(url_for(href_from(from_page, "assets/img/rajasthan-border-atlas-preview.webp")))
        viewer = esc(href_from(from_page, "subjects/reader/index.html") + "?" + urllib.parse.urlencode({"file": "content/rajasthan-geography/map/rajasthan/Rajasthan-Border-Districts-A4-Portrait.png"}))
        a3_pdf = esc(url_for(href_from(from_page, "content/rajasthan-geography/map/rajasthan/Rajasthan-Border-District-Atlas-A3-Print.pdf")))
        return f"""    <section class="section map-pdf-preview" id="map-pdf-preview">
      <div class="section-head"><h2>Rajasthan map — mobile preview</h2><span class="chip neutral">A4 · PDF</span></div>
      <p class="section-note">Map seedha dekhein — mobile par PDF plugin ki zaroorat nahi. Map kholo se zoom aur swipe karke padhein.</p>
      <a class="map-frame" href="{viewer}"><img src="{preview}" alt="Rajasthan district and border atlas — mobile map preview" width="1200" height="848" decoding="async"></a>
      <p class="pdf-mobile-note">Print ke liye PDF; phone par padhne ke liye zoomable map. Badi file ke liye stable internet rakhein.</p>
      <div class="button-row">
        <a class="button primary" href="{viewer}">Map kholo · Zoom</a>
        <a class="button secondary" href="{pdf_href}" target="_blank" rel="noopener noreferrer">Open A4 PDF ↗</a>
        <a class="button secondary" href="{pdf_href}" download>Download A4 PDF</a>
        <a class="button ghost" href="{a3_pdf}" download>Download print-ready A3 PDF</a>
      </div>
    </section>"""

    # -------------------------------------------------------------- subject
    def subject_page(self, subject: dict) -> None:
        slug = subject["slug"]
        is_pyq_subject = slug == "previous-year-papers"
        prefix = f"subjects/{slug}/"
        extras = SUBJECT_EXTRAS.get(slug, {})
        title = extras.get("title") or f'{subject["title_en"]} — EkGuru Learning'
        description = extras.get("description") or (
            f'{subject["title_en"]} ({subject["title_hi"]}) — {subject["tagline_en"]} '
            f'{plural(subject["folder_count"], "folder", "folders")}, '
            f'{plural(subject["file_count"], "file", "files")}.')
        quick = [("All subjects", "subjects/index.html"),
                 ("Previous year papers", "subjects/previous-year-papers/index.html")]
        subject_actions = ""
        subject_page_rel = f"subjects/{slug}/index.html"
        has_material = (ROOT / f"subjects/{slug}/material/index.html").is_file()
        has_test = (ROOT / f"subjects/{slug}/test/index.html").is_file()
        if has_material:
            subject_actions += f'<a class="button primary" href="{href_from(subject_page_rel, f"subjects/{slug}/material/index.html")}">Study Material</a>\n        '
            quick.insert(0, ("Study material", f"subjects/{slug}/material/index.html"))
        if has_test:
            subject_actions += f'<a class="button primary" href="{href_from(subject_page_rel, f"subjects/{slug}/test/index.html")}">Online Test</a>\n        '
            quick.insert(0, ("Online test", f"subjects/{slug}/test/index.html"))
        if is_pyq_subject:
            subject_actions += '<a class="button primary" href="#verified-paper-sources">Browse exam sources →</a>\n        '
        subject_actions += (f'<a class="button secondary" href="{href_from(subject_page_rel, "subjects/index.html")}">All subjects</a>\n        '
                            f'<a class="button ghost" href="{href_from(subject_page_rel, "index.html")}">Home</a>')
        tile_nodes = [
            node for node in subject["tree"]["folders"]
            if not is_pyq_subject or node["file_count"]
        ]
        tiles = "".join(
            folder_tile(node, self.folder_href_from(subject, node, 2, subject_page_rel))
            for node in tile_nodes
        )
        pyq_catalog = self.paper_catalog_block(subject_page_rel) if is_pyq_subject else ""
        topic_block = ""
        if subject["topics"]:
            cards = []
            for topic in subject["topics"]:
                theory = (topic["material"].get("theory") or [None])[0]
                chips = "".join(
                    f'<span class="chip neutral">{esc(section["short"])} · {section["count"]}</span>'
                    for section in topic["sections"][:3]
                )
                extra = (f'<span class="chip neutral">+{len(topic["sections"]) - 3} more</span>'
                         if len(topic["sections"]) > 3 else "")
                cards.append(f"""          <article class="card topic-card">
            <div class="topic-head">
              <span class="topic-badge">{esc(topic['id'])}</span>
              <div><h3 style="margin:0">{esc(topic['title_en'])}</h3>
              <p class="muted small" style="margin:0">{esc(topic['title_hi'])}</p></div>
            </div>
            <div class="topic-meta">
              <span class="chip green">{number(topic['question_count'])} online questions</span>
              <span class="chip neutral">{topic['section_count']} sections</span>
            </div>
            <div class="topic-meta">{chips}{extra}</div>
            <div class="topic-actions">
              <a class="button primary small" href="test/index.html?topic={esc(topic['id'])}">Test do</a>
              {f'<a class="button secondary small" href="{esc(url_for(href_from(subject_page_rel, theory["repo_path"])))}" download>Theory PDF</a>' if theory else ''}
            </div>
          </article>""")
            topic_block = f"""
    <section class="section">
      <div class="section-head">
        <h2>Topic-wise test</h2>
        <a href="test/index.html">Full mixed test →</a>
      </div>
      <p class="section-note">Har topic ka apna test — section bhi chun sakte ho.</p>
      <div class="topic-grid">
{chr(10).join(cards)}
      </div>
    </section>"""

        hero = ""
        if extras.get("hero_image"):
            primary_label, primary_target = extras["hero_primary"]
            secondary_label, secondary_target = extras["hero_secondary"]
            pdf_action = ""
            if extras.get("hero_pdf"):
                pdf_label, pdf_target = extras["hero_pdf"]
                pdf_action = f'<a class="button ghost" href="{esc(href_from(subject_page_rel, pdf_target))}">{esc(pdf_label)}</a>'
            hero = f"""
  <section class="hero">
    <div class="shell hero-inner has-media">
      <div>
        <span class="eyebrow">{esc(subject['title_en'])}</span>
        <h1>{esc(subject['title_en'])}</h1>
        <p class="hero-lead">{extras['hero_lead']}</p>
        <div class="hero-actions">
          <a class="button primary" href="{esc(href_from(subject_page_rel, primary_target))}">{esc(primary_label)}</a>
          <a class="button secondary" href="{esc(href_from(subject_page_rel, secondary_target))}" download>{esc(secondary_label)}</a>
          {pdf_action}
        </div>
      </div>
      <div class="map-frame">
        <a href="{esc(href_from(subject_page_rel, primary_target))}">
          <img src="{esc(href_from(subject_page_rel, extras['hero_image']))}" width="{extras['hero_image_w']}" height="{extras['hero_image_h']}" decoding="async" alt="{esc(extras['hero_alt'])}">
        </a>
        <p class="map-caption">{esc(extras['hero_caption'])}</p>
      </div>
    </div>
  </section>"""
        intro = "" if hero else f"""
      <span class="eyebrow">Subject</span>
      <h1>{esc(subject['title_en'])}</h1>
      <p class="section-note">{esc(subject['intro_en'] or subject['tagline_en'])}</p>"""

        body = f"""{head(title, description, 2, keywords=extras.get('keywords', ''), structured_data=extras.get('structured_data', ''))}
{header(2, self.nav, slug)}{hero}
  <main id="main" class="shell">
    <section class="section">
      {crumbs([('Home', href_from(subject_page_rel, 'index.html')), ('All Subjects', href_from(subject_page_rel, 'subjects/index.html')), (subject["title_en"], '')])}{intro}
      <div class="button-row">
{subject_actions}
      </div>
    </section>
    <section class="section">
      <div class="section-head">
        <h2>{'📁 EkGuru-hosted papers' if is_pyq_subject else '📁 Folders'}</h2>
        <span class="muted small">{plural(subject['file_count'], 'file', 'files')}</span>
      </div>
      <p class="section-note">{'Files stored on EkGuru are listed separately from the exam-wise external sources below. Check each file label to distinguish a question paper from an answer key.' if is_pyq_subject else 'Folder kholo → files dekho ya download karo.'}</p>
      <div class="folder-grid">
{tiles if tiles else '<p class="empty-state">No EkGuru-hosted paper files are available here yet. See the verified source directory below.</p>'}
      </div>
    </section>{pyq_catalog}{topic_block}
  </main>

{footer(2, self.subjects, quick)}"""
        self.add(f"{prefix}index.html", body)

        # one real page per folder
        for node in walk_nodes(subject["tree"]):
            if not node["path"]:
                continue
            self.folder_page(subject, node)

    def folder_page(self, subject: dict, node: dict) -> None:
        rel_path = self.folder_page_path(subject, node)
        depth = len(pathlib.PurePosixPath(rel_path).parts) - 1
        pieces = breadcrumb_parts(subject, node, rel_path)
        title = f'{node["title_en"]} — {subject["title_en"]} — EkGuru Learning'
        description = (f'{node["title_en"]} ({node["title_hi"]}) — {subject["title_en"]}: '
                       f'{plural(node["file_count"], "file", "files")}.')
        sub_tiles = "".join(
            folder_tile(child, self.folder_href_from(subject, child, depth, rel_path))
            for child in node["folders"]
        )
        # exam folder (jaise RPSC / DSSSB): folders ki jagah saal-wise chips
        years = subject.get("year_folders") or {}
        is_exam_folder = bool(years) and "/" not in node["path"] and any(
            child["file_count"] and child["path"].split("/")[-1].isdigit()
            for child in node["folders"]
        )
        year_block = year_section(subject, node, rel_path) if is_exam_folder else ""
        map_pdf = (self.map_pdf_preview(rel_path)
                   if subject["slug"] == "rajasthan-geography" and node["path"] == "map/rajasthan"
                   else "")
        # year folder (jaise RPSC > 2024): neeche dusre saal par jane ke chips
        year_switch = ""
        if years and "/" in node["path"]:
            parent_path = node["path"].rsplit("/", 1)[0]
            parent = next((item for item in walk_nodes(subject["tree"]) if item["path"] == parent_path), None)
            if parent is not None and "/" not in parent["path"]:
                year_switch = f"""
    <section class="section">
      <div class="section-head"><h2>🗓️ {esc(parent['title_en'])} ke doosre saal</h2></div>
      <div class="year-grid">
{year_chips(subject, parent, rel_path, current=node['path'].split('/')[-1])}
      </div>
    </section>"
                """.strip()
        files = "".join(file_row(item, depth, rel_path) for item in node["files"])
        file_block = (f'        <ul class="material-list">\n{files}\n        </ul>' if node["files"]
                      else '        <p class="empty-state">Is folder ka material jald aa raha hai. '
                           'Tab tak doosre subjects ka material dekh lo.</p>')
        quick = [("All subjects", "subjects/index.html"), ("Home", "index.html")]
        body = f"""{head(title, description, depth)}
{header(depth, self.nav, subject["slug"])}
  <main id="main" class="shell">
    <section class="section">
      {crumbs(pieces)}
      <h1>{esc(node['icon'])} {esc(node['title_en'])}</h1>
      <p class="muted">{esc(node['title_hi'])}{f' — {esc(node["note_en"])}' if node['note_en'] else ''}</p>
      <p class="section-note">{esc(subject['title_en'])} · {plural(node['file_count'], 'file', 'files')}
        {f" · {' / '.join(node['file_types'])}" if node['file_types'] else ''}</p>
    </section>{map_pdf}{year_block}
    {f'''<section class="section">
      <div class="section-head"><h2>Subfolders</h2></div>
      <div class="folder-grid">
{sub_tiles}
      </div>
    </section>''' if sub_tiles and not is_exam_folder else ''}
    <section class="section">
      <div class="section-head"><h2>Files</h2><span class="muted small">{plural(len(node['files']), 'file', 'files')}</span></div>
{file_block}
    </section>{year_switch}
  </main>

{footer(depth, self.subjects, quick)}"""
        self.add(rel_path, body)

    # ---------------------------------------------------------------- home
    def home(self) -> None:
        cards = []
        for subject in self.subjects:
            stats = [plural(subject["folder_count"], "folder", "folders"),
                     plural(subject["file_count"], "file", "files")]
            if subject.get("test"):
                stats.append(f'{number(subject["test"]["question_count"])} online questions')
            tiles = "".join(
                folder_tile(node, f'subjects/{subject["slug"]}/{node["path"]}/index.html', compact=True)
                for node in subject["tree"]["folders"][:6]
            )
            actions = f'<a class="button primary" href="subjects/{esc(subject["slug"])}/index.html">Folder kholo</a>'
            if subject.get("test_route"):
                actions += (f'<a class="button secondary" '
                            f'href="{esc(subject["test_route"])}">Test do</a>')
            cards.append(f"""        <article class="card subject-card">
          <div class="card-title-row">
            <h3 style="margin:0">{esc(subject['title_en'])}</h3>
            <span class="chip neutral">{esc(subject['title_hi'])}</span>
          </div>
          <p class="muted small" style="margin:0.3rem 0 0.7rem">{esc(' · '.join(stats))}</p>
          <p class="small" style="margin:0 0 0.7rem">{esc(subject['tagline_en'])}</p>
          <div class="folder-grid">
{tiles}
          </div>
          <div class="button-row" style="margin-top:0.9rem">{actions}</div>
        </article>""")

        total_files = sum(subject["file_count"] for subject in self.subjects)
        cn = next((subject for subject in self.subjects if subject["id"] == "computer-network"), None)
        questions = number(cn["test"]["question_count"]) if cn and cn.get("test") else "0"
        title = "EkGuru Learning — study material, previous year papers aur online test"
        description = ("EkGuru Learning by PRAKASH — Computer Network, Reasoning, Rajasthan Geography maps "
                       "aur Previous Year Papers (RPSC, DSSSB, SSC, NET). Folder-wise PDF aur online test, free.")
        body = f"""{head(title, description, 0)}
{header(0, self.nav)}
  <section class="hero">
    <div class="shell hero-inner">
      <div>
        <span class="eyebrow">EkGuru Learning · By PRAKASH</span>
        <h1>Padho, practice karo, <em>test do.</em></h1>
        <p class="hero-lead">Har subject ke folders — theory, practice, answers aur tests. Previous year papers
          exam-wise aur saal-wise, aur Computer Network ka online test turant.</p>
        <div class="hero-actions">
          <a class="button primary" href="subjects/computer-network/index.html">Computer Network</a>
          <a class="button secondary" href="subjects/previous-year-papers/index.html">Previous Year Papers</a>
          <a class="button secondary" href="subjects/rajasthan-geography/index.html">Rajasthan Map</a>
          <a class="button ghost" href="subjects/index.html">All subjects</a>
        </div>
        <div class="hero-stats">
          <span class="hero-stat"><strong>{len(self.subjects)}</strong><span>Subjects</span></span>
          <span class="hero-stat"><strong>{total_files}</strong><span>Files</span></span>
          <span class="hero-stat"><strong>{questions}</strong><span>Online questions</span></span>
        </div>
      </div>
    </div>
  </section>

  <main id="main" class="shell">
    <section class="section">
      <div class="section-head">
        <h2>Subjects</h2>
        <a href="subjects/index.html">All subjects →</a>
      </div>
      <p class="section-note">Har subject ke andar folder — folder ke andar files.</p>
      <div class="subject-grid">
{chr(10).join(cards)}
      </div>
    </section>
  </main>

{footer(0, self.subjects, [('All subjects', 'subjects/index.html'), ('Computer Network', 'subjects/computer-network/index.html'), ('Online test', 'subjects/computer-network/test/index.html')])}"""
        self.add("index.html", body)

    # ------------------------------------------------------------ explorer
    def subjects_index(self) -> None:
        cards = []
        for subject in self.subjects:
            stats = [plural(subject["folder_count"], "folder", "folders"),
                     plural(subject["file_count"], "file", "files")]
            if subject.get("test"):
                stats.append(f'{number(subject["test"]["question_count"])} online questions')
            names = " · ".join(node["title_en"] for node in subject["tree"]["folders"][:8])
            cards.append(f"""        <article class="card subject-card">
          <span class="eyebrow">{esc(subject['title_hi'])}</span>
          <h3 style="margin:0">{esc(subject['title_en'])}</h3>
          <p class="muted small" style="margin:0.3rem 0 0.6rem">{esc(' · '.join(stats))}</p>
          <p class="small muted" style="margin:0 0 0.8rem">{esc(names)}</p>
          <div class="button-row">
            <a class="button primary" href="{esc(subject['slug'])}/index.html">Kholo</a>
            {f'<a class="button secondary" href="{rel(1)}{esc(subject["test_route"])}">Test do</a>' if subject.get('test_route') else ''}
          </div>
        </article>""")
        body = f"""{head("All subjects — EkGuru Learning", "EkGuru Learning ke saare subjects — Computer Network, Reasoning, Rajasthan Geography aur Previous Year Papers.", 1)}
{header(1, self.nav, "all")}
  <main id="main" class="shell">
    <section class="section">
      {crumbs([('Home', '../index.html'), ('All Subjects', '')])}
      <span class="eyebrow">Subjects</span>
      <h1>Saare subjects</h1>
      <p class="section-note">Subject chuno → folder kholo → file dekho ya download karo.</p>
      <div class="subject-grid">
{chr(10).join(cards)}
      </div>
    </section>
  </main>

{footer(1, self.subjects, [('Computer Network', 'subjects/computer-network/index.html'), ('Previous year papers', 'subjects/previous-year-papers/index.html'), ('Reasoning', 'subjects/reasoning/index.html')])}"""
        self.add("subjects/index.html", body)

    def reader(self) -> None:
        body = f"""{head("PDF & Map Reader — EkGuru Learning", "Mobile-friendly PDF and map reader. Page-wise reading, zoom and direct downloads.", 2, extra_head='<script type="module" src="../../assets/js/viewer.mjs"></script>')}
{header(2, self.nav)}
  <main id="main" class="shell">
    <section class="section">
      {crumbs([('Home', '../../index.html'), ('All Subjects', '../index.html'), ('PDF / Map Reader', '')])}
      <h1 id="readerTitle">PDF / Map Reader</h1>
      <p id="readerStatus" role="status" aria-live="polite">File load ho rahi hai…</p>
      <noscript>Reader ke liye JavaScript on karein. Subject folder par Original / Download links bina JavaScript ke bhi kaam karte hain.</noscript>
      <div id="fileActions" class="button-row" hidden>
        <a id="originalFile" class="button secondary" href="../index.html" target="_blank" rel="noopener noreferrer">Original file ↗</a>
        <a id="downloadFile" class="button primary" href="../index.html">Download</a>
      </div>
      <div id="readerTools" class="reader-tools" hidden aria-label="Reader controls">
        <button id="readerPrev" class="button secondary small" type="button" disabled>← Page</button>
        <span id="pageLabel" aria-live="polite">—</span>
        <button id="readerNext" class="button secondary small" type="button" disabled>Page →</button>
        <button id="readerZoomOut" class="button secondary small" type="button" aria-label="Zoom out">−</button>
        <span id="zoomLabel">100%</span>
        <button id="readerZoomIn" class="button secondary small" type="button" aria-label="Zoom in">+</button>
        <button id="readerFit" class="button secondary small" type="button">Fit width</button>
      </div>
      <div id="readerStage" class="reader-stage" tabindex="0" role="region" aria-label="Document page — scroll to read">
        <canvas id="pdfCanvas" hidden aria-label="PDF page image"></canvas>
      </div>
      <p class="small muted">PDF page image ke roop mein dikhti hai; searchable text / screen reader ke liye Original file use karein.</p>
      <button id="readerRetry" class="button secondary" type="button" hidden>Retry loading</button>
    </section>
  </main>
{footer(2, self.subjects, [('All subjects', 'subjects/index.html'), ('Previous year papers', 'subjects/previous-year-papers/index.html')])}"""
        self.add("subjects/reader/index.html", body)

    # -------------------------------------------------------------- legacy
    def legacy_material(self) -> None:
        """Old links (…/computer-network/material/index.html) keep working: same folder list."""
        subject = next((item for item in self.subjects if item["id"] == "computer-network"), None)
        if not subject:
            return
        tiles = "".join(
            folder_tile(node, f'../{node["path"]}/index.html')
            for node in subject["tree"]["folders"]
        )
        body = f"""{head("Study Material — Computer Network — EkGuru Learning", "Computer Network ke saare PDF folder-wise — theory, practice, answers, tests, reference.", 3)}
{header(3, self.nav, "computer-network")}
  <main id="main" class="shell">
    <section class="section">
      {crumbs([('Home', '../../../index.html'), ('Computer Network', '../index.html'), ('Study Material', '')])}
      <h1>Study Material</h1>
      <p class="section-note">Folder kholo → file dekho ya download karo. Test dene ke liye
        <a href="../test/index.html">Online Test</a> kholo.</p>
      <div class="folder-grid">
{tiles}
      </div>
    </section>
  </main>

{footer(3, self.subjects, [('Home', 'index.html'), ('Computer Network', 'subjects/computer-network/index.html'), ('Online test', 'subjects/computer-network/test/index.html')])}"""
        self.add("subjects/computer-network/material/index.html", body)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if a generated page is missing or stale")
    args = parser.parse_args()

    if not SITE.is_file():
        raise SystemExit("FAIL: data/site.json missing — run tools/build_catalog.py first")
    if not PAPER_CATALOG.is_file():
        raise SystemExit("FAIL: data/catalog/previous-year-papers.json missing")
    site = json.loads(SITE.read_text(encoding="utf-8"))
    subjects_doc = json.loads(SUBJECTS.read_text(encoding="utf-8"))
    paper_catalog = json.loads(PAPER_CATALOG.read_text(encoding="utf-8"))
    validate_paper_catalog(paper_catalog)

    builder = Builder(site, subjects_doc, paper_catalog)
    builder.home()
    builder.subjects_index()
    builder.reader()
    for subject in builder.subjects:
        builder.subject_page(subject)
    builder.paper_exam_pages()
    builder.legacy_material()

    stale = []
    for path, content in builder.written:
        rel_path = path.relative_to(ROOT).as_posix()
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                stale.append(rel_path)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    if args.check:
        if stale:
            print("FAIL: pages are missing or out of date:\n  - " + "\n  - ".join(stale))
            print("      run: python3 tools/build_pages.py")
            return 1
        print(f"PASS: {len(builder.written)} generated page(s) match data/site.json.")
        return 0

    print(f"wrote {len(builder.written)} page(s):")
    for path, _ in sorted(builder.written, key=lambda item: item[0].as_posix()):
        print("  " + path.relative_to(ROOT).as_posix())
    return 0


if __name__ == "__main__":
    sys.exit(main())
