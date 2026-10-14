#!/usr/bin/env node
/* Optional, rendered browser QA. Requires temporary Playwright, Chromium and axe-core packages. */
const assert = require("node:assert/strict");
const crypto = require("node:crypto");
const fs = require("node:fs");
const http = require("node:http");
const path = require("node:path");
const ROOT = path.resolve(__dirname, "../..");
const REPORT_PATH = path.join(ROOT, "data/reports/browser_visual_qa.json");
const SCREENSHOT_DIR = path.join(ROOT, ".arena/browser-qa/screenshots");
const VIEWPORTS = [
  { name: "phone-320", width: 320, height: 780 },
  { name: "phone-375", width: 375, height: 812 },
  { name: "tablet-768", width: 768, height: 1024 },
  { name: "laptop-1365", width: 1365, height: 900 },
];

let playwrightChromium;
let chromiumPackage;
let axePath;
try {
  ({ chromium: playwrightChromium } = require("playwright-core"));
  chromiumPackage = require("@sparticuz/chromium");
  axePath = require.resolve("axe-core/axe.min.js");
} catch (error) {
  console.log(`SKIP: rendered browser QA packages are unavailable (${error.code || error.message}).`);
  process.exit(77);
}
const chromium = chromiumPackage.default;

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".mjs": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
};

function uiFingerprint() {
  const hash = crypto.createHash("sha256");
  for (const relative of ["index.html", "assets/css/portal.css", "assets/js/app.mjs", "assets/js/engine.mjs"]) {
    hash.update(relative).update("\0").update(fs.readFileSync(path.join(ROOT, relative))).update("\0");
  }
  return hash.digest("hex");
}

function startStaticServer() {
  const server = http.createServer((request, response) => {
    let pathname;
    try {
      pathname = decodeURIComponent(new URL(request.url, "http://qa.local").pathname);
    } catch {
      response.writeHead(400).end("Bad request");
      return;
    }
    if (pathname === "/") pathname = "/index.html";
    const file = path.resolve(ROOT, `.${pathname}`);
    if (file !== ROOT && !file.startsWith(ROOT + path.sep)) {
      response.writeHead(403).end("Forbidden");
      return;
    }
    fs.readFile(file, (error, contents) => {
      if (error) {
        response.writeHead(error.code === "ENOENT" ? 404 : 500).end("Not found");
        return;
      }
      response.writeHead(200, {
        "Content-Type": MIME[path.extname(file).toLowerCase()] || "application/octet-stream",
        "Cache-Control": "no-store",
        "X-Content-Type-Options": "nosniff",
      }).end(contents);
    });
  });
  return new Promise((resolve, reject) => {
    server.once("error", reject);
    server.listen(0, "127.0.0.1", () => {
      server.removeListener("error", reject);
      const address = server.address();
      resolve({ server, baseURL: `http://127.0.0.1:${address.port}/` });
    });
  });
}

function axeSummary(result) {
  return result.violations.map((violation) => ({
    id: violation.id,
    impact: violation.impact,
    help: violation.help,
    node_count: violation.nodes.length,
    targets: [...new Set(violation.nodes.flatMap((node) => node.target.slice(0, 2)))].slice(0, 8),
  }));
}

async function axeRun(page) {
  return page.evaluate(async () => await window.axe.run(document, {
    runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "best-practice"] },
  }));
}

