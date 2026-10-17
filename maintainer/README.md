# maintainer/ — website par publish nahi hota

Yahan wo sab hai jo student ko nahi dikhana hai, lekin repository me rakhna zaroori hai.
`tools/validate_site.py` check karta hai ki koi bhi public page is folder par link na kare.

| Folder | Kya hai |
|---|---|
| `maintainer/computer-network/reports/` | Bank inventory, answer-verification, duplicate audit, release notes, W6 import log |
| `maintainer/computer-network/intake/` | Naye question-source PDFs ke liye staging (`tools/cn_pipeline.py` yahin se padhta hai) |
| `maintainer/computer-network/sources/web-banks/` | Web se aaye compressed question banks + drop READMEs (ingest source) |
| `maintainer/computer-network/theory-md/` | Theory booklets ke editable Markdown (PDF `content/` me jata hai) |
| `maintainer/computer-network/legacy-apps/` | Purane standalone quiz HTML + v6 launchers (retired) |
| `maintainer/computer-network/past-papers/` | RPSC Programmer 2024 paper, source notes, question banks, syllabus |
| `maintainer/computer-network/docs/` | Purane CN notes (COVERAGE, topic-folder README) |
| `maintainer/rajasthan-geography/atlas-project/` | GIS project (`qgz`), render/review scripts, CSVs, fonts, atlas audits |
| `maintainer/rajasthan-geography/input-audit/` | Purana `Geography/Map/Rajasthan/` audit tree (reference upload + audits) |
| `maintainer/reports/` | Generated reports: release checks, duplicate audit, PDF rendering QA |
| `maintainer/catalog-inputs/` | Retired portal catalogue inputs (`books.json`, `exams.json`, `syllabus_mappings.json`, …) |
| `maintainer/releases/` | Purane release zip |
| `maintainer/archive/` | Purane snapshots (`pre-audit-2026-10-14`) — bytes kabhi edit nahi karte |
| `maintainer/AUTH_AND_PRACTICE.md` | Google OAuth activation, Test Room paper/key uploads, privacy, free-tier and deployment notes |
| `maintainer/COVERAGE.md` | Purana coverage note |

Ye files waise hi rakhi gayi hain jaisi thin — na rename, na rewrite. Sirf unka *location* badla hai
taaki website sirf student material serve kare.
