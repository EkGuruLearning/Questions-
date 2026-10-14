#!/usr/bin/env python3
"""Build validated subject/resource/map manifests and repository inventories.

Outputs are generated from real repository files and checked-in data only:
  assets/catalog/subjects.json
  assets/catalog/resources.json
  assets/catalog/maps.json
  data/reports/portal_repository_inventory.csv
  Rajasthan Geography Maps/STRUCTURE_AND_ASSET_INVENTORY.md

This script is read-only with respect to source material. It never edits or moves
question banks, maps, PDFs, CSV sources, or CBT files.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import mimetypes
import pathlib
import re
import subprocess
import sys
import urllib.parse
from collections import defaultdict
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "assets/catalog"
REPORTS = ROOT / "data/reports"
ATLAS_DIR = ROOT / "Rajasthan Geography Maps"
INVENTORY_OUTPUTS = {
    "data/reports/portal_repository_inventory.csv",
    "data/reports/portal_browser_visual_qa.json",
    "data/reports/portal_pdf_rendering_qa.json",
    "data/reports/portal_qa_results.json",
    "Rajasthan Geography Maps/STRUCTURE_AND_ASSET_INVENTORY.md",
}

TOPICS = [
    ("T01", "Introduction of Data Communication", "परिचय: डेटा संचार"),
    ("T02", "Network Models: OSI & TCP/IP", "नेटवर्क मॉडल: OSI और TCP/IP"),
    ("T03", "Addressing: MAC, IPv4, IPv6, Ports, DNS", "एड्रेसिंग: MAC, IPv4, IPv6, पोर्ट और DNS"),
    ("T04", "Networking Devices", "नेटवर्किंग उपकरण"),
    ("T05", "Transmission Medium", "ट्रांसमिशन माध्यम"),
    ("T06", "OSI Layers in Detail", "OSI लेयर्स का विस्तृत अध्ययन"),
    ("T07", "Network Security", "नेटवर्क सुरक्षा"),
]

BOOK_TYPES = {
    "theory_mcq_pdf": "Theory/Notes",
    "practice_pdf": "Practice PDF",
    "standalone_cbt": "Interactive CBT",
}
BOOK_KINDS = set(BOOK_TYPES)
TOPIC_IDS = {f"T{number:02d}" for number in range(1, 8)}
RESOURCE_CATEGORIES = {
    "Theory/Notes", "Practice PDF", "Answer Key/Solutions", "Interactive CBT", "Past Paper",
    "Reference Book", "Map/Atlas", "Source Register", "Audit/QA", "Metadata/CSV",
    "Archive/Legacy", "Planned/Under Review",
}
PORTAL_RESOURCE_SUBJECTS = {"computer-network", "rajasthan-geography"}


def json_read(path: pathlib.Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repo_paths() -> list[str]:
    output = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
    )
    values = [item.decode("utf-8") for item in output.split(bytes((0,))) if item]
    return sorted(set(values), key=lambda value: value.casefold())


def encoded(path: str) -> str:
    return urllib.parse.quote(path, safe="/")


def relative_file(path: str) -> pathlib.Path:
    candidate = (ROOT / pathlib.PurePosixPath(path)).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise ValueError(f"Repository path escapes root: {path}") from exc
    return candidate


def existing(path: str) -> pathlib.Path:
    candidate = relative_file(path)
    if not candidate.is_file():
        raise FileNotFoundError(f"Required repository file does not exist: {path}")
    return candidate


def read_csv(path: str) -> list[dict[str, str]]:
    with existing(path).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def type_for(path: str) -> str:
    suffix = pathlib.PurePosixPath(path).suffix.lower()
    if not suffix:
        return "extensionless file"
    known = {
        ".md": "Markdown",
        ".csv": "CSV",
        ".json": "JSON",
        ".html": "HTML",
        ".snapshot": "preserved HTML snapshot",
        ".pdf": "PDF",
        ".png": "PNG image",
        ".jpeg": "JPEG image",
        ".jpg": "JPEG image",
        ".webp": "WebP image",
        ".py": "Python source",
        ".sh": "Shell script",
        ".qgz": "QGIS project archive",
        ".rst": "reStructuredText",
        ".ttf": "TrueType font",
        ".zip": "ZIP archive",
        ".txt": "Text file",
        ".gitkeep": "placeholder",
        ".gitignore": "ignore rules",
    }
    return known.get(suffix, mimetypes.guess_type(path)[0] or suffix.lstrip("."))


def image_dimensions(path: pathlib.Path) -> str:
    try:
        result = subprocess.run(
            ["identify", "-format", "%w×%h", str(path)],
            check=True,
            text=True,
            capture_output=True,
            timeout=20,
        )
        if result.stdout.strip():
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.SubprocessError):
        pass
    data = path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        return f"{int.from_bytes(data[16:20], 'big')}×{int.from_bytes(data[20:24], 'big')}"
    if data[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            i += 2
            if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
                continue
            if i + 2 > len(data):
                break
            size = int.from_bytes(data[i:i + 2], "big")
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                if i + 7 <= len(data):
                    height = int.from_bytes(data[i + 3:i + 5], "big")
                    width = int.from_bytes(data[i + 5:i + 7], "big")
                    return f"{width}×{height}"
                break
            i += max(size, 2)
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        chunk = data[12:16]
        if chunk == b"VP8X" and len(data) >= 30:
            width = int.from_bytes(data[24:27], "little") + 1
            height = int.from_bytes(data[27:30], "little") + 1
            return f"{width}×{height}"
    return "not read"


def resource(
    *,
    resource_id: str,
    subject_id: str,
    title: str,
    category: str,
    repo_path: str,
    topic_id: str | None = None,
    open_behavior: str | None = None,
    availability_status: str = "available",
    source_status: str = "Repository file available; source/verification limits are described in the linked audit.",
    source_status_label: str = "Repository file",
    source_status_state: str = "neutral",
    notes: str = "",
    url: str | None = None,
) -> dict:
    path = existing(repo_path)
    suffix = path.suffix.lower()
    if open_behavior is None:
        open_behavior = "new_tab" if suffix == ".pdf" else "same_tab"
    item = {
        "id": resource_id,
        "subject_id": subject_id,
        "title": title,
        "category": category,
        "repo_path": repo_path,
        "url": url or encoded(repo_path),
        "availability_status": availability_status,
        "open_behavior": open_behavior,
        "source_status": source_status,
        "source_status_label": source_status_label,
        "source_status_state": source_status_state,
        "file_type": type_for(repo_path),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "notes": notes,
    }
    if topic_id:
        item["topic_id"] = topic_id
    if open_behavior == "new_tab":
        item["external_open_label"] = "opens in new tab"
    if category == "Map/Atlas" and suffix in (".png", ".jpeg", ".jpg", ".webp"):
        if repo_path.startswith("Geography/Map/Rajasthan/"):
            item["image_alt"] = "Earlier Rajasthan regional reference map image from the separate Geography input-audit folder; not a validated final GIS map."
        elif "/previews/" in repo_path:
            item["image_alt"] = "Preview of the repository's Rajasthan border-district atlas with Hindi labels and highlighted boundaries; source and boundary status needs verification."
        else:
            item["image_alt"] = f"Full-size map export {path.name}: Rajasthan and surrounding border-district atlas; source and boundary status needs verification."
    return item


def virtual_resource(
    *, resource_id: str, subject_id: str, title: str, category: str, repo_path: str,
    url: str, topic_id: str, notes: str, status_label: str, source_status: str,
) -> dict:
    path = existing(repo_path)
    return {
        "id": resource_id,
        "subject_id": subject_id,
        "topic_id": topic_id,
        "title": title,
        "category": category,
        "repo_path": repo_path,
        "url": url,
        "availability_status": "available",
        "open_behavior": "same_tab",
        "source_status": source_status,
        "source_status_label": status_label,
        "source_status_state": "neutral",
        "file_type": "topic-filtered portal route",
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "notes": notes,
    }


def csv_path(path: str) -> str:
    return f"{path}?download=1" if False else encoded(path)


def make_subjects(build: dict, map_build: dict, available: set[str]) -> dict:
    bank = json_read(existing("assets/banks/cn/manifest.json"))
    canonical = "Computer Network/data/cn_questions.json"
    cn_route = "subjects/computer-network/index.html"
    geo_route = "subjects/rajasthan-geography/index.html"
    required_cn = [
        canonical,
        "practice/index.html",
        "Computer Network/Reports/INVENTORY.md",
        "Computer Network/Reports/ANSWER_VERIFICATION.md",
        "Computer Network/Practice/Topic 1 - Practice Questions - 375Q (Test Booklet).pdf",
        "Computer Network/Online Quiz/v6/Topic 1 - EkGuru v6 CBT.html",
    ]
    topic_entries = bank.get("topics", [])
    topic_files_live = len(topic_entries) == 7 and all(item.get("file") in available and int(item.get("published_question_count", 0)) > 0 for item in topic_entries)
    cn_live = cn_route in available and all(item in available for item in required_cn) and bank.get("topic_count") == 7 and topic_files_live
    map_required = [
        geo_route,
        "maps/rajasthan/index.html",
        "Rajasthan Geography Maps/previews/Rajasthan_Border_District_Atlas_Preview.png",
        "Rajasthan Geography Maps/exports/Rajasthan_Border_District_Atlas_A1.png",
        "Rajasthan Geography Maps/data/metadata/BORDER_ONLY_DISTRICTS.csv",
        "Rajasthan Geography Maps/SOURCES_REGISTER.csv",
        "Rajasthan Geography Maps/UNRESOLVED_DISCREPANCIES.md",
    ]
    map_live = all(item in available for item in map_required)
    topic_counts = {item["topic_id"]: item for item in bank.get("topics", [])}
    topics = []
    for topic_id, title, title_hi in TOPICS:
        item = topic_counts.get(topic_id, {})
        chunk_path = item.get("file")
        topic_live = bool(chunk_path and chunk_path in available and int(item.get("published_question_count", 0)) > 0)
        topics.append({
            "id": topic_id,
            "title": title,
            "title_hi": title_hi,
            "canonical_question_count": int(item.get("record_count", 0)),
            "practice_question_count": int(item.get("published_question_count", 0)),
            "status": "live" if topic_live else "unavailable",
        })
    return {
        "schema_version": 1,
        "generated_on": date.today().isoformat(),
        "counts_source": "data/reports/build_manifest.json and assets/banks/cn/manifest.json",
        "subjects": [
            {
                "id": "computer-network",
                "title": "Computer Network",
                "title_hi": "कंप्यूटर नेटवर्क",
                "kind": "question-bank",
                "status": "live" if cn_live else "unavailable",
                "route": cn_route,
                "description": "Seven-topic, source-labelled practice with topic theory, CBT launchers, practice booklets and verification notes. Source type and answer-review status are kept separate.",
                "action_label": "Explore Computer Network",
                "updated_at": build.get("generated_on", "unknown"),
                "update_note": "Canonical question-bank build date from checked-in build metadata; not a website deployment date.",
                "canonical_sha256": build.get("canonical_sha256"),
                "question_count": int(build.get("question_count", 0)),
                "practice_question_count": int(build.get("published_question_count", 0)),
                "topic_count": int(bank.get("topic_count", len(topics))),
                "topics": topics,
                "resources_verified": cn_live,
            },
            {
                "id": "rajasthan-geography",
                "title": "Rajasthan Geography",
                "title_hi": "राजस्थान भूगोल",
                "kind": "resource-library",
                "status": "live" if map_live else "unavailable",
                "route": geo_route,
                "description": "Existing map previews, border-district data, CSV downloads and source/QA records. This is a resource collection, not a published question bank; boundary findings still need verification.",
                "action_label": "Explore Rajasthan Geography",
                "updated_at": map_build.get("build_date", "unknown"),
                "update_note": "Map build metadata date; map data and legal-boundary status remain subject to the linked audits.",
                "source_status": "needs_verification",
                "source_status_label": "Map sources / boundary claims need verification",
                "resources_verified": map_live,
            },
        ],
    }


def make_portal_resources(source_doc: dict, available: set[str]) -> list[dict]:
    if source_doc.get("schema_version") != 1 or not isinstance(source_doc.get("resources"), list):
        raise ValueError("data/catalog/portal_resources.json must use schema_version 1 and a resources array")
    items: list[dict] = []
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    for index, record in enumerate(source_doc["resources"]):
        prefix = f"data/catalog/portal_resources.json resources[{index}]"
        resource_id = str(record.get("id", ""))
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", resource_id):
            raise ValueError(f"{prefix}: id must use lowercase letters, digits and hyphens: {resource_id!r}")
        if resource_id in seen_ids:
            raise ValueError(f"{prefix}: duplicate resource id {resource_id}")
        seen_ids.add(resource_id)

        subject_id = record.get("subject_id")
        if subject_id not in PORTAL_RESOURCE_SUBJECTS:
            raise ValueError(f"{prefix}: unsupported subject_id {subject_id!r}; add a subject publication gate before using it")
        repo_path = str(record.get("repo_path", ""))
        if not repo_path or repo_path in seen_paths:
            raise ValueError(f"{prefix}: repo_path is empty or repeated: {repo_path!r}")
        seen_paths.add(repo_path)
        if repo_path not in available:
            raise FileNotFoundError(f"{prefix}: source path is not tracked/present: {repo_path}")
        source_file = existing(repo_path)

        if subject_id == "rajasthan-geography" and not repo_path.startswith(("Geography/Map/Rajasthan/", "Rajasthan Geography Maps/")):
            raise ValueError(f"{prefix}: geography resources must remain in one of the two audited source trees: {repo_path}")
        if subject_id == "computer-network" and repo_path.startswith(("Computer Network/Incoming/", "Computer Network/new/", "archive/")):
            raise ValueError(f"{prefix}: staging and preserved archive files must not be published as current Computer Network resources: {repo_path}")
        topic_id = record.get("topic_id")
        if topic_id is not None:
            if subject_id != "computer-network" or topic_id not in TOPIC_IDS:
                raise ValueError(f"{prefix}: topic_id is only valid for Computer Network T01–T07")
            if repo_path.startswith("Computer Network/Topics/") and not repo_path.startswith(f"Computer Network/Topics/{topic_id}/"):
                raise ValueError(f"{prefix}: path folder and topic_id disagree: {repo_path} vs {topic_id}")
        if subject_id == "computer-network" and repo_path.startswith("Computer Network/Topics/T"):
            folder_topic = pathlib.PurePosixPath(repo_path).parts[2]
            if folder_topic not in TOPIC_IDS or topic_id != folder_topic:
                raise ValueError(f"{prefix}: new topic-folder resources need a matching T01–T07 topic_id")

        category = record.get("category")
        if category not in RESOURCE_CATEGORIES:
            raise ValueError(f"{prefix}: unsupported resource category {category!r}")
        required_text = ("title", "source_status", "source_status_label", "notes")
        missing = [field for field in required_text if not isinstance(record.get(field), str) or not record[field].strip()]
        if missing:
            raise ValueError(f"{prefix}: required descriptive fields are missing/empty: {', '.join(missing)}")
        source_state = record.get("source_status_state", "neutral")
        if source_state not in ("neutral", "warning"):
            raise ValueError(f"{prefix}: source_status_state must be neutral or warning")
        availability = record.get("availability_status", "available")
        if availability not in ("available", "retired_redirect", "needs_verification", "unavailable"):
            raise ValueError(f"{prefix}: invalid availability_status {availability!r}")
        behavior = record.get("open_behavior")
        if behavior is not None and behavior not in ("same_tab", "new_tab"):
            raise ValueError(f"{prefix}: open_behavior must be same_tab or new_tab")

        map_image = category == "Map/Atlas" and source_file.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
        if map_image and not str(record.get("image_alt", "")).strip():
            raise ValueError(f"{prefix}: new map images must supply accurate descriptive image_alt text")
        if subject_id == "rajasthan-geography" and category == "Map/Atlas" and source_state != "warning":
            raise ValueError(f"{prefix}: unresolved geography map resources must retain warning source status")

        item = resource(
            resource_id=resource_id,
            subject_id=subject_id,
            title=record["title"],
            category=category,
            repo_path=repo_path,
            topic_id=topic_id,
            open_behavior=behavior,
            availability_status=availability,
            source_status=record["source_status"],
            source_status_label=record["source_status_label"],
            source_status_state=source_state,
            notes=record["notes"],
            url=record.get("url"),
        )
        if record.get("image_alt"):
            item["image_alt"] = record["image_alt"]
        if category == "Map/Atlas" and source_file.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp") and not item.get("image_alt"):
            raise ValueError(f"{prefix}: map image resources need descriptive image_alt text")
        if source_file.suffix.lower() == ".pdf" and item["open_behavior"] != "new_tab":
            raise ValueError(f"{prefix}: PDF resources must open in a new tab")
        items.append(item)
    return items


def make_resources(paths: list[str], build: dict, books_doc: dict, geography_rows: list[dict], portal_source: dict) -> list[dict]:
    available = set(paths)
    items: list[dict] = []
    portal_items = make_portal_resources(portal_source, available)
    portal_paths = {item["repo_path"] for item in portal_items}
    topic_lookup = {topic_id: title for topic_id, title, _ in TOPICS}
    bank_stats = build.get("verification_counts", {})
    bank_source = build.get("source_type_counts", {})
    bank_status_note = (
        f"Current build: {build.get('question_count', 0):,} canonical records; "
        f"{build.get('published_question_count', 0):,} practice records; "
        f"{bank_stats.get('paper_and_key_checked', 0)} question-level official paper + final-key evidence records."
    )

    # Topic-specific digital CBT launchers, generated from the topic names and real route files.
    for topic_id, title, _ in TOPICS:
        n = int(topic_id[1:])
        current_route = f"practice/index.html?subject=cn&topic={topic_id}&mode=practice#practice"
        items.append(virtual_resource(
            resource_id=f"cn-{topic_id.lower()}-cbt-current",
            subject_id="computer-network",
            title=f"{topic_id} — Start topic CBT (shared current engine)",
            category="Interactive CBT",
            repo_path="practice/index.html",
            url=current_route,
            topic_id=topic_id,
            notes="Starts the source-labelled shared practice engine in this tab with this topic preselected.",
            status_label="Current topic launcher · same tab",
            source_status="The shared CBT reads the generated, source-gated topic bank; individual answer/source labels remain visible in the app.",
        ))

    book_files: set[str] = set()
    book_ids: set[str] = set()
    for book in books_doc.get("books", []):
        book_id = str(book.get("id", ""))
        rel = str(book.get("file", ""))
        topic_id = book.get("topic_id")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", book_id):
            raise ValueError(f"Book catalog id must use lowercase letters, digits and hyphens: {book_id!r}")
        if book_id in book_ids:
            raise ValueError(f"Duplicate book catalog id: {book_id}")
        book_ids.add(book_id)
        if rel in book_files:
            raise ValueError(f"A file may only be registered once in data/catalog/books.json: {rel}")
        if book.get("subject_id") != "cn" or topic_id not in TOPIC_IDS:
            raise ValueError(f"Book {book_id} must belong to subject_id='cn' and topic T01–T07")
        if book.get("kind") not in BOOK_KINDS:
            raise ValueError(f"Book {book_id} has unsupported kind {book.get('kind')!r}")
        if rel not in available:
            raise FileNotFoundError(f"Book catalog path is not tracked/present: {rel}")
        book_files.add(rel)
        if rel.startswith("Computer Network/Topics/T"):
            folder_topic = pathlib.PurePosixPath(rel).parts[2]
            if folder_topic != topic_id or folder_topic not in TOPIC_IDS:
                raise ValueError(f"Topic material path and topic_id disagree for {book_id}: {rel} vs {topic_id}")
            if book.get("kind") not in ("theory_mcq_pdf", "practice_pdf"):
                raise ValueError(f"New topic-folder material must be a theory or practice PDF: {rel}")
            if pathlib.PurePosixPath(rel).suffix.lower() != ".pdf":
                raise ValueError(f"New topic-folder material must be registered through its PDF: {rel}")
        topic_name = topic_lookup.get(topic_id, "Computer Network")
        if book["kind"] == "standalone_cbt":
            n = int(topic_id[1:])
            items.append(resource(
                resource_id=f"cn-{topic_id.lower()}-cbt-v6",
                subject_id="computer-network",
                topic_id=topic_id,
                title=f"{topic_id} — Versioned v6 launcher",
                category="Interactive CBT",
                repo_path=rel,
                open_behavior="same_tab",
                source_status="Versioned launcher into the same shared current CBT engine; this is not a separate bank snapshot.",
                source_status_label="v6 topic launcher · same tab",
                notes=book.get("note", "Opens the shared current practice engine."),
            ))
        elif book["kind"] == "practice_pdf":
            items.append(resource(
                resource_id=f"cn-book-{book_id}",
                subject_id="computer-network",
                topic_id=topic_id,
                title=f"{topic_id} — {topic_name} practice booklet (PDF)",
                category="Practice PDF",
                repo_path=rel,
                open_behavior="new_tab",
                source_status="Existing PDF; its cover/file count is not a substitute for the canonical bank build count.",
                source_status_label="Existing PDF · historical booklet",
                source_status_state="neutral",
                notes="Opens in a new tab. Compare its filename count with the live canonical/published counts shown above; do not infer official PYQ status from the PDF.",
            ))
        elif book["kind"] == "theory_mcq_pdf":
            items.append(resource(
                resource_id=f"cn-book-{book_id}",
                subject_id="computer-network",
                topic_id=topic_id,
                title=f"{topic_id} — {topic_name} theory + selected MCQs (PDF)",
                category="Theory/Notes",
                repo_path=rel,
                open_behavior="new_tab",
                source_status="Existing historical subset; PDF filename count is not the current live-bank count.",
                source_status_label="Existing PDF · historical subset",
                notes="PDF opens in a new tab; file preserved at its original repository path.",
            ))
            markdown = rel[:-4] + ".md" if rel.lower().endswith(".pdf") else ""
            if markdown and markdown in available:
                items.append(resource(
                    resource_id=f"cn-book-{book_id}-markdown",
                    subject_id="computer-network",
                    topic_id=topic_id,
                    title=f"{topic_id} — {topic_name} theory + selected MCQs (Markdown)",
                    category="Theory/Notes",
                    repo_path=markdown,
                    open_behavior="same_tab",
                    source_status="Existing Markdown edition; historical subset, not the current full-bank count.",
                    source_status_label="Existing source notes",
                    notes="Plain-text/Markdown edition of the historical theory and selected-question material.",
                ))

    # The old public paths are redirect wrappers, not standalone current CBTs.
    for topic_id, topic_name, _ in TOPICS:
        n = int(topic_id[1:])
        rel = f"Computer Network/Online Quiz/Topic {n} - Online Quiz & Exam (by PRAKASH - EkGuru).html"
        if rel in available:
            items.append(resource(
                resource_id=f"cn-{topic_id.lower()}-retired-route",
                subject_id="computer-network",
                topic_id=topic_id,
                title=f"{topic_id} — retired standalone quiz URL (redirect)",
                category="Archive/Legacy",
                repo_path=rel,
                open_behavior="same_tab",
                availability_status="retired_redirect",
                source_status="The former standalone app is retired; its original snapshot is archived separately with historical labels.",
                source_status_label="Retired redirect · not a standalone CBT",
                source_status_state="warning",
                notes="This preserved public route redirects to the current shared practice page. Do not use the archived snapshot as the live bank.",
            ))

    # Canonical and generated bank evidence/data.
    items.append(resource(
        resource_id="cn-canonical-bank-json",
        subject_id="computer-network",
        title="Canonical Computer Network question bank (JSON)",
        category="Metadata/CSV",
        repo_path="Computer Network/data/cn_questions.json",
        open_behavior="same_tab",
        source_status=bank_status_note,
        source_status_label="Canonical source data · per-question evidence applies",
        notes="Full canonical JSON data. The 1,556 records are not 1,556 official PYQs; see answer-verification and source-type summaries.",
    ))
    items.append(resource(
        resource_id="cn-public-source-register-json",
        subject_id="computer-network",
        title="Public question-level source register (JSON)",
        category="Source Register",
        repo_path="assets/source-register.min.json",
        source_status="Generated citation register; no current question-level official paper/final-key evidence records are accepted in the build manifest.",
        source_status_label="Generated citation register",
        notes="Contains public source citations used by the practice portal; raw OCR and reviewer notes are not included.",
    ))
    items.append(resource(
        resource_id="cn-compatibility-payload",
        subject_id="computer-network",
        title="Generated compatibility question payload (JSON)",
        category="Archive/Legacy",
        repo_path="assets/cn-questions.min.json",
        source_status="Generated compatibility artifact; current portal loads versioned topic chunks instead.",
        source_status_label="Generated compatibility payload",
        notes="Kept for compatibility; not fetched by the current topic portal on page load.",
    ))

    # Existing answer-key and answer-check resources.
    solution_paths = [
        "Computer Network/Subject Test Solution -1 (CN & Security).pdf",
        "Computer Network/Subject Test Solution -1 (CN & Security) Part-2.pdf",
        "Computer Network/Unit Test -2 Solutions.pdf",
        "Computer Network/Unit Test-4 Solution.pdf",
        "Computer Network/Practice/ANSWER KEY - Added Questions (197) (Verification).pdf",
        "Computer Network/Past Papers/RPSC Programmer 2024 Paper-1/2024 Programmer Paper-1 ANSWERS.md",
    ]
    for rel in solution_paths:
        if rel not in available:
            continue
        filename = pathlib.PurePosixPath(rel).name
        is_check_aid = "Verification" in filename
        is_rpsc_transcript = filename.endswith("ANSWERS.md")
        note = (
            "Question-level official paper + final-key matches are not established by this file; see the current evidence register and answer-verification report."
            if not is_check_aid and not is_rpsc_transcript else
            "Answer-check aid / community-maintained answer table; this is not counted as question-level official paper + final-key evidence."
        )
        items.append(resource(
            resource_id="cn-solution-" + hashlib.sha256(rel.encode()).hexdigest()[:12],
            subject_id="computer-network",
            title=filename,
            category="Answer Key/Solutions",
            repo_path=rel,
            source_status="Answer-check material retained; not a blanket official-key claim.",
            source_status_label="Use with evidence-status note",
            source_status_state="warning",
            notes=note,
        ))

    # Past-paper and reference material, selected from real repository paths.
    if book_files & portal_paths:
        collisions = sorted(book_files & portal_paths)
        raise ValueError(f"A repository file cannot be registered in both books.json and portal_resources.json: {collisions}")

    for rel in sorted(available):
        if not rel.startswith("Computer Network/"):
            continue
        if rel in portal_paths:
            continue
        if rel == "Computer Network/Topics/README.md":
            continue
        if rel.startswith("Computer Network/Topics/"):
            topic_parts = pathlib.PurePosixPath(rel).parts
            folder_topic = topic_parts[2] if len(topic_parts) > 2 else ""
            if folder_topic not in TOPIC_IDS:
                raise ValueError(f"New topic materials must live in a T01–T07 folder: {rel}")
            if rel not in book_files:
                paired_markdown = rel.lower().endswith(".md") and (rel[:-3] + ".pdf") in book_files
                if not paired_markdown:
                    raise ValueError(f"New topic-folder resource must be registered in data/catalog/books.json: {rel}")
                continue
        path = pathlib.PurePosixPath(rel)
        if path.suffix.lower() not in (".pdf", ".md", ".rst"):
            continue
        if rel in book_files or rel in solution_paths:
            continue
        if rel.startswith("Computer Network/Reports/"):
            continue
        if rel.startswith("Computer Network/new/"):
            items.append(resource(
                resource_id="cn-legacy-" + hashlib.sha256(rel.encode()).hexdigest()[:12],
                subject_id="computer-network",
                title=path.name,
                category="Archive/Legacy",
                repo_path=rel,
                source_status="Preserved source/starter/older material; not included as a current bank resource without review.",
                source_status_label="Preserved legacy/source material",
                source_status_state="neutral",
                notes="Retained in its original `Computer Network/new/` location; check the file's own notes before reuse.",
            ))
            continue
        if rel.startswith("Computer Network/Past Papers/Reference Books/") or rel.startswith("Computer Network/Past Papers/Question Banks/"):
            category = "Reference Book"
            source_label = "Reference / textbook material"
            source_status = "Reference source; not an official exam-paper claim."
            notes = "Reference material. Check the local licence/source note before redistribution."
        elif rel.startswith("Computer Network/Past Papers/"):
            if "ANSWERS" in path.name.upper():
                category = "Answer Key/Solutions"
                source_label = "Answer transcript · evidence-limited"
                source_status = "The repository's current evidence report does not accept this transcript as an official final key."
                notes = "Community-maintained/transcribed answer material; not counted as question-level official paper + final-key evidence."
            elif path.suffix.lower() == ".md" and path.name in ("SOURCES.md",):
                category = "Source Register"
                source_label = "Source register / provenance notes"
                source_status = "Repository source notes; source-type labels do not prove official exam appearance."
                notes = "Read alongside `Computer Network/Reports/ANSWER_VERIFICATION.md` for the current verification gate."
            else:
                category = "Past Paper"
                source_label = "Repository past-paper / source material"
                source_status = "Exam/source provenance is not inferred from the filename; see per-question evidence status."
                notes = "Existing source or transcription material; a PYQ label alone is not proof of an official appearance."
        elif path.name.startswith("Topic ") and (path.suffix.lower() == ".pdf" or path.suffix.lower() == ".md"):
            category = "Theory/Notes"
            source_label = "Existing theory / selected MCQs"
            source_status = "Historical subset; filename counts are not the current canonical bank count."
            notes = "Topic-specific historical theory/selected MCQ edition; current live counts come from the canonical build manifest."
        elif path.suffix.lower() == ".pdf" and ("Solution" in path.name or "ANSWER KEY" in path.name.upper()):
            category = "Answer Key/Solutions"
            source_label = "Source-paper solution material"
            source_status = "Existing solution file; not a question-level official-key evidence record by itself."
            notes = "Use the source/answer-verification report before treating any answer as officially keyed."
        elif path.suffix.lower() == ".pdf":
            category = "Past Paper"
            source_label = "Repository source paper"
            source_status = "Source material; official exam-paper/final-key verification is tracked per question, not assumed from the filename."
            notes = "Opens in a new tab. Read the source register and verification report before using it as an official PYQ."
        elif path.name in ("README.md", "COVERAGE.md") or rel.endswith("/Incoming/README.md"):
            category = "Audit/QA"
            source_label = "Repository guide / historical coverage"
            source_status = "Background documentation; current bank counts and evidence statuses are in the generated reports."
            notes = "Historical descriptions may contain superseded counts; use the current build manifest and verification report."
        elif path.suffix.lower() == ".rst":
            category = "Reference Book"
            source_label = "Textbook-derived reference bank"
            source_status = "Reference text; licence and attribution apply."
            notes = "Existing question-bank reference section; see the included LICENSE.md."
        else:
            category = "Past Paper"
            source_label = "Source notes / transcription"
            source_status = "Source note; not itself an official answer-key record."
            notes = "Existing source note retained in the original folder."
        items.append(resource(
            resource_id="cn-material-" + hashlib.sha256(rel.encode()).hexdigest()[:12],
            subject_id="computer-network",
            title=path.name,
            category=category,
            repo_path=rel,
            source_status=source_status,
            source_status_label=source_label,
            source_status_state="warning" if category in ("Past Paper", "Answer Key/Solutions") else "neutral",
            notes=notes,
        ))

    # CN reports and provenance records.
    for rel in sorted(available):
        if not rel.startswith("Computer Network/Reports/"):
            continue
        path = pathlib.PurePosixPath(rel)
        category = "Source Register" if "SOURCE_REGISTER" in path.name else "Metadata/CSV" if path.suffix.lower() == ".csv" else "Audit/QA"
        items.append(resource(
            resource_id="cn-report-" + hashlib.sha256(rel.encode()).hexdigest()[:12],
            subject_id="computer-network",
            title=path.name,
            category=category,
            repo_path=rel,
            source_status="Checked-in CN inventory/provenance/QA report; review its date/build ID and caveats.",
            source_status_label="Existing build report",
            notes="Read the report together with the current canonical bank build ID; old counts in historical notes are not current counts.",
        ))

    # All maps, source registers, QA reports and CSV metadata under both geography roots.
    for rel in sorted(available):
        if not (rel.startswith("Geography/") or rel.startswith("Rajasthan Geography Maps/")):
            continue
        if rel in portal_paths:
            continue
        path = pathlib.PurePosixPath(rel)
        suffix = path.suffix.lower()
        if rel in {
            "Rajasthan Geography Maps/previews/Rajasthan_Border_District_Atlas_Preview.png",
            "Rajasthan Geography Maps/exports/Rajasthan_Border_District_Atlas_A1.png",
            "Rajasthan Geography Maps/exports/Rajasthan_Border_District_Atlas_A2.png",
            "Rajasthan Geography Maps/exports/Rajasthan_Border_District_Atlas_A3.png",
            "Rajasthan Geography Maps/exports/Rajasthan_Border_Districts_A4_Landscape.png",
            "Rajasthan Geography Maps/exports/Rajasthan_Border_Districts_A4_Portrait.png",
            "Geography/Map/Rajasthan/54fc0d18-7435-4472-a101-941c1af1ec9a.jpeg",
            "Geography/Map/Rajasthan/preview.webp",
        }:
            category = "Map/Atlas"
            if "Geography/Map/Rajasthan/" in rel:
                status_label = "Reference preview · not a validated final map"
                source_status = "The adjacent source audit says current multi-jurisdiction GIS geometry was not acquired; reference only, not final/official."
                notes = "Original retained unchanged. Consult the folder's input/source/QA audits before treating labels or borders as current."
            elif "/previews/" in rel:
                status_label = "GIS-derived atlas preview · needs verification"
                source_status = "Repository QA reports a GIS-derived atlas, but source authority, Pakistan vintage, open issues and visual-review gaps remain."
                notes = "Preview image; not an official or fully verified administrative map. See SOURCE_AUDIT.md, QA_REPORT.md and UNRESOLVED_DISCREPANCIES.md."
            else:
                status_label = "Generated map export · needs verification"
                source_status = "Derived export from the checked-in atlas workflow; underlying GIS data are ignored/untracked and the map source audit records unresolved issues."
                notes = "Full-size export; no corresponding PDF is tracked. Open in a new tab for zooming; see the map QA and source audits."
            items.append(resource(
                resource_id="geo-map-" + hashlib.sha256(rel.encode()).hexdigest()[:12],
                subject_id="rajasthan-geography",
                title=path.name,
                category=category,
                repo_path=rel,
                open_behavior="same_tab",
                source_status=source_status,
                source_status_label=status_label,
                source_status_state="warning",
                notes=notes,
            ))
        elif rel.endswith("SOURCES_REGISTER.csv"):
            items.append(resource(
                resource_id="geo-source-register-" + hashlib.sha256(rel.encode()).hexdigest()[:10],
                subject_id="rajasthan-geography",
                title=f"{path.parent.name or 'Geography'} source register (CSV)",
                category="Source Register",
                repo_path=rel,
                source_status="Existing source register; includes a mixture of official/secondary sources and disclosed acquisition limits.",
                source_status_label="Existing source register · read caveats",
                source_status_state="warning",
                notes="CSV is unchanged. The `Actually_inspected` / limitation fields are part of the source record; this integration did not re-fetch restricted source sites.",
            ))
        elif suffix == ".csv":
            items.append(resource(
                resource_id="geo-csv-" + hashlib.sha256(rel.encode()).hexdigest()[:12],
                subject_id="rajasthan-geography",
                title=path.name,
                category="Metadata/CSV",
                repo_path=rel,
                source_status="Existing source/derived metadata; boundary summary and relation values remain subject to the linked discrepancy and source audits.",
                source_status_label="Existing CSV · needs verification where noted",
                source_status_state="warning",
                notes="CSV source is linked without rewriting. Compare it with QA_REPORT.md, SOURCE_AUDIT.md and UNRESOLVED_DISCREPANCIES.md before treating values as definitive.",
            ))
        elif suffix == ".md":
            if "STRUCTURE_AND_ASSET_INVENTORY.md" == path.name:
                continue
            is_readme = path.name.lower() == "readme.md" or path.name.lower() == "first read.md"
            category = "Audit/QA" if not is_readme else "Audit/QA"
            items.append(resource(
                resource_id="geo-report-" + hashlib.sha256(rel.encode()).hexdigest()[:12],
                subject_id="rajasthan-geography",
                title=path.name,
                category=category,
                repo_path=rel,
                source_status="Existing geography source/QA documentation; several boundary claims and source limitations remain open.",
                source_status_label="Read with unresolved discrepancy notes",
                source_status_state="warning",
                notes="The two geography directory trees are distinct and preserved. This is a source/report file, not an independently verified boundary claim.",
            ))
        elif suffix == ".json" and rel.startswith("Rajasthan Geography Maps/data/metadata/"):
            items.append(resource(
                resource_id="geo-json-" + hashlib.sha256(rel.encode()).hexdigest()[:12],
                subject_id="rajasthan-geography",
                title=path.name,
                category="Metadata/CSV",
                repo_path=rel,
                source_status="Existing generated metadata; interpret alongside the source/QA audit.",
                source_status_label="Existing JSON metadata",
                source_status_state="warning",
                notes="Downloadable metadata file; source file preserved unchanged.",
            ))

    # Explicit, curated non-CN-book resources take precedence over broad folder discovery.
    items.extend(portal_items)

    # `tools/new` starter source PDFs are deliberately available only as collapsed legacy material.
    # Preserve deterministic order and stable IDs.
    unique = {}
    for item in items:
        if item["id"] in unique:
            raise ValueError(f"Duplicate resource ID: {item['id']}")
        unique[item["id"]] = item
    return sorted(unique.values(), key=lambda item: (
        item["subject_id"],
        item.get("topic_id", ""),
        item["category"],
        item["title"].casefold(),
        item["id"],
    ))


def make_maps(resources: list[dict], available: set[str], map_build: dict) -> dict:
    preview_repo = "Rajasthan Geography Maps/previews/Rajasthan_Border_District_Atlas_Preview.png"
    preview_thumb = "assets/catalog/rajasthan-border-atlas-preview.webp"
    full_a1 = "Rajasthan Geography Maps/exports/Rajasthan_Border_District_Atlas_A1.png"
    old_preview = "Geography/Map/Rajasthan/preview.webp"
    old_map = "Geography/Map/Rajasthan/54fc0d18-7435-4472-a101-941c1af1ec9a.jpeg"
    for path in (preview_repo, preview_thumb, full_a1, old_preview, old_map):
        existing(path)
    map_entries = [
        {
            "id": "rajasthan-border-atlas-preview",
            "title": "Rajasthan Border District Atlas — preview",
            "map_type": "preview",
            "subject_id": "rajasthan-geography",
            "preview_image_path": preview_thumb,
            "preview_image_url": encoded(preview_thumb),
            "original_repo_path": preview_repo,
            "original_url": encoded(preview_repo),
            "full_size_repo_path": full_a1,
            "full_size_url": encoded(full_a1),
            "image_alt": "Preview of the repository's Rajasthan border-district atlas: Rajasthan and neighbouring districts are shown in tinted regions, with highlighted state and international borders and Hindi labels. This is a study preview with unresolved source and verification issues.",
            "caption": "Existing GIS-derived atlas preview dated 2026-10-14 in its build metadata. The repository documents unresolved source, date, boundary and review issues; it is not an official or final verified map.",
            "source_status_label": "Preview only · source and boundary details need verification",
            "source_status": "needs_verification",
            "review_status": "needs_verification",
            "source_audit_repo_path": "Rajasthan Geography Maps/SOURCE_AUDIT.md",
            "qa_repo_path": "Rajasthan Geography Maps/reports/QA_REPORT.md",
            "discrepancy_repo_path": "Rajasthan Geography Maps/UNRESOLVED_DISCREPANCIES.md",
            "display_in_gallery": True,
            "image_open_behavior": "same_tab",
            "detail_route": "maps/rajasthan/index.html",
        },
        {
            "id": "rajasthan-input-feasibility-preview",
            "title": "Rajasthan geography input-audit preview",
            "map_type": "reference-preview",
            "subject_id": "rajasthan-geography",
            "preview_image_path": old_preview,
            "preview_image_url": encoded(old_preview),
            "original_repo_path": old_map,
            "original_url": encoded(old_map),
            "full_size_repo_path": old_map,
            "full_size_url": encoded(old_map),
            "image_alt": "An earlier Rajasthan regional map image with surrounding districts, from the separate Geography/Map/Rajasthan folder; its accompanying audit says it is not a validated final GIS map.",
            "caption": "Separate earlier reference image from `Geography/Map/Rajasthan/`. Its own input/source audit says the current multi-jurisdiction polygon data were not acquired and the map must not be presented as final.",
            "source_status_label": "Reference image · not a validated final map",
            "source_status": "needs_verification",
            "review_status": "needs_verification",
            "source_audit_repo_path": "Geography/Map/Rajasthan/SOURCE_AUDIT.md",
            "qa_repo_path": "Geography/Map/Rajasthan/QA_REPORT.md",
            "discrepancy_repo_path": "Geography/Map/Rajasthan/INPUT_AUDIT.md",
            "display_in_gallery": True,
            "image_open_behavior": "same_tab",
            "detail_route": "maps/rajasthan/index.html",
        },
    ]
    border_rows = read_csv("Rajasthan Geography Maps/data/metadata/BORDER_ONLY_DISTRICTS.csv")
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in border_rows:
        country = (row.get("country") or "").strip()
        region = (row.get("state_province") or "").strip()
        if country == "India" and region == "Rajasthan":
            continue
        grouped[(country, region)].append({
            "district_en": (row.get("district_en") or "").strip(),
            "district_hi": (row.get("district_hi") or "").strip(),
        })
    border_groups = [
        {
            "country": country,
            "neighbour_state_province": region,
            "districts": sorted(districts, key=lambda item: item["district_en"].casefold()),
        }
        for (country, region), districts in sorted(grouped.items(), key=lambda item: (item[0][0], item[0][1].casefold()))
    ]
    summary = read_csv("Rajasthan Geography Maps/data/metadata/BORDER_SUMMARY_BY_NEIGHBOUR.csv")
    border_summary = []
    for row in summary:
        border_summary.append({
            "neighbour_country": (row.get("neighbour_country") or "").strip(),
            "neighbour_state_province": (row.get("neighbour_state_province") or "").strip(),
            "districts_touching": int(float(row.get("districts_touching") or 0)),
            "source_status": "needs_verification",
        })
    official_sources = [
        {
            "title": "Rajasthan State Portal — state administrative overview",
            "url": "https://rajasthan.gov.in/",
            "open_behavior": "new_tab",
            "external_open_label": "opens in new tab",
            "note": "URL and 41-district reference are recorded in Geography/Map/Rajasthan/SOURCES_REGISTER.csv; not re-fetched during this integration.",
        },
        {
            "title": "Rajasthan 2026 District Disaster Management Plans",
            "url": "https://dmrelief.rajasthan.gov.in/content/raj/dmr/en/plans/district-dm-plans.html",
            "open_behavior": "new_tab",
            "external_open_label": "opens in new tab",
            "note": "Listed as an official count cross-check in the in-repository source audit; external availability was not tested here.",
        },
        {
            "title": "Vav-Tharad District Administration — About District",
            "url": "https://vavtharad.nic.in/about-district/",
            "open_behavior": "new_tab",
            "external_open_label": "opens in new tab",
            "note": "The existing input audit records this 2025 district change and says it borders Rajasthan; this integration did not fetch the external page or acquire matching updated polygons.",
        },
    ]
    return {
        "schema_version": 1,
        "generated_on": date.today().isoformat(),
        "map_build_date": map_build.get("build_date"),
        "map_page_route": "maps/rajasthan/index.html",
        "primary_map_id": "rajasthan-border-atlas-preview",
        "maps": map_entries,
        "border_summary": border_summary,
        "border_groups": border_groups,
        "boundary_csvs": [
            "Rajasthan Geography Maps/BOUNDARY_RELATIONS.csv",
            "Rajasthan Geography Maps/data/metadata/BORDER_ONLY_DISTRICTS.csv",
            "Rajasthan Geography Maps/data/metadata/BORDER_SUMMARY_BY_NEIGHBOUR.csv",
            "Rajasthan Geography Maps/data/metadata/BORDER_LENGTH_CROSSCHECK.csv",
            "Rajasthan Geography Maps/data/metadata/ACCEPTANCE_TESTS.csv",
        ],
        "official_sources": official_sources,
        "warnings": [
            {
                "id": "unofficial-source",
                "severity": "high",
                "text": "The atlas source audit identifies its India geometry as an unofficial Survey-of-India-derived republication with unresolved redistribution terms; the Pakistan district layer is COD-AB v01 valid 2022-09-09.",
                "repo_path": "Rajasthan Geography Maps/SOURCE_AUDIT.md",
            },
            {
                "id": "vav-tharad-change",
                "severity": "high",
                "text": "The separate Geography input/source audit records Vav-Tharad as created on 2025-10-02 and bordering southern Rajasthan; the checked-in atlas and border CSV need a dated reconciliation before their adjacent-district list is treated as current.",
                "repo_path": "Geography/Map/Rajasthan/SOURCE_AUDIT.md",
            },
            {
                "id": "open-discrepancies",
                "severity": "high",
                "text": "The atlas report lists seven open discrepancies, including the Pakistan neighbour list, published-vs-GIS border lengths, cross-source seams, disputed slivers, an unavailable gazette, the 2022 Pakistan snapshot and lack of human visual review.",
                "repo_path": "Rajasthan Geography Maps/UNRESOLVED_DISCREPANCIES.md",
            },
            {
                "id": "conflicting-audits",
                "severity": "high",
                "text": "The two Geography folders are not duplicates: one audit explicitly blocks final cartography due to missing current polygons, while the atlas folder contains a separately generated GIS preview and source/QA claims. Keep both source trees and reports intact.",
                "repo_path": "Rajasthan Geography Maps/STRUCTURE_AND_ASSET_INVENTORY.md",
            },
        ],
        "inventory_path": "Rajasthan Geography Maps/STRUCTURE_AND_ASSET_INVENTORY.md",
    }


def category_for(rel: str) -> str:
    p = pathlib.PurePosixPath(rel)
    parts = p.parts
    name = p.name
    suffix = p.suffix.lower()
    if rel.startswith("archive/") or rel.startswith("Computer Network/new/") or ".snapshot" in name:
        return "Archive/Legacy"
    if rel.startswith("Computer Network/Practice/"):
        return "Practice PDF" if suffix == ".pdf" else "Answer Key/Solutions" if "ANSWER" in name.upper() else "Archive/Legacy"
    if rel.startswith("Computer Network/Online Quiz/"):
        return "Interactive CBT" if "/v6/" in rel else "Archive/Legacy"
    if rel.startswith("Computer Network/Reports/"):
        return "Source Register" if "SOURCE_REGISTER" in name.upper() else "Audit/QA"
    if rel.startswith("Computer Network/Past Papers/Reference Books/") or rel.startswith("Computer Network/Past Papers/Question Banks/"):
        return "Reference Book"
    if rel.startswith("Computer Network/Past Papers/"):
        return "Past Paper"
    if rel.startswith("Computer Network/") and suffix == ".pdf":
        if "SOLUTION" in name.upper() or "ANSWER KEY" in name.upper():
            return "Answer Key/Solutions"
        if name.startswith("Topic ") or name.startswith("The Complete"):
            return "Theory/Notes"
        return "Past Paper"
    if rel.startswith("Computer Network/") and suffix == ".md" and (name.startswith("Topic ") or name.startswith("The Complete")):
        return "Theory/Notes"
    if rel.startswith("Geography/") or rel.startswith("Rajasthan Geography Maps/"):
        if suffix in (".png", ".jpeg", ".jpg", ".webp"):
            return "Map/Atlas"
        if suffix == ".csv":
            return "Source Register" if name == "SOURCES_REGISTER.csv" else "Metadata/CSV"
        if suffix == ".md":
            return "Audit/QA"
        if "/data/metadata/" in rel:
            return "Metadata/CSV"
    if rel.startswith("assets/") and (".min." in name or "/banks/" in rel):
        return "Generated browser data"
    if rel.startswith("data/reports/"):
        return "Generated QA/report"
    return "Repository / internal source"


def inventory_subject(rel: str) -> str:
    if rel.startswith("Computer Network/") or rel.startswith("assets/banks/cn/") or rel in ("assets/cn-questions.min.json", "assets/source-register.min.json", "assets/catalog.min.json"):
        return "Computer Network"
    if rel.startswith("Geography/") or rel.startswith("Rajasthan Geography Maps/"):
        return "Rajasthan Geography"
    if rel.startswith("assets/") or rel.startswith("subjects/") or rel.startswith("maps/") or rel.startswith("practice/") or rel.startswith("study-material/") or rel.startswith("sources/"):
        return "Shared portal"
    return "Repository QA/shared"


def visibility_for(rel: str, category: str) -> str:
    if rel.startswith("archive/") or rel.startswith("Computer Network/new/") or ".snapshot" in pathlib.PurePosixPath(rel).name:
        return "archive"
    if rel.startswith(("tools/", "tests/", "data/catalog/", "data/schemas/", "data/sources/", "tools/data/")):
        return "internal QA / not student-facing"
    if rel.startswith("Computer Network/Reports/") or rel.startswith("Rajasthan Geography Maps/reports/") or (rel.startswith("Geography/") and pathlib.PurePosixPath(rel).suffix.lower() in (".md", ".csv")):
        return "internal QA / publicly linked under Sources"
    if category in ("Map/Atlas", "Practice PDF", "Theory/Notes", "Past Paper", "Reference Book", "Interactive CBT", "Source Register", "Metadata/CSV"):
        return "public resource"
    if rel.startswith("assets/"):
        return "public site asset/data"
    if rel in ("README.md", "SITE_GUIDE.md", "COVERAGE.md", "CHANGELOG.md"):
        return "public documentation"
    return "repository source / not directly student-facing"


def classification_for(rel: str, category: str) -> str:
    path = pathlib.PurePosixPath(rel)
    name = path.name
    if rel.startswith("assets/css/") or rel.startswith("assets/js/") or rel.startswith("tools/") or rel.startswith("tests/"):
        return "source code"
    if rel.startswith("archive/") or ".snapshot" in name or rel.startswith("Computer Network/new/"):
        return "preserved source/archive"
    if rel.startswith("assets/catalog/") or rel.startswith("assets/banks/") or rel.startswith("data/reports/") or "/exports/" in rel or "/previews/" in rel or rel.startswith("Computer Network/Reports/"):
        return "generated/derived (reports or browser asset)"
    if rel == "Computer Network/data/cn_questions.json" or rel.startswith("data/catalog/") or rel.startswith("data/sources/"):
        return "canonical source data"
    if rel.startswith("Rajasthan Geography Maps/scripts/"):
        return "source code / reproducible workflow"
    if rel.startswith("Rajasthan Geography Maps/data/metadata/") or rel.startswith("Rajasthan Geography Maps/") and path.suffix.lower() == ".csv":
        return "derived source metadata (not edited by site build)"
    if category in ("Map/Atlas", "Past Paper", "Reference Book", "Practice PDF", "Theory/Notes"):
        return "existing source/student material"
    if rel.startswith("Geography/Map/Rajasthan/"):
        return "existing source/reference/report"
    if rel.startswith("assets/"):
        return "site source asset"
    return "existing source/document"


def report_note(rel: str) -> str:
    if rel == "Computer Network/data/cn_questions.json":
        return "Canonical CN bank; source type and answer-verification are distinct; see build manifest and reports."
    if rel.startswith("Geography/"):
        return "Separate geography input/audit tree. Its audit says current neighboring GIS polygons were not acquired; do not treat previews as a verified final map."
    if rel.startswith("Rajasthan Geography Maps/"):
        return "Separate atlas project tree. See source and unresolved-discrepancy audits; several source, date and boundary issues remain open."
    if rel.startswith("Computer Network/new/"):
        return "Preserved starter/older material, not automatically part of the published bank."
    if rel.startswith("archive/"):
        return "Pre-audit/archive snapshot retained for rollback and provenance; not a live public route."
    return "Existing repository file; see category, visibility and site-reference columns."


def collect_site_refs(resources: list[dict], maps_doc: dict, subjects_doc: dict, paths: list[str]) -> dict[str, set[str]]:
    refs: dict[str, set[str]] = defaultdict(set)
    for resource_item in resources:
        path = resource_item.get("repo_path")
        if not path:
            continue
        if resource_item["subject_id"] == "computer-network":
            refs[path].add("subjects/computer-network/index.html")
            if resource_item["category"] in ("Source Register", "Audit/QA", "Metadata/CSV"):
                refs[path].add("sources/index.html")
            if resource_item["category"] in ("Practice PDF", "Theory/Notes", "Reference Book"):
                refs[path].add("study-material/index.html")
            if resource_item["category"] == "Interactive CBT":
                refs[path].add("practice/index.html")
        elif resource_item["subject_id"] == "rajasthan-geography":
            refs[path].add("subjects/rajasthan-geography/index.html")
            if resource_item["category"] == "Map/Atlas":
                refs[path].add("maps/index.html")
                refs[path].add("maps/rajasthan/index.html")
            if resource_item["category"] in ("Source Register", "Audit/QA", "Metadata/CSV"):
                refs[path].add("sources/index.html")
        if "new" in pathlib.PurePosixPath(path).parts or resource_item["category"] == "Archive/Legacy":
            refs[path].add("subjects/computer-network/index.html (collapsed archive section)")
    for subject in subjects_doc.get("subjects", []):
        refs[subject["route"]].add("index.html; subjects/index.html")
    for map_entry in maps_doc.get("maps", []):
        for key in ("original_repo_path", "full_size_repo_path"):
            if map_entry.get(key):
                refs[map_entry[key]].add("index.html; subjects/rajasthan-geography/index.html; maps/index.html; maps/rajasthan/index.html")
        if map_entry.get("preview_image_path"):
            refs[map_entry["preview_image_path"]].add("index.html; subjects/rajasthan-geography/index.html; maps/index.html; maps/rajasthan/index.html")
    # Include literal local href/src references from all HTML pages.
    attr_pattern = re.compile(r"\b(?:href|src|poster)\s*=\s*['\"]([^'\"]+)['\"]", re.I)
    for rel in paths:
        if not rel.lower().endswith((".html", ".htm")):
            continue
        path = relative_file(rel)
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for raw in attr_pattern.findall(text):
            raw = html.unescape(raw).strip()
            parsed = urllib.parse.urlsplit(raw)
            if not parsed.path or parsed.scheme or parsed.netloc:
                continue
            decoded = urllib.parse.unquote(parsed.path)
            target = (path.parent / decoded).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                continue
            if target.is_file():
                refs[target.relative_to(ROOT).as_posix()].add(rel)
    return refs


def build_inventory(paths: list[str], resources: list[dict], maps_doc: dict, subjects_doc: dict) -> list[dict[str, str]]:
    refs = collect_site_refs(resources, maps_doc, subjects_doc, paths)
    hashes: dict[str, list[str]] = defaultdict(list)
    for rel in paths:
        path = relative_file(rel)
        if path.is_file():
            hashes[sha256(path)].append(rel)
    rows = []
    for rel in paths:
        if rel in INVENTORY_OUTPUTS:
            continue
        path = relative_file(rel)
        if not path.is_file():
            continue
        category = category_for(rel)
        dupe_paths = hashes[sha256(path)]
        duplicate = "Unique SHA-256 in current repo" if len(dupe_paths) == 1 else "Identical bytes: " + " | ".join(p for p in dupe_paths if p != rel)
        reference_list = sorted(refs.get(rel, set()))
        linked = "Yes — " + "; ".join(reference_list) if reference_list else "No direct link from current site/catalog"
        rows.append({
            "path": rel,
            "extension_or_type": type_for(rel),
            "size_bytes": str(path.stat().st_size),
            "subject": inventory_subject(rel),
            "student_facing_category": category,
            "visibility": visibility_for(rel, category),
            "source_generated_classification": classification_for(rel, category),
            "linked_on_site": linked,
            "sha256": sha256(path),
            "image_dimensions": image_dimensions(path) if path.suffix.lower() in (".png", ".jpeg", ".jpg", ".webp") else "",
            "notes_status": report_note(rel),
            "identical_copy_status": duplicate,
        })
    return rows


def markdown_inventory(paths: list[str], inventory_rows: list[dict[str, str]]) -> str:
    subset = [row for row in inventory_rows if row["path"].startswith(("Geography/", "Rajasthan Geography Maps/"))]
    lines = [
        "# Rajasthan Geography — Structure and Asset Inventory",
        "",
        f"**Generated:** {date.today().isoformat()} from repository paths and bytes. **Files inventoried:** {len(subset)}.",
        "",
        "This report documents two distinct source trees. No files were moved, merged, renamed or rewritten by the catalogue builder. The atlas preview/exports are present as raster files, but the source audit records unresolved source vintage, authority, boundary and visual-review issues. The earlier `Geography/Map/Rajasthan/` audit separately says the current multi-jurisdiction polygons were not acquired; its images are not accepted as a verified final map.",
        "",
        "`Identical-copy status` is SHA-256 byte equality across the two geography trees and all other files in this repository snapshot. A unique hash does not prove the maps depict different geography; it only means the files are not byte-identical.",
        "",
        "`Current website references` lists routes/catalogues that expose the resource. `No direct link` means retained source/build material remains in the repository but is not intentionally student-facing.",
        "",
        "| Path | File type | Size (bytes) | SHA-256 | Image dimensions | Role | Identical-copy status | Current website references |",
        "|---|---|---:|---|---|---|---|---|",
    ]
    for row in subset:
        values = [row["path"], row["extension_or_type"], row["size_bytes"], row["sha256"], row["image_dimensions"] or "—", row["student_facing_category"], row["identical_copy_status"], row["linked_on_site"]]
        escaped = [value.replace("|", "\\|").replace("\n", " ") for value in values]
        lines.append("| " + " | ".join(escaped) + " |")
    lines += [
        "",
        "## Role/status notes",
        "",
        "- `Map/Atlas` images are separately labelled preview, generated export, or reference-only in the resource manifest; none is described as official or fully verified.",
        "- `Metadata/CSV` and source registers are linked without changing their source bytes. Summary values are marked **Needs verification** on the site because the audits contain conflicts and an update gap.",
        "- Atlas-related reports, metadata and scripts are retained under `Rajasthan Geography Maps/`; older reference images and audits remain under `Geography/Map/Rajasthan/`.",
        "- See `Rajasthan Geography Maps/SOURCE_AUDIT.md`, `Rajasthan Geography Maps/UNRESOLVED_DISCREPANCIES.md`, `Rajasthan Geography Maps/reports/QA_REPORT.md`, and `Geography/Map/Rajasthan/SOURCE_AUDIT.md` for scope and limitations.",
        "",
    ]
    return "\n".join(lines)


def write_json(path: pathlib.Path, data: dict, check: bool) -> None:
    content = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if check:
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            raise SystemExit(f"STALE: {path.relative_to(ROOT)}; run python3 tools/build_catalog.py")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def write_csv(path: pathlib.Path, rows: list[dict[str, str]], check: bool) -> None:
    fieldnames = [
        "path", "extension_or_type", "size_bytes", "subject", "student_facing_category",
        "visibility", "source_generated_classification", "linked_on_site", "sha256",
        "image_dimensions", "notes_status", "identical_copy_status",
    ]
    from io import StringIO
    stream = StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    content = stream.getvalue()
    if check:
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            raise SystemExit(f"STALE: {path.relative_to(ROOT)}; run python3 tools/build_catalog.py")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="compare generated outputs without writing")
    args = parser.parse_args()

    paths = repo_paths()
    available = set(paths)
    build = json_read(existing("data/reports/build_manifest.json"))
    bank = json_read(existing("assets/banks/cn/manifest.json"))
    map_build = json_read(existing("Rajasthan Geography Maps/data/metadata/BUILD_METADATA.json"))
    books_doc = json_read(existing("data/catalog/books.json"))
    portal_resource_source = json_read(existing("data/catalog/portal_resources.json"))
    if build.get("canonical_sha256") != sha256(existing("Computer Network/data/cn_questions.json")):
        raise SystemExit("Canonical bank SHA-256 does not match data/reports/build_manifest.json; run the documented CN builder/review before publishing.")
    if build.get("bank_build_id") != bank.get("bank_build_id"):
        raise SystemExit("CN bank build ID mismatch between build manifest and topic manifest.")

    subjects_doc = make_subjects(build, map_build, available)
    if any(item["status"] != "live" for item in subjects_doc["subjects"]):
        raise SystemExit("A requested subject failed its required route/resource existence check; inspect the message above.")
    geo_rows = read_csv("Rajasthan Geography Maps/data/metadata/BORDER_ONLY_DISTRICTS.csv")
    resources = make_resources(paths, build, books_doc, geo_rows, portal_resource_source)
    maps_doc = make_maps(resources, available, map_build)

    write_json(CATALOG / "subjects.json", subjects_doc, args.check)
    write_json(CATALOG / "resources.json", {
        "schema_version": 1,
        "generated_on": date.today().isoformat(),
        "path_semantics": "repo_path is an exact repository-relative path; url is a project-root-relative, URL-encoded path resolved by assets/js/app.js against the current GitHub Pages project base.",
        "availability_status_values": ["available", "retired_redirect", "needs_verification", "unavailable"],
        "open_behavior_values": ["same_tab", "new_tab"],
        "categories": [
            "Theory/Notes", "Practice PDF", "Answer Key/Solutions", "Interactive CBT", "Past Paper",
            "Reference Book", "Map/Atlas", "Source Register", "Audit/QA", "Metadata/CSV",
            "Archive/Legacy", "Planned/Under Review",
        ],
        "resources": resources,
    }, args.check)
    write_json(CATALOG / "maps.json", maps_doc, args.check)

    # Refresh after writing manifests so the inventory includes the actual generated
    # catalogue files. Its own two output files are excluded to avoid self-hashes.
    paths = repo_paths()
    inventory_rows = build_inventory(paths, resources, maps_doc, subjects_doc)
    write_csv(REPORTS / "portal_repository_inventory.csv", inventory_rows, args.check)
    inventory_md = markdown_inventory(paths, inventory_rows)
    inventory_path = ATLAS_DIR / "STRUCTURE_AND_ASSET_INVENTORY.md"
    if args.check:
        if not inventory_path.is_file() or inventory_path.read_text(encoding="utf-8") != inventory_md:
            raise SystemExit(f"STALE: {inventory_path.relative_to(ROOT)}; run python3 tools/build_catalog.py")
    else:
        inventory_path.write_text(inventory_md, encoding="utf-8")
    print(f"PASS: built {len(subjects_doc['subjects'])} subject entries, {len(resources)} real resource records, {len(maps_doc['maps'])} map records, and {len(inventory_rows)} repository inventory rows.")
    print("Outputs: assets/catalog/{subjects,resources,maps}.json; data/reports/portal_repository_inventory.csv; Rajasthan Geography Maps/STRUCTURE_AND_ASSET_INVENTORY.md")


if __name__ == "__main__":
    main()
