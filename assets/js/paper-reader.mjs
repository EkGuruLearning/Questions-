/* Lazy PDF.js canvas reader. Only one page is rendered; old tasks are destroyed.
   Paper URLs must come from the local public manifest, never arbitrary proxies. */
const ROOT = new URL("../../", import.meta.url);
const $ = (id) => document.getElementById(id);

export class PaperReader {
  constructor(onPage = () => {}) {
    this.onPage = onPage;
    this.generation = 0; this.pdf = null; this.task = null; this.page = 1; this.zoom = 1;
    this.rendering = false; this.pending = false; this.renderTask = null;
    this.cleanup = Promise.resolve();
    $("roomPagePrev").addEventListener("click", () => this.go(this.page - 1));
    $("roomPageNext").addEventListener("click", () => this.go(this.page + 1));
    $("roomPageNumber").addEventListener("change", () => this.go(Number($("roomPageNumber").value)));
    $("roomZoomIn").addEventListener("click", () => { this.zoom = Math.min(3, this.zoom + 0.25); this.render(); });
    $("roomZoomOut").addEventListener("click", () => { this.zoom = Math.max(0.5, this.zoom - 0.25); this.render(); });
    let resize;
    window.addEventListener("resize", () => { clearTimeout(resize); resize = setTimeout(() => { if (this.pdf) this.render(); }, 200); });
  }
  status(text) { $("roomPdfStatus").textContent = text; }
  controls() {
    $("roomPagePrev").disabled = !this.pdf || this.page <= 1;
    $("roomPageNext").disabled = !this.pdf || this.page >= this.pdf.numPages;
    $("roomPageNumber").value = this.page;
    $("roomPageNumber").max = this.pdf?.numPages || 1;
    $("roomPageNumber").disabled = !this.pdf;
    $("roomPageCount").textContent = `/ ${this.pdf?.numPages || "…"}`;
  }
  go(number) {
    if (!this.pdf || !Number.isFinite(number)) return;
    this.page = Math.max(1, Math.min(this.pdf.numPages, Math.floor(number)));
    this.onPage(this.page); this.render();
  }
  close() {
    this.generation += 1;
    this.renderTask?.cancel(); this.renderTask = null;
    if (this.task) {
      const task = this.task;
      this.cleanup = this.cleanup.then(() => task.destroy()).catch(() => {});
    }
    this.task = null; this.pdf = null; this.pending = false;
    $("roomCanvas").width = 1; $("roomCanvas").height = 1;
    this.controls();
    return this.cleanup;
  }
  async open(paper, initialPage = 1) {
    const cleanup = this.close();
    const generation = this.generation;
    this.page = initialPage; this.zoom = 1;
    this.status("PDF load ho rahi hai…"); $("retryPaperPdf").hidden = true;
    const url = new URL(paper.pdf.split("/").map(encodeURIComponent).join("/"), ROOT);
    const content = new URL("content/previous-year-papers/", ROOT);
    if (url.origin !== ROOT.origin || !decodeURIComponent(url.pathname).startsWith(content.pathname)
        || !/\.pdf$/i.test(url.pathname) || url.search || url.hash) throw new Error("Invalid local paper URL");
    $("roomOriginal").href = url.href;
    const slow = setTimeout(() => {
      if (generation !== this.generation) return;
      this.status("PDF badi hai ya internet slow hai. Retry ya Original PDF khol sakte hain; answer sheet kaam karti rahegi.");
      $("retryPaperPdf").hidden = false;
    }, 20000);
    try {
      await cleanup;
      if (generation !== this.generation) return;
      const pdfjs = await import("../vendor/pdfjs/pdf.min.mjs");
      if (generation !== this.generation) return;
      pdfjs.GlobalWorkerOptions.workerSrc = new URL("../vendor/pdfjs/pdf.worker.min.mjs", import.meta.url).href;
      const task = pdfjs.getDocument({ url: url.href, isEvalSupported: false,
        cMapUrl: new URL("../vendor/pdfjs/cmaps/", import.meta.url).href, cMapPacked: true,
        standardFontDataUrl: new URL("../vendor/pdfjs/standard_fonts/", import.meta.url).href });
      this.task = task;
      task.onProgress = ({ loaded, total }) => {
        if (generation === this.generation && !this.pdf) this.status(total ? `PDF loading… ${Math.min(100, Math.round(loaded / total * 100))}%` : "PDF loading…");
      };
      const pdf = await task.promise;
      if (generation !== this.generation) return;
      this.pdf = pdf; this.page = Math.max(1, Math.min(pdf.numPages, initialPage));
      await this.render();
    } catch {
      if (generation !== this.generation) return;
      this.status("PDF abhi nahi khuli. Retry karein ya Original PDF ko alag tab mein padhein; answer sheet kaam karti rahegi.");
      $("retryPaperPdf").hidden = false;
    } finally { clearTimeout(slow); }
    this.controls();
  }
  async render() {
    if (!this.pdf) return;
    if (this.rendering) { this.pending = true; return; }
    this.rendering = true;
    const generation = this.generation;
    this.controls();
    try {
      const page = await this.pdf.getPage(this.page);
      if (generation !== this.generation) return;
      const base = page.getViewport({ scale: 1 });
      const available = Math.max(240, $("roomCanvasWrap").clientWidth - 16);
      const viewport = page.getViewport({ scale: available / base.width * this.zoom });
      const ratio = Math.min(window.devicePixelRatio || 1, 2, Math.sqrt(6000000 / (viewport.width * viewport.height)));
      const canvas = $("roomCanvas");
      canvas.width = Math.floor(viewport.width * ratio); canvas.height = Math.floor(viewport.height * ratio);
      canvas.style.width = `${viewport.width}px`; canvas.style.height = `${viewport.height}px`;
      canvas.setAttribute("aria-label", `Question paper PDF page ${this.page} of ${this.pdf.numPages}`);
      this.renderTask = page.render({ canvasContext: canvas.getContext("2d"), viewport, transform: [ratio, 0, 0, ratio, 0, 0] });
      await this.renderTask.promise;
      page.cleanup();
      if (generation === this.generation) {
        this.status(`Page ${this.page} ready · ${Math.round(this.zoom * 100)}% zoom · Swipe to read zoomed pages.`);
        $("retryPaperPdf").hidden = true;
      }
    } catch (error) {
      if (generation === this.generation && error.name !== "RenderingCancelledException") {
        this.status("Page render nahi hui. Retry ya Original PDF link use kar sakte hain.");
        $("retryPaperPdf").hidden = false;
      }
    } finally {
      this.renderTask = null; this.rendering = false;
      if (this.pending && this.pdf) { this.pending = false; this.render(); }
    }
  }
}
