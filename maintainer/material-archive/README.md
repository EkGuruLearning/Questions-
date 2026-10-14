# Material Archive — future subjects ke liye source store

Yeh archive isliye hai taaki **DBMS, SAD (System Analysis & Design), Java** aur baaki
core subjects ki books bhi bilkul CN jaisi (topic-wise, bilingual, PYQ-loaded) banein —
saara research material yahin store rehta hai, dobara dhoondna nahi padega.

## Kya-kya store hai

| Path | Kya hai |
|------|---------|
| `CN/pyq_adds_wave1.py` | Wave-1 PYQ entries (45 items, 2011–2026 India-level exams) — book data mein merged |
| `CN/pyq_adds_wave2.py` | Wave-2 PYQ entries (29 items: GATE 2011–2026 full sweep, KVS 2017, EMRS) + verified computations |
| `CN/research_notes.md` | Har source ka URL + takeaway + drop list (kya mila, kya chhoda aur kyun) |
| `DBMS/SOURCES.md` | DBMS ke liye verified source registry (banks, papers, textbooks) |
| `SAD/SOURCES.md` | SAD ke liye source registry |
| `Java/SOURCES.md` | Java ke liye source registry |
| `../Past Papers/` | Repo ki asli question-paper PDFs + Forouzan + cnp3 banks (canonical store) |
| `../tools/data/` | Canonical book data (`topic*_data.py`, `answer_keys.py`, `web_pyq_raw.py`) |

## Workflow (har subject ke liye same)

1. Papers/PYQs `Incoming/` ya is archive mein lao (`tools/cn_pipeline.py` ingest karta hai).
2. Sirf **sourced** questions (koi self-generated nahi) — complete items (Q + 4 options +
   verified key), dedupe mandatory (koi repeat nahi).
3. `tools/cn_engine.py` (v2 renderer) + `cn_build_topic.py` — bilingual EN+HI,
   side-by-side layout (why-correct + nukte), PyMuPDF Story.
4. Section order = syllabus; andar **Easy → Medium → Hard** (`tools/cn_difficulty.py`).
5. Books `Computer Network/` jaisi naming: `Topic N - … - X MCQs (Answers + Nukte).pdf/.md`.
6. Har drop/merge `COVERAGE.md` mein documented.

## Difficulty convention (user spec)

- **Easy** — SSC MTS/CHSL, REET, SCI, BCI, TCS/Wipro/Infosys (easy se medium)
- **Medium** — Forouzan, cnp3, SSC CGL, RRB, RSMSSB, HTET, IBPS/SBI, NIELIT, unit tests
- **Hard** — GATE, UGC NET, KVS, EMRS, DSSSB, JNV TAT, RPSC Programmer, PGT, Lecturer, UPSC

## Roadmap

- **Abhi:** Computer Network (done — 631 MCQs, 7 books)
- **Agle 2 din:** DBMS, SAD, Java (+ jitne main core subjects) — same pipeline
