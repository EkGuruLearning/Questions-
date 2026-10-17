import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import { createQuizDraft, restoreQuizDraft, gradeQuestion, gradeQuiz, quizRemaining, quizAttempt } from "../../assets/js/quiz-engine.mjs";
import { validateAttempt } from "../../server/handler.mjs";
const NOW = Date.parse("2026-10-17T00:00:00Z");
const ID = "c73434a3-bf4b-45f9-a1d4-e6a3e680a199";
const USER = "46f32a78-d05e-44ad-b064-2978523db855";
const options = ["A", "B", "C", "D", "E"].map((id) => ({ id, text: id }));
const definition = () => ({ id: "mixed", subject_id: "future-subject", title: "Mixed types", fingerprint: "same-data", kind: "quiz", duration_minutes: 10, questions: [
  { id: "1", text: "Single", type: "single", options, marks: 2, negative: .5, answer: ["A"], skip_option: "E" },
  { id: "2", text: "Multiple", type: "multiple", options, marks: 2, negative: 0, answer: ["B", "D"] },
  { id: "3", text: "Numeric", type: "numeric", marks: 2, negative: 0, answer_range: [1.42, 1.45] },
  { id: "4", text: "Unkeyed", type: "single", options, marks: 1, negative: 0 },
] });
const clone = (value) => structuredClone(value);

test("all subjects: single/MSQ/numeric scoring and partial keys are truthful", () => {
  const bank = definition(), draft = createQuizDraft(bank, {}, NOW, USER, ID);
  draft.answers = { 1: "A", 2: ["D", "B"], 3: "1.43", 4: "C" };
  const result = gradeQuiz(bank, draft);
  assert.equal(result.score, 6); assert.equal(result.max_score, 6); assert.equal(result.correct, 3); assert.equal(result.ungraded, 1);
  assert.equal(result.answered, 4); assert.equal(result.review[3].status, "ungraded");
  const payload = validateAttempt(quizAttempt(bank, draft, NOW + 900000));
  assert.equal(payload.subject_id, "future-subject"); assert.equal(payload.test_id, "mixed");
  assert.equal(payload.duration_seconds, 600); assert.equal(payload.completed_at, new Date(NOW + 900000).toISOString());
});

test("MSQ requires the exact set, not partial-credit or MCQ alternatives", () => {
  const q = definition().questions[1];
  for (const value of ["B", ["B"], ["B", "D", "A"], ["B", "B"], ["X"]]) assert.notEqual(gradeQuestion(q, value).status, "correct");
  assert.equal(gradeQuestion(q, ["D", "B"]).status, "correct");
});

test("numeric range boundaries, negative/zero and scientific notation work; invalid values are unanswered", () => {
  const q = definition().questions[2];
  for (const value of ["1.42", "1.45", "1.43e0", "+1.430"]) assert.equal(gradeQuestion(q, value).status, "correct");
  for (const value of ["", "-", "NaN", "Infinity", "1/2", "1,43", "1e99", " "]) assert.equal(gradeQuestion(q, value).answered, false);
  assert.equal(gradeQuestion({ ...q, answer_range: [-.5, -.5] }, "-0.5").status, "correct");
  assert.equal(gradeQuestion({ ...q, answer_range: [0, 0] }, "0").status, "correct");
});

test("E skip is unanswered, negative marking is per-question and MCQ alternatives are accepted", () => {
  const q = definition().questions[0];
  assert.equal(gradeQuestion(q, "E").status, "skipped");
  assert.equal(gradeQuestion(q, "B").score, -.5);
  assert.equal(gradeQuestion({ ...q, answer: ["A", "C"] }, "C").status, "correct");
});

test("no reliable keys yields null marks/counters, not a fabricated zero percent", () => {
  const bank = definition(); bank.questions.forEach((q) => { delete q.answer; delete q.answer_range; });
  const draft = createQuizDraft(bank, {}, NOW, null, ID), result = gradeQuiz(bank, draft);
  assert.equal(result.score, null); assert.equal(result.max_score, null); assert.equal(result.correct, null); assert.equal(result.wrong, null);
  assert.equal(result.unanswered, 4); assert.ok(validateAttempt(quizAttempt(bank, draft, NOW + 1000)));
});

test("resume is fingerprint-, test-, subject- and owner-bound; deadlines cannot be extended", () => {
  const bank = definition(), draft = createQuizDraft(bank, {}, NOW, USER, ID);
  draft.answers = { 1: "A", 2: ["D", "B"], 3: "1.43" }; draft.index = 2; draft.marked = [0, 2]; draft.visited = [0, 1, 2];
  const raw = { ...clone(draft), deadline: NOW + 86400000 };
  const restored = restoreQuizDraft(raw, bank, USER, NOW + 120000);
  assert.equal(restored.deadline, NOW + 600000); assert.equal(quizRemaining(restored, NOW + 120000), 480);
  assert.equal(quizRemaining(restored, NOW + 800000), 0); assert.equal(restored.id, ID);
  assert.deepEqual(restored.answers[2], ["B", "D"]);
  for (const patch of [{ owner: null }, { test_id: "other" }, { subject_id: "other" }, { fingerprint: "new-key" }, { id: "bad" }, { index: 99 }, { marked: [-1] }, { visited: [5] }, { answers: { 3: "NaN" } }, { started_at: NOW + 120000 }, { started_at: NOW - 8 * 86400000 }]) assert.equal(restoreQuizDraft({ ...raw, ...patch }, bank, USER, NOW), null);
});

test("untimed drafts have no deadline, 150+ answer payloads stay bounded and UUIDs are idempotent", () => {
  const bank = definition(); bank.questions = Array.from({ length: 500 }, (_, i) => ({ ...bank.questions[0], id: String(i + 1) }));
  const draft = createQuizDraft(bank, { minutes: 0, mode: "practice" }, NOW, null, ID);
  assert.equal(quizRemaining(draft, NOW + 999999), null);
  const payload = quizAttempt(bank, draft, NOW + 10000);
  assert.equal(payload.details.answers_saved, false); assert.equal(payload.details.answers, undefined);
  assert.equal(quizAttempt(bank, draft).id, ID); assert.ok(validateAttempt(payload));
});

test("native RPSC transcription has every option, preserves skip and excludes Q3/Q5; other subject samples are real", () => {
  const bank = JSON.parse(fs.readFileSync(new URL("../../data/tests/previous-year-papers/rpsc-programmer-2024-paper-1.test.json", import.meta.url)));
  assert.equal(bank.questions.length, 100);
  assert.equal(bank.questions.filter((q) => q.answer).length, 98);
  for (const [index, q] of bank.questions.entries()) { assert.equal(q.options.length, 5, `Q${index + 1}`); assert.equal(q.skip_option, "E"); assert.ok(q.text); }
  assert.equal(bank.questions[2].answer, undefined); assert.equal(bank.questions[4].answer, undefined);
  const reasoning = JSON.parse(fs.readFileSync(new URL("../../data/tests/reasoning/mixed-10.test.json", import.meta.url)));
  assert.equal(reasoning.questions.length, 10); assert.equal(reasoning.questions[5].answer, undefined); assert.match(reasoning.questions[5].notice, /Ungraded/);
});
