# -*- coding: utf-8 -*-
"""
cn_ocr_cache.py — OCR scanned source PDFs into cached text files.

For each PDF: OCR every page (RapidOCR), write per-page cache under
tools/data/ocr_text/<stem>/page_NNN.txt and a combined <stem>.txt with
'--- page N ---' markers. Idempotent: pages already cached are skipped,
so an interrupted run can be re-run safely.

Usage:
    /home/user/pdfenv/bin/python tools/cn_ocr_cache.py <pdf> [<pdf> ...]
    /home/user/pdfenv/bin/python tools/cn_ocr_cache.py --all-missing
"""
import os
import sys
import glob
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OCR_DIR = os.path.join(REPO, "tools", "data", "ocr_text")
SRC_DIR = os.path.join(REPO, "content", "computer-network", "tests")

# image-only source PDFs (no text layer) that must be OCR'd
SCANNED = [
    "Random-Test-Rajasthan-PYQ.pdf",
    "Subject-Test-01-CN-Security-Solutions.pdf",
    "Subject-Test-01-CN-Security-Solutions-Part-2.pdf",
    "Unit-Test-02-Solutions.pdf",
    "Unit-Test-04-Solutions.pdf",
]


def stem_of(pdf_path):
    return os.path.splitext(os.path.basename(pdf_path))[0]


def ocr_pdf(pdf_path, dpi=180):
    import fitz
    from rapidocr_onnxruntime import RapidOCR

    stem = stem_of(pdf_path)
    page_dir = os.path.join(OCR_DIR, stem)
    os.makedirs(page_dir, exist_ok=True)

    engine = RapidOCR()
    doc = fitz.open(pdf_path)
    n = len(doc)
    t0 = time.time()
    for i in range(n):
        cache = os.path.join(page_dir, "page_%03d.txt" % (i + 1))
        if os.path.exists(cache):
            continue
        pix = doc[i].get_pixmap(dpi=dpi)
        res, _ = engine(pix.tobytes("png"))
        text = "\n".join(r[1] for r in res) if res else ""
        with open(cache, "w", encoding="utf-8") as f:
            f.write(text)
        print("  %s: page %d/%d done (%.1fs)" % (stem[:30], i + 1, n, time.time() - t0), flush=True)
    doc.close()

    # combined file with page markers
    combined = os.path.join(OCR_DIR, stem + ".txt")
    with open(combined, "w", encoding="utf-8") as out:
        for i in range(n):
            cache = os.path.join(page_dir, "page_%03d.txt" % (i + 1))
            out.write("\n--- page %d ---\n" % (i + 1))
            with open(cache, encoding="utf-8") as f:
                out.write(f.read())
    print("  %s: COMBINED -> %s (%.1fs)" % (stem[:30], combined, time.time() - t0), flush=True)
    return combined


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    if args[0] == "--all-missing":
        pdfs = []
        for name in SCANNED:
            p = os.path.join(SRC_DIR, name)
            if os.path.exists(p):
                pdfs.append(p)
            else:
                # fall back to git-show extraction is caller's job; try /tmp
                alt = os.path.join("/tmp/ekguru-cn", name)
                if os.path.exists(alt):
                    pdfs.append(alt)
                else:
                    print("[warn] missing:", name)
    else:
        pdfs = args
    for p in pdfs:
        print("[ocr] %s" % p, flush=True)
        ocr_pdf(p)
    print("[done] all OCR complete", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
