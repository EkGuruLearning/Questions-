# -*- coding: utf-8 -*-
"""
cn_build_topic.py — build one topic's bilingual PDF + Markdown from its data file.

Usage:
    python tools/cn_build_topic.py <topic_num>        # e.g. 1 .. 7
    python tools/cn_build_topic.py --all              # rebuild every topic that has data

Reads:
    tools/data/topic<N>_data.py      -> SECTIONS (curated, verified)
    tools/data/topic<N>_pending.py   -> PENDING (auto-ingested, needs review) [optional]
Writes (into Computer Network/):
    Topic N - <title> - <count> MCQs (Answers + Nukte).pdf
    Topic N - <title> - <count> MCQs (Answers + Nukte).md
"""
import os, sys, importlib.util, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import cn_engine
from cn_taxonomy import TOPICS, topic_by_num

DATA_DIR = os.path.join(HERE, "data")
OUT_DIR = os.path.join(ROOT, "Computer Network")

def _load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def _slug(title):
    s = re.sub(r"[^A-Za-z0-9]+", " ", title).strip()
    return s

def load_topic(topic_num):
    t = topic_by_num(topic_num)
    if not t:
        raise SystemExit(f"Unknown topic number {topic_num}")
    data_path = os.path.join(DATA_DIR, f"topic{topic_num}_data.py")
    if not os.path.exists(data_path):
        raise SystemExit(f"No data file for topic {topic_num}: {data_path}")
    m = _load_module(data_path, f"topic{topic_num}_data")
    sections = m.SECTIONS
    pend_path = os.path.join(DATA_DIR, f"topic{topic_num}_pending.py")
    pending = []
    if os.path.exists(pend_path):
        pm = _load_module(pend_path, f"topic{topic_num}_pending")
        pending = getattr(pm, "PENDING", [])
    return t, sections, pending

def build_one(topic_num, verbose=True):
    t, sections, pending = load_topic(topic_num)
    n_q = sum(len(s["questions"]) for s in sections)
    if n_q == 0 and pending:
        base = f"Topic {topic_num} - {_slug(t.get('short', t['title']))} - {len(pending)} Pending Questions (Needs Verification)"
    else:
        base = f"Topic {topic_num} - {_slug(t.get('short', t['title']))} - {n_q} MCQs (Answers + Nukte)"
    pdf_path = os.path.join(OUT_DIR, base + ".pdf")
    md_path = os.path.join(OUT_DIR, base + ".md")
    pages = cn_engine.build_pdf(topic_num, t["title"], sections, pending, pdf_path)
    cn_engine.build_markdown(topic_num, t["title"], sections, pending, md_path)
    if verbose:
        print(f"Topic {topic_num} — {t['title']}")
        print(f"  questions: {n_q} (+{len(pending)} pending) | pages: {pages}")
        print(f"  PDF: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
        print(f"  MD : {md_path} ({os.path.getsize(md_path)} bytes)")
    return pdf_path, md_path

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    args = sys.argv[1:]
    if not args:
        print(__doc__); return
    if args[0] == "--all":
        for t in TOPICS:
            p = os.path.join(DATA_DIR, f"topic{t['num']}_data.py")
            if os.path.exists(p):
                build_one(t["num"])
            else:
                print(f"Topic {t['num']}: no data file yet, skipping")
        return
    for a in args:
        build_one(int(a))

if __name__ == "__main__":
    main()