async function main() {
  const manifest = JSON.parse(fs.readFileSync(path.join(ROOT, "data/reports/build_manifest.json"), "utf8"));
  const { server, baseURL } = await startStaticServer();
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
  const results = {
    schema_version: 1,
    status: "RUNNING",
    checked_at_utc: new Date().toISOString(),
    bank_build_id: manifest.bank_build_id,
    canonical_sha256: manifest.canonical_sha256,
    ui_sha256: uiFingerprint(),
    browser: null,
    viewports: [],
    browser_errors: [],
    total_axe_violations: null,
  };
  let browser;
  let failure = null;
  try {
    const packageRoot = path.dirname(require.resolve("@sparticuz/chromium"));
    const al2023Lib = await chromiumPackage.inflate(path.join(packageRoot, "../bin/al2023.tar.br"));
    chromiumPackage.setupLambdaEnvironment(path.join(al2023Lib, "lib"));
    const executablePath = await chromium.executablePath();
    browser = await playwrightChromium.launch({ executablePath, args: chromium.args, headless: true });
    results.browser = `Chromium ${await browser.version()} (headless)`;

    for (const viewport of VIEWPORTS) {
      const context = await browser.newContext({ viewport: { width: viewport.width, height: viewport.height }, deviceScaleFactor: 1 });
      const page = await context.newPage();
      const localErrors = [];
      page.on("pageerror", (error) => localErrors.push(`pageerror: ${error.message}`));
      page.on("console", (message) => { if (message.type() === "error") localErrors.push(`console: ${message.text()}`); });
      page.on("response", (response) => {
        if (response.status() >= 400 && !response.url().endsWith("/favicon.ico")) localErrors.push(`HTTP ${response.status()} ${response.url()}`);
      });

      const response = await page.goto(baseURL, { waitUntil: "networkidle", timeout: 30000 });
      assert.equal(response.status(), 200, `${viewport.name}: root page should load`);
      await page.waitForFunction(() => document.querySelector("#totalQuestions")?.textContent?.trim() === "1,556", null, { timeout: 15000 });
      await page.waitForFunction(() => document.querySelector("#poolStatus")?.textContent?.includes("847"), null, { timeout: 15000 });
      assert.equal(await page.locator("#officialCount").textContent(), "0");

      const landing = await page.evaluate(() => ({
        inner_width: innerWidth,
        document_width: document.documentElement.scrollWidth,
        body_width: document.body.scrollWidth,
        page_height: document.documentElement.scrollHeight,
        nav_toggle_display: getComputedStyle(document.querySelector("#navToggle")).display,
        nav_display: getComputedStyle(document.querySelector("#siteNav")).display,
      }));
      assert.ok(landing.document_width <= viewport.width, `${viewport.name}: landing overflow ${landing.document_width}/${viewport.width}px`);
      assert.ok(landing.body_width <= viewport.width, `${viewport.name}: body overflow ${landing.body_width}/${viewport.width}px`);

      let mobile_menu_tested = false;
      if (viewport.width <= 900) {
        const toggle = page.locator("#navToggle");
        assert.ok(await toggle.isVisible(), `${viewport.name}: menu button should be visible`);
        await toggle.click();
        assert.equal(await toggle.getAttribute("aria-expanded"), "true");
        assert.ok(await page.locator("#siteNav").isVisible());
        assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `${viewport.name}: open menu overflow`);
        await page.screenshot({ path: path.join(SCREENSHOT_DIR, `${viewport.name}-menu.png`) });
        await page.locator('#siteNav a[href="#practice"]').first().click();
        assert.equal(await toggle.getAttribute("aria-expanded"), "false");
        mobile_menu_tested = true;
      } else {
        assert.equal(await page.locator("#navToggle").evaluate((element) => getComputedStyle(element).display), "none");
      }

      await page.screenshot({ path: path.join(SCREENSHOT_DIR, `${viewport.name}-landing.png`), fullPage: false });
      await page.screenshot({ path: path.join(SCREENSHOT_DIR, `${viewport.name}-landing-full.png`), fullPage: true });
      await page.addScriptTag({ path: axePath });
      const landingAxe = await axeRun(page);

      await page.locator("#verificationSelect").selectOption("paper_and_key_checked");
      assert.equal(await page.locator("#startButton").isDisabled(), true, `${viewport.name}: verified mode must be disabled without evidence`);
      await page.locator("#verificationSelect").selectOption("claimed_answer_unverified");
      assert.equal(await page.locator("#startButton").isDisabled(), false, `${viewport.name}: explicit unverified opt-in should be available`);
      await page.locator("#verificationSelect").selectOption("reviewed_answers");
      assert.equal(await page.locator("#startButton").isDisabled(), false, `${viewport.name}: answer-checked pool should be available`);

      await page.locator("#topicSelect").selectOption("T01");
      await page.locator("#questionCountSelect").selectOption("10");
      await page.locator("#startButton").click();
      await page.locator("#playerPanel:not([hidden])").waitFor({ timeout: 15000 });
      await page.waitForFunction(() => document.querySelector("#questionStem")?.textContent?.trim().length > 0, null, { timeout: 15000 });
      await page.evaluate(() => document.querySelector("#playerPanel").scrollIntoView({ behavior: "instant", block: "start" }));
      await page.waitForFunction(() => {
        const panel = document.querySelector("#playerPanel").getBoundingClientRect();
        const scrollPadding = parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop) || 0;
        return Math.abs(panel.top - scrollPadding) < 2;
      }, null, { timeout: 5000 });
      assert.equal(await page.locator("#optionList button").count(), 4);
      const quiz = await page.evaluate(() => ({
        inner_width: innerWidth,
        document_width: document.documentElement.scrollWidth,
        body_width: document.body.scrollWidth,
        panel_width: document.querySelector("#playerPanel").scrollWidth,
        panel_client_width: document.querySelector("#playerPanel").clientWidth,
        stem_height: Math.round(document.querySelector("#questionStem").getBoundingClientRect().height),
        options_width: document.querySelector("#optionList").scrollWidth,
        options_client_width: document.querySelector("#optionList").clientWidth,
      }));
      assert.ok(quiz.document_width <= viewport.width, `${viewport.name}: quiz overflow ${quiz.document_width}/${viewport.width}px`);
      assert.ok(quiz.body_width <= viewport.width, `${viewport.name}: quiz body overflow ${quiz.body_width}/${viewport.width}px`);
      assert.ok(quiz.options_width <= quiz.options_client_width + 1, `${viewport.name}: answer options overflow`);
      await page.screenshot({ path: path.join(SCREENSHOT_DIR, `${viewport.name}-quiz.png`), fullPage: false });

      const visibleControls = await page.locator("button:visible, a.button:visible, select:visible, input:visible").evaluateAll((elements) => elements.map((element) => ({
        name: element.getAttribute("aria-label") || element.textContent.trim().replace(/\s+/g, " ").slice(0, 60) || element.id,
        height: Math.round(element.getBoundingClientRect().height),
        tag: element.tagName.toLowerCase(),
      })));
      const shortControls = visibleControls.filter((control) => control.height < 44);
      assert.equal(shortControls.length, 0, `${viewport.name}: controls below 44px: ${JSON.stringify(shortControls)}`);

      await page.locator("#sourceDetailsButton").click();
      await page.locator("#sourceDialog[open]").waitFor({ timeout: 10000 });
      const dialog = await page.locator("#sourceDialog").evaluate((element) => ({ width: Math.round(element.getBoundingClientRect().width), viewport: innerWidth }));
      assert.ok(dialog.width <= viewport.width, `${viewport.name}: source dialog exceeds viewport`);
      const dialogAxe = await axeRun(page);
      await page.screenshot({ path: path.join(SCREENSHOT_DIR, `${viewport.name}-source-dialog.png`) });
      await page.locator("#closeSourceDialog").click();
      const quizAxe = await axeRun(page);

      results.viewports.push({
        ...viewport,
        landing,
        quiz,
        dialog,
        mobile_menu_tested: mobile_menu_tested,
        minimum_control_height_px: visibleControls.length ? Math.min(...visibleControls.map((control) => control.height)) : null,
        controls_under_44px: shortControls.length,
        axe: {
          landing_violations: axeSummary(landingAxe),
          quiz_violations: axeSummary(quizAxe),
          source_dialog_violations: axeSummary(dialogAxe),
          landing_incomplete_checks: landingAxe.incomplete.length,
          quiz_incomplete_checks: quizAxe.incomplete.length,
          source_dialog_incomplete_checks: dialogAxe.incomplete.length,
        },
      });
      results.browser_errors.push(...localErrors.map((error) => `${viewport.name}: ${error}`));
      console.log(`${viewport.name}: widths=${landing.document_width}/${quiz.document_width}px; axe=${landingAxe.violations.length}/${quizAxe.violations.length}/${dialogAxe.violations.length}; <44px=${shortControls.length}; runtime/network errors=${localErrors.length}`);
      // Keep contexts alive until browser shutdown: single-process Chromium exits if contexts close early.
    }

    results.total_axe_violations = results.viewports.reduce((total, viewport) => total
      + viewport.axe.landing_violations.length
      + viewport.axe.quiz_violations.length
      + viewport.axe.source_dialog_violations.length, 0);
    results.status = results.total_axe_violations === 0 && results.browser_errors.length === 0 ? "PASS" : "FAIL";
  } catch (error) {
    failure = error;
    results.status = "FAIL";
    results.failure = error.message;
  } finally {
    if (browser) await browser.close().catch(() => {});
    await new Promise((resolve) => server.close(resolve));
    fs.mkdirSync(path.dirname(REPORT_PATH), { recursive: true });
    fs.writeFileSync(REPORT_PATH, JSON.stringify(results, null, 2) + "\n");
  }

  console.log(`${results.status}: rendered viewports=${results.viewports.length}, axe violations=${results.total_axe_violations ?? "incomplete"}, browser/network errors=${results.browser_errors.length}; report=${path.relative(ROOT, REPORT_PATH)}`);
  if (failure || results.status !== "PASS") process.exitCode = 1;
}

main().catch((error) => {
  console.error(error.stack || error);
  process.exitCode = 1;
});
