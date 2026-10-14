#!/usr/bin/env node
/* Optional rendered QA for the subject portal and shared practice app.
 * Requires Playwright Core, @sparticuz/chromium, and axe-core to be installed temporarily.
 */
const assert = require("node:assert/strict");
const crypto = require("node:crypto");
const fs = require("node:fs");
const http = require("node:http");
const path = require("node:path");

const ROOT = path.resolve(__dirname, "../..");
const BASE_PATH = "/Questions-/";
const REPORT_PATH = path.join(ROOT, "data/reports/portal_browser_visual_qa.json");
const SCREENSHOT_DIR = path.join(ROOT, ".arena/portal-browser-qa/screenshots");
const VIEWPORTS = [
  { name: "phone-320", width: 320, height: 780 },
  { name: "phone-360", width: 360, height: 800 },
  { name: "phone-390", width: 390, height: 844 },
  { name: "phone-430", width: 430, height: 932 },
  { name: "small-mobile-520", width: 520, height: 844 },
  { name: "zoom-200-css-640", width: 640, height: 900 },
  { name: "tablet-720", width: 720, height: 960 },
  { name: "tablet-768", width: 768, height: 1024 },
  { name: "tablet-950", width: 950, height: 900 },
  { name: "laptop-1024", width: 1024, height: 768 },
  { name: "laptop-1280", width: 1280, height: 800 },
  { name: "desktop-1440", width: 1440, height: 900 },
  { name: "desktop-1920", width: 1920, height: 1080 },
  { name: "phone-landscape", width: 844, height: 390 },
  { name: "tablet-landscape", width: 1180, height: 820 },
];
const ROUTES = [
  { id: "home", path: "", title: "EkGuru Learning", ready: "#catalogStatus" },
  { id: "subjects", path: "subjects/index.html", title: "All Subjects", ready: "#catalogStatus" },
  { id: "computer-network", path: "subjects/computer-network/index.html", title: "Computer Network", ready: "#cnCatalogStatus" },
  { id: "rajasthan-geography", path: "subjects/rajasthan-geography/index.html", title: "Rajasthan Geography", ready: "#geographyCatalogStatus" },
  { id: "maps", path: "maps/index.html", title: "Maps & Atlases", ready: "#mapCatalogStatus" },
  { id: "map-detail", path: "maps/rajasthan/index.html", title: "Rajasthan Map & Atlas Resources", ready: "#mapReviewStatus" },
  { id: "practice", path: "practice/index.html?subject=cn&topic=T01&mode=practice#practice", title: "Computer Network Practice", ready: "#totalQuestions" },
  { id: "study-material", path: "study-material/index.html", title: "Study Material", ready: "#studyCatalogStatus" },
  { id: "sources", path: "sources/index.html", title: "Sources & Verification", ready: "#sourcesCatalogStatus" },
  { id: "repository-guide", path: "guides/repository-structure/index.html", title: "Repository & Website File Guide", ready: "#guideTitle" },
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
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".csv": "text/csv; charset=utf-8",
  ".md": "text/markdown; charset=utf-8",
  ".txt": "text/plain; charset=utf-8",
  ".woff": "font/woff",
  ".woff2": "font/woff2",
};

function uiFingerprint() {
  const hash = crypto.createHash("sha256");
  const files = [
    "index.html",
    "subjects/index.html",
    "subjects/computer-network/index.html",
    "subjects/rajasthan-geography/index.html",
    "maps/index.html",
    "maps/rajasthan/index.html",
    "practice/index.html",
    "study-material/index.html",
    "sources/index.html",
    "guides/repository-structure/index.html",
    "assets/css/site.css",
    "assets/css/portal.css",
    "assets/js/app.js",
    "assets/js/app.mjs",
    "assets/js/engine.mjs",
  ];
  for (const relative of files) {
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
    if (pathname === BASE_PATH) pathname = `${BASE_PATH}index.html`;
    if (!pathname.startsWith(BASE_PATH)) {
      response.writeHead(404).end("Not found");
      return;
    }
    const relative = pathname.slice(BASE_PATH.length) || "index.html";
    const file = path.resolve(ROOT, relative);
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
      resolve({ server, baseURL: `http://127.0.0.1:${address.port}${BASE_PATH}` });
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
    sample_failures: violation.nodes.slice(0, 2).map((node) => ({ target: node.target, failure_summary: node.failureSummary })),
  }));
}

