#!/usr/bin/env node
/* Real-browser room/account regression. No real Google account or credentials.
   Start: EKGURU_DISABLE_AUTH=true npm run dev
   NODE_PATH=.cache/browser-deps/node_modules node tests/mobile/room_account_check.cjs
   Mocked auth checks are explicitly not a live Google OAuth completion test. */
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
let puppeteer, chromium;
try { puppeteer = require("puppeteer-core"); const mod = require("@sparticuz/chromium"); chromium = mod.default || mod; }
catch { console.log("SKIP: install optional puppeteer-core / @sparticuz/chromium browser tooling"); process.exit(77); }
const BASE = process.env.BASE || "http://127.0.0.1:8000/Questions-/";
const ROOT = path.resolve(__dirname, "../..");
const SHOTS = path.join(ROOT, ".cache/browser-shots");
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const UID = "a07a8170-ea16-4dd4-8ab3-e8fa19f1d800";
const errors = (page) => { const list = []; page.on("pageerror", (error) => list.push(error.message)); return list; };
const noOverflow = async (page) => assert(await page.evaluate((width) => document.documentElement.scrollWidth <= width + 1 && innerWidth <= width + 1, page.viewport().width), "horizontal overflow / expanded layout viewport");
const clickSubmit = async (page) => { page.once("dialog", (dialog) => dialog.accept()); await page.click("#submitPaperButton"); await page.waitForSelector("#paperResult:not([hidden])"); };
const ready = async (page) => {
  await page.waitForFunction(() => document.getElementById("startPaperButton") && !document.getElementById("startPaperButton").disabled);
  await page.$eval("#legacyPaperTools", (node) => { node.open = true; });
};
async function isolatedContext(browser) {
  let page;
  return { async newPage() {
    page = await browser.newPage();
    const client = await page.createCDPSession();
    await client.send("Storage.clearDataForOrigin", { origin: new URL(BASE).origin, storageTypes: "all" });
    await client.detach();
    return page;
  }, async close() { await page.close(); } };
}
async function start(page, { paper = "rpsc-programmer-2024-paper-1", minutes = "0", count, mode = "exam" } = {}) {
  await page.select("#paperSelect", paper);
  if (count) await page.$eval("#paperCount", (node, value) => { node.value = value; }, count);
  await page.$eval("#paperMinutes", (node, value) => { node.value = value; }, minutes);
  await page.select("#paperMode", mode);
  await page.click("#startPaperButton");
  await page.waitForSelector("#paperPlayer:not([hidden])");
}

