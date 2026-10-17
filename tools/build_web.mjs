/* Production export: allowlisted public files, minified text, maximum precompression.
   Also emits Vercel Build Output API v3 with a tiny, dependency-free Node function.
   Generated artifacts are ignored; no credentials, canonical bank or maintainer docs. */
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { promisify } from "node:util";
import { brotliCompress, constants, gzip } from "node:zlib";
import { build, transform } from "esbuild";

const ROOT = fileURLToPath(new URL("../", import.meta.url));
const PUBLIC = path.join(ROOT, "public");
const OUTPUT = path.join(ROOT, ".vercel/output");
const br = promisify(brotliCompress), gz = promisify(gzip);
const readJSON = async (name) => JSON.parse(await fs.readFile(path.join(ROOT, name), "utf8"));
const routes = (await fs.readFile(path.join(ROOT, "data/catalog/site-routes.txt"), "utf8")).split(/\r?\n/).filter((line) => line && !line.startsWith("#"));
const files = new Set([...routes, "robots.txt", "sitemap.xml", ".nojekyll", "data/site.json", "data/runtime.json", "data/practice/manifest.json", "data/banks/cn/manifest.json"]);
const site = await readJSON("data/site.json");
const bank = await readJSON("data/banks/cn/manifest.json");
for (const topic of bank.topics) files.add(topic.file);
for (const subject of site.subjects) for (const record of subject.files) {
  files.add(record.repo_path);
  if (record.thumb_url) files.add(record.thumb_url);
}
async function assets(directory) {
  for (const item of await fs.readdir(path.join(ROOT, directory), { withFileTypes: true })) {
    const rel = `${directory}/${item.name}`;
    if (item.isDirectory()) await assets(rel);
    else if (item.isFile() && (!/\.(md|txt)$/i.test(item.name) || /LICENSE/i.test(item.name))) files.add(rel);
  }
}
await assets("assets");
// Include every discovered paper, even if the material catalogue has not been rebuilt yet.
for (const paper of (await readJSON("data/practice/manifest.json")).papers) {
  files.add(paper.pdf); if (paper.key_pdf) files.add(paper.key_pdf);
}
await fs.rm(PUBLIC, { recursive: true, force: true });
await fs.mkdir(PUBLIC, { recursive: true });
let originalText = 0, minifiedText = 0, brotliText = 0, gzipText = 0, totalBytes = 0;
for (const rel of [...files].sort()) {
  if (rel.includes("..") || path.isAbsolute(rel) || /^(?:server|supabase|tools|tests|maintainer|\.env|\.git)(?:\/|$)/.test(rel)) throw new Error(`Unsafe public export: ${rel}`);
  const source = path.join(ROOT, rel), dest = path.join(PUBLIC, rel);
  await fs.mkdir(path.dirname(dest), { recursive: true });
  const ext = path.extname(rel);
  const text = [".html", ".css", ".mjs", ".js", ".json", ".xml", ".svg", ".txt"].includes(ext);
  if (!text) { await fs.copyFile(source, dest); totalBytes += (await fs.stat(source)).size; continue; }
  let code = await fs.readFile(source, "utf8"); originalText += Buffer.byteLength(code);
  if (ext === ".json") code = JSON.stringify(JSON.parse(code));
  if ([".js", ".mjs", ".css"].includes(ext) && !rel.startsWith("assets/vendor/")) {
    code = (await transform(code, { loader: ext === ".css" ? "css" : "js", minify: true, target: "es2022", legalComments: "eof" })).code;
  }
  if (ext === ".html") code = code.replace(/<!--[\s\S]*?-->/g, "").replace(/>\s+</g, "><").trim();
  const bytes = Buffer.from(code); minifiedText += bytes.length; totalBytes += bytes.length;
  await fs.writeFile(dest, bytes);
  if (bytes.length >= 1024) {
    const [compressed, zipped] = await Promise.all([
      br(bytes, { params: { [constants.BROTLI_PARAM_QUALITY]: 11, [constants.BROTLI_PARAM_MODE]: constants.BROTLI_MODE_TEXT } }),
      gz(bytes, { level: 9 }),
    ]);
    if (compressed.length < bytes.length) await fs.writeFile(dest + ".br", compressed);
    if (zipped.length < bytes.length) await fs.writeFile(dest + ".gz", zipped);
    brotliText += Math.min(compressed.length, bytes.length); gzipText += Math.min(zipped.length, bytes.length);
  } else { brotliText += bytes.length; gzipText += bytes.length; }
}
// Keep the ordinary public/ export usable on any static host. Vercel's CDN also
// negotiates compression automatically; .br/.gz are for compatible own servers.
await fs.rm(OUTPUT, { recursive: true, force: true });
await fs.mkdir(OUTPUT, { recursive: true });
await fs.cp(PUBLIC, path.join(OUTPUT, "static"), { recursive: true });
const functionDir = path.join(OUTPUT, "functions/api.func");
await fs.mkdir(functionDir, { recursive: true });
await build({ entryPoints: [path.join(ROOT, "server/handler.mjs")], outfile: path.join(functionDir, "index.mjs"), bundle: true,
  platform: "node", format: "esm", target: "node22", minify: true, legalComments: "eof" });
await fs.writeFile(path.join(functionDir, ".vc-config.json"), JSON.stringify({ runtime: "nodejs22.x", handler: "index.mjs", launcherType: "Nodejs", regions: ["bom1"], maxDuration: 30 }));
const security = {
  "X-Content-Type-Options": "nosniff",
  "Referrer-Policy": "strict-origin-when-cross-origin",
  "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
  "Strict-Transport-Security": "max-age=31536000",
  "Content-Security-Policy": "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; font-src 'self' data:; connect-src 'self'; worker-src 'self' blob:; base-uri 'self'; form-action 'self'; frame-ancestors 'none'",
};
await fs.writeFile(path.join(OUTPUT, "config.json"), JSON.stringify({ version: 3, routes: [
  { src: "/(.*)", headers: security, continue: true },
  { src: "/api/(.*)", dest: "/api?__path=$1" },
  { src: "/(.*)", headers: { "Cache-Control": "public, max-age=0, must-revalidate" }, continue: true },
  { src: "/data/banks/cn/(.*)\\.[a-f0-9]{12}\\.min\\.json", headers: { "Cache-Control": "public, max-age=31536000, immutable" }, continue: true },
  { src: "/", dest: "/index.html" },
  { src: "/subjects", status: 308, headers: { Location: "/subjects/" } },
  { src: "/subjects/(.*)/", dest: "/subjects/$1/index.html" },
  { handle: "filesystem" },
  { src: "/.*", dest: "/404.html", status: 404 },
] }, null, 2));
const stats = { files: files.size, public_bytes: totalBytes, text_original_bytes: originalText, text_minified_bytes: minifiedText,
  text_brotli_bytes: brotliText, text_gzip_bytes: gzipText, brotli_text_reduction_percent: Math.round((1 - brotliText / originalText) * 100) };
await fs.writeFile(path.join(OUTPUT, "build-stats.json"), JSON.stringify(stats, null, 2));
console.log(JSON.stringify(stats, null, 2));
console.log("Built public/ + .vercel/output/. Generated files and secrets are not committed.");
