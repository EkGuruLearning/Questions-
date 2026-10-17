import test from "node:test";
import assert from "node:assert/strict";
import { clearCookie, cookieName, parseCookies, readCookie, seal, unseal, writeCookie } from "../../server/cookies.mjs";

const secret = "test-secret-please-never-reuse-in-production-123";
const value = { access: "token", refresh: "private-refresh", expires: 1792200000 };
const header = (lines) => lines.filter((line) => !line.includes("Max-Age=0")).map((line) => line.split(";", 1)[0]).join("; ");

test("encrypted cookies round-trip but reveal no raw auth token", () => {
  const one = seal(value, secret, "session"), two = seal(value, secret, "session");
  assert.notEqual(one, two, "every write needs a fresh IV");
  assert.deepEqual(unseal(one, secret, "session"), value);
  assert.equal(unseal(one, secret, "oauth"), null, "cookie purposes are authenticated");
  assert.equal(unseal(one, "wrong secret", "session"), null);
  const at = Math.floor(one.length / 2);
  assert.equal(unseal(one.slice(0, at) + (one[at] === "A" ? "B" : "A") + one.slice(at + 1), secret, "session"), null);
  assert.ok(!one.includes(value.refresh));
});

test("large but bounded auth sessions are chunked below per-cookie limits", () => {
  const large = { ...value, access: "x".repeat(6000) };
  const lines = writeCookie("session", large, secret);
  assert.ok(lines.every((line) => Buffer.byteLength(line) < 4096));
  assert.deepEqual(readCookie(parseCookies(header(lines)), "session", secret), large);
  assert.throws(() => writeCookie("session", { access: "x".repeat(12000) }, secret));
});

test("missing chunks, oversized ciphertext and malformed count are rejected", () => {
  const cookies = parseCookies(header(writeCookie("session", value, secret)));
  delete cookies[cookieName("session") + ".0"];
  assert.equal(readCookie(cookies, "session", secret), null);
  assert.equal(readCookie({ [cookieName("session") + ".n"]: "999999" }, "session", secret), null);
  assert.equal(unseal("!not-base64", secret, "session"), null);
  assert.equal(unseal("x".repeat(12001), secret, "session"), null);
});

test("HttpOnly + Secure + SameSite=Lax + host-only + path=/; local HTTP is explicit", () => {
  for (const line of writeCookie("session", value, secret)) {
    assert.match(line, /^__Host-ekguru-session\./); assert.match(line, /; Secure$/);
    assert.match(line, /Path=\/; HttpOnly; SameSite=Lax;/); assert.ok(!line.includes("Domain="));
  }
  const local = writeCookie("session", value, secret, false);
  assert.ok(local.every((line) => !line.includes("; Secure") && !line.startsWith("__Host-")));
  assert.deepEqual(readCookie(parseCookies(header(local)), "session", secret, false), value);
  assert.ok(clearCookie("session").every((line) => line.includes("Max-Age=0")));
});

test("cookie parsing is bounded by fixed names and ignores inherited/prototype names", () => {
  const parsed = parseCookies("foo=one; foo=two; __proto__=not-a-prototype; constructor=safe; invalid");
  assert.equal(Object.getPrototypeOf(parsed), null);
  assert.equal(parsed.foo, "one");
  assert.equal(parsed.__proto__, "not-a-prototype");
  assert.equal(readCookie(parsed, "session", secret), null);
});
