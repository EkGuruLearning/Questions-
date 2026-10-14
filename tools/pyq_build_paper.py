# -*- coding: utf-8 -*-
"""
pyq_build_paper.py — turn an exam's Markdown paper into a printable PDF.

Source (editable, checked in):
    maintainer/computer-network/past-papers/Past Papers/<paper>/…-QUESTIONS.md
    maintainer/computer-network/past-papers/Past Papers/<paper>/…-ANSWERS.md

Output (published):
    content/previous-year-papers/<exam>/<year>/<name>-Questions.pdf
    content/previous-year-papers/<exam>/<year>/<name>-Answer-Key.pdf

The layout reuses the same engine, fonts and colours as the Computer Network
theory PDFs (tools/cn_engine.py), so a paper looks like the rest of the material:
a cover page, one section band per part of the paper, then the questions.

Usage:
    python3 tools/pyq_build_paper.py                 # every registered paper
    python3 tools/pyq_build_paper.py rpsc-2024-p1    # one paper
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import fitz  # noqa: E402  (PyMuPDF)
import cn_engine  # noqa: E402

FONT_DIR = cn_engine.FONT_DIR
PAPERS_DIR = os.path.join(ROOT, "maintainer", "computer-network", "past-papers", "Past Papers")

PAPERS = [
    {
        "id": "rpsc-2024-p1",
        "source_dir": "RPSC Programmer 2024 Paper-1",
        "questions_md": "2024 Programmer Paper-1 QUESTIONS.md",
        "answers_md": "2024 Programmer Paper-1 ANSWERS.md",
        "out_dir": os.path.join(ROOT, "content", "previous-year-papers", "rpsc", "2024"),
        "file_stem": "RPSC-Programmer-2024-Paper-1",
        "title": "RPSC Programmer 2024 — Paper 1",
        "subtitle": "Rajasthan Public Service Commission · Programmer (Paper 1)",
        "sections": [
            {"label": "Section A · Reasoning, Numerical Analysis & Current Affairs", "from": 1, "to": 40},
            {"label": "Section B · DBMS, Data Communication & Computer Fundamentals", "from": 41, "to": 100},
        ],
        "meta": {
            "exam": "RPSC Programmer 2024",
            "year": "2024",
            "questions": 100,
            "marks": 100,
        },
        "keywords": "RPSC, Programmer, 2024, Paper 1, previous year paper, Rajasthan, reasoning, DBMS, computer networks",
    },
]

QUESTION_RE = re.compile(r"^(\d{1,3})\.\s+\*\*Question\*\*:\s*(.*)$")
OPTION_RE = re.compile(r"^\s+([1-5])\)\s+(.*)$")
ANSWER_ROW_RE = re.compile(r"^\|\s*(\d{1,3})\s*\|\s*([1-5])\s*\|")


def read(path: str) -> str:
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def parse_questions(md: str) -> list[dict]:
    """Markdown -> [{n, stem: [lines], options: {1: text, ...}}]."""
    questions: list[dict] = []
    current = None
    in_fence = False
    for raw in md.splitlines():
        line = raw.rstrip()
        if line.strip().startswith("```"):
            in_fence = not in_fence  # fenced tables keep their rows, drop the markers
            continue
        match = QUESTION_RE.match(line)
        if match:
            current = {"n": int(match.group(1)), "stem": [match.group(2)], "options": {}}
            questions.append(current)
            continue
        if current is None:
            continue
        option = OPTION_RE.match(line)
        if option:
            current["options"][int(option.group(1))] = option.group(2).strip()
            continue
        text = line.strip()
        if text:
            current["stem"].append(text if in_fence else text)
    for question in questions:
        question["stem"] = [line for line in question["stem"] if line.strip() != ""]
    return questions


def parse_answers(md: str) -> dict[int, int]:
    """Answer key (`| Q | Ans | Q | Ans |` rows) -> {question: option}.

    Ek row me kai jodi hoti hai aur beech me khali cell bhi — isliye cells todo aur
    ek-ek (number, option) jodi padho. Regex se overlapping jodiyan chhoot jati hain
    (jaise `| 1 | 2 | | 26 | 3 |` me doosri jodi).
    """
    answers: dict[int, int] = {}
    for line in md.splitlines():
        if "|" not in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        index = 0
        while index < len(cells) - 1:
            number, option = cells[index], cells[index + 1]
            if number.isdigit() and option in {"1", "2", "3", "4", "5"}:
                answers[int(number)] = int(option)
                index += 2
                continue
            index += 1
    return answers


def esc(text: str) -> str:
    return cn_engine.esc(text)


def question_html(number: int, question: dict, answer: int | None = None) -> str:
    stem = "".join(f'<p class="qline">{esc(line)}</p>' for line in question["stem"])
    options = "".join(
        f'<p class="opt"><b>({key})</b> {esc(value)}</p>'
        for key, value in sorted(question["options"].items())
    )
    badge = ""
    if answer is not None:
        badge = f'<p class="ansline">Answer: <b>({answer})</b> {esc(question["options"].get(answer, ""))}</p>'
    return (f'<table class="qt"><tr><td class="tq">'
            f'<p class="qhead"><b>Q{number}.</b></p>{stem}{options}{badge}'
            f'</td></tr></table>')


PAPER_CSS = cn_engine.CSS + """
.qhead { font-family: 'DVSB'; font-size: 10pt; color: #1F3864; margin: 0 0 2pt 0; }
.qline { margin: 0 0 2pt 0; }
.opt { margin: 0 0 1pt 14pt; }
.ansline { margin: 3pt 0 0 0; color: #0B6B3A; }
.qt { margin: 0 0 8pt 0; }
.keyrow { padding: 3pt 0; border-bottom: 0.4pt solid #E2E8F4; }
.keyrow b { color: #1F3864; }
.note { font-size: 9.5pt; color: #444; }
"""


def paginate(chunks: list[str], css: str, archive) -> list[str]:
    """Measure every chunk and split them into A4-sized pages."""
    scratch = fitz.open()
    page_height = cn_engine.BOTTOM - cn_engine.TOP
    pages: list[str] = []
    current: list[str] = []
    used = 0.0
    measure_height = 4000
    for chunk in chunks:
        page = scratch.new_page(width=cn_engine.CONTENT_W, height=measure_height)
        spare, _ = page.insert_htmlbox(fitz.Rect(0, 0, cn_engine.CONTENT_W, measure_height - 2), chunk,
                                       css=css, archive=archive)
        height = (measure_height - 2) - spare + 8
        scratch.delete_page(-1)
        if current and used + height > page_height:
            pages.append("".join(current))
            current, used = [], 0.0
        current.append(chunk)
        used += height
    if current:
        pages.append("".join(current))
    scratch.close()
    return pages


def write_pdf(cfg: dict, pages: list[str], css: str, archive, out_path: str, footer_label: str, meta: dict) -> None:
    html = ("<html><head><meta charset='utf-8'><style>" + css + "</style></head><body>"
            + "\n".join(pages) + "</body></html>")
    story = fitz.Story(html=html, archive=archive)
    writer = fitz.DocumentWriter(out_path)
    where = fitz.Rect(cn_engine.LEFT, cn_engine.TOP, cn_engine.RIGHT, cn_engine.BOTTOM)
    more = 1
    while more:
        device = writer.begin_page(fitz.paper_rect("a4"))
        more, _ = story.place(where)
        story.draw(device)
        writer.end_page()
    writer.close()

    doc = fitz.open(out_path)
    total = len(doc)
    font_file = os.path.join(FONT_DIR, "DejaVuSans.ttf")
    font = fitz.Font(fontfile=font_file)
    for index, page in enumerate(doc):
        text = f"{footer_label} · Page {index + 1}/{total}"
        width = font.text_length(text, fontsize=7.6)
        rect = page.rect
        page.draw_line(fitz.Point(cn_engine.ML, rect.height - 32),
                       fitz.Point(rect.width - cn_engine.MR, rect.height - 32),
                       color=(0.78, 0.82, 0.9), width=0.5)
        page.insert_text(fitz.Point((rect.width - width) / 2, rect.height - 22), text,
                         fontfile=font_file, fontsize=7.6, color=(0.35, 0.35, 0.35))
    doc.set_metadata({**meta, "creator": "EkGuru Learning"})
    doc.save(out_path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()


def cover(cfg: dict, total_questions: int, kind: str) -> str:
    lines = [
        f'<div class="ctitle">{esc(cfg["title"])}</div>',
        f'<div class="csub">{esc(cfg["subtitle"])}</div>',
        '<div class="cline" style="margin-top:18pt">'
        f'<b>{total_questions} questions</b> · {cfg["meta"]["marks"]} marks · '
        f'{len(cfg["sections"])} sections</div>',
        f'<div class="cline" style="margin-top:26pt; font-size:14pt"><b>{esc(kind)}</b></div>',
    ]
    for section in cfg["sections"]:
        count = section["to"] - section["from"] + 1
        lines.append(f'<div class="cline">Q{section["from"]}–{section["to"]} &nbsp;·&nbsp; '
                     f'{esc(section["label"])} &nbsp;·&nbsp; {count} questions</div>')
    lines.append('<div class="cline" style="margin-top:26pt" class="note">'
                 'Ye paper official exam ke baad public hui question paper aur answer key se '
                 'taiyar kiya gaya hai. Practice ke liye print karein.</div>')
    lines.append('<div class="cline" style="margin-top:10pt">EkGuru Learning · By PRAKASH</div>')
    return cn_engine.pad_top("".join(lines), 40)


def band(text: str, note: str = "") -> str:
    return cn_engine.pad_top(f'<div class="band">{esc(text)}</div>'
                             f'<div class="bandnote">{esc(note)}</div>', 12) if note else \
        cn_engine.pad_top(f'<div class="band">{esc(text)}</div>', 12)


def build(cfg: dict) -> list[str]:
    source_dir = os.path.join(PAPERS_DIR, cfg["source_dir"])
    questions = parse_questions(read(os.path.join(source_dir, cfg["questions_md"])))
    answers = parse_answers(read(os.path.join(source_dir, cfg["answers_md"])))
    if not questions:
        raise SystemExit(f"FAIL: no questions parsed from {cfg['questions_md']}")
    by_number = {question["n"]: question for question in questions}
    missing = sorted(set(range(1, cfg["meta"]["questions"] + 1)) - set(by_number))
    if missing:
        raise SystemExit(f"FAIL: {cfg['id']}: questions missing from the markdown: {missing[:10]}")
    archive = cn_engine._archive()
    os.makedirs(cfg["out_dir"], exist_ok=True)
    written: list[str] = []

    # ---------------------------------------------------------------- paper
    chunks = [cover(cfg, len(questions), "Question Paper")]
    for section in cfg["sections"]:
        chunks.append(band(section["label"], f'Questions {section["from"]}–{section["to"]}'))
        for number in range(section["from"], section["to"] + 1):
            chunks.append(question_html(number, by_number[number]))
    out = os.path.join(cfg["out_dir"], f'{cfg["file_stem"]}-Questions.pdf')
    write_pdf(cfg, paginate(chunks, PAPER_CSS, archive), PAPER_CSS, archive, out,
              f'{cfg["title"]} · Question Paper', dict(meta_base(cfg, "Question Paper")))
    written.append(out)

    # ----------------------------------------------------------- answer key
    key_chunks = [cover(cfg, len(questions), "Answer Key")]
    for section in cfg["sections"]:
        rows = []
        for number in range(section["from"], section["to"] + 1):
            answer = answers.get(number)
            text = by_number[number]["options"].get(answer, "") if answer else ""
            rows.append(f'<div class="keyrow"><b>Q{number}.</b> ({answer}) {esc(text)}</div>')
        key_chunks.append(band(section["label"], f'Questions {section["from"]}–{section["to"]}'))
        key_chunks.extend(rows)
    out_key = os.path.join(cfg["out_dir"], f'{cfg["file_stem"]}-Answer-Key.pdf')
    write_pdf(cfg, paginate(key_chunks, PAPER_CSS, archive), PAPER_CSS, archive, out_key,
              f'{cfg["title"]} · Answer Key', dict(meta_base(cfg, "Answer Key")))
    written.append(out_key)
    return written


def meta_base(cfg: dict, kind: str) -> dict:
    return {
        "title": f'{cfg["title"]} — {kind}',
        "author": "EkGuru Learning",
        "subject": f'{cfg["subtitle"]} — {kind}',
        "keywords": cfg["keywords"],
    }


def main() -> int:
    wanted = sys.argv[1:] or [paper["id"] for paper in PAPERS]
    for cfg in PAPERS:
        if cfg["id"] not in wanted:
            continue
        for path in build(cfg):
            size = os.path.getsize(path) / 1024
            print(f"wrote {os.path.relpath(path, ROOT)}  ({size:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
