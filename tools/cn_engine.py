# -*- coding: utf-8 -*-
"""
cn_engine.py — shared bilingual (English + Hindi) MCQ rendering engine.

Renders a topic's curated question bank (SECTIONS) into:
  * a print-ready A4 PDF (PyMuPDF Story -> MuPDF/HarfBuzz gives correct Devanagari
    shaping; fonts embedded once via fitz.Archive), and
  * a Markdown source file.

Pagination: each chunk (cover block / section band+first question / question) is
measured with Page.insert_htmlbox on a scratch page, pagination is simulated, and
`page-break-before: always` markers are injected so that NO question is ever split
across pages and no content touches the footer. (MuPDF Story does NOT honour
break-inside: avoid, hence the manual engine.)

Question schema (per question):
  dict(src=str,
       q=[en, hi], opts=[[en,hi] x4], ans=int(0-3),
       wr=[en,hi],            # why the correct option is right
       nk=[en,hi],            # nukta / key exam point
       ww={wrong_idx: [en,hi]})  # why each wrong option is wrong
SECTIONS = list of {title, note, questions:[...]}  (sub-topic wise order)
"""
import os, html as _html
import fitz

try:
    from cn_taxonomy import EXAMS_LINE
except Exception:
    EXAMS_LINE = "Rajasthan Govt. Exams"

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")

# page geometry (points)
PAGE_W, PAGE_H = fitz.paper_rect("a4").width, fitz.paper_rect("a4").height
ML, MR, MT, MB = 42, 42, 46, 56
LEFT, RIGHT = ML, PAGE_W - MR
CONTENT_W = RIGHT - LEFT
TOP, BOTTOM = MT, PAGE_H - MB

LETTERS = ["A", "B", "C", "D"]
def esc(t): return _html.escape(str(t), quote=False)

CSS = """
@font-face { font-family: 'DVS'; src: url('DejaVuSans.ttf'); }
@font-face { font-family: 'DVSB'; src: url('DejaVuSans-Bold.ttf'); font-weight: bold; }
@font-face { font-family: 'ND'; src: url('NotoDev-Regular.ttf'); }
@font-face { font-family: 'NDB'; src: url('NotoDev-Bold.ttf'); font-weight: bold; }
body { font-family: 'DVS'; font-size: 9.6pt; line-height: 1.38; color: #1a1a1a; margin: 0; padding: 0; }
b, strong { font-family: 'DVSB'; }
.hi { font-family: 'ND'; }
.ctitle { font-size: 19pt; font-weight: bold; color: #1F3864; text-align: center; line-height: 1.25; }
.csub { font-size: 12.5pt; font-weight: bold; color: #1F3864; text-align: center; margin-top: 8pt; }
.cline { font-size: 10pt; text-align: center; color: #333; margin-top: 5pt; }
.cline b { color: #1F3864; }
.box { border: 0.7pt solid #C9D4E4; padding: 7px 10px; font-size: 9.5pt; }
.box .lbl { color: #1F3864; font-weight: bold; }
.irow { border-bottom: 0.5pt solid #DCE4F0; padding: 3.5pt 0; }
.h2 { font-size: 11.5pt; color: #1F3864; font-weight: bold; padding-top: 14pt; }
.crow { border-bottom: 0.5pt solid #DCE4F0; padding: 3.5pt 0; font-size: 9.3pt; }
.crow .qr { color: #1F3864; font-weight: bold; }
.howto { border: 1pt solid #E0C060; border-left: 5pt solid #E0C060; }
.srcfiles { border: 0.7pt solid #C9D4E4; font-size: 8.8pt; color: #333; }
.band { color: #1F3864; font-weight: bold; font-size: 11.5pt; border-bottom: 2.4pt solid #1F3864; padding: 2pt 0 5pt 0; }
.bandnote { font-size: 8.4pt; color: #555; margin: 3pt 0 6pt 0; }
.q { border-bottom: 0.5pt solid #C9D4E4; padding: 6pt 0 10pt 0; }
.qhead { font-size: 10pt; margin: 0 0 1pt 0; }
.qhi { font-family: 'ND'; font-size: 9.6pt; color: #3a3a3a; margin: 0 0 3pt 14pt; }
.opt { margin: 0 0 1pt 16pt; font-size: 9.6pt; }
.ans { color: #1E7B1E; margin: 4pt 0 1pt 2pt; font-size: 9.6pt; }
.anshi { font-family: 'ND'; color: #1E7B1E; margin: 0 0 1pt 16pt; font-size: 9.3pt; }
.nukta { color: #8A5A00; margin: 2pt 0 1pt 2pt; font-size: 9.6pt; }
.nuktahi { font-family: 'ND'; color: #8A5A00; margin: 0 0 1pt 16pt; font-size: 9.3pt; }
.wrong { color: #B00020; font-weight: bold; margin: 3pt 0 1pt 2pt; font-size: 9.6pt; }
.wopt { color: #8A1A1A; margin: 0 0 1pt 24pt; font-size: 9.2pt; }
.src { color: #7a7a7a; font-size: 7.8pt; margin: 3pt 0 0 2pt; }
/* NOTE: no `background` here — MuPDF Story leaks block backgrounds to the top of
   every following page. The dashed red border alone marks the pending box. */
.pending { border: 0.9pt dashed #B00020; padding: 6pt 8pt; margin: 6pt 0; }
.pending .ptag { color: #B00020; font-weight: bold; font-size: 8.6pt; }
"""

