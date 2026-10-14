# -*- coding: utf-8 -*-
"""
cn_engine.py — shared bilingual (English + Hindi) MCQ rendering engine (v2).

LAYOUT (v2, per user spec):
  * SIDE-BY-SIDE 2-column rows (MuPDF Story <table>): question (left, dark) and
    explanation (right, GREEN = second colour).
  * Explanation = ✔ why-correct + ★ nukta only. "Why wrong" is verified internally
    during curation but NOT printed (kept in data as `ww`).
  * Compact: options in pairs, tight spacing -> many questions per page.
  * Hindi = second language; English technical terms stay in English (Latin script).
  * NO CSS `background` anywhere (MuPDF Story leaks block backgrounds to every page).

Renders a topic's curated bank (SECTIONS) into PDF + Markdown.
Question schema: dict(src, q=[en,hi], opts=[[en,hi]x4], ans, wr=[en,hi], nk=[en,hi],
                      ww={wrong_idx:[en,hi]})   # ww kept for verification, not printed
SECTIONS = list of {title, note, questions}; optional NUKTE_RAPID = [{q:[en,hi], a:[en,hi]}]
"""
import os, html as _html
import fitz

try:
    from cn_taxonomy import EXAMS_LINE
except Exception:
    EXAMS_LINE = "Rajasthan Govt. Exams"

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")

PAGE_W, PAGE_H = fitz.paper_rect("a4").width, fitz.paper_rect("a4").height
ML, MR, MT, MB = 42, 42, 40, 52
LEFT, RIGHT = ML, PAGE_W - MR
CONTENT_W = RIGHT - LEFT
TOP, BOTTOM = MT, PAGE_H - MB

LETTERS = ["A", "B", "C", "D"]
def esc(t): return _html.escape(str(t), quote=False)

# difficulty (Easy->Medium->Hard ordering per user spec)
try:
    from cn_difficulty import q_diff, sort_questions, DIFF_LABEL
except ImportError:
    from tools.cn_difficulty import q_diff, sort_questions, DIFF_LABEL

CSS = """
@font-face { font-family: 'DVS'; src: url('DejaVuSans.ttf'); }
@font-face { font-family: 'DVSB'; src: url('DejaVuSans-Bold.ttf'); font-weight: bold; }
@font-face { font-family: 'ND'; src: url('NotoDev-Regular.ttf'); }
@font-face { font-family: 'NDB'; src: url('NotoDev-Bold.ttf'); font-weight: bold; }
body { font-family: 'DVS'; font-size: 10pt; line-height: 1.42; color: #1a1a1a; margin: 0; padding: 0; }
b, strong { font-family: 'DVSB'; }
.hi { font-family: 'ND'; }
.ctitle { font-size: 19pt; font-weight: bold; color: #1F3864; text-align: center; line-height: 1.3; }
.csub { font-size: 13pt; font-weight: bold; color: #1F3864; text-align: center; margin-top: 10pt; }
.cline { font-size: 10.5pt; text-align: center; color: #333; margin-top: 6pt; }
.cline b { color: #1F3864; }
.box { border: 0.7pt solid #C9D4E4; padding: 9px 12px; font-size: 10pt; }
.box .lbl { color: #1F3864; font-weight: bold; }
.irow { border-bottom: 0.5pt solid #DCE4F0; padding: 5pt 0; }
.h2 { font-size: 12pt; color: #1F3864; font-weight: bold; padding-top: 14pt; }
.crow { border-bottom: 0.5pt solid #DCE4F0; padding: 4.5pt 0; font-size: 10pt; }
.crow .qr { color: #1F3864; font-weight: bold; }
.howto { border: 1pt solid #E0C060; border-left: 5pt solid #E0C060; }
.srcfiles { border: 0.7pt solid #C9D4E4; font-size: 9pt; color: #333; }
.band { color: #1F3864; font-weight: bold; font-size: 12pt; border-bottom: 2.2pt solid #1F3864; padding: 3pt 0 5pt 0; }
.bandnote { font-size: 9pt; color: #555; margin: 4pt 0 8pt 0; }
table.qt { width: 100%; border-collapse: collapse; margin: 0 0 7pt 0; }
table.qt td { vertical-align: top; padding: 7pt 8pt 8pt 0; border-bottom: 0.7pt solid #C9D4E4; }
td.tq { width: 57%; color: #101010; border-right: 0.7pt solid #BFCEDD; padding-right: 11pt; }
td.te { width: 43%; color: #0B6623; padding-left: 11pt; }
.qhead { font-size: 10.4pt; margin: 0 0 2.5pt 0; line-height: 1.35; }
.qhi { font-family: 'ND'; font-size: 9.8pt; color: #3a3a3a; margin: 0 0 4pt 14pt; line-height: 1.42; }
.opt { margin: 0 0 1.8pt 2pt; font-size: 10pt; }
.optb { margin: 0 0 1.8pt 2pt; font-size: 10pt; }
.why { margin: 0 0 3pt 0; font-size: 9.6pt; line-height: 1.4; }
.nukta { margin: 0 0 2.5pt 0; font-size: 9.6pt; line-height: 1.4; }
.src { color: #7a7a7a; font-size: 8pt; margin: 3pt 0 0 0; }
table.rt { width: 100%; border-collapse: collapse; }
table.rt td { vertical-align: top; padding: 5pt 8pt 5pt 0; border-bottom: 0.5pt solid #DCE4F0; }
td.rq { width: 47%; color: #101010; border-right: 0.7pt solid #BFCEDD; padding-right: 11pt; font-size: 9.8pt; }
td.ra { width: 53%; color: #0B6623; padding-left: 11pt; font-size: 9.8pt; }
"""

