import "fake-indexeddb/auto";
import test from "node:test";
import assert from "node:assert/strict";
import { historyStore, normalizeAttempt } from "../../assets/js/history-store.mjs";
const A = "a07a8170-ea16-4dd4-8ab3-e8fa19f1d800", B = "9da10d8f-48a8-413a-bb51-c9a70b8b7fa2";
const id = (n) => `f0000000-0000-4000-8000-${String(n).padStart(12, "0")}`;
const attempt = (n, changes = {}) => ({ id: id(n), kind: "quiz", subject_id: `subject-${n % 50}`, test_id: `test-${n}`, label: `Result ${n}`,
  total: 20, unanswered: 20, correct: null, wrong: null, score: null, max_score: null, duration_seconds: 10,
  completed_at: "2026-10-17T10:00:00.000Z", details: { answers: { 1: "A" } }, ...changes });

async function all(owner, filters = {}) {
  const rows = []; let cursor = null;
  do { const page = await historyStore.page(owner, { ...filters, before: cursor }); rows.push(...page.attempts); cursor = page.next_cursor; } while (cursor);
  return rows;
}

test("IndexedDB keeps 550+ results and pending uploads across 50 subjects/550 tests with stable tied-time paging", async () => {
  await Promise.all(Array.from({ length: 550 }, (_, i) => historyStore.record(A, attempt(i + 1), true)));
  const rows = await all(A);
  assert.equal(rows.length, 550); assert.equal(new Set(rows.map((row) => row.id)).size, 550);
  assert.equal(new Set(rows.map((row) => row.subject_id)).size, 50);
  assert.equal(new Set(rows.map((row) => row.test_id)).size, 550);
  assert.equal(historyStore.durable, true);
  assert.equal((await historyStore.pending(A, 1000)).length, 550);
  assert.equal(rows[0].id, id(550)); assert.equal(rows.at(-1).id, id(1));
});

test("subject and test filters can reach old attempts, with or without subject, not just the latest fifty", async () => {
  assert.equal((await all(A, { subject: "subject-1" })).length, 11);
  assert.equal((await all(A, { subject: "subject-1", test: "test-1" }))[0].id, id(1));
  assert.equal((await all(A, { test: "test-1" }))[0].id, id(1));
  assert.equal((await all(A, { test: "does-not-exist" })).length, 0);
});

test("compound owner/UUID keys isolate guest/A/B, even with the same attempt UUID", async () => {
  await historyStore.record(B, attempt(1, { label: "B private" }), true);
  await historyStore.record("guest", attempt(1, { label: "Guest private" }), true);
  assert.equal((await historyStore.page(B)).attempts[0].label, "B private");
  assert.equal((await historyStore.page("guest")).attempts[0].label, "Guest private");
  assert.equal((await historyStore.pending("guest")).length, 0, "guest records must never silently upload");
  assert.equal((await historyStore.pending(B)).length, 1);
  assert.equal((await all(A)).find((row) => row.id === id(1)).label, "Result 1");
});

test("duplicate finish/retry cannot create or overwrite a result; ack drops only outbox details", async () => {
  await historyStore.record(A, attempt(1, { label: "Must not overwrite" }), true);
  await historyStore.acknowledge(A, id(1));
  assert.equal((await all(A)).length, 550);
  const row = (await all(A, { test: "test-1" }))[0];
  assert.equal(row.label, "Result 1"); assert.deepEqual(row.details, {});
  assert.equal(Object.hasOwn(row, "owner"), false); assert.equal(Object.hasOwn(row, "pending"), false);
  assert.equal((await historyStore.pending(A, 1000)).length, 549);
  assert.equal((await historyStore.pending(B)).length, 1, "ack cannot touch another owner");
});

test("device deletion is owner-scoped, and pending IDs never get dropped at a queue length of twenty", async () => {
  await historyStore.remove(B, id(1));
  assert.equal((await all(B)).length, 0);
  assert.equal((await all(A)).length, 550);
  assert.equal((await historyStore.pending(A, 1000)).length, 549);
});

test("legacy IDs/date upgrade safely; universal quiz identifiers are mandatory and timezone dates normalize", () => {
  const legacy = normalizeAttempt({ ...attempt(999), kind: "cn", subject_id: undefined, test_id: undefined, paper_id: "cn-mixed-20", completed_at: "2026-10-17T15:30:00+05:30" });
  assert.equal(legacy.subject_id, "computer-network"); assert.equal(legacy.test_id, "cn-mixed-20"); assert.equal(legacy.completed_at, "2026-10-17T10:00:00.000Z");
  assert.throws(() => normalizeAttempt(attempt(999, { subject_id: undefined })), /subject_id/);
  assert.throws(() => normalizeAttempt(attempt(999, { test_id: undefined })), /test_id/);
  assert.throws(() => normalizeAttempt(attempt(999, { completed_at: "bad" })), /Invalid/);
});