(async () => {
  fs.mkdirSync(SHOTS, { recursive: true });
  const browser = await puppeteer.launch({ executablePath: await chromium.executablePath(), args: chromium.args, headless: true });
  try {
    for (const width of [360, 390, 768, 951, 1280]) {
      console.log(`CHECK paper room ${width}px`);
      const context = await isolatedContext(browser); const page = await context.newPage();
      await page.setViewport({ width, height: 900, isMobile: width < 800, hasTouch: width < 800 });
      const pageErrors = errors(page);
      await page.goto(BASE + "subjects/test-room/index.html"); await ready(page); await noOverflow(page); await sleep(600);
      if ([360, 1280].includes(width)) await page.screenshot({ path: path.join(SHOTS, `room-${width}.png`), fullPage: true });
      await start(page);
      try {
        await page.waitForFunction(() => document.getElementById("roomCanvas").width > 200 && /ready/.test(document.getElementById("roomPdfStatus").textContent), { timeout: 30000 });
      } catch (error) {
        console.error("Reader failure:", await page.$eval("#roomPdfStatus", (e) => e.textContent), pageErrors); throw error;
      }
      assert.match(await page.$eval("#roomPageCount", (e) => e.textContent), /24/);
      await page.click('#roomOptions input[value="C"]');
      await page.click("#roomMark"); await page.click("#roomNext");
      await page.click('#roomOptions input[value="D"]'); await page.click("#roomClear");
      assert.equal(await page.$$eval("#roomOptions input:checked", (es) => es.length), 0);
      await page.click("#roomPalette button:first-child");
      assert.equal(await page.$eval("#roomOptions input:checked", (e) => e.value), "C");
      assert.equal(await page.$eval("#roomCheck", (e) => e.hidden), true, "exam must hide key checking");
      assert.equal(await page.$eval("#roomFeedback", (e) => e.hidden), true);
      const draft = await page.evaluate(() => JSON.parse(localStorage.getItem("ekguru.paper.draft.v1")));
      await page.click("#pausePaperButton"); await page.reload(); await ready(page);
      await page.waitForSelector("#draftNotice:not([hidden])"); await page.$eval("#legacyPaperTools", (node) => { node.open = true; }); await page.click("#resumePaperButton");
      await page.waitForSelector("#paperPlayer:not([hidden])");
      const restored = await page.evaluate(() => JSON.parse(localStorage.getItem("ekguru.paper.draft.v1")));
      assert.equal(restored.id, draft.id); assert.equal(restored.started_at, draft.started_at);
      assert.equal(await page.$eval("#roomOptions input:checked", (e) => e.value), "C");
      assert.equal(await page.$eval("#roomMark", (e) => e.getAttribute("aria-pressed")), "true");
      page.once("dialog", (dialog) => dialog.dismiss()); await page.click("#submitPaperButton");
      assert.equal(await page.$eval("#paperResult", (e) => e.hidden), true, "cancel submit keeps test");
      await clickSubmit(page);
      assert.match(await page.$eval("#paperResultStats", (e) => e.textContent), /1 \/ 98/);
      assert.equal(await page.$$eval("#paperReview .review-line", (es) => es.length), 100);
      assert.equal(await page.evaluate(() => localStorage.getItem("ekguru.paper.draft.v1")), null);
      await noOverflow(page); assert.deepEqual(pageErrors, []);
      await context.close(); console.log(`PASS paper room ${width}px: PDF, OMR, marks, clear, draft/resume, cancel/submit, review`);
    }
    {
      const context = await isolatedContext(browser); const page = await context.newPage(); const pageErrors = errors(page);
      await page.setViewport({ width: 390, height: 844, isMobile: true });
      await page.goto(BASE + "subjects/test-room/index.html"); await ready(page);
      await start(page, { paper: "bci-2022-paper-1", count: "3", mode: "practice" });
      await page.click('#roomOptions input[value="B"]'); await page.click("#roomCheck");
      assert.match(await page.$eval("#roomFeedback", (e) => e.textContent), /score nahi hoga/);
      await clickSubmit(page); assert.match(await page.$eval("#paperResultStats", (e) => e.textContent), /Unscored/);
      const last = await page.evaluate(() => JSON.parse(localStorage.getItem("ekguru.paper.last.v1")));
      assert.equal(last.score, null); assert.equal(last.correct, null); assert.equal(last.unanswered, 2);
      await page.click("#newPaperButton"); await start(page, { minutes: "1" });
      await page.click("#pausePaperButton");
      await page.evaluate(() => { const key = "ekguru.paper.draft.v1", d = JSON.parse(localStorage.getItem(key)); d.started_at = Date.now() - 120000; d.deadline = Date.now() + 999999999; localStorage.setItem(key, JSON.stringify(d)); });
      await page.reload(); await ready(page); await page.$eval("#legacyPaperTools", (node) => { node.open = true; }); await page.click("#resumePaperButton"); await page.waitForSelector("#paperResult:not([hidden])");
      assert.match(await page.$eval("#paperResultLabel", (e) => e.textContent), /time up, auto-submitted/);
      const timed = await page.evaluate(() => JSON.parse(localStorage.getItem("ekguru.paper.last.v1")));
      assert.equal(timed.duration_seconds, 60);
      assert.deepEqual(pageErrors, []); await context.close();
      console.log("PASS unkeyed scanned paper, practice feedback, wall-clock resume expiry/auto-submit");
    }
    {
      const context = await isolatedContext(browser); const page = await context.newPage(); const pageErrors = errors(page);
      let mode = "fail";
      await page.setCacheEnabled(false); await page.setRequestInterception(true);
      page.on("request", (request) => {
        if (/\.pdf$/i.test(new URL(request.url()).pathname)) {
          if (mode === "fail") return request.abort("failed");
          if (mode === "delay") return setTimeout(() => request.continue().catch(() => {}), 1300);
        }
        request.continue();
      });
      await page.goto(BASE + "subjects/test-room/index.html"); await ready(page); await start(page);
      await page.waitForSelector("#retryPaperPdf:not([hidden])");
      await page.click('#roomOptions input[value="A"]');
      assert.equal(await page.$eval('#roomOptions input:checked', (e) => e.value), "A", "OMR works even if PDF fails");
      mode = "normal"; await page.click("#retryPaperPdf");
      try {
        await page.waitForFunction(() => /Page 1 ready/.test(document.getElementById("roomPdfStatus").textContent), { timeout: 30000 });
      } catch (error) { console.error("Retry/cancel PDF status:", await page.$eval("#roomPdfStatus", (e) => e.textContent), pageErrors); throw error; }
      await page.click("#roomPageNext"); await page.click("#roomZoomIn"); await page.click("#roomZoomIn");
      await page.waitForFunction(() => /Page 2 ready/.test(document.getElementById("roomPdfStatus").textContent), { timeout: 30000 });
      assert(await page.$eval("#roomCanvas", (e) => e.width * e.height <= 6000000), "PDF canvas memory is bounded");
      await page.click("#pausePaperButton");
      mode = "delay"; await page.$eval("#legacyPaperTools", (node) => { node.open = true; }); await page.click("#resumePaperButton"); await sleep(100);
      await page.click("#roomNext"); await page.click("#pausePaperButton");
      await page.waitForSelector("#paperPlayer[hidden]");
      mode = "normal"; page.once("dialog", (dialog) => dialog.accept());
      await start(page, { paper: "bci-2022-paper-1", count: "3" });
      try {
        await page.waitForFunction(() => /Page 1 ready/.test(document.getElementById("roomPdfStatus").textContent), { timeout: 30000 });
      } catch (error) { console.error("Retry/cancel PDF status:", await page.$eval("#roomPdfStatus", (e) => e.textContent), pageErrors); throw error; }
      assert.match(await page.$eval("#roomPageCount", (e) => e.textContent), /8/);
      await sleep(1500);
      // PDF.js may report its own worker teardown after our intentional network
      // abort. Only these specific fault-injection notices are expected; normal
      // room/account checks above/below still require zero page errors.
      const expectedCancellation = /^(?:Worker was terminated\.?|Failed to fetch\nnew PDFFetchStreamReader \([^\n]+\))$/;
      assert.deepEqual(pageErrors.filter((text) => !expectedCancellation.test(text)), []);
      await context.close();
      console.log("PASS PDF failure/retry, delayed network keeps OMR responsive, cancellation/new paper and bounded zoom canvas");
    }
    {
      const context = await isolatedContext(browser); const page = await context.newPage(); const pageErrors = errors(page);
      await page.goto(BASE + "subjects/computer-network/test/index.html?mode=full&count=50&pattern=exam&minutes=60");
      await page.waitForFunction(() => !document.getElementById("startButton").disabled);
      assert.equal(await page.$eval("#modeFull", (e) => e.getAttribute("aria-pressed")), "true");
      assert.equal(await page.$eval("#countSelect", (e) => e.value), "50");
      assert.equal(await page.$eval("#minutesSelect", (e) => e.value), "60");
      await page.click("#startButton"); await page.waitForSelector("#playerPanel:not([hidden])");
      assert.match(await page.$eval("#questionNumber", (e) => e.textContent), /1 of 50/);
      assert.equal(await page.$eval("#feedback", (e) => e.hidden), true);
      assert.deepEqual(pageErrors, []); await context.close(); console.log("PASS CN quick-test presets use the existing real bank and CBT engine");
    }
    {
      const context = await isolatedContext(browser); const page = await context.newPage(); const pageErrors = errors(page);
      await page.setViewport({ width: 390, height: 844, isMobile: true });
      let signedIn = true, offline = true; const posted = [], authRequests = [];
      await page.setRequestInterception(true);
      page.on("request", (request) => {
        const url = new URL(request.url());
        if (url.pathname === "/api/auth/session") return request.respond({ status: 200, contentType: "application/json", body: JSON.stringify({ configured: true, google_enabled: true,
          user: signedIn ? { id: UID, name: "Student <script>not HTML</script>", email: "student@example.test" } : null }) });
        if (url.pathname === "/api/auth/logout") { signedIn = false; return request.respond({ status: 200, contentType: "application/json", body: '{"ok":true}' }); }
        if (url.pathname === "/api/attempts") {
          authRequests.push(request.headers()["x-ekguru-user"]);
          if (request.method() === "POST") {
            posted.push(JSON.parse(request.postData()));
            return request.respond({ status: offline ? 503 : 201, contentType: "application/json", body: offline ? '{"error":"service_unavailable"}' : '{"ok":true}' });
          }
          return request.respond({ status: 200, contentType: "application/json", body: JSON.stringify({ attempts: [{ id: "ec7b6860-83fa-4f1c-ae42-7d17a9c05a1e", label: "<script>no execution</script> & practice", total: 3,
            duration_seconds: 40, created_at: "2026-10-17T00:00:00Z", score: null, correct: null, wrong: null, max_score: null, unanswered: 2 }] }) });
        }
        request.continue();
      });
      await page.goto(BASE + "subjects/test-room/index.html"); await ready(page);
      await page.waitForFunction(() => window.EkGuruAccount?.user?.id);
      await start(page, { paper: "bci-2022-paper-2", count: "3" });
      await page.click('#roomOptions input[value="A"]'); await clickSubmit(page);
      await page.waitForFunction(() => document.querySelector("[data-cloud-status]").textContent.includes("Sync pending"));
      assert.equal(posted.length, 1); assert.equal(posted[0].user_id, undefined);
      offline = false; await page.evaluate(() => dispatchEvent(new Event("online")));
      await page.waitForFunction(() => document.querySelector("[data-cloud-status]").textContent.includes("sync ho gaya"));
      assert.equal(posted.length, 2); assert.equal(posted[0].id, posted[1].id, "offline retries keep idempotency key");
      await page.goto(BASE + "subjects/account/index.html");
      await page.waitForSelector("#accountHistory .history-row");
      assert.match(await page.$eval("[data-account-name]", (e) => e.textContent), /<script>/);
      assert.equal(await page.$$eval("#accountHistory script", (es) => es.length), 0);
      assert.ok(authRequests.every((id) => id === UID), "every history request is account-bound");
      assert.equal(await page.evaluate(() => /access_token|refresh_token/.test(JSON.stringify(localStorage))), false);
      await noOverflow(page);
      await sleep(600); await page.screenshot({ path: path.join(SHOTS, "account-390.png"), fullPage: true });
      await page.click("[data-account-logout]"); await page.waitForFunction(() => window.EkGuruAccount.user === null);
      assert.equal(await page.$$eval("#accountHistory .history-row", (es) => es.length), 0);
      assert.deepEqual(pageErrors, []); await context.close();
      console.log("PASS mocked Google-account UI, safe text, private owner header, offline retry, logout (not live OAuth)");
    }
    {
      const context = await isolatedContext(browser); const page = await context.newPage(); let posted = 0;
      await page.evaluateOnNewDocument(() => { Storage.prototype.setItem = () => { throw new DOMException("Storage disabled", "QuotaExceededError"); }; });
      await page.setRequestInterception(true);
      page.on("request", (r) => {
        const p = new URL(r.url()).pathname;
        if (p === "/api/auth/session") return r.respond({ status: 200, contentType: "application/json", body: JSON.stringify({ configured: true, google_enabled: true, user: { id: UID, name: "Student", email: "student@example.test" } }) });
        if (p === "/api/attempts") { if (r.method() === "POST") posted++; return r.respond({ status: 200, contentType: "application/json", body: r.method() === "POST" ? '{"ok":true}' : '{"attempts":[]}' }); }
        r.continue();
      });
      await page.goto(BASE + "subjects/test-room/index.html"); await ready(page); await page.waitForFunction(() => window.EkGuruAccount?.user);
      await start(page, { paper: "bci-2022-paper-1", count: "2" }); await page.click('#roomOptions input[value="A"]');
      assert.match(await page.$eval("#draftSaveStatus", (e) => e.textContent), /storage unavailable/);
      await clickSubmit(page); await sleep(300);
      assert.equal(posted, 1, "memory outbox must still send while localStorage is unavailable");
      await context.close(); console.log("PASS storage-disabled browser still grades, exports and syncs from memory");
    }
    {
      const context = await isolatedContext(browser); const page = await context.newPage(); let apiCalls = 0;
      await page.setRequestInterception(true);
      page.on("request", (r) => {
        if (r.url().includes("/data/runtime.json")) return r.respond({ status: 200, contentType: "application/json", body: '{"schema_version":1,"auth_origin":"https://ekguru-questions.vercel.app"}' });
        if (new URL(r.url()).pathname.startsWith("/api/")) apiCalls++;
        r.continue();
      });
      await page.goto(BASE + "subjects/account/index.html");
      await page.waitForFunction(() => window.EkGuruAccount?.remote);
      assert.equal(apiCalls, 0, "static GitHub Pages must not try unavailable /api endpoints");
      assert.match(await page.$eval("[data-account-login]", (e) => e.href), /^https:\/\/ekguru-questions\.vercel\.app\/api\/auth\/login/);
      await context.close(); console.log("PASS GitHub Pages guest mode links to same-site secure Vercel login; no cross-site token storage");
    }
    console.log("PASS all Test Room/account browser regressions; screenshots in .cache/browser-shots/ (not committed)");
  } finally { await browser.close(); }
})().catch((error) => { console.error(error); process.exit(1); });
