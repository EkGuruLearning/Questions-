/* Server-only encrypted, authenticated, HttpOnly cookies. No tokens in browser JS.
   AES-GCM uses a fresh IV per write. Chunks keep each cookie below browser limits. */
import { createCipheriv, createDecipheriv, createHash, randomBytes } from "node:crypto";

const CHUNK_SIZE = 3000;
const MAX_CHUNKS = 4;
export const SESSION_SECONDS = 30 * 24 * 60 * 60;
export const OAUTH_SECONDS = 10 * 60;

export function parseCookies(header = "") {
  const result = Object.create(null);
  for (const item of String(header).split(";")) {
    const at = item.indexOf("=");
    if (at < 1) continue;
    const name = item.slice(0, at).trim();
    if (!Object.hasOwn(result, name)) result[name] = item.slice(at + 1).trim();
  }
  return result;
}

export function seal(value, secret, purpose) {
  const key = createHash("sha256").update(secret).digest();
  const iv = randomBytes(12);
  const cipher = createCipheriv("aes-256-gcm", key, iv);
  cipher.setAAD(Buffer.from(purpose));
  const encrypted = Buffer.concat([cipher.update(JSON.stringify(value), "utf8"), cipher.final()]);
  return Buffer.concat([iv, cipher.getAuthTag(), encrypted]).toString("base64url");
}

export function unseal(value, secret, purpose) {
  try {
    if (typeof value !== "string" || value.length > CHUNK_SIZE * MAX_CHUNKS || !/^[\w-]+$/.test(value)) return null;
    const raw = Buffer.from(value, "base64url");
    if (raw.length < 29) return null;
    const key = createHash("sha256").update(secret).digest();
    const decipher = createDecipheriv("aes-256-gcm", key, raw.subarray(0, 12));
    decipher.setAAD(Buffer.from(purpose));
    decipher.setAuthTag(raw.subarray(12, 28));
    return JSON.parse(Buffer.concat([decipher.update(raw.subarray(28)), decipher.final()]).toString("utf8"));
  } catch { return null; }
}

export function cookieName(kind, secure = true) {
  return `${secure ? "__Host-" : ""}ekguru-${kind}`;
}

function serialize(name, value, maxAge, secure) {
  return `${name}=${value}; Path=/; HttpOnly; SameSite=Lax; Max-Age=${maxAge}${secure ? "; Secure" : ""}`;
}

export function readCookie(cookies, kind, secret, secure = true) {
  const name = cookieName(kind, secure);
  const count = Number(cookies[`${name}.n`]);
  if (!Number.isInteger(count) || count < 1 || count > MAX_CHUNKS) return null;
  const chunks = Array.from({ length: count }, (_, i) => cookies[`${name}.${i}`]);
  if (chunks.some((chunk) => !chunk || chunk.length > CHUNK_SIZE)) return null;
  return unseal(chunks.join(""), secret, kind);
}

export function writeCookie(kind, value, secret, secure = true, maxAge = SESSION_SECONDS) {
  const name = cookieName(kind, secure);
  const encrypted = seal(value, secret, kind);
  const count = Math.ceil(encrypted.length / CHUNK_SIZE);
  if (count > MAX_CHUNKS) throw new Error("Session exceeds safe cookie size");
  return [
    serialize(`${name}.n`, String(count), maxAge, secure),
    ...Array.from({ length: MAX_CHUNKS }, (_, i) => serialize(
      `${name}.${i}`, i < count ? encrypted.slice(i * CHUNK_SIZE, (i + 1) * CHUNK_SIZE) : "", i < count ? maxAge : 0, secure,
    )),
  ];
}

export function clearCookie(kind, secure = true) {
  const name = cookieName(kind, secure);
  return [serialize(`${name}.n`, "", 0, secure), ...Array.from({ length: MAX_CHUNKS }, (_, i) => serialize(`${name}.${i}`, "", 0, secure))];
}
