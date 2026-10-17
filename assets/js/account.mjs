/* All-subject results, local-first journal and same-origin HttpOnly auth.
   JavaScript only receives the safe user summary: never bearer tokens. */
import "./theme.mjs";
import { historyStore, normalizeAttempt } from "./history-store.mjs";
const ROOT = new URL("../../", import.meta.url);
const $ = (id) => document.getElementById(id);
const $all = (selector) => document.querySelectorAll(selector);
const messages = {
  google_setup_required: "Google login ka provider setup abhi pending hai. Guest practice bilkul chalti hai.",
  login_expired: "Login link expire/cancel hua. Dobara Google se login karein.",
  login_failed: "Login complete nahi hua. Cookies allow karke dobara try karein.",
};
const account = { user: null, configured: false, google_enabled: false, remote: false, origin: location.origin, ready: null };
window.EkGuruAccount = account;
const owner = () => account.user?.id || "guest";
const status = (text) => $all("[data-cloud-status]").forEach((node) => { node.textContent = text; });
const notice = (text) => $all("[data-account-notice]").forEach((node) => { node.textContent = text; node.hidden = !text; });

export async function api(path, { method = "GET", body } = {}) {
  const response = await fetch(path, { method, credentials: "same-origin", cache: "no-store", signal: AbortSignal.timeout(12000),
    headers: { ...(account.user && path.startsWith("/api/attempts") ? { "X-EkGuru-User": account.user.id } : {}),
      ...(method !== "GET" ? { "X-EkGuru-CSRF": "1" } : {}), ...(body ? { "Content-Type": "application/json" } : {}) },
    ...(body ? { body: JSON.stringify(body) } : {}) });
  const data = await response.json();
  if (!response.ok) { const error = new Error(data.error || "request_failed"); error.status = response.status; throw error; }
  return data;
}
function nextPath() {
  const requested = new URLSearchParams(location.search).get("next");
  if (requested?.startsWith("/subjects/")) return requested;
  const relative = location.pathname.startsWith(ROOT.pathname) ? location.pathname.slice(ROOT.pathname.length) : "";
  return relative.startsWith("subjects/") ? "/" + relative + location.search : "/subjects/test-room/index.html";
}
function renderAccount() {
  $all("[data-account-link]").forEach((link) => { link.href = account.remote ? account.origin + "/subjects/account/index.html" : new URL("subjects/account/index.html", ROOT).href; link.textContent = account.user ? "My account" : "My results"; });
  $all("[data-account-login]").forEach((link) => {
    link.href = account.origin + "/api/auth/login?" + new URLSearchParams({ next: nextPath() });
    link.setAttribute("aria-disabled", String(!account.remote && (!account.configured || !account.google_enabled)));
    link.hidden = Boolean(account.user);
  });
  $all("[data-account-guest]").forEach((node) => { node.hidden = Boolean(account.user); });
  $all("[data-account-signed]").forEach((node) => { node.hidden = !account.user; });
  $all("[data-account-name]").forEach((node) => { node.textContent = account.user?.name || "Student"; });
  $all("[data-account-email]").forEach((node) => { node.textContent = account.user?.email || ""; });
  status(account.user ? "Google se logged in · har subject ke naye results private account mein save honge."
    : "Guest mode · har subject ka result is browser mein saved; login se naye results cloud mein bhi sync honge.");
  if ($("historySource")) {
    $("historySource").value = account.user && !account.remote ? "cloud" : "local";
    $("historySource").querySelector('[value="cloud"]').disabled = !account.user || account.remote;
  }
  window.dispatchEvent(new CustomEvent("ekguru:account", { detail: { user: account.user } }));
}

let syncing = false;
async function flush() {
  if (syncing || !account.user || account.remote) return;
  const userId = account.user.id, sent = new Set();
  syncing = true;
  try {
    let count = 0;
    while (account.user?.id === userId) {
      const queue = (await historyStore.pending(userId)).filter((attempt) => !sent.has(attempt.id));
      if (!queue.length) break;
      for (const attempt of queue) {
        if (account.user?.id !== userId) return;
        await api("/api/attempts", { method: "POST", body: attempt });
        sent.add(attempt.id); await historyStore.acknowledge(userId, attempt.id); count++;
      }
    }
    if (count) status("Result sync ho gaya · har subject ki private history saved hai.");
  } catch (error) {
    status(error.status === 401 ? "Session expire hui. Isi Google account se dobara login karke Sync dabayein; result is device par queued hai."
      : error.status === 409 ? "Browser mein account change hua hai. Page refresh karein; doosre account ka result upload nahi kiya."
      : !historyStore.durable ? "Sync pending · browser storage unavailable, is tab ko band na karein. Sync button se retry karein."
      : "Sync pending · result is device par queued hai. Online aane par ya Sync se retry hoga.");
  } finally { syncing = false; }
}
account.saveAttempt = async (raw, startedOwner) => {
  // Save before network work. Guest results stay guest; an account switch cannot
  // move a result into the newly logged-in person's journal or cloud account.
  const attempt = normalizeAttempt(raw);
  await historyStore.record(startedOwner || "guest", attempt, Boolean(startedOwner));
  await account.ready;
  window.dispatchEvent(new Event("ekguru:attempt-saved"));
  if (!historyStore.durable) notice("Local history storage unavailable/full: result sirf is tab mein hai. Result JSON download karein. Cloud retry still works while this tab stays open.");
  if (!startedOwner || startedOwner !== account.user?.id || account.remote) {
    status(historyStore.durable ? "Result is device par saved hai. Google login ke baad shuru kiye tests hi account mein sync hote hain."
      : "Browser storage unavailable. Result JSON download karein; tab band hone par local history nahi bachegi.");
    return false;
  }
  await flush(); return true;
};
account.retrySync = flush;
account.historyStore = historyStore;
// Existing/custom subject players can use the same versioned event contract.
window.addEventListener("ekguru:test-complete", (event) => {
  const value = event.detail;
  if (value?.attempt && Object.hasOwn(value, "owner")) account.saveAttempt(value.attempt, value.owner).catch(() => notice("Result persist nahi hua. Result export karke retry karein."));
});

