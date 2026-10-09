# -*- coding: utf-8 -*-
"""
cn_parse_ocr.py — extract questions from OCR texts of the 5 scanned PDFs
(Random Test Rajasthan PYQ + 4 solution-slide sets).

Each question: rough question-text + up to 4 English options (Hindi after '/'
dropped). Noise lines removed. Items are deduped against ALL existing questions
using an alnum-only key (OCR drops spaces: 'DataEntry Office' vs 'Data Entry
Office'). Clean items (>=3 options, decent question text) are ingested into the
topic queues (T3-7 -> pending with ans/note when known; T1-2 -> holding).
Messer items are printed for hand review.

Usage: /home/user/pdfenv/bin/python tools/cn_parse_ocr.py [--dry-run]
"""
import os
import re
import sys
import importlib.util

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "tools"))
sys.path.insert(0, os.path.join(REPO, "tools", "data"))

import cn_taxonomy
from cn_pipeline import _norm_key
from answer_keys import RAJASTHAN_PYQ

OCR_DIR = os.path.join(REPO, "tools", "data", "ocr_text")

NOISE = re.compile(
    r"^(SUNIL YADAV SIR|9694473047|Question ?not ?attempted|INSTITUTE|COMPUTESCIENCE|"
    r"JTE'?FOR|FOR|COMPUTER ?SCIENCE|Analysis|Reset ?Attempt.*|S\.No\.|Name|Email|"
    r"Phone|Marks|Photo|View ?Analysis.*|\d{1,3}|[()a-eA-E)]+|[A-Z]{1,3}|"
    r"Computer|Nelwork|Network|Rajashan.*|Random Test|Deliveuy|Deliver.*)$",
    re.IGNORECASE,
)

# out-of-syllabus (Java / arithmetic from the mixed Unit-Tests) + leaderboard junk
JAVA = re.compile(
    r"\b(java|jdk|jvm|class name|constructor|inheritance|overrid|encapsulation|"
    r"object oriented|blueprint for a software|anonymous inner|\.java|this. operator|"
    r"instance variable|scope limited to a method|value of the expression|"
    r"compiling and|public types|overloaded constructor)\b", re.I)
JUNK = re.compile(r"(Date ?& ?Time|@gmail|View ?Analysis|Ashutosh|komal samariya|"
                  r"Topic Computer|Nelwork - Lnbeduehon|2# YADAV)", re.I)

OPT_LABEL = re.compile(r"^\s*[([(]?\s*([a-eA-E])\s*[).)\]]\s*(.+)$")
OPT_INLINE = re.compile(r"[([{]\s*([a-eA-E])\s*[).)\]]\s*")
PAGE_RE = re.compile(r"--- page (\d+) ---")


def alnum_key(text):
    return re.sub(r"[^a-z0-9]", "", str(text).lower())


def load_existing():
    def _load(path, name):
        spec = importlib.util.spec_from_file_location(name, path)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        return m

    keys = set()
    for n in range(1, 8):
        for fname in (f"topic{n}_data.py", f"topic{n}_pending.py", "web_extra_t1t2.py"):
            p = os.path.join(REPO, "tools", "data", fname)
            if not os.path.exists(p):
                continue
            m = _load(p, fname.replace(".py", ""))
            for sec in getattr(m, "SECTIONS", []):
                for q in sec["questions"]:
                    t = q["q"][0] if isinstance(q["q"], list) else q["q"]
                    keys.add(alnum_key(t))
            for q in list(getattr(m, "PENDING", [])) + list(getattr(m, "EXTRA", [])):
                keys.add(alnum_key(q["q_en"]))
    return keys


def parse_pages(text):
    pages = []
    parts = PAGE_RE.split(text)
    # parts: [pre, num, body, num, body...]
    for i in range(1, len(parts) - 1, 2):
        pages.append((int(parts[i]), parts[i + 1]))
    return pages


def clean_lines(body):
    out = []
    for ln in body.splitlines():
        s = ln.strip()
        if not s or NOISE.match(s):
            continue
        s = re.sub(r"\s+", " ", s)
        out.append(s)
    return out


def extract_items(pdf_stem, body, qnum_offset=None):
    """Best-effort: question text + options from one page body."""
    lines = clean_lines(body)
    if not lines:
        return []
    # drop leading pure-number lines (question number alone)
    qnum = None
    if lines and re.fullmatch(r"\d{1,3}", lines[0]):
        qnum = int(lines[0])
        lines = lines[1:]
    # find option start
    q_lines = []
    opt_start = None
    for i, ln in enumerate(lines):
        m = OPT_LABEL.match(ln)
        if m and len(ln) > 2:
            opt_start = i
            break
        if re.match(r"^[a-eA-E][).]\s+\S", ln):
            opt_start = i
            break
    if opt_start is None:
        # maybe options are label-less short lines after '?'
        for i, ln in enumerate(lines):
            if ln.rstrip().endswith("?") or ln.rstrip().endswith("-"):
                q_lines = lines[: i + 1]
                rest = [x for x in lines[i + 1:] if len(x) > 1][:4]
                if len(rest) >= 3 and q_lines:
                    return [(pdf_stem, qnum, " ".join(q_lines), rest)]
                return [(pdf_stem, qnum, " ".join(lines), [])]
        return [(pdf_stem, qnum, " ".join(lines), [])]
    q_lines = lines[:opt_start]
    # parse options
    opts = []
    cur = None
    for ln in lines[opt_start:]:
        m = OPT_LABEL.match(ln)
        if m and (not opts or len(ln) < 80 or m.group(1).lower() == "abcd"[len(opts):len(opts) + 1].lower()):
            if cur is not None:
                opts.append(cur)
            cur = re.sub(r"\s*/\s*.*$", "", m.group(2)).strip()  # drop Hindi after '/'
        elif cur is not None:
            # continuation
            cur = (cur + " " + re.sub(r"\s*/\s*.*$", "", ln)).strip()
        if len(opts) + (1 if cur else 0) >= 5:
            break
    if cur is not None and len(opts) < 4:
        opts.append(cur)
    opts = [o for o in opts if o][:4]
    qtext = " ".join(q_lines).strip()
    qtext = re.sub(r"\s+", " ", qtext)
    return [(pdf_stem, qnum, qtext, opts)]


