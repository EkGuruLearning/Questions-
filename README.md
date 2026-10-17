# EkGuru Learning — all-subject CBT, results & study material

- Static / guest site: `https://ekgurulearning.github.io/Questions-/`
- Configured Vercel target (**deployment pending**, not a live-site claim): `https://ekguru-questions.vercel.app/subjects/test-room/index.html`
- **Google provider activation is pending the owner's Google OAuth setup.** Connecting hosting/database alone does not enable Google consent. Exact dashboard steps: [`maintainer/AUTH_AND_PRACTICE.md`](maintainer/AUTH_AND_PRACTICE.md).

1. **Native question/options CBT** — RPSC's existing 100-question reprint, two Reasoning samples and an original five-question IT check; single-choice, MSQ and numerical answers. Existing CN's 1,554-question engine and 20/50/100 presets remain available.
2. **One results timeline for every subject/test** — no automatic 200-result deletion, IndexedDB offline journal, owner-isolated retries, subject/test filters, Load older and export. Scale regressions cover **50 subjects / 550+ tests/results**; that is capacity testing, not a claim that 550 tests are already authored.
3. **Modern light / dark / system theme** — responsive 320px–desktop CBT. Native RPSC does not load the disliked PDF/OMR interface; optional older-scan tools are collapsed, and infeasible/unreviewed conversions stay reader-only.
4. **Six added IT-exam PDFs** — GATE CSE 2012/2016/2018/2019/2022 and ISRO ICRB CSE 2023 Set A. Pinned mirror hashes, source limitations and reader checks are recorded; not an exhaustive or independently official-authenticated archive. [Curation details](maintainer/CBT_AUTHORING.md#curated-it-pdfs--not-an-exhaustive-archive).
5. **Optional Google login** — encrypted HttpOnly/Secure cookies (up to 30 days) and private RLS-backed results. Owner's Google/provider and deployment setup is still pending; guest practice stays usable.

Static HTML/native JS + a tiny Node API; no React/Next, browser auth SDK or webfonts CDN. Production uses bundled/hash-cached entries and CSS, **Brotli 11 / gzip 9**, lazy subject/test banks and a **~5 KB CN bootstrap** instead of the roughly 400 KB file catalogue. PDF quality is not destroyed to inflate compression claims. Free-tier quotas/inactivity policies apply; lifetime-free availability is not guaranteed. Private results are **never** stored in public GitHub files.

Authoring/custom-player save contract: [`maintainer/CBT_AUTHORING.md`](maintainer/CBT_AUTHORING.md).

Audit reports, source registers, GIS scripts, purane legacy apps — kuch bhi website par nahi dikhta.
Wo sab `maintainer/` me hai (dekhne ke liye [`maintainer/README.md`](maintainer/README.md)).

## Folder structure

Website par wahi folders dikhte hain jo repository me hain — `content/` ka tree hi site ka tree hai.

```
index.html                                  home (subject cards + folder tiles)
subjects/                                   subject pages
  index.html                                  saare subjects
  computer-network/index.html                 CN home — folders + topic list
  computer-network/material/index.html        folder browser (folder kholo → files)
  computer-network/test/index.html            online test (topic-wise + full mix)
  test-room/index.html                        CBT starts + curated PDFs / optional scan tools
  practice/index.html                         shared all-subject native CBT player
  account/index.html                          optional Google login + private results
  rajasthan-geography/index.html              Map folder → Rajasthan → maps
404.html                                     purane link ke liye friendly page

content/                                    STUDENT CONTENT (yahi publish hota hai)
  reasoning/                                  Reasoning material (theory/practice/answers/tests)
  previous-year-papers/                       Old papers, exam-wise: ia/ sci/ computer-operator/
                                              system-assistant/ dsssb/ ssc/ net/ rpsc/
                                              (har exam ke andar saal ka folder: 2019/, 2020/ …)
  computer-network/
    theory/        📘 Theory — T01..T07 + complete book (8 PDF)
    practice/      ✍️ Practice questions — T01..T07 booklets (7 PDF)
    answers/       ✅ Answers & explanations — key + solutions (5 PDF)
    tests/         🧾 Tests — topic/unit/subject papers (11 PDF)
    reference/     📚 Reference book (1 PDF)
  rajasthan-geography/
    map/           🗂️ Map
      rajasthan/   🗺️ Rajasthan ke maps — A1/A2/A3/A4 + preview (6 PNG)

assets/                                     site code
  css/ekguru.css                               ek hi stylesheet (light + dark)
  js/test.mjs                                  online test app (player, result, review)
  js/engine.mjs                                existing CN helpers
  js/quiz{,-engine}.mjs                        shared typed CBT player / rules
  js/account.mjs + history-store.mjs            owner-scoped results journal / cloud sync
  img/                                         map preview image

data/                                       site data
  site.json                                    generated page data (counts, titles, hashes)
  banks/cn/cn_questions.json                   canonical question bank (schema v2)
  banks/cn/manifest.json + T0N.<hash>.json     generated topic chunks (test page inhe load karta hai)
  catalog/subjects.json                        subject/topic titles (EN + HI)
  catalog/materials.json                       har downloadable file ka record
  catalog/site-routes.txt                      published page list
  tests/<subject>/*.test.json                 authoring contract (not directly exported)
  quizzes/manifest.json + hash indexes/banks  lazy generated CBT publication
  catalog/imported-papers.json                 pinned IT-paper provenance

maintainer/                                 NOT published — audits, reports, GIS, legacy, archive
tools/ tests/                               builders, validators, tests
```

## Naya material add karna — koi code change nahi

```bash
# 1. file rakho — jis folder me rakhoge, wahi folder website par banega
content/previous-year-papers/dsssb/2019/DSSSB-Computer-Operator-2019-Paper-1.pdf
content/reasoning/practice/series/Sitting-Arrangement-Set-1.pdf

# 2. rebuild (+ image ho to pehle preview)
python3 tools/build_thumbs.py       # sirf nayi picture ke liye (PNG/JPG)
python3 tools/build_practice.py     # old-paper uploads -> Test Room manifest
python3 tools/build_catalog.py      # content -> data/site.json
python3 tools/build_quizzes.py      # data/tests/<subject>/*.test.json -> lazy CBT banks
python3 tools/build_pages.py        # data/site.json -> plain HTML pages
python3 tools/build_site_routes.py  # published page list (validate/test isi ko padhte hain)

# 3. verify
python3 tools/validate_site.py
```

Folder aur file ke naam se hi title ban jata hai (`dsssb` → DSSSB, `2019` → 2019,
`DSSSB-...-Paper-1.pdf` → DSSSB Computer Operator 2019 Paper 1). Hindi title, note ya SEO
alt/description chahiye to `data/catalog/materials.json` me us file ka record likh do — optional hai.

Builder khud check karta hai: jo file register nahi hui, ya jo registered path gayab hai — dono par
build fail ho jata hai. Isliye website par kabhi adhura/tuta hua record nahi jayega.

## Question bank rebuild

```bash
python3 tools/build_site_data.py     # canonical bank -> data/banks/cn/manifest.json + topic chunks
python3 tools/build_catalog.py       # chunks + catalogue -> data/site.json
python3 tools/read_structure.py --check
```

## Pages kaise bante hain

Website plain HTML hai — koi page browser me JavaScript se nahi banta, isliye page turant khulta hai.
`tools/build_pages.py` har subject ka page aur har folder ka apna page likhta hai, `content/` ke folder
structure ke hisaab se (folder rakho → page apne aap). Har page par breadcrumb aur "↑ upar wale page
par jao" link hota hai. Online test app alag hai: wo `assets/js/test.mjs` se chalta hai.

Sirf visitor material publish hota hai — `maintainer/`, `tools/`, `tests/` aur `.md` files site par
kahin link nahi hoti (`tools/validate_site.py` isi par fail karta hai).

## Reasoning chapters kaise add karein (namuna pehle se hai)

Har Reasoning folder me ek **sample** rakha hai, taaki format saaf dikhe:

```
content/reasoning/theory/      📘 Reasoning-Series-Sample-Chapter.pdf     (notes ka namuna)
content/reasoning/practice/    ✍️ Reasoning-Series-Sample-Practice.pdf    (12 sawal, options ke saath)
content/reasoning/answers/     ✅ Reasoning-Series-Sample-Answer-Key.pdf   (key + ek-line hal)
content/reasoning/tests/       🧾 Reasoning-Sample-Test-Paper.pdf         (10 sawal ka test)
```

### Apne chapters upload karne ka tarika (do step)

```bash
# 1. chapter ke chaaron folder ek command me banao (Calendar, Clock, Blood Relations …)
python3 tools/new_reasoning_chapter.py "Calendar" "Clock" "Blood Relations"

# 2. PDFs in folders me daaliye (GitHub par bhi drag-drop kar sakte hain) —
#    content/reasoning/theory/Calendar/Calendar-Short-Notes.pdf
#    content/reasoning/practice/Calendar/Calendar-Practice-Questions.pdf
#    content/reasoning/answers/Calendar/Calendar-Answer-Key.pdf
#    content/reasoning/tests/Calendar/Calendar-Test-Paper.pdf

# 3. site bana dijiye
npm run build:content
```

Chapter ka folder khali ho to site par nahi dikhta — PDF daalte hi us chapter ka page apne aap
ban jata hai (naam se hi title, PDF ke andar ka content waisa hi rehta hai). Chapter ke andar ka
folder bhi dikhta hai: `content/reasoning/practice/Calendar/…` → website par `Practice questions ›
Calendar`. Naye sample PDF banane ke liye: `python3 tools/reasoning_samples.py [doc-id]`.

## Previous Year Papers — exam-wise aur saal-wise

`content/previous-year-papers/<exam>/<saal>/` me paper rakho; uploaded exam/year folders and reader cards automatically appear after rebuilding. Source-directory links are separately labelled official paper, key, candidate login or third-party material. A year link is not a promise that every exam/year PDF is already hosted. Native CBT conversion needs reviewed question/options data; scans/mixed formats can stay reader-only.

## Local preview

```bash
npm ci
EKGURU_DISABLE_AUTH=true npm run dev  # http://localhost:8000 — website + guest API
# Real local login: fill ignored .env.local from .env.example, then npm run dev
# Static-only fallback: python3 tools/serve_site.py
```

## Mobile check (asli browser me)

```bash
# ek baar setup (browser puppeteer ke saath)
mkdir -p /tmp/mcheck && cd /tmp/mcheck && npm init -y && npm i puppeteer-core @sparticuz/chromium

node tests/mobile/mobile_check.cjs   # 360/390/768/1280 widths par saare important pages
```

Ye check pakka karta hai: koi page sideways scroll nahi karta, phone par "Menu" dikhta hai
(desktop nav 951px ke baad), tap targets chhote nahi, console me error nahi. Screenshots
`/tmp/ekguru-mobile-shots` me aate hain. `run_release_checks.py` ise bhi chalata hai aur
browser na milne par skip (exit 77) kar deta hai.

## Checks

```bash
python3 tools/validate_site.py                    # routes, links, downloads, hashes, no .md/audit links
python3 tools/validate_question_bank.py           # canonical bank + evidence gate + chunk coverage
python3 tools/read_structure.py --check           # structure + generated data + whitespace preflight
python3 tools/run_release_checks.py               # poora suite + maintainer/reports/release_checks.json
python3 -m unittest discover -s tests/site -p 'test_*.py' -v
python3 -m unittest discover -s tests/navigation -p 'test_*.py' -v
python3 -m unittest discover -s tests/responsive -p 'test_*.py' -v
python3 -m unittest discover -s tests/data -p 'test_*.py' -v
node --test tests/engine/engine.test.mjs
NODE_PATH=<node_modules> node tests/navigation/site_dom_smoke.cjs       # optional (jsdom)
NODE_PATH=<node_modules> node tests/navigation/test_app_dom_smoke.cjs   # optional (jsdom)
```

`SITE_GUIDE.md` me data flow, folder responsibilities aur maintenance recipes detail me hain.

## GitHub Pages loading / mobile reader

- Test data is resolved relative to `assets/js/test.mjs` (`../../`), **not** the
  current page or the domain root. This preserves `/Questions-/` on GitHub Pages.
- PDF and map **Open** buttons use `subjects/reader/index.html?file=content%2F…`.
  PDF.js is self-hosted in `assets/vendor/pdfjs/` (Apache-2.0); no CDN, backend,
  iframe PDF plugin or external proxy is required. PDFs render one page at a time
  with page/zoom controls. Original and Download links remain available.
- The map folder shows a lightweight image immediately, instead of an embedded
  PDF that may be blank on Android/iOS. Full maps open in the zoomable reader.
- The CBT player supports countdown/auto-submit, saved answers during question
  navigation, clear response, mark-for-review & next, and a mobile palette toggle.
  CN attempts are in memory; reloading a running CN test resets it. Old-paper Test Room
  drafts auto-save locally and resume with the original wall-clock deadline.
- Only locally hosted files are guaranteed by repository checks. Other exams'
  official/third-party sites may be unavailable, require login, or remove papers;
  these are external source links, not files hosted by EkGuru. RPSC Paper I 2024
  questions and the answer key are hosted locally and available in the reader.

Real-browser regression (start `EKGURU_DISABLE_AUTH=true npm run dev` first):

```bash
npm install --prefix /tmp/ekguru-deps puppeteer-core @sparticuz/chromium
NODE_PATH=/tmp/ekguru-deps/node_modules node tests/mobile/cbt_reader_check.cjs
```

The preview server accepts both `/` and `/Questions-/` so project-path bugs can
be reproduced locally. The browser check uses **real ES modules** and the
`/Questions-/` prefix, covering CBT at 360/390/768/1280px and PDF/map reading.

Changes on an Arena working branch do not update the public site automatically:
GitHub Pages is configured to deploy **main / (root)**. Merge the reviewed fix PR
into main and wait for the Pages deployment before checking the public URL.

## Google login / old-paper upload / production build

```bash
npm ci
npm run build:content   # discover paper uploads + regenerate manifests/pages/routes
npm test               # auth/cookie/CSRF/ownership/timer/grading tests
npm run build          # ignored public/ + Vercel Build Output API
```

Upload PDFs to `content/previous-year-papers/<exam>/<year>/`; optional count/answer-key
metadata goes in the mirrored `data/practice/papers/<exam>/<year>/<name>.paper.json`,
not in `content/`. Unreviewed/mixed-format papers can set `reader_only: true`. Native tests use `data/tests/<subject>/*.test.json`; no paid OCR API is required. The existing RPSC key is labelled
provided/unverified; Q3 and Q5 are intentionally ungraded. BCI scans are unscored until
a digital key is supplied; optional PDF tools do not pretend to be a native question transcription.

Full instructions, Google activation, privacy/retention, deployment integration limits
and free-tier caveats: [`maintainer/AUTH_AND_PRACTICE.md`](maintainer/AUTH_AND_PRACTICE.md).
GitHub Actions can publish a fresh static build after uploads to main; select
**Settings → Pages → Source: GitHub Actions** once. Vercel automatic updates separately
require granting its GitHub app access to this repository.