const historyState = { cursor: null, generation: 0, source: "local", owner: "guest", subject: "", test: "" };
function filters() {
  const subject = $("historySubject")?.value.trim() || "", test = $("historyTest")?.value.trim() || "";
  if (subject && !/^[a-z0-9][a-z0-9_.-]{0,95}$/.test(subject) || test && !/^[\w.-]{1,128}$/.test(test)) throw new Error("Subject/test ID mein sirf letters, numbers, dash, dot ya underscore use karein.");
  return { subject, test };
}
async function historyPage(source, user, subject, test, cursor) {
  if (source === "local") return historyStore.page(user, { subject, test, before: cursor });
  if (!account.user || account.user.id !== user || account.remote) throw new Error("Same account se login karein.");
  const params = new URLSearchParams({ limit: "50", ...(subject ? { subject_id: subject } : {}), ...(test ? { test_id: test } : {}), ...(cursor ? { cursor } : {}) });
  return api("/api/attempts?" + params);
}
function historyRow(attempt, source, expectedOwner) {
  const row = document.createElement("article"); row.className = "history-row";
  const tag = document.createElement("span"); tag.className = "eyebrow"; tag.textContent = attempt.subject_id || (attempt.kind === "cn" ? "computer-network" : "previous-year-papers");
  const title = document.createElement("h3"); title.textContent = attempt.label;
  const meta = document.createElement("p"); meta.className = "small muted";
  const when = new Date(attempt.completed_at || attempt.created_at).toLocaleString("en-IN", { dateStyle: "medium", timeStyle: "short" });
  meta.textContent = `${when} · ${attempt.total} questions · ${Math.round(attempt.duration_seconds / 60)} min · ${attempt.test_id || attempt.paper_id}`;
  const score = document.createElement("p");
  score.textContent = attempt.score === null ? `Unscored self-practice · ${attempt.total - attempt.unanswered} attempted, ${attempt.unanswered} skipped`
    : `${attempt.score} / ${attempt.max_score} practice marks · ${attempt.correct} correct, ${attempt.wrong} wrong, ${attempt.unanswered} skipped`;
  const remove = document.createElement("button"); remove.className = "button ghost small"; remove.type = "button"; remove.textContent = "Delete result";
  remove.setAttribute("aria-label", `Delete result: ${attempt.label}`);
  remove.addEventListener("click", async () => {
    if (owner() !== expectedOwner || !window.confirm(source === "cloud" ? "Sirf ye cloud result permanently delete karein? Local copy alag rahegi." : "Sirf ye device copy delete karein? Unsynced copy bhi remove ho jayegi; synced cloud result alag rahega.")) return;
    remove.disabled = true;
    try {
      if (source === "cloud") await api(`/api/attempts?id=${encodeURIComponent(attempt.id)}`, { method: "DELETE" });
      else await historyStore.remove(expectedOwner, attempt.id);
      await loadHistory();
    } catch { notice("Result delete nahi hua. Dobara try karein."); remove.disabled = false; }
  });
  row.append(tag, title, meta, score, remove); return row;
}
async function loadHistory(more = false) {
  const list = $("accountHistory"); if (!list) return;
  let filter;
  try { filter = filters(); } catch (error) { notice(error.message); return; }
  if (!more) Object.assign(historyState, { ...filter, cursor: null, generation: historyState.generation + 1, source: $("historySource")?.value || "local", owner: owner() });
  const snapshot = { ...historyState }, generation = snapshot.generation;
  if (more && !snapshot.cursor) return;
  if (!more) list.textContent = "History load ho rahi hai…";
  if ($("historyMore")) $("historyMore").disabled = true;
  try {
    const result = await historyPage(snapshot.source, snapshot.owner, snapshot.subject, snapshot.test, snapshot.cursor);
    if (generation !== historyState.generation || owner() !== snapshot.owner) return;
    if (!more) list.replaceChildren();
    if (!result.attempts.length && !more) list.textContent = snapshot.source === "local" ? "Is browser mein abhi matching result nahi. Kisi bhi subject ka test complete karein." : "Abhi matching synced result nahi. Kisi bhi subject ka naya test login ke baad complete karein.";
    result.attempts.forEach((attempt) => list.append(historyRow(attempt, snapshot.source, snapshot.owner)));
    historyState.cursor = result.next_cursor || null;
    if ($("historyMore")) { $("historyMore").hidden = !historyState.cursor; $("historyMore").disabled = false; }
    if ($("historyCaption")) $("historyCaption").textContent = `${snapshot.source === "local" ? "This device" : "Private cloud"} · ${list.querySelectorAll(".history-row").length} shown · no automatic 200-result expiry`;
  } catch { if (generation === historyState.generation) { if (!more) list.textContent = "History abhi load nahi hui. Refresh / Sync se retry karein; local practice chalti rahegi."; if ($("historyMore")) $("historyMore").disabled = false; } }
}
async function exportHistory(button) {
  button.disabled = true;
  try {
    const user = owner(), source = $("historySource")?.value || "local", { subject, test } = filters();
    const rows = [], cursors = new Set(); let cursor = null;
    do {
      const result = await historyPage(source, user, subject, test, cursor);
      if (owner() !== user) throw new Error("Account change hua; export cancel kar diya.");
      rows.push(...result.attempts); cursor = result.next_cursor || null;
      const token = JSON.stringify(cursor); if (cursor && cursors.has(token)) throw new Error("History cursor repeated; retry export."); cursors.add(token);
    } while (cursor);
    const url = URL.createObjectURL(new Blob([JSON.stringify({ version: 2, exported_at: new Date().toISOString(), source, attempts: rows }, null, 2)], { type: "application/json" }));
    const link = document.createElement("a"); link.href = url; link.download = "ekguru-all-subject-results.json"; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  } catch (error) { notice(error.message || "Export nahi hua. Retry karein."); } finally { button.disabled = false; }
}

