/* Progressive enhancement only. Reading and guest practice never require auth.
   All auth is same-origin; JS sees a safe user summary, never session tokens. */
const ROOT = new URL("../../", import.meta.url);
const ACCOUNT = "/subjects/account/index.html";
const $all = (selector) => document.querySelectorAll(selector);
const outboxKey = (id) => `ekguru.outbox.v1.${id}`;
const messages = {
  google_setup_required: "Google login ka provider setup abhi pending hai. Guest practice bilkul chalti hai.",
  login_expired: "Login link expire/cancel hua. Dobara Google se login karein.",
  login_failed: "Login complete nahi hua. Cookies allow karke dobara try karein.",
};

const volatile = new Map();
function localRead(key, fallback) {
  if (volatile.has(key)) return volatile.get(key);
  try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; }
}
function localWrite(key, value) {
  volatile.set(key, value);
  try { localStorage.setItem(key, JSON.stringify(value)); volatile.delete(key); } catch { /* memory outbox still syncs while this tab is open */ }
}

const account = { user: null, configured: false, google_enabled: false, remote: false, origin: location.origin, ready: null };
window.EkGuruAccount = account;

export async function api(path, { method = "GET", body } = {}) {
  const response = await fetch(path, { method, credentials: "same-origin", cache: "no-store",
    signal: AbortSignal.timeout(12000),
    headers: { ...(account.user && path.startsWith("/api/attempts") ? { "X-EkGuru-User": account.user.id } : {}), ...(method !== "GET" ? { "X-EkGuru-CSRF": "1" } : {}), ...(body ? { "Content-Type": "application/json" } : {}) },
    ...(body ? { body: JSON.stringify(body) } : {}),
  });
  const data = await response.json();
  if (!response.ok) { const error = new Error(data.error || "request_failed"); error.status = response.status; throw error; }
  return data;
}

function status(text) { $all("[data-cloud-status]").forEach((node) => { node.textContent = text; }); }
function notice(text) { $all("[data-account-notice]").forEach((node) => { node.textContent = text; node.hidden = !text; }); }
function nextPath() {
  const requested = new URLSearchParams(location.search).get("next");
  if (requested?.startsWith("/subjects/")) return requested;
  const relative = location.pathname.startsWith(ROOT.pathname) ? location.pathname.slice(ROOT.pathname.length) : "";
  return relative.startsWith("subjects/") ? "/" + relative + location.search : "/subjects/test-room/index.html";
}

function renderAccount() {
  $all("[data-account-link]").forEach((link) => {
    link.href = account.origin + ACCOUNT;
    link.textContent = account.user ? "My account" : "Google login";
  });
  $all("[data-account-login]").forEach((link) => {
    link.href = account.origin + "/api/auth/login?" + new URLSearchParams({ next: nextPath() });
    const disabled = !account.remote && (!account.configured || !account.google_enabled);
    link.setAttribute("aria-disabled", String(disabled));
    link.hidden = Boolean(account.user);
  });
  $all("[data-account-guest]").forEach((node) => { node.hidden = Boolean(account.user); });
  $all("[data-account-signed]").forEach((node) => { node.hidden = !account.user; });
  $all("[data-account-name]").forEach((node) => { node.textContent = account.user?.name || "Student"; });
  $all("[data-account-email]").forEach((node) => { node.textContent = account.user?.email || ""; });
  if (account.user) status("Google se logged in · naye results aapke private account mein save honge.");
  else if (account.remote) status("Guest mode · cross-device results ke liye secure login site kholein.");
  else status("Guest mode · answers is device par; Google login se future results sync honge.");
  window.dispatchEvent(new CustomEvent("ekguru:account", { detail: { user: account.user } }));
}

let syncing = false;
async function flush() {
  if (syncing || !account.user || account.remote) return;
  const userId = account.user.id;
  const key = outboxKey(userId);
  let queue = localRead(key, []);
  if (!Array.isArray(queue)) queue = [];
  if (!queue.length) return;
  syncing = true;
  try {
    while (queue.length && account.user?.id === userId) {
      const attempt = queue[0];
      await api("/api/attempts", { method: "POST", body: attempt });
      // Merge with storage again: another completed test may have been queued mid-request.
      const current = localRead(key, queue);
      queue = (Array.isArray(current) ? current : queue).filter((item) => item.id !== attempt.id);
      localWrite(key, queue);
    }
    status("Result sync ho gaya · aapke account mein private history saved hai.");
  } catch (error) {
    status(error.status === 401
      ? "Session expire hui. Isi Google account se dobara login karke Sync dabayein; result is device par queued hai."
      : error.status === 409 ? "Browser mein account change hua hai. Page refresh karein; doosre account ka result upload nahi kiya."
      : volatile.has(key) ? "Sync pending · browser storage unavailable, is tab ko band na karein. Sync button se retry karein."
      : "Sync pending · result is device par queued hai. Online aane par ya Sync se retry hoga.");
  } finally { syncing = false; }
}

