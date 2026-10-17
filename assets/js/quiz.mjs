import { createQuizDraft, restoreQuizDraft, gradeQuestion, gradeQuiz, quizRemaining, quizAttempt } from "./quiz-engine.mjs";
const ROOT = new URL("../../", import.meta.url), $ = (id) => document.getElementById(id);
const state = { manifest: null, entries: [], test: null, draft: null, active: false, timer: null, load: 0, review: 0, result: null, checked: new Set() };
const owner = () => window.EkGuruAccount?.user?.id || null;
const key = () => `ekguru.quiz.draft.v1.${state.test.subject_id}.${state.test.id}.${owner() || "guest"}`;
const read = (name) => { try { return JSON.parse(localStorage.getItem(name)); } catch { return null; } };
const message = (text) => { $("quizMessage").textContent = text; $("quizMessage").hidden = !text; };
const time = (seconds) => `${String(Math.floor(seconds / 60)).padStart(2, "0")}:${String(seconds % 60).padStart(2, "0")}`;
function urlFor(path) { return new URL(path.split("/").map(encodeURIComponent).join("/"), ROOT); }
async function json(path) {
  const url = urlFor(path);
  if (url.origin !== ROOT.origin || !url.pathname.startsWith(new URL("data/quizzes/", ROOT).pathname)) throw new Error("Invalid local test URL");
  const response = await fetch(url, { cache: /\.[a-f0-9]{12}\.min\.json$/.test(path) ? "default" : "no-cache", signal: AbortSignal.timeout(15000) });
  if (!response.ok) throw new Error("Test data load nahi hui. Internet check karke Retry karein.");
  return response.json();
}
function persist() {
  if (!state.draft || !state.test) return false;
  try {
    // Use captured owner, not whichever account is active when a timer fires.
    const draftKey = `ekguru.quiz.draft.v1.${state.test.subject_id}.${state.test.id}.${state.draft.owner || "guest"}`;
    localStorage.setItem(draftKey, JSON.stringify(state.draft));
    $("quizSaveStatus").textContent = "Responses auto-saved on this device · timer never resets on reload."; return true;
  } catch { $("quizSaveStatus").textContent = "Browser storage unavailable/full. Tab khula rakhein aur result JSON download karein."; return false; }
}
function palette() {
  const draft = state.draft, container = $("quizPalette"), visited = new Set(draft.visited), marked = new Set(draft.marked); let answered = 0;
  if (container.children.length !== state.test.questions.length) {
    const fragment = document.createDocumentFragment();
    state.test.questions.forEach((question, index) => { const button = document.createElement("button"); button.type = "button"; button.textContent = index + 1; button.addEventListener("click", () => go(index)); fragment.append(button); });
    container.replaceChildren(fragment);
  }
  state.test.questions.forEach((question, index) => {
    const selected = gradeQuestion(question, draft.answers[question.id]).answered;
    if (selected) answered++;
    const button = container.children[index];
    button.className = [selected ? "answered" : visited.has(index) ? "visited" : "", marked.has(index) ? "marked" : "", draft.index === index ? "current" : ""].join(" ");
    button.setAttribute("aria-label", `Question ${index + 1}${selected ? ", answered" : ", unanswered"}${draft.marked.includes(index) ? ", marked for review" : ""}`);
    if (draft.index === index) button.setAttribute("aria-current", "true"); else button.removeAttribute("aria-current");
  });
  $("quizProgress").textContent = `${answered} answered · ${state.test.questions.length - answered} skipped · ${draft.marked.length} marked`;
}
function feedback() {
  const q = state.test.questions[state.draft.index], result = gradeQuestion(q, state.draft.answers[q.id]);
  const answer = q.type === "numeric" ? q.answer_range?.join(" to ") : q.answer?.join(q.type === "multiple" ? " + " : " / ");
  $("quizFeedback").hidden = false;
  $("quizFeedback").textContent = result.keyed ? `${result.status.toUpperCase()} · Key: ${answer}. ${q.explanation || ""}` : `Unscored: no reliable key for this question. ${q.notice || ""}`;
  state.checked.add(q.id);
}
function render() {
  const draft = state.draft, q = state.test.questions[draft.index];
  if (!draft.visited.includes(draft.index)) draft.visited.push(draft.index);
  $("quizQuestionNumber").textContent = `Question ${draft.index + 1} of ${state.test.questions.length}`;
  $("quizQuestionType").textContent = q.type === "numeric" ? "Numerical answer" : q.type === "multiple" ? "Choose ALL correct options" : "Single correct option";
  $("quizMarking").textContent = `+${q.marks} / −${q.negative}`;
  $("quizQuestionText").textContent = q.text;
  const media = $("quizQuestionMedia"); media.replaceChildren(); media.hidden = !q.image;
  if (q.image) {
    const image = document.createElement("img"); image.id = "quizQuestionImage"; image.className = "quiz-question-image";
    image.alt = "Original question and options from the source PDF";
    [image.width, image.height] = q.image_size; image.src = urlFor(q.image).href; media.append(image);
  }
  $("quizQuestionNotice").hidden = !q.notice; $("quizQuestionNotice").textContent = q.notice || "";
  $("quizOptions").replaceChildren(); $("quizNumericWrap").hidden = q.type !== "numeric";
  if (q.type === "numeric") $("quizNumeric").value = draft.answers[q.id] || "";
  else for (const option of q.options) {
    const button = document.createElement("button"); button.type = "button"; button.className = "option";
    const chosen = q.type === "multiple" ? (draft.answers[q.id] || []).includes(option.id) : draft.answers[q.id] === option.id;
    button.setAttribute("aria-pressed", String(chosen)); button.dataset.answer = option.id;
    const badge = document.createElement("span"); badge.className = "key"; badge.textContent = option.id;
    const caption = document.createElement("span"); caption.className = "opt-text"; caption.textContent = option.text;
    button.append(badge, caption);
    button.addEventListener("click", () => {
      if (q.type === "multiple") {
        const selected = new Set(draft.answers[q.id] || []); selected.has(option.id) ? selected.delete(option.id) : selected.add(option.id);
        if (selected.size) draft.answers[q.id] = [...selected].sort(); else delete draft.answers[q.id];
      } else draft.answers[q.id] = option.id;
      state.checked.delete(q.id); render(); persist();
    });
    $("quizOptions").append(button);
  }
  $("quizFeedback").hidden = true;
  if (draft.mode === "practice" && state.checked.has(q.id)) feedback();
  $("quizCheck").hidden = draft.mode !== "practice";
  $("quizPrev").disabled = draft.index === 0;
  $("quizNext").textContent = draft.index === state.test.questions.length - 1 ? "Save & submit" : "Save & next →";
  $("quizMark").setAttribute("aria-pressed", String(draft.marked.includes(draft.index)));
  $("quizMark").textContent = draft.marked.includes(draft.index) ? "Unmark review" : "Mark for review";
  palette();
}
function go(index) {
  if (!state.active || index < 0 || index >= state.test.questions.length) return;
  state.draft.index = index; render(); persist(); window.scrollTo({ top: 0, behavior: "instant" }); $("quizQuestionText").focus({ preventScroll: true });
}
function tick() {
  if (!state.active) return;
  const left = quizRemaining(state.draft);
  $("quizTimer").textContent = time(left === null ? Math.floor((Date.now() - state.draft.started_at) / 1000) : left);
  if (left === 0) finish(true);
}
async function start(resume = false) {
  if (!state.test || state.active) return;
  const selectedTest = state.test;
  await window.EkGuruAccount?.ready;
  if (state.active || state.test !== selectedTest) return;
  const saved = read(key()), restored = resume ? restoreQuizDraft(saved, state.test, owner()) : null;
  if (resume && !restored) { message("Saved draft badal/expire ho gaya ya account match nahi hua. Naya attempt shuru karein."); return; }
  if (!resume && saved && !window.confirm("Is test ka purana draft replace karke naya attempt shuru karein?")) return;
  state.draft = restored || createQuizDraft(state.test, { mode: $("quizMode").value, minutes: Number($("quizMinutes").value) }, Date.now(), owner());
  state.checked.clear(); state.active = true; message("");
  $("quizSetup").hidden = true; $("quizIntro").hidden = true; $("quizResult").hidden = true; $("quizPlayer").hidden = false;
  document.body.classList.add("cbt-active");
  $("quizTitle").textContent = state.test.title; $("quizSubjectLabel").textContent = state.test.subject_title;
  $("quizOriginal").hidden = !state.test.source?.pdf;
  if (state.test.source?.pdf) $("quizOriginal").href = urlFor(state.test.source.pdf).href;
  $("quizPaletteDetails").open = innerWidth >= 900;
  render(); persist(); clearInterval(state.timer); state.timer = setInterval(tick, 1000); tick();
  window.scrollTo({ top: 0, behavior: "instant" });
}
function reviewMore() {
  if (!state.result) return;
  const end = Math.min(state.review + 50, state.test.questions.length);
  for (; state.review < end; state.review++) {
    const q = state.test.questions[state.review], result = state.result.review[state.review];
    const row = document.createElement("article"); row.className = `review-item ${result.status}`;
    const heading = document.createElement("h3"); heading.textContent = `Q${state.review + 1} · ${result.status}`;
    const stem = document.createElement("p"); stem.className = "small"; stem.textContent = q.text;
    const answer = document.createElement("p"); answer.className = "small";
    answer.textContent = `Your answer: ${Array.isArray(result.selected) ? result.selected.join(" + ") : result.selected ?? "Skipped"} · Key: ${q.answer?.join(" / ") || q.answer_range?.join(" to ") || "Not graded"}. ${q.notice || q.explanation || ""}`;
    row.append(heading, stem, answer); $("quizReview").append(row);
  }
  $("quizReviewMore").hidden = state.review >= state.test.questions.length;
}
function finish(auto = false) {
  if (!state.active) return;
  const result = gradeQuiz(state.test, state.draft);
  if (!auto && !confirm(`Submit test?\n${result.answered}/${result.total} answered · ${result.unanswered} skipped. Marked selected answers also count.`)) return;
  state.active = false; clearInterval(state.timer); document.body.classList.remove("cbt-active");
  const attempt = quizAttempt(state.test, state.draft);
  state.result = { ...attempt, review: result.review }; state.review = 0;
  try { localStorage.removeItem(`ekguru.quiz.draft.v1.${state.test.subject_id}.${state.test.id}.${state.draft.owner || "guest"}`); } catch { /* journal/export still available */ }
  $("quizPlayer").hidden = true; $("quizResult").hidden = false;
  $("quizResultTitle").textContent = `${state.test.title} · ${auto ? "Time up, auto-submitted · " : ""}${time(attempt.duration_seconds)}`;
  $("quizStats").replaceChildren();
  for (const [label, value] of [["Practice marks", result.score === null ? "Unscored" : `${result.score} / ${result.max_score}`], ["Correct", result.correct ?? "—"], ["Answered", result.answered], ["Skipped", result.unanswered]]) {
    const item = document.createElement("div"); item.className = "stat";
    const strong = document.createElement("strong"); strong.textContent = value; const span = document.createElement("span"); span.textContent = label;
    item.append(strong, span); $("quizStats").append(item);
  }
  $("quizResultNote").textContent = `${result.keyed}/${result.total} keyed questions; ${result.ungraded} unkeyed items excluded. ${state.test.note || "Self-practice result, not a proctored/official score."}`;
  $("quizReview").replaceChildren(); $("quizReviewDetails").open = false;
  window.EkGuruAccount?.saveAttempt(attempt, state.draft.owner).catch(() => message("History save nahi hui. Result JSON download karein aur retry karein."));
  $("quizResult").scrollIntoView({ block: "start", behavior: "instant" });
}
async function chooseTest() {
  const token = ++state.load, entry = state.entries.find((test) => test.id === $("quizTest").value);
  state.test = null; $("quizStart").disabled = true; $("quizResume").hidden = true;
  if (!entry) return;
  $("quizMeta").textContent = `${entry.question_count} questions · ${entry.duration_minutes || "No"} minute limit · only this test is fetched`;
  $("quizMinutes").value = entry.duration_minutes;
  if (entry.legacy_url) {
    $("quizSourceNote").textContent = "Ye test existing Computer Network CBT engine mein khulega. Result isi all-subject history mein save hoga."; $("quizSourceNote").hidden = false;
    $("quizStart").disabled = false; return;
  }
  try {
    const bank = await json(entry.file);
    if (token !== state.load) return;
    if (bank.schema_version !== 1 || bank.subject_id !== $("quizSubject").value || bank.id !== entry.id || !Array.isArray(bank.questions) || bank.questions.length !== entry.question_count) throw new Error("Test definition invalid");
    state.test = { ...bank, fingerprint: entry.fingerprint };
    $("quizSourceNote").textContent = bank.note || "Self-practice test; marking aur timing apne practice settings hain."; $("quizSourceNote").hidden = false;
    $("quizStart").disabled = false;
    await window.EkGuruAccount?.ready;
    if (token === state.load) $("quizResume").hidden = !restoreQuizDraft(read(key()), state.test, owner());
    message("");
  } catch (error) { if (token === state.load) message(error.message + " Page refresh karke retry kar sakte hain."); }
}
async function chooseSubject(testId = "") {
  const token = ++state.load; state.test = null; state.entries = [];
  $("quizStart").disabled = true; $("quizTest").disabled = true; $("quizResume").hidden = true; $("quizSourceNote").hidden = true;
  const subjectId = $("quizSubject").value, subject = state.manifest.subjects.find((item) => item.id === subjectId);
  if (!subject) return;
  try {
    const index = await json(subject.file);
    if (token !== state.load || $("quizSubject").value !== subjectId) return;
    state.entries = index.tests; $("quizTest").replaceChildren();
    for (const test of index.tests) { const option = document.createElement("option"); option.value = test.id; option.textContent = test.title; $("quizTest").append(option); }
    $("quizTest").disabled = !index.tests.length;
    if (testId && index.tests.some((item) => item.id === testId)) $("quizTest").value = testId;
    else if (testId) { message("Requested test is subject mein nahi mila. Niche available tests mein se choose karein."); return; }
    await chooseTest();
  } catch (error) { if (token === state.load) message(error.message); }
}
$("quizSetupForm").addEventListener("submit", (event) => {
  event.preventDefault();
  const entry = state.entries.find((test) => test.id === $("quizTest").value);
  if (entry?.legacy_url) { location.href = new URL(entry.legacy_url, ROOT).href; return; }
  start().catch((error) => message(error.message));
});
$("quizResume").addEventListener("click", () => start(true).catch((error) => message(error.message)));
$("quizSubject").addEventListener("change", () => chooseSubject()); $("quizTest").addEventListener("change", chooseTest);
$("quizPrev").addEventListener("click", () => go(state.draft.index - 1));
$("quizNext").addEventListener("click", () => state.draft.index === state.test.questions.length - 1 ? finish() : go(state.draft.index + 1));
$("quizCheck").addEventListener("click", feedback);
$("quizClear").addEventListener("click", () => { delete state.draft.answers[state.test.questions[state.draft.index].id]; state.checked.delete(state.test.questions[state.draft.index].id); render(); persist(); });
$("quizMark").addEventListener("click", () => { const d = state.draft; d.marked = d.marked.includes(d.index) ? d.marked.filter((i) => i !== d.index) : d.marked.concat(d.index); render(); persist(); });
$("quizNumeric").addEventListener("input", () => { const q = state.test.questions[state.draft.index], value = $("quizNumeric").value;
  if (gradeQuestion(q, value).answered) state.draft.answers[q.id] = value; else delete state.draft.answers[q.id];
  state.checked.delete(q.id); $("quizFeedback").hidden = true; palette(); persist();
});
$("quizSubmit").addEventListener("click", () => finish());
$("quizLeave").addEventListener("click", () => { if (!persist()) { message("Draft save nahi hui. Tab khula rakhein ya submit karke result export karein."); return; }
  state.active = false; clearInterval(state.timer); document.body.classList.remove("cbt-active"); $("quizPlayer").hidden = true; $("quizSetup").hidden = false; $("quizIntro").hidden = false; $("quizResume").hidden = false;
  message("Draft saved. Timed attempt ka deadline continue ho raha hai.");
});
$("quizAgain").addEventListener("click", () => { $("quizResult").hidden = true; $("quizSetup").hidden = false; $("quizIntro").hidden = false; $("quizResume").hidden = true; message(""); window.scrollTo({ top: 0, behavior: "instant" }); });
$("quizReviewDetails").addEventListener("toggle", () => { if ($("quizReviewDetails").open && state.review === 0) reviewMore(); });
$("quizReviewMore").addEventListener("click", reviewMore);
$("quizExport").addEventListener("click", () => { if (!state.result) return; const url = URL.createObjectURL(new Blob([JSON.stringify(state.result, null, 2)], { type: "application/json" })); const link = document.createElement("a"); link.href = url; link.download = `${state.test.subject_id}-${state.test.id}-result.json`; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000); });
document.addEventListener("visibilitychange", tick);
window.addEventListener("beforeunload", (event) => { if (state.active && !persist()) { event.preventDefault(); event.returnValue = ""; } });
window.addEventListener("keydown", (event) => { if (!state.active || !event.altKey || !["n", "p"].includes(event.key.toLowerCase()) || /INPUT|TEXTAREA|SELECT/.test(document.activeElement?.tagName)) return; event.preventDefault(); go(state.draft.index + (event.key.toLowerCase() === "n" ? 1 : -1)); });
(async () => {
  try {
    state.manifest = await json("data/quizzes/manifest.json");
    $("quizSubject").replaceChildren();
    for (const subject of state.manifest.subjects) { const option = document.createElement("option"); option.value = subject.id; option.textContent = `${subject.title} · ${subject.test_count} tests`; $("quizSubject").append(option); }
    $("quizSubject").disabled = !state.manifest.subjects.length;
    const params = new URLSearchParams(location.search), requested = params.get("subject");
    if (requested && state.manifest.subjects.some((s) => s.id === requested)) $("quizSubject").value = requested;
    else if (requested) { message("Requested subject abhi available nahi. Subject picker se choose karein."); return; }
    await chooseSubject(params.get("test") || "");
  } catch (error) { message(error.message); }
})();
