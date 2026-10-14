#!/usr/bin/env python3
"""Store archived HTML byte-for-byte with a non-runnable .snapshot suffix."""
from __future__ import annotations
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "archive"

def main():
    changed = 0
    for source in sorted(ARCHIVE.rglob("*.html")):
        destination = source.with_name(source.name + ".snapshot")
        if destination.exists():
            if source.read_bytes() != destination.read_bytes():
                raise SystemExit(f"Refusing to overwrite a different archived copy: {destination}")
            source.unlink()
        else:
            source.rename(destination)
        changed += 1
    remaining = list(ARCHIVE.rglob("*.html"))
    if remaining:
        raise SystemExit(f"Runnable HTML remains in archive: {remaining[0]}")
    print(f"PASS: {changed} archived HTML file(s) are preserved byte-for-byte as inert .html.snapshot files.")

if __name__ == "__main__":
    main()