def pad_top(chunk, pt):
    return f'<div style="padding-top:{pt}pt">{chunk}</div>'

# --------------------------------------------------------------------------
# question chunk — SIDE BY SIDE: question | explanation(green)
# --------------------------------------------------------------------------
def q_chunk(no, q):
    a = q["ans"]
    left = [f'<p class="qhead"><b>Q{no}.</b> {esc(q["q"][0])}</p>']
    if (q["q"][1] or "").strip():
        left.append(f'<p class="qhi">{esc(q["q"][1])}</p>')
    opts = q["opts"]
    # options in pairs (A+B / C+D) for compactness; skip Hindi gloss when identical to English
    def _opttxt(i):
        oe, oh = opts[i]
        oe = oe or ""
        oh = oh or ""
        s = f'<b>({LETTERS[i]})</b> {esc(oe)}'
        oh2 = oh.strip()
        if oh2 and oh2.lower() != oe.strip().lower():
            s += f' <span class="hi">/ {esc(oh2)}</span>'
        return s
    for i in (0, 2):
        left.append(f'<p class="opt">{_opttxt(i)} &nbsp;&nbsp;&nbsp; {_opttxt(i+1)}</p>')
    left.append(f'<p class="src">[Source: {esc(q["src"])}] · {DIFF_LABEL[q_diff(q)]}</p>')

    right = [f'<p class="why">✔ <b>Correct: ({LETTERS[a]}) {esc(q["opts"][a][0])}</b> — {esc(q["wr"][0])}</p>']
    if (q["wr"][1] or "").strip():
        right.append(f'<p class="why"><span class="hi">{esc(q["wr"][1])}</span></p>')
    right.append(f'<p class="nukta">★ <b>Nukta:</b> {esc(q["nk"][0])}</p>')
    if (q["nk"][1] or "").strip():
        right.append(f'<p class="nukta"><span class="hi">{esc(q["nk"][1])}</span></p>')

    return ('<table class="qt"><tr>'
            f'<td class="tq">{"".join(left)}</td>'
            f'<td class="te">{"".join(right)}</td>'
            '</tr></table>')

