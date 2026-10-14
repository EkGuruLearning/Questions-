#!/usr/bin/env python3
"""Guard exam-profile status and subject/topic mapping claims."""
from __future__ import annotations
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXAMS = json.loads((ROOT / "data/catalog/exams.json").read_text(encoding="utf-8"))
SUBJECTS = json.loads((ROOT / "data/catalog/subjects.json").read_text(encoding="utf-8"))
MAPPINGS = json.loads((ROOT / "data/catalog/syllabus_mappings.json").read_text(encoding="utf-8"))
BANK = json.loads((ROOT / "Computer Network/data/cn_questions.json").read_text(encoding="utf-8"))


def main():
    profiles = {profile["id"]: profile for profile in EXAMS.get("profiles", [])}
    subjects = {subject["id"]: subject for subject in SUBJECTS.get("subjects", [])}
    topics = {q["topic_id"] for q in BANK["questions"]}
    errors = []
    if len(profiles) != len(EXAMS.get("profiles", [])):
        errors.append("duplicate exam profile id")
    for pid, profile in profiles.items():
        if profile.get("simulation_level") == "exact_simulation":
            if not profile.get("official_syllabus_url") or not profile.get("official_pattern_url"):
                errors.append(f"{pid}: exact simulation without official syllabus/pattern references")
            if profile.get("pattern_status") != "officially_checked":
                errors.append(f"{pid}: exact simulation not marked officially checked")
        if profile.get("question_types") and any(qt not in ("single_select_mcq",) for qt in profile["question_types"]):
            errors.append(f"{pid}: profile exposes unimplemented question type")
        for key in ("official_syllabus_url", "official_pattern_url"):
            url = profile.get(key)
            if url and not url.startswith(("https://", "http://")):
                errors.append(f"{pid}: unsafe URL field {key}")
    for mapping in MAPPINGS.get("mappings", []):
        if mapping.get("exam_profile_id") not in profiles:
            errors.append(f"mapping references unknown exam {mapping.get('exam_profile_id')}")
        subject = subjects.get(mapping.get("subject_id"))
        if not subject:
            errors.append(f"mapping references unknown subject {mapping.get('subject_id')}")
            continue
        if mapping.get("subject_id") == "cn" and any(t not in topics for t in mapping.get("topic_ids", [])):
            errors.append(f"mapping references nonexistent CN topic for {mapping.get('exam_profile_id')}")
        if mapping.get("mapping_status") not in ("subject_scope", "suggested_practice_fit", "officially_verified"):
            errors.append(f"mapping has unsupported status for {mapping.get('exam_profile_id')}")
        if mapping.get("mapping_status") == "officially_verified":
            errors.append(f"{mapping.get('exam_profile_id')}: official mapping has no implemented evidence gate")
    for subject in SUBJECTS.get("subjects", []):
        if subject.get("status") == "live" and subject["id"] != "cn":
            errors.append(f"subject {subject['id']} is marked live without a published data bank")
    if errors:
        print("FAIL: " + str(len(errors)) + " blueprint/catalog issues")
        for error in errors:
            print(" -", error)
        raise SystemExit(1)
    print(f"PASS: {len(profiles)} exam profiles and {len(MAPPINGS.get('mappings', []))} mappings; none claims an exact simulation.")


if __name__ == "__main__":
    main()
