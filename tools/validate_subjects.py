#!/usr/bin/env python3
"""Validate live subject publication gates and required subject resources."""
from __future__ import annotations

import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOPIC_IDS = [f"T{i:02d}" for i in range(1, 8)]
TOPIC_TITLES = {
    "T01": "Introduction of Data Communication",
    "T02": "Network Models: OSI & TCP/IP",
    "T03": "Addressing: MAC, IPv4, IPv6, Ports, DNS",
    "T04": "Networking Devices",
    "T05": "Transmission Medium",
    "T06": "OSI Layers in Detail",
    "T07": "Network Security",
}
CATEGORIES = {
    "Theory/Notes", "Practice PDF", "Answer Key/Solutions", "Interactive CBT", "Past Paper",
    "Reference Book", "Map/Atlas", "Source Register", "Audit/QA", "Metadata/CSV",
    "Archive/Legacy", "Planned/Under Review",
}


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def file_at(repo_path: str) -> bool:
    candidate = (ROOT / pathlib.PurePosixPath(repo_path)).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError:
        return False
    return candidate.is_file()


def main() -> None:
    subjects_doc = load("assets/catalog/subjects.json")
    resources_doc = load("assets/catalog/resources.json")
    cn_manifest = load("assets/banks/cn/manifest.json")
    build = load("data/reports/build_manifest.json")
    maps_doc = load("assets/catalog/maps.json")
    resources = resources_doc.get("resources", [])
    subjects = subjects_doc.get("subjects", [])
    errors: list[str] = []
    ids = [subject.get("id") for subject in subjects]
    if len(ids) != len(set(ids)):
        errors.append("Subject IDs must be unique")
    if set(ids) != {"computer-network", "rajasthan-geography"}:
        errors.append(f"Expected exactly the two published subject entries; got {ids}")
    resource_ids = [item.get("id") for item in resources]
    if len(resource_ids) != len(set(resource_ids)):
        errors.append("Resource IDs must be unique")
    if not CATEGORIES.issuperset(item.get("category") for item in resources):
        errors.append("A resource uses an unsupported catalogue category")

    subject_by_id = {item.get("id"): item for item in subjects}
    cn = subject_by_id.get("computer-network", {})
    geo = subject_by_id.get("rajasthan-geography", {})
    by_id = {item.get("id"): item for item in resources}
    for subject in subjects:
        route = subject.get("route", "")
        if subject.get("status") == "live" and not file_at(route):
            errors.append(f"Live subject route does not exist: {subject.get('id')} → {route}")
        if subject.get("status") == "live" and subject.get("resources_verified") is not True:
            errors.append(f"Live subject has not passed its resource existence gate: {subject.get('id')}")
        if subject.get("status") not in ("live", "unavailable"):
            errors.append(f"Unknown subject availability status: {subject.get('id')}={subject.get('status')}")

    canonical_path = ROOT / "Computer Network/data/cn_questions.json"
    canonical_sha = hashlib.sha256(canonical_path.read_bytes()).hexdigest()
    if cn.get("status") != "live":
        errors.append("Computer Network is not live despite its published bank/resources")
    if cn.get("canonical_sha256") != canonical_sha or cn_manifest.get("canonical_sha256") != canonical_sha or build.get("canonical_sha256") != canonical_sha:
        errors.append("Canonical bank SHA-256 does not match all build/catalogue records")
    if cn.get("question_count") != cn_manifest.get("question_count") or cn.get("question_count") != build.get("question_count"):
        errors.append("Computer Network question count does not match canonical/build manifests")
    if cn.get("practice_question_count") != cn_manifest.get("published_question_count") or cn.get("practice_question_count") != build.get("published_question_count"):
        errors.append("Computer Network practice count does not match canonical/build manifests")
    if cn.get("topic_count") != 7 or cn_manifest.get("topic_count") != 7 or len(cn.get("topics", [])) != 7:
        errors.append("Computer Network must expose exactly seven checked topic records")
    if {item.get("id") for item in cn.get("topics", [])} != set(TOPIC_IDS):
        errors.append("The CN topic manifest must include T01–T07")
    for topic in cn.get("topics", []):
        topic_id = topic.get("id")
        if topic.get("title") != TOPIC_TITLES.get(topic_id):
            errors.append(f"Topic display title mismatch for {topic_id}: {topic.get('title')!r}")
        bank_topic = next((item for item in cn_manifest.get("topics", []) if item.get("topic_id") == topic_id), None)
        if not bank_topic:
            errors.append(f"No canonical topic manifest entry for {topic_id}")
            continue
        if topic.get("canonical_question_count") != bank_topic.get("record_count") or topic.get("practice_question_count") != bank_topic.get("published_question_count"):
            errors.append(f"Topic counts are not canonical/build-derived for {topic_id}")
        if topic.get("status") != "live" or not file_at(bank_topic.get("file", "")):
            errors.append(f"Topic bank chunk is unavailable for {topic_id}")
        current = by_id.get(f"cn-{topic_id.lower()}-cbt-current")
        v6 = by_id.get(f"cn-{topic_id.lower()}-cbt-v6")
        practice = [item for item in resources if item.get("subject_id") == "computer-network" and item.get("topic_id") == topic_id and item.get("category") == "Practice PDF" and item.get("file_type") == "PDF"]
        theory = [item for item in resources if item.get("subject_id") == "computer-network" and item.get("topic_id") == topic_id and item.get("category") == "Theory/Notes" and item.get("file_type") == "PDF"]
        if not current or current.get("open_behavior") != "same_tab" or not file_at(current.get("repo_path", "")):
            errors.append(f"Same-tab current CBT route is missing for {topic_id}")
        if not v6 or v6.get("open_behavior") != "same_tab" or not file_at(v6.get("repo_path", "")):
            errors.append(f"v6 topic launcher is missing or not same-tab for {topic_id}")
        if not practice or any(item.get("open_behavior") != "new_tab" for item in practice):
            errors.append(f"Existing practice PDF/new-tab link is missing or unsafe for {topic_id}")
        if not theory or any(item.get("open_behavior") != "new_tab" for item in theory):
            errors.append(f"Existing topic theory PDF/new-tab link is missing or unsafe for {topic_id}")

    if geo.get("status") != "live" or geo.get("kind") != "resource-library":
        errors.append("Rajasthan Geography must be a live resource library, not a question-bank claim")
    if "question_count" in geo or "practice_question_count" in geo:
        errors.append("Rajasthan Geography must not display a fake question-bank count")
    if geo.get("source_status") != "needs_verification":
        errors.append("Geography subject must retain needs-verification source status")
    if not file_at("subjects/rajasthan-geography/index.html") or not file_at("maps/rajasthan/index.html"):
        errors.append("Geography landing page or map catalogue route is missing")
    required_geo_paths = [
        "Rajasthan Geography Maps/previews/Rajasthan_Border_District_Atlas_Preview.png",
        "assets/catalog/rajasthan-border-atlas-preview.webp",
        "Rajasthan Geography Maps/exports/Rajasthan_Border_District_Atlas_A1.png",
        "Rajasthan Geography Maps/BOUNDARY_RELATIONS.csv",
        "Rajasthan Geography Maps/data/metadata/BORDER_ONLY_DISTRICTS.csv",
        "Rajasthan Geography Maps/data/metadata/BORDER_SUMMARY_BY_NEIGHBOUR.csv",
        "Rajasthan Geography Maps/data/metadata/BORDER_LENGTH_CROSSCHECK.csv",
        "Rajasthan Geography Maps/data/metadata/ACCEPTANCE_TESTS.csv",
        "Rajasthan Geography Maps/SOURCES_REGISTER.csv",
        "Rajasthan Geography Maps/SOURCE_AUDIT.md",
        "Rajasthan Geography Maps/UNRESOLVED_DISCREPANCIES.md",
        "Geography/Map/Rajasthan/SOURCE_AUDIT.md",
        "Geography/Map/Rajasthan/preview.webp",
    ]
    for path in required_geo_paths:
        if not file_at(path):
            errors.append(f"Required geography source/resource is missing: {path}")
    if len(maps_doc.get("maps", [])) < 2:
        errors.append("Both the atlas preview and separate input-audit reference must remain represented in maps.json")
    if len(maps_doc.get("border_summary", [])) == 0 or len(maps_doc.get("border_groups", [])) == 0:
        errors.append("Map manifest must contain CSV-derived border summary and district groups")

    for item in resources:
        if item.get("availability_status") in ("available", "retired_redirect") and not file_at(item.get("repo_path", "")):
            errors.append(f"Resource marked available but file missing: {item.get('id')} {item.get('repo_path')}")
        if item.get("category") == "Map/Atlas" and not (item.get("image_alt") or "").strip():
            errors.append(f"Map catalogue entry lacks descriptive alt: {item.get('id')}")
        if item.get("file_type") == "PDF" and item.get("open_behavior") != "new_tab":
            errors.append(f"PDF must open in a labelled new tab: {item.get('id')}")
        if item.get("open_behavior") == "new_tab":
            if not item.get("url"):
                errors.append(f"New-tab resource has no URL: {item.get('id')}")
            if "new tab" not in str(item.get("external_open_label", "")).lower():
                errors.append(f"New-tab resource is not explicitly labelled: {item.get('id')}")

    checks = {
        "resources": len(resources),
        "subjects": len(subjects),
        "computer_network_topics": len(cn.get("topics", [])),
        "same_tab_current_cbt_routes": sum(bool(item and item.get("open_behavior") == "same_tab") for item in (by_id.get(f"cn-{topic_id.lower()}-cbt-current") for topic_id in TOPIC_IDS)),
        "v6_launchers": sum(bool(item and item.get("open_behavior") == "same_tab") for item in (by_id.get(f"cn-{topic_id.lower()}-cbt-v6") for topic_id in TOPIC_IDS)),
        "practice_pdfs": sum(item.get("subject_id") == "computer-network" and item.get("category") == "Practice PDF" and item.get("file_type") == "PDF" for item in resources),
        "theory_pdfs": sum(item.get("subject_id") == "computer-network" and item.get("category") == "Theory/Notes" and item.get("file_type") == "PDF" for item in resources),
        "geography_map_entries": len(maps_doc.get("maps", [])),
        "geography_border_groups": len(maps_doc.get("border_groups", [])),
    }
    print(json.dumps(checks, ensure_ascii=False, sort_keys=True))
    if errors:
        print(f"FAIL: {len(errors)} subject publication issue(s)")
        for error in errors:
            print(" -", error)
        raise SystemExit(1)
    print("PASS: both live routes and all required CN/geography resources meet their publication gates.")


if __name__ == "__main__":
    main()
