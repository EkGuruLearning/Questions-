export const STATUS = Object.freeze({
  OFFICIAL: "paper_and_key_checked",
  ANSWER_CHECKED: "answer_checked",
  CLAIMED_UNVERIFIED: "claimed_answer_unverified",
  DISPUTED: "disputed",
  PENDING: "pending_review",
});

export const SOURCE_TYPE = Object.freeze({
  VERIFIED_OFFICIAL: "verified_official_pyq",
  CLAIMED_PYQ: "claimed_pyq_unverified",
  INTERNAL: "repository_internal",
  TEXTBOOK: "textbook_paraphrase",
  ORIGINAL: "original_practice",
});

const PRACTICE_STATUSES = new Set([STATUS.OFFICIAL, STATUS.ANSWER_CHECKED]);
const NEVER_TEST_STATUSES = new Set([STATUS.DISPUTED, STATUS.PENDING]);

export function filterQuestions(questions, filters = {}) {
  const statusFilter = filters.verificationStatus || "reviewed_answers";
  return questions.filter((question) => {
    const status = question.verification_status;
    if (NEVER_TEST_STATUSES.has(status)) return false;
    if (statusFilter === "reviewed_answers" && !PRACTICE_STATUSES.has(status)) return false;
    if (statusFilter !== "reviewed_answers" && statusFilter !== "all_practice" && status !== statusFilter) return false;
    if (statusFilter === "all_practice" && !PRACTICE_STATUSES.has(status) && status !== STATUS.CLAIMED_UNVERIFIED) return false;
    if (filters.topic && filters.topic !== "all" && question.topic_id !== filters.topic) return false;
    if (filters.difficulty && filters.difficulty !== "all" && question.difficulty !== filters.difficulty) return false;
    if (filters.sourceType && filters.sourceType !== "all" && question.source_type !== filters.sourceType) return false;
    if (filters.examTag && filters.examTag !== "all" && !(question.exam_tags || []).includes(filters.examTag)) return false;
    return true;
  });
}

export function sampleQuestions(questions, count, rng = Math.random) {
  const shuffled = questions.slice();
  for (let i = shuffled.length - 1; i > 0; i -= 1) {
    const sample = Math.max(0, Math.min(0.999999999999, Number(rng()) || 0));
    const j = Math.floor(sample * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  if (count === "all" || count === Infinity || count == null) return shuffled;
  const safeCount = Math.max(0, Math.floor(Number(count) || 0));
  return shuffled.slice(0, safeCount);
}

export function gradeAttempt(questions, answers = {}) {
  const topicBreakdown = Object.create(null);
  const verificationBreakdown = Object.create(null);
  let correct = 0;
  let wrong = 0;
  let unanswered = 0;

  for (const question of questions) {
    const selected = answers[question.id];
    const topic = question.topic_id || "unknown";
    const sourceStatus = question.verification_status || "unknown";
    topicBreakdown[topic] ||= { total: 0, correct: 0, wrong: 0, unanswered: 0 };
    verificationBreakdown[sourceStatus] = (verificationBreakdown[sourceStatus] || 0) + 1;
    topicBreakdown[topic].total += 1;

    if (selected == null || selected === "") {
      unanswered += 1;
      topicBreakdown[topic].unanswered += 1;
    } else if (selected === question.answer_option_id) {
      correct += 1;
      topicBreakdown[topic].correct += 1;
    } else {
      wrong += 1;
      topicBreakdown[topic].wrong += 1;
    }
  }

  const total = questions.length;
  return {
    total,
    correct,
    wrong,
    unanswered,
    percent: total ? Math.round((correct / total) * 100) : 0,
    topicBreakdown,
    verificationBreakdown,
  };
}

export function localizeText(english, hindi, language = "both") {
  const en = typeof english === "string" ? english : "";
  const hi = typeof hindi === "string" ? hindi : "";
  if (language === "en") return { primary: en || hi, secondary: "", fallback: !en && Boolean(hi), language: en ? "en" : hi ? "hi" : "none" };
  if (language === "hi") return { primary: hi || en, secondary: "", fallback: !hi && Boolean(en), language: hi ? "hi" : en ? "en" : "none" };
  if (!hi) return { primary: en, secondary: "", fallback: Boolean(en), language: en ? "en" : "none" };
  if (!en) return { primary: hi, secondary: "", fallback: true, language: "hi" };
  return { primary: en, secondary: hi === en ? "" : hi, fallback: false, language: "both" };
}

export function answerLabel(question, optionId) {
  if (!optionId) return "Unanswered";
  const option = (question.options || []).find((item) => item.id === optionId);
  return option ? `${option.id}) ${option.text_en || option.text_hi || ""}` : "Unknown option";
}

export function isPracticeEligible(question) {
  return PRACTICE_STATUSES.has(question?.verification_status);
}

export function verificationLabel(status) {
  const labels = {
    [STATUS.OFFICIAL]: "Official paper + final key checked",
    [STATUS.ANSWER_CHECKED]: "Answer checked; not official-key matched",
    [STATUS.CLAIMED_UNVERIFIED]: "Claimed source/answer — unverified",
    [STATUS.DISPUTED]: "Disputed — excluded from tests",
    [STATUS.PENDING]: "Pending review — excluded from tests",
  };
  return labels[status] || "Verification status unknown";
}

export function sourceTypeLabel(sourceType) {
  const labels = {
    [SOURCE_TYPE.VERIFIED_OFFICIAL]: "Verified official PYQ",
    [SOURCE_TYPE.CLAIMED_PYQ]: "Claimed PYQ — unverified",
    [SOURCE_TYPE.INTERNAL]: "Repository / third-party source",
    [SOURCE_TYPE.TEXTBOOK]: "Textbook paraphrase",
    [SOURCE_TYPE.ORIGINAL]: "Original practice",
  };
  return labels[sourceType] || "Source type unknown";
}
