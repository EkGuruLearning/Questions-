import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  STATUS,
  filterQuestions,
  gradeAttempt,
  isPracticeEligible,
  localizeText,
  sampleQuestions,
  verificationLabel,
} from "../../assets/js/engine.mjs";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const BANK_PATH = path.resolve(HERE, "../../assets/cn-questions.min.json");
const canonicalPublicBank = JSON.parse(fs.readFileSync(BANK_PATH, "utf8"));
const clone = (item, changes = {}) => ({ ...item, ...changes });

test("default practice eligibility excludes claimed, disputed and pending records", () => {
  const source = canonicalPublicBank[0];
  const answerChecked = clone(source, { verification_status: STATUS.ANSWER_CHECKED });
  const official = clone(source, { verification_status: STATUS.OFFICIAL });
  const claimed = clone(source, { verification_status: STATUS.CLAIMED_UNVERIFIED });
  const disputed = clone(source, { verification_status: STATUS.DISPUTED });
  const pending = clone(source, { verification_status: STATUS.PENDING });
  assert.equal(isPracticeEligible(answerChecked), true);
  assert.equal(isPracticeEligible(official), true);
  assert.equal(isPracticeEligible(claimed), false);
  assert.equal(isPracticeEligible(disputed), false);
  assert.equal(isPracticeEligible(pending), false);
  assert.deepEqual(filterQuestions([answerChecked, official, claimed, disputed, pending]).map((q) => q.verification_status), [STATUS.ANSWER_CHECKED, STATUS.OFFICIAL]);
  assert.deepEqual(filterQuestions([answerChecked, official, claimed, disputed, pending], { verificationStatus: "all_practice" }).map((q) => q.verification_status), [STATUS.ANSWER_CHECKED, STATUS.OFFICIAL, STATUS.CLAIMED_UNVERIFIED]);
  assert.deepEqual(filterQuestions([answerChecked, official, claimed], { verificationStatus: STATUS.CLAIMED_UNVERIFIED }).map((q) => q.verification_status), [STATUS.CLAIMED_UNVERIFIED]);
  assert.equal(filterQuestions([disputed, pending], { verificationStatus: STATUS.DISPUTED }).length, 0);
});

test("topic, difficulty, source type and exam tag filters compose", () => {
  const rows = canonicalPublicBank.slice(0, 8);
  const first = rows[0];
  const selected = filterQuestions(rows, {
    verificationStatus: "all_practice",
    topic: first.topic_id,
    difficulty: first.difficulty,
    sourceType: first.source_type,
    examTag: first.exam_tags[0] || "all",
  });
  assert.ok(selected.length >= 1);
  assert.ok(selected.every((q) => q.topic_id === first.topic_id));
  assert.ok(selected.every((q) => q.difficulty === first.difficulty));
  assert.ok(selected.every((q) => q.source_type === first.source_type));
  if (first.exam_tags.length) assert.ok(selected.every((q) => q.exam_tags.includes(first.exam_tags[0])));
});

test("sampling is stable for a supplied RNG and never mutates the input", () => {
  const list = canonicalPublicBank.slice(0, 12);
  const before = list.map((q) => q.id);
  const a = sampleQuestions(list, 7, () => 0.5);
  const b = sampleQuestions(list, 7, () => 0.5);
  assert.deepEqual(a.map((q) => q.id), b.map((q) => q.id));
  assert.equal(a.length, 7);
  assert.equal(new Set(a.map((q) => q.id)).size, 7);
  assert.deepEqual(list.map((q) => q.id), before);
  assert.equal(sampleQuestions(list, "all", () => 0.2).length, list.length);
});

test("grading counts correct, incorrect and unanswered without negative scoring", () => {
  const questions = canonicalPublicBank.slice(0, 3);
  assert.equal(questions.length, 3);
  const wrongOption = questions[1].options.find((option) => option.id !== questions[1].answer_option_id).id;
  const result = gradeAttempt(questions, {
    [questions[0].id]: questions[0].answer_option_id,
    [questions[1].id]: wrongOption,
  });
  assert.equal(result.total, 3);
  assert.equal(result.correct, 1);
  assert.equal(result.wrong, 1);
  assert.equal(result.unanswered, 1);
  assert.equal(result.percent, 33);
  assert.equal(Object.values(result.topicBreakdown).reduce((sum, topic) => sum + topic.total, 0), 3);
});

test("Hindi fallback is explicit and verification labels stay distinct", () => {
  const sample = canonicalPublicBank[0];
  const fallback = localizeText(sample.stem_en, "", "hi");
  assert.equal(fallback.primary, sample.stem_en);
  assert.equal(fallback.fallback, true);
  const bilingual = localizeText(sample.stem_en, sample.stem_hi, "both");
  assert.equal(bilingual.primary, sample.stem_en);
  if (sample.stem_hi) assert.equal(bilingual.fallback, false);
  else assert.equal(bilingual.fallback, true);
  assert.equal(verificationLabel(STATUS.OFFICIAL), "Official paper + final key checked");
  assert.notEqual(verificationLabel(STATUS.ANSWER_CHECKED), verificationLabel(STATUS.OFFICIAL));
});
