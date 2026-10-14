#!/usr/bin/env node
/* Static page checks — no browser, no JavaScript needed.
 *
 * The site is generated as plain HTML (tools/build_pages.py), so the content a
 * visitor sees must already be inside the HTML file. These checks read the real
 * pages and assert exactly that: lists, breadcrumbs with a way back up, nav and
 * footer links, file rows with download buttons.
 *
 * The interactive test page keeps its own jsdom check (test_app_dom_smoke.cjs).
 *
 *   node tests/navigation/site_dom_smoke.cjs
 */
"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..", "..");
const results = [];
let failures = 0;

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function read(rel) {
  const file = path.join(ROOT, rel);
  assert(fs.existsSync(file), `missing page: ${rel}`);
  return fs.readFileSync(file, "utf8");
}

function all(html, pattern) {
  return [...html.matchAll(pattern)];
}

function section(title, fn) {
  try {
    const detail = fn();
    results.push(`${title}: ${detail}`);
  } catch (error) {
    failures += 1;
    results.push(`FAIL ${title}: ${error.message}`);
  }
}

function links(html) {
  return all(html, /<a\b[^>]*href="([^"]+)"[^>]*>/g).map((match) => match[1]);
}

/* repo path a link on `page` resolves to */
function repoPath(page, href) {
  const clean = href.split("?")[0].split("#")[0];
  if (!clean || /^[a-z]+:/i.test(clean)) return "";
  const resolved = path.posix.normalize(path.posix.join(path.posix.dirname(page), clean));
  return resolved.split("/").filter((part) => part !== "..").join("/");
}

function text(html) {
  return html.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ");
}

/* home ------------------------------------------------------------------ */
section("home (static HTML)", () => {
  const html = read("index.html");
  assert(!/assets\/js\/site\.js/.test(html), "home must not depend on site.js");
  const cards = all(html, /class="card subject-card"/g).length;
  assert(cards === 4, `expected 4 subject cards in the HTML, saw ${cards}`);
  for (const subject of ["Computer Network", "Rajasthan Geography", "Reasoning", "Previous Year Papers"]) {
    assert(text(html).includes(subject), `home is missing the ${subject} card`);
  }
  const navTargets = links(html).map((href) => repoPath("index.html", href));
  for (const href of ["subjects/computer-network/index.html", "subjects/index.html",
                      "subjects/previous-year-papers/index.html"]) {
    assert(navTargets.includes(href), `home nav is missing ${href}`);
  }
  assert(/class="hero-stat"/.test(html), "home hero stats are missing");
  assert(/1,554/.test(text(html)), "home should show the 1,554 online questions");
  return `${cards} subject cards, nav + footer + hero stats baked into the HTML`;
});

/* subject explorer ------------------------------------------------------- */
section("subjects/index.html", () => {
  const html = read("subjects/index.html");
  const cards = all(html, /class="card subject-card"/g).length;
  assert(cards === 4, `expected 4 subject cards, saw ${cards}`);
  const up = all(html, /class="crumb-up" href="([^"]+)"/g).map((match) => match[1]);
  assert(up.length === 1 && repoPath("subjects/index.html", up[0]) === "index.html",
    "the explorer should offer one way back, to Home");
  assert(text(html).includes("Saare subjects"), "explorer heading is missing");
  return `${cards} subjects, breadcrumb, static links`;
});

