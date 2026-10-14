# -*- coding: utf-8 -*-
"""
cn_build_verify_key.py — Verification Answer Key for the questions added to the
quiz/practice bank (self-authored / wave originals).

User ask: "jo questions tumne quiz mai add kiya ... fir mai unka ans verify kr lunga"
-> har added question ka Q + 4 options + correct answer + why (EN/HI) + nukte + source,
   taaki user khud answers verify kar sake.

Covered: every question whose source contains "Practice - original" (all waves 1-5),
plus wave-5 ("textbook-based") gap-concept questions — i.e. everything NOT from the
repo source banks (those already have answers in the topic books).

Output: content/computer-network/practice/Answer-Key-Added-Questions-<count>.pdf
"""
import os, sys
import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cn_engine as E
from cn_engine import (esc, _archive, PAGE_W, PAGE_H, ML, MR,
                       LEFT, RIGHT, CONTENT_W, TOP, BOTTOM, LETTERS, FONT_DIR,
                       EXAMS_LINE, q_diff, DIFF_LABEL)

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT_DIR = os.path.abspath(os.path.join(HERE, "..", "content", "computer-network", "practice"))

TOPICS = [
    (1, "Data Communications & Networks"),
    (2, "OSI & TCP/IP Models"),
    (3, "Internetworking & Addressing"),
    (4, "Connecting LANs, Switching & Routing"),
    (5, "Telephony, TV, Cable & Wireless"),
    (6, "Transport, Routing & Application"),
    (7, "Network Security"),
]

CSS = """
@font-face { font-family: 'DVS'; src: url('DejaVuSans.ttf'); }
@font-face { font-family: 'DVSB'; src: url('DejaVuSans-Bold.ttf'); font-weight: bold; }
@font-face { font-family: 'ND'; src: url('NotoDev-Regular.ttf'); }
body { font-family: 'DVS'; font-size: 9.6pt; line-height: 1.38; color: #101010; margin: 0; padding: 0; }
b, strong { font-family: 'DVSB'; }
.hi { font-family: 'ND'; }
.ptitle { font-family: 'DVSB'; font-size: 14pt; color: #1F3864; margin: 0 0 2pt 0; }
.psub { font-size: 8.8pt; color: #444; margin: 0 0 4pt 0; }
.psub b { color: #1F3864; }
.tband { color: #1F3864; font-weight: bold; font-size: 11.5pt; border-bottom: 2pt solid #1F3864; padding: 4pt 0 5pt 0; margin: 10pt 0 6pt 0; }
.qbox { border: 0.6pt solid #BFCEDD; background: #F7F9FC; padding: 6pt 8pt 5pt 8pt; margin: 0 0 7pt 0; }
.qh { font-family: 'DVSB'; font-size: 9.8pt; margin: 0 0 1.5pt 0; line-height: 1.32; }
.qhi { font-family: 'ND'; font-size: 9pt; color: #2a2a2a; margin: 0 0 3.5pt 0; line-height: 1.38; }
.op { margin: 0 0 1pt 8pt; font-size: 9pt; line-height: 1.3; }
.opc { margin: 0 0 1pt 8pt; font-size: 9pt; line-height: 1.3; color: #0B6623; font-family: 'DVSB'; }
.ans { margin: 4pt 0 1pt 0; font-family: 'DVSB'; font-size: 9.4pt; color: #0B6623; }
.why { margin: 2pt 0 0 0; font-size: 8.9pt; line-height: 1.36; }
.nk { margin: 2pt 0 0 0; font-size: 8.7pt; color: #444; line-height: 1.36; }
.ps { color: #7a7a7a; font-size: 7.6pt; margin: 3pt 0 0 0; }
.ww { margin: 1.5pt 0 0 0; font-size: 8.5pt; color: #7a2020; line-height: 1.32; }
"""