def pad_top(chunk, pt):
    return f'<div style="padding-top:{pt}pt">{chunk}</div>'

# --------------------------------------------------------------------------
# chunk builders
# --------------------------------------------------------------------------
def q_chunk(no, q):
    a = q["ans"]
    p = ['<div class="q">']
    p.append(f'<p class="qhead"><b>Q{no}.</b> {esc(q["q"][0])}</p>')
    if q["q"][1].strip():
        p.append(f'<p class="qhi">{esc(q["q"][1])}</p>')
    for i, (oe, oh) in enumerate(q["opts"]):
        hi = f' <span class="hi">/ {esc(oh)}</span>' if oh.strip() else ""
        p.append(f'<p class="opt"><b>({LETTERS[i]})</b> {esc(oe)}{hi}</p>')
    p.append(f'<p class="ans">✔ <b>Correct Answer: ({LETTERS[a]}) {esc(q["opts"][a][0])}</b> — {esc(q["wr"][0])}</p>')
    if q["wr"][1].strip():
        p.append(f'<p class="anshi">{esc(q["wr"][1])}</p>')
    p.append(f'<p class="nukta">★ <b>Nukta (Key Point):</b> {esc(q["nk"][0])}</p>')
    if q["nk"][1].strip():
        p.append(f'<p class="nuktahi">{esc(q["nk"][1])}</p>')
    p.append('<p class="wrong">✖ Why the other options are WRONG (verified):</p>')
    for i in range(4):
        if i != a:
            w = q["ww"][i]
            hi = f' <span class="hi">/ {esc(w[1])}</span>' if w[1].strip() else ""
            p.append(f'<p class="wopt">• <b>({LETTERS[i]})</b> {esc(w[0])}{hi}</p>')
    p.append(f'<p class="src">[Source: {esc(q["src"])}]</p>')
    p.append('</div>')
    return "\n".join(p)

def pending_chunk(no, q):
    """A question that has been auto-ingested but not yet curated/verified."""
    p = ['<div class="pending">']
    p.append(f'<p class="ptag">⚠ NEW — auto-ingested, answer needs verification (pending review)</p>')
    p.append(f'<p class="qhead"><b>P{no}.</b> {esc(q.get("q_en",""))}</p>')
    for i, oe in enumerate(q.get("opts_en", [])):
        p.append(f'<p class="opt"><b>({LETTERS[i]})</b> {esc(oe)}</p>')
    p.append(f'<p class="src">[Source: {esc(q.get("src",""))} | auto-classified: Topic {q.get("topic","?")} / {esc(q.get("subtopic",""))}]</p>')
    p.append('</div>')
    return "\n".join(p)

