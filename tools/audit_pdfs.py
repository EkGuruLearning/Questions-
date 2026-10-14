#!/usr/bin/env python3
"""Read-only PDF integrity and page-render smoke audit for Git-tracked PDFs.

PyMuPDF is an optional QA dependency. The script never writes to or replaces a
source PDF; only its JSON report and ignored PNG previews are written.
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import subprocess
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPORT = ROOT / "maintainer/reports/pdf_rendering_qa.json"
PREVIEW_DIR = ROOT / ".arena/pdf-qa/previews"
OPTIONAL_PACKAGES = ROOT / ".arena/pdf-qa/packages"
if OPTIONAL_PACKAGES.is_dir():
    sys.path.insert(0, str(OPTIONAL_PACKAGES))

try:
    import pymupdf
except ImportError:
    print("SKIP: PyMuPDF is unavailable; install it under .arena/pdf-qa/packages to run this optional read-only check.")
    raise SystemExit(77)


def tracked_pdfs() -> list[str]:
    output = subprocess.run(
        ["git", "ls-files", "-z", "--", "*.pdf"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    return sorted(item.decode("utf-8") for item in output.split(b"\0") if item)


def file_digest(path: pathlib.Path) -> tuple[int, str]:
    value = hashlib.sha256()
    size = 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            size += len(chunk)
            value.update(chunk)
    return size, value.hexdigest()


def render_scale(page, limit: float) -> float:
    rect = page.rect
    largest = max(float(rect.width), float(rect.height), 1.0)
    return min(limit, 1200.0 / largest)


def preview_name(index: int, relative: str, page_number: int) -> str:
    name_hash = hashlib.sha256(relative.encode("utf-8")).hexdigest()[:10]
    stem = pathlib.Path(relative).stem[:32]
    safe_stem = "".join(character if character.isalnum() or character in "-_" else "_" for character in stem)
    return f"{index:02d}_{safe_stem}_{name_hash}_page-{page_number:04d}.png"


def audit_one(index: int, relative: str, original_size: int, original_sha: str) -> dict:
    path = ROOT / relative
    result = {
        "path": relative,
        "size_bytes": original_size,
        "sha256_before": original_sha,
        "page_count": 0,
        "pages_rendered": 0,
        "samples": [],
        "repaired_by_mupdf": False,
        "warnings": [],
        "errors": [],
        "status": "FAIL",
    }
    document = None
    try:
        document = pymupdf.open(path.as_posix())
        if document.needs_pass:
            authenticated = document.authenticate("")
            if not authenticated or document.needs_pass:
                raise RuntimeError("encrypted PDF requires a password; pages could not be validated")
        page_count = document.page_count
        result["page_count"] = page_count
        result["repaired_by_mupdf"] = bool(document.is_repaired)
        if document.is_repaired:
            result["warnings"].append("MuPDF repaired PDF structure while opening; inspect original separately if strict conformance is required.")
        if page_count < 1:
            raise RuntimeError("PDF contains no pages")

        sample_indices = sorted({0, page_count // 2, page_count - 1})
        for page_index in range(page_count):
            page = document.load_page(page_index)
            rect = page.rect
            if rect.width <= 0 or rect.height <= 0:
                raise RuntimeError(f"page {page_index + 1} has a non-positive page size ({rect.width}×{rect.height})")
            scale = render_scale(page, 1.0 if page_index in sample_indices else 0.45)
            pixmap = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=False, annots=True)
            if pixmap.width <= 0 or pixmap.height <= 0 or pixmap.samples_mv.nbytes == 0:
                raise RuntimeError(f"page {page_index + 1} produced an empty render")
            result["pages_rendered"] += 1
            if page_index in sample_indices:
                PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
                filename = preview_name(index, relative, page_index + 1)
                preview_path = PREVIEW_DIR / filename
                pixmap.save(preview_path.as_posix())
                result["samples"].append({
                    "page_number": page_index + 1,
                    "render_width_px": pixmap.width,
                    "render_height_px": pixmap.height,
                    "scale": round(scale, 4),
                })
            del pixmap

        if result["pages_rendered"] != page_count:
            raise RuntimeError(f"rendered {result['pages_rendered']} of {page_count} pages")
        result["status"] = "PASS_WITH_WARNINGS" if result["warnings"] else "PASS"
    except Exception as error:  # keep auditing subsequent PDFs after one failure
        result["errors"].append(f"{type(error).__name__}: {error}")
    finally:
        if document is not None:
            document.close()
    return result


def main() -> int:
    pdfs = tracked_pdfs()
    if not pdfs:
        print("FAIL: no Git-tracked PDFs were found.")
        return 1

    before = {}
    for relative in pdfs:
        before[relative] = file_digest(ROOT / relative)

    files = [audit_one(index, relative, *before[relative]) for index, relative in enumerate(pdfs, start=1)]

    after = {}
    for relative in pdfs:
        after[relative] = file_digest(ROOT / relative)
    unchanged = all(before[relative] == after[relative] for relative in pdfs)
    for item in files:
        size_after, sha_after = after[item["path"]]
        item["size_unchanged"] = size_after == item["size_bytes"]
        item["sha256_after"] = sha_after
        item["sha256_unchanged"] = sha_after == item["sha256_before"]
        if not item["sha256_unchanged"]:
            item["errors"].append("source PDF changed during read-only audit")
            item["status"] = "FAIL"

    total_pages = sum(item["page_count"] for item in files)
    total_rendered = sum(item["pages_rendered"] for item in files)
    failures = [item for item in files if item["status"] == "FAIL"]
    repaired_count = sum(item["repaired_by_mupdf"] for item in files)
    warning_count = sum(bool(item["warnings"]) for item in files)
    overall = "FAIL" if failures or not unchanged else "PASS_WITH_WARNINGS" if warning_count else "PASS"
    report = {
        "schema_version": 1,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "status": overall,
        "tool": f"PyMuPDF {pymupdf.VersionBind}",
        "scope": "Git-tracked PDFs; page-tree load and raster render of every page; first, middle and last page previews per file.",
        "rendering": "Every page rendered to an in-memory RGB pixmap (max 1200 px dimension for page samples; 0.45 scale for others). This checks parsing/renderability, not document content, answer correctness, print quality, or archival PDF/A conformance.",
        "tracked_pdf_count": len(pdfs),
        "total_source_bytes": sum(item["size_bytes"] for item in files),
        "total_pages": total_pages,
        "total_pages_rendered": total_rendered,
        "all_source_hashes_unchanged": unchanged,
        "mupdf_repaired_files": repaired_count,
        "files_with_warnings": warning_count,
        "failed_files": len(failures),
        "files": files,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"{overall}: PDFs={len(pdfs)}, pages={total_pages}, rendered={total_rendered}, "
        f"repaired={repaired_count}, failures={len(failures)}, unchanged={unchanged}; report={REPORT.relative_to(ROOT)}"
    )
    for item in files:
        if item["status"] != "PASS":
            print(f"{item['status']}: {item['path']} — {'; '.join(item['errors'] + item['warnings'])}")
    return 1 if overall == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
