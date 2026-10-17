import { createDraft, gradePaper, paperAttempt, remainingSeconds, restoreDraft, validateSettings } from "./paper-engine.mjs";
import { PaperReader } from "./paper-reader.mjs";

const ROOT = new URL("../../", import.meta.url);
const DRAFT = "ekguru.paper.draft.v1";
const LAST = "ekguru.paper.last.v1";
const $ = (id) => document.getElementById(id);
const state = { papers: [], draft: null, saved: null, active: false, timer: null, result: null, feedback: new Set() };
const read = (key) => { try { return JSON.parse(localStorage.getItem(key)); } catch { return null; } };
const store = (key, value) => { try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch { return false; } };
const remove = (key) => { try { localStorage.removeItem(key); } catch { /* optional storage */ } };
const currentPaper = () => state.papers.find((paper) => paper.id === (state.draft?.paper_id || $("paperSelect").value));
const selectedPaper = () => state.papers.find((paper) => paper.id === $("paperSelect").value);
const formatTime = (seconds) => `${String(Math.floor(Math.max(0, seconds) / 60)).padStart(2, "0")}:${String(Math.max(0, seconds) % 60).padStart(2, "0")}`;

function message(text) { $("roomMessage").textContent = text; $("roomMessage").hidden = !text; }
function saveDraft() {
  if (!state.draft) return false;
  const ok = store(DRAFT, state.draft);
  $("draftSaveStatus").textContent = ok
    ? "Answers is device par auto-saved hain. Timed paper ka timer tab band hone par bhi chalta hai."
    : "Browser storage unavailable: answers sirf is tab mein hain. Tab band na karein; result submit karke download karein.";
  return ok;
}
const reader = new PaperReader((page) => { if (state.active) { state.draft.pdf_page = page; saveDraft(); } });

function choosePaper(id, scroll = false) {
  if (state.active) return;
  const paper = state.papers.find((entry) => entry.id === id);
  if (!paper) return;
  $("paperSelect").value = id;
  $("paperCount").value = paper.question_count || 100;
  $("paperCount").disabled = paper.question_count !== null;
  $("paperOptions").value = paper.options_count;
  $("paperOptions").disabled = Boolean(Object.keys(paper.answer_key).length || paper.skip_option);
  $("paperMinutes").value = paper.duration_minutes;
  $("paperMarks").value = paper.marks;
  $("paperNegative").value = paper.negative_marks;
  $("paperMeta").textContent = `${paper.exam.toUpperCase()}${paper.year ? ` · ${paper.year}` : ""} · ${(paper.bytes / 1048576).toFixed(1)} MB PDF · ${paper.question_count ? `${paper.question_count} questions` : "Count PDF se confirm karein"}`;
  $("paperKeyNote").textContent = `${paper.key_label}. ${paper.key_note || ""}`;
  if (scroll) $("paperSetup").scrollIntoView({ behavior: "smooth", block: "start" });
}

function readSettings() {
  return validateSettings({ count: Number($("paperCount").value), options: Number($("paperOptions").value),
    minutes: Number($("paperMinutes").value), mode: $("paperMode").value,
    marks: Number($("paperMarks").value), negative: Number($("paperNegative").value) });
}

function renderDraftNotice() {
  $("draftNotice").hidden = !state.saved;
  if (!state.saved) return;
  const paper = state.papers.find((entry) => entry.id === state.saved.paper_id);
  const left = remainingSeconds(state.saved);
  $("draftText").textContent = `Saved draft: ${paper.title} · ${Object.keys(state.saved.answers).length} responses · ${left === null ? "untimed" : left === 0 ? "time expired — resume to see result" : `${formatTime(left)} left`}.`;
}

function activate(draft) {
  state.draft = draft; state.active = true; state.saved = null; state.feedback.clear();
  $("roomIntro").hidden = true; $("roomCatalog").hidden = true; $("paperResult").hidden = true;
  $("paperPlayer").hidden = false; document.body.classList.add("paper-active");
  $("activePaperTitle").textContent = currentPaper().title;
  message(""); renderAnswer(); renderPalette(); saveDraft();
  clearInterval(state.timer);
  state.timer = setInterval(tick, 1000);
  tick();
  if (state.active) reader.open(currentPaper(), draft.pdf_page || 1).catch(() => message("PDF link invalid hai. Original paper folder use karein."));
  $("paperPlayer").scrollIntoView({ block: "start" });
}

