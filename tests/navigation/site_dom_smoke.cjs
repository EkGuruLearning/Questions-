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

async function render(page, waitForSelector) {
  const assetPath = page.split("?")[0];
  let html = fs.readFileSync(path.join(ROOT, assetPath), "utf8");
  const scripts = [...html.matchAll(/<script\s+src="([^"]+)"[^>]*><\/script>/g)];
  const injected = scripts
    .filter((match) => !/type="module"/.test(match[0]))
    .map((match) => {
      const src = match[1].replace(/^https?:\/\/[^/]+\//, "");
      const file = path.join(path.dirname(path.join(ROOT, assetPath)), src);
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
  await new Promise((resolve) => setTimeout(resolve, 150));
  if (waitForSelector) {
    await waitFor(() => dom.window.document.querySelector(waitForSelector), `${page}: ${waitForSelector} to render`);
  }
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

/* The pages render from data/site.json, so give the async render a moment and
   fail with a clear message instead of a null-property crash. */
async function waitFor(check, message, timeout = 5000) {
  const started = Date.now();
  for (;;) {
    const value = check();
    if (value) return value;
    if (Date.now() - started > timeout) throw new Error("timeout: " + message);
    await new Promise((resolve) => setTimeout(resolve, 50));
  }
}

async function main() {
  const results = [];
  let failures = 0;

  // ---- home -------------------------------------------------------------
  {
    const dom = await render("index.html", "#subjectCards .subject-card");
    const doc = dom.window.document;
    const questions = doc.querySelector("[data-count='questions']").textContent.trim();
    const subjects = doc.querySelector("[data-count='subjects']").textContent.trim();
    const downloads = doc.querySelector("[data-count='downloads']").textContent.trim();
    assertClean(dom, "index.html");
    assert(questions === "1,554", `home: expected 1,554 questions, saw ${questions}`);
    assert(subjects === "4", `home: expected 4 subjects, saw ${subjects}`);
    assert(downloads === "38", `home: expected 38 files, saw ${downloads}`);

    const cards = [...doc.querySelectorAll("#subjectCards .subject-card")];
    assert(cards.length === 4, `home: expected 4 subject cards, saw ${cards.length}`);
    const names = cards.map((card) => card.querySelector("h3").textContent.trim());
    for (const expected of ["Computer Network", "Rajasthan Geography", "Reasoning", "Previous Year Papers"]) {
      assert(names.includes(expected), `home: subject card missing: ${expected}`);
    }

    const pyq = cards.find((card) => /Previous Year Papers/.test(card.textContent));
    const pyqFolders = [...pyq.querySelectorAll(".folder-card strong")].map((node) => node.textContent.trim());
    for (const exam of ["IA", "SCI", "Computer Operator", "System Assistant", "DSSSB", "SSC", "NET", "RPSC"]) {
      assert(pyqFolders.includes(exam), `home: previous year papers missing exam folder: ${exam}`);
    }

    const navLinks = [...doc.querySelectorAll("nav.site-nav a")].map((link) => link.textContent.trim());
    for (const expected of ["Home", "All Subjects", "Computer Network", "Reasoning", "Previous Year Papers"]) {
      assert(navLinks.includes(expected), `home: nav link missing: ${expected}`);
    }
    const footerLinks = [...doc.querySelectorAll("[data-footer-subjects] a")];
    assert(footerLinks.length === 4, `home: footer should list 4 subjects, saw ${footerLinks.length}`);
    assert(/\d+ subjects · \d+ files/.test(doc.querySelector("[data-footer-stats]").textContent),
      "home: footer stats are missing");

    results.push(`home: ${cards.length} subject cards (${pyqFolders.length} exam folders), nav + footer from site data`);
    dom.window.close();
  }

  // ---- computer network hub --------------------------------------------
  {
    const dom = await render("subjects/computer-network/index.html", "#topicGrid .topic-card");
    const doc = dom.window.document;
    assertClean(dom, "subjects/computer-network/index.html");
    const folders = doc.querySelectorAll("#subjectFolders .folder-card");
    assert(folders.length === 5, `CN hub: expected 5 folder tiles, saw ${folders.length}`);
    const folderNames = [...folders].map((tile) => tile.querySelector("strong").textContent.trim());
    assert(folderNames.join("|") === "Theory|Practice questions|Answers & explanations|Tests|Reference book",
      `CN hub: folder order/names are wrong: ${folderNames.join("|")}`);
    assert(/8 file/.test(folders[0].textContent), `CN hub: theory folder should show 8 files, saw ${folders[0].textContent}`);
    const cards = [...doc.querySelectorAll("#topicGrid .topic-card")];
    assert(cards.length === 7, `CN hub: expected 7 topic cards, saw ${cards.length}`);
    const first = cards[0];
    assert(/T01/.test(first.textContent), "CN hub: first card is not T01");
    const testLink = first.querySelector("a[href*='test/index.html?topic=T01']");
    assert(testLink, "CN hub: topic card has no deep link into the test page");
    assert(/374/.test(first.textContent), "CN hub: T01 question count is missing");
    results.push(`CN hub: ${folders.length} folder tiles + ${cards.length} topic cards with deep links`);
    dom.window.close();
  }

  // ---- material page: folders first, then files --------------------------
  {
    const dom = await render("subjects/computer-network/material/index.html", "#folderBrowser .folder-card");
    const doc = dom.window.document;
    assertClean(dom, "material page");
    const tiles = [...doc.querySelectorAll("#folderBrowser .folder-card")];
    assert(tiles.length === 5, `material page: expected 5 folder tiles, saw ${tiles.length}`);
    assert(doc.querySelectorAll("#folderBrowser .material-item").length === 0, "material page: files should sit inside a folder");
    assert(/Saare folders/.test(doc.getElementById("folderCrumbs").textContent), "material page: breadcrumb is missing");
    results.push(`material page: ${tiles.length} folder tiles, files hidden until a folder is opened`);
    dom.window.close();
  }

  // ---- material page: open the answers folder ----------------------------
  {
    const dom = await render("subjects/computer-network/material/index.html?folder=answers", "#folderBrowser .material-item");
    const doc = dom.window.document;
    assertClean(dom, "answers folder");
    assert(/Answers & explanations/.test(doc.getElementById("folderCrumbs").textContent), "answers: breadcrumb should show the folder");
    const items = doc.querySelectorAll("#folderBrowser .material-item");
    assert(items.length === 5, `answers folder: expected 5 files, saw ${items.length}`);
    assert(/answers\//.test(items[0].querySelector("a[download]").textContent + items[0].innerHTML), "answers: download link is wrong");
    const crumbs = doc.querySelectorAll("#folderCrumbs a");
    assert(crumbs.length >= 1, "answers: breadcrumb should link back to the folder list");
    assert(!/\?folder=/.test(crumbs[0].getAttribute("href")), "answers: first crumb must return to the folder list");
    results.push(`answers folder: ${items.length} files with working download links`);
    dom.window.close();
  }

  // ---- subject explorer: saare subjects ---------------------------------
  {
    const dom = await render("subjects/index.html", "#subjectExplorer .subject-card");
    const doc = dom.window.document;
    assertClean(dom, "subjects index");
    const cards = doc.querySelectorAll("#subjectExplorer .subject-card");
    assert(cards.length === 4, `explorer: expected 4 subject cards, saw ${cards.length}`);
    results.push(`explorer: ${cards.length} subject cards`);
    dom.window.close();
  }

  // ---- subject explorer: naya subject bina page code ke -----------------
  {
    const dom = await render("subjects/index.html?subject=reasoning", "#subjectExplorer .folder-card");
    const doc = dom.window.document;
    assertClean(dom, "reasoning explorer");
    assert(/Reasoning/.test(doc.getElementById("explorerTitle").textContent), "explorer: subject title is wrong");
    const tiles = [...doc.querySelectorAll("#subjectExplorer .folder-card")];
    const names = tiles.map((tile) => tile.querySelector("strong").textContent.trim());
    assert(names.join("|") === "Theory|Practice questions|Answers & explanations|Tests",
      `explorer: reasoning folders are wrong: ${names.join("|")}`);
    assert(tiles.every((tile) => tile.classList.contains("is-empty")), "explorer: empty folders should be marked");
    results.push("explorer: Reasoning folders (khali, file daalte hi bhar jayenge)");
    dom.window.close();
  }

  // ---- previous year papers: exam sections ------------------------------
  {
    const dom = await render("subjects/index.html?subject=previous-year-papers", "#subjectExplorer .folder-card");
    const doc = dom.window.document;
    assertClean(dom, "pyq explorer");
    const names = [...doc.querySelectorAll("#subjectExplorer .folder-card strong")].map((n) => n.textContent.trim());
    for (const exam of ["IA", "SCI", "Computer Operator", "System Assistant", "DSSSB", "SSC", "NET", "RPSC"]) {
      assert(names.includes(exam), `pyq: missing exam folder ${exam}`);
    }
    results.push(`previous year papers: ${names.length} exam sections`);
    dom.window.close();
  }

  // ---- geography: Map folder -> Rajasthan folder -> maps -----------------
  {
    const dom = await render("subjects/rajasthan-geography/index.html", "#folderBrowser .folder-card");
    const doc = dom.window.document;
    assertClean(dom, "map page");
    const hero = doc.querySelector(".map-frame img");
    assert(hero && /rajasthan-border-atlas-preview\.webp$/.test(hero.getAttribute("src")), "map page: hero map image is missing");
    const topTiles = [...doc.querySelectorAll("#folderBrowser .folder-card")];
    assert(topTiles.length === 1, `map page: expected the Map folder, saw ${topTiles.length} tiles`);
    assert(/Map/.test(topTiles[0].textContent), "map page: the folder should be called Map");
    assert(/folder=map$/.test(new URL(topTiles[0].getAttribute("href"), "https://example.test/Questions-/").search)
      || /folder=map%2F/.test(topTiles[0].getAttribute("href")), "map page: Map folder link is wrong");
    results.push("map page: Map folder tile");
    dom.window.close();
  }

  {
    const dom = await render("subjects/rajasthan-geography/index.html?folder=map", "#folderBrowser .folder-card");
    const doc = dom.window.document;
    assertClean(dom, "Map folder");
    const tiles = [...doc.querySelectorAll("#folderBrowser .folder-card")];
    assert(tiles.length === 1, `Map folder: expected the Rajasthan folder, saw ${tiles.length}`);
    assert(/Rajasthan/.test(tiles[0].textContent), "Map folder: the subfolder should be Rajasthan");
    results.push("Map folder: Rajasthan subfolder tile");
    dom.window.close();
  }

  {
    const dom = await render("subjects/rajasthan-geography/index.html?folder=map%2Frajasthan", "#folderBrowser .material-item");
    const doc = dom.window.document;
    assertClean(dom, "Rajasthan folder");
    const crumbs = doc.getElementById("folderCrumbs").textContent;
    assert(/Map/.test(crumbs) && /Rajasthan/.test(crumbs), `Rajasthan folder: breadcrumb is wrong: ${crumbs}`);
    const items = doc.querySelectorAll("#folderBrowser .material-item");
    assert(items.length === 6, `Rajasthan folder: expected 6 maps, saw ${items.length}`);
    const thumb = items[0].querySelector("img");
    assert(thumb, "Rajasthan folder: map files should show a preview thumbnail");
    assert(/data\/thumbs\/rajasthan-geography\/map\/rajasthan\/.+\.png$/.test(thumb.getAttribute("src")), `Rajasthan folder: preview src is wrong: ${thumb.getAttribute("src")}`);
    const fullLink = items[0].querySelector("a.button.secondary");
    assert(/content\/rajasthan-geography\/map\/rajasthan\/.+\.png$/.test(fullLink.getAttribute("href")), "Rajasthan folder: the full-size map link is missing");
    assert(/download/.test(items[0].innerHTML), "Rajasthan folder: download button is missing");
    const firstAlt = items[0].querySelector("img").getAttribute("alt");
    assert(/Rajasthan border districts|Rajasthan border district atlas/.test(firstAlt), `Rajasthan folder: SEO alt text is missing: ${firstAlt}`);
    const described = [...items].filter((item) => item.querySelector(".file-description"));
    assert(described.length === items.length, "Rajasthan folder: every map should show its SEO description");
    assert(/41/.test(items[0].textContent) && /सीमावर्ती/.test(items[0].textContent), "Rajasthan folder: the description text is not shown");
    results.push(`Rajasthan folder: ${items.length} map files with previews and downloads`);
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