/* computer network ------------------------------------------------------- */
section("computer-network subject page", () => {
  const html = read("subjects/computer-network/index.html");
  const tiles = all(html, /class="folder-card[^"]*" href="([^"]+)"/g)
    .map((match) => repoPath("subjects/computer-network/index.html", match[1]));
  assert(tiles.length === 5, `expected 5 folder tiles, saw ${tiles.length}`);
  for (const folder of ["theory", "practice", "answers", "tests", "reference"]) {
    assert(tiles.includes(`subjects/computer-network/${folder}/index.html`), `missing folder tile: ${folder}`);
  }
  const topics = all(html, /class="card topic-card"/g).length;
  assert(topics === 7, `expected 7 topic cards, saw ${topics}`);
  assert(/test\/index\.html\?topic=T01/.test(html), "topic cards need a deep link into the test");
  assert(/class="crumb-up"/.test(html), "subject page needs an up link");
  return `${tiles.length} folder tiles + ${topics} topic cards`;
});

/* one folder page per folder -------------------------------------------- */
section("folder page (files + breadcrumb back up)", () => {
  const html = read("subjects/computer-network/answers/index.html");
  const rows = all(html, /class="material-item/g).length;
  assert(rows === 5, `answers folder should list 5 files, saw ${rows}`);
  assert(/download>Download<\/a>/.test(html), "file rows need a download button");
  assert(/crumbs/.test(html) && /crumb-up/.test(html), "folder page needs a breadcrumb with a back link");
  const up = all(html, /class="crumb-up" href="([^"]+)"/g).map((match) => match[1])[0];
  assert(repoPath("subjects/computer-network/answers/index.html", up) === "subjects/computer-network/index.html",
    `the back link should go to the subject page, saw ${up}`);
  return `${rows} files, breadcrumb back to the subject page`;
});

/* deeper folder (year folders) ------------------------------------------ */
section("previous year papers page", () => {
  const subject = read("subjects/previous-year-papers/index.html");
  const exams = all(subject, /class="folder-card[^"]*" href="([^"]+)"/g)
    .map((match) => repoPath("subjects/previous-year-papers/index.html", match[1]));
  for (const exam of ["ia", "sci", "computer-operator", "system-assistant", "dsssb", "ssc", "net", "rpsc"]) {
    assert(exams.includes(`subjects/previous-year-papers/${exam}/index.html`), `missing exam folder: ${exam}`);
  }
  const year = read("subjects/previous-year-papers/rpsc/2024/index.html");
  const files = all(year, /class="material-item/g).length;
  assert(files === 2, `RPSC 2024 should publish the paper + answer key, saw ${files}`);
  assert(/RPSC-Programmer-2024-Paper-1-Questions\.pdf/.test(year), "the question paper link is missing");
  assert(/RPSC-Programmer-2024-Paper-1-Answer-Key\.pdf/.test(year), "the answer key link is missing");
  const crumb = all(year, /<nav class="crumbs"[^>]*>(.*?)<\/nav>/gs);
  assert(crumb.length === 1, "year page needs a breadcrumb");
  const crumbText = text(crumb[0][1]);
  for (const part of ["All Subjects", "Previous Year Papers", "RPSC", "2024"]) {
    assert(crumbText.includes(part), `breadcrumb is missing ${part}: ${crumbText}`);
  }
  return `${exams.length} exam folders, RPSC 2024 page with ${files} files and a full breadcrumb`;
});

/* reasoning (empty folders still published) ------------------------------ */
section("reasoning folder pages", () => {
  const hub = read("subjects/reasoning/index.html");
  const tiles = all(hub, /class="folder-card/g).length;
  assert(tiles === 4, `expected 4 folder tiles, saw ${tiles}`);
  for (const folder of ["theory", "practice", "answers", "tests"]) {
    const page = read(`subjects/reasoning/${folder}/index.html`);
    assert(/material-item/.test(page), `reasoning/${folder} should hold its files`);
  }
  const calendar = read("subjects/reasoning/practice/Calendar/index.html");
  assert(/Calendar-700-Practice-Book-RPSC-RSMSSB\.pdf/.test(calendar), "the Calendar practice set is missing");
  assert(/crumb-up/.test(calendar), "chapter folder page keeps the back link");
  const practice = read("subjects/reasoning/practice/index.html");
  assert(/material-item/.test(practice), "the sample practice paper should be listed");
  assert(/crumb-up/.test(practice), "every folder page keeps the back link");
  return `${tiles} folder pages, empty ones explained`;
});

/* maps ------------------------------------------------------------------- */
section("map folder pages", () => {
  const hub = read("subjects/rajasthan-geography/index.html");
  assert(/map\/index\.html/.test(hub), "the map folder tile is missing");
  const rajasthan = read("subjects/rajasthan-geography/map/rajasthan/index.html");
  const rows = all(rajasthan, /class="material-item/g).length;
  assert(rows === 8, `expected 8 map files (PNG prints + PDF prints), saw ${rows}`);
  assert(/A3-Print\.pdf/.test(rajasthan), "the A3 print PDF should be listed");
  assert(/data\/thumbs\//.test(rajasthan), "map rows should show the light preview image");
  assert(/content\/rajasthan-geography\/map\/rajasthan\//.test(rajasthan), "map download links are missing");
  return `${rows} map rows with previews and downloads`;
});

/* navigation + footer on every page ------------------------------------- */
section("nav + footer on every published page", () => {
  const routes = fs.readFileSync(path.join(ROOT, "data/catalog/site-routes.txt"), "utf8")
    .split("\n").filter((line) => line && !line.startsWith("#"));
  const subjects = Object.keys(JSON.parse(fs.readFileSync(path.join(ROOT, "data/site.json"), "utf8"))
    .subjects.reduce((acc, subject) => ({ ...acc, [subject.slug]: subject }), {}));
  let checked = 0;
  for (const route of routes) {
    if (route === "404.html") continue;  // the not-found page keeps its own short list
    const html = read(route);
    const targets = links(html).map((href) => repoPath(route, href));
    assert(/aria-label="Main navigation"/.test(html), `${route}: nav is missing`);
    for (const slug of subjects) {
      assert(targets.includes(`subjects/${slug}/index.html`), `${route}: nav/footer misses ${slug}`);
    }
    assert(/footer-grid/.test(html), `${route}: footer is missing`);
    checked += 1;
  }
  return `${checked} pages carry the full nav + footer`;
});

/* serialisable count ----------------------------------------------------- */
console.log(failures ? "FAIL: static page checks" : "PASS: static page checks");
for (const line of results) console.log("  - " + line);
process.exit(failures ? 1 : 0);
