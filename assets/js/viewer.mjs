/* Same-origin, self-hosted reader. Never proxy arbitrary external URLs. */
const ROOT = new URL('../../', import.meta.url);
const $ = (id) => document.getElementById(id);
let pdf, pageNumber = 1, zoom = 1, image, rendering = false;
let pendingRender = false;
const status = (text) => { $('readerStatus').textContent = text; };

function controls() {
  $('pageLabel').textContent = pdf ? `${pageNumber} / ${pdf.numPages}` : 'Map / image';
  $('readerPrev').disabled = !pdf || pageNumber <= 1;
  $('readerNext').disabled = !pdf || pageNumber >= pdf.numPages;
  $('zoomLabel').textContent = `${Math.round(zoom * 100)}%`;
}

async function render() {
  if (rendering) { pendingRender = true; return; }
  rendering = true;
  controls();
  status('Page load ho raha hai…');
  try {
    if (pdf) {
      const page = await pdf.getPage(pageNumber);
      const base = page.getViewport({ scale: 1 });
      const available = Math.max(240, $('readerStage').clientWidth - 24);
      const viewport = page.getViewport({ scale: (available / base.width) * zoom });
      // Keep large maps within phone memory limits, regardless of device DPI.
      const ratio = Math.min(window.devicePixelRatio || 1, 2, Math.sqrt(8000000 / (viewport.width * viewport.height)));
      const canvas = $('pdfCanvas');
      canvas.width = Math.floor(viewport.width * ratio);
      canvas.height = Math.floor(viewport.height * ratio);
      canvas.style.width = `${viewport.width}px`;
      canvas.style.height = `${viewport.height}px`;
      canvas.hidden = false;
      await page.render({ canvasContext: canvas.getContext('2d'), viewport, transform: [ratio, 0, 0, ratio, 0, 0] }).promise;
      page.cleanup();
    } else if (image) {
      image.style.width = `${zoom * 100}%`;
      image.style.maxWidth = 'none';
    }
    status('Ready · Zoom + / − se bada karein; badi page ko swipe karke padhein.');
  } catch (error) {
    status('Page nahi khula. Neeche “Original file” ya “Download” use karein.');
  } finally {
    rendering = false;
    if (pendingRender) { pendingRender = false; render(); }
  }
}

async function init() {
  try {
    const file = new URLSearchParams(location.search).get('file');
    if (!file) throw new Error('Pehle subject folder se PDF ya map choose karein.');
    const url = new URL(file, ROOT);
    const contentRoot = new URL('content/', ROOT);
    const decoded = decodeURIComponent(url.pathname);
    if (url.origin !== ROOT.origin || !decoded.startsWith(contentRoot.pathname) || /[\\\u0000-\u001f]/.test(decoded) || url.search || url.hash) {
      throw new Error('Sirf is website ki content files yahan khul sakti hain.');
    }
    const isPDF = /\.pdf$/i.test(decoded);
    if (!isPDF && !/\.(png|jpe?g|webp)$/i.test(decoded)) throw new Error('Yeh file format supported nahi hai.');
    const name = decoded.split('/').pop().replace(/[-_]/g, ' ');
    $('readerTitle').textContent = name;
    document.title = `${name} — EkGuru Reader`;
    $('originalFile').href = url.href;
    $('downloadFile').href = url.href;
    $('downloadFile').setAttribute('download', decoded.split('/').pop());
    $('fileActions').hidden = false;
    $('readerTools').hidden = false;
    $('readerRetry').hidden = false;
    if (isPDF) {
      const pdfjs = await import('../vendor/pdfjs/pdf.min.mjs');
      pdfjs.GlobalWorkerOptions.workerSrc = new URL('../vendor/pdfjs/pdf.worker.min.mjs', import.meta.url).href;
      const task = pdfjs.getDocument({
        url: url.href,
        cMapUrl: new URL('../vendor/pdfjs/cmaps/', import.meta.url).href,
        cMapPacked: true,
        standardFontDataUrl: new URL('../vendor/pdfjs/standard_fonts/', import.meta.url).href,
        isEvalSupported: false,
      });
      task.onProgress = ({ loaded, total }) => { if (!pdf) status(total ? `PDF load ho raha hai… ${Math.min(100, Math.round(loaded / total * 100))}%` : 'PDF load ho raha hai…'); };
      const timeout = setTimeout(() => status('File badi hai ya internet slow hai. Aap Original file / Download bhi use kar sakte hain.'), 20000);
      try { pdf = await task.promise; } finally { clearTimeout(timeout); }
    } else {
      image = new Image();
      image.alt = name;
      image.className = 'reader-image';
      await new Promise((resolve, reject) => {
        image.onload = resolve;
        image.onerror = () => reject(new Error('Map load nahi hua. Download ya Retry use karein.'));
        image.src = url.href;
      });
      $('readerStage').appendChild(image);
    }
    await render();
  } catch (error) {
    status(`${error.message} Original file / Download available ho to use karein.`);
  }
}

$('readerPrev').addEventListener('click', () => { if (pdf && pageNumber > 1) { pageNumber--; render(); } });
$('readerNext').addEventListener('click', () => { if (pdf && pageNumber < pdf.numPages) { pageNumber++; render(); } });
$('readerZoomIn').addEventListener('click', () => { zoom = Math.min(3, zoom + 0.25); render(); });
$('readerZoomOut').addEventListener('click', () => { zoom = Math.max(0.5, zoom - 0.25); render(); });
$('readerFit').addEventListener('click', () => { zoom = 1; render(); });
$('readerRetry').addEventListener('click', () => location.reload());
let resizeTimer;
window.addEventListener('resize', () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(() => { if (pdf || image) render(); }, 200); });
init();
