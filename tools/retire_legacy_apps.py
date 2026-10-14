#!/usr/bin/env python3
"""Retire stale public CBT snapshots while preserving exact copies as inert files."""
from __future__ import annotations
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIVE_DIR = ROOT / "Computer Network/Online Quiz"
ARCHIVE_DIR = ROOT / "archive/pre-audit-2026-10-14/Computer Network/Online Quiz"
REDIRECT_MARKER = b"legacy CBT snapshot has been retired"


def preserve_original(page: pathlib.Path) -> pathlib.Path:
    archive_html = ARCHIVE_DIR / page.name
    snapshot = ARCHIVE_DIR / f"{page.name}.snapshot"
    if archive_html.exists():
        archived = archive_html.read_bytes()
        if REDIRECT_MARKER in archived:
            if not snapshot.exists():
                raise SystemExit(f"Archived redirect exists but original snapshot is missing: {snapshot}")
            archive_html.unlink()
        elif snapshot.exists():
            if snapshot.read_bytes() != archived:
                raise SystemExit(f"Refusing to overwrite a different preserved original: {snapshot}")
            archive_html.unlink()
        else:
            archive_html.rename(snapshot)
    if not snapshot.exists():
        live_bytes = page.read_bytes()
        if REDIRECT_MARKER in live_bytes:
            raise SystemExit(f"Cannot reconstruct missing original snapshot from retired path: {page}")
        shutil.copy2(page, snapshot)
    if REDIRECT_MARKER not in page.read_bytes() and page.read_bytes() != snapshot.read_bytes():
        raise SystemExit(f"Live legacy source differs from its preserved archive: {page}")
    return snapshot


def redirect_document(number: int, topic_id: str) -> str:
    fallback = f"../../practice/index.html?subject=cn&amp;topic={topic_id}&amp;mode=practice#practice"
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <meta http-equiv="refresh" content="2;url={fallback}">
  <meta name="theme-color" content="#16283f">
  <title>Legacy quiz retired — EkGuru Learning</title>
  <style>
    :root {{ font-family: system-ui, sans-serif; color: #172433; background: #f3f6fa; }}
    * {{ box-sizing: border-box; }}
    body {{ display: grid; min-height: 100vh; place-items: center; margin: 0; padding: 1rem; }}
    main {{ width: min(100%, 38rem); padding: clamp(1.25rem, 5vw, 2.5rem); border: 1px solid #d7e0e9; border-radius: 1rem; background: #fff; }}
    h1 {{ color: #16283f; }}
    p {{ line-height: 1.65; }}
    a {{ display: inline-flex; min-height: 44px; align-items: center; padding: .65rem 1rem; border-radius: .5rem; background: #16283f; color: #fff; font-weight: 750; text-decoration: none; }}
    .notice {{ padding: .85rem 1rem; border-left: 4px solid #e97313; background: #fff7ed; }}
  </style>
</head>
<body>
  <main>
    <h1>This legacy CBT snapshot has been retired</h1>
    <p class="notice">The old page used a historical embedded bank and verification labels. Its original file is preserved as a non-runnable audit snapshot; use the shared portal for current source-labelled practice.</p>
    <p>Opening Computer Networks {topic_id}…</p>
    <a id="portalLink" href="{fallback}">Open current Topic {number} practice</a>
  </main>
  <script>
    (function () {{
      var target = new URL("../../practice/index.html", window.location.href);
      target.searchParams.set("subject", "cn");
      target.searchParams.set("topic", "{topic_id}");
      target.searchParams.set("mode", "practice");
      target.hash = "practice";
      document.getElementById("portalLink").href = target.href;
      window.location.replace(target.href);
    }}());
  </script>
</body>
</html>
'''


def main():
    pages = sorted(LIVE_DIR.glob("Topic * - Online Quiz & Exam (by PRAKASH - EkGuru).html"))
    if len(pages) != 7:
        raise SystemExit(f"Expected 7 legacy topic pages, found {len(pages)}")
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    for page in pages:
        match = re.search(r"Topic (\d+)", page.name)
        if not match:
            raise SystemExit(f"Could not resolve topic from file name: {page}")
        snapshot = preserve_original(page)
        number = int(match.group(1))
        page.write_text(redirect_document(number, f"T{number:02d}"), encoding="utf-8")
        if not snapshot.is_file():
            raise SystemExit(f"Original snapshot missing after redirect: {snapshot}")
    print(f"PASS: {len(pages)} legacy paths redirect; exact originals remain as non-runnable .html.snapshot files.")


if __name__ == "__main__":
    main()
