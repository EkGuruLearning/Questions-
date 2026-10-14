# -*- coding: utf-8 -*-
"""
cn_extract.py — extract MCQs from a question PDF (text or scanned/OCR).

The source PDFs are bilingual EN+HI, but their embedded Hindi text layer is
OCR-garbled (broken ToUnicode): some Hindi survives as Devanagari, some as
Latin mojibake (digits/punctuation). This extractor pulls the CLEAN ENGLISH
question + 4 options and drops the garbled Hindi (Hindi is re-authored later
during curation). It also strips the copy-pasted page headers/footers.

Handles option-label styles: (a) (A) a) a. A) A.  and  (1) (2) 1. 2. (fallback).
Output per question: dict(q_en, opts_en[4], src)
"""
import os, re

DEV_RANGE = re.compile(r"[\u0900-\u097F\u1CD0-\u1CFF]")  # Devanagari

# ---------------------------------------------------------------------------
# text retrieval (pymupdf, with RapidOCR fallback for scanned PDFs)
# ---------------------------------------------------------------------------
def _latin_ratio(text):
    if not text:
        return 0.0
    return sum(1 for c in text if c.isascii()) / max(1, len(text))

def get_text(pdf_path):
    import fitz
    doc = fitz.open(pdf_path)
    pages = [p.get_text() for p in doc]
    doc.close()
    full = "\n".join(pages)
    if _latin_ratio(full) < 0.05 or len(full.strip()) < 200:  # scanned -> OCR
        try:
            return _ocr_pdf(pdf_path)
        except Exception as e:
            print(f"  [warn] OCR failed for {os.path.basename(pdf_path)}: {e}")
    return full

def _ocr_pdf(pdf_path):
    import fitz
    from rapidocr_onnxruntime import RapidOCR
    engine = RapidOCR()
    doc = fitz.open(pdf_path)
    out = []
    for page in doc:
        pix = page.get_pixmap(dpi=200)
        res, _ = engine(pix.tobytes("png"))
        if res:
            out.append("\n".join(r[1] for r in res))
    doc.close()
    return "\n".join(out)

# ---------------------------------------------------------------------------
# cleaning
# ---------------------------------------------------------------------------
NOISE_RE = re.compile(
    r"^\s*TOPIC\s*-|Join\s+\w+|Contact\s*@|\d{7,}|BCI\s*/?\s*SCI\s*Batch|"
    r"Batch\s*–|UNIT\s*TEST|^\s*Page\s+\d+|Rajasthan\s*PYQ|^\s*Random\s*Test|"
    r"^\s*\d{1,3}\s*$|^\s*Subject\s*Test\s*Solution|^\s*Unit\s*Test",
    re.IGNORECASE,
)

# trailing garbled-Hindi fragment (must contain a mojibake punct char > % / | < \ )
GARBLED_TAIL = re.compile(r"\s+(?=[\d\s>%/<>|\\+\\-]*[>%/<>|\\])[\d\s>%/<>|\\+\\-]+\??\s*$")

def _strip_devanagari_line(line):
    if DEV_RANGE.search(line):
        stripped = re.sub(r"\s+", " ", DEV_RANGE.sub(" ", line)).strip(" /-|,")
        if len(stripped) >= 2 and _latin_ratio(stripped) > 0.6:
            return stripped
        return None
    return line

def clean_text(text):
    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or NOISE_RE.search(line):
            continue
        line = _strip_devanagari_line(line)
        if line:
            lines.append(line)
    return "\n".join(lines)

def _collapse(s):
    return re.sub(r"\s+", " ", s).strip()

def _drop_garbled_hi_tail(s):
    """If s ends with ' / <no-letter garbled fragment>', drop the fragment."""
    if " / " in s:
        head, _, tail = s.rpartition(" / ")
        if tail and not re.search(r"[A-Za-z]", tail):
            return head
    return s

def clean_question(qtext):
    q = _collapse(qtext)
    q = re.sub(r"^\d{1,3}\s*[.)]\s*", "", q)
    q = _drop_garbled_hi_tail(q)
    q = GARBLED_TAIL.sub("", q)
    return q.strip(" ?")

def clean_option(otext):
    o = _collapse(otext)
    o = _drop_garbled_hi_tail(o)
    o = GARBLED_TAIL.sub("", o)
    return o.strip(" /-|,")

# ---------------------------------------------------------------------------
# MCQ parsing
# ---------------------------------------------------------------------------
def _opt(cls):  # cls like "aA"
    return rf"(?:\(\s*[{cls}]\s*\)|[{cls}]\s*[.)])\s*"

def _qpat(optfn):
    return re.compile(
        r"(?ms)^\s*(\d{1,3})\s*[.)]\s*(.*?)\s*"
        + optfn(0) + r"(.*?)\s*"
        + optfn(1) + r"(.*?)\s*"
        + optfn(2) + r"(.*?)\s*"
        + optfn(3) + r"(.*?)\s*"
        + r"(?=^\s*\d{1,3}\s*[.)]|\Z)"
    )

_LETTER_OPT = _qpat(lambda i: _opt("aAbBcCdD"[2 * i:2 * i + 2]))
_NUM_OPT = _qpat(lambda i: _opt("1234"[i]))

def parse_questions(clean, src):
    results = []
    for pat in (_LETTER_OPT, _NUM_OPT):
        for m in pat.finditer(clean):
            _num, qtext, oa, ob, oc, od = m.groups()
            q = clean_question(qtext)
            opts = [clean_option(x) for x in (oa, ob, oc, od)]
            if len(q) < 8 or not all(opts):
                continue
            # guard: an "option" that is actually a long question sentence = mis-parse
            if any(len(o) > 70 and o.lower().startswith(("what ", "which ", "how ", "the ", "a ", "an ", "in ", "is ")) for o in opts):
                continue
            results.append({"q_en": q, "opts_en": opts, "src": src})
        if results:
            break
    return results

def extract_questions(pdf_path, verbose=False):
    src = os.path.basename(pdf_path)
    raw = get_text(pdf_path)
    clean = clean_text(raw)
    qs = parse_questions(clean, src)
    if verbose:
        print(f"  {src}: {len(qs)} questions extracted")
    return qs

if __name__ == "__main__":
    import sys
    for path in sys.argv[1:]:
        qs = extract_questions(path, verbose=True)
        for i, q in enumerate(qs[:4], 1):
            print(f"   Q{i}: {q['q_en'][:90]}")
            for j, o in enumerate(q["opts_en"]):
                print(f"      ({'ABCD'[j]}) {o[:60]}")
