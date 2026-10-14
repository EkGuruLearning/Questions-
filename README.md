# EkGuru Learning — student portal (Computer Network + Rajasthan map atlas)

Live site (GitHub Pages project path): `https://ekgurulearning.github.io/Questions-/`

Website par sirf do cheezein hain, aur dono student ke kaam ki hain:

1. **Computer Network** — 7 topics, topic-wise/full-mix online test (1,554 questions) aur PDF study material (32 files).
2. **Rajasthan Geography** — border-district map atlas, A1 se A4 print sizes (6 files).

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
  js/engine.mjs                                pure question-engine helpers
  img/                                         map preview image

data/                                       site data
  site.json                                    generated page data (counts, titles, hashes)
  banks/cn/cn_questions.json                   canonical question bank (schema v2)
  banks/cn/manifest.json + T0N.<hash>.json     generated topic chunks (test page inhe load karta hai)
  catalog/subjects.json                        subject/topic titles (EN + HI)
  catalog/materials.json                       har downloadable file ka record
  catalog/site-routes.txt                      published page list

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
python3 tools/build_catalog.py      # content -> data/site.json
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

Apne asli chapter ki file usi folder me rakh dijiye — naam se hi title ban jayega, aur website par
apne aap dikh jayega (`build_catalog.py` → `build_pages.py`). Chapter ke andar subfolder bhi ban
sakta hai, jaise `content/reasoning/theory/Series/Series-Notes.pdf` → website par `Series` folder.
Naye sample banane ke liye: `python3 tools/reasoning_samples.py [doc-id]`.

## Previous Year Papers — exam-wise aur saal-wise

`content/previous-year-papers/<exam>/<saal>/` me paper rakho. Har exam ke page par **2000 se 2026 tak
ke saare saal** chip ke roop me dikhte hain: jis saal ka paper aa chuka hai wo gehra (blue) chip hai
aur us par click karke paper khulta hai; baaki saal muted chip hain. Jo saal folder banta hai, uska page
apne aap ban jata hai.

## Local preview

```bash
python3 tools/serve_site.py          # http://localhost:8000 — sirf public pages
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
