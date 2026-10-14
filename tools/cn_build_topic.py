# -*- coding: utf-8 -*-
"""
cn_build_topic.py — build one topic's bilingual PDF + Markdown from its data file.

Usage:
    python tools/cn_build_topic.py <topic_num>        # e.g. 1 .. 7
    python tools/cn_build_topic.py --all              # rebuild every topic that has data

Reads:
    tools/data/topic<N>_data.py      -> SECTIONS (curated, verified) + optional NUKTE_RAPID
    tools/data/topic<N>_pending.py   -> PENDING (auto-ingested) [optional, legacy]
Writes:
    content/computer-network/theory/T0N-<slug>-Theory-MCQ.pdf   (student material)
    maintainer/computer-network/theory-md/T0N-<slug>-Theory-MCQ.md  (editable source)
"""
import os, sys, importlib.util, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import cn_engine
from cn_taxonomy import TOPICS, topic_by_num

DATA_DIR = os.path.join(HERE, "data")
OUT_DIR = os.path.join(ROOT, "content", "computer-network", "theory")
MD_DIR = os.path.join(ROOT, "maintainer", "computer-network", "theory-md")
# Topic number -> file-name slug used by data/catalog/materials.json
SLUGS = {
    1: "T01-Introduction-to-Data-Communication",
    2: "T02-Network-Models-OSI-TCP-IP",
    3: "T03-Addressing-MAC-IPv4-IPv6-Port-DNS",
    4: "T04-Networking-Devices",
    5: "T05-Transmission-Medium",
    6: "T06-OSI-Layers-in-Detail",
    7: "T07-Network-Security",
}

def _load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    try:
        import cn_textfix
        cn_textfix.normalize_module(m)
    except Exception:
        pass
    return m

def _slug(title):
    return re.sub(r"[^A-Za-z0-9]+", " ", title).strip()

def load_topic(topic_num):
    t = topic_by_num(topic_num)
    if not t:
        raise SystemExit(f"Unknown topic number {topic_num}")
    data_path = os.path.join(DATA_DIR, f"topic{topic_num}_data.py")
    if not os.path.exists(data_path):
        raise SystemExit(f"No data file for topic {topic_num}: {data_path}")
    m = _load_module(data_path, f"topic{topic_num}_data")
    sections = m.SECTIONS
    rapid = getattr(m, "NUKTE_RAPID", [])
    pend_path = os.path.join(DATA_DIR, f"topic{topic_num}_pending.py")
    pending = []
    if os.path.exists(pend_path):
        pm = _load_module(pend_path, f"topic{topic_num}_pending")
        pending = getattr(pm, "PENDING", [])
    return t, sections, pending, rapid

def build_one(topic_num, verbose=True):
    t, sections, pending, rapid = load_topic(topic_num)
    n_q = sum(len(s["questions"]) for s in sections)
    base = SLUGS.get(topic_num, f"T{topic_num:02d}-{_slug(t.get('short', t['title']))}") + "-Theory-MCQ"
    if n_q == 0 and pending:
        base = SLUGS.get(topic_num, f"T{topic_num:02d}") + "-Pending-Questions"
    pdf_path = os.path.join(OUT_DIR, base + ".pdf")
    md_path = os.path.join(MD_DIR, base + ".md")
    pages = cn_engine.build_pdf(topic_num, t["title"], sections, pending, pdf_path, nukte_rapid=rapid)
    cn_engine.build_markdown(topic_num, t["title"], sections, pending, md_path, nukte_rapid=rapid)
    if verbose:
        print(f"Topic {topic_num} — {t['title']}")
        print(f"  questions: {n_q} (+{len(rapid)} rapid) (+{len(pending)} pending) | pages: {pages}")
        print(f"  PDF: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
        print(f"  MD : {md_path} ({os.path.getsize(md_path)} bytes)")
    return pdf_path, md_path

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(MD_DIR, exist_ok=True)
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
