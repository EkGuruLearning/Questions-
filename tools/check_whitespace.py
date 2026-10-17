#!/usr/bin/env python3
"""Check changed and untracked text files for trailing spaces/tabs.

`maintainer/` and `archive/` hold preserved original material (audits, GIS scripts,
source registers, old snapshots). Hash-verified `library/third_party/` sources and
`assets/library/licenses/` notices also preserve upstream bytes, including Markdown
hard line breaks and CRLF. These precise namespaces are skipped, not library code/docs.
"""
from __future__ import annotations
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

def git_paths(*args: str) -> set[str]:
    raw = subprocess.check_output(["git", *args, "-z"], cwd=ROOT)
    return {item.decode("utf-8") for item in raw.split(b"\0") if item}

def main():
    paths = set()
    paths |= git_paths("diff", "--name-only")
    paths |= git_paths("diff", "--cached", "--name-only")
    paths |= git_paths("ls-files", "--others", "--exclude-standard")
    errors = []
    for relative in sorted(paths):
        path = ROOT / relative
        if not path.is_file() or relative.startswith(("archive/", "maintainer/", "library/third_party/", "assets/library/licenses/")):
            continue
        raw = path.read_bytes()
        if b"\0" in raw:
            continue
        for number, line in enumerate(raw.split(b"\n"), 1):
            if line.endswith((b" ", b"\t", b"\r")):
                errors.append(f"{relative}:{number}: trailing whitespace")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: changed text files contain no trailing whitespace ({len(paths)} paths inspected; preserved maintainer/archive/upstream originals excluded).")

if __name__ == "__main__":
    main()
