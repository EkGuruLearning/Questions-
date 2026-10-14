#!/usr/bin/env python3
"""Validate catalogue file paths, hashes and map image metadata."""
from __future__ import annotations

import hashlib
import json
import pathlib
import re
import subprocess
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent


def read_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def sha256(path: pathlib.Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def image_dimensions(path: pathlib.Path) -> tuple[int, int] | None:
    try:
        result = subprocess.run(
            ["identify", "-format", "%w %h", str(path)],
            check=True,
            text=True,
            capture_output=True,
            timeout=20,
        )
        parts = result.stdout.strip().split()
        if len(parts) == 2:
            return int(parts[0]), int(parts[1])
    except (FileNotFoundError, subprocess.SubprocessError, ValueError):
        pass
    data = path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")
    if data[:2] == b"\xff\xd8":
        index = 2
        while index + 9 < len(data):
            if data[index] != 0xFF:
                index += 1
                continue
            marker = data[index + 1]
            index += 2
            if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
                continue
            if index + 2 > len(data):
                return None
            size = int.from_bytes(data[index:index + 2], "big")
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                if index + 7 <= len(data):
                    return int.from_bytes(data[index + 5:index + 7], "big"), int.from_bytes(data[index + 3:index + 5], "big")
                return None
            index += max(size, 2)
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP" and data[12:16] == b"VP8X" and len(data) >= 30:
        return int.from_bytes(data[24:27], "little") + 1, int.from_bytes(data[27:30], "little") + 1
    return None


def main() -> None:
    errors: list[str] = []
    resources_doc = read_json("assets/catalog/resources.json")
    maps_doc = read_json("assets/catalog/maps.json")
    subjects_doc = read_json("assets/catalog/subjects.json")
    checked_resources = 0
    checked_images = 0
    total_bytes = 0

    for resource in resources_doc.get("resources", []):
        rel = resource.get("repo_path", "")
        path = (ROOT / pathlib.PurePosixPath(rel)).resolve()
        try:
            path.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"Resource path escapes repository: {rel}")
            continue
        if not path.is_file():
            errors.append(f"Missing resource file: {rel}")
            continue
        checked_resources += 1
        total_bytes += path.stat().st_size
        if resource.get("bytes") != path.stat().st_size:
            errors.append(f"Resource byte count stale for {rel}: {resource.get('bytes')} != {path.stat().st_size}")
        if resource.get("sha256") != sha256(path):
            errors.append(f"Resource SHA-256 stale for {rel}")
        if resource.get("category") == "Map/Atlas" and path.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"):
            checked_images += 1
            dims = image_dimensions(path)
            if not dims or min(dims) <= 0:
                errors.append(f"Map image dimensions could not be read: {rel}")
            if not (resource.get("image_alt") or "").strip():
                errors.append(f"Map image is missing descriptive alt text: {rel}")
            if resource.get("open_behavior") == "new_tab" and not resource.get("external_open_label"):
                errors.append(f"Map image new-tab link is not labelled: {rel}")

    map_paths = []
    for item in maps_doc.get("maps", []):
        if item.get("display_in_gallery") and not item.get("image_alt", "").strip():
            errors.append(f"Gallery map lacks alt text: {item.get('id')}")
        for key in ("preview_image_path", "original_repo_path", "full_size_repo_path"):
            rel = item.get(key)
            if not rel:
                continue
            path = (ROOT / pathlib.PurePosixPath(rel)).resolve()
            if not path.is_file():
                errors.append(f"Map {item.get('id')} references missing {key}: {rel}")
            else:
                map_paths.append((item.get("id"), key, rel, path))
                if path.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"):
                    dims = image_dimensions(path)
                    if not dims or dims[0] <= 0 or dims[1] <= 0:
                        errors.append(f"Map {item.get('id')} image has unreadable dimensions: {rel}")
        if item.get("review_status") != "needs_verification":
            errors.append(f"Map {item.get('id')} was promoted without an audit review: {item.get('review_status')}")
        if item.get("source_status") != "needs_verification":
            errors.append(f"Map {item.get('id')} must retain the unresolved source status")

    primary = next((item for item in maps_doc.get("maps", []) if item.get("id") == maps_doc.get("primary_map_id")), None)
    if not primary:
        errors.append("maps.json primary_map_id does not match a map entry")
    else:
        preview = (ROOT / primary["preview_image_path"]).resolve()
        original = (ROOT / primary["original_repo_path"]).resolve()
        thumb_dimensions = image_dimensions(preview)
        original_dimensions = image_dimensions(original)
        if thumb_dimensions and original_dimensions:
            thumb_ratio = thumb_dimensions[0] / thumb_dimensions[1]
            original_ratio = original_dimensions[0] / original_dimensions[1]
            if abs(thumb_ratio - original_ratio) > 0.005:
                errors.append(f"Optimized preview aspect ratio differs from its source: {thumb_ratio:.5f} vs {original_ratio:.5f}")
        if not str(primary.get("full_size_url", "")).endswith(".png"):
            errors.append("Primary full-size map action must point to an existing PNG image export")

    # Ensure the shared site CSS never crops or stretches map labels/boundaries.
    css = (ROOT / "assets/css/site.css").read_text(encoding="utf-8")
    if not re.search(r"\.map-frame\s+img\s*\{[^}]*height:\s*auto", css, re.S):
        errors.append("Shared CSS must keep map previews at height:auto")
    if not re.search(r"img,\s*svg,\s*video\s*\{[^}]*max-width:\s*100%", css, re.S):
        errors.append("Shared CSS must constrain images responsively")

    print(f"Checked resources={checked_resources}, map images={checked_images}, total referenced bytes={total_bytes:,}, map entries={len(maps_doc.get('maps', []))}, live subjects={sum(item.get('status') == 'live' for item in subjects_doc.get('subjects', []))}.")
    if errors:
        print(f"FAIL: {len(errors)} asset/catalogue issue(s)")
        for error in errors:
            print(" -", error)
        raise SystemExit(1)
    print("PASS: resource hashes, path availability, image dimensions/alt text and responsive map aspect ratios.")


if __name__ == "__main__":
    main()