function axeIncompleteSummary(result) {
  return result.map((check) => ({
    id: check.id,
    impact: check.impact,
    help: check.help,
    node_count: check.nodes.length,
    targets: [...new Set(check.nodes.flatMap((node) => node.target.slice(0, 2)))].slice(0, 8),
    sample_checks: check.nodes.slice(0, 2).map((node) => ({
      target: node.target,
      checks: [...node.any, ...node.all, ...node.none].map((item) => ({ id: item.id, message: item.message })),
    })),
  }));
}

async function axeRun(page) {
  return page.evaluate(async () => await window.axe.run(document, {
    runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "best-practice"] },
  }));
}

async function waitForRouteReady(page, route) {
  await page.waitForSelector(route.ready, { state: "attached", timeout: 15000 });
  if (route.id === "home" || route.id === "subjects") {
    await page.waitForFunction(() => document.querySelector("#catalogStatus")?.textContent?.includes("catalog loaded"), null, { timeout: 15000 });
  } else if (route.id === "computer-network") {
    await page.waitForFunction(() => document.querySelector("#cnCatalogStatus")?.textContent?.includes("validated") && document.querySelectorAll("#topicCards > article").length === 7, null, { timeout: 15000 });
  } else if (route.id === "rajasthan-geography") {
    await page.waitForFunction(() => document.querySelector("#geographyCatalogStatus")?.textContent?.includes("loaded") && document.querySelectorAll("#boundarySummary tbody tr").length === 7, null, { timeout: 15000 });
  } else if (route.id === "maps") {
    await page.waitForFunction(() => document.querySelector("#mapCatalogStatus")?.textContent?.includes("loaded") && document.querySelectorAll("#mapGrid > article").length === 2, null, { timeout: 15000 });
  } else if (route.id === "map-detail") {
    await page.waitForFunction(() => document.querySelector("#mapReviewStatus")?.textContent?.toLowerCase().includes("verification") && document.querySelectorAll("#boundarySummary tbody tr").length === 7, null, { timeout: 15000 });
  } else if (route.id === "practice") {
    await page.waitForFunction(() => document.querySelector("#totalQuestions")?.textContent?.trim() === "1,556", null, { timeout: 15000 });
  } else if (route.id === "study-material") {
    await page.waitForFunction(() => document.querySelector("#studyCatalogStatus")?.textContent?.includes("loaded") && document.querySelectorAll("[data-resource-list] .resource-item").length > 0, null, { timeout: 15000 });
  } else if (route.id === "sources") {
    await page.waitForFunction(() => document.querySelector("#sourcesCatalogStatus")?.textContent?.includes("loaded") && document.querySelectorAll("#officialSourceLinks a[target='_blank']").length === 3, null, { timeout: 15000 });
  }
}

