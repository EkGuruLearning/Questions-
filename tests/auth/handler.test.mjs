import test from "node:test";
import assert from "node:assert/strict";
import { Readable } from "node:stream";
import { createHash } from "node:crypto";
import { createHandler, loadConfig, safeNext, validateAttempt } from "../../server/handler.mjs";
import { cookieName, parseCookies, readCookie, writeCookie } from "../../server/cookies.mjs";

const UID = "a07a8170-ea16-4dd4-8ab3-e8fa19f1d800";
const OTHER = "9da10d8f-48a8-413a-bb51-c9a70b8b7fa2";
const ID = "ec7b6860-83fa-4f1c-ae42-7d17a9c05a1e";
const ORIGIN = "https://ekguru.example";
const ENV = { APP_ORIGIN: ORIGIN, SUPABASE_URL: "https://project.supabase.co", SUPABASE_PUBLISHABLE_KEY: "sb_publishable_test", SESSION_SECRET: "a-unique-unit-test-session-secret-at-least-32-characters" };
const TIME = 1792200000000;
const user = { id: UID, email: "student@example.test", user_metadata: { full_name: "A <Student>" } };
const tokens = { access_token: "test-access-DO-NOT-EXPOSE", refresh_token: "test-refresh-DO-NOT-EXPOSE", expires_in: 3600 };
const json = (data, status = 200) => new Response(JSON.stringify(data), { status, headers: { "Content-Type": "application/json" } });
const cookieHeader = (setCookies = []) => setCookies.filter((line) => !line.includes("Max-Age=0")).map((line) => line.split(";", 1)[0]).join("; ");
const sessionCookie = (overrides = {}) => cookieHeader(writeCookie("session", { access: tokens.access_token, refresh: tokens.refresh_token,
  expires: TIME + 3600000, until: TIME + 86400000, ...overrides }, ENV.SESSION_SECRET));
const attempt = (overrides = {}) => ({ id: ID, kind: "paper", paper_id: "paper-2024", label: "Practice paper", total: 3,
  correct: 1, wrong: 1, unanswered: 1, score: 0.75, max_score: 3, duration_seconds: 60, details: {}, ...overrides });

function setup({ fetcher, env = ENV, now = () => TIME } = {}) {
  const calls = [];
  const handler = createHandler({ env, now, fetcher: async (url, options) => {
    calls.push({ url, ...options });
    if (fetcher) return fetcher(url, options);
    if (url.endsWith("/settings")) return json({ external: { google: true } });
    if (url.includes("/token?")) return json(tokens);
    if (url.endsWith("/user")) return json(user);
    if (url.includes("/rest/v1/")) return options.method === "GET" ? json([]) : new Response(null, { status: 204 });
    if (url.includes("/logout?")) return new Response(null, { status: 204 });
    throw new Error("Unexpected mock endpoint: " + url);
  } });
  async function request(url, { method = "GET", cookie = "", headers = {}, body, rawBody, chunks } = {}) {
    const req = Readable.from((chunks || (rawBody !== undefined ? [rawBody] : body !== undefined ? [JSON.stringify(body)] : [])).map((chunk) => Buffer.from(chunk)));
    req.url = url; req.method = method;
    req.headers = { ...(cookie ? { cookie } : {}), ...(body !== undefined ? { "content-type": "application/json" } : {}), ...headers };
    let status, resultHeaders, raw = "";
    const res = { writeHead(code, value) { status = code; resultHeaders = value; }, end(value) { raw = value || ""; } };
    await handler(req, res);
    return { status, headers: resultHeaders, raw, data: raw ? JSON.parse(raw) : null };
  }
  return { request, calls };
}
const writeHeaders = { origin: ORIGIN, "x-ekguru-csrf": "1", "x-ekguru-user": UID };

async function loginFlow(harness, next = "/subjects/test-room/index.html") {
  const login = await harness.request(`/api/auth/login?next=${encodeURIComponent(next)}`);
  const authorize = new URL(login.headers.Location);
  const callback = new URL(authorize.searchParams.get("redirect_to"));
  callback.searchParams.set("code", "one-time-code");
  return { login, authorize, callback, cookie: cookieHeader(login.headers["Set-Cookie"]) };
}

