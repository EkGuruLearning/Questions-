#!/usr/bin/env python3
"""Serve the published website locally — student-facing paths only.

`maintainer/`, `tools/`, `tests/` and the repository docs are **not** reachable:
any other path returns `404.html`, which is exactly what GitHub Pages shows for
an unknown page. Use it to preview the site before pushing:

    python3 tools/serve_site.py            # http://localhost:8000
    python3 tools/serve_site.py 9000       # custom port
"""
from __future__ import annotations

import http.server
import mimetypes
import pathlib
import posixpath
import socketserver
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUBLIC_FILES = ("index.html", "404.html", ".nojekyll")
PUBLIC_DIRS = ("subjects", "assets", "data", "content")

mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("application/javascript", ".mjs")
mimetypes.add_type("application/json", ".json")
mimetypes.add_type("image/webp", ".webp")


def resolve(request_path: str) -> pathlib.Path | None:
    """Return the file to serve, or None when the path is not public."""
    clean = urllib.parse.unquote(request_path.split("?", 1)[0].split("#", 1)[0])
    clean = posixpath.normpath(clean)
    if clean in ("/", ""):
        return ROOT / "index.html"
    relative = clean.lstrip("/")
    if relative in PUBLIC_FILES:
        return ROOT / relative
    first = relative.split("/", 1)[0]
    if first not in PUBLIC_DIRS:
        return None
    target = (ROOT / relative).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return None
    if target.is_dir():
        index = target / "index.html"
        return index if index.is_file() else None
    return target if target.is_file() else None


class Handler(http.server.BaseHTTPRequestHandler):
    server_version = "EkGuruPreview/1.0"

    def do_GET(self):  # noqa: N802 (stdlib naming)
        self.respond(body=True)

    def do_HEAD(self):  # noqa: N802
        self.respond(body=False)

    def respond(self, body: bool):
        target = resolve(self.path)
        if target is None:
            content = (ROOT / "404.html").read_bytes()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            if body:
                self.wfile.write(content)
            return
        content = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", mimetypes.guess_type(target.name)[0] or "application/octet-stream")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        if body:
            self.wfile.write(content)

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def main() -> int:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("0.0.0.0", port), Handler) as httpd:
        print(f"EkGuru preview: http://localhost:{port}/  (serving {ROOT})")
        print("Public paths: index.html, 404.html, subjects/, assets/, data/, content/ — everything else returns 404.")
        httpd.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