account.saveAttempt = async (attempt, owner) => {
  await account.ready;
  // Never silently upload guest history or another account's unfinished draft.
  if (!owner || owner !== account.user?.id || account.remote) {
    status("Result is device par saved hai. Google login ke baad shuru kiye tests hi account mein sync hote hain.");
    return false;
  }
  const key = outboxKey(owner);
  const stored = localRead(key, []);
  const queue = Array.isArray(stored) ? stored : [];
  if (!queue.some((item) => item.id === attempt.id)) queue.push(attempt);
  localWrite(key, queue.slice(-20));
  await flush();
  return true;
};
account.retrySync = flush;

async function loadHistory() {
  const list = document.getElementById("accountHistory");
  if (!list || !account.user) return;
  list.textContent = "History load ho rahi hai…";
  try {
    const { attempts } = await api("/api/attempts");
    list.replaceChildren();
    if (!attempts.length) { list.textContent = "Abhi koi synced test nahi. Test Room se apni pehli practice shuru karein."; return; }
    for (const attempt of attempts) {
      const row = document.createElement("article"); row.className = "history-row";
      const title = document.createElement("h3"); title.textContent = attempt.label;
      const meta = document.createElement("p"); meta.className = "small muted";
      const when = new Date(attempt.created_at).toLocaleString("en-IN", { dateStyle: "medium", timeStyle: "short" });
      meta.textContent = `${when} · ${attempt.total} questions · ${Math.round(attempt.duration_seconds / 60)} min`;
      const score = document.createElement("p");
      score.textContent = attempt.score === null
        ? `Unscored self-practice · ${attempt.total - attempt.unanswered} attempted, ${attempt.unanswered} skipped`
        : `${attempt.score} / ${attempt.max_score} practice marks · ${attempt.correct} correct, ${attempt.wrong} wrong, ${attempt.unanswered} skipped`;
      const remove = document.createElement("button"); remove.className = "button secondary"; remove.type = "button";
      remove.textContent = "Delete result"; remove.setAttribute("aria-label", `Delete result: ${attempt.label}`);
      remove.addEventListener("click", async () => {
        if (!window.confirm("Sirf ye account result permanently delete karein?")) return;
        remove.disabled = true;
        try { await api(`/api/attempts?id=${encodeURIComponent(attempt.id)}`, { method: "DELETE" }); await loadHistory(); }
        catch { notice("Result delete nahi hua. Dobara try karein."); remove.disabled = false; }
      });
      row.append(title, meta, score, remove); list.append(row);
    }
  } catch { list.textContent = "History abhi load nahi hui. Refresh / Sync se dobara try karein; local practice chalti rahegi."; }
}

async function init() {
  try {
    const response = await fetch(new URL("data/runtime.json", ROOT), { cache: "no-cache", signal: AbortSignal.timeout(8000) });
    if (!response.ok) throw new Error("runtime_unavailable");
    const runtime = await response.json();
    const target = new URL(runtime.auth_origin === "same-origin" ? location.origin : runtime.auth_origin);
    if (target.protocol !== "https:" && !["localhost", "127.0.0.1"].includes(target.hostname)) throw new Error("invalid_origin");
    account.origin = target.origin;
    account.remote = account.origin !== location.origin;
    if (!account.remote) Object.assign(account, await api("/api/auth/session"));
    if (account.remote) notice("GitHub Pages par secure backend cookies nahi chal sakti. Google login ke liye EkGuru ki secure site khulegi; guest practice yahin available hai.");
    else if (!account.configured) notice("Login server ka setup pending hai. Aap bina login ke saare papers practice kar sakte hain.");
    else if (!account.google_enabled) notice(messages.google_setup_required);
  } catch {
    notice("Login service filhaal reachable nahi hai. Guest practice aur PDFs phir bhi available hain.");
  }
  const error = new URLSearchParams(location.search).get("error");
  if (messages[error]) {
    notice(messages[error]);
    // OAuth error flags need not remain in copied/shared URLs.
    const url = new URL(location.href); url.searchParams.delete("error"); history.replaceState(null, "", url);
  }
  renderAccount();
}

$all("[data-account-login]").forEach((link) => link.addEventListener("click", (event) => {
  if (link.getAttribute("aria-disabled") === "true") { event.preventDefault(); notice(messages.google_setup_required); }
}));
$all("[data-account-logout]").forEach((button) => button.addEventListener("click", async () => {
  button.disabled = true;
  try {
    await api("/api/auth/logout", { method: "POST" });
    if (account.user) { volatile.delete(outboxKey(account.user.id)); try { localStorage.removeItem(outboxKey(account.user.id)); } catch { /* optional storage */ } }
    account.user = null; renderAccount();
    const list = document.getElementById("accountHistory"); if (list) list.replaceChildren();
    notice("Logout ho gaya. Is browser ka session clear kar diya hai.");
  } catch { notice("Logout confirm nahi hua. Internet check karke dobara try karein."); }
  finally { button.disabled = false; }
}));
$all("[data-account-sync]").forEach((button) => button.addEventListener("click", async () => {
  button.disabled = true;
  try { await flush(); await loadHistory(); } finally { button.disabled = false; }
}));
window.addEventListener("online", flush);
account.ready = init();
account.ready.then(async () => { if (account.user) { await flush(); await loadHistory(); } });