def key2(text):
    t = re.sub(r"^\s*\d{1,3}\s*[.。)）]?\s*", "", str(text))
    return alnum_key(t)


def is_dup(k, exist_list):
    if k in existing_keys_cached:
        return True
    for ek in exist_list:
        if (len(k) > 30 and k[:30] in ek) or (len(ek) > 30 and ek[:30] in k):
            return True
    try:
        import difflib
        return bool(difflib.get_close_matches(k, exist_list, n=1, cutoff=0.68))
    except Exception:
        return False


existing_keys_cached = set()


def main():
    dry = "--dry-run" in sys.argv
    existing = load_existing()
    global existing_keys_cached
    existing_keys_cached = existing
    EXIST = list(existing)
    print("existing keys:", len(existing))

    files = [
        "Random Test- Rajasthan PYQ",
        "Subject Test Solution -1 (CN & Security)",
        "Subject Test Solution -1 (CN & Security) Part-2",
        "Unit Test -2 Solutions",
        "Unit Test-4 Solution",
    ]
    new_items = []   # (stem, qnum, qtext, opts, topic, sub, ans, note, pgno)
    for stem in files:
        p = os.path.join(OCR_DIR, stem + ".txt")
        if not os.path.exists(p):
            print("[miss]", stem)
            continue
        text = open(p, encoding="utf-8").read()
        pages = parse_pages(text)
        n_new = n_dup = n_bad = n_java = 0
        for pgno, body in pages:
            for stem2, qnum, qtext, opts in extract_items(stem, body):
                if len(qtext) < 15 or ("?" not in qtext and "-" not in qtext and len(qtext) < 25):
                    n_bad += 1
                    continue
                if JAVA.search(qtext) or JUNK.search(qtext):
                    n_java += 1
                    continue
                k = key2(qtext)
                if not k or is_dup(k, EXIST):
                    n_dup += 1
                    continue
                existing.add(k)
                EXIST.append(k)
                n_new += 1
                note = "OCR-parse staging: verify options/answer at curation (see src page)."
                if stem.startswith("Random") and qnum and qnum in RAJASTHAN_PYQ:
                    note = "Verified key: " + RAJASTHAN_PYQ[qnum]
                topic, sub = cn_taxonomy.classify(qtext + " " + " ".join(opts))
                if not topic:
                    topic, sub = (6, "General")
                new_items.append((stem, qnum, qtext, opts, topic, sub, None, note, pgno))
        print("%-45s pages=%d new=%d dup=%d bad=%d java/junk=%d" %
              (stem[:45], len(pages), n_new, n_dup, n_bad, n_java))

    clean = [x for x in new_items if x[4] and len(x[3]) >= 2]
    messy = [x for x in new_items if not (x[4] and len(x[3]) >= 2)]
    print("\nCLEAN new items:", len(clean), " MESSY (few/no opts, staged anyway):", len(messy))
    for x in messy:
        print("  [messy] %s p%d Q%s: %s | opts=%s" % (x[0][:25], x[8], x[1], x[2][:60], x[3]))
    for x in clean[:10]:
        print("  [clean] %s p%d Q%s: %s" % (x[0][:25], x[8], x[1], x[2][:70]))

    if dry:
        return
    # ingest ALL new items (messy ones staged with a warning note)
    additions = {n: [] for n in range(1, 8)}
    for stem, qnum, qtext, opts, topic, sub, ans, note, pgno in new_items:
        if len(opts) < 2:
            note = (note or "") + " OPTIONS INCOMPLETE in OCR — re-check source page."
        rec = {
            "src": "%s.pdf (OCR), p%d%s" % (stem, pgno, (" Q%s" % qnum) if qnum else ""),
            "q_en": qtext,
            "opts_en": opts,
            "topic": topic,
            "subtopic": sub,
            "note": note,
        }
        additions[topic].append(rec)
    for n in range(1, 8):
        recs = additions[n]
        if not recs:
            continue
        if n <= 2:
            hold_p = os.path.join(REPO, "tools", "data", "web_extra_t1t2.py")
            hold = []
            if os.path.exists(hold_p):
                spec = importlib.util.spec_from_file_location("h", hold_p)
                m = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(m)
                hold = list(m.EXTRA)
            hold.extend(recs)
            open(hold_p, "w", encoding="utf-8").write(
                "# -*- coding: utf-8 -*-\n"
                '"""Web/OCR-sourced MCQs for Topics 1-2 awaiting merge into the books (holding)."""\n\n'
                "EXTRA = " + repr(hold) + "\n")
            print("topic %d: +%d -> holding (total %d)" % (n, len(recs), len(hold)))
        else:
            pend_p = os.path.join(REPO, "tools", "data", "topic%d_pending.py" % n)
            spec = importlib.util.spec_from_file_location("p", pend_p)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            pend = list(m.PENDING) + recs
            open(pend_p, "w", encoding="utf-8").write(
                "# -*- coding: utf-8 -*-\n"
                '"""Auto-ingested questions for Topic %d — NEED VERIFICATION."""\n\n' % n
                + "PENDING = " + repr(pend) + "\n")
            print("topic %d: +%d -> pending (total %d)" % (n, len(recs), len(pend)))


if __name__ == "__main__":
    main()
