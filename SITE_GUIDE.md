# Site guide — how the EkGuru portal is wired

## 1. Published pages

| Route | Kya dikhta hai |
|---|---|
| `index.html` | Home — do subject cards + link counts + map preview |
| `subjects/index.html` | Saare subjects ki list |
| `subjects/computer-network/index.html` | CN home: **Material kholo** ya **Test shuru karo**, phir 7 topic cards |
| `subjects/index.html` | Saare subjects; `?subject=<slug>` par us subject ke folders (`&folder=` se andar) |
| `subjects/computer-network/material/index.html` | Folder browser: folder tile kholo → files dikhte hain (open/download) |
| `subjects/computer-network/test/index.html` | Test setup + player + result + review |
| `subjects/rajasthan-geography/index.html` | Map folder → Rajasthan folder → A1/A2/A3/A4 map files |
| `404.html` | Purane/unknown link ke liye friendly page |

`data/catalog/site-routes.txt` published page list rakhta hai; `tools/validate_site.py` isi list se
link check karta hai. Naya page banao to yahan bhi likho.

## 2. Data flow

```
data/banks/cn/cn_questions.json      canonical bank (schema v2, 1,556 records)
        │  tools/build_site_data.py
        ▼
data/banks/cn/manifest.json + T0N.<hash>.min.json     (test page inhi chunks ko fetch karti hai)
        │
data/catalog/subjects.json  (titles, topics, routes)  │  tools/build_catalog.py
data/catalog/materials.json (file registry + labels)  ▼
                                              data/site.json  ←  pages isi se bante hain
                                                      │  tools/build_pages.py
                                                      ▼
                                index.html, subjects/**/index.html  (plain HTML, 27 pages)
                                                      │  tools/build_site_routes.py
                                                      ▼
                                            data/catalog/site-routes.txt
```

* `data/site.json` hi website ka single source of truth hai: subject titles (EN/HI), topic counts,
  section names, file sizes, SHA-256 aur download URLs.
* Pages **plain HTML** hain — `tools/build_pages.py` unhe `data/site.json` se likhta hai, isliye
  browser me koi render/fetch nahi hota aur page turant khulta hai. Har folder ka apna page hai,
  har page par breadcrumb + "↑ upar wale page par jao" link hai, aur links relative hain — GitHub
  Pages project path `/Questions-/` par bhi sahi chalti hain.
* Sirf visitor material publish hota hai: `maintainer/`, `tools/`, `tests/` aur `.md` files kisi
  published page par link nahi hoti (validator isi par fail karta hai).
* Test page pehle `manifest.json` load karti hai, phir sirf chune gaye topic ke chunk(s). Isliye
  topic-wise test poore bank ko download nahi karta.

## 3. Folder responsibilities

Website ka folder view `content/` ke asli folders se banta hai:

| `content/` folder | Website par |
|---|---|
| `computer-network/theory/` | 📘 Theory |
| `computer-network/practice/` | ✍️ Practice questions |
| `computer-network/answers/` | ✅ Answers & explanations |
| `computer-network/tests/` | 🧾 Tests |
| `computer-network/reference/` | 📚 Reference book |
| `rajasthan-geography/map/` | 🗂️ Map |
| `rajasthan-geography/map/rajasthan/` | 🗺️ Rajasthan (map files) |
| `reasoning/{theory,practice,answers,tests}/` | 🧠 Reasoning (khali folder bhi dikhta hai) |
| `previous-year-papers/<exam>/<saal>/` | 🧾 Exam folder → saal ka folder (apne aap) |

| Folder | Kya rakhna hai | Website par? |
|---|---|---|
| `content/<subject>/<folder>/...` | Student PDF/PNG files (bas yahi publish hota hai) | Haan — folder view + download/open links |
| `assets/` | CSS, JS, images | Haan (code) |
| `data/banks/cn/` | Canonical bank + generated chunks | Haan (test data) |
| `data/catalog/` | Editable catalogue inputs | Nahi (build input) |
| `maintainer/` | Audits, reports, GIS project, intake, legacy apps, archive | **Nahi** — kabhi link nahi karna |
| `tools/`, `tests/` | Builders, validators, tests | Nahi |

