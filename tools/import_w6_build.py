# -*- coding: utf-8 -*-
"""
import_w6_build.py — Bulk import of ALL `Computer Network/new/` compiled-bank questions.

User instruction (2026-10-14): add ALL questions from the 23 new/ PDFs (900+), zero
repeats, verified answers -> normal; unverified -> CAUTION note in nukte.

Pipeline:
  1. /tmp/newbank_raw.json  (1008 candidates from 21 PDFs, already extracted)
  2. Parser #2 for the 2 remaining PDFs (Computer-Network-MCQ.pdf, networkmcq.pdf)
  3. Dedupe: internal + vs 817 bank. Drop ONLY true repeats:
       exact stem  OR  (overlap>=0.75 AND same answer)  OR  overlap>=0.90
     (concept repetition / same-topic different-demand questions are KEPT)
  4. Topic classify (keyword scoring) -> emit tools/data/w6_bank.py lists
     P{n}_{lastsec}_X9xx  (auto-picked by the existing *_X loaders)

Every imported record carries a nukte CAUTION: answer NOT verified (source key).
"""
import json, os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEW = os.path.join(ROOT, "Computer Network", "new")
DATA = os.path.join(ROOT, "tools", "data")
RAW = "/tmp/newbank_raw.json"

CAUTION_EN = ("⚠ CAUTION — answer NOT verified: compiled-bank source key = ({}). "
              "Please verify before relying.")
CAUTION_HI = ("⚠ सावधान — उत्तर verify नहीं है: source key = ({})। "
              "कृपया उपयोग से पहले स्वयं जाँच कर लें।")

FILL = set("which of the following is a an in are and to or be its with for that it the what "
           "who when how of in is a not the one".split())

def clean_text(s):
    s = re.sub(r"\s+", " ", s or "")
    s = re.sub(r"#\s*View all MCQ'?s? at McqMate\.co[m]?", "", s, flags=re.I)
    s = re.sub(r"View all MCQ'?s? at McqMate\.co[m]?", "", s, flags=re.I)
    s = re.sub(r"View Answers?.*$", "", s, flags=re.I)
    s = re.sub(r"\s*#\s*$", "", s)
    return s.strip(" .;,-")

def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", (s or "").lower())).strip()

def toks(s):
    return set(norm(s).split()) - FILL

def anstext(rec):
    a = rec.get("ans_idx", rec.get("ans"))
    if isinstance(a, str):
        a = "abcd".index(a.strip().lower()[0])
    opts = rec["opts"]
    return norm(opts[a]) if isinstance(opts[a], str) else norm(opts[a][0])

# ---------------------------------------------------------------- parser #2
Q_SPLIT = re.compile(r"(?m)^\s*(\d{1,3})\s*[.)]\s+")
OPT_RE = re.compile(r"(?:\s|^)\(?([a-dA-D])\)[.\s)]|(?:\s|^)([a-dA-D])\.\s+")
KEY_A = re.compile(r"(?m)^\s*(\d{1,3})\s*\.\s*([a-dA-D])\s*\.?\s*$")
KEY_B = re.compile(r"(?m)^\s*(\d{1,3})\s*\.\s*\(?([a-dA-D])\)?[.\s]\s*\S")

def parse2(path):
    import fitz
    doc = fitz.open(path)
    txt = "\n".join(p.get_text() for p in doc).replace("\u00a0", " ")
    # ---- keys
    keys = {}
    for m in KEY_A.finditer(txt):
        keys[int(m.group(1))] = m.group(2).lower()
    # style-B keys only inside "Answers:" regions
    for am in re.finditer(r"(?i)answers?:", txt):
        region = txt[am.end():am.end() + 800]
        for m in KEY_B.finditer(region):
            keys.setdefault(int(m.group(1)), m.group(2).lower())
    # ---- questions
    parts = Q_SPLIT.split(txt)
    out = []
    for i in range(1, len(parts) - 1, 2):
        num, body = int(parts[i]), parts[i + 1]
        marks = list(OPT_RE.finditer(body))
        got = {}
        for j, m in enumerate(marks):
            letter = (m.group(1) or m.group(2)).lower()
            if letter in got:
                continue
            start = m.end()
            end = marks[j + 1].start() if j + 1 < len(marks) else len(body)
            got[letter] = body[start:end].strip()
        if sorted(got) != ["a", "b", "c", "d"]:
            continue
        stem = body[:marks[0].start()].strip()
        stem = re.sub(r"\s+", " ", stem)
        if len(stem) < 12:
            continue
        opts = [re.sub(r"\s+", " ", got[k]).strip(" .;") for k in "abcd"]
        if any(len(o) < 1 for o in opts):
            continue
        ans = keys.get(num)
        if ans not in "abcd":
            continue
        out.append(dict(stem=stem, opts=opts, ans=ans.upper()))
    return out

