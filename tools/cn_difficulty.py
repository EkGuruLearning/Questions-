# -*- coding: utf-8 -*-
"""Question difficulty classifier + section ordering (user spec).

Within each syllabus section, questions are ordered Easy -> Medium -> Hard
(jaise "MAC ka easy, MAC ka medium, MAC ka hard").

Exam-level base (user's grouping):
- Easy exams  (SSC MTS/CHSL, REET, SCI, BCI, TCS/Wipro/Infosys...) -> base 0
- Hard exams  (GATE, UGC NET, KVS, EMRS, DSSSB, JNV, RPSC Programmer,
  PGT, Lecturer, UPSC) -> base 2
- Everything else (Forouzan, cnp3, SSC CGL, RRB, RSMSSB, HTET, IBPS/SBI,
  NIELIT, unit tests, web banks...) -> base 1

Content bump (+1): numerics/computation, negative stems (NOT/except/false),
multi-statement analysis. Clamped to 0..2.
"""
import re

DIFF_LABEL = ("Easy", "Medium", "Hard")

_EASY = re.compile(r"\b(MTS|CHSL|REET|SCI|BCI|TCS|Wipro|Infosys|TNPSC|Clerk|"
                   r"Constable|OSSC|Police|CTET|REET)\b", re.I)
_HARD = re.compile(r"\b(GATE|NET|KVS|EMRS|DSSSB|JNV|PGT|Lecturer|UPSC|"
                   r"Assistant Professor|Programmer)\b", re.I)

_NUM = re.compile(
    r"(\b\d+(\.\d+)?\s*(bps|kbps|mbps|gbps|hz|khz|mhz|ms|sec|second|seconds|byte|"
    r"bytes|bit|bits|km|metre|meters?|baud|%|frames?)\b)|"
    r"(how many|calculate|minimum (frame|time|number|bits)|bit rate|baud rate|"
    r"total length|fragment|subnet|cidr|sequence number)",
    re.I)
_NEG = re.compile(r"\b(NOT|not|except|incorrect|false|wrong|galat)\b")
_ANA = re.compile(r"(statements?|both|neither|all of|only I|match|respectively)", re.I)


def q_diff(q):
    """Return 0 (Easy), 1 (Medium) or 2 (Hard) for a question dict."""
    src = str(q.get("src", ""))
    text = str(q.get("q", ["", ""])[0]) + " " + " ".join(
        str(o[0]) for o in q.get("opts", []))
    if _EASY.search(src):
        base = 0
    elif _HARD.search(src):
        base = 2
    else:
        base = 1
    bump = 0
    if _NUM.search(text):
        bump += 1
    if _NEG.search(text):
        bump += 1
    if _ANA.search(text):
        bump += 1
    return max(0, min(2, base + min(bump, 1)))


def sort_questions(questions):
    """Stable Easy -> Medium -> Hard ordering."""
    return sorted(questions, key=q_diff)