def load(name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, os.path.join(DATA, f"{name}.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    try:
        import cn_textfix
        cn_textfix.normalize_module(m)
    except Exception:
        pass
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


def is_added(src):
    s = (src or "").lower()
    return "practice — original" in s or "practice - original" in s or "practice —original" in s


def collect():
    """Return [(topic_no, [qdict...added ones], [qdict...wave5 ones])] with wave5 separated."""
    new_mods = [load(f"practice_new_p{i}") for i in range(1, 6)]
    new_map = {}
    for mi, m in enumerate(new_mods, 1):
        for k in dir(m):
            if k.startswith("P") and isinstance(getattr(m, k), list):
                new_map[k] = (mi, getattr(m, k))

    out = []
    for n, title in TOPICS:
        d = load(f"topic{n}_data")
        added = []
        for s in d.SECTIONS:
            for t in s["questions"]:
                # SECTIONS records are dicts (Q() helper or dict literal)
                src = t["src"] if isinstance(t, dict) else t[0]
                if is_added(src):
                    q = t if isinstance(t, dict) else to_qdict(t)
                    added.append(q)
        # wave lists for this topic (incl. _X, _X2, _X3 ...)
        w5 = []
        for idx, s in enumerate(d.SECTIONS):
            newname = NEW_MAP[n][idx] if idx < len(NEW_MAP[n]) else None
            if not newname:
                continue
            for k2 in sorted(new_map):
                if k2 == newname or k2.startswith(newname + "_X"):
                    mi, lst = new_map[k2]
                    for t in lst:
                        q = to_qdict(t)
                        if mi == 5:
                            w5.append(q)
                        else:
                            added.append(q)
        out.append((n, title, added, w5))
    return out


def q_block(no, q):
    a = q["ans"]
    parts = [f'<div class="qbox">']
    parts.append(f'<p class="qh"><b>Q{no}.</b> {esc(q["q"][0])}</p>')
    if (q["q"][1] or "").strip():
        parts.append(f'<p class="qhi">{esc(q["q"][1])}</p>')
    for i in range(4):
        oe, oh = q["opts"][i]
        oe = oe or ""
        oh = (oh or "").strip()
        cls = "opc" if i == a else "op"
        mark = "<b>✓ </b>" if i == a else ""
        s = f'{mark}<b>({LETTERS[i]})</b> {esc(oe)}'
        if oh and oh.lower() != oe.strip().lower():
            s += f' <span class="hi">/ {esc(oh)}</span>'
        parts.append(f'<p class="{cls}">{s}</p>')
    atext = q["opts"][a][0]
    parts.append(f'<p class="ans">✓ Answer: ({LETTERS[a]}) {esc(atext)}</p>')
    wr = q["wr"][0] if q["wr"] else ""
    wrh = q["wr"][1] if len(q["wr"]) > 1 else ""
    if wr:
        parts.append(f'<p class="why"><b>Why:</b> {esc(wr)}</p>')
    if wrh and wrh.strip() and wrh.strip() != (wr or "").strip():
        parts.append(f'<p class="why"><span class="hi"><b>क्यों:</b> {esc(wrh)}</span></p>')
    nk = q["nk"][0] if q["nk"] else ""
    if nk:
        parts.append(f'<p class="nk"><b>Nukte:</b> {esc(nk)}</p>')
    parts.append(f'<p class="ps">[Source: {esc(q["src"])}] · {DIFF_LABEL[q_diff(q)]}</p>')
    parts.append('</div>')
    return "".join(parts)


def build():
    data = collect()
    chunks = []
    tot = sum(len(a) + len(w) for _, _, a, w in data)
    head = (f'<div class="ptitle">Answer Key &amp; Explanations — Quiz/Practice me add kiye gaye Questions</div>'
            f'<div class="psub"><b>Verification Copy</b> — {tot} self-authored questions (waves 1–5) · '
            f'Har question: stem (EN/HI) + 4 options + <b>✓ correct answer</b> + why (EN/HI) + nukte + source · '
            f'Ye un questions ka key hai jo source banks se NAHI aaye (topic books me inke answers nahi the) · '
            f'Compiled by PRAKASH • EkGuru Learning · Prepared for: {esc(EXAMS_LINE)}</div>')
    chunks.append(head)

    # Part A: wave-5 first (latest additions user wants to verify)
    w5_tot = sum(len(w) for _, _, _, w in data)
    if w5_tot:
        chunks.append(f'<div class="tband">Part A — Wave-5 NEW (new/ material ke gap concepts) — {w5_tot} Q</div>')
        no = 0
        for n, title, added, w5 in data:
            if not w5:
                continue
            chunks.append(f'<div class="tband">Topic {n} — {esc(title)}</div>')
            for q in w5:
                no += 1
                chunks.append(q_block(no, q))

    # Part B: earlier waves
    chunks.append(f'<div class="tband">Part B — Waves 1–4 originals (pehle se bank me) — {tot - w5_tot} Q</div>')
    no = 0
    for n, title, added, w5 in data:
        if not added:
            continue
        chunks.append(f'<div class="tband">Topic {n} — {esc(title)}</div>')
        for q in added:
            no += 1
            chunks.append(q_block(no, q))

    arch = _archive()
    body = []
    y = TOP
    placed = []
    scratch = fitz.open()
    SAFETY = 8
    BOTTOM_LIM = BOTTOM - 6
    for chunk in chunks:
        MH = 3200
        p = scratch.new_page(width=CONTENT_W, height=MH)
        spare, _ = p.insert_htmlbox(fitz.Rect(0, 0, CONTENT_W, MH - 2), chunk, css=CSS, archive=arch)
        h = (MH - 2) - spare + SAFETY
        scratch.delete_page(-1)
        new_page = (chunk != chunks[0] and y + h > BOTTOM_LIM)
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
    out_pdf = os.path.join(OUT_DIR, f"Answer-Key-Added-Questions-{tot}.pdf")
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
    foot = f"Answer Key — Added Questions (Verification) — {tot} Q — CN (Forouzan) • Page {{}} of {total}"
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
        "title": f"CN - Answer Key & Explanations - Added Questions ({tot}) - Verification Copy",
        "author": "Compiled & updated by PRAKASH - EkGuru Learning",
        "subject": "Self-authored CN questions with answers and explanations for user verification",
        "keywords": "CN, answer key, verification, MCQ, Forouzan, Hindi, English",
    })
    doc.save(out_pdf, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    print(f"VERIFY KEY: {tot} Qs -> {os.path.basename(out_pdf)} ({total} pages)")
    for n, title, added, w5 in data:
        print(f"  T{n}: added={len(added)} wave5={len(w5)}")


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    build()
