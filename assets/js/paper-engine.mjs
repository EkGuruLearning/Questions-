/* Pure practice-room rules shared by the browser and unit tests. */
export const DRAFT_VERSION = 1;
export const MAX_QUESTIONS = 300;
const letter = (value, count) => typeof value === "string" && "ABCDE".slice(0, count).includes(value) && value.length === 1;
const integer = (value, min, max) => Number.isInteger(value) && value >= min && value <= max;

export function validateSettings(settings) {
  if (!settings || !integer(settings.count, 1, MAX_QUESTIONS) || !integer(settings.options, 2, 5)
      || !integer(settings.minutes, 0, 360) || !["exam", "practice"].includes(settings.mode)
      || !Number.isFinite(settings.marks) || settings.marks <= 0 || settings.marks > 100
      || !Number.isFinite(settings.negative) || settings.negative < 0 || settings.negative > 100) {
    throw new Error("Question count, options, time ya marking sahi bharein.");
  }
  return { count: settings.count, options: settings.options, minutes: settings.minutes,
    mode: settings.mode, marks: settings.marks, negative: settings.negative };
}

export function createDraft(paper, settings, now = Date.now(), owner = null, id = globalThis.crypto.randomUUID()) {
  const clean = validateSettings(settings);
  if (paper.question_count != null && clean.count !== paper.question_count) throw new Error("Paper question count does not match.");
  return { version: DRAFT_VERSION, id, paper_id: paper.id, fingerprint: paper.fingerprint,
    settings: clean, started_at: now, deadline: clean.minutes ? now + clean.minutes * 60000 : null,
    index: 0, answers: {}, marked: [], visited: [1], pdf_page: 1, owner };
}

export function restoreDraft(raw, paper, now = Date.now()) {
  try {
    if (!raw || raw.version !== DRAFT_VERSION || raw.paper_id !== paper.id || raw.fingerprint !== paper.fingerprint
        || !/^[0-9a-f-]{36}$/i.test(raw.id || "") || !Number.isFinite(raw.started_at)
        || raw.started_at > now + 60000 || now - raw.started_at > 7 * 86400000) return null;
    const clean = validateSettings(raw.settings);
    if (paper.question_count != null && clean.count !== paper.question_count) return null;
    if (!integer(raw.index, 0, clean.count - 1) || !raw.answers || typeof raw.answers !== "object" || Array.isArray(raw.answers)) return null;
    const answers = {};
    for (const [key, value] of Object.entries(raw.answers)) {
      if (!/^[1-9]\d{0,2}$/.test(key) || Number(key) > clean.count || !letter(value, clean.options)) return null;
      answers[key] = value;
    }
    const list = (value) => Array.isArray(value) && value.length <= clean.count
      && value.every((n) => integer(n, 1, clean.count));
    if (!list(raw.marked) || !list(raw.visited)) return null;
    // Recompute, do not trust a modified deadline. Reload never resets the timer.
    const deadline = clean.minutes ? raw.started_at + clean.minutes * 60000 : null;
    return { version: DRAFT_VERSION, id: raw.id, paper_id: paper.id, fingerprint: paper.fingerprint,
      settings: clean, started_at: raw.started_at, deadline, index: raw.index, answers,
      pdf_page: integer(raw.pdf_page, 1, 10000) ? raw.pdf_page : 1,
      marked: [...new Set(raw.marked)], visited: [...new Set(raw.visited)],
      owner: typeof raw.owner === "string" && /^[0-9a-f-]{36}$/i.test(raw.owner) ? raw.owner : null };
  } catch { return null; }
}

export function remainingSeconds(draft, now = Date.now()) {
  return draft.deadline === null ? null : Math.max(0, Math.ceil((draft.deadline - now) / 1000));
}

export function gradePaper(paper, draft) {
  const { count, options, marks, negative } = validateSettings(draft.settings);
  const key = paper.answer_key || {};
  let answered = 0, correct = 0, wrong = 0, keyed = 0, dropped = 0;
  const review = [];
  for (let number = 1; number <= count; number += 1) {
    const selected = letter(draft.answers[number], options) && draft.answers[number] !== paper.skip_option ? draft.answers[number] : null;
    if (selected) answered += 1;
    const accepted = key[number];
    let status = "ungraded";
    if (accepted === "DROP") { dropped += 1; status = "dropped"; }
    else if (Array.isArray(accepted) && accepted.length && accepted.every((option) => letter(option, options) && option !== paper.skip_option)) {
      keyed += 1;
      if (!selected) status = "skipped";
      else if (accepted.includes(selected)) { correct += 1; status = "correct"; }
      else { wrong += 1; status = "wrong"; }
    }
    review.push({ number, selected, accepted: Array.isArray(accepted) ? accepted : null, status });
  }
  const round = (value) => Math.round((value + Number.EPSILON) * 1000) / 1000;
  return { total: count, answered, unanswered: count - answered, correct: keyed ? correct : null,
    wrong: keyed ? wrong : null, keyed, dropped, ungraded: count - keyed - dropped,
    score: keyed ? round(correct * marks - wrong * negative) : null,
    max_score: keyed ? round(keyed * marks) : null, review };
}

export function paperAttempt(paper, draft, now = Date.now()) {
  const result = gradePaper(paper, draft);
  return { id: draft.id, kind: "paper", subject_id: "previous-year-papers", test_id: paper.id, completed_at: new Date(now).toISOString(), paper_id: paper.id, label: paper.title,
    total: result.total, correct: result.correct, wrong: result.wrong, unanswered: result.unanswered,
    score: result.score, max_score: result.max_score,
    duration_seconds: Math.min(604800, Math.max(0, Math.floor(((draft.deadline ? Math.min(now, draft.deadline) : now) - draft.started_at) / 1000))),
    details: { version: 1, fingerprint: paper.fingerprint, settings: draft.settings,
      answers: draft.answers, keyed: result.keyed, dropped: result.dropped, ungraded: result.ungraded } };
}
