# -*- coding: utf-8 -*-
"""cn_export_json.py — normalized question-bank export + audit reports.

Spec: Computer Network/new/README.md (master execution prompt, §6 schema).
Outputs (all under Computer Network/):
  data/cn_questions.json            — normalized bank, stable IDs, full schema
  Reports/INVENTORY.md              — question inventory
  Reports/DUPLICATE_AUDIT.md        — exact + near-duplicate candidates
  Reports/ANSWER_VERIFICATION.md    — honest verification status counts
  Reports/SOURCE_REGISTER.md        — classification rules + evidence files

Honesty rules (spec §8, §10): source labels are classified, never upgraded
without evidence; never claim 100% verified.
"""
import importlib.util
import json
import os
import re
import sys
import hashlib
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(HERE, "data")
CN = os.path.join(ROOT, "Computer Network")
OUT_DATA = os.path.join(CN, "data")
OUT_REP = os.path.join(CN, "Reports")
sys.path.insert(0, HERE)
import cn_textfix  # noqa: E402
import cn_difficulty  # noqa: E402
import audit_duplicates  # noqa: E402

TOPICS = {
    1: ("T01", "Introduction of Data Communication"),
    2: ("T02", "Network Models (OSI & TCP/IP)"),
    3: ("T03", "Addressing (MAC, IPv4, IPv6, Port, DNS)"),
    4: ("T04", "Networking Devices"),
    5: ("T05", "Transmission Medium"),
    6: ("T06", "OSI Layers in Detail"),
    7: ("T07", "Network Security"),
}
LETTERS = "ABCD"

# ---- evidence files actually present in the repo (paper + key) ----
OFFICIAL_EVIDENCE_PATH = os.path.join(ROOT, "data", "sources", "official_paper_key_evidence.json")


def load_official_evidence_ids():
    """Only explicitly audited, question-level official paper+final-key links count."""
    if not os.path.exists(OFFICIAL_EVIDENCE_PATH):
        return set()
    with open(OFFICIAL_EVIDENCE_PATH, encoding="utf-8") as f:
        evidence = json.load(f)
    ids = set()
    for record in evidence.get("records", []):
        paper = record.get("official_paper") or {}
        key = record.get("official_final_key") or {}
        if not (paper.get("url") or paper.get("file")):
            continue
        if not (key.get("url") or key.get("file")):
            continue
        ids.update(record.get("question_ids", []))
    return ids


OFFICIAL_EVIDENCE_IDS = load_official_evidence_ids()


