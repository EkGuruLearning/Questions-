# -*- coding: utf-8 -*-
"""
cn_build_practice.py — Topic-wise Practice Test Booklets (print-ready).

User spec:
  * 2 columns per page, BINA solution — sirf question + 4 options + [Source]
  * Max questions per page; readable font (na chhota, na bada)
  * Easy + Medium + Hard mix; section order; Easy->Hard inside sections
  * Existing sourced questions + ORIGINAL predicted questions (practice_new_*)
  * ZERO repeats (dedupe check against the book banks)
  * Answer key (letters only) at the end — print ke liye
Output: Computer Network/Practice/Topic N - Practice Questions (Test Booklet).pdf
"""
import os, sys, html as _html
import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cn_engine as E
from cn_engine import (esc, pad_top, _archive, PAGE_W, PAGE_H, ML, MR,
                       LEFT, RIGHT, CONTENT_W, TOP, BOTTOM, LETTERS, FONT_DIR,
                       EXAMS_LINE, q_diff, sort_questions, DIFF_LABEL)

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT_DIR = os.path.abspath(os.path.join(HERE, "..", "Computer Network", "Practice"))

TOPICS = [
    (1, "Introduction of Data Communication"),
    (2, "Network Models (OSI & TCP/IP)"),
    (3, "Addressing (MAC, IPv4, IPv6, Port, DNS)"),
    (4, "Networking Devices"),
    (5, "Transmission Medium"),
    (6, "OSI Layers in Detail"),
    (7, "Network Security"),
]

CSS = """
@font-face { font-family: 'DVS'; src: url('DejaVuSans.ttf'); }
@font-face { font-family: 'DVSB'; src: url('DejaVuSans-Bold.ttf'); font-weight: bold; }
@font-face { font-family: 'ND'; src: url('NotoDev-Regular.ttf'); }
body { font-family: 'DVS'; font-size: 9.1pt; line-height: 1.32; color: #101010; margin: 0; padding: 0; }
b, strong { font-family: 'DVSB'; }
.hi { font-family: 'ND'; }
.ptitle { font-family: 'DVSB'; font-size: 13.5pt; color: #1F3864; margin: 0 0 2pt 0; }
.psub { font-size: 8.6pt; color: #444; margin: 0 0 3pt 0; }
.psub b { color: #1F3864; }
table.pt { width: 100%; border-collapse: collapse; margin: 0; }
table.pt td.pc { width: 50%; vertical-align: top; padding: 4.5pt 9pt 5pt 0; border-bottom: 0.5pt solid #D5DEEA; }
table.pt td.pcl { border-right: 0.5pt solid #BFCEDD; }
.pq { font-family: 'DVSB'; font-size: 9.1pt; margin: 0 0 1.5pt 0; line-height: 1.3; }
.pqhi { font-family: 'ND'; font-size: 8.5pt; color: #2a2a2a; margin: 0 0 3pt 11pt; line-height: 1.34; }
.po { margin: 0 0 1pt 2pt; font-size: 8.55pt; line-height: 1.28; }
.ps { color: #8a8a8a; font-size: 6.9pt; margin: 2pt 0 0 0; }
.akband { color: #1F3864; font-weight: bold; font-size: 11pt; border-bottom: 2pt solid #1F3864; padding: 3pt 0 5pt 0; }
.ak { font-size: 8.2pt; margin: 0 0 2.5pt 0; line-height: 1.45; }
.ak b { color: #1F3864; }
"""


def _optpair(opts, i):
    def one(j):
        oe, oh = opts[j]
        oe = oe or ""; oh = (oh or "").strip()
        s = f'<b>({LETTERS[j]})</b> {esc(oe)}'
        if oh and oh.lower() != oe.strip().lower():
            s += f' <span class="hi">/ {esc(oh)}</span>'
        return s
    return f'<p class="po">{one(i)} &nbsp;&nbsp; {one(i+1)}</p>'


def q_cell(no, q, first):
    cls = "pc pcl" if first else "pc"
    a = q["ans"]
    parts = [f'<p class="pq"><b>Q{no}.</b> {esc(q["q"][0])}</p>']
    if (q["q"][1] or "").strip():
        parts.append(f'<p class="pqhi">{esc(q["q"][1])}</p>')
    parts.append(_optpair(q["opts"], 0))
    parts.append(_optpair(q["opts"], 2))
    parts.append(f'<p class="ps">[Source: {esc(q["src"])}] · {DIFF_LABEL[q_diff(q)]}</p>')
    return f'<td class="{cls}">{"".join(parts)}</td>'


