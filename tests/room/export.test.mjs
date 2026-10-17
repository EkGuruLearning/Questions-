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
  for (const rel of [".env", ".env.local", ".git", "server", "supabase", "tools", "tests", "maintainer", "README.md", "data/practice/papers", "data/tests", "data/banks/cn/cn_questions.json"]) {
    assert.equal(fs.existsSync(path.join(PUBLIC, rel)), false, `${rel} must not be exported`);
  }
});

test("Brotli/gzip round-trip; production entries/CSS are bundled, hash-addressed and rewritten in HTML", { skip: !built }, () => {
  const mapping = json("public/data/asset-manifest.json").files;
  for (const source of ["assets/js/account.mjs", "assets/js/room.mjs", "assets/js/quiz.mjs", "assets/css/ekguru.css", "data/practice/manifest.json"]) {
    const rel = mapping[source] || source, original = fs.readFileSync(path.join(PUBLIC, rel));
    assert.deepEqual(brotliDecompressSync(fs.readFileSync(path.join(PUBLIC, rel + ".br"))), original);
    assert.deepEqual(gunzipSync(fs.readFileSync(path.join(PUBLIC, rel + ".gz"))), original);
    assert.ok(fs.statSync(path.join(PUBLIC, rel + ".br")).size < original.length);
    if (mapping[source]) { assert.match(rel, /\.(?:[A-Z0-9]{8}|[a-f0-9]{12})\.(?:mjs|css)$/); assert.equal(fs.existsSync(path.join(PUBLIC, source)), false); }
  }
  const html = fs.readFileSync(path.join(PUBLIC, "subjects/practice/index.html"), "utf8");
  assert.ok(html.includes(mapping["assets/js/account.mjs"])); assert.ok(html.includes(mapping["assets/js/quiz.mjs"])); assert.ok(html.includes(mapping["assets/css/ekguru.css"]));
  const quiz = fs.readFileSync(path.join(PUBLIC, mapping["assets/js/quiz.mjs"]), "utf8");
  assert.ok(quiz.length < 35000, "native CBT must not bundle PDF.js or a framework"); assert.ok(!quiz.includes("pdfjsVersion"));
  assert.ok(fs.statSync(path.join(PUBLIC, "data/banks/cn/topics.json")).size < 6000);
});

test("Vercel function is separate from static output; API dispatch and immutable hash caching are emitted", { skip: !built }, () => {
  const output = json(".vercel/output/config.json");
  assert.equal(output.version, 3);
  assert.ok(output.routes.some((route) => route.dest === "/api?__path=$1"));
  const immutable = output.routes.find((route) => route.headers?.["Cache-Control"]?.includes("immutable"));
  assert.ok(new RegExp(immutable.src).test("/data/banks/cn/T01.d1e56839b7ef.min.json"));
  const general = output.routes.findIndex((route) => route.headers?.["Cache-Control"]?.includes("must-revalidate"));
  assert.ok(general < output.routes.indexOf(immutable), "specific cache rule must override the general rule, not vice versa");
  assert.ok(new RegExp(immutable.src).test("/data/quizzes/reasoning/series-12.d1e56839b7ef.min.json"));
  const assetCache = output.routes.find((route) => route.src?.startsWith("/assets/") && route.headers?.["Cache-Control"]?.includes("immutable"));
  for (const name of Object.values(json("public/data/asset-manifest.json").files)) assert.ok(new RegExp(assetCache.src).test("/" + name));
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

test("only the manifest, subject indexes and published test banks ship; no authoring data or unselected bank is in the player bundle", { skip: !built }, () => {
  const manifest = json("public/data/quizzes/manifest.json");
  assert.ok(manifest.subjects.length >= 3); assert.ok(manifest.test_count >= 6);
  assert.ok(fs.statSync(path.join(PUBLIC, "data/quizzes/manifest.json")).size < 2000);
  for (const subject of manifest.subjects) for (const bank of json("public/" + subject.file).tests) if (bank.file) assert.ok(fs.existsSync(path.join(PUBLIC, bank.file)));
});