test("unconfigured guest session works without contacting Supabase", async () => {
  const { request, calls } = setup({ env: {} });
  const response = await request("/api/auth/session");
  assert.equal(response.status, 200); assert.equal(response.data.configured, false);
  assert.equal(response.data.user, null); assert.equal(calls.length, 0);
  assert.match(response.headers["Cache-Control"], /private, no-store/);
});

test("config rejects insecure origins, path origins, short secrets and privileged keys", () => {
  assert.ok(loadConfig(ENV));
  for (const changes of [{ APP_ORIGIN: "http://ekguru.example" }, { APP_ORIGIN: ORIGIN + "/path" }, { APP_ORIGIN: "https://user:password@ekguru.example" },
    { SESSION_SECRET: "short" }, { SUPABASE_URL: "http://project.supabase.co" }, { SUPABASE_PUBLISHABLE_KEY: "sb_secret_never_use" },
    { SUPABASE_PUBLISHABLE_KEY: "eyJ." + Buffer.from(JSON.stringify({ role: "service_role" })).toString("base64url") + ".sig" }]) {
    assert.equal(loadConfig({ ...ENV, ...changes }), null);
  }
  assert.ok(loadConfig({ ...ENV, APP_ORIGIN: "http://localhost:8000", ALLOW_INSECURE_LOCALHOST: "true" }));
});

test("redirect destinations stay on published subject index pages", () => {
  for (const input of ["https://evil.test/subjects/test-room/index.html", "//evil.test/", "/\\evil.test/", "/api/auth/logout", "/subjects/../api/index.html", "/subjects/a/index.html\r\nLocation:bad"]) {
    assert.equal(safeNext(input, ORIGIN), "/subjects/test-room/index.html");
  }
  assert.equal(safeNext("/subjects/computer-network/test/index.html?topic=T01", ORIGIN), "/subjects/computer-network/test/index.html?topic=T01");
});

test("Google login uses PKCE, state and short-lived encrypted Secure HttpOnly cookies", async () => {
  const harness = setup();
  const { login, authorize, callback, cookie } = await loginFlow(harness);
  assert.equal(login.status, 303);
  assert.equal(authorize.origin, "https://project.supabase.co");
  assert.equal(authorize.searchParams.get("provider"), "google");
  assert.equal(authorize.searchParams.get("code_challenge_method"), "s256");
  const flow = readCookie(parseCookies(cookie), "oauth", ENV.SESSION_SECRET);
  assert.equal(createHash("sha256").update(flow.verifier).digest("base64url"), authorize.searchParams.get("code_challenge"));
  assert.equal(callback.searchParams.get("state"), flow.state);
  assert.equal(flow.until, TIME + 600000);
  for (const item of login.headers["Set-Cookie"].filter((v) => !v.includes("Max-Age=0"))) {
    assert.match(item, /^__Host-/); assert.match(item, /HttpOnly; SameSite=Lax; Max-Age=600; Secure/);
    assert.ok(!item.includes(flow.verifier));
  }
  const result = await harness.request(callback.pathname + callback.search, { cookie });
  assert.equal(result.status, 303); assert.equal(result.headers.Location, "/subjects/test-room/index.html");
  assert.ok(result.headers["Set-Cookie"].some((item) => item.startsWith(cookieName("session") + ".n=")));
  assert.ok(result.headers["Set-Cookie"].some((item) => item.includes("Max-Age=2592000")));
  assert.ok(!JSON.stringify(result.headers).includes(tokens.access_token));
  assert.ok(!JSON.stringify(result.headers).includes(tokens.refresh_token));
  const exchange = harness.calls.find((call) => call.url.includes("grant_type=pkce"));
  assert.deepEqual(JSON.parse(exchange.body), { auth_code: "one-time-code", code_verifier: flow.verifier });
});