async function inspectLayout(page, viewport, route) {
  const measurements = await page.evaluate(() => {
    const images = [...document.images].map((image) => {
      const box = image.getBoundingClientRect();
      return {
        alt: image.getAttribute("alt") || "",
        natural_width: image.naturalWidth,
        left: Math.round(box.left),
        right: Math.round(box.right),
        width: Math.round(box.width),
      };
    });
    return {
      viewport_width: innerWidth,
      document_width: document.documentElement.scrollWidth,
      body_width: document.body.scrollWidth,
      page_height: document.documentElement.scrollHeight,
      images,
      external_new_tabs: [...document.querySelectorAll('a[target="_blank"]')].map((anchor) => ({
        href: anchor.href,
        text: anchor.textContent.replace(/\s+/g, " ").trim(),
        rel: anchor.rel,
      })),
      controls: [...document.querySelectorAll("button, a.button, select, input, summary.site-menu-toggle")]
        .filter((element) => {
          const style = getComputedStyle(element);
          const rect = element.getBoundingClientRect();
          const visuallyHiddenChoice = element instanceof HTMLInputElement
            && ["checkbox", "radio"].includes(element.type)
            && rect.width <= 2 && rect.height <= 2;
          return !visuallyHiddenChoice && style.display !== "none" && style.visibility !== "hidden" && rect.width > 0 && rect.height > 0;
        })
        .map((element) => ({
          name: element.getAttribute("aria-label") || element.innerText?.replace(/\s+/g, " ").trim().slice(0, 50) || element.id,
          height: Math.round(element.getBoundingClientRect().height),
        })),
    };
  });
  assert.equal(measurements.viewport_width, viewport.width, `${viewport.name}/${route.id}: viewport width`);
  assert.ok(measurements.document_width <= viewport.width, `${viewport.name}/${route.id}: document overflow ${measurements.document_width}/${viewport.width}px`);
  assert.ok(measurements.body_width <= viewport.width, `${viewport.name}/${route.id}: body overflow ${measurements.body_width}/${viewport.width}px`);
  const badImages = measurements.images.filter((image) => image.right > viewport.width + 1 || image.left < -1 || !image.alt.trim());
  assert.deepEqual(badImages, [], `${viewport.name}/${route.id}: image overflow or missing alternative text`);
  const unsafeNewTabs = measurements.external_new_tabs.filter((anchor) => {
    const rel = new Set(anchor.rel.toLowerCase().split(/\s+/));
    return !rel.has("noopener") || !rel.has("noreferrer") || !/opens in new tab/i.test(anchor.text);
  });
  assert.deepEqual(unsafeNewTabs, [], `${viewport.name}/${route.id}: new-tab links need safe rel and visible labels`);
  const shortControls = measurements.controls.filter((control) => control.height < 44);
  assert.deepEqual(shortControls, [], `${viewport.name}/${route.id}: interactive controls below 44px: ${JSON.stringify(shortControls)}`);
  return measurements;
}

