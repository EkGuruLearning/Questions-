#!/usr/bin/env python3
"""One-time/reviewable import of existing repo questions into native CBT authoring.
Requires PyMuPDF only for re-importing the existing RPSC reprint, not normal builds.
No OCR or new exam questions/keys are invented. Existing PDFs stay byte-identical.
"""
import hashlib
import json
import pathlib
import re
ROOT = pathlib.Path(__file__).resolve().parent.parent

def save(subject, doc):
    path = ROOT / f"data/tests/{subject}/{doc['id']}.test.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"schema_version": 1, **doc}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(path.relative_to(ROOT))

def source(pdf):
    return {"pdf": pdf, "sha256": hashlib.sha256((ROOT / pdf).read_bytes()).hexdigest(), "label": "Existing repository practice material — not independently verified official key"}

def rpsc():
    import pymupdf
    pdf = "content/previous-year-papers/rpsc/2024/RPSC-Programmer-2024-Paper-1-Questions.pdf"
    meta = json.loads((ROOT / "data/practice/papers/rpsc/2024/RPSC-Programmer-2024-Paper-1-Questions.paper.json").read_text())
    assert hashlib.sha256((ROOT / pdf).read_bytes()).hexdigest() == meta["paper_sha256"]
    document = pymupdf.open(ROOT / pdf)
    pages, page_by_question = [], {}
    for i, page in enumerate(document):
        lines = [line for line in page.get_text().splitlines() if not re.match(r"^RPSC Programmer 2024 · Paper 1 · Question Paper · Page|^Section [AB] ·|^Questions (?:1–40|41–100)$", line)]
        content = "\n".join(lines)
        for number in re.findall(r"(?m)^Q(\d+)\.$", content): page_by_question[int(number)] = i + 1
        pages.append(content)
    parts = re.split(r"(?m)^Q(\d+)\.\s*\n", "\n".join(pages))
    questions = []
    ligatures = str.maketrans({"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl"})
    for number, body in zip(parts[1::2], parts[2::2]):
        split = re.split(r"(?m)^\(([1-5])\)\s*", body.translate(ligatures))
        assert split[1::2] == list("12345"), f"Review options for Q{number}"
        q = {"text": split[0].strip(), "options": [value.strip() for value in split[2::2]], "skip_option": "E", "source_page": page_by_question[int(number)]}
        answer = meta["answer_key"].get(number)
        if answer and answer != "DROP": q["answer"] = [answer] if isinstance(answer, str) else answer
        if number == "3": q["notice"] = "Ungraded: provided key conflicts with the question (500 − 70 = 430). Original PDF/key are preserved."
        if number == "5": q["notice"] = "Ungraded: the existing reprint does not include the complete source table."
        questions.append(q)
    assert len(questions) == 100 and len(page_by_question) == 100
    save("previous-year-papers", {"id": "rpsc-programmer-2024-paper-1", "title": "RPSC Programmer 2024 — Paper 1", "subject_title": "Previous Year Papers", "kind": "paper", "duration_minutes": 120,
        "note": "Native CBT transcription of the existing repository reprint. Provided practice key, not independently verified official final key. Q3/Q5 are intentionally ungraded. Timing/marking are practice settings, not an official pattern claim.", "source": source(pdf), "questions": questions})

def reasoning():
    for test, paper, answers, pdf in [
        ("series-12", "Series-Practice.md", "Series-Answers.md", "content/reasoning/practice/Reasoning-Series-Sample-Practice.pdf"),
        ("mixed-10", "Mixed-Test-Paper.md", "Mixed-Test-Answers.md", "content/reasoning/tests/Reasoning-Sample-Test-Paper.pdf"),
    ]:
        base = ROOT / "maintainer/reasoning/samples"
        body, keys = (base / paper).read_text(), (base / answers).read_text()
        answer = dict(re.findall(r"\|\s*(\d+)\s*\|\s*([1-4])\s*\|", keys))
        explanation = dict(re.findall(r"(?m)^- \*\*Q(\d+).*?\*\* — (.+)$", keys))
        parts = re.split(r"(?m)^(\d+)\. \*\*Question\*\*: ", body)
        questions = []
        for number, content in zip(parts[1::2], parts[2::2]):
            options = re.split(r"(?m)^\s*([1-4])\) ", content)
            assert options[1::2] == list("1234")
            q = {"text": options[0].strip(), "options": [value.strip() for value in options[2::2]], "answer": ["ABCD"[int(answer[number]) - 1]], "explanation": explanation.get(number, "")}
            if test == "mixed-10" and number == "6":
                q.pop("answer"); q["explanation"] = "Given that Q is R's sister does not determine R's gender. The source key incorrectly assumes R is female."
                q["notice"] = "Ungraded: the provided relationship is insufficient to determine R's gender."
            questions.append(q)
        assert len(questions) == (12 if test == "series-12" else 10)
        save("reasoning", {"id": test, "title": "Series practice — 12 questions" if test == "series-12" else "Mixed reasoning — 10 questions", "subject_title": "Reasoning", "duration_minutes": 12 if test == "series-12" else 10,
            "note": "Existing EkGuru sample questions, not a previous official exam. Mixed test Q6 is ungraded because its source relationship is ambiguous.", "source": source(pdf), "questions": questions})
if __name__ == "__main__": rpsc(); reasoning()