def load(name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, os.path.join(DATA, f"{name}.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def to_qdict(t):
    src, qen, qhi, opts, ans, wr, nk, ww = t
    o2 = [(list(o) if isinstance(o, (tuple, list)) else [o, o]) for o in opts]
    return dict(src=src, q=[qen, qhi], opts=o2, ans=ans, wr=list(wr), nk=list(nk),
                ww={i: (list(w) if isinstance(w, (tuple, list)) else [w, w]) for i, w in ww.items()})


NEW_MAP = {
    1: ["P1_A", "P1_B", "P1_C", "P1_D", "P1_E", "P1_F", "P1_G"],
    2: ["P2_A", "P2_B", "P2_C", "P2_D"],
    3: ["P3_A", "P3_B", "P3_C", "P3_D", "P3_E"],
    4: ["P4_A", "P4_B", "P4_C", "P4_D"],
    5: ["P5_A", "P5_B", "P5_C"],
    6: ["P6_A", "P6_B", "P6_C", "P6_D", "P6_E"],
    7: ["P7_A", "P7_B", "P7_C"],
}


def build_booklet(n, title):
    d = load(f"topic{n}_data")
    new_mods = [load("practice_new_p1"), load("practice_new_p2"), load("practice_new_p3")]
    new_map = {}
    for m in new_mods:
        for k in dir(m):
            if k.startswith("P") and isinstance(getattr(m, k), list):
                new_map[k] = getattr(m, k)

    sec_blocks = []   # [(section_title, [qs sorted])]
    qno = 0
    keys = []
    for idx, s in enumerate(d.SECTIONS):
        qs = list(s["questions"])
        newname = NEW_MAP[n][idx] if idx < len(NEW_MAP[n]) else None
        if newname and newname in new_map:
            qs.extend(to_qdict(t) for t in new_map[newname])
        qs = sort_questions(qs)
        for q in qs:
            qno += 1
            keys.append((qno, LETTERS[q["ans"]]))
        sec_blocks.append((s["title"], qs))

    chunks = []
    head = (f'<div class="ptitle">Data Communication &amp; Computer Networks — Topic {n}: {esc(title)}</div>'
            f'<div class="psub"><b>Practice Test Booklet</b> — {qno} MCQs (2-column, without solutions) · '
            f'Easy + Medium + Hard mix · Har question ke saath <b>Source</b> · '
            f'Print ke liye · Reference: Forouzan + India-level &amp; worldwide exam papers (GATE/NET/KVS/EMRS/DSSSB/SSC/RRB/IBPS) · '
            f'Prepared for: {esc(EXAMS_LINE)}</div>')
    chunks.append(("head", head))

    rows = []
    for stitle, qs in sec_blocks:
        rows.append(("sec", f'<div class="akband">{esc(stitle)}</div>'))
        for i in range(0, len(qs), 2):
            pair = qs[i:i+2]
            cells = q_cell(i + 1, pair[0], True)  # numbering fixed below
            rows.append(("pair", pair))
    # rebuild with continuous numbering
    chunks = [("head", head)]
    row_html = []
    def flush_rows():
        if row_html:
            chunks.append(("rows", '<table class="pt">' + "".join(row_html) + '</table>'))
            row_html.clear()
    qno = 0
    for stitle, qs in sec_blocks:
        flush_rows()
        sec_prefix = f'<div class="akband">{esc(stitle)}</div>'
        for i in range(0, len(qs), 2):
            pair = qs[i:i+2]
            qno += 1
            cells = q_cell(qno, pair[0], True)
            if len(pair) == 2:
                qno += 1
                cells += q_cell(qno, pair[1], False)
            else:
                cells += '<td class="pc"></td>'
            row_html.append(f'<tr>{cells}</tr>')
            chunks.append(("rows", (sec_prefix if i == 0 else "") +
                           '<table class="pt">' + "".join(row_html) + '</table>'))
            row_html.clear()
    flush_rows()

    # answer key
    ak_rows = []
    for i in range(0, len(keys), 10):
        ak_rows.append(" &nbsp; ".join(f"<b>Q{no}:</b> {a}" for no, a in keys[i:i+10]))
    ak = ('<div class="akband">Answer Key — sirf letters (no solutions)</div>' +
          "".join(f'<p class="ak">{r}</p>' for r in ak_rows))
    chunks.append(("ak", ak))

    # paginate
    arch = _archive()
    scratch = fitz.open()
    SAFETY = 6
    BOTTOM_LIM = BOTTOM - 6
    placed = []
    y = TOP
    for idx, (kind, chunk) in enumerate(chunks):
        MH = 3000
        p = scratch.new_page(width=CONTENT_W, height=MH)
        spare, _ = p.insert_htmlbox(fitz.Rect(0, 0, CONTENT_W, MH - 2), chunk, css=CSS, archive=arch)
        h = (MH - 2) - spare + SAFETY
        scratch.delete_page(-1)
        new_page = (idx != 0 and y + h > BOTTOM_LIM)
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
    html = ("<html><head><meta charset='utf-8'><style>" + CSS +
            "</style></head><body>" + "\n".join(body) + "</body></html>")
    story = fitz.Story(html=html, archive=arch)
    out_pdf = os.path.join(OUT_DIR, f"Topic {n} - Practice Questions - {qno}Q (Test Booklet).pdf")
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
    foot = f"Topic {n} Practice Test Booklet — {qno} MCQs (bina solution) — CN (Forouzan)  •  Page {{}} of {total}"
    for i, page in enumerate(doc):
        r = page.rect
        txt = foot.format(i + 1)
        w = font.text_length(txt, fontsize=7.4)
        x = (r.width - w) / 2
        page.draw_line(fitz.Point(ML, r.height - 32), fitz.Point(PAGE_W - MR, r.height - 32),
                       color=(0.78, 0.82, 0.9), width=0.5)
        page.insert_text(fitz.Point(x, r.height - 22), txt,
                         fontfile=os.path.join(FONT_DIR, "DejaVuSans.ttf"),
                         fontsize=7.4, color=(0.35, 0.35, 0.35))
    doc.set_metadata({
        "title": f"Topic {n} - {title} - Practice Questions ({qno} MCQs, Test Booklet)",
        "author": "Arena.ai Agent Mode",
        "subject": f"CN Topic {n} practice test booklet - 2-column, without solutions, with sources",
        "keywords": "CN, practice, MCQ, test booklet, Forouzan, GATE, Hindi, English",
    })
    doc.save(out_pdf, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    print(f"T{n}: {qno} Qs -> {os.path.basename(out_pdf)} ({total} pages)")
    return qno, total


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tot_q = tot_p = 0
    for n, title in TOPICS:
        q, p = build_booklet(n, title)
        tot_q += q; tot_p += p
    print(f"TOTAL practice: {tot_q} Qs, {tot_p} pages")


if __name__ == "__main__":
    main()
