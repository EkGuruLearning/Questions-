/* Tiny same-origin BFF: Google PKCE OAuth, server-only cookies, RLS-backed history.
   No service-role key, no browser auth SDK, no browser-readable bearer tokens. */
import { createHash, randomBytes, timingSafeEqual } from "node:crypto";
import { clearCookie, OAUTH_SECONDS, parseCookies, readCookie, SESSION_SECONDS, writeCookie } from "./cookies.mjs";

const ACCOUNT = "/subjects/account/index.html";
const ROOM = "/subjects/test-room/index.html";
const MAX_BODY = 24 * 1024;
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
const SELECT = "id,kind,subject_id,test_id,paper_id,label,total,correct,wrong,unanswered,score,max_score,duration_seconds,completed_at,created_at";

function timestamp(value) {
  if (typeof value !== "string") return false;
  const match = /^(20\d{2})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(?:\.\d{1,6})?(?:Z|[+-]\d{2}:\d{2})$/.exec(value);
  if (!match || !Number.isFinite(Date.parse(value))) return false;
  const [, year, month, day, hour, minute, second] = match.map(Number);
  return month >= 1 && month <= 12 && day >= 1 && day <= new Date(Date.UTC(year, month, 0)).getUTCDate() && hour <= 23 && minute <= 59 && second <= 59;
}

class APIError extends Error {
  constructor(status, code) { super(code); this.status = status; this.code = code; }
}

export function loadConfig(env = process.env) {
  try {
    const origin = new URL(env.APP_ORIGIN || "");
    const local = ["localhost", "127.0.0.1", "[::1]"].includes(origin.hostname);
    if (origin.username || origin.password || origin.pathname !== "/" || origin.search || origin.hash) return null;
    const secure = origin.protocol === "https:";
    if (!secure && !(local && origin.protocol === "http:" && env.ALLOW_INSECURE_LOCALHOST === "true")) return null;
    const supabase = new URL(env.SUPABASE_URL || "");
    if (supabase.protocol !== "https:" || supabase.username || supabase.password || supabase.pathname !== "/") return null;
    if (!env.SUPABASE_PUBLISHABLE_KEY || (env.SESSION_SECRET || "").length < 32) return null;
    // A privileged key is unnecessary and must not be used for user requests.
    const key = env.SUPABASE_PUBLISHABLE_KEY;
    if (key.startsWith("sb_secret_")) return null;
    if (key.startsWith("eyJ")) {
      const payload = JSON.parse(Buffer.from(key.split(".")[1], "base64url").toString());
      if (payload.role !== "anon") return null;
    } else if (!key.startsWith("sb_publishable_")) return null;
    return { origin: origin.origin, supabase: supabase.origin, key, secret: env.SESSION_SECRET, secure };
  } catch { return null; }
}

export function safeNext(raw, origin) {
  try {
    if (typeof raw !== "string" || raw.length > 1024 || /[\\\r\n\u0000]/.test(raw)) return ROOM;
    const url = new URL(raw, origin);
    if (url.origin !== origin || !url.pathname.startsWith("/subjects/") || !url.pathname.endsWith("/index.html")) return ROOM;
    return url.pathname + url.search;
  } catch { return ROOM; }
}

export function validateAttempt(input) {
  const integer = (n, min, max) => Number.isInteger(n) && n >= min && n <= max;
  if (!input || typeof input !== "object" || Array.isArray(input) || typeof input.id !== "string" || !UUID.test(input.id)) throw new APIError(400, "invalid_attempt");
  if (!["cn", "paper", "quiz"].includes(input.kind)) throw new APIError(400, "invalid_attempt");
  const subjectId = input.subject_id ?? (input.kind === "cn" ? "computer-network" : input.kind === "paper" ? "previous-year-papers" : "");
  const testId = input.test_id ?? input.paper_id;
  if (typeof subjectId !== "string" || typeof testId !== "string" || !/^[a-z0-9][a-z0-9_.-]{0,95}$/.test(subjectId) || !/^[\w.-]{1,128}$/.test(testId)) throw new APIError(400, "invalid_attempt");
  input = { ...input, subject_id: subjectId, test_id: testId, paper_id: input.paper_id ?? testId };
  if (typeof input.paper_id !== "string" || !/^[\w.-]{1,128}$/.test(input.paper_id)) throw new APIError(400, "invalid_attempt");
  if (typeof input.label !== "string" || !input.label.trim() || input.label.length > 200) throw new APIError(400, "invalid_attempt");
  if (!integer(input.total, 1, input.kind === "paper" ? 300 : 2000) || !integer(input.unanswered, 0, input.total) || !integer(input.duration_seconds, 0, 7 * 86400)) throw new APIError(400, "invalid_attempt");
  const unscored = input.correct === null && input.wrong === null && input.score === null && input.max_score === null;
  if (!unscored && (!integer(input.correct, 0, input.total) || !integer(input.wrong, 0, input.total)
    || input.correct + input.wrong + input.unanswered > input.total
    || !Number.isFinite(input.score) || !Number.isFinite(input.max_score)
    || input.max_score <= 0 || input.max_score > 30000 || input.score > input.max_score || input.score < -30000)) throw new APIError(400, "invalid_attempt");
  const extra = [];
  if (input.completed_at !== undefined) {
    if (!timestamp(input.completed_at)) throw new APIError(400, "invalid_attempt");
    extra.push(["completed_at", new Date(input.completed_at).toISOString()]);
  }
  const details = input.details ?? {};
  if (!details || typeof details !== "object" || Array.isArray(details) || JSON.stringify(details).length > 16000) throw new APIError(400, "invalid_attempt");
  return Object.fromEntries([
    "id", "kind", "subject_id", "test_id", "paper_id", "label", "total", "correct", "wrong", "unanswered", "score", "max_score", "duration_seconds",
  ].map((key) => [key, key === "label" ? input.label.trim() : input[key]]).concat([["details", details]], extra));
}

