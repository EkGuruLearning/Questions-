# -*- coding: utf-8 -*-
"""
cn_build_complete.py — The Complete Computer Network Book (Theory + MCQs).

Structure (user spec):
  * Har topic/sub-topic PEHLE samjhaya jata hai (theory — full-width, bilingual,
    structured lining); PHIR questions Easy -> Medium -> Hard.
  * Question row = 2 columns: LEFT question + options; RIGHT = sirf ✔ answer +
    ★ nukte (lambi explanation nahi — theory pages woh kaam karte hain).
  * Sab 7 topics, saare 631 MCQs covered. No pictures. Clean lining.
"""
import os, sys, html as _html
import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cn_engine as E
from cn_engine import (CSS, esc, pad_top, rapid_chunks, _archive, PAGE_W, PAGE_H,
                       ML, MR, MT, MB, LEFT, RIGHT, CONTENT_W, TOP, BOTTOM,
                       LETTERS, FONT_DIR, EXAMS_LINE, q_diff, sort_questions, DIFF_LABEL)

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT_DIR = os.path.abspath(os.path.join(HERE, "..", "content", "computer-network", "theory"))
MD_DIR = os.path.abspath(os.path.join(HERE, "..", "maintainer", "computer-network", "theory-md"))

TOPICS = [
    (1, "Introduction of Data Communication"),
    (2, "Network Models (OSI & TCP/IP)"),
    (3, "Addressing (MAC, IPv4, IPv6, Port, DNS)"),
    (4, "Networking Devices"),
    (5, "Transmission Medium"),
    (6, "OSI Layers in Detail"),
    (7, "Network Security"),
]

CSS_EXT = CSS + """
.tband { color: #1F3864; font-weight: bold; font-size: 11.5pt; border-bottom: 2.2pt solid #1F3864; padding: 3pt 0 5pt 0; }
.tbandnote { font-size: 9pt; color: #555; margin: 3pt 0 6pt 0; }
.tintro { font-size: 10.3pt; margin: 4pt 0 8pt 0; line-height: 1.46; }
.tintrohi { font-family: 'ND'; font-size: 9.7pt; color: #333; margin: 0 0 9pt 0; line-height: 1.5; }
.tp { margin: 0 0 2.2pt 10pt; font-size: 9.9pt; line-height: 1.4; }
.tpin { margin: 0 0 6.5pt 22pt; font-family: 'ND'; font-size: 9.3pt; color: #333; line-height: 1.46; }
table.tt { width: 100%; border-collapse: collapse; margin: 7pt 0 9pt 0; }
table.tt td { vertical-align: top; padding: 4.2pt 7pt 4.2pt 0; border-bottom: 0.5pt solid #DCE4F0; font-size: 9.3pt; }
table.tt tr.hdr td { font-weight: bold; color: #1F3864; border-bottom: 1.3pt solid #1F3864; }
.ans { margin: 0 0 3pt 0; font-size: 9.9pt; line-height: 1.38; }
.topicband { color: #1F3864; font-weight: bold; font-size: 15pt; text-align: center; border-bottom: 2.6pt solid #1F3864; padding: 6pt 0 8pt 0; }
.topicnote { font-size: 10pt; text-align: center; color: #333; margin: 6pt 0; }
"""


def q_short(no, q):
    """2-column row: LEFT question + options; RIGHT = answer + nukte only."""
    a = q["ans"]
    left = [f'<p class="qhead"><b>Q{no}.</b> {esc(q["q"][0])}</p>']
    if (q["q"][1] or "").strip():
        left.append(f'<p class="qhi">{esc(q["q"][1])}</p>')
    opts = q["opts"]
    def _opttxt(i):
        oe, oh = opts[i]
        oe = oe or ""; oh = (oh or "").strip()
        s = f'<b>({LETTERS[i]})</b> {esc(oe)}'
        if oh and oh.lower() != oe.strip().lower():
            s += f' <span class="hi">/ {esc(oh)}</span>'
        return s
    for i in (0, 2):
        left.append(f'<p class="opt">{_opttxt(i)} &nbsp;&nbsp;&nbsp; {_opttxt(i+1)}</p>')
    left.append(f'<p class="src">[Source: {esc(q["src"])}] · {DIFF_LABEL[q_diff(q)]}</p>')
    right = [f'<p class="ans">✔ <b>({LETTERS[a]}) {esc(q["opts"][a][0])}</b></p>']
    right.append(f'<p class="nukta">★ <b>Nukta:</b> {esc(q["nk"][0])}</p>')
    if (q["nk"][1] or "").strip():
        right.append(f'<p class="nukta"><span class="hi">{esc(q["nk"][1])}</span></p>')
    return ('<table class="qt"><tr>'
            f'<td class="tq">{"".join(left)}</td>'
            f'<td class="te">{"".join(right)}</td>'
            '</tr></table>')