# ---------------------------------------------------------------- topic classify
TOPIC_KEYS = {
    1: ["topology", "bandwidth", "data communication", "data communication system", "throughput",
        "latency", "protocol", "architecture", "client-server", "client server", "peer",
        "arpanet", "network that connects", "network type", "internet", "www", "world wide web",
        "intranet", "extranet", "network model"],
    2: ["osi", "tcp/ip model", "encapsulation", "session layer", "presentation layer",
        "layer of the osi", "layer of osi", "seven layer", "seven-layer", "five layer",
        "open system interconnection", "data link layer", "network layer", "physical layer",
        "transport layer", "application layer"],
    3: ["ip address", "ip-address", "subnet", "ipv4", "ipv6", "mac address", "arp ", " arp",
        "rarp", "icmp", "dns", "dhcp", "port number", "port address", "cidr", "class a",
        "class b", "class c", "class d", "classful", "datagram", "fragment", "ttl", "ip header",
        "logical address", "physical address", "binary", "octet", "dotted", "ip addressing",
        "network address", "address resolution", "address mask", "supernet"],
    4: ["router", "switch", "bridge", "hub", "repeater", "gateway", "brouter", "broadcast domain",
        "collision domain", "vlan", "packet switching", "circuit switching"],
    5: ["fiber", "fibre", "coax", "twisted", "wireless", "cellular", "satellite", "sonet",
        "dsl", "modem", "transmission media", "transmission medium", "guided", "unguided",
        "radio", "microwave", "infrared", "multiplex", "fdm", "tdm", "wdm", "cable",
        "hfc", "telephone", "copper", "optical", "propagation", "antenna", "ethernet",
        "10base", "100base", "1000base", "cable", "bandwidth of"],
    6: ["tcp", "udp", "routing", "rip ", "ospf", "bgp", "congestion", "flow control",
        "error control", "arq", "stop-and-wait", "stop and wait", "sliding window", "http",
        "smtp", "ftp", "tftp", "socket", "checksum",
        "handshake", "window", "acknowledgment", "acknowledgement", "segmen", "qos", "reliable",
        "cookie", "web ", "browser"],
    7: ["security", "firewall", "encrypt", "decrypt", "cipher", "rsa", "des ", "aes",
        "authentic", "virus", "worm", "malware", "vpn", "ipsec", "ssl", "tls", "ids",
        "honeypot", "attack", "denial", "dos", "password", "certificate", "hash",
        "digital signature", "public key", "private key", "spoof", "phishing", "access control",
        "integrity", "confidentiality", "non-repudiation"],
}

SEC_PRIORITY = ["attack", "security", "encrypt", "dos", "malware", "virus", "firewall"]

def classify(stem, opts):
    s = (stem + " " + " ".join(opts)).lower()
    scores = {}
    for t, kws in TOPIC_KEYS.items():
        scores[t] = sum(1 for kw in kws if kw in s)
    if any(kw in s for kw in SEC_PRIORITY):
        scores[7] += 3
    best = max(scores.values())
    if best == 0:
        return 1
    for t in sorted(scores):
        if scores[t] == best:
            return t
    return 1