async function testNavigationFlows(page, baseURL, results) {
  const events = [];
  const response = await page.goto(baseURL, { waitUntil: "networkidle", timeout: 30000 });
  assert.equal(response.status(), 200);
  await waitForRouteReady(page, ROUTES.find((route) => route.id === "home"));

  await page.locator('#subjectGrid a[href*="subjects/computer-network/index.html"]').click();
  await page.waitForURL("**/subjects/computer-network/index.html", { timeout: 10000 });
  await waitForRouteReady(page, ROUTES.find((route) => route.id === "computer-network"));
  events.push("home → Computer Network");

  const startTopic = page.locator("#topicCards article").first().getByRole("link", { name: /Start topic CBT/ });
  const topicHref = await startTopic.getAttribute("href");
  assert.ok(topicHref.includes("/Questions-/practice/index.html?subject=cn&topic=T01"), `unexpected topic CBT URL: ${topicHref}`);
  await startTopic.click();
  await page.waitForURL("**/practice/index.html?subject=cn&topic=T01&mode=practice#practice", { timeout: 10000 });
  await waitForRouteReady(page, ROUTES.find((route) => route.id === "practice"));
  assert.equal(await page.locator("#topicSelect").inputValue(), "T01");
  events.push("Computer Network → topic CBT (same tab, topic preselected)");
  await page.goBack({ waitUntil: "networkidle" });
  assert.ok(new URL(page.url()).pathname.endsWith("/subjects/computer-network/index.html"));
  events.push("Back → Computer Network");

  await page.goto(baseURL, { waitUntil: "networkidle" });
  await page.locator('#subjectGrid a[href*="subjects/rajasthan-geography/index.html"]').click();
  await page.waitForURL("**/subjects/rajasthan-geography/index.html", { timeout: 10000 });
  await waitForRouteReady(page, ROUTES.find((route) => route.id === "rajasthan-geography"));
  events.push("home → Rajasthan Geography");
  const fullSize = page.locator("#fullSizeMapLink");
  assert.notEqual(await fullSize.getAttribute("target"), "_blank", "full-size map is intentionally same-tab so browser Back returns to the subject page");
  await fullSize.click();
  await page.waitForURL((url) => url.pathname.toLowerCase().endsWith(".png"), { timeout: 15000 });
  await page.locator("body").waitFor();
  const imageSize = await page.evaluate(() => ({
    count: document.images.length,
    natural_width: document.images[0]?.naturalWidth || 0,
    natural_height: document.images[0]?.naturalHeight || 0,
  }));
  assert.ok(imageSize.natural_width > 0 && imageSize.natural_height > 0, "full-size map PNG should render in the same tab");
  events.push("Rajasthan Geography → full-size PNG");
  await page.goBack({ waitUntil: "networkidle" });
  assert.ok(new URL(page.url()).pathname.endsWith("/subjects/rajasthan-geography/index.html"));
  events.push("Back → Rajasthan Geography");

  await page.goto(new URL("maps/index.html", baseURL).href, { waitUntil: "networkidle" });
  await waitForRouteReady(page, ROUTES.find((route) => route.id === "maps"));
  await page.locator('#mapGrid a[href*="/maps/rajasthan/index.html"]').first().click();
  await page.waitForURL("**/maps/rajasthan/index.html", { timeout: 10000 });
  await waitForRouteReady(page, ROUTES.find((route) => route.id === "map-detail"));
  events.push("Maps catalogue → map details");
  await page.goBack({ waitUntil: "networkidle" });
  assert.ok(new URL(page.url()).pathname.endsWith("/maps/index.html"));
  events.push("Back → maps catalogue");

  await page.goto(baseURL, { waitUntil: "networkidle" });
  await page.getByRole("link", { name: /Open the File Guide/ }).click();
  await page.waitForURL("**/guides/repository-structure/index.html", { timeout: 10000 });
  assert.ok(await page.getByRole("heading", { name: "Where should this file go?" }).isVisible());
  events.push("home → Repository File Guide (same tab)");
  await page.goBack({ waitUntil: "networkidle" });
  assert.equal(new URL(page.url()).pathname, BASE_PATH);
  events.push("Back → home catalogue");

  results.navigation_flows = events;
}