# --------------------------------------------------------------------------
# cover
# --------------------------------------------------------------------------
def cover_chunks(topic_num, topic_title, n_q, n_pending, sections_meta):
    ranges, n = [], 0
    for s in sections_meta:
        start = n + 1; n += s["count"]; ranges.append((start, n, s["title"]))
    if n_q:
        headline = f"<b>{n_q} MCQs</b> — Repo Questions + Extra (Forouzan) — with Answers, Nukte &amp; Option-wise Verification"
    else:
        headline = f"<b>Curation in progress</b> — {n_pending} auto-extracted questions pending verification (see Pending Review at the end)"
    c1 = pad_top(f"""
<div class="ctitle">Data Communication &amp; Computer Networks (CN)</div>
<div class="csub">Topic {topic_num} of 7 : {esc(topic_title)}</div>
<div class="cline">{headline}</div>
<div class="cline">Reference Book: <b>Data Communications and Networking — Behrouz A. Forouzan</b></div>
<div class="cline">Prepared for: <b>{esc(EXAMS_LINE)}</b></div>
""", 26)
    info_rows = [
        ("Total Questions", f"<b>{n_q}</b> verified MCQs" + (f" + <b>{n_pending}</b> pending review" if n_pending else "")),
        ("Question Type", "MCQ — every question has 4 options (A, B, C, D)"),
        ("Languages", "<b>Bilingual:</b> English + Hindi (हिन्दी)"),
        ("Every question includes", "✔ Correct answer (why it is RIGHT) &nbsp;•&nbsp; ★ Nukta / key point (exam tip) &nbsp;•&nbsp; ✖ why each wrong option is WRONG"),
        ("Verification", "Every answer cross-verified <b>4 times</b> (Forouzan facts + official answer keys of Subject Test / Unit Test Solutions where available)"),
    ]
    irows = "\n".join(f'<div class="irow"><span class="lbl">{k}:</span> {v}</div>' for k, v in info_rows)
    c2 = pad_top(f'<div class="box">{irows}</div>', 12)
    if ranges:
        crows = "\n".join(f'<div class="crow"><b>{i+1}.</b> {esc(t)} &nbsp;—&nbsp; <span class="qr">Q{a} - Q{b}</span></div>'
                          for i, (a, b, t) in enumerate(ranges))
    else:
        crows = '<div class="crow">Sub-topic curation in progress — auto-extracted questions are listed in the <b>"Pending Review"</b> section at the end.</div>'
    c3 = f'<div class="h2">Syllabus Coverage — sub-topic wise order</div><div class="box">{crows}</div>'
    c4 = pad_top("""<div class="box howto"><b style="color:#8A5A00">How to read this PDF:</b> Each question shows 4 options (A-D) in English and Hindi. The line starting with <b>✔</b> gives the correct answer and why it is right. The line starting with <b>★</b> is the <b>Nukta</b> — the key point to remember for the exam. The lines starting with <b>✖</b> explain why every wrong option is wrong. Read the question, try it yourself, then check the answer.</div>""", 12)
    c5 = pad_top("""<div class="box srcfiles"><b style="color:#1F3864">System:</b> This PDF is generated by <b>tools/cn_build_topic.py</b> from <b>tools/data/topic%d_data.py</b>. To add more questions, drop PDFs into <b>Computer Network/Incoming/</b> and run <b>tools/cn_pipeline.py</b> — new questions are auto-classified into topics and appended here (as pending) for review. See <b>Computer Network/README.md</b>.</div>""" % topic_num, 12)
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

