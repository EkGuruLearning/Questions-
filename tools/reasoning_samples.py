# -*- coding: utf-8 -*-
"""
reasoning_samples.py — sample chapter ka PDF set banata hai (Reasoning subject).

Ye sirf **namune (samples)** hain, taaki folder ka format saaf dikhe: chapter notes,
practice, answer key aur test paper — har folder me ek file. Asli chapter files
ussi tarah `content/reasoning/<folder>/` me daali jaati hain.

Source (editable, checked in):
    maintainer/reasoning/samples/Series-Chapter.md          → theory PDF
    maintainer/reasoning/samples/Series-Practice.md         → practice PDF
    maintainer/reasoning/samples/Series-Answers.md          → answer key PDF
    maintainer/reasoning/samples/Mixed-Test-Paper.md        → test paper PDF
    maintainer/reasoning/samples/Mixed-Test-Answers.md      → test paper key (answer key PDF me)

Output (published):
    content/reasoning/theory/Reasoning-Series-Sample-Chapter.pdf
    content/reasoning/practice/Reasoning-Series-Sample-Practice.pdf
    content/reasoning/answers/Reasoning-Series-Sample-Answer-Key.pdf
    content/reasoning/tests/Reasoning-Sample-Test-Paper.pdf

Usage:
    python3 tools/reasoning_samples.py            # saare sample banao
    python3 tools/reasoning_samples.py series-practice
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import cn_engine  # noqa: E402
import pyq_build_paper as paper  # noqa: E402  (same fonts, CSS aur page writer)

SRC_DIR = os.path.join(ROOT, "maintainer", "reasoning", "samples")
OUT_DIR = os.path.join(ROOT, "content", "reasoning")

DOCS = [
    {
        "id": "series-chapter",
        "kind": "notes",
        "source": "Series-Chapter.md",
        "out": "theory/Reasoning-Series-Sample-Chapter.pdf",
        "title": "Reasoning — Series (sample chapter)",
        "subtitle": "EkGuru Learning · Reasoning chapter ka namuna",
        "footer": "Reasoning · Series sample chapter",
        "keywords": "reasoning, series, number series, letter series, sample chapter, EkGuru",
    },
    {
        "id": "series-practice",
        "kind": "questions",
        "source": "Series-Practice.md",
        "out": "practice/Reasoning-Series-Sample-Practice.pdf",
        "title": "Reasoning — Series (sample practice)",
        "subtitle": "12 sawal · Rashtra Pariksha ke liye abhyas",
        "footer": "Reasoning · Series sample practice",
        "keywords": "reasoning practice, series questions, number series, letter series",
    },
    {
        "id": "series-answers",
        "kind": "key",
        "source": "Series-Answers.md",
        "questions_source": "Series-Practice.md",
        "extra_source": "Mixed-Test-Answers.md",
        "extra_questions_source": "Mixed-Test-Paper.md",
        "out": "answers/Reasoning-Series-Sample-Answer-Key.pdf",
        "title": "Reasoning — Series (sample answer key)",
        "subtitle": "Hal ke saath jawab · practice + sample test",
        "footer": "Reasoning · sample answer key",
        "keywords": "reasoning answer key, series solutions, explanation",
    },
    {
        "id": "mixed-test",
        "kind": "questions",
        "source": "Mixed-Test-Paper.md",
        "out": "tests/Reasoning-Sample-Test-Paper.pdf",
        "title": "Reasoning — sample test paper",
        "subtitle": "10 sawal · 10 marks · 10 minute",
        "footer": "Reasoning · sample test paper",
        "keywords": "reasoning test paper, mixed reasoning, sample test, 10 questions",
    },
]


def read(relative: str) -> str:
    with open(os.path.join(SRC_DIR, relative), encoding="utf-8") as handle:
        return handle.read()


def inline(text: str) -> str:
    """Plain text ko PDF HTML me badlo — `**bold**` support ke saath."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", paper.esc(text))


