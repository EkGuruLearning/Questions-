#!/usr/bin/env node
/* Real production bundles/HTTP/IndexedDB. Auth/cloud portions are explicitly
   mocked; this does not complete live Google OAuth. Optional browser dependencies. */
const assert = require("node:assert/strict"), fs = require("node:fs"), path = require("node:path");
let puppeteer, chromium;
try { puppeteer = require("puppeteer-core"); const mod = require("@sparticuz/chromium"); chromium = mod.default || mod; }
catch { console.log("SKIP: optional puppeteer-core / @sparticuz/chromium not installed"); process.exit(77); }
const BASE = process.env.BASE || "http://127.0.0.1:8000/Questions-/", ROOT = path.resolve(__dirname, "../..");
const SHOTS = path.join(ROOT, ".cache/browser-shots"), A = "a07a8170-ea16-4dd4-8ab3-e8fa19f1d800", B = "9da10d8f-48a8-413a-bb51-c9a70b8b7fa2";
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const id = (n) => `f0000000-0000-4000-8000-${String(n).padStart(12, "0")}`;
const raw = (n, label = `Saved result ${n}`) => ({ id: id(n), kind: "quiz", subject_id: `subject-${n % 50}`, test_id: `test-${n}`, label, total: 20, correct: null, wrong: null, unanswered: 20, score: null, max_score: null, duration_seconds: 20, completed_at: "2026-10-17T00:00:00.000Z", details: {} });
const ready = async (p) => p.waitForFunction(() => !document.getElementById("quizStart").disabled && window.EkGuruAccount);
const fit = async (p) => assert(await p.evaluate((width) => document.documentElement.scrollWidth <= width + 1 && innerWidth <= width + 1, p.viewport().width), "layout viewport expands / content overflows device width");
const number = async (p, value) => p.$eval("#quizNumeric", (e, v) => { e.value = v; e.dispatchEvent(new Event("input", { bubbles: true })); }, value);
async function submit(p) { p.once("dialog", (d) => d.accept()); await p.click("#quizSubmit"); await p.waitForSelector("#quizResult:not([hidden])"); }
async function pageFor(browser, width = 390) {
  const p = await browser.newPage(), client = await p.createCDPSession();
  await client.send("Storage.clearDataForOrigin", { origin: new URL(BASE).origin, storageTypes: "all" }); await client.detach();
  await p.setViewport({ width, height: 900, isMobile: width < 800, hasTouch: width < 800 });
  p.issues = []; p.paths = [];
  p.on("pageerror", (e) => p.issues.push(e.message)); p.on("request", (r) => p.paths.push(new URL(r.url()).pathname));
  return p;
}
(async () => {
  fs.mkdirSync(SHOTS, { recursive: true });
  const browser = await puppeteer.launch({ executablePath: await chromium.executablePath(), args: chromium.args, headless: true });
  const report = { native_widths: [], imported_pdf_browser_checks: [] };
  try {
    for (const width of [320, 360, 390, 768, 951, 1280]) {
      const p = await pageFor(browser, width);
      await p.goto(BASE + "subjects/practice/index.html?subject=reasoning&test=series-12"); await ready(p); await fit(p);
      assert(!p.paths.some((s) => /data\/site\.json|vendor\/pdfjs/.test(s)), "native CBT must not fetch the full catalogue/PDF.js");
      assert.equal(p.paths.filter((s) => /data\/quizzes\/.+\/index\./.test(s)).length, 1, "fetch only selected subject index");
      assert.equal(p.paths.filter((s) => /data\/quizzes\/.+\/series-12\./.test(s)).length, 1);
      await p.$eval("#quizMinutes", (e) => { e.value = "0"; });
      await p.click("#quizStart"); await p.waitForSelector("#quizPlayer:not([hidden])");
      await p.click('[data-answer="B"]'); await p.click("#quizMark"); await p.click("#quizNext");
      await p.click('[data-answer="B"]'); await p.click("#quizPrev");
      assert.equal(await p.$eval('#quizOptions [aria-pressed="true"]', (e) => e.dataset.answer), "B");
      assert.equal(await p.$eval("#quizMark", (e) => e.getAttribute("aria-pressed")), "true");
      assert.equal(await p.$eval("#quizCheck", (e) => e.hidden), true);
      await p.$eval("#quizPaletteDetails", (e) => { e.open = true; }); await p.click("#quizPalette button:nth-child(3)");
      await p.click('[data-answer="C"]'); await p.click("#quizClear");
      assert.equal(await p.$$eval('#quizOptions [aria-pressed="true"]', (e) => e.length), 0);
      await fit(p);
      if ([390, 1280].includes(width)) { await sleep(150); await p.screenshot({ path: path.join(SHOTS, `native-cbt-${width}.png`), fullPage: true }); }
      const saved = await p.evaluate(() => JSON.parse(localStorage.getItem("ekguru.quiz.draft.v1.reasoning.series-12.guest")));
      await p.click("#quizLeave"); await p.reload(); await ready(p); await p.click("#quizResume");
      await p.waitForSelector("#quizPlayer:not([hidden])");
      const restored = await p.evaluate(() => JSON.parse(localStorage.getItem("ekguru.quiz.draft.v1.reasoning.series-12.guest")));
      assert.equal(restored.id, saved.id); assert.equal(restored.started_at, saved.started_at); assert.deepEqual(restored.answers, saved.answers);
      if (width === 320) await p.setOfflineMode(true);
      await submit(p);
      await p.waitForFunction(async () => (await window.EkGuruAccount.historyStore.page("guest")).attempts.length === 1);
      const history = await p.evaluate(async () => (await window.EkGuruAccount.historyStore.page("guest")).attempts[0]);
      assert.equal(history.subject_id, "reasoning"); assert.equal(history.test_id, "series-12"); assert.equal(history.correct, 2); assert.equal(history.max_score, 12);
      if (width === 320) await p.setOfflineMode(false);
      assert.equal(await p.$$eval("#quizReview .review-item", (e) => e.length), 0, "review DOM must be lazy");
      await p.click("#quizReviewDetails summary"); await p.waitForFunction(() => document.querySelectorAll("#quizReview .review-item").length === 12);
      await p.goto(BASE + "subjects/account/index.html"); await p.waitForSelector("#accountHistory .history-row");
      assert.match(await p.$eval("#accountHistory", (e) => e.textContent), /reasoning.*Series practice/s); await fit(p);
      assert(await p.$$eval("#historySubject, #historyTest", (fields) => fields.every((field) => field.getBoundingClientRect().height >= 44 && parseFloat(getComputedStyle(field).fontSize) >= 16)), "History filters need phone-sized targets and no iOS input zoom");
      assert.deepEqual(p.issues, []); await p.close(); report.native_widths.push(width);
      console.log(`PASS native CBT ${width}px: real questions, selection/clear/review, owner-bound resume, result journal; ${width === 320 ? "offline finish; " : ""}guest history`);
    }
    {
      const p = await pageFor(browser, 1280);
      await p.goto(BASE + "subjects/practice/index.html?subject=computer-network&test=it-fundamentals-5"); await ready(p);
      await p.select("#quizMode", "practice"); await p.$eval("#quizMinutes", (e) => { e.value = "0"; }); await p.click("#quizStart");
      await p.click('[data-answer="B"]'); await p.click("#quizCheck"); assert.match(await p.$eval("#quizFeedback", (e) => e.textContent), /^CORRECT/);
      await p.click("#quizNext"); await p.click('[data-answer="A"]'); await p.click("#quizCheck"); assert.match(await p.$eval("#quizFeedback", (e) => e.textContent), /^WRONG/);
      await p.click('[data-answer="B"]'); await p.click("#quizCheck"); assert.match(await p.$eval("#quizFeedback", (e) => e.textContent), /^CORRECT/);
      assert.equal(await p.$$eval('#quizOptions [aria-pressed="true"]', (e) => e.length), 2);
      await p.click("#quizNext"); await number(p, "32"); await p.click("#quizCheck"); assert.match(await p.$eval("#quizFeedback", (e) => e.textContent), /^CORRECT/);
      await p.click("#quizClear"); assert.equal(await p.$eval("#quizNumeric", (e) => e.value), ""); await number(p, "32");
      await p.click("#quizNext"); await p.click('[data-answer="A"]'); await p.click("#quizNext"); await number(p, "11"); await submit(p);
      assert.match(await p.$eval("#quizStats", (e) => e.textContent), /5 \/ 5/);
      await p.click("[data-theme-toggle]"); await p.click("[data-theme-toggle]");
      assert.equal(await p.evaluate(() => document.documentElement.dataset.theme), "dark");
      await p.reload(); await ready(p); assert.equal(await p.evaluate(() => document.documentElement.dataset.theme), "dark");
      await p.screenshot({ path: path.join(SHOTS, "native-dark-1280.png"), fullPage: true });
      assert.deepEqual(p.issues, []); await p.close(); console.log("PASS single/MSQ/numeric native controls, exact-set key checks, 5/5 scoring, manual dark theme persists");
    }
    {
      const p = await pageFor(browser);
      await p.goto(BASE + "subjects/practice/index.html?subject=previous-year-papers&test=rpsc-programmer-2024-paper-1"); await ready(p);
      await p.select("#quizMode", "practice"); await p.$eval("#quizMinutes", (e) => { e.value = "0"; }); await p.click("#quizStart");
      assert.equal(await p.$eval("#quizQuestionNumber", (e) => e.textContent), "Question 1 of 100");
      assert.equal(await p.$$eval("#quizOptions button", (e) => e.length), 5); assert.equal(await p.$$eval("#quizPlayer canvas", (e) => e.length), 0);
      await p.click('[data-answer="C"]'); assert.equal(await p.$eval('#quizOptions [aria-pressed="true"]', (e) => e.dataset.answer), "C"); await p.$eval("#quizPaletteDetails", (e) => { e.open = true; }); await p.click("#quizPalette button:nth-child(3)");
      await p.click("#quizCheck"); assert.match(await p.$eval("#quizFeedback", (e) => e.textContent), /Unscored/);
      await submit(p); assert.match(await p.$eval("#quizStats", (e) => e.textContent), /1 \/ 98/); assert.match(await p.$eval("#quizResultNote", (e) => e.textContent), /2 unkeyed/);
      assert(!p.paths.some((s) => /vendor\/pdfjs|\.pdf$/.test(s)), "native RPSC does not load the PDF/OMR interface");
      await p.goto(BASE + "subjects/practice/index.html?subject=reasoning&test=series-12"); await ready(p); await p.click("#quizStart"); await p.click("#quizLeave");
      await p.evaluate(() => { const k = "ekguru.quiz.draft.v1.reasoning.series-12.guest", d = JSON.parse(localStorage.getItem(k)); d.started_at = Date.now() - 120000; d.minutes = 1; d.deadline = Date.now() + 99999999; localStorage.setItem(k, JSON.stringify(d)); });
      await p.reload(); await ready(p); await p.click("#quizResume"); await p.waitForSelector("#quizResult:not([hidden])");
      assert.match(await p.$eval("#quizResultTitle", (e) => e.textContent), /Time up.*01:00/);
      assert.deepEqual(p.issues, []); await p.close(); console.log("PASS RPSC native transcription, 98-key partial scoring, no PDF.js, and wall-clock auto-submit after reload");
    }
    {
      const p = await pageFor(browser); let active = A, online = false; const accepted = [], posts = [];
      const fixtures = Array.from({ length: 551 }, (_, i) => raw(i + 1)).reverse();
      await p.setRequestInterception(true);
      p.on("request", (request) => {
        const url = new URL(request.url()), send = (data, status = 200) => request.respond({ status, contentType: "application/json", body: JSON.stringify(data) });
        if (url.pathname === "/api/auth/session") return send({ configured: true, google_enabled: true, user: { id: active, name: active === A ? "Student A <script>not executed</script>" : "Student B", email: "example@example.test" } });
        if (url.pathname === "/api/attempts") {
          const expected = request.headers()["x-ekguru-user"]; assert.equal(expected, active, "account-bound request header");
          if (request.method() === "POST") { const value = JSON.parse(request.postData()); posts.push({ user: active, ...value }); if (online) accepted.push(value.id); return send(online ? { ok: true } : { error: "offline" }, online ? 201 : 503); }
          let rows = active === A ? fixtures : [raw(999, "B private result")];
          for (const field of ["subject_id", "test_id"]) if (url.searchParams.get(field)) rows = rows.filter((r) => r[field] === url.searchParams.get(field));
          const offset = url.searchParams.get("cursor") ? Number(Buffer.from(url.searchParams.get("cursor"), "base64url").toString()) : 0;
          const limit = Number(url.searchParams.get("limit") || 50);
          return send({ attempts: rows.slice(offset, offset + limit), next_cursor: offset + limit < rows.length ? Buffer.from(String(offset + limit)).toString("base64url") : null });
        }
        request.continue();
      });
      await p.goto(BASE + "subjects/account/index.html"); await p.waitForFunction(() => document.querySelectorAll("#accountHistory .history-row").length === 50);
      await p.click("#historyMore"); await p.waitForFunction(() => document.querySelectorAll("#accountHistory .history-row").length === 100);
      await p.click("#historyMore"); await p.waitForFunction(() => document.querySelectorAll("#accountHistory .history-row").length === 150);
      await p.$eval("#historyTest", (e) => { e.value = "test-1"; }); await p.click('#historyFilter button[type="submit"]');
      await p.waitForFunction(() => document.querySelectorAll("#accountHistory .history-row").length === 1);
      assert.match(await p.$eval("#accountHistory", (e) => e.textContent), /Saved result 1/);
      await p.$eval("#historyTest", (e) => { e.value = ""; }); await p.click('#historyFilter button[type="submit"]');
      await p.waitForFunction(() => document.querySelectorAll("#accountHistory .history-row").length === 50);
      await p.evaluate(() => { const original = URL.createObjectURL; URL.createObjectURL = (blob) => { window.__export = blob; return original(blob); }; });
      await p.click("#historyExport"); await p.waitForFunction(() => window.__export && !document.getElementById("historyExport").disabled);
      const exported = await p.evaluate(async () => JSON.parse(await window.__export.text())); assert.equal(exported.attempts.length, 551);
      await p.evaluate(async ({ user, values, guest }) => { for (const row of values) await window.EkGuruAccount.historyStore.record(user, row, true); await window.EkGuruAccount.historyStore.record("guest", guest, true); }, { user: A, values: Array.from({ length: 35 }, (_, i) => raw(2000 + i)), guest: raw(9000) });
      await p.click("[data-account-sync]"); await p.waitForFunction(() => document.querySelector("[data-cloud-status]").textContent.includes("Sync pending"));
      assert.equal(await p.evaluate(async (user) => (await window.EkGuruAccount.historyStore.pending(user, 1000)).length, A), 35);
      active = B; await p.reload(); await p.waitForFunction(() => window.EkGuruAccount?.user?.name === "Student B");
      await p.waitForSelector("#accountHistory .history-row"); assert.match(await p.$eval("#accountHistory", (e) => e.textContent), /B private/);
      assert.equal(posts.filter((r) => r.user === B).length, 0, "A's queued results must not upload into B");
      active = A; online = true; await p.reload();
      await p.waitForFunction(async (user) => window.EkGuruAccount?.user?.id === user && (await window.EkGuruAccount.historyStore.pending(user, 1000)).length === 0, { timeout: 30000 }, A);
      assert.equal(new Set(accepted).size, 35); assert(!accepted.includes(id(9000)), "guest history stays guest");
      assert(posts.every((r) => r.user_id === undefined), "caller never sends a trusted user_id");
      assert.equal(await p.$$eval("#accountHistory script", (e) => e.length), 0); await fit(p);
      await p.screenshot({ path: path.join(SHOTS, "universal-history-390.png"), fullPage: true });
      assert.deepEqual(p.issues, []); await p.close(); console.log("PASS mocked cloud: 551-result paging/filter/export, 35-result offline queue without truncation, A/B isolation, guest non-upload, stable retry IDs (not live OAuth)");
    }
    for (const record of JSON.parse(fs.readFileSync(path.join(ROOT, "data/catalog/imported-papers.json"))).papers) {
      const p = await pageFor(browser, 768);
      await p.goto(BASE + "subjects/reader/index.html?" + new URLSearchParams({ file: record.file }));
      await p.waitForFunction(() => document.getElementById("readerStatus").textContent.startsWith("Ready"), { timeout: 45000 });
      assert.match(await p.$eval("#pageLabel", (e) => e.textContent), new RegExp(`1 / ${record.page_count}$`)); await fit(p);
      const rendered = await p.evaluate(async (file, base) => {
        const mod = await import(new URL("assets/vendor/pdfjs/pdf.min.mjs", base).href);
        const task = mod.getDocument({ url: new URL(file, base).href, isEvalSupported: false, standardFontDataUrl: new URL("assets/vendor/pdfjs/standard_fonts/", base).href, cMapUrl: new URL("assets/vendor/pdfjs/cmaps/", base).href, cMapPacked: true });
        const pdf = await task.promise, page = await pdf.getPage(pdf.numPages), view = page.getViewport({ scale: .3 }), canvas = document.createElement("canvas"); canvas.width = Math.ceil(view.width); canvas.height = Math.ceil(view.height);
        await page.render({ canvasContext: canvas.getContext("2d"), viewport: view }).promise;
        const result = { version: mod.version, pages: pdf.numPages, last_page_rendered: true }; await pdf.destroy(); return result;
      }, record.file, BASE);
      assert.equal(rendered.pages, record.page_count); assert.deepEqual(p.issues, []);
      report.imported_pdf_browser_checks.push({ file: record.file, ...rendered }); await p.close();
      console.log(`PASS PDF.js ${rendered.version}: ${path.basename(record.file)} · ${rendered.pages} pages · first/last render`);
    }
    fs.writeFileSync(path.join(ROOT, ".cache/universal-browser-report.json"), JSON.stringify(report, null, 2));
    console.log("PASS universal CBT/history/PDF browser regressions; screenshots/report stay ignored in .cache/");
  } finally { await browser.close(); }
})().catch((error) => { console.error(error.stack || error); process.exitCode = 1; });