async function init() {
  try {
    const response = await fetch(new URL("data/runtime.json", ROOT), { cache: "no-cache", signal: AbortSignal.timeout(8000) });
    if (!response.ok) throw new Error("runtime_unavailable");
    const runtime = await response.json(), target = new URL(runtime.auth_origin === "same-origin" ? location.origin : runtime.auth_origin);
    if (target.protocol !== "https:" && !["localhost", "127.0.0.1"].includes(target.hostname)) throw new Error("invalid_origin");
    account.origin = target.origin; account.remote = account.origin !== location.origin;
    if (!account.remote) Object.assign(account, await api("/api/auth/session"));
    if (account.remote) notice("GitHub Pages par history is browser mein save hoti hai. Cross-device sync ke liye secure login site kholein; cookies domains ke beech share nahi hoti.");
    else if (!account.configured) notice("Login server ka setup pending hai. Aap bina login ke practice aur device history use kar sakte hain.");
    else if (!account.google_enabled) notice(messages.google_setup_required);
  } catch { notice("Login service filhaal reachable nahi hai. Guest practice aur device history available hain."); }
  const error = new URLSearchParams(location.search).get("error");
  if (messages[error]) { notice(messages[error]); const url = new URL(location.href); url.searchParams.delete("error"); history.replaceState(null, "", url); }
  // Upgrade only the currently authenticated user's old outbox; never guest data.
  if (account.user) {
    const oldKey = `ekguru.outbox.v1.${account.user.id}`;
    try {
      const queued = JSON.parse(localStorage.getItem(oldKey) || "[]");
      if (Array.isArray(queued)) for (const attempt of queued) await historyStore.record(account.user.id, attempt, true);
      if (historyStore.durable) localStorage.removeItem(oldKey);
    } catch { /* existing history is left untouched if storage is unavailable */ }
  }
  renderAccount();
}
$all("[data-account-login]").forEach((link) => link.addEventListener("click", (event) => { if (link.getAttribute("aria-disabled") === "true") { event.preventDefault(); notice(messages.google_setup_required); } }));
$all("[data-account-logout]").forEach((button) => button.addEventListener("click", async () => {
  button.disabled = true;
  try {
    await api("/api/auth/logout", { method: "POST" });
    account.user = null; historyState.generation++; renderAccount(); await loadHistory();
    notice("Logout ho gaya. Cloud session clear hai; account-specific device records sirf usi account ko UI mein dikhte hain. Shared browser private vault nahi hai—zarurat par browser site data clear karein.");
  } catch { notice("Logout confirm nahi hua. Internet check karke dobara try karein."); } finally { button.disabled = false; }
}));
$all("[data-account-sync]").forEach((button) => button.addEventListener("click", async () => { button.disabled = true; try { await flush(); await loadHistory(); } finally { button.disabled = false; } }));
$("historyMore")?.addEventListener("click", () => loadHistory(true));
$("historyFilter")?.addEventListener("submit", (event) => { event.preventDefault(); loadHistory(); });
$("historySource")?.addEventListener("change", () => loadHistory());
$("historyExport")?.addEventListener("click", (event) => exportHistory(event.currentTarget));
window.addEventListener("online", flush);
window.addEventListener("ekguru:attempt-saved", () => { if ($("accountHistory")) loadHistory(); });
account.ready = init();
account.ready.then(() => { loadHistory(); flush(); });