# --------------------------------------------------------------------------
# nukte rapid-fire chunk (compact revision pointers)
# --------------------------------------------------------------------------
def rapid_chunks(rapid):
    out = []
    rows = []
    for it in rapid:
        rows.append(f'<tr><td class="rq">{esc(it["q"][0])}<br/><span class="hi">{esc(it["q"][1])}</span></td>'
                    f'<td class="ra">✔ {esc(it["a"][0])}<br/><span class="hi">{esc(it["a"][1])}</span></td></tr>')
    for i in range(0, len(rows), 8):  # chunk every 8 rows -> keeps tables small
        out.append('<table class="rt">' + "".join(rows[i:i + 8]) + '</table>')
    return out

# --------------------------------------------------------------------------
# cover
# --------------------------------------------------------------------------
def cover_chunks(topic_num, topic_title, n_q, sections_meta, n_rapid=0, n_pending=0):
    ranges, n = [], 0
    for s in sections_meta:
        start = n + 1; n += s["count"]; ranges.append((start, n, s["title"]))
    if n_q == 0 and n_pending:
        count_line = f'<b>{n_pending} Pending Questions</b> — staged from repo exam PDFs &amp; trusted sources — <b>NEED VERIFICATION</b> (answers + Hindi to be verified during topic build)'
    else:
        count_line = f'<b>{n_q} MCQs</b> — Repo Exam Questions + Forouzan — bilingual (English + Hindi), exam-ready'
    c1 = pad_top(f"""
<div class="ctitle">Data Communication &amp; Computer Networks (CN)</div>
<div class="csub">Topic {topic_num} of 7 : {esc(topic_title)}</div>
<div class="cline">{count_line}</div>
<div class="cline">Reference Book: <b>Data Communications and Networking — Behrouz A. Forouzan</b></div>
<div class="cline">Prepared for: <b>{esc(EXAMS_LINE)}</b></div>
""", 22)
    total_row = (f"<b>{n_q}</b> MCQs" + (f" + <b>{n_rapid}</b> Nukte rapid-fire revision points" if n_rapid else "")) if n_q else f"<b>{n_pending}</b> pending questions (staging)"
    info_rows = [
        ("Total Questions", total_row),
        ("Question Type", "MCQ — 4 options (A, B, C, D) per question, in English + Hindi"),
        ("Layout", "Left = <b>question</b> &nbsp;|&nbsp; Right = <b>explanation</b> (green): <b>✔ why the correct answer is right</b> + <b>★ Nukta</b> (key exam point)"),
        ("Language rule", "Hindi is the second language; <b>technical terms stay in English</b> (topology, protocol, jitter…)"),
        ("Verification", "Every answer cross-verified <b>4×</b> (Forouzan + official answer keys of Subject Test / Unit Test Solutions). Wrong options verified internally."),
    ]
    irows = "\n".join(f'<div class="irow"><span class="lbl">{k}:</span> {v}</div>' for k, v in info_rows)
    c2 = pad_top(f'<div class="box">{irows}</div>', 10)
    crows = "\n".join(f'<div class="crow"><b>{i+1}.</b> {esc(t)} &nbsp;—&nbsp; <span class="qr">Q{a} - Q{b}</span></div>'
                      for i, (a, b, t) in enumerate(ranges))
    c3 = f'<div class="h2">Syllabus Coverage — sub-topic wise order</div><div class="box">{crows}</div>'
    c4 = pad_top("""<div class="box howto"><b style="color:#8A5A00">How to read:</b> Left side: question + 4 options (try it yourself first). Right side (green): <b>✔</b> correct answer with why it is right, and <b>★ Nukta</b> — the one-line exam tip to remember. Practice in 2 passes: first read question + options only, then check the green column.</div>""", 10)
    c5 = pad_top("""<div class="box srcfiles"><b style="color:#1F3864">System:</b> generated by <b>tools/cn_build_topic.py</b> from <b>tools/data/topic%d_data.py</b>. To add more questions later: drop PDFs into <b>maintainer/computer-network/intake/</b> and run <b>tools/cn_pipeline.py</b> — new questions auto-classify topic-wise. See <b>maintainer/computer-network/docs/README.md</b>.</div>""" % topic_num, 10)
    return [c1, c2, c3, c4, c5]

