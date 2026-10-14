# EkGuru Learning — student portal (Computer Network + Rajasthan map atlas)

Live site (GitHub Pages project path): `https://ekgurulearning.github.io/Questions-/`

Website par sirf do cheezein hain, aur dono student ke kaam ki hain:

1. **Computer Network** — 7 topics, topic-wise/full-mix online test (1,554 questions) aur PDF study material (32 files).
2. **Rajasthan Geography** — border-district map atlas, A1 se A4 print sizes (6 files).

Audit reports, source registers, GIS scripts, purane legacy apps — kuch bhi website par nahi dikhta.
Wo sab `maintainer/` me hai (dekhne ke liye [`maintainer/README.md`](maintainer/README.md)).

## Folder structure

```
index.html                                  home
subjects/                                   subject pages
  index.html                                  saare subjects
  computer-network/index.html                 CN home — "Material" ya "Test"
  computer-network/material/index.html        study material (downloads)
  computer-network/test/index.html            online test (topic-wise + full mix)
  rajasthan-geography/index.html              map gallery + downloads
404.html                                     purane link ke liye friendly page

content/                                    STUDENT CONTENT (yahi publish hota hai)
  computer-network/theory/                     T01..T07 theory + complete book (PDF)
  computer-network/practice/                   practice booklets + answer key (PDF)
  computer-network/tests/                      topic/unit/subject tests (PDF)
  computer-network/reference/                  reference book (PDF)
  rajasthan-geography/maps/                    A1..A4 atlas + preview (PNG)

assets/                                     site code
  css/ekguru.css                               ek hi stylesheet (light + dark)
  js/site.js                                   topic/material/map lists render karta hai
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

## Naya material add karna

```bash
# 1. file rakho
content/computer-network/theory/T08-...-Theory-MCQ.pdf

# 2. data/catalog/materials.json me entry likho (subject, topic, kind, title_en, title_hi, note)

# 3. rebuild + validate
python3 tools/build_catalog.py
python3 tools/validate_site.py
```

Builder khud check karta hai: jo file register nahi hui, ya jo registered path gayab hai — dono par
build fail ho jata hai. Isliye website par kabhi adhura/tuta hua record nahi jayega.

## Question bank rebuild

```bash
python3 tools/build_site_data.py     # canonical bank -> data/banks/cn/manifest.json + topic chunks
python3 tools/build_catalog.py       # chunks + catalogue -> data/site.json
python3 tools/read_structure.py --check
```

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
