#!/usr/bin/env python3
"""Print the website file map or run the one-command structure/merge preflight."""
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED_PATHS = (
    "index.html",
    "subjects/index.html",
    "subjects/computer-network/index.html",
    "subjects/rajasthan-geography/index.html",
    "maps/index.html",
    "maps/rajasthan/index.html",
    "practice/index.html",
    "study-material/index.html",
    "sources/index.html",
    "guides/repository-structure/index.html",
    "assets/css/site.css",
    "assets/js/app.js",
    "assets/catalog/subjects.json",
    "assets/catalog/resources.json",
    "assets/catalog/maps.json",
    "assets/banks/cn/manifest.json",
    "Computer Network/data/cn_questions.json",
    "Computer Network/Topics/README.md",
    "data/catalog/books.json",
    "data/catalog/portal_resources.json",
    "data/catalog/subjects.json",
    "tools/build_catalog.py",
    "tools/validate_links.py",
    "tools/validate_assets.py",
    "tools/validate_subjects.py",
)
PREFLIGHT_COMMANDS = (
    ("Generated catalogues and inventories", [sys.executable, "tools/build_catalog.py", "--check"]),
    ("GitHub Pages links and project-base paths", [sys.executable, "tools/validate_links.py"]),
    ("Resource files, hashes and map metadata", [sys.executable, "tools/validate_assets.py"]),
    ("Subject/topic publication gates", [sys.executable, "tools/validate_subjects.py"]),
    ("Whitespace and conflict markers", [sys.executable, "tools/check_whitespace.py"]),
    ("Git diff whitespace", ["git", "diff", "--check"]),
    ("Staged diff whitespace", ["git", "diff", "--cached", "--check"]),
)

GUIDE = r"""
EkGuru repository structure / वेबसाइट की फाइल संरचना

PUBLIC WEBSITE ROUTES — browser इन्हीं HTML routes को खोलता है:
  index.html                                  home / विषय सूची
  subjects/computer-network/index.html        Computer Network subject page
  subjects/rajasthan-geography/index.html     Rajasthan Geography resource page
  maps/                                       map catalogue and detail routes
  practice/index.html                        shared CN practice app
  study-material/ and sources/                 resource and evidence pages
  guides/repository-structure/index.html      this reader-friendly file guide

WEBSITE CODE AND DATA FLOW:
  assets/css/site.css + assets/js/app.js      shared catalogue-site presentation
  assets/css/portal.css + assets/js/app.mjs   existing practice-player UI
  data/catalog/*.json                         editable catalogue source inputs
  assets/catalog/*.json                       generated manifests read by app.js
  Computer Network/data/cn_questions.json     canonical CN question records
  assets/banks/cn/manifest.json + TNN chunks  generated; practice app loads selected topic
  data/catalog/books.json                     maps CN topic PDFs/launchers to topic IDs
  data/catalog/portal_resources.json          registers curated non-book add-on resources

SOURCE MATERIAL (keep originals in place):
  Computer Network/Incoming/                   question-source intake; not published as approved content
  Computer Network/Topics/T01 ... T07/         recommended home for new topic study PDFs
  Computer Network/Practice/                   existing practice PDFs / answer aids
  Computer Network/Past Papers/                existing papers, references and source notes
  Computer Network/Reports/                    CN inventory, evidence, QA and release reports
  Rajasthan Geography Maps/                    atlas project, exports, CSVs, audits and workflow
  Geography/Map/Rajasthan/                     separate older geography source/audit tree; do not merge
  tools/ and tests/                            builders, validators and tests; not student material
  archive/                                      preserved snapshots; never edit as current source

FOR EACH CN TOPIC:
  T01  Introduction of Data Communication       Computer Network/Topics/T01/
  T02  Network Models: OSI & TCP/IP             Computer Network/Topics/T02/
  T03  Addressing: MAC, IPv4, IPv6, Ports, DNS   Computer Network/Topics/T03/
  T04  Networking Devices                       Computer Network/Topics/T04/
  T05  Transmission Medium                      Computer Network/Topics/T05/
  T06  OSI Layers in Detail                     Computer Network/Topics/T06/
  T07  Network Security                         Computer Network/Topics/T07/

IMPORTANT: adding a file is not the same as publishing it. Add the exact path and
status to the correct source catalogue, rebuild generated manifests, then run:
  python3 tools/read_structure.py --check

For the bilingual website guide and the safe next-repository merge checklist, open:
  guides/repository-structure/index.html
""".strip()


def unmerged_paths() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-u", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    paths = []
    for item in result.stdout.split(b"\0"):
        if not item:
            continue
        record = item.decode("utf-8", errors="replace")
        paths.append(record.split("\t", 1)[-1])
    return paths


def run_check() -> int:
    print("EkGuru structure / merge preflight — read-only")
    print("Repository:", ROOT)
    conflicts = unmerged_paths()
    if conflicts:
        print(f"FAIL: {len(conflicts)} unmerged path entr(y/ies); resolve or abort the merge first:")
        for entry in conflicts:
            print(" -", entry)
        print("After resolving, rerun this command. To discard an in-progress merge, use `git merge --abort`.")
        return 1
    print("PASS: git index has no unresolved merge-conflict entries.")

    missing = [rel for rel in REQUIRED_PATHS if not (ROOT / rel).is_file()]
    if missing:
        print(f"FAIL: {len(missing)} required route/source/tool path(s) are missing:")
        for rel in missing:
            print(" -", rel)
        print("Do not publish until the route, source catalogue, and generated assets are restored.")
        return 1
    print(f"PASS: all {len(REQUIRED_PATHS)} required website, catalogue, source and validator paths exist.")

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
        print(f"\nNOT READY: {failures} structural preflight check(s) failed. Fix the source/path issue, rebuild if needed, and rerun this command.")
        return 1
    print("\nREADY: repository structure, project-base links, generated catalogues and publication gates are consistent.")
    print("This preflight does not run all data, browser, PDF, deployment or post-deployment tests; use tools/run_release_checks.py for release QA.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="run read-only route/catalogue/merge preflight checks")
    args = parser.parse_args()
    if args.check:
        return run_check()
    print(GUIDE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
