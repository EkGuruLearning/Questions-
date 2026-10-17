#!/usr/bin/env node
/* Real ES modules + real HTTP under /Questions-/ (no mocked module base URL).
 * npm install --prefix /tmp/ekguru-deps puppeteer-core @sparticuz/chromium
 * NODE_PATH=/tmp/ekguru-deps/node_modules node tests/mobile/cbt_reader_check.cjs
 * Start tools/serve_site.py first. Set BASE to test another deployment.
 */
const assert = require('node:assert/strict');
let puppeteer, chromium;
try {
  puppeteer = require('puppeteer-core');
  const module_ = require('@sparticuz/chromium');
  chromium = module_.default || module_;
} catch {
  console.log('SKIP: puppeteer-core / @sparticuz/chromium not installed');
  process.exit(77);
}
const BASE = process.env.BASE || 'http://127.0.0.1:8000/Questions-/';
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
(async () => {
  const browser = await puppeteer.launch({ executablePath: await chromium.executablePath(), args: chromium.args, headless: true });
  try {
    for (const width of [360, 390, 768, 1280]) {
      const page = await browser.newPage();
      await page.setViewport({ width, height: 844, isMobile: width < 800, hasTouch: width < 800 });
      const errors = [];
      const bad = [];
      page.on('pageerror', (error) => errors.push(error.message));
      page.on('response', (r) => { if (r.status() >= 400) bad.push(`${r.status()} ${r.url()}`); });
      await page.goto(BASE + 'subjects/computer-network/test/index.html?topic=T02');
      await page.waitForFunction(() => !document.getElementById('startButton').disabled);
      await page.click('[data-pattern="exam"]');
      await page.select('#countSelect', '10');
      await page.select('#minutesSelect', '15');
      await page.click('#startButton');
      await page.waitForSelector('#playerPanel:not([hidden]) .option');
      await page.click('#optionList .option');
      assert(await page.$eval('#feedback', (e) => e.hidden), 'CBT must hide answers');
      await page.click('#markNextButton');
      assert.match(await page.$eval('#questionNumber', (e) => e.textContent), /2 of 10/);
      assert.equal(await page.$$eval('#paletteGrid .answered.marked', (es) => es.length), 1);
      await page.click('#optionList .option');
      await page.click('#clearAnswerButton');
      assert.equal(await page.$$eval('#optionList [aria-pressed="true"]', (es) => es.length), 0);
      if (width < 950) await page.click('#paletteToggle');
      await page.click('#paletteGrid button:nth-child(1)');
      assert.equal(await page.$$eval('#optionList [aria-pressed="true"]', (es) => es.length), 1, 'answer survives navigation');
      assert(await page.$eval('#timer', (e) => /^1[45]:\d\d$/.test(e.textContent)), 'countdown should run');
      assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), 'CBT overflows horizontally');
      page.once('dialog', (dialog) => dialog.dismiss());
      await page.click('#finishButton');
      await sleep(100);
      assert(await page.$eval('#resultPanel', (e) => e.hidden), 'cancel submit must keep attempt');
      page.once('dialog', (dialog) => dialog.accept());
      await page.click('#finishButton');
      await page.waitForSelector('#resultPanel:not([hidden])');
      assert.match(await page.$eval('#scoreValue', (e) => e.textContent), /^\d+%$/);
      await page.close();
      assert.deepEqual(errors, []);
      assert.deepEqual(bad, []);
      console.log(`PASS CBT ${width}px: topic load, exam, review+next, clear, palette, timer, submit/cancel, result`);
    }
    const page = await browser.newPage();
    await page.setViewport({ width: 360, height: 740, isMobile: true });
    const errors = [];
    page.on('pageerror', (error) => errors.push(error.message));
    const files = [
      'content/previous-year-papers/rpsc/2024/RPSC-Programmer-2024-Paper-1-Questions.pdf',
      'content/previous-year-papers/rpsc/2024/RPSC-Programmer-2024-Paper-1-Answer-Key.pdf',
      'content/computer-network/theory/T01-Data-Communication-Theory.pdf',
      'content/rajasthan-geography/map/rajasthan/Rajasthan-Border-Districts-A4-Portrait-Print.pdf',
      'content/rajasthan-geography/map/rajasthan/Rajasthan-Border-Districts-A4-Portrait.png',
    ];
    const fs = require('node:fs');
    const path = require('node:path');
    // Use the actual registered theory filename, not an assumed spelling.
    const site = JSON.parse(fs.readFileSync(path.join(__dirname, '../../data/site.json'), 'utf8'));
    const findPDF = (node) => node.files.find((f) => /T01.*\.pdf$/.test(f.url))?.url || node.folders.map(findPDF).find(Boolean);
    files.push('content/rajasthan-geography/map/rajasthan/Rajasthan_Border_District_Map_A4 (1).pdf');
    files.push('content/rajasthan-geography/map/rajasthan/PDF/Rajasthan_Border_District_Map_A4.pdf');
    files[2] = findPDF(site.subjects.find((s) => s.id === 'computer-network').tree);
    for (const file of files) {
      console.log("CHECK mobile reader: " + file);
      await page.goto(BASE + 'subjects/reader/index.html?file=' + encodeURIComponent(file));
      await page.waitForFunction(() => /^(Ready|Page nahi)|Original file \/ Download available/.test(document.getElementById('readerStatus').textContent), { timeout: 60000 });
      assert.match(await page.$eval('#readerStatus', (e) => e.textContent), /^Ready/, file);
      assert(await page.$eval('#downloadFile', (e) => e.hasAttribute('download')));
      if (file.endsWith('.pdf')) {
        const pixels = await page.$eval('#pdfCanvas', (c) => {
          const data = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
          let dark = 0;
          for (let i = 0; i < data.length; i += 4) if (data[i] < 200 && data[i + 1] < 200 && data[i + 2] < 200) dark++;
          return dark;
        });
        assert(pixels > 100, 'PDF rendered blank');
        const nextDisabled = await page.$eval('#readerNext', (e) => e.disabled);
        if (!nextDisabled) {
          await page.click('#readerNext');
          await page.waitForFunction(() => document.getElementById('pageLabel').textContent.startsWith('2 /') && document.getElementById('readerStatus').textContent.startsWith('Ready'));
        }
      } else assert(await page.$eval('.reader-image', (e) => e.naturalWidth > 0));
      await page.click('#readerZoomIn');
      await page.waitForFunction(() => document.getElementById('zoomLabel').textContent === '125%' && document.getElementById('readerStatus').textContent.startsWith('Ready'));
      assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), 'reader overflows horizontally');
      console.log('PASS mobile reader: ' + file);
    }
    await page.goto(BASE + 'subjects/rajasthan-geography/map/rajasthan/index.html');
    assert(await page.$eval('.map-frame img', (e) => e.complete && e.naturalWidth > 0), 'map preview missing');
    await page.goto(BASE + 'subjects/reader/index.html?file=https://example.com/private.pdf');
    await page.waitForFunction(() => document.getElementById('readerStatus').textContent.includes('Sirf is website'));
    assert.deepEqual(errors, []);
    await page.close();
    console.log('PASS lightweight map preview and external URL rejection');
  } finally { await browser.close(); }
})().catch((error) => { console.error(error); process.exit(1); });
