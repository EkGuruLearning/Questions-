#!/usr/bin/env node
/* Asli browser me mobile check — puppeteer ke saath (optional).
 *
 * Ye script website ko phone/tablet/desktop width par kholti hai aur pakka karti hai:
 *   1. koi page horizontally scroll nahi karta (koi element screen se bahar nahi),
 *   2. nav sahi hai (phone par "Menu" toggle, 951px+ par desktop nav row),
 *   3. console me koi error nahi,
 *   4. tap targets chhote nahi (link/button ki height).
 * Screenshots bhi leta hai (path niche dikhta hai).
 *
 * Chalane ke liye (ek baar):
 *   mkdir -p /tmp/mcheck && cd /tmp/mcheck && npm init -y && npm i puppeteer-core @sparticuz/chromium
 *   LD_LIBRARY_PATH=... node tests/mobile/mobile_check.cjs      # ya system ka Chrome:
 *   CHROME_PATH=/usr/bin/chromium node tests/mobile/mobile_check.cjs
 *
 * Agar puppeteer/Chrome na mile to ye script exit 77 deta hai (skip), fail nahi.
 */
"use strict";

const child = require("child_process");
const fs = require("fs");
const http = require("http");
const os = require("os");
const path = require("path");
const zlib = require("zlib");

const ROOT = path.resolve(__dirname, "..", "..");
const BASE = process.env.BASE || "http://127.0.0.1:8000";
const OUT = process.env.OUT || path.join("/tmp", "ekguru-mobile-shots");
const WIDTHS = [
  { name: "phone-360", width: 360, height: 740, dsf: 2 },
  { name: "phone-390", width: 390, height: 844, dsf: 2 },
  { name: "tab-768", width: 768, height: 1024, dsf: 1 },
  { name: "desktop-1280", width: 1280, height: 900, dsf: 1 },
];
/* Page list site-routes.txt se aati hai, isliye naye pages apne aap check hote hain.
   Har category se kam se kam ek page liya jata hai + 404. */
