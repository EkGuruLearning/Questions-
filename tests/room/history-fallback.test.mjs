import test from "node:test";
import assert from "node:assert/strict";
import { historyStore } from "../../assets/js/history-store.mjs";
// This process intentionally has no IndexedDB: exercise honest memory-only mode.
const row = (n) => ({ id: `f0000000-0000-4000-8000-${String(n).padStart(12, "0")}`, kind: "quiz", subject_id: "reasoning", test_id: `test-${n}`, label: `Attempt ${n}`,
  completed_at: "2026-10-17T00:00:00.000Z", total: 1, correct: 0, wrong: 0, unanswered: 1, score: 0, max_score: 1, duration_seconds: 1, details: {} });
test("blocked/unsupported IndexedDB stays usable but never claims persistence; >20 pending rows remain available", async () => {
  assert.equal(typeof globalThis.indexedDB, "undefined");
  for (let n = 1; n <= 60; n++) await historyStore.record("account-a", row(n), true);
  assert.equal(historyStore.durable, false);
  assert.equal((await historyStore.pending("account-a", 100)).length, 60);
  assert.equal((await historyStore.page("guest")).attempts.length, 0);
  assert.equal((await historyStore.page("account-b")).attempts.length, 0);
  const first = await historyStore.page("account-a"), second = await historyStore.page("account-a", { before: first.next_cursor });
  assert.equal(first.attempts.length, 50); assert.equal(second.attempts.length, 10);
  await historyStore.acknowledge("account-a", row(1).id);
  assert.equal((await historyStore.pending("account-a", 100)).length, 59);
  await historyStore.remove("account-a", row(2).id);
  assert.equal((await historyStore.pending("account-a", 100)).length, 58);
});