def theory_chunk(sec_title, note, th):
    """Full-width theory: title band + intro + points (EN + HI) + optional table."""
    parts = [f'<div class="tband">📖 Samjh — {esc(sec_title)}</div>']
    if note:
        parts.append(f'<div class="tbandnote">{esc(note)}</div>')
    intro = th.get("intro")
    if intro:
        parts.append(f'<p class="tintro"><b>{esc(intro[0])}</b></p>')
        if (intro[1] or "").strip():
            parts.append(f'<p class="tintrohi">{esc(intro[1])}</p>')
    for en, hi in th.get("points", []):
        parts.append(f'<p class="tp">• {esc(en)}</p>')
        if (hi or "").strip():
            parts.append(f'<p class="tpin">{esc(hi)}</p>')
    tbl = th.get("table")
    if tbl:
        rows = ['<tr class="hdr">' + "".join(f'<td>{esc(h)}</td>' for h in tbl["head"]) + '</tr>']
        for r in tbl["rows"]:
            rows.append('<tr>' + "".join(f'<td>{esc(c)}</td>' for c in r) + '</tr>')
        parts.append('<table class="tt">' + "".join(rows) + '</table>')
    return "".join(parts)


def cover_chunks(n_q, all_meta):
    c1 = pad_top(f"""
<div class="ctitle">Data Communication &amp; Computer Networks (CN)</div>
<div class="csub">The Complete Book — Theory + MCQs (Topic 1 to 7)</div>
<div class="cline"><b>{n_q} MCQs</b> — har topic pehle <b>समझ (Theory)</b>, phir questions <b>Easy → Medium → Hard</b></div>
<div class="cline">Reference Book: <b>Data Communications and Networking — Behrouz A. Forouzan</b></div>
<div class="cline">Prepared for: <b>{esc(EXAMS_LINE)}</b></div>
""", 26)
    rows = [
        ("Format", "Har section: <b>पहले समझ (full-page theory)</b> → <b>phir questions</b> (Easy → Medium → Hard)"),
        ("Question row", "Left = <b>question + options</b> | Right = <b>✔ correct answer + ★ Nukte</b> (theory pages mein poori समझ)"),
        ("Language", "Hindi second language; <b>technical terms English mein</b> (protocol, topology, jitter…)"),
        ("Difficulty", "Har question par chip: <b>· Easy</b> / <b>· Medium</b> / <b>· Hard</b> — sections mein Easy se Hard tak"),
        ("Coverage", f"<b>{n_q} MCQs</b> — 2011–2026 India-level exams (GATE, NET, KVS, EMRS, DSSSB, RPSC, SSC, RRB, IBPS…) + Forouzan"),
    ]
    irows = "\n".join(f'<div class="irow"><span class="lbl">{k}:</span> {v}</div>' for k, v in rows)
    c2 = pad_top(f'<div class="box">{irows}</div>', 12)
    trows, n = [], 0
    for tnum, ttitle, secs in all_meta:
        trows.append(f'<div class="crow"><b>Topic {tnum}.</b> {esc(ttitle)}')
        for stitle, cnt in secs:
            trows.append(f'<div class="crow" style="padding-left:16pt">{esc(stitle)} &nbsp;—&nbsp; <span class="qr">{cnt} Q</span></div>')
        trows.append('</div>')
    c3 = f'<div class="h2">Syllabus Map — 7 Topics, 31 Sections</div><div class="box">{"".join(trows)}</div>'
    c4 = pad_top("""<div class="box howto"><b style="color:#8A5A00">Kaise padhein:</b> Har section mein pehle <b>समझ</b> padho (concepts, table, formulas) — phir questions karo. Question ka left side khud try karo, right side par <b>✔</b> answer aur <b>★ Nukte</b> (exam trick) check karo. Revision: last mein <b>Nukte Rapid-Fire</b>.</div>""", 10)
    return [c1, c2, c3, c4]