# ---------------------------------------------------------------- dedupe
def is_dup(a, b_ta, b_ans, seen_exact, seen_toks):
    """True if candidate a repeats an existing question."""
    ns = norm(a["stem"])
    if ns in seen_exact:
        return "exact"
    ta = toks(a["stem"])
    if len(ta) >= 3:
        for tb, ansb, stemkey in seen_toks:
            if len(tb) < 3:
                continue
            ov = len(ta & tb) / min(len(ta), len(tb))
            if ov >= 0.90:
                return "near90"
            if ov >= 0.75 and (anstext(a) == ansb or anstext(a) in ansb or ansb in anstext(a)):
                return "near-same-ans"
    return None

def main():
    pool = json.load(open(RAW))
    n_raw = len(pool)

    # parser #2
    p2 = []
    for f, label in [("Computer-Network-MCQ.pdf", "Computer-Network-MCQ.pdf (new/ 2026 drop)"),
                     ("networkmcq.pdf", "networkmcq — GDC Ramban solved MCQ (new/ 2026 drop)")]:
        path = os.path.join(NEW, f)
        if os.path.exists(path):
            got = parse2(path)
            for r in got:
                r["file"] = label
            p2.extend(got)
            print(f"parser2 {f}: {len(got)} questions")

    allc = pool + p2
    # normalize opts to list[str]; ans to letter
    clean = []
    for r in allc:
        opts = [clean_text(o if isinstance(o, str) else o[0]) for o in r["opts"]]
        ans = r["ans"].strip().upper()[:1]
        if len(opts) != 4 or ans not in "ABCD":
            continue
        if len(set(o.lower() for o in opts)) < 4:
            continue
        stem = clean_text(r["stem"])
        if len(stem) < 12:
            continue
        clean.append(dict(file=r["file"], stem=stem, opts=opts, ans=ans))
    print(f"clean pool: {len(clean)} (raw {n_raw} + parser2 {len(p2)})")

    # ---- bank for dup check
    bank = json.load(open(os.path.join(ROOT, "Computer Network", "data", "cn_questions.json")))["questions"]
    seen_exact = set()
    seen_toks = []   # (toks, anstext, stem)
    W6_PAT = re.compile(r"McqMate|DCN_MCQ|Computer-Network-MCQ|networkmcq|"
                        r"computer-networks \[set |\(new/ 2026 drop\)", re.I)
    for q in bank:
        if W6_PAT.search(q.get("source_url_or_file") or ""):
            continue   # w6 records themselves (re-run safety)
        seen_exact.add(norm(q["stem_en"]))
        i = ord(q["correct_option"]) - 65
        seen_toks.append((toks(q["stem_en"]), norm(q["options_en"][i]), q["stem_en"]))

    kept = []
    counts = {"exact": 0, "near90": 0, "near-same-ans": 0}
    for r in clean:
        d = is_dup(r, None, None, seen_exact, seen_toks)
        if d:
            counts[d] += 1
            continue
        kept.append(r)
        seen_exact.add(norm(r["stem"]))
        seen_toks.append((toks(r["stem"]), anstext(r), r["stem"]))
    print(f"dropped as repeats: {counts}  -> kept NEW: {len(kept)}")

    # ---- classify + chunk per topic
    SEC = {1: "G", 2: "D", 3: "E", 4: "D", 5: "C", 6: "E", 7: "C"}
    for r in kept:
        r["topic"] = classify(r["stem"], r["opts"])
    per = {}
    for r in kept:
        per.setdefault(r["topic"], []).append(r)

    # ---- agent verdicts (tools/data/w6_verdicts.py)
    try:
        import importlib.util as _iu
        vspec = _iu.spec_from_file_location("w6_verdicts", os.path.join(DATA, "w6_verdicts.py"))
        vmod = _iu.module_from_spec(vspec); vspec.loader.exec_module(vmod)
        VERD = vmod.VERDICTS
    except Exception:
        VERD = {}
    vstat = {"ok": 0, "fix": 0, "claim": 0, "unseen": 0}

    lines = ["# -*- coding: utf-8 -*-",
             '"""w6_bank.py — AUTO-GENERATED by tools/import_w6_build.py.',
             "All usable questions from Computer Network/new/ compiled banks (2026 drop).",
             "Zero repeats (exact + near-same-answer vs bank + internal).",
             "Unverified answers carry the ⚠ CAUTION banner in nukte;",
             "agent-verified batches come from tools/data/w6_verdicts.py.",
             '"""',
             ""]
    total = 0
    for t in sorted(per):
        recs = per[t]
        sec = SEC[t]
        ck = 1
        for i in range(0, len(recs), 60):
            part = recs[i:i + 60]
            name = f"P{t}_{sec}_X9{ck:02d}"
            lines.append(f"{name} = [")
            for ix, r in enumerate(part):
                src = f"Repo: {r['file']}"
                if "new/ 2026 drop" not in src:
                    src += " (new/ 2026 drop)"
                opts = "[" + ", ".join(f"[{json.dumps(o, ensure_ascii=False)}, \"\"]" for o in r["opts"]) + "]"
                ans_idx = "abcd".index(r["ans"].lower())
                verdict = (VERD.get(name) or {}).get(ix)
                if verdict and verdict[0] == "ok":
                    vstat["ok"] += 1
                    if len(verdict) >= 3:
                        nk = "[" + json.dumps(verdict[1], ensure_ascii=False) + ", " + \
                             json.dumps(verdict[2], ensure_ascii=False) + "]"
                    else:
                        nk = '["✓ Agent-verified (Oct 2026): source key confirmed.", "✓ agent-verified: key सही।"]'
                elif verdict and verdict[0] == "fix":
                    vstat["fix"] += 1
                    ans_idx = verdict[1]
                    nk = "[" + json.dumps(verdict[2], ensure_ascii=False) + ", " + \
                         json.dumps(verdict[3], ensure_ascii=False) + "]"
                elif verdict and verdict[0] == "claim":
                    vstat["claim"] += 1
                    nk = "[" + json.dumps(CAUTION_EN.format(r["ans"]), ensure_ascii=False) + ", " + \
                         json.dumps(CAUTION_HI.format(r["ans"]), ensure_ascii=False) + "]"
                else:
                    vstat["unseen"] += 1
                    nk = "[" + json.dumps(CAUTION_EN.format(r["ans"]), ensure_ascii=False) + ", " + \
                         json.dumps(CAUTION_HI.format(r["ans"]), ensure_ascii=False) + "]"
                lines.append(f" ({json.dumps(src, ensure_ascii=False)},")
                lines.append(f"  {json.dumps(r['stem'], ensure_ascii=False)}, \"\",")
                lines.append(f"  {opts},")
                lines.append(f"  {ans_idx}, [\"\", \"\"], {nk}, {{}}),")
                total += 1
            lines.append("]")
            lines.append("")
            ck += 1
        print(f"  topic {t}: {len(recs)} recs -> P{t}_{sec}_X9*")
    out = os.path.join(DATA, "w6_bank.py")
    open(out, "w").write("\n".join(lines))
    print(f"WROTE {out}: {total} records | verdicts: {vstat}")

    # report
    with open(os.path.join(ROOT, "Computer Network", "Reports", "W6_IMPORT_LOG.md"), "w") as f:
        f.write("# W6 bulk import log (new/ compiled banks)\n\n")
        f.write(f"- Raw pool (21 PDFs): {n_raw}\n- Parser-2 (2 PDFs): {len(p2)}\n")
        f.write(f"- Clean (4 opts + key + non-trivial): {len(clean)}\n")
        f.write(f"- Dropped repeats: {counts}\n- **Imported: {total}**\n\n")
        f.write(f"## Agent verification verdicts\n\n{vstat}\n\n")
        f.write("- `ok`/`fix` = agent-verified (caution removed; `fix` = source key corrected).\n")
        f.write("- `claim`/`unseen` = ⚠ CAUTION banner stays (answer NOT verified).\n\n")
        f.write("Zero-repeat policy: exact stem / >=0.90 overlap / >=0.75+same answer = dropped.\n")

if __name__ == "__main__":
    main()