`tools/validate_site.py` fail ho jata hai agar koi page `maintainer/`, `tools/`, `tests/` ya kisi
`.md` file par link kare — isliye audit material galti se public nahi ho sakta.

## 4. Recipes

### Nayi PDF student ko dena hai
1. File `content/<subject>/<folder>/` me rakho (naam me topic prefix, e.g. `T03-...`).
2. `data/catalog/materials.json` me entry: `file`, `subject`, `topic` (ya `null`),
   `order`, `title_en`, `title_hi`, `note_en`, `note_hi`.
3. Naya folder banaya? `data/catalog/subjects.json` ke `folders` me uska label likho
   (`title_en`, `title_hi`, `note_en`, `note_hi`, `icon`, `order`) — site par folder card apne aap ban jayega.
4. Picture (map/PNG) hai to `python3 tools/build_thumbs.py` — halka preview `data/thumbs/` me banta hai,
   jise website thumbnail ke liye use karti hai (full file dekho/download ke liye alag rehti hai).
   Picture ke entry me `alt_en`, `alt_hi`, `description_en`, `description_hi` bhi likho — alt text image
   SEO hai aur description folder view me map ke neeche dikhti hai (kitne jile, kis se seema lagti hai etc.).
5. `python3 tools/build_catalog.py && python3 tools/validate_site.py`

### Nayi quiz/test file (HTML) banani hai?
Zaroorat nahi — topic-wise aur full-mix test site ke andar hi hai. Naya topic add karne ke liye
`tools/data/topicN_data.py` me questions likho, `python3 tools/cn_export_json.py` chalao, phir
`tools/build_site_data.py` + `tools/build_catalog.py`.

### Naya subject / naya map folder
`data/catalog/subjects.json` me subject (aur uske `folders`) add karo, `content/<subject>/...` me
files rakho, routes banao, `data/catalog/site-routes.txt` me pages likho, phir builder + validator
chalao. Map ke liye jaise `content/rajasthan-geography/map/<state>/` — folder khud site par aa jayega.

### Question bank ke sections
Test page section filter topic ke `subtopic` se banata hai (canonical bank ke sections). Section ka
chhota naam builder nikalta hai: "Section A - DC Components & Protocol Basics (…)" → "DC Components
& Protocol Basics".

## 5. Test page behaviour

* **Do modes:** Topic-wise (topic → optional section ticks → count) aur Full mix (saare topics).
* **Do pattern:** Practice (turant answer + explanation/nukta) aur Exam (end me result, optional time limit).
* **Language:** English + हिंदी (dono), English, ya हिंदी.
* Result: score ring, correct/wrong/skipped, topic-wise bars, poora answer review, "galat questions dobara".
* Saved questions (⭐) aur pichhle test results `localStorage` me rehte hain — server par kuch nahi jata.

## 5b. Naya subject ya folder — bina code change

1. `content/<subject>/<folder>/` banao aur file daalo (khali chhodna ho to `.gitkeep` rakho taaki git me rahe).
2. `python3 tools/build_thumbs.py && python3 tools/build_catalog.py`.
3. Subject/folder card apne aap ban jayega (naam se label). Hindi naam, icon, note, order ya
   "subject ka online test bhi hai" chahiye to `data/catalog/subjects.json` me us entry ko likh do.

## 6. Local preview

```bash
python3 tools/serve_site.py          # http://localhost:8000
```

Ye server sirf public paths deta hai (`index.html`, `404.html`, `subjects/`, `assets/`, `data/`,
`content/`). `maintainer/`, `tools/`, `tests/` aur repo docs par 404 page milta hai — bina directory
listing. GitHub Pages par ye files URL se technically reachable hoti hain (static host), lekin website
kabhi unhe link nahi karti; `tools/validate_site.py` isi rule ko enforce karta hai.

## 7. Release checks

```bash
python3 tools/read_structure.py --check      # required paths + generated data + links + whitespace
python3 tools/run_release_checks.py          # poora suite, report: maintainer/reports/release_checks.json
```

`run_release_checks.py` ka report `maintainer/` me likha jata hai — website par nahi.
Optional browser checks (jsdom) skip ho jate hain agar package installed na ho.