async function main() {
  const manifest = JSON.parse(fs.readFileSync(path.join(ROOT, "data/reports/build_manifest.json"), "utf8"));
  const { server, baseURL } = await startStaticServer();
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
  const results = {
    schema_version: 1,
    status: "RUNNING",
    checked_at_utc: new Date().toISOString(),
    project_base: BASE_PATH,
    bank_build_id: manifest.bank_build_id,
    canonical_sha256: manifest.canonical_sha256,
    ui_sha256: uiFingerprint(),
    browser: null,
    zoom_equivalence_note: "The 640 CSS-pixel viewport models a 200% reflow width on a 1280-pixel-wide baseline. Browser chrome/OS zoom controls were not automated.",
    viewports: [],
    navigation_flows: [],
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

    let activeErrors = [];
    let context;
    let page;
    for (const viewport of VIEWPORTS) {
      if (!page) {
        context = await browser.newContext({
          viewport: { width: viewport.width, height: viewport.height },
          deviceScaleFactor: 1,
          isMobile: true,
          hasTouch: true,
        });
        page = await context.newPage();
        page.on("pageerror", (error) => activeErrors.push(`pageerror: ${error.message}`));
        page.on("console", (message) => { if (message.type() === "error") activeErrors.push(`console: ${message.text()}`); });
        page.on("response", (response) => {
          if (response.status() >= 400 && !response.url().endsWith("/favicon.ico")) activeErrors.push(`HTTP ${response.status()} ${response.url()}`);
        });
      } else {
        await page.setViewportSize({ width: viewport.width, height: viewport.height });
      }
      const localErrors = [];
      activeErrors = localErrors;
      const routeResults = [];

      for (const route of ROUTES) {
        const routeURL = new URL(route.path, baseURL).href;
        const response = await page.goto(routeURL, { waitUntil: "networkidle", timeout: 30000 });
        assert.equal(response.status(), 200, `${viewport.name}/${route.id}: route should load`);
        await waitForRouteReady(page, route);
        assert.match(await page.title(), new RegExp(route.title.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "i"), `${viewport.name}/${route.id}: page title`);
        const measurements = await inspectLayout(page, viewport, route);

        if (route.id === "home") {
          assert.equal(await page.locator("#subjectGrid > article").count(), 2);
          if (viewport.name === "phone-320") {
            await page.keyboard.press("Tab");
            assert.equal(await page.evaluate(() => document.activeElement?.classList.contains("skip-link")), true, "first keyboard stop should be Skip to content");
            const menuSummary = page.locator(".site-menu > summary");
            await menuSummary.click();
            assert.equal(await page.locator(".site-menu").getAttribute("open"), "");
            assert.ok(await page.locator(".site-menu .site-nav").isVisible());
            assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), "open mobile menu should not overflow");
            await page.locator('.site-nav a[href="subjects/index.html"]').click();
            await page.waitForURL("**/subjects/index.html", { timeout: 10000 });
            assert.equal(await page.locator(".site-menu").getAttribute("open"), null, "menu should be closed on the destination route");
          }
          if (viewport.name === "phone-320" || viewport.name === "laptop-1280") {
            await page.addScriptTag({ path: axePath });
            const axe = await axeRun(page);
            results.accessibility ||= [];
            results.accessibility.push({ viewport: viewport.name, route: route.id, violations: axeSummary(axe), incomplete_checks: axe.incomplete.length, incomplete: axeIncompleteSummary(axe.incomplete) });
          }
          await page.screenshot({ path: path.join(SCREENSHOT_DIR, `${viewport.name}-home.png`), fullPage: false });
        }

        if (route.id === "computer-network") {
          assert.match(await page.locator("#cnBankStatus").innerText(), /1,556 records/);
          assert.equal(await page.locator("#topicCards > article").count(), 7);
          if (viewport.name === "phone-320" || viewport.name === "laptop-1280") {
            await page.addScriptTag({ path: axePath });
            const axe = await axeRun(page);
            results.accessibility ||= [];
            results.accessibility.push({ viewport: viewport.name, route: route.id, violations: axeSummary(axe), incomplete_checks: axe.incomplete.length, incomplete: axeIncompleteSummary(axe.incomplete) });
          }
          if (viewport.name === "phone-320") await page.screenshot({ path: path.join(SCREENSHOT_DIR, `${viewport.name}-computer-network.png`), fullPage: true });
        }

        if (route.id === "rajasthan-geography" || route.id === "map-detail") {
          assert.equal(await page.locator("#boundarySummary tbody tr").count(), 7);
          assert.match(await page.locator("#mapReviewStatus").innerText(), /verification/i);
          if (viewport.name === "phone-320" || viewport.name === "laptop-1280") {
            await page.addScriptTag({ path: axePath });
            const axe = await axeRun(page);
            results.accessibility ||= [];
            results.accessibility.push({ viewport: viewport.name, route: route.id, violations: axeSummary(axe), incomplete_checks: axe.incomplete.length, incomplete: axeIncompleteSummary(axe.incomplete) });
          }
          if (viewport.name === "phone-320") await page.screenshot({ path: path.join(SCREENSHOT_DIR, `${viewport.name}-${route.id}.png`), fullPage: true });
        }

        if (route.id === "maps") assert.equal(await page.locator("#mapGrid > article").count(), 2);
        if (route.id === "practice" && viewport.name === "phone-320") {
          assert.equal(await page.locator("#topicSelect").inputValue(), "T01");
          await page.locator("#questionCountSelect").selectOption("10");
          await page.locator("#startButton").click();
          await page.locator("#playerPanel:not([hidden])").waitFor({ timeout: 15000 });
          assert.equal(await page.locator("#optionList button").count(), 4);
          const quizMeasurements = await inspectLayout(page, viewport, route);
          assert.ok(quizMeasurements.document_width <= viewport.width, "practice quiz layout should fit the phone viewport");
          await page.addScriptTag({ path: axePath });
          const axe = await axeRun(page);
          results.accessibility ||= [];
          results.accessibility.push({ viewport: viewport.name, route: "practice-active-quiz", violations: axeSummary(axe), incomplete_checks: axe.incomplete.length, incomplete: axeIncompleteSummary(axe.incomplete) });
          await page.screenshot({ path: path.join(SCREENSHOT_DIR, `${viewport.name}-practice-quiz.png`), fullPage: false });
        }

        if (route.id === "sources" && viewport.name === "phone-320") {
          assert.equal(await page.locator("#officialSourceLinks a[target='_blank']").count(), 3);
          const safeExternalLinks = await page.locator("#officialSourceLinks a[target='_blank']").evaluateAll((links) => links.every((link) => /noopener/.test(link.rel) && /noreferrer/.test(link.rel) && /opens in new tab/i.test(link.parentElement.textContent)));
          assert.equal(safeExternalLinks, true, "official source links should be labelled and protected against opener access");
        }

        if (route.id === "repository-guide") {
          assert.ok(await page.getByRole("heading", { name: "Where should this file go?" }).isVisible());
          assert.ok((await page.locator("main").innerText()).includes("T07"));
          if (viewport.name === "phone-320" || viewport.name === "laptop-1280") {
            await page.addScriptTag({ path: axePath });
            const axe = await axeRun(page);
            results.accessibility ||= [];
            results.accessibility.push({ viewport: viewport.name, route: route.id, violations: axeSummary(axe), incomplete_checks: axe.incomplete.length, incomplete: axeIncompleteSummary(axe.incomplete) });
          }
          if (viewport.name === "phone-320") await page.screenshot({ path: path.join(SCREENSHOT_DIR, `${viewport.name}-repository-guide.png`), fullPage: true });
        }

        routeResults.push({ id: route.id, title: route.title, document_width: measurements.document_width, body_width: measurements.body_width, image_count: measurements.images.length });
      }

      results.viewports.push({ ...viewport, routes: routeResults });
      results.browser_errors.push(...localErrors.map((error) => `${viewport.name}: ${error}`));
      console.log(`${viewport.name}: routes=${routeResults.length}, max document width=${Math.max(...routeResults.map((route) => route.document_width))}/${viewport.width}px, browser/network errors=${localErrors.length}`);
    }

    await page.setViewportSize({ width: 390, height: 844 });
    const flowErrors = [];
    activeErrors = flowErrors;
    await testNavigationFlows(page, baseURL, results);
    results.browser_errors.push(...flowErrors.map((error) => `navigation flow: ${error}`));

    results.total_axe_violations = (results.accessibility || []).reduce((total, state) => total + state.violations.length, 0);
    results.status = results.total_axe_violations === 0 && results.browser_errors.length === 0 ? "PASS" : "FAIL";
  } catch (error) {
    failure = error;
    results.status = "FAIL";
    results.failure = error.message;
    results.stack = error.stack;
  } finally {
    if (browser) await browser.close().catch(() => {});
    await new Promise((resolve) => server.close(resolve));
    fs.mkdirSync(path.dirname(REPORT_PATH), { recursive: true });
    fs.writeFileSync(REPORT_PATH, JSON.stringify(results, null, 2) + "\n");
  }

  console.log(`${results.status}: rendered viewports=${results.viewports.length}, routes=${results.viewports.reduce((total, item) => total + item.routes.length, 0)}, axe violations=${results.total_axe_violations ?? "incomplete"}, browser/network errors=${results.browser_errors.length}; report=${path.relative(ROOT, REPORT_PATH)}`);
  if (failure || results.status !== "PASS") process.exitCode = 1;
}

main().catch((error) => {
  console.error(error.stack || error);
  process.exitCode = 1;
});