def stable_source_id(value):
    return "src-" + hashlib.sha256((value or "").encode("utf-8")).hexdigest()[:12]


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(DATA, f"{name}.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    cn_textfix.normalize_module(m)
    return m


def load_tuple_module(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(DATA, f"{name}.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ---------------- source classification (spec §8) ----------------
REPO_LABEL = re.compile(
    r"(Repo:|Random Test|Unit Test|CN Topic Test|Subject Test|BCI|OCR|"
    r"InstrumentationTools|Medium blog|pscarivukal|examsmantra|yctfastbook|"
    r"compsciedu|byjus|geeksforgeeks|indiabix|sanfoundry|tutorialspoint)", re.I)
ORIGINAL_LABEL = re.compile(r"Practice — original", re.I)
TEXTBOOK_LABEL = re.compile(r"Forouzan|textbook|Tanenbaum|Kurose|Stallings", re.I)
UNSUPPORTED_RPSC_KEY_LABEL = re.compile(r"RPSC\s+Programmer\s+2024\s+Paper[- ]?1", re.I)
EXAM_YEAR = re.compile(
    r"\b(GATE|NET|UGC[- ]NET|KVS|EMRS|DSSSB|JNV|RPSC|BPSC|TNPSC|OSSC|Kerala PSC|"
    r"SSC|MTS|CHSL|CGL|RRB|IBPS|SBI|RSMSSB|HTET|PGT|Lecturer|UPSC|NIELIT|"
    r"Assistant Professor|Informatics Assistant|Programmer|ACP|Deputy Director|"
    r"TCS|Wipro|Infosys)\b(?:[- ]?(20\d{2}))?", re.I)


def classify_source(src, nk=None, question_id=None):
    """Return (source_type, exam_name, exam_year, verification_status).

    A filename or the words “official key” are not evidence. Only a stable
    question ID listed in the audited paper+final-key evidence register may be
    classified as an official PYQ.
    """
    s = src or ""
    exam_m = EXAM_YEAR.search(s)
    exam_name = exam_m.group(1) if exam_m else None
    exam_year = exam_m.group(2) if (exam_m and exam_m.group(2)) else None
    if re.search(r"RPSC\s+Programmer\s+2024", s, re.I):
        exam_name, exam_year = "RPSC Programmer", "2024"

    if question_id and question_id in OFFICIAL_EVIDENCE_IDS:
        st, vs = "verified_official_pyq", "paper_and_key_checked"
    elif UNSUPPORTED_RPSC_KEY_LABEL.search(s):
        st, vs = "claimed_pyq_unverified", "claimed_answer_unverified"
    elif ORIGINAL_LABEL.search(s):
        st, vs = "original_practice", "answer_checked"
    elif TEXTBOOK_LABEL.search(s) and not REPO_LABEL.search(s):
        st, vs = "textbook_paraphrase", "answer_checked"
    elif REPO_LABEL.search(s):
        st = "repository_internal"
        vs = ("claimed_answer_unverified" if nk and isinstance(nk, (list, tuple))
              and nk and nk[0] and "NOT verified" in nk[0] else "answer_checked")
    elif exam_name:
        st = "claimed_pyq_unverified"
        vs = ("claimed_answer_unverified" if nk and isinstance(nk, (list, tuple))
              and nk and nk[0] and "NOT verified" in nk[0] else "answer_checked")
    else:
        st = "repository_internal"
        vs = ("claimed_answer_unverified" if nk and isinstance(nk, (list, tuple))
              and nk and nk[0] and "NOT verified" in nk[0] else "answer_checked")
    return st, exam_name, exam_year, vs


def scrub_unverified_source_key_text(value):
    text = value or ""
    patterns = (
        r"(?i)matches?\s+the\s+official\s+RPSC(?:\s+2024)?\s+key(?:\s*\([a-d]\))?",
        r"(?i)official\s+RPSC(?:\s+2024)?\s+key(?:\s*\([a-d]\))?",
        r"(?i)RPSC(?:\s+2024)?\s+official\s+key(?:\s*\([a-d]\))?",
        r"(?i)official\s+key(?:\s*\([a-d]\))?",
    )
    for pattern in patterns:
        text = re.sub(pattern, "unverified supplied answer-table claim", text)
    return text


def public_source_reference(src):
    if UNSUPPORTED_RPSC_KEY_LABEL.search(src or ""):
        return (
            "Computer Network/Past Papers/RPSC Programmer 2024 Paper-1/"
            "2024 Programmer Paper-1 QUESTIONS.md; "
            "2024 Programmer Paper-1 ANSWERS.md (community-maintained; "
            "not an official final answer key)"
        )
    return src


def provenance_note(src, opts):
    if any(not (option[0] or "").strip() for option in opts):
        return "Question content is incomplete because at least one answer option is blank; do not use in practice until a source-backed correction is reviewed."
    if UNSUPPORTED_RPSC_KEY_LABEL.search(src or ""):
        return "Community-maintained RPSC 2024 source; answer table is not an official final key."
    return None


def verification_note(status):
    if status == "paper_and_key_checked":
        return "Question-level official paper and final-key evidence recorded in data/sources/official_paper_key_evidence.json"
    if status == "answer_checked":
        return "EkGuru curation pipeline — cross-checked concept answer; not official-key matching"
    if status == "pending_review":
        return "Pending review: one or more answer options are blank; source wording is preserved and the item is excluded from practice."
    return "NOT independently verified — source answer only; review required"


def exam_tag_basis(source_type, exam_name):
    if source_type == "claimed_pyq_unverified":
        return "source_claim_unverified"
    if exam_name and source_type != "original_practice":
        return "source_label_unverified"
    return "suggested_practice_fit"


def infer_style(qen):
    t = qen.lower()
    if re.search(r"\bmatch\b", t) or "जोड़ी" in qen:
        return "match"
    if re.search(r"statements?|सूत्र|कथन", t) and re.search(r"true|false|correct|सही|गलत", t):
        return "statement"
    if re.search(r"\d", qen) and re.search(
            r"how many|calculate|maximum|minimum|speed|rate|bytes?|bits?|ms\b|कितने|गणना", t):
        return "numerical"
    if re.search(r"scenario|case|office|organization|company|एक कार्यालय", t):
        return "scenario"
    return "concept"


def exam_tags_for(src, diff, st):
    tags = []
    m = EXAM_YEAR.search(src or "")
    if m:
        name = m.group(1).upper()
        mapping = {
            "GATE": "GATE CS", "NET": "UGC-NET 087", "UGC-NET": "UGC-NET 087",
            "UGC NET": "UGC-NET 087", "RPSC": "RPSC Programmer",
            "PROGRAMMER": "RPSC Programmer", "ACP": "RPSC ACP/DD",
            "DEPUTY DIRECTOR": "RPSC ACP/DD", "INFORMATICS ASSISTANT": "RSMSSB Informatics Assistant",
            "RSMSSB": "RSMSSB Informatics Assistant", "KVS": "KVS PGT/CS",
            "EMRS": "EMRS PGT CS", "DSSSB": "DSSSB", "JNV": "JNV TAT",
            "SSC": "SSC Computer Awareness", "MTS": "SSC Computer Awareness",
            "CHSL": "SSC Computer Awareness", "CGL": "SSC Computer Awareness",
            "RRB": "RRB Computer Awareness", "IBPS": "IBPS Computer Awareness",
            "SBI": "IBPS Computer Awareness", "BPSC": "BPSC", "TNPSC": "TNPSC",
            "OSSC": "OSSC", "KERALA PSC": "Kerala PSC", "HTET": "HTET/PGT",
            "PGT": "HTET/PGT", "LECTURER": "Lecturer/AP", "UPSC": "UPSC",
            "ASSISTANT PROFESSOR": "Lecturer/AP", "NIELIT": "NIELIT",
            "TCS": "Campus Placement", "WIPRO": "Campus Placement",
            "INFOSYS": "Campus Placement",
        }
        if name in mapping:
            tags.append(mapping[name])
    if not tags:
        # syllabus-fit default tags (documented in SOURCE_REGISTER)
        if diff == 2:
            tags = ["GATE CS", "UGC-NET 087", "RPSC Programmer", "RPSC ACP/DD"]
        elif diff == 1:
            tags = ["RSMSSB Informatics Assistant", "SSC Computer Awareness", "RPSC Programmer"]
        else:
            tags = ["SSC Computer Awareness", "RSMSSB Informatics Assistant", "JNV TAT"]
    if st == "original_practice":
        tags = tags + ["Practice Set"]
    out, seen = [], set()
    for t in tags:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def main():
    os.makedirs(OUT_DATA, exist_ok=True)
    os.makedirs(OUT_REP, exist_ok=True)
    records = []
    inv = Counter()
    by_src = Counter()
    by_style = Counter()
    by_diff = Counter()
    by_ver = Counter()

    for n in range(1, 8):
        tid, tname = TOPICS[n]
        d = load(f"topic{n}_data")
        seq = 0
        for si, s in enumerate(d.SECTIONS):
            sub = s["title"]
            # merge practice-new originals into their sections (same as builders)
            qs = list(s["questions"])
            for q in qs:
                seq += 1
                qen, qhi = q["q"][0], q["q"][1]
                opts = [[o[0], (o[1] or o[0])] for o in q["opts"]]
                ans = q["ans"]
                wr, nk = q["wr"], q["nk"]
                src = q["src"]
                if UNSUPPORTED_RPSC_KEY_LABEL.search(src):
                    wr = [scrub_unverified_source_key_text(x) for x in wr]
                    nk = [scrub_unverified_source_key_text(x) for x in nk]
                rid = f"CN-{tid}-{seq:04d}"
                st, exam_name, exam_year, vs = classify_source(src, nk, rid)
                if any(not (option[0] or "").strip() for option in opts):
                    vs = "pending_review"
                diff = cn_difficulty.q_diff(dict(src=src, q=[qen, qhi], opts=opts, ans=ans))
                style = infer_style(qen)
                ww = {str(k): [v[0], (v[1] or v[0])] for k, v in (q.get("ww") or {}).items()}
                rec = {
                    "id": rid,
                    "subject_id": "cn",
                    "topic_id": tid,
                    "question_type": "single_select_mcq",
                    "option_ids": list(LETTERS),
                    "answer_option_id": LETTERS[ans],
                    "source_id": stable_source_id(public_source_reference(src)),
                    "topic": tname,
                    "subtopic": sub,
                    "stem_en": qen,
                    "stem_hi": qhi,
                    "options_en": [o[0] for o in opts],
                    "options_hi": [o[1] for o in opts],
                    "correct_option": LETTERS[ans],
                    "explanation_en": wr[0],
                    "explanation_hi": wr[1],
                    "nukte_en": nk[0],
                    "nukte_hi": nk[1],
                    "why_wrong": {LETTERS[int(k)]: [v[0], v[1]] for k, v in ww.items()},
                    "question_style": style,
                    "difficulty": ["easy", "medium", "hard"][diff],
                    "difficulty_basis": "heuristic_classifier_estimate",
                    "exam_tags": exam_tags_for(src, diff, st),
                    "exam_tag_basis": exam_tag_basis(st, exam_name),
                    "source_type": st,
                    "exam_name": exam_name,
                    "exam_year": exam_year,
                    "paper_or_shift": None,
                    "question_id_in_official_key": None,
                    "source_url_or_file": public_source_reference(src),
                    "provenance_note": provenance_note(src, opts),
                    "answer_verified_by": verification_note(vs),
                    "verification_status": vs,
                    "duplicate_group": None,
                    "concept_tags": [sub.split("—")[0].strip()[:60]] if "—" in sub else [tname],
                    "last_reviewed": "2026-10-14",
                }
                records.append(rec)
                inv[tid] += 1
                by_src[st] += 1
                by_style[style] += 1
                by_diff[rec["difficulty"]] += 1
                by_ver[vs] += 1

        # practice originals (practice_new p1..p4, *_X lists)
        new_map = {}
        for pn in ("practice_new_p1", "practice_new_p2", "practice_new_p3", "practice_new_p4",
                   "practice_new_p5", "w6_bank"):
            m = load_tuple_module(pn)
            for k in dir(m):
                if k.startswith("P") and isinstance(getattr(m, k), list):
                    new_map[k] = getattr(m, k)
        newnames = ["P%d_" % n]
        for idx2, s2 in enumerate(d.SECTIONS):
            pass
        # attach by NEW_MAP convention used in builders
        import re as _re
        nmap = {
            1: ["P1_A", "P1_B", "P1_C", "P1_D", "P1_E", "P1_F", "P1_G"],
            2: ["P2_A", "P2_B", "P2_C", "P2_D"],
            3: ["P3_A", "P3_B", "P3_C", "P3_D", "P3_E"],
            4: ["P4_A", "P4_B", "P4_C", "P4_D"],
            5: ["P5_A", "P5_B", "P5_C"],
            6: ["P6_A", "P6_B", "P6_C", "P6_D", "P6_E"],
            7: ["P7_A", "P7_B", "P7_C"],
        }
        for idx3, s3 in enumerate(d.SECTIONS):
            base = nmap[n][idx3] if idx3 < len(nmap[n]) else None
            if not base:
                continue
            for k2 in sorted(new_map):
                if k2 == base or k2.startswith(base + "_X"):
                    for t in new_map[k2]:
                        seq += 1
                        src, qen, qhi, opts, ans, wr, nk, ww = t
                        opts = [[o[0], (o[1] or o[0])] for o in opts]
                        if UNSUPPORTED_RPSC_KEY_LABEL.search(src):
                            wr = [scrub_unverified_source_key_text(x) for x in wr]
                            nk = [scrub_unverified_source_key_text(x) for x in nk]
                        rid = f"CN-{tid}-{seq:04d}"
                        st, exam_name, exam_year, vs = classify_source(src, nk, rid)
                        if any(not (option[0] or "").strip() for option in opts):
                            vs = "pending_review"
                        diff = cn_difficulty.q_diff(dict(src=src, q=[qen, qhi], opts=opts, ans=ans))
                        rec = {
                            "id": rid,
                            "subject_id": "cn",
                            "topic_id": tid,
                            "question_type": "single_select_mcq",
                            "option_ids": list(LETTERS),
                            "answer_option_id": LETTERS[ans],
                            "source_id": stable_source_id(public_source_reference(src)),
                            "topic": tname,
                            "subtopic": s3["title"],
                            "stem_en": qen,
                            "stem_hi": qhi,
                            "options_en": [o[0] for o in opts],
                            "options_hi": [o[1] for o in opts],
                            "correct_option": LETTERS[ans],
                            "explanation_en": wr[0],
                            "explanation_hi": wr[1],
                            "nukte_en": nk[0],
                            "nukte_hi": nk[1],
                            "why_wrong": {LETTERS[k]: [v[0], (v[1] or v[0])] for k, v in (ww or {}).items()},
                            "question_style": infer_style(qen),
                            "difficulty": ["easy", "medium", "hard"][diff],
                            "difficulty_basis": "heuristic_classifier_estimate",
                            "exam_tags": exam_tags_for(src, diff, st),
                            "exam_tag_basis": exam_tag_basis(st, exam_name),
                            "source_type": st,
                            "exam_name": exam_name,
                            "exam_year": exam_year,
                            "paper_or_shift": None,
                            "question_id_in_official_key": None,
                            "source_url_or_file": public_source_reference(src),
                            "provenance_note": provenance_note(src, opts),
                            "answer_verified_by": verification_note(vs),
                            "verification_status": vs,
                            "duplicate_group": None,
                            "concept_tags": [s3["title"].split("—")[0].strip()[:60]],
                            "last_reviewed": "2026-10-14",
                        }
                        records.append(rec)
                        inv[tid] += 1
                        by_src[st] += 1
                        by_style[rec["question_style"]] += 1
                        by_diff[rec["difficulty"]] += 1
                        by_ver[vs] += 1

    # Use the same Unicode-normalized exact/near-duplicate audit as the release reports.
    dup_groups, near = audit_duplicates.audit(records)
    duplicate_ids = {}
    for index, group in enumerate(dup_groups, 1):
        group_id = f"DUP-{index:03d}"
        for question_id in group["question_ids"]:
            duplicate_ids[question_id] = group_id
    for rec in records:
        rec["duplicate_group"] = duplicate_ids.get(rec["id"])

    payload = {
        "schema_version": 2,
        "project": "EkGuru CN Question Bank",
        "brand": "EkGuru Learning",
        "compiler": "PRAKASH",
        "generated": "2026-10-14",
        "spec": "Computer Network/new/README.md (master execution prompt)",
        "counts": {
            "total": len(records),
            "per_topic": dict(inv),
            "by_source_type": {k: by_src.get(k, 0) for k in ("verified_official_pyq", "claimed_pyq_unverified", "repository_internal", "textbook_paraphrase", "original_practice")},
            "by_difficulty": dict(by_diff),
            "by_style": dict(by_style),
            "by_verification": {k: by_ver.get(k, 0) for k in ("paper_and_key_checked", "answer_checked", "claimed_answer_unverified", "disputed", "pending_review")},
            "exact_duplicate_groups": len(dup_groups),
            "near_duplicate_candidates": len(near),
        },
        "questions": records,
    }
    with open(os.path.join(OUT_DATA, "cn_questions.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)

    # Keep all derived public assets and reports in their deterministic builders.
    import subprocess
    for script in ("build_site_data.py", "build_reports.py"):
        subprocess.run([sys.executable, os.path.join(HERE, script)], check=True)
    print("records:", len(records))
    print("exact dup groups:", len(dup_groups))
    print("near candidates:", len(near))
    print("by source:", dict(by_src))
    print("by verification:", dict(by_ver))


if __name__ == "__main__":
    main()