async function readJSON(req) {
  if (!String(req.headers["content-type"] || "").toLowerCase().startsWith("application/json")) throw new APIError(415, "json_required");
  if (Number(req.headers["content-length"] || 0) > MAX_BODY) throw new APIError(413, "body_too_large");
  // Vercel may preparse a body. Apply the same limits and validation in either runtime.
  if (req.body !== undefined) {
    const raw = typeof req.body === "string" ? req.body : JSON.stringify(req.body);
    if (Buffer.byteLength(raw) > MAX_BODY) throw new APIError(413, "body_too_large");
    try { return JSON.parse(raw); } catch { throw new APIError(400, "invalid_json"); }
  }
  let size = 0;
  const chunks = [];
  for await (const chunk of req) {
    size += chunk.length;
    if (size > MAX_BODY) throw new APIError(413, "body_too_large");
    chunks.push(chunk);
  }
  try { return JSON.parse(Buffer.concat(chunks).toString("utf8")); }
  catch { throw new APIError(400, "invalid_json"); }
}

export function createHandler({ env = process.env, fetcher = fetch, now = Date.now } = {}) {
  // One handler per warm function instance. Only in-flight refreshes, never user history.
  const refreshes = new Map();
  let settingsCache = null;

  return async function handler(req, res) {
    const config = loadConfig(env);
    const requestURL = new URL(req.url, config?.origin || "https://unconfigured.invalid");
    const path = requestURL.pathname === "/api" && requestURL.searchParams.has("__path")
      ? "/api/" + requestURL.searchParams.get("__path") : requestURL.pathname;
    const headers = {
      "Cache-Control": "private, no-store, max-age=0",
      "Vary": "Cookie, Origin",
      "X-Content-Type-Options": "nosniff",
      "Referrer-Policy": "no-referrer",
      "Content-Security-Policy": "default-src 'none'; frame-ancestors 'none'",
    };
    const setCookies = [];
    const cookie = (kind, value, maxAge) => setCookies.push(...writeCookie(kind, value, config.secret, config.secure, maxAge));
    const clear = (kind) => setCookies.push(...clearCookie(kind, config.secure));
    const send = (status, body, extra = {}) => {
      res.writeHead(status, { ...headers, ...(body ? { "Content-Type": "application/json; charset=utf-8" } : {}),
        ...(setCookies.length ? { "Set-Cookie": setCookies } : {}), ...extra });
      res.end(body ? JSON.stringify(body) : undefined);
    };
    const redirect = (where) => send(303, null, { Location: where });

    async function upstream(endpoint, { method = "GET", body, token, headers: more = {} } = {}) {
      let response;
      try {
        response = await fetcher(config.supabase + endpoint, {
          method, signal: AbortSignal.timeout(8000),
          headers: { apikey: config.key, ...(token ? { Authorization: `Bearer ${token}` } : {}),
            ...(body ? { "Content-Type": "application/json" } : {}), ...more },
          ...(body ? { body: JSON.stringify(body) } : {}),
        });
      } catch { throw new APIError(503, "service_unavailable"); }
      let data = null;
      try { data = await response.json(); } catch { /* 204 has no JSON */ }
      if (!response.ok) {
        if (response.status === 429) throw new APIError(429, "try_later");
        if (response.status >= 500) throw new APIError(503, "service_unavailable");
        if (endpoint.startsWith("/auth/v1/")) throw new APIError(401, "session_expired");
        throw new APIError(response.status === 403 ? 403 : 502, "history_unavailable");
      }
      return data;
    }

    async function googleEnabled() {
      if (settingsCache && settingsCache.until > now()) return settingsCache.enabled;
      const settings = await upstream("/auth/v1/settings");
      const enabled = settings?.external?.google === true;
      settingsCache = { enabled, until: now() + 60_000 };
      return enabled;
    }

    function tokenSession(data) {
      if (typeof data?.access_token !== "string" || typeof data.refresh_token !== "string" || !Number.isFinite(data.expires_in)) throw new APIError(502, "service_unavailable");
      return { access: data.access_token, refresh: data.refresh_token, expires: now() + data.expires_in * 1000, until: now() + SESSION_SECONDS * 1000 };
    }

    async function refresh(session) {
      const key = createHash("sha256").update(session.refresh).digest("hex");
      if (!refreshes.has(key)) {
        const promise = upstream("/auth/v1/token?grant_type=refresh_token", { method: "POST", body: { refresh_token: session.refresh } })
          .then(tokenSession).finally(() => refreshes.delete(key));
        refreshes.set(key, promise);
      }
      const next = await refreshes.get(key);
      cookie("session", next);
      return next;
    }

    async function authenticate() {
      const cookies = parseCookies(req.headers.cookie);
      let session = readCookie(cookies, "session", config.secret, config.secure);
      if (!session || session.until <= now() || typeof session.access !== "string" || typeof session.refresh !== "string") return null;
      try {
        if (session.expires <= now() + 60_000) session = await refresh(session);
        let user;
        try { user = await upstream("/auth/v1/user", { token: session.access }); }
        catch (error) {
          if (error.status !== 401) throw error;
          session = await refresh(session);
          user = await upstream("/auth/v1/user", { token: session.access });
        }
        if (!UUID.test(user?.id || "")) throw new APIError(401, "session_expired");
        return { user, session };
      } catch (error) {
        if (error.status === 401) { clear("session"); return null; }
        throw error; // Never destroy a valid cookie for a temporary upstream outage.
      }
    }

    try {
      if (path === "/api/auth/session" && req.method === "GET") {
        if (!config) return send(200, { configured: false, google_enabled: false, user: null });
        const auth = await authenticate();
        const user = auth?.user;
        return send(200, { configured: true, google_enabled: await googleEnabled(), user: user ? {
          id: user.id, email: user.email || "", name: String(user.user_metadata?.full_name || user.user_metadata?.name || user.email || "Student").slice(0, 200),
        } : null });
      }
      if (!config) throw new APIError(503, "setup_required");
      if (path === "/api/auth/login" && req.method === "GET") {
        if (!(await googleEnabled())) return redirect(`${ACCOUNT}?error=google_setup_required`);
        const verifier = randomBytes(48).toString("base64url");
        const state = randomBytes(24).toString("base64url");
        const next = safeNext(requestURL.searchParams.get("next"), config.origin);
        cookie("oauth", { verifier, state, next, until: now() + OAUTH_SECONDS * 1000 }, OAUTH_SECONDS);
        const target = new URL(config.supabase + "/auth/v1/authorize");
        target.search = new URLSearchParams({
          provider: "google", redirect_to: `${config.origin}/api/auth/callback?state=${state}`,
          code_challenge: createHash("sha256").update(verifier).digest("base64url"), code_challenge_method: "s256",
        }).toString();
        return redirect(target.href);
      }
      if (path === "/api/auth/callback" && req.method === "GET") {
        const flow = readCookie(parseCookies(req.headers.cookie), "oauth", config.secret, config.secure);
        clear("oauth");
        const code = requestURL.searchParams.get("code");
        const state = requestURL.searchParams.get("state") || "";
        const matches = typeof flow?.state === "string" && Buffer.byteLength(state) === Buffer.byteLength(flow.state)
          && timingSafeEqual(Buffer.from(state), Buffer.from(flow.state));
        if (!flow || flow.until <= now() || !matches || !code || code.length > 4096) return redirect(`${ACCOUNT}?error=login_expired`);
        try {
          const data = await upstream("/auth/v1/token?grant_type=pkce", { method: "POST", body: { auth_code: code, code_verifier: flow.verifier } });
          const session = tokenSession(data);
          // Verify with the auth server; never authorize solely from decoded JWT claims.
          const user = await upstream("/auth/v1/user", { token: session.access });
          if (!UUID.test(user?.id || "")) throw new APIError(401, "session_expired");
          cookie("session", session);
          return redirect(safeNext(flow.next, config.origin));
        } catch { return redirect(`${ACCOUNT}?error=login_failed`); }
      }
      if (["POST", "DELETE", "PUT", "PATCH"].includes(req.method)) {
        if (req.headers.origin !== config.origin || req.headers["x-ekguru-csrf"] !== "1") throw new APIError(403, "origin_rejected");
      }
      if (path === "/api/auth/logout" && req.method === "POST") {
        const session = readCookie(parseCookies(req.headers.cookie), "session", config.secret, config.secure);
        // Local sign-out must work even when Supabase is temporarily unavailable.
        if (session?.access) {
          try { await upstream("/auth/v1/logout?scope=local", { method: "POST", token: session.access }); } catch { /* cookies still expire */ }
        }
        clear("session"); clear("oauth");
        return send(200, { ok: true });
      }
      if (path === "/api/attempts" && ["GET", "POST", "DELETE"].includes(req.method)) {
        const auth = await authenticate();
        if (!auth) throw new APIError(401, "login_required");
        if (req.headers["x-ekguru-user"] !== auth.user.id) throw new APIError(409, "account_changed");
        if (req.method === "GET") {
          const rawLimit = requestURL.searchParams.get("limit") ?? "50";
          if (!/^\d{1,3}$/.test(rawLimit) || Number(rawLimit) < 1 || Number(rawLimit) > 100) throw new APIError(400, "invalid_page");
          const limit = Number(rawLimit);
          const query = new URLSearchParams({ user_id: `eq.${auth.user.id}`, select: SELECT, order: "completed_at.desc,id.desc", limit: String(limit + 1) });
          for (const field of ["subject_id", "test_id"]) {
            const value = requestURL.searchParams.get(field);
            if (value !== null) {
              if (!(field === "subject_id" ? /^[a-z0-9][a-z0-9_.-]{0,95}$/ : /^[\w.-]{1,128}$/).test(value)) throw new APIError(400, "invalid_filter");
              query.set(field, `eq.${value}`);
            }
          }
          const rawCursor = requestURL.searchParams.get("cursor");
          if (rawCursor !== null) {
            let cursor;
            try {
              if (rawCursor.length > 256 || !/^[A-Za-z0-9_-]+$/.test(rawCursor)) throw new Error();
              cursor = JSON.parse(Buffer.from(rawCursor, "base64url").toString());
              if (typeof cursor?.id !== "string" || !UUID.test(cursor.id) || !timestamp(cursor.at)) throw new Error();
            } catch { throw new APIError(400, "invalid_cursor"); }
            // Preserve Postgres microseconds; truncating through JS Date loses tied rows.
            query.set("or", `(completed_at.lt.${cursor.at},and(completed_at.eq.${cursor.at},id.lt.${cursor.id}))`);
          }
          const rows = await upstream(`/rest/v1/ekguru_attempts?${query}`, { token: auth.session.access });
          if (!Array.isArray(rows)) throw new APIError(502, "history_unavailable");
          const attempts = rows.slice(0, limit), last = attempts.at(-1);
          const next_cursor = rows.length > limit && last ? Buffer.from(JSON.stringify({ at: last.completed_at || last.created_at, id: last.id })).toString("base64url") : null;
          return send(200, { attempts, next_cursor });
        }
        if (req.method === "POST") {
          const attempt = validateAttempt(await readJSON(req));
          await upstream("/rest/v1/ekguru_attempts?on_conflict=id", {
            method: "POST", token: auth.session.access, body: { ...attempt, user_id: auth.user.id },
            headers: { Prefer: "resolution=ignore-duplicates,return=minimal" },
          });
          return send(201, { ok: true, id: attempt.id });
        }
        const id = requestURL.searchParams.get("id");
        if (!UUID.test(id || "")) throw new APIError(400, "invalid_attempt");
        await upstream(`/rest/v1/ekguru_attempts?id=eq.${id}&user_id=eq.${auth.user.id}`, { method: "DELETE", token: auth.session.access });
        return send(200, { ok: true });
      }
      const known = ["/api/auth/login", "/api/auth/callback", "/api/auth/logout", "/api/auth/session", "/api/attempts"].includes(path);
      return send(known ? 405 : 404, { error: known ? "method_not_allowed" : "not_found" }, known ? { Allow: path === "/api/auth/logout" ? "POST" : path === "/api/attempts" ? "GET, POST, DELETE" : "GET" } : {});
    } catch (error) {
      // No upstream text, keys, cookies, codes or PII is logged or reflected.
      return send(error instanceof APIError ? error.status : 500, { error: error instanceof APIError ? error.code : "internal_error" });
    }
  };
}

export default createHandler();