function pageList() {
  const routes = fs.readFileSync(path.join(ROOT, "data/catalog/site-routes.txt"), "utf8")
    .split("\n").map((line) => line.trim())
    .filter((line) => line && !line.startsWith("#"));
  const wanted = [
    "index.html",
    "subjects/index.html",
    "subjects/computer-network/index.html",
    "subjects/computer-network/material/index.html",
    "subjects/computer-network/test/index.html",
    "subjects/previous-year-papers/index.html",
    "subjects/previous-year-papers/rpsc/index.html",
    "subjects/rajasthan-geography/index.html",
    "subjects/reasoning/index.html",
  ];
  const chosen = wanted.filter((route) => routes.includes(route));
  const extras = routes.filter((route) => !chosen.includes(route) && route !== "404.html");
  const sample = extras.filter((route, index) => index % Math.max(1, Math.ceil(extras.length / 6)) === 0).slice(0, 6);
  return [...chosen, ...sample, ...extras.filter((r) => /\/\d{4}\//.test(r)).slice(0, 2), "404.html"]
    .filter((route, index, all) => all.indexOf(route) === index)
    .map((route) => [route.replace(/[\/]/g, "-").replace(".html", ""), `/${route}`]);
}

/* Chrome ko chahiye libraries (@sparticuz/chromium apne saath brotli-compressed tar
   bhejta hai). Zaroorat pade to yahin extract kar lete hain, warna system ko hi use
   karne dete hain. Isse release check CI/clean sandbox me bhi chal jata hai. */
function prepareChromiumLibs() {
  if (process.env.LD_LIBRARY_PATH && process.env.LD_LIBRARY_PATH.includes("ekguru-chromium-libs")) {
    return process.env.LD_LIBRARY_PATH;
  }
  for (const base of [process.env.PUPPETEER_DIR, "/tmp/mcheck", ROOT].filter(Boolean)) {
    let archive = "";
    try {
      // package.json `exports` me nahi hai, isliye main entry se upar walk karte hain
      let dir = path.dirname(require.resolve("@sparticuz/chromium", { paths: [base] }));
      for (let step = 0; step < 4 && dir !== path.dirname(dir); step += 1) {
        const candidate = path.join(dir, "bin", "al2023.tar.br");
        if (fs.existsSync(candidate)) { archive = candidate; break; }
        dir = path.dirname(dir);
      }
    } catch (error) {
      archive = "";
    }
    if (!archive) continue;
    const target = path.join(os.tmpdir(), "ekguru-chromium-libs");
    try {
      fs.mkdirSync(target, { recursive: true });
      const tarPath = path.join(target, "al2023.tar");
      fs.writeFileSync(tarPath, zlib.brotliDecompressSync(fs.readFileSync(archive)));
      child.execFileSync("tar", ["-xf", tarPath, "-C", target, "--strip-components=1"], { stdio: "ignore" });
      fs.unlinkSync(tarPath);
    } catch (error) {
      return null;
    }
    return [target, process.env.LD_LIBRARY_PATH].filter(Boolean).join(":");
  }
  return null;
}

function loadPuppeteer() {
  const candidates = [process.env.PUPPETEER_DIR, "/tmp/mcheck", ROOT].filter(Boolean);
  for (const base of candidates) {
    try {
      const puppeteer = require(require.resolve("puppeteer-core", { paths: [base] }));
      let chromium = null;
      try {
        const module_ = require(require.resolve("@sparticuz/chromium", { paths: [base] }));
        chromium = module_.default || module_;
      } catch (error) {
        chromium = null;
      }
      return { puppeteer, chromium };
    } catch (error) {
      continue;
    }
  }
  return null;
}

function serverUp() {
  return new Promise((resolve) => {
    const request = http.get(BASE, (response) => {
      response.resume();
      resolve(true);
    });
    request.on("error", () => resolve(false));
    request.setTimeout(2000, () => {
      request.destroy();
      resolve(false);
    });
  });
}

(async () => {
  const loaded = loadPuppeteer();
  if (!loaded) {
    console.log("SKIP: puppeteer-core install nahi hai (exit 77). README me setup likha hai.");
    process.exit(77);
  }
  if (!(await serverUp())) {
    console.log(`SKIP: ${BASE} par site nahi chal rahi — pehle 'python3 tools/serve_site.py 8000' chalao (exit 77).`);
    process.exit(77);
  }
  const { puppeteer, chromium } = loaded;
  const executablePath = process.env.CHROME_PATH ||
    (chromium && chromium.executablePath ? await chromium.executablePath() : undefined);
  if (!executablePath) {
    const found = puppeteer.executablePath && puppeteer.executablePath();
    if (!found || !fs.existsSync(found)) {
      console.log("SKIP: Chrome/Chromium nahi mila (CHROME_PATH set karo) — exit 77.");
      process.exit(77);
    }
  }

  fs.mkdirSync(OUT, { recursive: true });
  const libPath = prepareChromiumLibs();
  const env = { ...process.env };
  if (libPath) env.LD_LIBRARY_PATH = libPath;
  let browser;
  try {
    browser = await puppeteer.launch({
      args: [...((chromium && chromium.args) || []), "--no-sandbox", "--disable-setuid-sandbox"],
      executablePath: executablePath || undefined,
      headless: chromium ? chromium.headless : true,
      defaultViewport: null,
      env,
    });
  } catch (error) {
    console.log("SKIP: browser launch nahi hua (system libs missing?) — exit 77.");
    console.log("      " + String(error.message).split("\n")[0]);
    process.exit(77);
  }

  let failures = 0;
  const lines = [];
  const pages = pageList();
  console.log(`checking ${pages.length} page(s) × ${WIDTHS.length} widths`);
  for (const view of WIDTHS) {
    const page = await browser.newPage();
    await page.setViewport({ width: view.width, height: view.height, deviceScaleFactor: view.dsf,
                             isMobile: view.width < 800, hasTouch: view.width < 800 });
    const consoleErrors = [];
    page.on("console", (message) => { if (message.type() === "error") consoleErrors.push(message.text()); });
    page.on("pageerror", (error) => consoleErrors.push(String(error)));

    for (const [name, url] of pages) {
      await page.goto(BASE + url, { waitUntil: "networkidle2", timeout: 30000 });
      const metrics = await page.evaluate(() => {
        const style = (selector) => {
          const element = document.querySelector(selector);
          return element ? getComputedStyle(element).display : "missing";
        };
        const desktopNav = style(".desktop-nav");
        const toggle = style(".site-menu-toggle");
        const closedNav = style(".site-menu:not([open]) .site-nav");
        const limit = document.documentElement.clientWidth + 1;
        const wide = [];
        document.querySelectorAll("body *").forEach((element) => {
          const rect = element.getBoundingClientRect();
          if (rect.width > 0 && rect.right > limit) {
            wide.push(`${element.tagName.toLowerCase()}.${(element.className || "").toString().split(" ")[0]}`);
          }
        });
        const small = [];
        document.querySelectorAll("main a, main button, .site-nav a, .site-menu-toggle").forEach((element) => {
          const rect = element.getBoundingClientRect();
          if (rect.width === 0) return;
          const inline = element.closest(".crumbs, .footer-grid, p, .section-note, .hero-lead");
          if (rect.height < 32 && !inline) small.push(`${element.textContent.trim().slice(0, 16)} ${Math.round(rect.height)}`);
        });
        return {
          scrollWidth: document.documentElement.scrollWidth,
          clientWidth: document.documentElement.clientWidth,
          desktopNav, toggle, closedNav,
          wide: [...new Set(wide)].slice(0, 5),
          small: [...new Set(small)].slice(0, 5),
        };
      });

      const narrow = view.width < 951;
      const problems = [];
      if (metrics.scrollWidth > metrics.clientWidth + 1) problems.push("horizontal scroll");
      if (narrow && metrics.desktopNav !== "none") problems.push(`desktop nav visible (${metrics.desktopNav})`);
      if (narrow && metrics.toggle === "none") problems.push("menu toggle hidden");
      if (narrow && metrics.closedNav !== "none") problems.push("closed menu visible");
      if (!narrow && metrics.desktopNav !== "flex") problems.push(`desktop nav hidden (${metrics.desktopNav})`);
      if (metrics.wide.length) problems.push(`wide element: ${metrics.wide.join(", ")}`);
      if (metrics.small.length) problems.push(`tiny tap target (<32px): ${metrics.small.join(", ")}`);
      if (consoleErrors.length) problems.push(`console: ${consoleErrors[0].slice(0, 80)}`);
      if (problems.length) failures += 1;

      lines.push(`${problems.length ? "FAIL" : "ok  "} ${view.name.padEnd(12)} ${url.padEnd(50)} ` +
                 (problems.length ? problems.join(" | ") : `scrollW=${metrics.scrollWidth}`));
      if (view.width <= 390) {
        await page.screenshot({ path: path.join(OUT, `${name}-${view.name}.png`), fullPage: true });
      }
    }
    await page.close();
  }
  await browser.close();

  console.log(lines.join("\n"));
  console.log(`\n${failures === 0 ? "PASS" : "FAIL"}: ${pages.length * WIDTHS.length} page/viewport checks, ` +
              `${failures} problem(s). Screenshots: ${OUT}`);
  process.exit(failures ? 1 : 0);
})();
