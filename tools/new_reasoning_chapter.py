#!/usr/bin/env python3
"""Naya Reasoning chapter — chaaron folder ek command me taiyar.

Aapke paas chapter ki PDFs hon to unhe daalna asaan ho jaye: ye script chapter ka
folder chaaron folders me bana deti hai (`theory/`, `practice/`, `answers/`, `tests/`),
aur `.gitkeep` rakh deti hai taaki GitHub par folder turant dikhe aur aap upload kar sako.

    python3 tools/new_reasoning_chapter.py "Time and Work"
    python3 tools/new_reasoning_chapter.py "Time and Work" "Calendar"      # ek saath kai

Phir PDFs daaliye (naam se hi title ban jata hai):

    content/reasoning/theory/Time-and-Work/Time-and-Work-Notes.pdf
    content/reasoning/practice/Time-and-Work/Time-and-Work-Practice.pdf
    content/reasoning/answers/Time-and-Work/Time-and-Work-Answer-Key.pdf
    content/reasoning/tests/Time-and-Work/Time-and-Work-Test.pdf

Aur site bana dijiye (teen command):

    python3 tools/build_catalog.py && python3 tools/build_pages.py && python3 tools/build_site_routes.py

Chapter ka folder bina file ke bhi site par dikhta hai ("jald aa raha hai"), isliye
aap aaram se baad me PDFs daal sakte hain.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REASONING = ROOT / "content" / "reasoning"
CHAPTERS = ("theory", "practice", "answers", "tests")


def slugify(name: str) -> str:
    """`Time and Work` -> `Time-and-Work` -> `Time-And-Work`."""
    words = re.split(r"[\s_]+", name.strip())
    cleaned = []
    for word in words:
        piece = re.sub(r"[^A-Za-z0-9\u0900-\u097F-]", "", word)
        if piece:
            cleaned.append(piece[:1].upper() + piece[1:])
    return "-".join(cleaned) or "Chapter"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("chapters", nargs="+", help="chapter ka naam, e.g. \"Time and Work\"")
    parser.add_argument("--dry-run", action="store_true", help="sirf dikhao, kuch likho nahi")
    args = parser.parse_args()

    if not REASONING.is_dir():
        raise SystemExit(f"FAIL: {REASONING.relative_to(ROOT)}/ nahi mila")
    created = 0
    for chapter in args.chapters:
        slug = slugify(chapter)
        for folder in CHAPTERS:
            target = REASONING / folder / slug
            if target.is_dir():
                print(f"  (pehle se hai) {target.relative_to(ROOT).as_posix()}")
                continue
            if args.dry_run:
                print(f"  + {target.relative_to(ROOT).as_posix()}")
            else:
                target.mkdir(parents=True)
                (target / ".gitkeep").write_text("", encoding="utf-8")
                print(f"  + {target.relative_to(ROOT).as_posix()}")
            created += 1

    print(f"\n{created} folder bana. Ab PDFs in folders me daaliye, phir:")
    print("  python3 tools/build_catalog.py && python3 tools/build_pages.py && python3 tools/build_site_routes.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