function tick() {
  if (!state.active) return;
  const left = remainingSeconds(state.draft);
  $("roomTimer").textContent = left === null ? formatTime(Math.floor((Date.now() - state.draft.started_at) / 1000)) : formatTime(left);
  if (left === 0) finish(true);
}

function renderAnswer() {
  const draft = state.draft;
  const number = draft.index + 1;
  const paper = currentPaper();
  if (!draft.visited.includes(number)) draft.visited.push(number);
  $("roomQuestionLabel").textContent = `Question ${number} / ${draft.settings.count}`;
  const legend = document.createElement("legend"); legend.className = "sr-only"; legend.textContent = `Select answer for question ${number}`;
  $("roomOptions").replaceChildren(legend);
  "ABCDE".slice(0, draft.settings.options).split("").forEach((option, index) => {
    const label = document.createElement("label"); label.className = "room-option";
    const input = document.createElement("input"); input.type = "radio"; input.name = "paper-answer"; input.value = option;
    input.checked = draft.answers[number] === option;
    const caption = document.createElement("span");
    caption.textContent = `${option} · ${index + 1}${option === paper.skip_option ? " (Not attempted)" : ""}`;
    input.addEventListener("change", () => {
      draft.answers[number] = option; state.feedback.delete(number);
      $("roomFeedback").hidden = true; renderPalette(); saveDraft();
    });
    label.append(input, caption); $("roomOptions").append(label);
  });
  $("roomPrev").disabled = draft.index === 0;
  $("roomNext").disabled = draft.index === draft.settings.count - 1;
  $("roomMark").setAttribute("aria-pressed", String(draft.marked.includes(number)));
  $("roomMark").textContent = draft.marked.includes(number) ? "Remove review mark" : "Mark for review";
  $("roomCheck").hidden = draft.settings.mode !== "practice";
  $("roomFeedback").hidden = !state.feedback.has(number);
  if (state.feedback.has(number)) checkAnswer();
}

function renderPalette() {
  const draft = state.draft, paper = currentPaper();
  const fragment = document.createDocumentFragment();
  let answered = 0;
  for (let number = 1; number <= draft.settings.count; number++) {
    const hasAnswer = Boolean(draft.answers[number] && draft.answers[number] !== paper.skip_option);
    if (hasAnswer) answered++;
    const button = document.createElement("button"); button.type = "button"; button.textContent = number;
    button.className = [hasAnswer ? "answered" : draft.visited.includes(number) ? "visited" : "", draft.marked.includes(number) ? "marked" : "", draft.index + 1 === number ? "current" : ""].filter(Boolean).join(" ");
    button.setAttribute("aria-label", `Question ${number}${hasAnswer ? ", answered" : ", unanswered"}${draft.marked.includes(number) ? ", marked for review" : ""}`);
    if (draft.index + 1 === number) button.setAttribute("aria-current", "step");
    button.addEventListener("click", () => { draft.index = number - 1; renderAnswer(); renderPalette(); saveDraft(); });
    fragment.append(button);
  }
  $("roomPalette").replaceChildren(fragment);
  $("roomProgress").textContent = `${answered}/${draft.settings.count} attempted · ${draft.marked.length} marked for review · ${draft.settings.mode === "exam" ? "Exam mode: key hidden until submit" : "Practice mode"}`;
}

function checkAnswer() {
  if (!state.active || state.draft.settings.mode !== "practice") return;
  const number = state.draft.index + 1;
  const result = gradePaper(currentPaper(), state.draft).review[number - 1];
  $("roomFeedback").textContent = result.status === "ungraded" ? "Is question ki reliable digital key add nahi hui; ye question score nahi hoga."
    : result.status === "dropped" ? "Key mein dropped question hai — practice scoring se excluded."
    : !result.selected ? "Pehle answer select karein."
    : `${result.status === "correct" ? "Sahi ✓" : "Provided key se match nahi hua"} · Provided key: ${result.accepted.join(" / ")} (${result.accepted.map((v) => "ABCDE".indexOf(v) + 1).join(" / ")}). Key official final-key verified nahi hai.`;
  $("roomFeedback").hidden = false; state.feedback.add(number);
}

