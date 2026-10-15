#!/usr/bin/env node
/* End-to-end DOM test for the online test page.
 *
 * jsdom cannot execute ES modules, so this script assembles the two real source
 * files (engine.mjs + test.mjs) into one classic script, swaps `import.meta.url`
 * for the real script URL, and then drives the page the way a student would:
 * pick a topic -> start -> answer -> submit -> check the result screen.
 *
 * Exits 77 when jsdom is not installed (optional tooling, no runtime dependency).
 *
 *   NODE_PATH=/path/to/node_modules node tests/navigation/test_app_dom_smoke.cjs
 */
"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..", "..");
const BASE = "https://example.test/Questions-/";
const PAGE = "subjects/computer-network/test/index.html";

let JSDOM;
let VirtualConsole;
try {
  ({ JSDOM, VirtualConsole } = require("jsdom"));
} catch (error) {
  console.log("SKIP: jsdom is not installed, so the test-app DOM smoke test was skipped.");
  process.exit(77);
}

function sitePath(rawUrl) {
  let rel = String(rawUrl && rawUrl.url ? rawUrl.url : rawUrl)
    .replace(BASE, "")
    .replace(/^https?:\/\/[^/]+\/Questions-\//, "")
    .replace(/^file:\/\//, "");
  rel = decodeURIComponent(rel).split("?")[0].split("#")[0].replace(/^\//, "");
  return path.join(ROOT, rel);
}

function appSource() {
  const engine = fs.readFileSync(path.join(ROOT, "assets/js/engine.mjs"), "utf8")
    .replace(/^export\s+/gm, "");
  const app = fs.readFileSync(path.join(ROOT, "assets/js/test.mjs"), "utf8")
    .replace(/^import .*$/gm, "")
    .replaceAll("import.meta.url", JSON.stringify(BASE + "assets/js/test.mjs"));
  return `${engine}\n${app}`;
}

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function until(check, message, timeout = 6000) {
  const started = Date.now();
  for (;;) {
    const value = check();
    if (value) return value;
    if (Date.now() - started > timeout) throw new Error("timeout: " + message);
    await sleep(50);
  }
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

async function main() {
  const pageFile = path.join(ROOT, PAGE);
  let html = fs.readFileSync(pageFile, "utf8");
  html = html.replace('<script type="module" src="../../../assets/js/test.mjs"></script>', "");
  html = html.replace("</head>", `<script>
    window.fetch = async function (input) {
      const text = window.__readFile(String(input && input.url ? input.url : input));
      if (text === null) return { ok: false, status: 404, json: async () => { throw new Error("404"); } };
      return { ok: true, status: 200, json: async () => JSON.parse(text) };
    };
  <\/script></head>`);
  html = html.replace("</body>", `<script>${appSource()}<\/script></body>`);

  const errors = [];
  const virtualConsole = new VirtualConsole();
  virtualConsole.on("jsdomError", (error) => errors.push(error.message));
  virtualConsole.on("error", (...args) => errors.push(args.join(" ")));

  const dom = new JSDOM(html, {
    url: BASE + PAGE,
    runScripts: "dangerously",
    pretendToBeVisual: true,
    virtualConsole,
    beforeParse(window) {
      window.__readFile = (rawUrl) => {
        const file = sitePath(rawUrl);
        return fs.existsSync(file) ? fs.readFileSync(file, "utf8") : null;
      };
      window.confirm = () => true;
      window.scrollTo = () => {};
    },
  });

  const doc = dom.window.document;
  const $ = (id) => doc.getElementById(id);
  const lines = [];

  // 1. setup screen loads the real topic list
  await until(() => doc.querySelectorAll("#topicPicker .pick-card").length === 7, "topic picker to render");
  assert(/1,554/.test($("bankInfo").textContent), "bank info line does not show the published question count");
  lines.push("setup: 7 topics loaded from the bank manifest");

  // 1b. full mixed mode offers the whole published bank
  $("modeFull").click();
  await until(() => /all 7 topics mixed/.test($("poolStatus").textContent) && !$("startButton").disabled, "full-mix pool to load");
  assert(/1,554/.test($("poolStatus").textContent), "full mix should offer all published questions: " + $("poolStatus").textContent);
  lines.push("full mix: all published questions across the 7 topics");
  $("modeTopic").click();
  await until(() => doc.querySelectorAll("#topicPicker .pick-card").length === 7, "topic picker to return");

  // 2. pick topic T02 and wait for the pool to load
  const cards = [...doc.querySelectorAll("#topicPicker .pick-card")];
  cards[1].click();
  await until(() => /questions ready/.test($("poolStatus").textContent) && !$("startButton").disabled, "question pool to load");
  assert(/\b144\b/.test($("poolStatus").textContent), "T02 pool should contain 144 questions: " + $("poolStatus").textContent);
  assert(doc.querySelectorAll("#sectionPicker label").length === 5, "T02 should expose its 4 sections plus 'all sections'");
  lines.push("topic-wise: T02 pool 144 questions with section filter");

  // 3. section filter narrows the pool
  const poolNumber = () => Number(($("poolStatus").textContent.match(/^[\s]*([\d,]+)/) || [0, "0"])[1].replace(/,/g, ""));
  const sectionBoxes = [...doc.querySelectorAll("#sectionPicker input[value]")];
  sectionBoxes[0].click();
  await until(() => /questions ready/.test($("poolStatus").textContent) && poolNumber() !== 144, "section filter to change the pool size");
  const filtered = poolNumber();
  assert(filtered > 0 && filtered < 144, "one section should narrow the pool: " + filtered);
  lines.push(`section filter: ${filtered} questions in the chosen section`);

  // 4. start a 10-question practice test
  $("countSelect").value = "10";
  $("countSelect").dispatchEvent(new dom.window.Event("change"));
  $("startButton").click();
  await until(() => $("playerPanel").hidden === false && $("optionList").children.length === 4, "player to render a question");
  assert(doc.querySelectorAll("#paletteGrid button").length === 10, "palette should hold 10 questions");
  assert($("questionStem").textContent.trim().length > 5, "question stem is empty");
  lines.push("player: 10-question practice session rendered");

  // 5. answer the first question and check instant feedback
  doc.querySelector("#optionList .option").click();
  await until(() => !$("feedback").hidden, "feedback to appear");
  assert($("feedback").textContent.trim().length > 5, "feedback text is empty");
  lines.push("practice mode: instant feedback after answering");

  // 6. answer the rest and submit
  for (let index = 0; index < 10; index += 1) {
    const options = doc.querySelectorAll("#optionList .option");
    if (options.length && !options[0].disabled) options[0].click();
    const next = $("nextButton");
    if (next && !next.hidden) next.click();
    await sleep(30);
  }
  $("finishButton").click();
  await until(() => $("resultPanel").hidden === false, "result panel to appear");
  assert(/^\d+%$/.test($("scoreValue").textContent), "score ring has no percentage: " + $("scoreValue").textContent);
  assert(doc.querySelectorAll("#resultStats .stat").length === 4, "result statistics are incomplete");
  assert(doc.querySelectorAll("#topicBars .bar-row").length >= 1, "topic-wise score bars are missing");
  doc.getElementById("reviewButton").click();
  assert(doc.querySelectorAll("#reviewList .review-item").length === 10, "review list does not list every question");
  lines.push(`result: ${$("scoreValue").textContent} score, stats, topic bars and 10 review items`);

  // 7. exam pattern: no instant feedback, timer field appears, retry flow works
  $("newTestButton").click();
  assert($("setupPanel").hidden === false, "Naya test should return to the setup screen");
  doc.querySelector("[data-pattern='exam']").click();
  assert($("timeField").hidden === false, "exam pattern should reveal the time limit field");
  await until(() => !$("startButton").disabled, "pool to be ready again");
  $("countSelect").value = "10";
  $("countSelect").dispatchEvent(new dom.window.Event("change"));
  $("startButton").click();
  await until(() => !$("playerPanel").hidden && $("optionList").children.length === 4, "exam session to render");
  doc.querySelector("#optionList .option").click();
  await sleep(60);
  assert($("feedback").hidden === true, "exam pattern must not reveal the answer while running");
  assert(doc.querySelectorAll("#paletteGrid button.answered").length === 1, "palette should mark the answered question");
  $("finishButton").click();
  await until(() => !$("resultPanel").hidden, "exam result to appear");
  assert(/^\d+%$/.test($("scoreValue").textContent), "exam result score is missing");
  lines.push("exam mode: hidden answers, palette marking, submit and result");

  assert(errors.length === 0, "page errors: " + errors.join(" | "));
  dom.window.close();

  console.log("PASS: rendered test-app smoke test");
  lines.forEach((line) => console.log("  - " + line));
}

main().catch((error) => {
  console.error("FAIL: rendered test-app smoke test —", error.message);
  process.exit(1);
});
