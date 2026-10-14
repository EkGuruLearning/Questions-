#!/usr/bin/env node
/* Renders the real pages in jsdom and checks that the lists actually appear.
 *
 * jsdom is optional (no npm runtime dependency is shipped with the site).
 * When it is not installed, this script exits 77 so the release report can mark
 * the check as skipped instead of failed. Run it with jsdom available:
 *
 *   NODE_PATH=/path/to/node_modules node tests/navigation/site_dom_smoke.cjs
 */
"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..", "..");
const BASE = "https://example.test/Questions-/";

let JSDOM;
let VirtualConsole;
try {
  ({ JSDOM, VirtualConsole } = require("jsdom"));
} catch (error) {
  console.log("SKIP: jsdom is not installed, so the rendered DOM smoke test was skipped.");
  process.exit(77);
}

/* The page files are read straight from disk: no HTTP server is needed, and the
   fetch shim is installed through `beforeParse` so it exists before site.js runs. */
function sitePath(rawUrl) {
  let rel = String(rawUrl && rawUrl.url ? rawUrl.url : rawUrl)
    .replace(BASE, "")
    .replace(/^https?:\/\/[^/]+\/Questions-\//, "")
    .replace(/^file:\/\//, "");
  rel = decodeURIComponent(rel).split("?")[0].split("#")[0].replace(/^\//, "");
  return path.join(ROOT, rel);
}

function fetchShim() {
  return `
    window.fetch = async function (input) {
      const text = window.__readFile(String(input && input.url ? input.url : input));
      if (text === null) return { ok: false, status: 404, json: async () => { throw new Error("404"); } };
      return { ok: true, status: 200, json: async () => JSON.parse(text) };
    };
  `;
}

async function render(page) {
  let html = fs.readFileSync(path.join(ROOT, page), "utf8");
  const scripts = [...html.matchAll(/<script\s+src="([^"]+)"[^>]*><\/script>/g)];
  const injected = scripts
    .filter((match) => !/type="module"/.test(match[0]))
    .map((match) => {
      const src = match[1].replace(/^https?:\/\/[^/]+\//, "");
      const file = path.join(path.dirname(path.join(ROOT, page)), src);
      return `<script>${fs.readFileSync(file, "utf8")}<\/script>`;
    })
    .join("\n");
  html = html.replace("</head>", `<script>${fetchShim()}<\/script>\n</head>`);
  html = html.replace(/<script\s+src="[^"]+"[^>]*><\/script>/g, (match) => (/type="module"/.test(match) ? "" : ""));
  html = html.replace("</body>", `${injected}\n</body>`);

  const errors = [];
  const virtualConsole = new VirtualConsole();
  virtualConsole.on("jsdomError", (error) => errors.push(error.message));
  virtualConsole.on("error", (...args) => errors.push(args.join(" ")));
  const dom = new JSDOM(html, {
    url: BASE + page,
    runScripts: "dangerously",
    pretendToBeVisual: true,
    virtualConsole,
    beforeParse(window) {
      window.__readFile = (rawUrl) => {
        const file = sitePath(rawUrl);
        return fs.existsSync(file) ? fs.readFileSync(file, "utf8") : null;
      };
    },
  });
  await new Promise((resolve) => setTimeout(resolve, 300));
  dom.pageErrors = errors;
  return dom;
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function assertClean(dom, page) {
  if (dom.pageErrors.length) {
    throw new Error(`${page}: page errors — ${dom.pageErrors.join(" | ")}`);
  }
}

async function main() {
  const results = [];
  let failures = 0;

  // ---- home -------------------------------------------------------------
  {
    const dom = await render("index.html");
    const doc = dom.window.document;
    const questions = doc.querySelector("[data-count='questions']").textContent.trim();
    const cards = doc.querySelectorAll("[data-subject-card]").length;
    const downloads = doc.querySelector("[data-count='downloads']").textContent.trim();
    assertClean(dom, "index.html");
    assert(questions === "1,554", `home: expected 1,554 questions, saw ${questions}`);
    assert(cards === 2, `home: expected 2 subject cards, saw ${cards}`);
    assert(downloads === "38", `home: expected 38 downloads, saw ${downloads}`);
    results.push("home: 2 subject cards, 1,554 questions, 38 downloads");
    dom.window.close();
  }

  // ---- computer network hub --------------------------------------------
  {
    const dom = await render("subjects/computer-network/index.html");
    const doc = dom.window.document;
    assertClean(dom, "subjects/computer-network/index.html");
    const cards = [...doc.querySelectorAll("#topicGrid .topic-card")];
    assert(cards.length === 7, `CN hub: expected 7 topic cards, saw ${cards.length}`);
    const first = cards[0];
    assert(/T01/.test(first.textContent), "CN hub: first card is not T01");
    const testLink = first.querySelector("a[href*='test/index.html?topic=T01']");
    assert(testLink, "CN hub: topic card has no deep link into the test page");
    assert(/374/.test(first.textContent), "CN hub: T01 question count is missing");
    results.push(`CN hub: ${cards.length} topic cards with test deep links`);
    dom.window.close();
  }

  // ---- material page ----------------------------------------------------
  {
    const dom = await render("subjects/computer-network/material/index.html");
    const doc = dom.window.document;
    assertClean(dom, "material page");
    const items = doc.querySelectorAll("#materialGroups .material-item");
    const filters = doc.querySelectorAll("#materialFilters button");
    assert(items.length === 32, `material page: expected 32 files, saw ${items.length}`);
    assert(filters.length === 8, `material page: expected 8 topic filters, saw ${filters.length}`);
    const download = items[0].querySelector("a[download]");
    assert(download && /\.pdf$/.test(download.getAttribute("href")), "material page: download link is missing");
    results.push(`material page: ${items.length} files, ${filters.length} filters`);
    dom.window.close();
  }

  // ---- geography maps ---------------------------------------------------
  {
    const dom = await render("subjects/rajasthan-geography/index.html");
    const doc = dom.window.document;
    assertClean(dom, "map page");
    const cards = doc.querySelectorAll("#mapGrid .card");
    assert(cards.length === 6, `map page: expected 6 map cards, saw ${cards.length}`);
    results.push(`map page: ${cards.length} map cards`);
    dom.window.close();
  }

  console.log("PASS: rendered DOM smoke test");
  results.forEach((line) => console.log("  - " + line));
  process.exit(failures ? 1 : 0);
}

main().catch((error) => {
  console.error("FAIL: rendered DOM smoke test —", error.message);
  process.exit(1);
});
