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
| `subjects/test-room/index.html` | Old-paper PDF + OMR, timer, local resume, review/export |
| `subjects/account/index.html` | Optional Google login + private synced history |
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
1. File `content/<subject>/<folder>/` me rakho (naam me topic prefix, e.g. `T03-...`) —
   jitne chahe folder/andar ke folder banao, sab apne aap dikhenge. Title aur description
   file ke naam se apne aap bante hain (Hindi + English).
2. Build chalao (bas ek baar): `python3 tools/build_thumbs.py && python3 tools/build_practice.py && python3 tools/build_catalog.py && python3 tools/build_pages.py && python3 tools/build_site_routes.py`
   — picture ke liye halka preview bhi `data/thumbs/` me apne aap ban jata hai
   (ImageMagick chahiye; na ho to website asli picture hi dikha degi).
3. Bas — folder card, file row (title + description + preview + download) aur us folder ka
   SEO-ready page (title, description, keywords, canonical, OG/Twitter, JSON-LD) taiyar.
4. *Optional sundarta:* `data/catalog/subjects.json` me folder/subject ka apna
   `title_en`, `title_hi`, `note_en`, `note_hi`, `icon`, `order` likh do; `data/catalog/materials.json`
   me file ke liye `title_en`, `title_hi`, `note_en`, `note_hi`, `topic`, `order` aur picture ke liye
   `alt_en`, `alt_hi`, `description_en`, `description_hi` (image SEO). Catalogue ke bina bhi sab chalta hai.

### Nayi quiz/test file (HTML) banani hai?
Zaroorat nahi — topic-wise aur full-mix test site ke andar hi hai. Naya topic add karne ke liye
`tools/data/topicN_data.py` me questions likho, `python3 tools/cn_export_json.py` chalao, phir
`tools/build_site_data.py` + `tools/build_catalog.py`.

### Naya subject / naya map folder
`content/<subject>/...` me folder/files rakho aur upar wala build chalao — subject card, folder
pages aur routes (`data/catalog/site-routes.txt`) sab apne aap ban jate hain. Hindi naam, icon,
note, order ya online test chahiye to `data/catalog/subjects.json` me us entry ko likh do. Map ke
liye jaise `content/rajasthan-geography/map/<state>/` — folder khud site par aa jayega.

### Question bank ke sections
Test page section filter topic ke `subtopic` se banata hai (canonical bank ke sections). Section ka
chhota naam builder nikalta hai: "Section A - DC Components & Protocol Basics (…)" → "DC Components
& Protocol Basics".

## 5. Test page behaviour

* **Do modes:** Topic-wise (topic → optional section ticks → count) aur Full mix (saare topics).
* **Do pattern:** Practice (turant answer + explanation/nukta) aur Exam (end me result, optional time limit).
* **Language:** English + हिंदी (dono), English, ya हिंदी.
* Result: score ring, correct/wrong/skipped, topic-wise bars, poora answer review, "galat questions dobara".
* Saved questions (⭐) aur local results browser mein rehte hain. Google se pehle se logged-in users ke **naye** completed tests private Supabase history mein bhi sync ho sakte hain; guest history silently upload nahi hoti.

## 5b. Naya subject ya folder — bina code change

1. `content/<subject>/<folder>/` banao aur file daalo (khali chhodna ho to `.gitkeep` rakho taaki git me rahe).
   Andar ke andar ke folders bhi chalega — PDF, PNG/JPG/WebP/AVIF/GIF sab dikhte hain, title aur
   description file ke naam se apne aap (Hindi + English) bante hain.
2. `python3 tools/build_thumbs.py && python3 tools/build_practice.py && python3 tools/build_catalog.py && python3 tools/build_pages.py && python3 tools/build_site_routes.py`
   (sitemap.xml aur robots.txt bhi isi me update ho jate hain).
3. Subject/folder card, uska SEO-ready page aur links apne aap ban jayenge (naam se label).
   Hindi naam, icon, note, order ya "subject ka online test bhi hai" chahiye to
   `data/catalog/subjects.json` me us entry ko likh do. Folder delete kiya to next build uske
   purane pages bhi hata deta hai.

## 6. Local preview

```bash
npm ci
EKGURU_DISABLE_AUTH=true npm run dev  # website + same-origin guest API, http://localhost:8000
# Static-only: python3 tools/serve_site.py
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

## 8. Google login + old-paper Test Room

`tools/build_practice.py` scans all old-paper PDFs, skips key PDFs, validates optional
metadata under `data/practice/papers/`, and writes `data/practice/manifest.json`.
`npm run build:content` includes this step before the ordinary catalogue/pages/routes.
New scanned papers need no OCR; without a digital key they get attempted/skipped
progress, not fabricated marks. Provided-key scores exclude dropped/unkeyed questions.
Drafts save per browser for up to seven days; timers do not restart on reload.

`server/handler.mjs` provides same-origin Google PKCE OAuth, encrypted HttpOnly session
cookies, CSRF checks and a user-bound history API. Supabase RLS, not a client user ID,
protects private results; no service-role key or auth token is sent to browser JS.
Google provider credentials still require owner dashboard setup. GitHub Pages remains
static and points its login link to the Vercel site rather than sharing cross-site cookies.

`npm run build` creates ignored, allowlisted `public/` plus `.vercel/output/`; only
public assets are shipped, not maintainer/tools/server source/metadata/.env files.
Build-time minification and Brotli 11/gzip 9 reduce text payloads; existing PDF/image
quality is preserved. No claim of a universally fastest language or lifetime hosting.

Owner setup, exact callback URLs, upload metadata example, retention, deployment
permission limits and security tests: [AUTH_AND_PRACTICE.md](maintainer/AUTH_AND_PRACTICE.md).
