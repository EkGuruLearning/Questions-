/* One IndexedDB record per attempt, across every subject. No 200-result pruning.
   Owner-isolated local journal/outbox; guest records are NEVER silently uploaded.
   No email, cookie, access token or refresh token is stored here. */
const memory = new Map();
let database;
const request = (req) => new Promise((resolve, reject) => { req.onsuccess = () => resolve(req.result); req.onerror = () => reject(req.error); });
async function open() {
  if (!database) database = new Promise((resolve, reject) => {
    const req = indexedDB.open("ekguru-practice-history-v2", 1);
    req.onupgradeneeded = () => {
      const store = req.result.createObjectStore("attempts", { keyPath: ["owner", "id"] });
      store.createIndex("recent", ["owner", "completed_at", "id"]);
      store.createIndex("subject", ["owner", "subject_id", "completed_at", "id"]);
      store.createIndex("test", ["owner", "subject_id", "test_id", "completed_at", "id"]);
      store.createIndex("pending", ["owner", "pending"]);
    };
    req.onsuccess = () => { req.result.onversionchange = () => { req.result.close(); database = null; }; resolve(req.result); };
    req.onerror = () => reject(req.error);
    req.onblocked = () => reject(new Error("Close another old EkGuru tab to upgrade local history"));
  }).catch(() => null);
  return database;
}
const key = (owner, id) => `${owner}:${id}`;
export function normalizeAttempt(attempt) {
  if (!attempt || typeof attempt !== "object") throw new TypeError("Attempt required");
  const kind = attempt.kind || "quiz";
  if (!["cn", "paper", "quiz"].includes(kind) || kind === "quiz" && (!attempt.subject_id || !attempt.test_id)) throw new TypeError("Quiz needs subject_id and test_id");
  const subject_id = attempt.subject_id || (kind === "cn" ? "computer-network" : "previous-year-papers");
  const test_id = attempt.test_id || attempt.paper_id;
  const date = new Date(attempt.completed_at || attempt.created_at || Date.now());
  if (!/^[a-z0-9][a-z0-9_.-]{0,95}$/.test(subject_id) || !/^[\w.-]{1,128}$/.test(test_id || "") || !Number.isFinite(date.getTime())
    || typeof attempt.id !== "string" || !/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(attempt.id) || typeof attempt.label !== "string" || !attempt.label.trim() || attempt.label.length > 200) throw new TypeError("Invalid attempt identifiers / date / label");
  return { ...attempt, id: attempt.id.toLowerCase(), kind, subject_id, test_id, paper_id: attempt.paper_id || test_id, completed_at: date.toISOString() };
}

const clean = (row) => { const { owner, pending, ...attempt } = row; return attempt; };
async function transaction(mode, action) {
  const db = await open();
  if (!db) return null;
  return new Promise((resolve, reject) => {
    const tx = db.transaction("attempts", mode), store = tx.objectStore("attempts");
    let result;
    tx.oncomplete = () => resolve(result);
    tx.onerror = tx.onabort = () => reject(tx.error || new Error("Local history unavailable"));
    action(store, (value) => { result = value; });
  });
}
export const historyStore = {
  durable: true,
  async record(owner, raw, pending = false) {
    owner ||= "guest";
    pending = Boolean(pending && owner !== "guest");
    const attempt = normalizeAttempt(raw);
    const row = { ...attempt, owner, pending: pending ? 1 : 0, details: pending ? (attempt.details || {}) : {} };
    try {
      const value = await transaction("readwrite", (store, result) => {
        const lookup = store.get([owner, row.id]);
        lookup.onsuccess = () => { const saved = lookup.result || row; if (!lookup.result) store.put(row); result(saved); };
      });
      if (value) return clean(value);
    } catch { /* disk-full / private-mode fallback, never pretend it persisted */ }
    this.durable = false;
    if (!memory.has(key(owner, row.id))) memory.set(key(owner, row.id), row);
    return clean(memory.get(key(owner, row.id)));
  },
  async acknowledge(owner, id) {
    try {
      await transaction("readwrite", (store) => {
        const lookup = store.get([owner, id]);
        lookup.onsuccess = () => { if (lookup.result) store.put({ ...lookup.result, pending: 0, details: {} }); };
      });
    } catch { this.durable = false; }
    const row = memory.get(key(owner, id)); if (row) { row.pending = 0; row.details = {}; }
  },
  async pending(owner, limit = 20) {
    const volatile = [...memory.values()].filter((row) => row.owner === owner && row.pending === 1);
    let rows = [];
    try {
      const db = await open();
      if (db) rows = await request(db.transaction("attempts").objectStore("attempts").index("pending").getAll(IDBKeyRange.only([owner, 1]), limit));
    } catch { this.durable = false; }
    return [...new Map([...rows, ...volatile].map((row) => [row.id, row])).values()]
      .sort((a, b) => a.completed_at.localeCompare(b.completed_at)).slice(0, limit).map(clean);
  },
  async page(owner = "guest", { subject = "", test = "", before = null, limit = 50 } = {}) {
    const matches = (row) => row.owner === owner && (!subject || row.subject_id === subject) && (!test || row.test_id === test)
      && (!before || row.completed_at < before.at || row.completed_at === before.at && row.id < before.id);
    const volatile = [...memory.values()].filter(matches);
    let rows = [];
    try {
      const db = await open();
      if (db) rows = await new Promise((resolve, reject) => {
        const store = db.transaction("attempts").objectStore("attempts");
        const prefix = subject ? test ? [owner, subject, test] : [owner, subject] : [owner];
        const index = store.index(subject ? test ? "test" : "subject" : "recent");
        const upper = before ? [...prefix, before.at, before.id] : [...prefix, "\uffff", "\uffff"];
        const cursor = index.openCursor(IDBKeyRange.bound([...prefix, ""], upper, false, Boolean(before)), "prev");
        const found = [];
        cursor.onerror = () => reject(cursor.error);
        cursor.onsuccess = () => { const current = cursor.result;
          if (!current || found.length > limit) return resolve(found);
          if (matches(current.value)) found.push(current.value);
          current.continue();
        };
      });
    } catch { this.durable = false; }
    rows = [...new Map([...rows, ...volatile].map((row) => [row.id, row])).values()]
      .sort((a, b) => b.completed_at.localeCompare(a.completed_at) || b.id.localeCompare(a.id));
    const attempts = rows.slice(0, limit).map(clean), last = attempts.at(-1);
    return { attempts, next_cursor: rows.length > limit && last ? { at: last.completed_at, id: last.id } : null };
  },
  async remove(owner, id) {
    await transaction("readwrite", (store) => store.delete([owner || "guest", id]));
    memory.delete(key(owner || "guest", id));
  },
};
