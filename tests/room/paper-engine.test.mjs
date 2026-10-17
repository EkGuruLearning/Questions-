import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import { createDraft, gradePaper, paperAttempt, remainingSeconds, restoreDraft, validateSettings } from "../../assets/js/paper-engine.mjs";
import { validateAttempt } from "../../server/handler.mjs";

const NOW = 1792200000000;
const paper = { id: "paper-1", title: "Practice", fingerprint: "same-file-and-key", question_count: 5,
  options_count: 5, skip_option: "E", answer_key: { 1: ["A"], 2: ["B", "C"], 3: "DROP", 4: ["D"] } };
const settings = { count: 5, options: 5, mode: "exam", minutes: 10, marks: 2, negative: 0.5 };
const copy = (v) => JSON.parse(JSON.stringify(v));

test("grading supports negative marks, multiple accepted answers, dropped and unkeyed questions", () => {
  const draft = createDraft(paper, settings, NOW);
  draft.answers = { 1: "A", 2: "C", 3: "A", 4: "A", 5: "B" };
  const result = gradePaper(paper, draft);
  assert.equal(result.correct, 2); assert.equal(result.wrong, 1);
  assert.equal(result.score, 3.5); assert.equal(result.max_score, 6);
  assert.equal(result.keyed, 3); assert.equal(result.dropped, 1); assert.equal(result.ungraded, 1);
  assert.equal(result.answered, 5); assert.equal(result.review[2].status, "dropped");
});

test("no key means unscored, not fabricated 0% or zero marks", () => {
  const draft = createDraft(paper, settings, NOW); draft.answers = { 1: "A" };
  const result = gradePaper({ ...paper, answer_key: {} }, draft);
  assert.equal(result.score, null); assert.equal(result.max_score, null);
  assert.equal(result.correct, null); assert.equal(result.wrong, null);
  assert.equal(result.answered, 1); assert.equal(result.unanswered, 4);
});

test("explicit not-attempted option is a skip, not a wrong answer", () => {
  const draft = createDraft(paper, settings, NOW); draft.answers = { 1: "E" };
  const result = gradePaper(paper, draft);
  assert.equal(result.answered, 0); assert.equal(result.unanswered, 5);
  assert.equal(result.wrong, 0); assert.equal(result.review[0].status, "skipped");
  const fifth = { ...paper, skip_option: null, answer_key: { 1: ["E"] } };
  assert.equal(gradePaper(fifth, draft).correct, 1, "E is a real answer unless paper explicitly marks it as skip");
});

test("invalid answers are ignored by scoring and rejected by draft restore", () => {
  const draft = createDraft(paper, settings, NOW); draft.answers = { 1: "Z", 900: "A" };
  assert.equal(gradePaper(paper, draft).answered, 0);
  assert.equal(restoreDraft(draft, paper, NOW), null);
});

test("untimed and timed countdown use wall clock; background tabs cannot reset time", () => {
  const timed = createDraft(paper, settings, NOW);
  assert.equal(remainingSeconds(timed, NOW), 600);
  assert.equal(remainingSeconds(timed, NOW + 123456), 477);
  assert.equal(remainingSeconds(timed, NOW + 700000), 0);
  const untimed = createDraft(paper, { ...settings, minutes: 0 }, NOW);
  assert.equal(remainingSeconds(untimed, NOW + 700000), null);
});

test("resume preserves order, responses, review marks, PDF page and original deadline", () => {
  const draft = createDraft(paper, settings, NOW);
  draft.index = 2; draft.answers = { 1: "B", 2: "C" }; draft.marked = [2]; draft.visited = [1, 2, 3]; draft.pdf_page = 4;
  draft.deadline = NOW + 999999999;
  const restored = restoreDraft(copy(draft), paper, NOW + 300000);
  assert.deepEqual(restored.answers, draft.answers); assert.equal(restored.index, 2);
  assert.equal(restored.pdf_page, 4); assert.deepEqual(restored.marked, [2]);
  assert.equal(restored.deadline, NOW + 600000); assert.equal(remainingSeconds(restored, NOW + 300000), 300);
});

test("changed paper/key fingerprints and corrupt/outdated drafts cannot be resumed", () => {
  const draft = createDraft(paper, settings, NOW);
  for (const changes of [{ version: 99 }, { paper_id: "other" }, { fingerprint: "updated-key" }, { index: 5 },
    { marked: [-1] }, { started_at: NOW + 120000 }, { started_at: NOW - 8 * 86400000 }, { id: "not-uuid" }]) {
    assert.equal(restoreDraft({ ...draft, ...changes }, paper, NOW), null);
  }
  assert.equal(restoreDraft(null, paper, NOW), null);
});

test("question count, options and marking are bounded and finite", () => {
  for (const changes of [{ count: 0 }, { count: 301 }, { options: 6 }, { marks: 0 }, { marks: NaN },
    { negative: -1 }, { minutes: -1 }, { minutes: 361 }, { mode: "admin" }]) assert.throws(() => validateSettings({ ...settings, ...changes }));
  assert.throws(() => createDraft(paper, { ...settings, count: 4 }, NOW));
});

test("practice result payload fits the API contract and elapsed time stops at deadline", () => {
  const draft = createDraft(paper, settings, NOW, "a07a8170-ea16-4dd4-8ab3-e8fa19f1d800");
  draft.answers = { 1: "A", 2: "B" };
  const payload = paperAttempt(paper, draft, NOW + 999999);
  assert.equal(payload.duration_seconds, 600); assert.equal(payload.score, 4);
  assert.equal(validateAttempt(payload).id, draft.id);
  assert.equal(payload.user_id, undefined, "owner is never accepted as authorization in result payloads");
  assert.ok(validateAttempt(paperAttempt({ ...paper, answer_key: {} }, draft, NOW + 5000)));
});

test("provided-key transcription excludes the two known incomplete/conflicting reprint questions", () => {
  const manifest = JSON.parse(fs.readFileSync(new URL("../../data/practice/manifest.json", import.meta.url)));
  const rpsc = manifest.papers.find((p) => p.id === "rpsc-programmer-2024-paper-1");
  assert.equal(rpsc.question_count, 100); assert.equal(Object.keys(rpsc.answer_key).length, 98);
  assert.equal(rpsc.answer_key[3], undefined); assert.equal(rpsc.answer_key[5], undefined);
  assert.match(rpsc.key_label, /not independently verified/); assert.match(rpsc.key_note, /Q3/);
  assert.equal(manifest.papers.filter((p) => p.exam === "BCI").length, 2);
  assert.ok(manifest.papers.filter((p) => p.exam === "BCI").every((p) => !Object.keys(p.answer_key).length));
});
