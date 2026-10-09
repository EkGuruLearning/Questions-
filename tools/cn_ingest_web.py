# -*- coding: utf-8 -*-
"""
cn_ingest_web.py — merge web-sourced + cnp3-parsed MCQs into the topic queues.

* Dedupe against ALL existing questions (topic1-7 data + pending) via
  cn_pipeline._norm_key (question-text normalisation).
* Classify via cn_taxonomy.classify (content-based); an explicit topic_hint
  from the source file wins only when the classifier finds no keyword match.
* Topics 3-7  -> append to tools/data/topicN_pending.py (keeps `ans`/`note`).
* Topics 1-2  -> tools/data/web_extra_t1t2.py (HOLDING: books are under user
  review; items merge into the books at the next T1/T2 update pass).

Usage: /home/user/pdfenv/bin/python tools/cn_ingest_web.py
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

# hand overrides when the keyword classifier has no match:
# norm_key(question) -> (topic_num, subtopic_name)
HAND_TOPIC = {
    _norm_key("A distributed network configuration in which all data/information passes through a central computer is"):
        (1, "Network Structure / Topology"),
    _norm_key("Which of the following is a benefit of networking?"):
        (1, "General Network Basics"),
}


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def existing_keys():
    keys = set()
    hold_p = os.path.join(REPO, "tools", "data", "web_extra_t1t2.py")
    if os.path.exists(hold_p):
        for q in _load(hold_p, "web_extra_t1t2").EXTRA:
            keys.add(_norm_key(q["q_en"]))
    for n in range(1, 8):
        for fname in (f"topic{n}_data.py", f"topic{n}_pending.py"):
            p = os.path.join(REPO, "tools", "data", fname)
            if not os.path.exists(p):
                continue
            m = _load(p, fname.replace(".py", ""))
            for sec in getattr(m, "SECTIONS", []):
                for q in sec["questions"]:
                    keys.add(_norm_key(q["q"][0] if isinstance(q["q"], list) else q["q"]))
            for q in getattr(m, "PENDING", []):
                keys.add(_norm_key(q["q_en"]))
    return keys


def main():
    web = _load(os.path.join(REPO, "tools", "data", "web_pyq_raw.py"), "web_pyq_raw").WEB_PYQ
    cnp3 = _load(os.path.join(REPO, "tools", "data", "cnp3_parsed.py"), "cnp3_parsed").PARSED

    seen = existing_keys()
    print("existing unique questions:", len(seen))

    additions = {n: [] for n in range(1, 8)}
    skipped_dup = 0
    for item in list(web) + list(cnp3):
        k = _norm_key(item["q_en"])
        if k in seen:
            skipped_dup += 1
            print("  [dup] %s — %s" % (item["src"][:40], item["q_en"][:55]))
            continue
        seen.add(k)
        topic, sub = cn_taxonomy.classify(item["q_en"] + " " + " ".join(item["opts_en"]))
        if not topic:
            topic, sub = HAND_TOPIC.get(_norm_key(item["q_en"]), (None, None))
        if not topic and item.get("topic"):
            topic, sub = item["topic"], item.get("subtopic", "General")
        if not topic:
            print("  [no-topic] %s — %s" % (item["src"][:40], item["q_en"][:60]))
            continue
        rec = {
            "src": item["src"],
            "q_en": item["q_en"],
            "opts_en": item["opts_en"],
            "topic": topic,
            "subtopic": sub,
        }
        if "ans" in item:
            rec["ans"] = item["ans"]
        if item.get("note"):
            rec["note"] = item["note"]
        if "ans" in item and item.get("ans_src"):
            rec["ans_src"] = item["ans_src"]
        additions[topic].append(rec)

    for n in range(1, 8):
        recs = additions[n]
        if not recs:
            continue
        if n <= 2:
            # holding file for T1/T2 (books under review)
            hold_p = os.path.join(REPO, "tools", "data", "web_extra_t1t2.py")
            existing_hold = []
            if os.path.exists(hold_p):
                existing_hold = _load(hold_p, "web_extra_t1t2").EXTRA
            existing_hold.extend(recs)
            with open(hold_p, "w", encoding="utf-8") as f:
                f.write("# -*- coding: utf-8 -*-\n")
                f.write('"""Web-sourced MCQs for Topics 1-2 awaiting merge into the books (holding)."""\n\n')
                f.write("EXTRA = ")
                f.write(repr(existing_hold))
                f.write("\n")
            print("topic %d: +%d -> web_extra_t1t2.py (total %d)" % (n, len(recs), len(existing_hold)))
        else:
            pend_p = os.path.join(REPO, "tools", "data", "topic%d_pending.py" % n)
            pm = _load(pend_p, "topic%d_pending" % n)
            pend = list(pm.PENDING) + recs
            with open(pend_p, "w", encoding="utf-8") as f:
                f.write("# -*- coding: utf-8 -*-\n")
                f.write('"""Auto-ingested questions for Topic %d — NEED VERIFICATION."""\n\n' % n)
                f.write("PENDING = ")
                f.write(repr(pend))
                f.write("\n")
            print("topic %d: +%d -> pending (total %d)" % (n, len(recs), len(pend)))
    print("skipped as duplicate:", skipped_dup)
    print("new added:", sum(len(v) for v in additions.values()))


if __name__ == "__main__":
    main()