def build(out_pdf, out_md):
    import importlib
    def load(name):
        spec = importlib.util.spec_from_file_location(name, os.path.join(DATA, f"{name}.py"))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        try:
            import cn_textfix
            cn_textfix.normalize_module(m)
        except Exception:
            pass
        return m

    topics = []
    for n, title in TOPICS:
        d = load(f"topic{n}_data")
        th = load(f"topic{n}_theory")
        topics.append((n, title, d, th))

    n_q = sum(len(s["questions"]) for _, _, d, _ in topics for s in d.SECTIONS)
    n_rapid = sum(len(getattr(d, "NUKTE_RAPID", [])) for _, _, d, _ in topics)

    all_meta = [(n, title, [(s["title"], len(s["questions"])) for s in d.SECTIONS])
                for n, title, d, _ in topics]

    chunks = [("cover", c) for c in cover_chunks(n_q, all_meta)]

    qno = 0
    rapid_all = []
    for n, title, d, th in topics:
        tcount = sum(len(s["questions"]) for s in d.SECTIONS)
        band = pad_top(f'<div class="topicband">TOPIC {n} — {esc(title)}</div>'
                       f'<div class="topicnote">{tcount} MCQs • Theory → Questions (Easy → Medium → Hard)</div>', 10)
        chunks.append(("topic", band))
        rapid_all.extend(getattr(d, "NUKTE_RAPID", []))
        th_list = th.THEORY
        for idx, s in enumerate(d.SECTIONS):
            thx = th_list[idx] if idx < len(th_list) else {"points": []}
            chunks.append(("theory", theory_chunk(s["title"], s.get("note", ""), thx)))
            qs = sort_questions(s["questions"])
            if qs:
                chunks.append(("q", q_short(qno + 1, qs[0])))
                qno += 1
                for q in qs[1:]:
                    qno += 1
                    chunks.append(("q", q_short(qno, q)))

    if rapid_all:
        band = pad_top('<div class="band">★ Nukte Rapid-Fire — Exam Pointers (quick revision)</div>'
                       '<div class="bandnote">One-line question (left) with its answer + trick (right). Exam se pehle revise karo.</div>', 12)
        rchunks = rapid_chunks(rapid_all)
        chunks.append(("bandq", band + rchunks[0]))
        for rc in rchunks[1:]:
            chunks.append(("q", rc))

    # ---- pagination (measure per chunk; theory + topic bands start new pages) ----
    arch = _archive()
    scratch = fitz.open()
    SAFETY = 6
    BOTTOM_LIM = BOTTOM - 6
    placed = []
    y = TOP
    for idx, (kind, chunk) in enumerate(chunks):
        MH = 3000
        p = scratch.new_page(width=CONTENT_W, height=MH)
        spare, _ = p.insert_htmlbox(fitz.Rect(0, 0, CONTENT_W, MH - 2), chunk, css=CSS_EXT, archive=arch)
        h = (MH - 2) - spare + SAFETY
        scratch.delete_page(-1)
        force_break = kind in ("theory", "topic")
        new_page = (idx != 0 and (force_break or y + h > BOTTOM_LIM))
        if new_page:
            y = TOP
        placed.append((chunk, new_page))
        y += h
    scratch.close()

    body = []
    for chunk, new_page in placed:
        if new_page:
            chunk = f'<div style="page-break-before: always">{chunk}</div>'
        body.append(chunk)
    html = ("<html><head><meta charset='utf-8'><style>" + CSS_EXT +
            "</style></head><body>" + "\n".join(body) + "</body></html>")
    story = fitz.Story(html=html, archive=arch)
    writer = fitz.DocumentWriter(out_pdf)
    where = fitz.Rect(LEFT, TOP, RIGHT, BOTTOM)
    more = 1
    while more:
        dev = writer.begin_page(fitz.paper_rect("a4"))
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page()
    writer.close()

    doc = fitz.open(out_pdf)
    total = len(doc)
    font = fitz.Font(fontfile=os.path.join(FONT_DIR, "DejaVuSans.ttf"))
    foot = f"The Complete Computer Network — Theory + {n_q} MCQs (EN+HI)  •  Forouzan  •  Page {{}} of {total}"
    for i, page in enumerate(doc):
        r = page.rect
        txt = foot.format(i + 1)
        w = font.text_length(txt, fontsize=7.6)
        x = (r.width - w) / 2
        page.draw_line(fitz.Point(ML, r.height - 32), fitz.Point(PAGE_W - MR, r.height - 32),
                       color=(0.78, 0.82, 0.9), width=0.5)
        page.insert_text(fitz.Point(x, r.height - 22), txt,
                         fontfile=os.path.join(FONT_DIR, "DejaVuSans.ttf"),
                         fontsize=7.6, color=(0.35, 0.35, 0.35))
    doc.set_metadata({
        "title": f"The Complete Computer Network - Theory + {n_q} MCQs (EN+HI, Answers + Nukte)",
        "author": "Arena.ai Agent Mode",
        "subject": "Data Communication & Computer Networks - complete bilingual book: theory + MCQs Easy to Hard (Forouzan)",
        "keywords": "CN, Data Communication, Computer Networks, Forouzan, MCQ, GATE, KVS, RPSC, Hindi, English",
    })
    doc.save(out_pdf, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    print(f"PDF: {out_pdf} ({os.path.getsize(out_pdf)} bytes, {total} pages, {n_q} Qs + {n_rapid} rapid)")
    return n_q, n_rapid, total


def build_md(out_md):
    import importlib
    def load(name):
        spec = importlib.util.spec_from_file_location(name, os.path.join(DATA, f"{name}.py"))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        try:
            import cn_textfix
            cn_textfix.normalize_module(m)
        except Exception:
            pass
        return m
    topics = []
    for n, title in TOPICS:
        d = load(f"topic{n}_data"); th = load(f"topic{n}_theory")
        topics.append((n, title, d, th))
    n_q = sum(len(s["questions"]) for _, _, d, _ in topics for s in d.SECTIONS)
    L = ["# Data Communication & Computer Networks (CN) — The Complete Book", "",
         f"## Theory + {n_q} MCQs (English + Hindi) — Topic 1 to 7", "",
         "**Reference Book:** Data Communications and Networking — Behrouz A. Forouzan", "",
         f"**Prepared for:** {EXAMS_LINE}", "",
         "Format: har section mein pehle **समझ (Theory)**, phir questions **Easy → Medium → Hard**.",
         "Question row: left = question + options | right = **✔ answer + ★ Nukte**.", ""]
    qno = 0
    for n, title, d, th in topics:
        L += [f"# TOPIC {n} — {title}", ""]
        for idx, s in enumerate(d.SECTIONS):
            thx = th.THEORY[idx] if idx < len(th.THEORY) else {"points": []}
            L += [f"## {s['title']}", "", f"*{s['note']}*", ""]
            if thx.get("intro"):
                L += [f"**{thx['intro'][0]}**", "", f"*{thx['intro'][1]}*", ""]
            for en, hi in thx.get("points", []):
                L.append(f"- {en}")
                L.append(f"  - *{hi}*")
            if thx.get("table"):
                L.append("")
                L.append("| " + " | ".join(thx["table"]["head"]) + " |")
                L.append("|" + "---|" * len(thx["table"]["head"]))
                for r in thx["table"]["rows"]:
                    L.append("| " + " | ".join(r) + " |")
            L.append("")
            L.append("### Questions (Easy → Medium → Hard)")
            L.append("")
            for q in sort_questions(s["questions"]):
                qno += 1
                a = q["ans"]
                L.append(f"**Q{qno}.** {q['q'][0]}")
                if (q["q"][1] or "").strip():
                    L.append(f"*{q['q'][1]}*")
                for i, (oe, oh) in enumerate(q["opts"]):
                    hi_s = f" / {oh}" if (oh or "").strip() and (oh or "").strip().lower() != (oe or "").strip().lower() else ""
                    L.append(f"- **({LETTERS[i]})** {oe}{hi_s}")
                L.append(f"✔ **({LETTERS[a]}) {q['opts'][a][0]}**")
                L.append(f"★ **Nukta:** {q['nk'][0]}")
                if (q["nk"][1] or "").strip():
                    L.append(f"*{q['nk'][1]}*")
                L.append(f"*[Source: {q['src']}] · {DIFF_LABEL[q_diff(q)]}*")
                L.append("")
    L += ["# ★ Nukte Rapid-Fire — Exam Pointers", ""]
    for n, title, d, _ in topics:
        for it in getattr(d, "NUKTE_RAPID", []):
            L.append(f"- **{it['q'][0]}** — ✔ {it['a'][0]}")
            L.append(f"  - *{it['q'][1]} — {it['a'][1]}*")
    open(out_md, "w", encoding="utf-8").write("\n".join(L))
    print(f"MD:  {out_md} ({os.path.getsize(out_md)} bytes)")


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    stem = "Complete-Computer-Network-Theory-631-MCQ"
    os.makedirs(MD_DIR, exist_ok=True)
    n_q, n_rapid, pages = build(os.path.join(OUT_DIR, stem + ".pdf"),
                                os.path.join(MD_DIR, stem + ".md"))
    build_md(os.path.join(MD_DIR, stem + ".md"))
    print(f"COMPLETE BOOK: {n_q} Qs + {n_rapid} rapid, {pages} pages")
