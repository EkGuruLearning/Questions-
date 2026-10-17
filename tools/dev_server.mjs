/* Single-origin preview: public allowlist + the same auth handler as production.
   Binds 0.0.0.0, supports the GitHub Pages /Questions-/ prefix and PDF byte ranges.
   WEB_ROOT=public uses minified/precompressed production assets for verification. */
import fs from "node:fs/promises";
import { createReadStream } from "node:fs";
import http from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createHandler } from "../server/handler.mjs";

const REPO = fileURLToPath(new URL("../", import.meta.url));
const ROOT = path.resolve(REPO, process.env.WEB_ROOT || ".");
const PORT = Number(process.env.PORT || 8000);
const handler = createHandler({ env: process.env.EKGURU_DISABLE_AUTH === "true" ? {} : process.env });
const publicDirs = new Set(["subjects", "assets", "data", "content"]);
const publicFiles = new Set(["index.html", "404.html", ".nojekyll", "robots.txt", "sitemap.xml"]);
const mime = { ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8", ".js": "application/javascript; charset=utf-8", ".mjs": "application/javascript; charset=utf-8", ".json": "application/json; charset=utf-8", ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp", ".avif": "image/avif", ".pdf": "application/pdf", ".xml": "application/xml", ".txt": "text/plain; charset=utf-8" };
const allowed = (rel) => publicFiles.has(rel) || publicDirs.has(rel.split("/")[0]);

async function resolve(raw) {
  try {
    let clean = decodeURIComponent(new URL(raw, "http://preview.invalid").pathname);
    if (/[\\\u0000-\u001f]/.test(clean)) return null;
    if (clean === "/Questions-" || clean.startsWith("/Questions-/")) clean = clean.slice("/Questions-".length);
    let rel = clean.replace(/^\/+/, "") || "index.html";
    if (rel.split("/").some((segment) => segment === ".." || (segment.startsWith(".") && segment !== ".nojekyll")) || !allowed(rel)) return null;
    let target = path.resolve(ROOT, rel);
    if (!(target === ROOT || target.startsWith(ROOT + path.sep))) return null;
    if ((await fs.stat(target)).isDirectory()) target = path.join(target, "index.html");
    const real = await fs.realpath(target);
    rel = path.relative(ROOT, real).split(path.sep).join("/");
    if (!allowed(rel) || !(await fs.stat(real)).isFile() || /\.(?:md|paper\.json)$/i.test(real)) return null;
    return real;
  } catch { return null; }
}

function compression(header = "") {
  const values = new Map(String(header).split(",").map((part) => {
    const [type, ...params] = part.trim().split(";");
    const quality = params.find((p) => p.trim().startsWith("q="));
    const q = quality ? Number(quality.trim().slice(2)) : 1;
    return [type, Number.isFinite(q) && q >= 0 && q <= 1 ? q : 0];
  }));
  const quality = (type) => values.get(type) ?? values.get("*") ?? 0;
  return ["br", "gzip"].filter((type) => quality(type) > 0).sort((a, b) => quality(b) - quality(a));
}

const server = http.createServer(async (req, res) => {
  try {
    const url = new URL(req.url, "http://preview.invalid");
    if (url.pathname.startsWith("/api/")) return await handler(req, res);
    if (!["GET", "HEAD"].includes(req.method)) { res.writeHead(405, { Allow: "GET, HEAD" }); return res.end(); }
    // Relative marker rather than a hardcoded localhost URL, so the Arena preview works.
    if (["/data/runtime.json", "/Questions-/data/runtime.json"].includes(url.pathname)) {
      const body = JSON.stringify({ schema_version: 1, auth_origin: "same-origin" });
      res.writeHead(200, { "Content-Type": mime[".json"], "Cache-Control": "no-store", "Content-Length": Buffer.byteLength(body) });
      return res.end(req.method === "HEAD" ? undefined : body);
    }
    let target = await resolve(req.url), status = 200;
    if (!target) { target = path.join(ROOT, "404.html"); status = 404; }
    const original = target;
    let stat = await fs.stat(target);
    const headers = { "Content-Type": mime[path.extname(original)] || "application/octet-stream", "Cache-Control": "no-cache", "X-Content-Type-Options": "nosniff", "Referrer-Policy": "strict-origin-when-cross-origin", "Accept-Ranges": "bytes", "Vary": "Accept-Encoding" };
    // Do not block iframe embedding: Arena displays this server in a preview iframe.
    if (!req.headers.range) {
      for (const encoding of compression(req.headers["accept-encoding"])) {
        const candidate = original + (encoding === "br" ? ".br" : ".gz");
        try { stat = await fs.stat(candidate); target = candidate; headers["Content-Encoding"] = encoding; break; } catch { /* raw fallback */ }
      }
    }
    let start = 0, end = stat.size - 1;
    if (req.headers.range && status === 200) {
      const match = /^bytes=(\d*)-(\d*)$/.exec(req.headers.range);
      if (!match || !(match[1] || match[2])) { res.writeHead(416, { "Content-Range": `bytes */${stat.size}` }); return res.end(); }
      start = match[1] ? Number(match[1]) : Math.max(0, stat.size - Number(match[2]));
      end = match[1] && match[2] ? Math.min(stat.size - 1, Number(match[2])) : stat.size - 1;
      if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end) || start > end || start >= stat.size) {
        res.writeHead(416, { "Content-Range": `bytes */${stat.size}` }); return res.end();
      }
      status = 206; headers["Content-Range"] = `bytes ${start}-${end}/${stat.size}`;
    }
    headers["Content-Length"] = Math.max(0, end - start + 1);
    res.writeHead(status, headers);
    if (req.method === "HEAD" || stat.size === 0) return res.end();
    const stream = createReadStream(target, { start, end });
    stream.on("error", () => res.destroy()); res.on("close", () => stream.destroy()); stream.pipe(res);
  } catch {
    if (!res.headersSent) res.writeHead(500, { "Content-Type": "text/plain" });
    res.end("Preview request failed");
  }
});
server.listen(PORT, "0.0.0.0", () => console.log(`EkGuru website + API listening on 0.0.0.0:${PORT} (${ROOT === path.resolve(REPO) ? "source" : "production export"}).`));