test("callback rejects missing/tampered/expired state before exchanging a code", async () => {
  const h = setup(); const { callback, cookie } = await loginFlow(h);
  for (const badCookie of ["", cookie.replace(/=./, "=X")]) {
    const response = await h.request(callback.pathname + callback.search, { cookie: badCookie });
    assert.match(response.headers.Location, /login_expired/);
  }
  callback.searchParams.set("state", "wrong-state");
  const bad = await h.request(callback.pathname + callback.search, { cookie });
  assert.match(bad.headers.Location, /login_expired/);
  assert.equal(h.calls.filter((call) => call.url.includes("grant_type=pkce")).length, 0);
  const expired = cookieHeader(writeCookie("oauth", { until: TIME - 1, state: "state", verifier: "verifier" }, ENV.SESSION_SECRET));
  assert.match((await h.request("/api/auth/callback?code=code&state=state", { cookie: expired })).headers.Location, /login_expired/);
});

test("disabled Google provider is an honest setup-pending redirect, not a broken OAuth URL", async () => {
  const h = setup({ fetcher: async () => json({ external: { google: false } }) });
  const response = await h.request("/api/auth/login");
  assert.equal(response.headers.Location, "/subjects/account/index.html?error=google_setup_required");
  assert.equal(response.headers["Set-Cookie"], undefined);
});

test("session exposes only the safe summary, refreshes expiring tokens and verifies getUser", async () => {
  const h = setup();
  const response = await h.request("/api/auth/session", { cookie: sessionCookie({ expires: TIME + 1000 }) });
  assert.equal(response.status, 200); assert.deepEqual(response.data.user, { id: UID, email: user.email, name: user.user_metadata.full_name });
  assert.equal(h.calls.filter((call) => call.url.includes("grant_type=refresh_token")).length, 1);
  assert.ok(h.calls.some((call) => call.url.endsWith("/user")));
  assert.ok(!response.raw.includes(tokens.access_token));
  assert.ok(!response.raw.includes(tokens.refresh_token));
  assert.ok(response.headers["Set-Cookie"]);
});

test("temporary upstream failures never clear a valid session or reflect upstream secrets", async () => {
  const h = setup({ fetcher: async () => json({ message: "private upstream detail SECRET" }, 503) });
  const response = await h.request("/api/auth/session", { cookie: sessionCookie() });
  assert.equal(response.status, 503); assert.equal(response.headers["Set-Cookie"], undefined);
  assert.deepEqual(response.data, { error: "service_unavailable" }); assert.ok(!response.raw.includes("SECRET"));
});

test("invalid refresh clears cookies and returns guest instead of trusting stored tokens", async () => {
  const h = setup({ fetcher: async (url) => url.endsWith("/settings") ? json({ external: { google: true } }) : json({ message: "invalid" }, 400) });
  const response = await h.request("/api/auth/session", { cookie: sessionCookie({ expires: TIME - 1 }) });
  assert.equal(response.data.user, null);
  assert.ok(response.headers["Set-Cookie"].every((line) => line.includes("Max-Age=0")));
});

test("write CSRF rejects cross-origin and missing custom header, without touching history", async () => {
  for (const headers of [{ origin: "https://evil.test", "x-ekguru-csrf": "1" }, { origin: ORIGIN }, {}]) {
    const h = setup(); const response = await h.request("/api/attempts", { method: "POST", cookie: sessionCookie(), headers, body: attempt() });
    assert.equal(response.status, 403); assert.equal(h.calls.length, 0);
  }
});

test("history requires verified login, binds to JWT user, ignores caller user_id and is idempotent", async () => {
  const h = setup();
  assert.equal((await h.request("/api/attempts")).status, 401);
  const response = await h.request("/api/attempts", { method: "POST", cookie: sessionCookie(), headers: writeHeaders, body: attempt({ user_id: OTHER, created_at: "2099-01-01" }) });
  assert.equal(response.status, 201);
  const call = h.calls.find((item) => item.url.includes("/rest/v1/"));
  assert.equal(JSON.parse(call.body).user_id, UID); assert.equal(JSON.parse(call.body).created_at, undefined);
  assert.equal(call.headers.Authorization, `Bearer ${tokens.access_token}`);
  assert.equal(call.headers.apikey, ENV.SUPABASE_PUBLISHABLE_KEY);
  assert.equal(call.headers.Prefer, "resolution=ignore-duplicates,return=minimal");
});

