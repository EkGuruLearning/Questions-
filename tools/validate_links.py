#!/usr/bin/env python3
"""Validate website-local links and manifests under the GitHub Pages project base.

This is a structural check: local URLs are resolved exactly as they would be under
/Questions-/. External hosts are not fetched (many official domains are outside
the sandbox allowlist); their URL, target and rel policy are validated locally.
"""
from __future__ import annotations

import argparse
import html.parser
import json
import pathlib
import sys
import urllib.parse
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE_PATH = "/Questions-/"
PUBLISHED_ROOTS = ("subjects/", "maps/", "practice/", "study-material/", "sources/", "guides/", "Computer Network/Online Quiz/")
EXCLUDED_PREFIXES = ("archive/", "Computer Network/new/")


class HTMLLinks(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links: list[dict[str, str | int]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        line, _ = self.getpos()
        for attr in ("href", "src", "poster", "action"):
            if values.get(attr) is not None:
                self.links.append({
                    "tag": tag,
                    "attr": attr,
                    "value": values[attr],
                    "target": values.get("target", ""),
                    "rel": values.get("rel", ""),
                    "line": line,
                })
        if values.get("srcset"):
            for candidate in values["srcset"].split(","):
                url = candidate.strip().split()[0] if candidate.strip() else ""
                self.links.append({"tag": tag, "attr": "srcset", "value": url, "target": "", "rel": "", "line": line})


def published_html() -> list[pathlib.Path]:
    candidates = [ROOT / "index.html", ROOT / "404.html"]
    for prefix in PUBLISHED_ROOTS:
        directory = ROOT / prefix
        if directory.exists():
            candidates.extend(directory.rglob("*.html"))
    return sorted({path for path in candidates if path.is_file() and not any(path.relative_to(ROOT).as_posix().startswith(prefix) for prefix in EXCLUDED_PREFIXES)})


def load_parser(path: pathlib.Path, errors: list[str]) -> HTMLLinks | None:
    parser = HTMLLinks()
    try:
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: cannot parse HTML: {exc}")
        return None
    return parser


def resolve_local(source: str, raw: str) -> tuple[pathlib.Path | None, urllib.parse.SplitResult, str | None]:
    page_url = BASE_PATH + urllib.parse.quote(source, safe="/")
    source_url = urllib.parse.urljoin("https://pages.local", page_url)
    resolved = urllib.parse.urlsplit(urllib.parse.urljoin(source_url, raw))
    if resolved.scheme not in ("http", "https") or resolved.netloc != "pages.local":
        return None, resolved, None
    if not resolved.path.startswith(BASE_PATH):
        return None, resolved, f"local URL escaped GitHub Pages base {BASE_PATH}: {raw} -> {resolved.path}"
    relative = urllib.parse.unquote(resolved.path[len(BASE_PATH):])
    if not relative:
        relative = "index.html"
    target = (ROOT / pathlib.PurePosixPath(relative)).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return None, resolved, f"local URL escapes repository: {raw}"
    if target.is_dir():
        target = target / "index.html"
    return target, resolved, None


def validate_html(errors: list[str], counts: Counter) -> dict[str, set[str]]:
    page_ids: dict[str, set[str]] = {}
    for path in published_html():
        relative = path.relative_to(ROOT).as_posix()
        parsed = load_parser(path, errors)
        if parsed is None:
            continue
        page_ids[relative] = parsed.ids
        counts["html_pages"] += 1
        for link in parsed.links:
            raw = str(link["value"] or "").strip()
            attr = str(link["attr"])
            line = int(link["line"])
            prefix = f"{relative}:{line}"
            counts["html_references"] += 1
            if not raw or raw == "#":
                errors.append(f"{prefix}: dead/empty {attr}={raw!r}")
                continue
            if raw.lower().startswith("javascript:"):
                errors.append(f"{prefix}: javascript: URL is not allowed")
                continue
            parsed_url = urllib.parse.urlsplit(raw)
            target = str(link["target"] or "").strip().lower()
            rel = {token.lower() for token in str(link["rel"] or "").split()}
            external = bool(parsed_url.scheme or parsed_url.netloc)
            if target == "_blank" and not {"noopener", "noreferrer"}.issubset(rel):
                errors.append(f"{prefix}: target=_blank must include rel=noopener noreferrer: {raw}")
            if target == "_blank" and not external and urllib.parse.unquote(parsed_url.path).lower().endswith(".pdf"):
                counts["pdf_new_tab_links"] += 1
            if external:
                if parsed_url.scheme.lower() not in ("http", "https", "mailto", "tel", "data"):
                    errors.append(f"{prefix}: unsupported external scheme in {raw}")
                elif parsed_url.scheme.lower() in ("http", "https"):
                    counts["external_links"] += 1
                continue
            if parsed_url.scheme.lower() in ("mailto", "tel", "data"):
                continue
            target_path, resolved, problem = resolve_local(relative, raw)
            if problem:
                errors.append(f"{prefix}: {problem}")
                continue
            if target_path is None or not target_path.is_file():
                errors.append(f"{prefix}: missing project-base target: {raw}")
                continue
            counts["local_links"] += 1
            decoded_suffix = target_path.suffix.lower()
            if decoded_suffix == ".pdf" and target != "_blank":
                errors.append(f"{prefix}: PDF link must explicitly open in a new tab: {raw}")
            if resolved.fragment and decoded_suffix in (".html", ".htm"):
                target_rel = target_path.relative_to(ROOT).as_posix()
                if target_rel == relative:
                    ids = parsed.ids
                else:
                    target_parser = load_parser(target_path, errors)
                    ids = target_parser.ids if target_parser else set()
                fragment = urllib.parse.unquote(resolved.fragment)
                if fragment and fragment not in ids:
                    errors.append(f"{prefix}: missing HTML anchor #{fragment} in {target_rel}")
    return page_ids


def validate_manifests(errors: list[str], counts: Counter) -> None:
    for name in ("subjects.json", "resources.json", "maps.json"):
        path = ROOT / "assets/catalog" / name
        if not path.is_file():
            errors.append(f"Missing catalogue manifest assets/catalog/{name}")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid JSON in assets/catalog/{name}: {exc}")
            continue
        counts["catalog_manifests"] += 1
        if name == "subjects.json":
            for subject in data.get("subjects", []):
                if subject.get("status") == "live":
                    route = subject.get("route", "")
                    target = (ROOT / urllib.parse.unquote(route)).resolve()
                    if not target.is_file():
                        errors.append(f"Live subject {subject.get('id')} has missing route {route}")
        elif name == "resources.json":
            seen = set()
            for item in data.get("resources", []):
                resource_id = item.get("id")
                if not resource_id or resource_id in seen:
                    errors.append(f"Resource ID missing or duplicated: {resource_id!r}")
                seen.add(resource_id)
                raw_path = item.get("repo_path")
                if not raw_path:
                    errors.append(f"Resource {resource_id}: repo_path is required")
                    continue
                target = (ROOT / pathlib.PurePosixPath(raw_path)).resolve()
                try:
                    target.relative_to(ROOT.resolve())
                except ValueError:
                    errors.append(f"Resource {resource_id}: repository path escapes root: {raw_path}")
                    continue
                if not target.is_file():
                    errors.append(f"Resource {resource_id}: missing repository path: {raw_path}")
                    continue
                url = item.get("url", "")
                if not url or url.startswith("/"):
                    errors.append(f"Resource {resource_id}: URL must be project-relative (no leading slash): {url!r}")
                    continue
                counts["manifest_resource_paths"] += 1
                if item.get("open_behavior") not in ("same_tab", "new_tab"):
                    errors.append(f"Resource {resource_id}: invalid open_behavior {item.get('open_behavior')!r}")
                if target.suffix.lower() == ".pdf" and item.get("open_behavior") != "new_tab":
                    errors.append(f"PDF resource {resource_id} must open in a new tab")
                if item.get("open_behavior") == "new_tab" and "new tab" not in str(item.get("external_open_label", "")).lower():
                    errors.append(f"New-tab resource {resource_id} must have an explicit visible open label")
                if item.get("availability_status") not in ("available", "retired_redirect", "needs_verification", "unavailable"):
                    errors.append(f"Resource {resource_id}: invalid availability_status {item.get('availability_status')!r}")
                if item.get("category") == "Map/Atlas" and target.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp") and not item.get("image_alt"):
                    errors.append(f"Map resource {resource_id} lacks image_alt")
                if item.get("open_behavior") == "new_tab":
                    counts["manifest_new_tab_resources"] += 1
        elif name == "maps.json":
            for item in data.get("maps", []):
                for path_key in ("preview_image_path", "original_repo_path", "full_size_repo_path"):
                    rel = item.get(path_key)
                    if not rel:
                        continue
                    target = (ROOT / pathlib.PurePosixPath(rel)).resolve()
                    if not target.is_file():
                        errors.append(f"Map {item.get('id')}: missing {path_key} {rel}")
                    else:
                        counts["map_asset_paths"] += 1
                for url_key in ("preview_image_url", "original_url", "full_size_url"):
                    value = item.get(url_key)
                    if value and value.startswith("/"):
                        errors.append(f"Map {item.get('id')}: project URL must not start with /: {url_key}={value}")
                if item.get("display_in_gallery") and not item.get("image_alt"):
                    errors.append(f"Map {item.get('id')}: gallery image is missing descriptive alt text")
                behavior = item.get("image_open_behavior")
                if item.get("full_size_url") and behavior not in ("new_tab", "same_tab"):
                    errors.append(f"Map {item.get('id')}: full-size open behavior is not declared")
                if behavior == "new_tab" and "new tab" not in str(item.get("external_open_label", "")).lower():
                    errors.append(f"Map {item.get('id')}: a new-tab full-size image action must be visibly labelled")
            for source in data.get("official_sources", []):
                url = source.get("url", "")
                if not url.startswith("https://"):
                    errors.append(f"Official source URL must use HTTPS: {url}")
                if source.get("open_behavior") != "new_tab" or "new tab" not in str(source.get("external_open_label", "")).lower():
                    errors.append(f"Official source link must be safely configured and labelled as opening in a new tab: {url}")
                counts["recorded_external_sources"] += 1


def main() -> None:
    global BASE_PATH
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-path", default=BASE_PATH, help="GitHub Pages project base, default /Questions-/")
    args = parser.parse_args()
    BASE_PATH = args.base_path if args.base_path.endswith("/") else args.base_path + "/"
    errors: list[str] = []
    counts: Counter = Counter()
    validate_html(errors, counts)
    validate_manifests(errors, counts)
    print("GitHub Pages local-link validation base:", BASE_PATH)
    print(json.dumps(dict(sorted(counts.items())), sort_keys=True))
    if errors:
        print(f"FAIL: {len(errors)} broken-link or project-base issue(s)")
        for error in errors[:150]:
            print(" -", error)
        if len(errors) > 150:
            print(f" - ... {len(errors)-150} further issue(s)")
        raise SystemExit(1)
    print("PASS: HTML, catalog, project-base URLs and new-tab safety are valid.")


if __name__ == "__main__":
    main()
