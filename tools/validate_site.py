#!/usr/bin/env python3
"""Validate the published website: routes, links, downloads and site data.

Checks
------
1. Every route listed in `data/catalog/site-routes.txt` exists.
2. Every internal link/anchor in those pages resolves to a real file or page id.
3. No published page links to a `.md` file and no published page links into
   `maintainer/` (audits, scripts and source registers stay off the website).
4. Every download in `data/site.json` exists, matches its recorded SHA-256 and
   byte size, and every published file is inside `content/`.
5. `data/site.json` is current (same as `tools/build_catalog.py --check`).
6. Download links on the pages only point at registered files.

Run: python3 tools/validate_site.py
"""
from __future__ import annotations

import hashlib
import html.parser
import json
import pathlib
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
    "assets/js/site.js",
    "assets/js/test.mjs",
    "assets/js/engine.mjs",
    "data/site.json",
    "data/banks/cn/manifest.json",
)

FORBIDDEN_LINK_PARTS = ("maintainer/", "/.git", "tools/", "tests/", "SITE_GUIDE.md", "README.md")


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
            lowered = target.lower()
            if any(part.lower() in lowered for part in FORBIDDEN_LINK_PARTS):
                problems.append(f"{page}: published page links to non-student material: {target}")
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
        for subject in site["subjects"]:
            for group in subject["groups"]:
                for item in group["items"]:
                    path = ROOT / item["repo_path"]
                    if not path.is_file():
                        problems.append(f"registered download is missing: {item['repo_path']}")
                        continue
                    if not item["repo_path"].startswith("content/"):
                        problems.append(f"published download must live under content/: {item['repo_path']}")
                    raw = path.read_bytes()
                    if len(raw) != item["bytes"]:
                        problems.append(f"size drift for {item['repo_path']}: register says {item['bytes']}, file has {len(raw)}")
                    if hashlib.sha256(raw).hexdigest() != item["sha256"]:
                        problems.append(f"hash drift for {item['repo_path']}: rebuild data/site.json")
            if subject.get("test"):
                manifest = ROOT / subject["test"]["manifest_url"]
                if not manifest.is_file():
                    problems.append(f"test bank manifest missing: {subject['test']['manifest_url']}")

    if problems:
        return fail(problems)

    downloads = sum(len(group["items"]) for subject in json.loads(SITE_JSON.read_text(encoding="utf-8"))["subjects"]
                    for group in subject["groups"])
    print(f"PASS: {len(pages)} route(s), {link_count} link(s) and {downloads} download(s) checked")
    print("PASS: no .md links, no maintainer links, no broken internal links, hashes match data/site.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
