# 🖧 Data Communication & Computer Networks (CN) — 7 Topic-wise MCQ PDFs

Exam-ready, **bilingual (English + Hindi)** MCQ books for Rajasthan Govt. exams, built
from the repo's real exam papers + Forouzan. Reference book: **Behrouz A. Forouzan —
*Data Communications and Networking***.

**Serves:** RPSC Programmer • RSMSSB Informatics Assistant (IA) • School Administrator (SA) •
Data Entry / Computer Operator (DD) • **BCI** (Basic Computer Instructor) • **SCI** (Senior
Computer Instructor) • REET (Computer) • RAS & other Rajasthan Govt. exams.

---

## 📘 The 7 Topics (deliverable PDF + Markdown each)

| # | Topic | Sub-topics covered |
|---|-------|--------------------|
| 1 | **Introduction of DC** | DC components (Message/Sender/Receiver/Medium/Protocol); characteristics (Delivery/Accuracy/Timeliness/Jitter); criteria (Performance/Reliability/Security); transmission modes (Simplex/Half/Full-Duplex); topology (Mesh/Star/Bus/Ring/Hybrid/Tree, logical IEEE 802); network types (LAN/MAN/WAN/PAN/CAN/SAN, Internet/Intranet/Extranet, Point-to-Point/Multipoint, Client-Server/P2P); history (ARPANET→today); general basics (WWW/E-mail/switching) |
| 2 | **Network Models** | OSI model (1984, 7 layers); TCP/IP model (1972, 4/5 layers); comparison; encapsulation/PDU; layer functions & protocols |
| 3 | **Addressing** | MAC (48-bit); IPv4 (32-bit, classes, private IP); subnetting & CIDR; IPv6 (128-bit); port (16-bit); DNS/URL |
| 4 | **Networking Devices** | Hub/Repeater/Modem; Switch/NIC/Bridge; Router/Brouter; Gateway/Firewall; layer & collision/broadcast domains |
| 5 | **Transmission Medium** | Guided (twisted pair/coax/fiber); Unguided (radio/microwave/infrared); signals, attenuation/distortion/noise, bandwidth/throughput/Shannon |
| 6 | **OSI Layers in Detail** | Physical; Data Link (flow control Stop-and-Wait/Go-Back-N/Selective Repeat, error control Parity/Checksum/CRC/Hamming, framing, MAC ALOHA/CSMA/CD/CSMA/CA); Network (IPv4/IPv6 headers, RIP/OSPF/BGP, ICMP/ARP/RARP/DHCP); Transport (TCP/UDP/SCTP); Session; Presentation; Application (HTTP/HTTPS, SMTP/POP/IMAP/MIME, FTP/TELNET, DNS) |
| 7 | **Network Security** | Cryptography (symmetric/asymmetric, digital signature); IDS/IPS/Firewall/VPN; IPSec (transport/tunnel), SSL/TLS, PGP, WPA2 |

Each output file: `Topic N - <name> - <count> MCQs (Answers + Nukte).pdf` (+ `.md` source).

## ✅ What every question contains

- **4 options (A–D)** in English + Hindi
- **✔ Correct answer** + why it is right (EN + HI)
- **★ Nukta** — the key exam point / memory tip (EN + HI)
- **✖ Option-wise verification** — why each wrong option is wrong (EN + HI)
- a grey **source tag** (which paper/book it came from)
- Answers **cross-verified 4×** and matched against official answer keys (Subject Test /
  Unit Test Solutions) where available.

---

## ⚙️ The Auto-Update System (add questions by dropping a PDF)

The whole bank is generated from data files by small tools in `tools/`. To add **any** new
question PDF in future (e.g. an RSSB/RPSC previous paper), just **drop it into
`Computer Network/Incoming/`** and run two commands — new questions are automatically
extracted, **classified into the right topic by content**, de-duplicated, and merged:

```bash
# 1) ingest everything in Incoming/  (or: --pdf path/to/file.pdf , --dir some/folder)
python tools/cn_pipeline.py ingest

# 2) rebuild the affected topic PDF(s)+MD
python tools/cn_pipeline.py rebuild --all          # or: rebuild 2   (just Topic 2)

python tools/cn_pipeline.py status                 # see pending counts per topic
```

New questions first land in `tools/data/topicN_pending.py` and appear in the topic PDF
under a clearly-marked **"Pending Review — needs verification"** section (so nothing is
lost). Verify them (answer + nukta + Hindi + option-verification) and move them into
`tools/data/topicN_data.py` (the curated, verified bank shown in the main body), then
rebuild. `tools/cn_build_topic.py <N>` builds a single topic; `--all` builds all.

### How it works
- `tools/cn_taxonomy.py` — the 7 topics, sub-topics, keywords, exam list, and the
  **content-based classifier** (`classify()`). Repo PDF page headers are unreliable, so
  classification is by content only.
- `tools/cn_extract.py` — pulls clean English MCQs from a PDF (pymupdf text; **RapidOCR**
  fallback for scanned PDFs). Drops the garbled Hindi (re-authored later) and the
  copy-pasted headers/footers.
- `tools/cn_pipeline.py` — extract → classify → **de-duplicate** → merge into pending →
  rebuild. (The auto-update engine.)
- `tools/cn_engine.py` — renders a topic's data into the bilingual PDF (PyMuPDF Story →
  MuPDF/HarfBuzz gives **correct Devanagari shaping**; fonts embedded once) + Markdown.
  Custom pagination guarantees **no question is ever split** across pages and nothing
  touches the footer.
- `tools/cn_build_topic.py` — builds one (or all) topic PDF+MD from `tools/data/topicN_data.py`.
- `tools/data/topicN_data.py` — curated, verified questions (source of truth, main body).
- `tools/data/topicN_pending.py` — auto-ingested, not-yet-verified questions (Pending Review).
- `tools/fonts/` — embedded fonts (Noto Sans Devanagari + DejaVu Sans, OFL).

### Requirements
Python 3 with `pymupdf` (and `rapidocr-onnxruntime` + `opencv-python-headless` for OCR of
scanned PDFs). Fonts are bundled in `tools/fonts/`.

---

## 📚 Source papers

See **`Past Papers/SOURCES.md`** — the 15 Rajasthan exam PDFs shipped in this repo (the
primary question source, with official answer keys) + the RPSC Programmer solved-papers
reference. All content is curated from these; nothing is invented.

## 📂 Folder layout

```
Computer Network/
  Topic N - ....pdf / .md        # the 7 deliverable topic books (generated)
  <15 source exam PDFs>          # original question papers (from main branch)
  Past Papers/                   # SOURCES.md + extra trusted sources
  Incoming/                      # DROP new question PDFs here
tools/
  cn_taxonomy.py  cn_extract.py  cn_pipeline.py  cn_engine.py  cn_build_topic.py
  data/topicN_data.py  topicN_pending.py
  fonts/                         # bundled fonts
```