function finish(auto = false) {
  if (!state.active) return;
  const paper = currentPaper(), draft = state.draft;
  const result = gradePaper(paper, draft);
  if (!auto && !window.confirm(`Paper submit karein?\nAttempted: ${result.answered}/${result.total}\nSkipped: ${result.unanswered}\nReview marks: ${draft.marked.length}\nSelected marked answers bhi count honge.`)) return;
  state.active = false; clearInterval(state.timer); reader.close();
  document.body.classList.remove("paper-active");
  const attempt = paperAttempt(paper, draft);
  state.result = { ...attempt, owner: draft.owner, saved_at: new Date().toISOString() };
  const stored = store(LAST, state.result);
  remove(DRAFT); state.saved = null;
  $("paperPlayer").hidden = true; $("paperResult").hidden = false;
  $("paperResultLabel").textContent = `${paper.title} · ${formatTime(attempt.duration_seconds)}${auto ? " · time up, auto-submitted" : ""}`;
  const stats = [["Practice marks", result.score === null ? "Unscored" : `${result.score} / ${result.max_score}`],
    ["Attempted", result.answered], ["Skipped", result.unanswered], ["Keyed questions", `${result.keyed} / ${result.total}`]];
  $("paperResultStats").replaceChildren();
  for (const [label, value] of stats) {
    const item = document.createElement("div"); item.className = "stat";
    const strong = document.createElement("strong"); strong.textContent = value;
    const caption = document.createElement("span"); caption.textContent = label;
    item.append(strong, caption); $("paperResultStats").append(item);
  }
  $("paperResultNote").textContent = result.score === null
    ? "Digital key add nahi hui, isliye koi percentage/marks invent nahi kiye. Ye unscored self-practice hai."
    : `${result.correct} correct · ${result.wrong} wrong. ${result.ungraded} unkeyed aur ${result.dropped} dropped questions score se excluded hain. ${paper.key_label}. ${paper.key_note || ""}`;
  $("paperReview").replaceChildren();
  for (const row of result.review) {
    const item = document.createElement("p"); item.className = `review-line ${row.status}`;
    item.textContent = `Q${row.number} · Your answer: ${row.selected || "Skipped"} · Key: ${row.accepted?.join(" / ") || (row.status === "dropped" ? "Dropped" : "Not added")} · ${row.status}`;
    $("paperReview").append(item);
  }
  const account = window.EkGuruAccount;
  account?.saveAttempt(attempt, draft.owner).catch(() => message("Cloud sync pending. Local result download kar sakte hain."));
  if (!stored) message("Browser local storage unavailable. Tab band karne se pehle Download result JSON use karein.");
  $("paperResult").scrollIntoView({ block: "start" });
}

