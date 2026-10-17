import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { brotliDecompressSync, gunzipSync } from "node:zlib";
const ROOT = fileURLToPath(new URL("../../", import.meta.url));
const PUBLIC = path.join(ROOT, "public");
const built = fs.existsSync(path.join(ROOT, ".vercel/output/config.json"));
const json = (rel) => JSON.parse(fs.readFileSync(path.join(ROOT, rel), "utf8"));

test("production export is an allowlist, not the entire repository", { skip: !built }, () => {
  assert.deepEqual([...new Set(fs.readdirSync(PUBLIC).map((file) => file.replace(/\.(br|gz)$/, "")))].sort(), [".nojekyll", "404.html", "assets", "content", "data", "index.html", "robots.txt", "sitemap.xml", "subjects"].sort());
  for (const rel of [".env", ".env.local", ".git", "server", "supabase", "tools", "tests", "maintainer", "README.md", "data/practice/papers", "data/banks/cn/cn_questions.json"]) {
    assert.equal(fs.existsSync(path.join(PUBLIC, rel)), false, `${rel} must not be exported`);
  }
});

test("Brotli/gzip artifacts round-trip and own JS is minified without changing module paths", { skip: !built }, () => {
  for (const rel of ["assets/js/account.mjs", "assets/js/room.mjs", "assets/css/ekguru.css", "data/practice/manifest.json"]) {
    const original = fs.readFileSync(path.join(PUBLIC, rel));
    assert.deepEqual(brotliDecompressSync(fs.readFileSync(path.join(PUBLIC, rel + ".br"))), original);
    assert.deepEqual(gunzipSync(fs.readFileSync(path.join(PUBLIC, rel + ".gz"))), original);
    assert.ok(fs.statSync(path.join(PUBLIC, rel + ".br")).size < original.length);
    if (rel.endsWith(".mjs")) assert.ok(original.length < fs.statSync(path.join(ROOT, rel)).size);
  }
});

test("Vercel function is separate from static output; API dispatch and immutable hash caching are emitted", { skip: !built }, () => {
  const output = json(".vercel/output/config.json");
  assert.equal(output.version, 3);
  assert.ok(output.routes.some((route) => route.dest === "/api?__path=$1"));
  const immutable = output.routes.find((route) => route.headers?.["Cache-Control"]?.includes("immutable"));
  assert.ok(new RegExp(immutable.src).test("/data/banks/cn/T01.d1e56839b7ef.min.json"));
  const general = output.routes.findIndex((route) => route.headers?.["Cache-Control"]?.includes("must-revalidate"));
  assert.ok(general < output.routes.indexOf(immutable), "specific cache rule must override the general rule, not vice versa");
  const config = json(".vercel/output/functions/api.func/.vc-config.json");
  assert.equal(config.runtime, "nodejs22.x"); assert.deepEqual(config.regions, ["bom1"]);
  assert.ok(fs.statSync(path.join(ROOT, ".vercel/output/functions/api.func/index.mjs")).size < 50000);
});

test("every discovered paper and its optional key are included, even scanned PDFs", { skip: !built }, () => {
  for (const paper of json("data/practice/manifest.json").papers) {
    assert.equal(fs.statSync(path.join(PUBLIC, paper.pdf)).size, paper.bytes);
    if (paper.key_pdf) assert.ok(fs.existsSync(path.join(PUBLIC, paper.key_pdf)));
  }
});
