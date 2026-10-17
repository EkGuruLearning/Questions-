/* Subject-independent CBT rules. Single choice, exact-set MSQ and numeric ranges.
   Scores are self-practice, never proof of a proctored exam. */
export const QUIZ_VERSION = 1;
const integer = (value, low, high) => Number.isInteger(value) && value >= low && value <= high;
const uuid = (value) => typeof value === "string" && /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(value);
function selection(question, value) {
  if (question.type === "numeric") {
    if (typeof value !== "string" || value.length > 32 || !/^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d{1,2})?$/.test(value.trim())) return null;
    const number = Number(value); return Number.isFinite(number) && Math.abs(number) <= 1e12 ? value.trim() : null;
  }
  const valid = new Set(question.options.map((option) => option.id));
  if (question.type === "multiple") return Array.isArray(value) && value.length && value.length <= valid.size && new Set(value).size === value.length && value.every((item) => valid.has(item)) ? [...value].sort() : null;
  return typeof value === "string" && valid.has(value) ? value : null;
}
export function createQuizDraft(test, { mode = "exam", minutes = test.duration_minutes } = {}, now = Date.now(), owner = null, id = globalThis.crypto.randomUUID()) {
  if (!test.questions?.length || test.questions.length > 2000 || !["exam", "practice"].includes(mode) || !integer(minutes, 0, 360) || !uuid(id)) throw new Error("Invalid test settings");
  return { version: QUIZ_VERSION, id, subject_id: test.subject_id, test_id: test.id, fingerprint: test.fingerprint,
    owner, mode, minutes, started_at: now, deadline: minutes ? now + minutes * 60000 : null, index: 0, answers: {}, marked: [], visited: [0] };
}
export function restoreQuizDraft(raw, test, owner = null, now = Date.now()) {
  try {
    if (!raw || raw.version !== QUIZ_VERSION || raw.subject_id !== test.subject_id || raw.test_id !== test.id || raw.fingerprint !== test.fingerprint || raw.owner !== owner
      || !uuid(raw.id) || !Number.isFinite(raw.started_at) || raw.started_at > now + 60000 || now - raw.started_at > 7 * 86400000 || !integer(raw.index, 0, test.questions.length - 1)
      || !raw.answers || typeof raw.answers !== "object" || Array.isArray(raw.answers)) return null;
    const draft = createQuizDraft(test, raw, raw.started_at, owner, raw.id);
    const questions = new Map(test.questions.map((q) => [q.id, q]));
    for (const [key, value] of Object.entries(raw.answers)) {
      const question = questions.get(key), clean = question && selection(question, value);
      if (clean === null || clean === undefined) return null;
      draft.answers[key] = clean;
    }
    for (const field of ["marked", "visited"]) {
      if (!Array.isArray(raw[field]) || raw[field].length > test.questions.length || raw[field].some((index) => !integer(index, 0, test.questions.length - 1))) return null;
      draft[field] = [...new Set(raw[field])];
    }
    draft.index = raw.index; return draft;
  } catch { return null; }
}
export const quizRemaining = (draft, now = Date.now()) => draft.deadline === null ? null : Math.max(0, Math.ceil((draft.deadline - now) / 1000));
export function gradeQuestion(question, value) {
  const selected = selection(question, value), answered = selected !== null && selected !== question.skip_option;
  const keyed = question.type === "numeric" ? Array.isArray(question.answer_range) : Array.isArray(question.answer) && question.answer.length > 0;
  let correct = false;
  if (answered && keyed) {
    if (question.type === "numeric") correct = Number(selected) >= question.answer_range[0] && Number(selected) <= question.answer_range[1];
    else if (question.type === "multiple") correct = selected.length === question.answer.length && selected.every((option) => question.answer.includes(option));
    else correct = question.answer.includes(selected);
  }
  return { selected, answered, keyed, status: !keyed ? "ungraded" : !answered ? "skipped" : correct ? "correct" : "wrong",
    score: !keyed || !answered ? 0 : correct ? question.marks : -question.negative };
}
export function gradeQuiz(test, draft) {
  const review = test.questions.map((question) => ({ id: question.id, ...gradeQuestion(question, draft.answers[question.id]) }));
  const keyed = review.filter((q) => q.keyed).length;
  const round = (value) => Math.round((value + Number.EPSILON) * 1000) / 1000;
  return { total: review.length, answered: review.filter((q) => q.answered).length, unanswered: review.filter((q) => !q.answered).length,
    keyed, ungraded: review.length - keyed, correct: keyed ? review.filter((q) => q.status === "correct").length : null,
    wrong: keyed ? review.filter((q) => q.status === "wrong").length : null,
    score: keyed ? round(review.reduce((sum, q) => sum + q.score, 0)) : null,
    max_score: keyed ? round(test.questions.reduce((sum, q, index) => sum + (review[index].keyed ? q.marks : 0), 0)) : null, review };
}
export function quizAttempt(test, draft, now = Date.now()) {
  const { total, correct, wrong, unanswered, score, max_score, keyed, ungraded } = gradeQuiz(test, draft);
  const end = draft.deadline ? Math.min(now, draft.deadline) : now;
  return { id: draft.id, subject_id: test.subject_id, test_id: test.id, kind: test.kind || "quiz", paper_id: test.id, label: test.title,
    total, correct, wrong, unanswered, score, max_score, duration_seconds: Math.max(0, Math.min(604800, Math.floor((end - draft.started_at) / 1000))), completed_at: new Date(now).toISOString(),
    details: { version: 1, fingerprint: test.fingerprint, mode: draft.mode, keyed, ungraded, answers_saved: total <= 150, ...(total <= 150 ? { answers: draft.answers } : {}) } };
}