test("account-switch race cannot upload an old draft to a newly signed-in user's account", async () => {
  const h = setup();
  const response = await h.request("/api/attempts", { method: "POST", cookie: sessionCookie(), headers: { ...writeHeaders, "x-ekguru-user": OTHER }, body: attempt() });
  assert.equal(response.status, 409); assert.equal(response.data.error, "account_changed");
  assert.equal(h.calls.filter((call) => call.url.includes("/rest/v1/")).length, 0);
});

test("history list and deletion always include the authenticated user filter", async () => {
  const h = setup();
  assert.equal((await h.request("/api/attempts", { cookie: sessionCookie(), headers: { "x-ekguru-user": UID } })).status, 200);
  assert.equal((await h.request(`/api/attempts?id=${ID}`, { method: "DELETE", cookie: sessionCookie(), headers: writeHeaders })).status, 200);
  for (const call of h.calls.filter((call) => call.url.includes("/rest/v1/"))) assert.equal(new URL(call.url).searchParams.get("user_id"), `eq.${UID}`);
  assert.equal((await h.request("/api/attempts?id=not-a-uuid", { method: "DELETE", cookie: sessionCookie(), headers: writeHeaders })).status, 400);
});

test("attempt validator supports unkeyed/partial scoring but rejects corrupt totals or unbounded payloads", () => {
  assert.ok(validateAttempt(attempt({ correct: null, wrong: null, score: null, max_score: null })));
  assert.ok(validateAttempt(attempt({ total: 100, unanswered: 98 })));
  assert.ok(validateAttempt(attempt({ kind: "cn", total: 1554, unanswered: 1552, max_score: 1554 })));
  for (const changes of [{ total: 0 }, { total: 301 }, { unanswered: -1 }, { correct: 3 }, { correct: null }, { score: 4 },
    { score: Infinity }, { id: "bad" }, { kind: "admin" }, { duration_seconds: 99999999 }, { details: { big: "x".repeat(16001) } }]) {
    assert.throws(() => validateAttempt(attempt(changes)));
  }
});

test("API rejects invalid JSON, wrong media type and oversized bodies", async () => {
  const h = setup(); const base = { method: "POST", cookie: sessionCookie(), headers: writeHeaders };
  assert.equal((await h.request("/api/attempts", { ...base, rawBody: "{}" })).status, 415);
  assert.equal((await h.request("/api/attempts", { ...base, headers: { ...writeHeaders, "content-type": "application/json" }, rawBody: "{" })).status, 400);
  assert.equal((await h.request("/api/attempts", { ...base, body: attempt({ details: { big: "x".repeat(25000) } }) })).status, 413);
});

test("logout clears both cookies even if upstream revocation fails", async () => {
  const h = setup({ fetcher: async () => { throw new Error("network offline"); } });
  assert.equal((await h.request("/api/auth/logout", { method: "POST", cookie: sessionCookie() })).status, 403);
  const response = await h.request("/api/auth/logout", { method: "POST", cookie: sessionCookie(), headers: writeHeaders });
  assert.equal(response.status, 200); assert.equal(response.data.ok, true);
  assert.equal(response.headers["Set-Cookie"].length, 10);
  assert.ok(response.headers["Set-Cookie"].every((line) => line.includes("Max-Age=0")));
});

test("Build Output API's captured path dispatches to the same handler", async () => {
  const h = setup();
  const response = await h.request("/api?__path=auth/session");
  assert.equal(response.status, 200); assert.equal(response.data.google_enabled, true);
  assert.equal((await h.request("/api/does-not-exist")).status, 404);
});
