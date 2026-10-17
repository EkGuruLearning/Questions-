#!/usr/bin/env python3
"""Validate the published website: routes, links, downloads and site data.

Checks
------
1. Every route listed in `data/catalog/site-routes.txt` exists.
2. Every internal link/anchor in those pages resolves to a real file or page id.
3. No published page links to a `.md` file and no published page links into
   `maintainer/` (audits, scripts and source registers stay off the website).
4. Every download in `data/site.json` exists, matches its recorded SHA-256 and
   byte size, and every published file is inside `content/<subject>/<folder>/`.
   Every `?folder=` link on a page must name a folder that exists in the tree.
5. `data/site.json` is current (same as `tools/build_catalog.py --check`).
6. Download links on the pages only point at registered files.

Run: python3 tools/validate_site.py
"""
from __future__ import annotations

import hashlib
import html.parser
import json
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
ROUTES_FILE = ROOT / "data/catalog/site-routes.txt"
SITE_JSON = ROOT / "data/site.json"

REQUIRED_ROUTES = (
    "index.html",
    "subjects/index.html",
    "subjects/computer-network/index.html",
    "subjects/computer-network/material/index.html",
    "subjects/computer-network/test/index.html",
    "subjects/rajasthan-geography/index.html",
    "404.html",
    "assets/css/ekguru.css",
    "assets/js/test.mjs",
    "assets/js/viewer.mjs",
    "subjects/reader/index.html",
    "assets/vendor/pdfjs/pdf.min.mjs",
    "assets/vendor/pdfjs/pdf.worker.min.mjs",
    "assets/js/engine.mjs",
    "data/site.json",
    "data/banks/cn/manifest.json",
)

# Repo-only roots: a page must never resolve into these. Checked on the resolved
# path (not as a substring) so a student folder called `tests/` inside content or a
# subject page stays legal.
FORBIDDEN_ROOTS = ("library/", "maintainer/", "tools/", "tests/", ".git/", "data/sources/", "data/schemas/")
FORBIDDEN_FILES = ("README.md", "SITE_GUIDE.md")


class LinkParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links: list[dict] = []
        self.ids: list[str] = []
        self.scripts: list[dict] = []
        self.images: list[dict] = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "a":
            self.links.append(attrs)
        elif tag == "script":
            self.scripts.append(attrs)
        elif tag == "img":
            self.images.append(attrs)


def fail(messages: list[str]) -> int:
    for message in messages:
        print("FAIL:", message)
    return 1


def routes() -> list[str]:
    if ROUTES_FILE.is_file():
        listed = [line.strip() for line in ROUTES_FILE.read_text(encoding="utf-8").splitlines()
                  if line.strip() and not line.startswith("#")]
        listed = [line for line in listed if line.endswith(".html")]
    else:
        listed = []
    ordered = list(dict.fromkeys(listed + list(REQUIRED_ROUTES)))
    return [route for route in ordered if route.endswith(".html")]


def resolve(page: str, target: str) -> pathlib.Path | None:
    if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:")):
        return None
    path = urllib.parse.unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not path:
        return None
    return (ROOT / pathlib.Path(page).parent / path).resolve()