def notes_chunks(title: str, markdown: str) -> list[str]:
    """Simple notes markdown -> PDF blocks (`#` title, `##` heading, `-` bullet, text)."""
    chunks: list[str] = []
    buffer: list[str] = []

    def flush() -> None:
        if buffer:
            chunks.append(f'<p>{" ".join(buffer)}</p>')
            buffer.clear()

    for raw in markdown.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        if line.startswith("# "):
            flush()
            continue  # title cover par hi aata hai
        if line.startswith("## "):
            flush()
            chunks.append(paper.band(line[3:].strip()))
            continue
        if line.startswith("- "):
            flush()
            chunks.append(f'<div class="bull">• {inline(line[2:].strip())}</div>')
            continue
        buffer.append(inline(line.strip()))
    flush()
    return chunks


def question_chunks(markdown: str) -> list[str]:
    questions = paper.parse_questions(markdown)
    if not questions:
        raise SystemExit("FAIL: koi question parse nahi hua — markdown format dekho")
    return [paper.question_html(question["n"], question) for question in questions]


def key_chunks(markdown: str, questions_md: str, heading: str) -> list[str]:
    answers = paper.parse_answers(markdown)
    questions = {question["n"]: question for question in paper.parse_questions(questions_md)}
    rows: list[str] = [paper.band(heading, f'Questions 1–{len(questions)}')]
    for number in sorted(questions):
        option = answers.get(number)
        text = questions[number]["options"].get(option, "") if option else ""
        rows.append(f'<div class="keyrow"><b>Q{number}.</b> ({option}) {paper.esc(text)}</div>')
    return rows


def explanation_chunks(markdown: str) -> list[str]:
    chunks: list[str] = []
    for raw in markdown.splitlines():
        line = raw.strip()
        if not line.startswith("- "):
            continue
        text = line[2:].strip()
        bold = text.startswith("**") and "**" in text[2:]
        if bold:
            head, rest = text[2:].split("**", 1)
            chunks.append(f'<div class="note"><b>{paper.esc(head)}</b>{paper.esc(rest)}</div>')
        else:
            chunks.append(f'<div class="note">{paper.esc(text)}</div>')
    return chunks


def build(doc: dict) -> str:
    archive = cn_engine._archive()
    css = paper.PAPER_CSS + "\n.bull { margin: 0 0 3pt 10pt; }\n"
    chunks = [sample_cover(doc)]

    if doc["kind"] == "notes":
        chunks += notes_chunks(doc["title"], read(doc["source"]))
    elif doc["kind"] == "questions":
        chunks += question_chunks(read(doc["source"]))
    else:
        chunks += key_chunks(read(doc["source"]), read(doc["questions_source"]), "Practice — jawab")
        chunks += explanation_chunks(read(doc["source"]))
        if doc.get("extra_source"):
            chunks += key_chunks(read(doc["extra_source"]), read(doc["extra_questions_source"]),
                                 "Sample test — jawab")
            chunks += explanation_chunks(read(doc["extra_source"]))

    out_path = os.path.join(OUT_DIR, doc["out"])
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    paper.write_pdf({}, paper.paginate(chunks, css, archive), css, archive, out_path,
                    doc["footer"], {
                        "title": doc["title"],
                        "author": "EkGuru Learning",
                        "subject": doc["subtitle"],
                        "keywords": doc["keywords"],
                    })
    return out_path


def sample_cover(doc: dict) -> str:
    lines = [
        f'<div class="ctitle">{paper.esc(doc["title"])}</div>',
        f'<div class="csub">{paper.esc(doc["subtitle"])}</div>',
        '<div class="cline" style="margin-top:22pt; font-size:13pt"><b>Namuna (sample)</b></div>',
        '<div class="cline" style="margin-top:6pt">Ye file sirf folder ka format dikhane ke liye hai. '
        'Apne asli chapter ki PDF isi folder me rakh dijiye — website par wo bhi apne aap aa jayegi.</div>',
        '<div class="cline" style="margin-top:18pt">EkGuru Learning · By PRAKASH</div>',
    ]
    return cn_engine.pad_top("".join(lines), 40)


def main() -> int:
    wanted = sys.argv[1:] or [doc["id"] for doc in DOCS]
    for doc in DOCS:
        if doc["id"] not in wanted:
            continue
        path = build(doc)
        print(f"wrote {os.path.relpath(path, ROOT)}  ({os.path.getsize(path) / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
