/* Optional JSDOM interaction smoke test; install jsdom separately, no runtime dependency. */
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
let JSDOM;
try {
  ({ JSDOM } = require("jsdom"));
} catch {
  console.log("SKIP: jsdom is not installed (the production portal has no npm runtime dependency).");
  process.exit(77);
}

const ROOT = path.resolve(__dirname, "../..");
const html = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
const dom = new JSDOM(html, { url: "http://localhost/Questions-/index.html", pretendToBeVisual: true });
const { window } = dom;
globalThis.window = window;
globalThis.document = window.document;
globalThis.localStorage = window.localStorage;
globalThis.URLSearchParams = URLSearchParams;
Object.defineProperty(globalThis, "navigator", { value: window.navigator, configurable: true });
window.confirm = () => true;
window.HTMLElement.prototype.scrollIntoView = function () {};
window.HTMLElement.prototype.focus = function () {};
window.HTMLDialogElement.prototype.showModal = function () { this.setAttribute("open", ""); };
window.HTMLDialogElement.prototype.close = function () { this.removeAttribute("open"); };

const fetches = [];
globalThis.fetch = async (url) => {
  const target = new URL(url, window.location.href);
  fetches.push(target.pathname);
  const prefix = "/Questions-/";
  const relative = decodeURIComponent(target.pathname.startsWith(prefix) ? target.pathname.slice(prefix.length) : target.pathname.slice(1));
  const file = path.resolve(ROOT, relative);
  if (!file.startsWith(ROOT + path.sep) && file !== path.join(ROOT, "index.html")) throw new Error("fetch path escapes repository");
  if (!fs.existsSync(file)) return { ok: false, status: 404, json: async () => ({}) };
  return { ok: true, status: 200, json: async () => JSON.parse(fs.readFileSync(file, "utf8")) };
};

function wait(ms = 30) { return new Promise((resolve) => setTimeout(resolve, ms)); }

(async () => {
  await import(pathToFileURL(path.join(ROOT, "assets/js/app.mjs")).href);
  await wait(100);
  assert.equal(document.getElementById("totalQuestions").textContent, "1,556");
  assert.equal(document.getElementById("publishedSubjects").textContent, "1");
  assert.equal(document.getElementById("officialCount").textContent, "0");
  assert.equal(document.getElementById("startButton").disabled, false);
  assert.match(document.getElementById("poolStatus").textContent, /847/);
  assert.deepEqual(fetches.map((item) => item.split("/").pop()).filter((name) => name.endsWith(".json")), ["catalog.min.json", "manifest.json"]);

  const navToggle = document.getElementById("navToggle");
  navToggle.click();
  assert.equal(navToggle.getAttribute("aria-expanded"), "true");
  assert.equal(document.getElementById("siteNav").classList.contains("open"), true);
  document.querySelector('#siteNav a[href="#subjects"]').click();
  assert.equal(navToggle.getAttribute("aria-expanded"), "false");

  document.getElementById("topicSelect").value = "T01";
  document.getElementById("questionCountSelect").value = "10";
  document.getElementById("topicSelect").dispatchEvent(new window.Event("change", { bubbles: true }));
  document.getElementById("startButton").click();
  await wait(150);
  assert.equal(document.getElementById("playerPanel").hidden, false);
  assert.equal(document.querySelectorAll("#optionList button").length, 4);
  assert.match(document.getElementById("questionVerification").textContent, /Answer checked/);
  assert.ok(fetches.some((item) => item.includes("T01.")));
  assert.equal(fetches.filter((item) => /T0[2-7]\./.test(item)).length, 0, "only the selected topic chunk should load");

  const qid = document.getElementById("questionId").textContent.match(/CN-T01-\d{4}/)[0];
  const manifest = JSON.parse(fs.readFileSync(path.join(ROOT, "assets/banks/cn/manifest.json"), "utf8"));
  const topicChunk = JSON.parse(fs.readFileSync(path.join(ROOT, manifest.topics.find((item) => item.topic_id === "T01").file), "utf8"));
  const question = topicChunk.find((item) => item.id === qid);
  assert.ok(question);
  document.querySelector(`#optionList button[data-option-id="${question.answer_option_id}"]`).click();
  assert.equal(document.getElementById("feedbackPanel").hidden, false);
  assert.match(document.getElementById("feedbackTitle").textContent, /Correct/);
  document.getElementById("bookmarkButton").click();
  assert.equal(document.getElementById("localBookmarkCount").textContent, "1");
  document.getElementById("sourceDetailsButton").click();
  await wait(100);
  assert.equal(document.getElementById("sourceDialog").hasAttribute("open"), true);
  assert.ok(document.getElementById("sourceDialogContent").textContent.length > 0);
  document.getElementById("closeSourceDialog").click();

  document.getElementById("finishButton").click();
  await wait(50);
  assert.equal(document.getElementById("resultsPanel").hidden, false);
  assert.match(document.getElementById("resultsIntro").textContent, /no negative marking/i);
  assert.equal(document.getElementById("retryWrongButton").disabled, true);
  document.getElementById("reviewAnswersButton").click();
  assert.equal(document.getElementById("reviewList").hidden, false);
  assert.equal(document.querySelectorAll("#reviewList .review-item").length, 10);
  assert.equal(JSON.parse(localStorage.getItem("ekguru.portal.history.v1")).length, 1);

  document.getElementById("verificationSelect").value = "claimed_answer_unverified";
  document.getElementById("verificationSelect").dispatchEvent(new window.Event("change", { bubbles: true }));
  assert.equal(document.getElementById("startButton").disabled, false);
  assert.match(document.getElementById("poolDisclosure").textContent, /opt-in/i);
  document.getElementById("verificationSelect").value = "paper_and_key_checked";
  document.getElementById("verificationSelect").dispatchEvent(new window.Event("change", { bubbles: true }));
  assert.equal(document.getElementById("startButton").disabled, true);

  console.log("PASS: JSDOM portal smoke — catalog-first loading, topic-only fetch, nav, answer feedback, bookmark, source dialog, scoring/review and verification filters.");
  dom.window.close();
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});

function pathToFileURL(file) {
  const { pathToFileURL: toURL } = require("node:url");
  return toURL(file);
}