$("paperSetupForm").addEventListener("submit", (event) => {
  event.preventDefault();
  try {
    const paper = selectedPaper(); if (!paper) throw new Error("Pehle ek paper choose karein.");
    const settings = readSettings();
    if (state.saved && !window.confirm("Pichhla saved draft replace karke naya paper shuru karein?")) return;
    activate(createDraft(paper, settings, Date.now(), window.EkGuruAccount?.user?.id || null));
  } catch (error) { message(error.message); }
});
$("paperSelect").addEventListener("change", () => choosePaper($("paperSelect").value));
$("resumePaperButton").addEventListener("click", () => {
  if (state.saved) activate(state.saved);
});
$("discardPaperButton").addEventListener("click", () => {
  if (!window.confirm("Saved draft delete karein?")) return;
  state.saved = null; remove(DRAFT); renderDraftNotice();
});
$("roomPrev").addEventListener("click", () => { if (state.draft.index > 0) state.draft.index--; renderAnswer(); renderPalette(); saveDraft(); });
$("roomNext").addEventListener("click", () => { if (state.draft.index < state.draft.settings.count - 1) state.draft.index++; renderAnswer(); renderPalette(); saveDraft(); });
$("roomClear").addEventListener("click", () => {
  delete state.draft.answers[state.draft.index + 1]; state.feedback.delete(state.draft.index + 1);
  renderAnswer(); renderPalette(); saveDraft();
});
$("roomMark").addEventListener("click", () => {
  const number = state.draft.index + 1, marked = state.draft.marked;
  state.draft.marked = marked.includes(number) ? marked.filter((n) => n !== number) : marked.concat(number);
  renderAnswer(); renderPalette(); saveDraft();
});
$("roomCheck").addEventListener("click", checkAnswer);
$("submitPaperButton").addEventListener("click", () => finish());
$("pausePaperButton").addEventListener("click", () => {
  if (!saveDraft()) { message("Draft save nahi ho raha. Is tab ko khula rakhein ya paper submit karke result download karein."); return; }
  state.saved = state.draft; state.active = false; clearInterval(state.timer); reader.close();
  document.body.classList.remove("paper-active");
  $("paperPlayer").hidden = true; $("roomIntro").hidden = false; $("roomCatalog").hidden = false;
  renderDraftNotice();
  message("Draft saved. Timed paper ka timer continue ho raha hai; resume karne se time reset nahi hoga.");
  $("draftNotice").scrollIntoView({ block: "center" });
});
$("newPaperButton").addEventListener("click", () => {
  state.draft = null; $("paperResult").hidden = true; $("roomIntro").hidden = false; $("roomCatalog").hidden = false;
  renderDraftNotice(); message(""); $("paperSetup").scrollIntoView({ block: "start" });
});
$("downloadPaperResult").addEventListener("click", () => {
  if (!state.result) return;
  const { owner, ...download } = state.result; // no account identifier in a shared export
  const url = URL.createObjectURL(new Blob([JSON.stringify(download, null, 2) + "\n"], { type: "application/json" }));
  const link = document.createElement("a"); link.href = url; link.download = `${download.paper_id}-practice-result.json`;
  link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
});
$("retryPaperPdf").addEventListener("click", () => { if (state.active) reader.open(currentPaper(), state.draft.pdf_page || 1); });
document.addEventListener("visibilitychange", tick);
window.addEventListener("beforeunload", (event) => { if (state.active && !saveDraft()) { event.preventDefault(); event.returnValue = ""; } });

async function init() {
  try {
    const response = await fetch(new URL("data/practice/manifest.json", ROOT), { cache: "no-cache", signal: AbortSignal.timeout(20000) });
    if (!response.ok) throw new Error("Paper list load nahi hui.");
    const manifest = await response.json();
    if (manifest.schema_version !== 1 || !Array.isArray(manifest.papers)) throw new Error("Paper list format invalid hai.");
    state.papers = manifest.papers;
    $("paperSelect").replaceChildren();
    for (const paper of state.papers) {
      const option = document.createElement("option"); option.value = paper.id; option.textContent = paper.title; $("paperSelect").append(option);
    }
    $("paperSelect").disabled = !state.papers.length; $("startPaperButton").disabled = !state.papers.length;
    $("roomLoadStatus").textContent = state.papers.length ? `${state.papers.length} uploaded papers · PDF + answer-sheet practice` : "Abhi old papers upload nahi hue. Upar CN practice se shuru karein.";
    const requested = new URLSearchParams(location.search).get("paper");
    choosePaper(state.papers.some((p) => p.id === requested) ? requested : state.papers[0]?.id);
    document.querySelectorAll("[data-paper-id]").forEach((link) => link.addEventListener("click", () => choosePaper(link.dataset.paperId)));
    const raw = read(DRAFT);
    if (raw) {
      const paper = state.papers.find((p) => p.id === raw.paper_id);
      state.saved = paper ? restoreDraft(raw, paper) : null;
      if (!state.saved) { remove(DRAFT); message("Purana draft expire/invalid hai ya paper/key update hui hai; fresh paper shuru karein."); }
    }
    renderDraftNotice();
    const last = read(LAST);
    if (last?.label && typeof last.saved_at === "string") $("lastLocalResult").textContent = `Last result on this device: ${String(last.label).slice(0, 200)} · ${last.score === null ? "unscored" : `${last.score}/${last.max_score}`} · ${new Date(last.saved_at).toLocaleDateString("en-IN")}. Account history ya downloaded JSON mein poora result dekhein.`;
  } catch {
    $("roomLoadStatus").textContent = "Paper list load nahi hui. Internet check karke page reload karein; Original PDF links upar available hain.";
  }
}
init();
