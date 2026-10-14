#!/usr/bin/env python3
"""EkGuru site data builder - PRAKASH (EkGuru Learning)
Padho: Computer Network/data/cn_questions.json  (poora bank, source of truth)
Likho: assets/cn-questions.min.json            (website ke liye halka version)

Sirf wahi field rakhe hain jo browser ko chahiye. Baaki audit/source
metadata bank me hi rehta hai, website par load nahi hota.

Chalao:  python3 tools/build_site_data.py
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "Computer Network" / "data" / "cn_questions.json"
OUT = ROOT / "assets" / "cn-questions.min.json"
def main():
    bank = json.loads(SRC.read_text(encoding="utf-8"))
    slim = []
    for q in bank["questions"]:
        slim.append({
            "i": q["id"], "t": q["topic_id"], "st": q.get("subtopic",""),
            "q": q.get("stem_en",""), "qh": q.get("stem_hi",""),
            "o": q.get("options_en",[]), "oh": q.get("options_hi",[]),
            "a": "ABCD".find(q.get("correct_option","A")),
            "e": q.get("explanation_en",""), "eh": q.get("explanation_hi",""),
            "n": q.get("nukte_en",""), "nh": q.get("nukte_hi",""),
            "d": q.get("difficulty","medium"), "s": q.get("question_style","concept"),
            "src": q.get("exam_name","") or q.get("source_type",""),
        })
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(slim, ensure_ascii=False, separators=(",",":")), encoding="utf-8")
    print(f"{len(slim)} questions -> {OUT} ({OUT.stat().st_size//1024} KB)")
if __name__ == "__main__": main()