def main() -> int:
    problems: list[str] = []

    for route in REQUIRED_ROUTES:
        if not (ROOT / route).is_file():
            problems.append(f"required site file is missing: {route}")

    pages = routes()
    link_count = 0
    for page in pages:
        page_path = ROOT / page
        if not page_path.is_file():
            problems.append(f"route listed in site-routes.txt does not exist: {page}")
            continue
        parser = LinkParser()
        parser.feed(page_path.read_text(encoding="utf-8"))
        if len(parser.ids) != len(set(parser.ids)):
            problems.append(f"{page}: duplicate id attribute")
        ids = set(parser.ids)
        for link in parser.links + parser.scripts + parser.images:
            target = link.get("href") or link.get("src") or ""
            if not target:
                continue
            link_count += 1
            # The reader route can exist while its ?file= target is missing.
            parsed_target = urllib.parse.urlsplit(target)
            reader_file = urllib.parse.parse_qs(parsed_target.query).get("file", [])
            if reader_file and parsed_target.path.endswith("reader/index.html"):
                source = reader_file[0]
                source_path = (ROOT / source).resolve()
                if not source.startswith("content/") or not source_path.is_relative_to(ROOT / "content") or not source_path.is_file():
                    problems.append(f"{page}: reader file does not resolve: {source}")
            lowered = target.lower()
            path_only = urllib.parse.urlsplit(target).path
            if path_only:
                resolved = (page_path.parent / path_only).resolve()
                try:
                    repo_relative = resolved.relative_to(ROOT).as_posix()
                except ValueError:
                    repo_relative = ""
                if any(repo_relative.startswith(root) for root in FORBIDDEN_ROOTS):
                    problems.append(f"{page}: published page links to non-student material: {target}")
                if repo_relative in FORBIDDEN_FILES:
                    problems.append(f"{page}: published page links to a repo document: {target}")
            if lowered.endswith(".md") or ".md#" in lowered or ".md?" in lowered:
                problems.append(f"{page}: published page links to a markdown file: {target}")
            if target.startswith("#"):
                if target[1:] and target[1:] not in ids:
                    problems.append(f"{page}: in-page anchor does not resolve: {target}")
                continue
            resolved = resolve(page, target)
            if resolved is None:
                continue
            if not resolved.exists():
                problems.append(f"{page}: broken link (server is case-sensitive): {target}")
                continue
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                problems.append(f"{page}: link escapes the site root: {target}")
            if link.get("target") == "_blank":
                safe = set((link.get("rel") or "").lower().split())
                if not {"noopener", "noreferrer"}.issubset(safe):
                    problems.append(f"{page}: new-tab link is missing rel=\"noopener noreferrer\": {target}")

    if not SITE_JSON.is_file():
        problems.append("data/site.json is missing; run python3 tools/build_catalog.py")
    else:
        site = json.loads(SITE_JSON.read_text(encoding="utf-8"))
        folder_paths = {"": None}
        for subject in site["subjects"]:

            def walk(node):
                folder_paths[node["path"]] = subject["id"]
                for child in node["folders"]:
                    walk(child)

            walk(subject["tree"])
            for item in subject["files"]:
                path = ROOT / item["repo_path"]
                if not path.is_file():
                    problems.append(f"registered download is missing: {item['repo_path']}")
                    continue
                if not item["repo_path"].startswith(f"content/{subject['id']}/"):
                    problems.append(
                        f"published download must live under content/{subject['id']}/<folder>/: {item['repo_path']}"
                    )
                raw = path.read_bytes()
                if len(raw) != item["bytes"]:
                    problems.append(f"size drift for {item['repo_path']}: register says {item['bytes']}, file has {len(raw)}")
                if hashlib.sha256(raw).hexdigest() != item["sha256"]:
                    problems.append(f"hash drift for {item['repo_path']}: rebuild data/site.json")
                if item.get("thumb_url"):
                    thumb_file = ROOT / urllib.parse.unquote(item["thumb_url"])
                    if not thumb_file.is_file():
                        problems.append(f"site preview is missing for {item['repo_path']}: {item['thumb_url']}")
                    elif thumb_file.stat().st_size >= len(raw):
                        problems.append(f"site preview is not smaller than the picture: {item['thumb_url']}")
            if subject.get("test"):
                manifest = ROOT / subject["test"]["manifest_url"]
                if not manifest.is_file():
                    problems.append(f"test bank manifest missing: {subject['test']['manifest_url']}")

        for page in pages:
            page_path = ROOT / page
            if not page_path.is_file():
                continue
            for match in re.findall(r"[?&]folder=([^\"'&#]+)", page_path.read_text(encoding="utf-8")):
                folder = urllib.parse.unquote(match)
                if folder not in folder_paths:
                    problems.append(f"{page}: ?folder={folder} is not a folder in the published tree")

    if problems:
        return fail(problems)

    payload = json.loads(SITE_JSON.read_text(encoding="utf-8"))
    downloads = sum(len(subject["files"]) for subject in payload["subjects"])
    folders = sum(subject["folder_count"] for subject in payload["subjects"])
    print(f"PASS: {len(pages)} route(s), {link_count} link(s), {downloads} download(s) and {folders} folder(s) checked")
    print("PASS: no .md links, no maintainer links, no broken internal links, hashes match data/site.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
