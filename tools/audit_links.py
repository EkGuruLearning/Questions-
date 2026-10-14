#!/usr/bin/env python3
"""Validate local static links, anchors, assets and new-tab safety."""
from __future__ import annotations

import argparse
import html.parser
import json
import pathlib
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent


class Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        for attr in ("href", "src", "poster", "action"):
            if a.get(attr) is not None:
                self.links.append({"tag": tag, "attr": attr, "value": a[attr], "target": a.get("target"), "rel": a.get("rel", "")})

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


def check_html(path: pathlib.Path, errors: list[str], counts: dict):
    parser = Links()
    try:
        parser.feed(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: HTML parse error: {exc}")
        return
    counts["html_files"] += 1
    counts["references"] += len(parser.links)
    for item in parser.links:
        raw = (item["value"] or "").strip()
        if not raw or raw == "#":
            errors.append(f"{path.relative_to(ROOT)}: dead/empty {item['attr']}={raw!r}")
            continue
        rel = {token.lower() for token in item["rel"].split()}
        if item["target"] == "_blank" and not {"noopener", "noreferrer"}.issubset(rel):
            errors.append(f"{path.relative_to(ROOT)}: target=_blank lacks rel=noopener noreferrer: {raw}")
        parsed = urllib.parse.urlsplit(raw)
        if parsed.scheme.lower() in ("mailto", "tel", "data", "javascript"):
            if parsed.scheme.lower() == "javascript":
                errors.append(f"{path.relative_to(ROOT)}: javascript: URL is not allowed")
            continue
        if parsed.scheme or parsed.netloc:
            continue
        if item["attr"] == "action" and not parsed.path:
            continue
        decoded_path = urllib.parse.unquote(parsed.path)
        if decoded_path:
            target = (path.parent / decoded_path).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: local URL escapes repository: {raw}")
                continue
            if not target.is_file() and not target.is_dir():
                errors.append(f"{path.relative_to(ROOT)}: missing local target {raw}")
                continue
            counts["local_files"] += 1
            if parsed.fragment and target.is_file() and target.suffix.lower() in (".html", ".htm"):
                sub = Links()
                try:
                    sub.feed(target.read_text(encoding="utf-8"))
                except Exception as exc:
                    errors.append(f"{target.relative_to(ROOT)}: cannot parse anchor target: {exc}")
                    continue
                if urllib.parse.unquote(parsed.fragment) not in sub.ids:
                    errors.append(f"{path.relative_to(ROOT)}: missing anchor {parsed.fragment!r} in {target.relative_to(ROOT)}")
        elif parsed.fragment and urllib.parse.unquote(parsed.fragment) not in parser.ids:
            errors.append(f"{path.relative_to(ROOT)}: missing in-page anchor #{parsed.fragment}")


def check_catalog(errors: list[str], counts: dict):
    path = ROOT / "assets/catalog.min.json"
    if not path.exists():
        errors.append("missing assets/catalog.min.json; run tools/build_site_data.py")
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    for subject in data.get("subjects", []):
        for book in subject.get("books", []):
            file_path = urllib.parse.unquote(book.get("href") or "")
            target = (ROOT / file_path).resolve()
            if not target.is_file():
                errors.append(f"catalog book link missing: {book.get('href')}")
            else:
                counts["catalog_links"] += 1
    for profile in data.get("exam_profiles", []):
        for key in ("official_syllabus_url", "official_pattern_url"):
            url = profile.get(key)
            if url and not url.startswith(("https://", "http://")):
                errors.append(f"exam profile {profile.get('id')}: unsafe external link in {key}")
    manifest = ROOT / "assets/banks/cn/manifest.json"
    if not manifest.is_file():
        errors.append("missing CN bank manifest")
    else:
        for chunk in json.loads(manifest.read_text(encoding="utf-8")).get("topics", []):
            if not (ROOT / chunk["file"]).is_file():
                errors.append(f"missing topic chunk: {chunk['file']}")
            else:
                counts["topic_chunks"] += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="fail on every unresolved local link")
    args = parser.parse_args()
    errors = []
    counts = {"html_files": 0, "references": 0, "local_files": 0, "catalog_links": 0, "topic_chunks": 0}
    files = [ROOT / "index.html"]
    files.extend(sorted((ROOT / "Computer Network/Online Quiz").glob("**/*.html")))
    for path in files:
        check_html(path, errors, counts)
    check_catalog(errors, counts)
    if errors:
        print(f"FAIL: {len(errors)} link/access-safety issues")
        for error in errors[:100]:
            print(" -", error)
        if len(errors) > 100:
            print(f" - ... {len(errors)-100} additional issues")
        raise SystemExit(1)
    print("PASS: local links and new-tab rel attributes")
    print(json.dumps(counts, sort_keys=True))


if __name__ == "__main__":
    main()