def build_pdf(topic_num, topic_title, sections, pending, out_pdf):
    """sections: list of {title, note, questions}. pending: list of pending dicts."""
    arch = _archive()
    scratch = fitz.open()
    chunks = [("cover", c) for c in cover_chunks(topic_num, topic_title, sum(len(s["questions"]) for s in sections), len(pending), [{"title": s["title"], "count": len(s["questions"])} for s in sections])]
    qno = 0
    for s in sections:
        band = pad_top(f'<div class="band">{esc(s["title"])}</div><div class="bandnote">{esc(s["note"])}</div>', 14)
        qs = s["questions"]
        qno += 1
        chunks.append(("bandq", band + q_chunk(qno, qs[0])))
        for q in qs[1:]:
            qno += 1
            chunks.append(("q", q_chunk(qno, q)))
    if pending:
        band = pad_top('<div class="band">Pending Review — auto-ingested, needs verification</div><div class="bandnote">These questions were auto-extracted &amp; classified from uploaded PDFs. Answers/nukte to be verified before counting.</div>', 14)
        chunks.append(("bandq", band + pending_chunk(1, pending[0])))
        for i, q in enumerate(pending[1:], start=2):
            chunks.append(("q", pending_chunk(i, q)))

    # measure + simulate
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

    n_q = sum(len(s["questions"]) for s in sections)
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
        page.draw_line(fitz.Point(ML, r.height - 34), fitz.Point(PAGE_W - MR, r.height - 34), color=(0.78, 0.82, 0.9), width=0.5)
        page.insert_text(fitz.Point(x, r.height - 24), txt, fontfile=os.path.join(FONT_DIR, "DejaVuSans.ttf"), fontsize=7.6, color=(0.35, 0.35, 0.35))
    doc.set_metadata({
        "title": f"Topic {topic_num} - {topic_title} - {n_q} MCQs (Answers + Nukte) — Data Communication & Computer Networks (Forouzan)",
        "author": "Arena.ai Agent Mode",
        "subject": f"Computer Networks - Topic {topic_num}: {topic_title} - bilingual MCQ bank with answers, nukte and option-wise verification",
        "keywords": "CN, Data Communication, Forouzan, MCQ, BCI, SCI, RPSC, Rajasthan, Hindi, English",
    })
    doc.save(out_pdf, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    return total

# --------------------------------------------------------------------------
# markdown
# --------------------------------------------------------------------------
def build_markdown(topic_num, topic_title, sections, pending, out_md):
    n_q = sum(len(s["questions"]) for s in sections)
    L = []
    L.append("# Data Communication & Computer Networks (CN)")
    L.append(f"## Topic {topic_num} of 7 : {topic_title} — {n_q} MCQs (English + Hindi)")
    L.append("")
    L.append("**Reference Book:** Data Communications and Networking — Behrouz A. Forouzan")
    L.append("")
    L.append(f"**Prepared for:** {EXAMS_LINE}")
    L.append("")
    L.append(f"**Total Questions:** {n_q} | **Type:** MCQ (4 options each) | **Bilingual:** English + Hindi | Every question has: ✔ Correct answer (why right) + ★ Nukta (key point) + ✖ option-wise verification (why each wrong option is wrong). All answers cross-verified 4 times.")
    L.append("")
    L.append("**System:** generated by `tools/cn_build_topic.py` from `tools/data/topic%d_data.py`. Add more questions by dropping PDFs into `Computer Network/Incoming/` and running `tools/cn_pipeline.py`. See `Computer Network/README.md`." % topic_num)
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
        for q in s["questions"]:
            qno += 1
            a = q["ans"]
            L.append(f"### Q{qno}. {q['q'][0]}")
            L.append("")
            if q["q"][1].strip():
                L.append(f"<span lang='hi'>{q['q'][1]}</span>")
                L.append("")
            for i, (oe, oh) in enumerate(q["opts"]):
                mark = " ✅ **(CORRECT)**" if i == a else ""
                hi = f" / {oh}" if oh.strip() else ""
                L.append(f"- **({LETTERS[i]})** {oe}{hi}{mark}")
            L.append("")
            L.append(f"**✔ Correct Answer: ({LETTERS[a]}) {q['opts'][a][0]}** — {q['wr'][0]}")
            L.append("")
            if q["wr"][1].strip():
                L.append(f"*{q['wr'][1]}*")
                L.append("")
            L.append(f"**★ Nukta (Key Point):** {q['nk'][0]}")
            L.append("")
            if q["nk"][1].strip():
                L.append(f"*{q['nk'][1]}*")
                L.append("")
            L.append("**✖ Why the other options are WRONG (verified):**")
            for i in range(4):
                if i != a:
                    w = q["ww"][i]
                    hi = f" / {w[1]}" if w[1].strip() else ""
                    L.append(f"- **({LETTERS[i]})** {w[0]}{hi}")
            L.append("")
            L.append(f"*[Source: {q['src']}]*")
            L.append("")
            L.append("---")
    if pending:
        L.append("")
        L.append("## Pending Review — auto-ingested, needs verification")
        L.append("")
        L.append("*These questions were auto-extracted & classified from uploaded PDFs. Answers/nukte to be verified before counting.*")
        L.append("")
        for i, q in enumerate(pending, start=1):
            L.append(f"### P{i}. {q.get('q_en','')}")
            L.append("")
            for j, oe in enumerate(q.get("opts_en", [])):
                L.append(f"- **({LETTERS[j]})** {oe}")
            L.append("")
            L.append(f"*[Source: {q.get('src','')} | auto-classified: Topic {q.get('topic','?')} / {q.get('subtopic','')}]*")
            L.append("")
            L.append("---")
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
