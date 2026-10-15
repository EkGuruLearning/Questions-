# tools/ — builders, validators aur bank pipeline

## Website build + checks (yeh rozana kaam ke hain)

| Command | Kaam |
|---|---|
| `python3 tools/build_site_data.py` | Canonical bank → `data/banks/cn/manifest.json` + topic chunks. `--check` verify karta hai |
| `python3 tools/build_thumbs.py` | Picture files ke halke preview (`data/thumbs/`) → website thumbnails. `--check` verify karta hai. Naya picture add karne par ImageMagick chahiye |
| `python3 tools/build_catalog.py` | Catalogue inputs + previews + chunks → `data/site.json` (alt/description = image SEO). `--check` verify karta hai |
| `python3 tools/build_pages.py` | `data/site.json` + `data/catalog/previous-year-papers.json` → plain HTML pages, year-wise exam source pages and the Rajasthan map PDF preview. `--check` verify karta hai |
| `python3 tools/build_site_routes.py` | HTML files se `data/catalog/site-routes.txt` likhta hai. `--check` verify karta hai |
| `python3 tools/validate_site.py` | Routes, links, anchors, `.md`/maintainer leak, download hashes, `?folder=` links, preview files |
| `python3 tools/validate_question_bank.py` | Bank schema v2, evidence gate, chunk coverage |
| `python3 tools/read_structure.py` | Structure ka map; `--check` par poora preflight |
| `python3 tools/run_release_checks.py` | Saare checks ek saath + `maintainer/reports/release_checks.json` |
| `python3 tools/check_whitespace.py` | Badli hui text files me trailing whitespace |
| `python3 tools/reasoning_samples.py [--check]` | Reasoning ke sample chapter/practice/test/answer-key PDFs banao (source: `maintainer/reasoning/samples/`) |
| `python3 tools/new_reasoning_chapter.py "Calendar"` | Naye Reasoning chapter ke chaaron folder ek command me (upload ke liye) |
| `python3 tools/scaffold_exam_years.py [--check\|--prune]` | Previous Year Papers me har exam ke 2000–2026 saal folders |
| `node tests/mobile/mobile_check.cjs` | Asli browser me phone/tablet/desktop widths — overflow, nav, tap targets, console errors (browser na ho to skip 77) |

## Question bank pipeline (source → site)

| Command | Kaam |
|---|---|
| `python3 tools/cn_export_json.py` | Sari topic modules → canonical bank → chunks → `data/site.json` |
| `python3 tools/cn_build_topic.py [N\|--all]` | Topic theory PDF (`content/.../theory/`) + Markdown source (`maintainer/.../theory-md/`) |
| `python3 tools/cn_build_practice.py` | Topic practice booklet PDFs |
| `python3 tools/cn_build_complete.py` | Complete book PDF |
| `python3 tools/cn_build_verify_key.py` | Added-questions answer key PDF |
| `python3 tools/cn_pipeline.py` | Naye source PDF → review queue (intake: `maintainer/computer-network/intake/`) |
| `python3 tools/audit_duplicates.py --check` | Exact + near duplicate scan (report → `maintainer/`) |
| `python3 tools/audit_pdfs.py` | Har PDF parse/render check (PyMuPDF chahiye; warna exit 77) |

## Helper modules

`cn_engine.py` (PDF/Markdown layout), `cn_taxonomy.py` (7-topic system), `cn_textfix.py`
(normalization), `cn_difficulty.py` (heuristic difficulty), `cn_extract.py`, `cn_ingest_web.py`,
`cn_parse_ocr.py`, `cn_parse_cnp3.py`, `cn_ocr_cache.py`, `import_w6_build.py`, `reconcile_cn_bank.py`.

Question data modules `tools/data/topicN_data.py` (curated) aur `tools/data/*_pN.py` (import waves)
me hain — bank yahin se banta hai. Kuch bhi generate karne ke baad `data/site.json` rebuild karna
mat bhoolna:

```bash
python3 tools/cn_export_json.py && python3 tools/read_structure.py --check
```
