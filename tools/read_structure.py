#!/usr/bin/env python3
"""Print the EkGuru site/repository map, or run the read-only structure preflight."""
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

REQUIRED_PATHS = (
    # published pages
    "index.html",
    "404.html",
    "subjects/index.html",
    "subjects/computer-network/index.html",
    "subjects/computer-network/material/index.html",
    "subjects/computer-network/test/index.html",
    "subjects/rajasthan-geography/index.html",
    # site code and data
    "assets/css/ekguru.css",
    "assets/js/site.js",
    "assets/js/test.mjs",
    "assets/js/engine.mjs",
    "assets/img/rajasthan-border-atlas-preview.webp",
    "data/thumbs/manifest.json",
    "data/site.json",
    "data/banks/cn/cn_questions.json",
    "data/banks/cn/manifest.json",
    # editable catalogue inputs
    "data/catalog/subjects.json",
    "data/catalog/materials.json",
    "data/catalog/site-routes.txt",
    # student content roots
    "content/computer-network/theory",
    "content/computer-network/practice",
    "content/computer-network/answers",
    "content/computer-network/tests",
    "content/computer-network/reference",
    "content/rajasthan-geography/map/rajasthan",
    # builders and validators
    "tools/build_catalog.py",
    "tools/build_site_data.py",
    "tools/validate_site.py",
    "tools/validate_question_bank.py",
)

PREFLIGHT_COMMANDS = (
    ("Bank chunks are current", [sys.executable, "tools/build_site_data.py", "--check"]),
    ("Site data is current", [sys.executable, "tools/build_catalog.py", "--check"]),
    ("Published routes, links and downloads", [sys.executable, "tools/validate_site.py"]),
    ("Question bank and evidence gate", [sys.executable, "tools/validate_question_bank.py"]),
    ("Whitespace and conflict markers", [sys.executable, "tools/check_whitespace.py"]),
    ("Git diff whitespace", ["git", "diff", "--check"]),
    ("Staged diff whitespace", ["git", "diff", "--cached", "--check"]),
)

GUIDE = r"""
EkGuru Learning — repository structure / वेबसाइट की फाइल संरचना

STUDENTS JO DEKHTE HAIN (website routes):
  index.html                                       home
  subjects/index.html                              saare subjects
  subjects/computer-network/index.html             CN home (Material / Test)
  subjects/computer-network/material/index.html     study material (PDF downloads)
  subjects/computer-network/test/index.html         online test (topic-wise + full mix)
  subjects/rajasthan-geography/index.html           Rajasthan map atlas
  404.html                                          purane link ke liye friendly page

STUDENT FILES (only these get published) — folder structure = website structure:
  content/computer-network/theory/     📘 Theory: T01..T07 + complete book (PDF)
  content/computer-network/practice/   ✍️ Practice questions: T01..T07 booklets (PDF)
  content/computer-network/answers/    ✅ Answers & explanations: answer key + solutions (PDF)
  content/computer-network/tests/      🧾 Tests: topic/unit/subject test papers (PDF)
  content/computer-network/reference/  📚 Reference book (PDF)
  content/rajasthan-geography/map/     🗂️ Map folder
    rajasthan/                           🗺️ Rajasthan ke maps (PNG: A1..A4 + preview)

SITE CODE AND DATA:
  assets/css/ekguru.css                one stylesheet for every page
  assets/js/site.js                    renders topic/material/map lists from data/site.json
  assets/js/test.mjs                   online test app (player, result, review)
  assets/js/engine.mjs                 pure question-engine helpers
  data/site.json                       generated page data (counts, titles, file hashes)
  data/banks/cn/cn_questions.json      canonical Computer Network bank (schema v2)
  data/banks/cn/manifest.json          generated topic manifest
  data/banks/cn/T0N.<hash>.min.json    generated topic chunks (test page fetches one at a time)

EDITABLE CATALOGUE INPUTS (yahan likho, phir rebuild karo):
  data/catalog/subjects.json           subject/topic titles + folder labels (icon, English/Hindi note)
  data/catalog/materials.json          har downloadable file ka record + label
  data/catalog/site-routes.txt         published page list used by the link validator

SAFELY HIDDEN (never linked from the website):
  maintainer/computer-network/         audits, reports, intake, legacy apps, past papers
  maintainer/rajasthan-geography/      GIS project, scripts, audits, metadata exports
  maintainer/reports/                  generated audit reports
  maintainer/archive/                  preserved older snapshots
  tools/  tests/                       builders, validators and tests

HOW TO ADD A FILE (e.g. a new topic PDF):
  1. File rakho:          content/computer-network/theory/T08-...-Theory-MCQ.pdf
  2. Entry add karo:      data/catalog/materials.json (subject, topic, title_en, title_hi)
  3. Rebuild + validate:  python3 tools/build_thumbs.py && python3 tools/build_catalog.py && python3 tools/validate_site.py
                          (image add ki ho to build_thumbs pehle — preview banata hai)
  (Naya folder banao to uska label data/catalog/subjects.json ke `folders` me likhna zaroori hai,
   warna website par wahi folder card apne aap ban jayega — bina page code chhue.)
  (Registry check: agar file register nahi hui ya registered file gayab hai, build fail ho jayega.)

HOW TO REBUILD THE QUESTION BANK:
  python3 tools/build_site_data.py     # canonical bank -> chunks + manifest
  python3 tools/build_catalog.py       # chunks + catalogue -> data/site.json
  python3 tools/read_structure.py --check
"""


def unmerged_paths() -> list[str]:
    result = subprocess.run(["git", "ls-files", "-u", "-z"], cwd=ROOT, check=True, capture_output=True)
    return [item.decode("utf-8", errors="replace").split("\t", 1)[-1]
            for item in result.stdout.split(b"\0") if item]


def run_check() -> int:
    print("EkGuru structure preflight — read-only")
    print("Repository:", ROOT)
    conflicts = unmerged_paths()
    if conflicts:
        print(f"FAIL: {len(conflicts)} unmerged path(s); resolve or abort the merge first:")
        for entry in conflicts:
            print(" -", entry)
        return 1
    print("PASS: git index has no unresolved merge-conflict entries.")

    missing = [rel for rel in REQUIRED_PATHS if not (ROOT / rel).exists()]
    if missing:
        print(f"FAIL: {len(missing)} required path(s) are missing:")
        for rel in missing:
            print(" -", rel)
        return 1
    print(f"PASS: all {len(REQUIRED_PATHS)} required site/content/catalogue paths exist.")

    failures = 0
    for label, command in PREFLIGHT_COMMANDS:
        print(f"\n--- {label} ---", flush=True)
        result = subprocess.run(command, cwd=ROOT)
        if result.returncode:
            failures += 1
            print(f"FAIL: {label} (exit {result.returncode})")
        else:
            print(f"PASS: {label}")
    if failures:
        print(f"\nNOT READY: {failures} preflight check(s) failed.")
        return 1
    print("\nREADY: structure, generated data, links and downloads are consistent.")
    print("This preflight does not replace the unit tests or a browser check on the live site.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="run the read-only structure preflight")
    args = parser.parse_args()
    if args.check:
        return run_check()
    print(GUIDE.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