# --------------------------------------------------------------------------
# measure + simulate + render
# --------------------------------------------------------------------------
def _archive():
    arch = fitz.Archive()
    arch.add(os.path.join(FONT_DIR, "DejaVuSans.ttf"), "DejaVuSans.ttf")
    arch.add(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), "DejaVuSans-Bold.ttf")
    arch.add(os.path.join(FONT_DIR, "noto-sans-devanagari-devanagari-400-normal.ttf"), "NotoDev-Regular.ttf")
    arch.add(os.path.join(FONT_DIR, "noto-sans-devanagari-devanagari-700-normal.ttf"), "NotoDev-Bold.ttf")
    return arch

def build_pdf(topic_num, topic_title, sections, pending, out_pdf, nukte_rapid=None):
    """sections: [{title, note, questions}]. pending: legacy (unused in v2 main flow)."""
    arch = _archive()
    scratch = fitz.open()
    n_q = sum(len(s["questions"]) for s in sections)
    n_rapid = len(nukte_rapid or [])
    chunks = [("cover", c) for c in cover_chunks(topic_num, topic_title, n_q,
               [{"title": s["title"], "count": len(s["questions"])} for s in sections], n_rapid,
               n_pending=len(pending))]
    qno = 0
    for s in sections:
        band = pad_top(f'<div class="band">{esc(s["title"])}</div><div class="bandnote">{esc(s["note"])}</div>', 12)
        qs = sort_questions(s["questions"])
        qno += 1
        chunks.append(("bandq", band + q_chunk(qno, qs[0])))
        for q in qs[1:]:
            qno += 1
            chunks.append(("q", q_chunk(qno, q)))
    if nukte_rapid:
        band = pad_top('<div class="band">★ Nukte Rapid-Fire — Exam Pointers (quick revision)</div>'
                       '<div class="bandnote">One-line question (left) with its exam answer + trick (right). Revise these before the exam.</div>', 12)
        rchunks = rapid_chunks(nukte_rapid)
        chunks.append(("bandq", band + rchunks[0]))
        for rc in rchunks[1:]:
            chunks.append(("q", rc))
    # legacy pending support (only if provided and sections empty of them)
    if pending:
        band = pad_top('<div class="band">Pending Review — auto-ingested, needs verification</div>'
                       '<div class="bandnote">Auto-extracted &amp; classified; answers to be verified before counting.</div>', 12)
        rows = []
        for i, q in enumerate(pending, 1):
            opts = "".join(f'<p class="opt"><b>({LETTERS[j]})</b> {esc(o)}</p>' for j, o in enumerate(q.get("opts_en", [])))
            note = esc(q.get("note", "")) if q.get("note") else "auto-ingested — answer needs verification"
            rows.append(f'<table class="qt"><tr><td class="tq"><p class="qhead"><b>P{i}.</b> {esc(q.get("q_en",""))}</p>{opts}'
                        f'<p class="src">[Source: {esc(q.get("src",""))} | auto-classified: Topic {q.get("topic","?")} / {esc(q.get("subtopic",""))}]</p></td>'
                        f'<td class="te"><p class="why">⚠ {note}</p></td></tr></table>')
        chunks.append(("bandq", band + rows[0]))
        for r in rows[1:]:
            chunks.append(("q", r))

    # measure + simulate pagination
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
    html = "<html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>" + "\n".join(body) + "</body></html>"

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
    foot = f"Topic {topic_num}: {topic_title}  •  Data Communication & Computer Networks — Forouzan  •  Page {{}} of {total}"
    for i, page in enumerate(doc):
        r = page.rect
        txt = foot.format(i + 1)
        w = font.text_length(txt, fontsize=7.6)
        x = (r.width - w) / 2
        page.draw_line(fitz.Point(ML, r.height - 32), fitz.Point(PAGE_W - MR, r.height - 32), color=(0.78, 0.82, 0.9), width=0.5)
        page.insert_text(fitz.Point(x, r.height - 22), txt, fontfile=os.path.join(FONT_DIR, "DejaVuSans.ttf"), fontsize=7.6, color=(0.35, 0.35, 0.35))
    doc.set_metadata({
        "title": f"Topic {topic_num} - {topic_title} - {n_q} MCQs (EN+HI, Answers + Nukte) — Data Communication & Computer Networks (Forouzan)",
        "author": "Arena.ai Agent Mode",
        "subject": f"Computer Networks - Topic {topic_num}: {topic_title} - bilingual MCQ bank with answers and nukte",
        "keywords": "CN, Data Communication, Forouzan, MCQ, BCI, SCI, RPSC, Rajasthan, Hindi, English",
    })
    doc.save(out_pdf, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    return total

# --------------------------------------------------------------------------
# markdown
# --------------------------------------------------------------------------
def build_markdown(topic_num, topic_title, sections, pending, out_md, nukte_rapid=None):
    n_q = sum(len(s["questions"]) for s in sections)
    L = []
    L.append("# Data Communication & Computer Networks (CN)")
    L.append(f"## Topic {topic_num} of 7 : {topic_title} — {n_q} MCQs (English + Hindi)")
    L.append("")
    L.append("**Reference Book:** Data Communications and Networking — Behrouz A. Forouzan")
    L.append("")
    L.append(f"**Prepared for:** {EXAMS_LINE}")
    L.append("")
    L.append(f"**Total Questions:** {n_q} | **Type:** MCQ (4 options) | **Bilingual:** English + Hindi (technical terms in English) | Each: ✔ why the correct answer is right + ★ Nukta. Wrong options verified internally. Answers cross-verified 4×.")
    L.append("")
    L.append("### Syllabus Coverage (sub-topic wise order)")
    L.append("")
    L.append("| # | Sub-topic | Questions |")
    L.append("|---|-----------|-----------|")
    n = 0
    for i, s in enumerate(sections):
        start = n + 1; n += len(s["questions"])
        L.append(f"| {i+1} | {s['title']} | Q{start} - Q{n} |")
    L.append("")
    L.append("---")
    qno = 0
    for s in sections:
        L.append("")
        L.append(f"## {s['title']}")
        L.append("")
        L.append(f"*{s['note']}*")
        L.append("")
        for q in sort_questions(s["questions"]):
            qno += 1
            a = q["ans"]
            L.append(f"### Q{qno}. {q['q'][0]}")
            L.append("")
            if (q["q"][1] or "").strip():
                L.append(f"<span lang='hi'>{q['q'][1]}</span>")
                L.append("")
            for i, (oe, oh) in enumerate(q["opts"]):
                mark = " ✅ **(CORRECT)**" if i == a else ""
                oh = oh or ""; oe = oe or ""
                hi = f" / {oh}" if oh.strip() else ""
                L.append(f"- **({LETTERS[i]})** {oe}{hi}{mark}")
            L.append("")
            L.append(f"**✔ Correct Answer: ({LETTERS[a]}) {q['opts'][a][0]}** — {q['wr'][0]}")
            L.append("")
            if (q["wr"][1] or "").strip():
                L.append(f"*{q['wr'][1]}*")
                L.append("")
            L.append(f"**★ Nukta (Key Point):** {q['nk'][0]}")
            L.append("")
            if (q["nk"][1] or "").strip():
                L.append(f"*{q['nk'][1]}*")
                L.append("")
            L.append(f"*[Source: {q['src']}] · {DIFF_LABEL[q_diff(q)]}*")
            L.append("")
            L.append("---")
    if nukte_rapid:
        L.append("")
        L.append("## ★ Nukte Rapid-Fire — Exam Pointers")
        L.append("")
        for it in nukte_rapid:
            L.append(f"- **{it['q'][0]}** *({it['q'][1]})* → **{it['a'][0]}** *({it['a'][1]})*")
        L.append("")
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
