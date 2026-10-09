# -*- coding: utf-8 -*-
"""
cn_parse_cnp3.py — parse cnp3/MCQ RST question banks (Bonaventure textbook).

Format per question:
    .. question:: <id>
       :nb_prop: N
       :nb_pos: M
       <question text>
       .. positive:: <correct statement>
       .. negative:: <wrong statement>

Converts ONLY clean single-answer questions with exactly 4 statements
(1 positive + 3 negative) into pending-style dicts; the 4 statements become
options A–D. Everything else is counted but skipped (kept as reference source).

Output: tools/data/cnp3_parsed.py with PARSED=[{src,q_en,opts_en,topic,subtopic}]
"""
import os
import re
import glob

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK = os.path.join(REPO, "Computer Network", "Past Papers", "Question Banks",
                    "cnp3-MCQ (Kurose-Bonaventure textbook)")

FILE_TOPIC = {
    "mcq-app.rst": (6, "Application Layer Protocols"),
    "mcq-bgp.rst": (6, "Routing Protocols (RIP/OSPF/BGP)"),
    "mcq-congestion.rst": (6, "Congestion Control"),
    "mcq-ipv6.rst": (3, "IPv6 Addressing"),
    "mcq-network-ftable.rst": (6, "Forwarding & Routing"),
    "mcq-network-pftables.rst": (6, "Forwarding & Routing"),
    "mcq-network-shortest.rst": (6, "Forwarding & Routing"),
    "mcq-network-vc.rst": (6, "Forwarding & Routing"),
    "mcq-network.rst": (6, "Network Layer & IPv4"),
    "mcq-reliability.rst": (6, "Flow & Error Control"),
    "mcq-sharing.rst": (6, "Multiple Access (ALOHA/CSMA)"),
    "mcq-transport.rst": (6, "Transport Layer (TCP/UDP)"),
}


def parse_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    base = os.path.basename(path)
    topic, sub = FILE_TOPIC.get(base, (6, "General"))
    items = []
    stats = {"total": 0, "clean4": 0, "skipped": 0}
    # split into question blocks
    blocks = re.split(r"(?m)^.. question:: ", text)[1:]
    for b in blocks:
        stats["total"] += 1
        lines = b.splitlines()
        qid = lines[0].strip()
        body = "\n".join(lines[1:])
        # statements
        stmts = re.findall(r"(?m)^\s*\.\. (positive|negative)::\s*(.+?)\s*$", body)
        # question text = lines before first statement directive
        first = re.search(r"(?m)^\s*\.\. (positive|negative)::", body)
        qtext = body[:first.start()] if first else body
        # strip directive option lines (:nb_prop: etc.)
        qtext = re.sub(r"(?m)^\s*:[a-z_]+:.*$", "", qtext)
        qtext = re.sub(r"\s+", " ", qtext).strip()
        qtext = re.sub(r"^[\s:|.-]+", "", qtext)
        pos = [s for kind, s in stmts if kind == "positive"]
        neg = [s for kind, s in stmts if kind == "negative"]
        if len(stmts) == 4 and len(pos) == 1 and qtext:
            opts = [pos[0] + " (Correct)" ]  # placeholder, fix below
            # options: correct + 3 wrong in original order
            ordered = [s for _, s in stmts]
            ans = ordered.index(pos[0])
            items.append({
                "src": "cnp3 MCQ (Bonaventure CN textbook), %s" % qid,
                "q_en": qtext if qtext.endswith(("?", ".", ":")) else qtext + ".",
                "opts_en": [re.sub(r"\s+", " ", s).strip() for s in ordered],
                "ans": ans,
                "topic": topic,
                "subtopic": sub,
            })
            stats["clean4"] += 1
        else:
            stats["skipped"] += 1
    return items, stats


def main():
    all_items = []
    print("file                          total clean4 skipped")
    for path in sorted(glob.glob(os.path.join(BANK, "mcq-*.rst"))):
        items, stats = parse_file(path)
        all_items.extend(items)
        print("%-28s %5d %6d %7d" % (os.path.basename(path), stats["total"],
                                     stats["clean4"], stats["skipped"]))
    out = os.path.join(REPO, "tools", "data", "cnp3_parsed.py")
    with open(out, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Auto-parsed single-answer MCQs from cnp3/MCQ RST banks (Bonaventure textbook)."""\n\n')
        f.write("PARSED = ")
        f.write(repr(all_items))
        f.write("\n")
    print("TOTAL parsed: %d -> %s" % (len(all_items), out))


if __name__ == "__main__":
    main()
