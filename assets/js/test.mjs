/* EkGuru Learning — Computer Network online test.
   Loads data/banks/cn/manifest.json, fetches only the topic chunk(s) needed, and runs
   either a topic-wise test (with optional section filter) or a full mixed test. */
import { filterQuestions, gradeAttempt, sampleQuestions } from "./engine.mjs";

const ROOT = new URL("../../", import.meta.url);
const STORAGE = { sessions: "ekguru.sessions.v2", saved: "ekguru.saved.v2" };
const sessionKey = (who) => `ekguru.sessions.v3.${who || "guest"}`;
const POOL_STATUS = "all_practice"; // answer-checked + community-answered; review-only records stay out

const state = {
  site: null,
  manifest: null,
  manifestTopics: new Map(),
  chunks: new Map(),
  topicNames: new Map(),
  sectionLabels: new Map(),
  mode: "topic",
  topicId: null,
  sections: null,        // null = whole topic
  count: 20,
  language: "both",
  exam: false,
  minutes: 0,
  questions: [],
  answers: {},
  marked: new Set(),
  visited: new Set(),
  index: 0,
  checked: new Set(),
  startedAt: 0,
  timerId: null,
  elapsed: 0,
  saved: new Map(),
  sessions: [],
  owner: null,
  attemptId: null,
};

const $ = (id) => document.getElementById(id);
const esc = (value) => String(value == null ? "" : value).replace(/[&<>"']/g, (char) => (
  { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[char]
));
const root = (path) => new URL(path, ROOT).href;
const number = (value) => Number(value || 0).toLocaleString("en-IN");

function readLocal(key, fallback) {
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : fallback;
  } catch { return fallback; }
}

function writeLocal(key, value) {
  try { localStorage.setItem(key, JSON.stringify(value)); } catch { /* private mode: memory only */ }
}

async function fetchJSON(path) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 20000);
  try {
    const response = await fetch(root(path), { cache: /\.[a-f0-9]{12}\.min\.json$/.test(path) ? "default" : "no-cache", signal: controller.signal });
    if (!response.ok) throw new Error(`${response.status} for ${path}`);
    return await response.json();
  } finally { clearTimeout(timeout); }
}

function sectionShort(fullTitle) {
  return state.sectionLabels.get(fullTitle) || (fullTitle || "").replace(/^Section\s+[A-Z0-9]+\s*[-–—:]\s*/i, "").split(" (")[0];
}

function showToast(message) {
  const toast = $("toast");
  toast.textContent = message;
  toast.classList.add("show");
  clearTimeout(showToast.timer);
  showToast.timer = setTimeout(() => toast.classList.remove("show"), 2600);
}

async function loadTopic(topicId) {
  if (state.chunks.has(topicId)) return state.chunks.get(topicId);
  const entry = state.manifestTopics.get(topicId);
  if (!entry) throw new Error(`unknown topic ${topicId}`);
  const records = await fetchJSON(entry.file);
  if (!Array.isArray(records) || !records.length) throw new Error(`Empty topic ${topicId}`);
  state.chunks.set(topicId, records);
  return records;
}

async function loadTopics(topicIds) {
  const sets = await Promise.all(topicIds.map((id) => loadTopic(id)));
  return sets.flat();
}

/* ---------------------------------------------------------------- setup ---- */
function renderTopicPicker() {
  const wrap = $("topicPicker");
  wrap.innerHTML = "";
  state.site.topics.forEach((topic) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "pick-card";
    button.setAttribute("aria-pressed", String(state.topicId === topic.id));
    button.innerHTML =
      `<span class="pick-head"><span class="topic-badge">${esc(topic.id)}</span>${esc(topic.title_en)}</span>` +
      `<span class="muted small">${esc(topic.title_hi)}</span>` +
      `<span class="topic-meta"><span class="chip green">${number(topic.question_count)} questions</span>` +
      `<span class="chip neutral">${topic.section_count} sections</span></span>`;
    button.addEventListener("click", () => {
      state.topicId = topic.id;
      state.sections = null;
      renderTopicPicker();
      renderSectionPicker();
      updatePool();
    });
    wrap.appendChild(button);
  });
}

function renderSectionPicker() {
  const wrap = $("sectionPicker");
  const block = $("topicDetail");
  wrap.innerHTML = "";
  if (!state.topicId) {
    block.hidden = true;
    return;
  }
  block.hidden = false;
  const topic = state.site.topics.find((item) => item.id === state.topicId);
  $("topicDetailTitle").textContent = `${topic.id} · ${topic.title_en}`;
  const all = document.createElement("label");
  all.innerHTML = `<input type="checkbox" id="allSections" ${state.sections === null ? "checked" : ""}><span>All sections</span>`;
  wrap.appendChild(all);
  topic.sections.forEach((section) => {
    const label = document.createElement("label");
    const checked = state.sections === null || state.sections.includes(section.title);
    label.innerHTML = `<input type="checkbox" value="${esc(section.title)}" ${checked ? "checked" : ""}>` +
      `<span>${esc(section.short)} <span class="count">· ${section.count}</span></span>`;
    wrap.appendChild(label);
  });
  $("allSections").addEventListener("change", (event) => {
    state.sections = event.target.checked ? null : [];
    renderSectionPicker();
    updatePool();
  });
  wrap.querySelectorAll("input[value]").forEach((input) => {
    input.addEventListener("change", () => {
      const chosen = [...wrap.querySelectorAll("input[value]:checked")].map((node) => node.value);
      state.sections = chosen.length === topic.sections.length ? null : chosen;
      const allBox = $("allSections");
      if (allBox) allBox.checked = state.sections === null;
      updatePool();
    });
  });
}

function poolQuestions(records) {
  return filterQuestions(records, {
    verificationStatus: POOL_STATUS,
    topic: state.mode === "topic" && state.topicId ? state.topicId : "all",
  }).filter((question) => {
    if (state.mode === "topic" && state.sections) return state.sections.includes(question.subtopic);
    return true;
  });
}

let poolRequest = 0;
function updatePool() {
  const request = ++poolRequest;
  const startButton = $("startButton");
  const status = $("poolStatus");
  startButton.disabled = true;
  $("retryPoolButton").hidden = true;
  if (state.mode === "topic" && !state.topicId) {
    status.textContent = "Pehle ek topic choose karein.";
    startButton.disabled = true;
    return;
  }
  const selectedIds = state.mode === "full"
    ? state.site.topics.map((topic) => topic.id)
    : [state.topicId];

  status.textContent = "Questions load ho rahe hain…";
  Promise.all(selectedIds.map(loadTopic))
    .then((sets) => {
      if (request !== poolRequest) return;
      const pool = poolQuestions(sets.flat());
      state.poolSize = pool.length;
      status.textContent = `${number(pool.length)} questions ready` +
        (state.mode === "full" ? " (all 7 topics mixed)" : ` — ${state.topicId}`);
      startButton.disabled = pool.length === 0;
      const select = $("countSelect");
      const wanted = [10, 20, 30, 50, 100, "all"];
      select.innerHTML = "";
      wanted.forEach((value) => {
        if (value !== "all" && value > pool.length) return;
        const option = document.createElement("option");
        option.value = String(value);
        option.textContent = value === "all" ? `All ${number(pool.length)} questions` : `${value} questions`;
        if (state.count === value || (!select.options.length && value === 20)) option.selected = true;
        select.appendChild(option);
      });
      if (!select.options.length) {
        const option = document.createElement("option");
        option.value = "all";
        option.textContent = `All ${number(pool.length)} questions`;
        option.selected = true;
        select.appendChild(option);
      }
      state.count = select.value === "all" ? "all" : Number(select.value);
    })
    .catch((error) => {
      if (request !== poolRequest) return;
      $("retryPoolButton").hidden = false;
      status.textContent = "Question data load nahi hua: " + error.message;
      startButton.disabled = true;
    });
}

function renderSavedPanel() {
  const panel = $("savedPanel");
  const count = state.saved.size;
  panel.hidden = count === 0;
  if (!count) return;
  $("savedCount").textContent = `${count} saved`;
  $("practiceSavedButton").disabled = false;
  $("clearSavedButton").disabled = false;
}

function renderHistory() {
  const list = $("historyList");
  list.innerHTML = "";
  if (!state.sessions.length) {
    list.innerHTML = '<p class="muted small">Abhi tak koi test nahi diya.</p>';
    return;
  }
  state.sessions.slice(0, 6).forEach((session) => {
    const row = document.createElement("div");
    row.className = "material-meta";
    row.innerHTML = `<span class="chip neutral">${esc(session.date)}</span>` +
      `<span class="chip">${esc(session.label)}</span>` +
      `<span class="chip green">${session.correct}/${session.total} · ${session.percent}%</span>`;
    list.appendChild(row);
  });
}

function setMode(mode) {
  state.mode = mode;
  if (mode === "full") state.topicId = null;
  $("modeTopic").setAttribute("aria-pressed", String(mode === "topic"));
  $("modeFull").setAttribute("aria-pressed", String(mode === "full"));
  $("topicBlock").hidden = mode !== "topic";
  $("fullBlock").hidden = mode !== "full";
  $("topicDetail").hidden = mode !== "topic" || !state.topicId;
  renderTopicPicker();
  renderSectionPicker();
  updatePool();
}

/* ------------------------------------------------------------- session ----- */
async function startTest(questionList, label, presetAnswers) {
  await window.EkGuruAccount?.ready;
  state.questions = questionList;
  state.owner = window.EkGuruAccount?.user?.id || null;
  state.attemptId = globalThis.crypto?.randomUUID?.() || null;
  state.sessions = readLocal(sessionKey(state.owner), []);
  state.answers = presetAnswers || {};
  state.marked = new Set();
  state.visited = new Set();
  document.body.classList.add("cbt-active");
  $("palettePanel").classList.remove("is-open");
  $("paletteToggle").setAttribute("aria-expanded", "false");
  state.checked = new Set();
  state.index = 0;
  state.startedAt = Date.now();
  state.elapsed = 0;
  state.label = label;
  $("setupPanel").hidden = true;
  $("playerPanel").hidden = false;
  $("resultPanel").hidden = true;
  $("sessionLabel").textContent = label;
  renderQuestion();
  renderPalette();
  updateProgress();
  startTimer();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function startTimer() {
  clearInterval(state.timerId);
  const timer = $("timer");
  timer.textContent = state.exam && state.minutes ? formatTime(state.minutes * 60) : "00:00";
  state.timerId = setInterval(() => {
    state.elapsed = Math.floor((Date.now() - state.startedAt) / 1000);
    if (state.exam && state.minutes) {
      const left = state.minutes * 60 - state.elapsed;
      timer.textContent = formatTime(Math.max(0, left));
      if (left <= 0) {
        clearInterval(state.timerId);
        showToast("Time up — test submit ho gaya.");
        finishTest(true);
      }
    } else {
      timer.textContent = formatTime(state.elapsed);
    }
  }, 1000);
}

function formatTime(seconds) {
  const safe = Math.max(0, Math.floor(seconds));
  const minutes = String(Math.floor(safe / 60)).padStart(2, "0");
  return `${minutes}:${String(safe % 60).padStart(2, "0")}`;
}

function currentQuestion() {
  return state.questions[state.index];
}

function localized(primaryEn, primaryHi) {
  if (state.language === "en") return { main: primaryEn || primaryHi || "", second: "" };
  if (state.language === "hi") return { main: primaryHi || primaryEn || "", second: "" };
  const main = primaryEn || primaryHi || "";
  const second = primaryHi && primaryHi !== main ? primaryHi : "";
  return { main, second };
}

function renderQuestion() {
  const question = currentQuestion();
  state.visited.add(question.id);
  const stem = localized(question.stem_en, question.stem_hi);
  $("questionNumber").textContent = `Question ${state.index + 1} of ${state.questions.length}`;
  $("questionTopic").textContent = `${question.topic_id} · ${sectionShort(question.subtopic)}`;
  $("questionStem").textContent = stem.main;
  $("stemSecondary").textContent = stem.second;
  $("stemSecondary").hidden = !stem.second;

  const list = $("optionList");
  list.innerHTML = "";
  const reveal = state.checked.has(question.id);
  question.options.forEach((option) => {
    const text = localized(option.text_en, option.text_hi);
    const button = document.createElement("button");
    button.type = "button";
    button.className = "option";
    button.setAttribute("aria-pressed", String(state.answers[question.id] === option.id));
    button.innerHTML = `<span class="key">${esc(option.id)}</span><span class="opt-text">${esc(text.main)}` +
      (text.second ? `<span class="opt-secondary">${esc(text.second)}</span>` : "") + "</span>";
    if (reveal) {
      button.disabled = true;
      if (option.id === question.answer_option_id) button.classList.add("correct");
      else if (state.answers[question.id] === option.id) button.classList.add("wrong");
    } else {
      button.addEventListener("click", () => selectOption(option.id));
    }
    list.appendChild(button);
  });

  $("markButton").setAttribute("aria-pressed", String(state.marked.has(question.id)));
  $("saveButton").setAttribute("aria-pressed", String(state.saved.has(question.id)));
  $("prevButton").disabled = state.index === 0;
  $("nextButton").textContent = state.index === state.questions.length - 1 ? "Save & submit" : "Save & next →";
  $("markNextButton").textContent = "Mark for review & next";

  const feedback = $("feedback");
  if (reveal) {
    const correct = state.answers[question.id] === question.answer_option_id;
    const answerText = localized(
      (question.options.find((option) => option.id === question.answer_option_id) || {}).text_en,
      (question.options.find((option) => option.id === question.answer_option_id) || {}).text_hi
    );
    const explanation = localized(question.explanation_en, question.explanation_hi);
    const nukta = localized(question.nukta_en, question.nukta_hi);
    feedback.hidden = false;
    feedback.className = "feedback" + (correct ? "" : " bad");
    feedback.innerHTML =
      `<h4>${correct ? "✅ Sahi jawab!" : "❌ Galat — sahi jawab: " + esc(question.answer_option_id)}</h4>` +
      `<p><b>${esc(question.answer_option_id)})</b> ${esc(answerText.main)}</p>` +
      (explanation.main ? `<p>${esc(explanation.main)}</p>` : "") +
      (nukta.main ? `<div class="nukta"><b>Nukta:</b> ${esc(nukta.main)}</div>` : "");
  } else {
    feedback.hidden = true;
    feedback.innerHTML = "";
  }
}

function selectOption(optionId) {
  const question = currentQuestion();
  state.answers[question.id] = optionId;
  if (!state.exam) state.checked.add(question.id);
  renderQuestion();
  renderPalette();
  updateProgress();
  if (!state.exam) {
    const correct = optionId === question.answer_option_id;
    showToast(correct ? "Sahi! ✅" : "Galat — neeche explanation dekhein.");
  }
}

function renderPalette() {
  const grid = $("paletteGrid");
  grid.innerHTML = "";
  state.questions.forEach((question, index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = String(index + 1);
    if (state.visited.has(question.id)) button.classList.add("visited");
    if (state.answers[question.id]) button.classList.add("answered");
    if (state.marked.has(question.id)) button.classList.add("marked");
    if (index === state.index) button.classList.add("current");
    const status = state.marked.has(question.id) ? (state.answers[question.id] ? "answered and marked" : "marked for review")
      : state.answers[question.id] ? "answered" : state.visited.has(question.id) ? "not answered" : "not visited";
    button.setAttribute("aria-label", `Question ${index + 1}, ${status}`);
    if (index === state.index) button.setAttribute("aria-current", "true");
    button.addEventListener("click", () => {
      state.index = index;
      renderQuestion();
      renderPalette();
      updateProgress();
      $("palettePanel").classList.remove("is-open");
      $("paletteToggle").setAttribute("aria-expanded", "false");
      $("questionCard").scrollIntoView?.({ block: "start", behavior: "smooth" });
    });
    grid.appendChild(button);
  });
  const answered = state.questions.filter((q) => state.answers[q.id]).length;
  $("paletteSummary").textContent = `${answered} answered · ${state.questions.length - answered} pending · ${state.marked.size} marked`;
}

function updateProgress() {
  const answered = state.questions.filter((question) => state.answers[question.id]).length;
  $("progressFill").style.width = `${(answered / state.questions.length) * 100}%`;
  $("progressText").textContent = `${answered} / ${state.questions.length} answered`;
  $("progressTrack").setAttribute("aria-valuenow", String(answered));
  $("progressTrack").setAttribute("aria-valuemax", String(state.questions.length));
}

/* -------------------------------------------------------------- result ----- */
function finishTest(silent) {
  const answeredCount = state.questions.filter((question) => state.answers[question.id]).length;
  if (!silent && !window.confirm(`Submit test?\nAnswered: ${answeredCount}/${state.questions.length}\nNot answered: ${state.questions.length - answeredCount}\nMarked for review: ${state.marked.size} (selected answers will be counted)`)) return;
  state.elapsed = Math.floor((Date.now() - state.startedAt) / 1000);
  document.body.classList.remove("cbt-active");
  clearInterval(state.timerId);
  const result = gradeAttempt(state.questions, state.answers);
  state.lastResult = result;
  const label = state.label || "Test";
  state.sessions = [{
    date: new Date().toISOString().slice(0, 10),
    label,
    total: result.total,
    correct: result.correct,
    percent: result.percent,
  }].concat(state.sessions).slice(0, 12);
  writeLocal(sessionKey(state.owner), state.sessions);
  if (state.attemptId && window.EkGuruAccount?.saveAttempt) {
    const details = { version: 1, mode: state.exam ? "exam" : "practice", language: state.language,
      answers_saved: state.questions.length <= 150 };
    if (details.answers_saved) details.answers = state.answers;
    window.EkGuruAccount.saveAttempt({ id: state.attemptId, kind: "cn", subject_id: "computer-network",
      test_id: state.mode === "full" ? `cn-mixed-${result.total}` : `cn-topic-${(state.topicId || "mixed").toLowerCase()}-${result.total}`,
      completed_at: new Date().toISOString(), paper_id: "cn-" + (state.topicId || "full"),
      label, total: result.total, correct: result.correct, wrong: result.wrong, unanswered: result.unanswered,
      score: result.correct, max_score: result.total, duration_seconds: Math.min(604800, state.elapsed), details }, state.owner)
      .catch(() => showToast("Cloud sync pending. Result is browser mein available hai."));
  }

  $("playerPanel").hidden = true;
  $("resultPanel").hidden = false;
  $("resultIntro").textContent = `${label} · ${number(result.total)} questions · time ${formatTime(state.elapsed)}`;
  $("scoreRing").style.setProperty("--value", result.percent);
  $("scoreValue").textContent = `${result.percent}%`;
  $("scoreCaption").textContent = `${result.correct} correct`;
  $("resultStats").innerHTML = [
    ["Correct", result.correct, "green"],
    ["Wrong", result.wrong, "danger"],
    ["Skipped", result.unanswered, "warn"],
    ["Total", result.total, "neutral"],
  ].map(([label, value, tone]) => `<div class="stat"><strong>${number(value)}</strong><span>${label}</span></div>`).join("");

  renderTopicBars(result);
  renderReview();
  $("reviewList").hidden = true;
  $("reviewButton").setAttribute("aria-expanded", "false");
  renderHistory();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function renderTopicBars(result) {
  const wrap = $("topicBars");
  wrap.innerHTML = "";
  Object.keys(result.topicBreakdown).sort().forEach((topicId) => {
    const row = result.topicBreakdown[topicId];
    const percent = row.total ? Math.round((row.correct / row.total) * 100) : 0;
    const name = state.topicNames.get(topicId) || topicId;
    const block = document.createElement("div");
    block.className = "bar-row";
    block.innerHTML =
      `<div class="bar-label"><span>${esc(topicId)} · ${esc(name)}</span><span>${row.correct}/${row.total} · ${percent}%</span></div>` +
      `<div class="bar-track"><span style="width:${percent}%"></span></div>`;
    wrap.appendChild(block);
  });
}

function renderReview() {
  const wrap = $("reviewList");
  wrap.innerHTML = "";
  state.questions.forEach((question, index) => {
    const given = state.answers[question.id];
    const correct = given === question.answer_option_id;
    const item = document.createElement("article");
    item.className = "review-item" + (correct ? "" : given ? " wrong" : " skipped");
    const stem = localized(question.stem_en, question.stem_hi);
    const correctOption = question.options.find((option) => option.id === question.answer_option_id) || {};
    const givenOption = question.options.find((option) => option.id === given) || {};
    const explanation = localized(question.explanation_en, question.explanation_hi);
    const nukta = localized(question.nukta_en, question.nukta_hi);
    item.innerHTML =
      `<p class="small muted" style="margin:0">Q${index + 1} · ${esc(question.topic_id)} · ${esc(sectionShort(question.subtopic))}</p>` +
      `<p style="margin:0.2rem 0 0.5rem"><b>${esc(stem.main)}</b></p>` +
      `<p class="answer-line">Aapka jawab: <b>${given ? esc(given) + ") " + esc(localized(givenOption.text_en, givenOption.text_hi).main) : "—"}</b></p>` +
      `<p class="answer-line">Sahi jawab: <b>${esc(question.answer_option_id)}) ${esc(localized(correctOption.text_en, correctOption.text_hi).main)}</b></p>` +
      (explanation.main ? `<p class="small">${esc(explanation.main)}</p>` : "") +
      (nukta.main ? `<div class="nukta small"><b>Nukta:</b> ${esc(nukta.main)}</div>` : "");
    wrap.appendChild(item);
  });
}

/* --------------------------------------------------------------- wiring ---- */
function bind() {
  window.addEventListener("beforeunload", (event) => {
    if (!$("playerPanel").hidden) { event.preventDefault(); event.returnValue = ""; }
  });
  $("retryPoolButton").addEventListener("click", updatePool);
  $("paletteToggle").addEventListener("click", () => {
    const open = $("palettePanel").classList.toggle("is-open");
    $("paletteToggle").setAttribute("aria-expanded", String(open));
    if (open) $("palettePanel").scrollIntoView?.({ block: "nearest", behavior: "smooth" });
  });
  $("markNextButton").addEventListener("click", () => {
    state.marked.add(currentQuestion().id);
    if (state.index < state.questions.length - 1) state.index += 1;
    renderQuestion(); renderPalette(); updateProgress();
  });
  $("modeTopic").addEventListener("click", () => setMode("topic"));
  $("modeFull").addEventListener("click", () => setMode("full"));
  $("countSelect").addEventListener("change", (event) => {
    state.count = event.target.value === "all" ? "all" : Number(event.target.value);
  });
  document.querySelectorAll("[data-language]").forEach((button) => {
    button.addEventListener("click", () => {
      state.language = button.getAttribute("data-language");
      document.querySelectorAll("[data-language]").forEach((node) => {
        node.setAttribute("aria-pressed", String(node === button));
      });
      if (!$("playerPanel").hidden) renderQuestion();
    });
  });
  document.querySelectorAll("[data-pattern]").forEach((button) => {
    button.addEventListener("click", () => {
      state.exam = button.getAttribute("data-pattern") === "exam";
      document.querySelectorAll("[data-pattern]").forEach((node) => {
        node.setAttribute("aria-pressed", String(node === button));
      });
      $("timeField").hidden = !state.exam;
    });
  });
  $("minutesSelect").addEventListener("change", (event) => { state.minutes = Number(event.target.value); });

  $("startButton").addEventListener("click", async () => {
    $("startButton").disabled = true;
    try {
    const topicIds = state.mode === "full" ? state.site.topics.map((topic) => topic.id) : [state.topicId];
    const records = await loadTopics(topicIds);
    const pool = poolQuestions(records);
    const picked = sampleQuestions(pool, state.count === "all" ? pool.length : state.count);
    const label = state.mode === "full"
      ? "Full mixed test (all topics)"
      : `${state.topicId} test${state.sections ? ` · ${state.sections.length} section(s)` : " · all sections"}`;
    if (!picked.length) throw new Error("Koi question nahi mila; section choose karein.");
    await startTest(picked, label);
    } catch (error) {
      showToast("Test load nahi hua. Dobara try karein. " + error.message);
    } finally { $("startButton").disabled = false; }
  });

  $("practiceSavedButton").addEventListener("click", async () => {
    try {
    const ids = [...state.saved.keys()];
    const topicIds = [...new Set(ids.map((id) => state.saved.get(id)))];
    const records = await loadTopics(topicIds);
    const picked = records.filter((question) => state.saved.has(question.id));
    if (!picked.length) { showToast("Saved questions abhi khaali hain."); return; }
    await startTest(picked, `Saved questions (${picked.length})`);
    } catch (error) { showToast("Saved questions load nahi hue. Dobara try karein."); }
  });
  $("clearSavedButton").addEventListener("click", () => {
    state.saved.clear();
    writeLocal(STORAGE.saved, []);
    renderSavedPanel();
    if (currentQuestion()) renderQuestion();
    showToast("Saved questions clear ho gaye.");
  });

  $("prevButton").addEventListener("click", () => { if (state.index > 0) { state.index -= 1; renderQuestion(); renderPalette(); } });
  $("nextButton").addEventListener("click", () => { if (state.index < state.questions.length - 1) { state.index += 1; renderQuestion(); renderPalette(); } else finishTest(false); });
  $("clearAnswerButton").addEventListener("click", () => {
    const question = currentQuestion();
    delete state.answers[question.id];
    state.checked.delete(question.id);
    renderQuestion(); renderPalette(); updateProgress();
  });
  $("markButton").addEventListener("click", () => {
    const question = currentQuestion();
    if (state.marked.has(question.id)) state.marked.delete(question.id);
    else state.marked.add(question.id);
    renderQuestion(); renderPalette();
  });
  $("saveButton").addEventListener("click", () => {
    const question = currentQuestion();
    if (state.saved.has(question.id)) state.saved.delete(question.id);
    else state.saved.set(question.id, question.topic_id);
    writeLocal(STORAGE.saved, [...state.saved.entries()]);
    renderSavedPanel();
    renderQuestion();
  });
  $("finishButton").addEventListener("click", () => finishTest(false));
  $("exitButton").addEventListener("click", () => {
    if (!window.confirm("Test chhod dein? Answer save nahi honge.")) return;
    clearInterval(state.timerId);
    document.body.classList.remove("cbt-active");
    $("playerPanel").hidden = true;
    $("setupPanel").hidden = false;
  });

  $("reviewButton").addEventListener("click", () => {
    const list = $("reviewList");
    const open = list.hidden;
    list.hidden = !open;
    $("reviewButton").setAttribute("aria-expanded", String(open));
  });
  $("retryWrongButton").addEventListener("click", () => {
    const wrong = state.questions.filter((question) => {
      const given = state.answers[question.id];
      return given && given !== question.answer_option_id;
    });
    if (!wrong.length) { showToast("Koi galat jawab nahi hai — shabaash!"); return; }
    startTest(wrong, `Retry — ${wrong.length} galat questions`);
  });
  $("newTestButton").addEventListener("click", () => {
    clearInterval(state.timerId);
    $("resultPanel").hidden = true;
    $("setupPanel").hidden = false;
    updatePool();
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

async function init() {
  try {
    const [site, manifest] = await Promise.all([
      fetchJSON("data/banks/cn/topics.json"),
      fetchJSON("data/banks/cn/manifest.json"),
    ]);
    state.site = site;
    state.manifest = manifest;
    manifest.topics.forEach((topic) => state.manifestTopics.set(topic.topic_id, topic));
    state.site.topics.forEach((topic) => {
      state.topicNames.set(topic.id, topic.title_en);
      topic.sections.forEach((section) => state.sectionLabels.set(section.title, section.short));
    });
    state.saved = new Map(readLocal(STORAGE.saved, []));
    await window.EkGuruAccount?.ready;
    state.sessions = readLocal(sessionKey(window.EkGuruAccount?.user?.id), []);
    /* student-facing line: sirf numbers — koi internal build id/version nahi */
    $("bankInfo").textContent =
      `${number(manifest.published_question_count)} questions · ${manifest.topics.length} topics`;
    bind();
    const params = new URLSearchParams(window.location.search);
    const topicParam = params.get("topic");
    const countParam = params.get("count");
    if (["10", "20", "30", "50", "100", "all"].includes(countParam)) state.count = countParam === "all" ? "all" : Number(countParam);
    if (["practice", "exam"].includes(params.get("pattern"))) {
      state.exam = params.get("pattern") === "exam";
      document.querySelectorAll("[data-pattern]").forEach((node) => node.setAttribute("aria-pressed", String(node.getAttribute("data-pattern") === params.get("pattern"))));
      $("timeField").hidden = !state.exam;
    }
    const minutesParam = params.get("minutes");
    if ([...$("minutesSelect").options].some((option) => option.value === minutesParam)) {
      state.minutes = Number(minutesParam); $("minutesSelect").value = minutesParam;
    }
    const sectionParam = params.get("section");
    renderSavedPanel();
    renderHistory();
    if (topicParam && state.site.topics.some((topic) => topic.id === topicParam)) {
      state.topicId = topicParam;
      const topic = state.site.topics.find((item) => item.id === topicParam);
      if (sectionParam) {
        const matched = topic.sections.filter((section) => section.short.toLowerCase() === sectionParam.toLowerCase()
          || section.title.toLowerCase().includes(sectionParam.toLowerCase()));
        state.sections = matched.length ? matched.map((section) => section.title) : null;
      }
      setMode("topic");
    } else {
      setMode(params.get("mode") === "full" ? "full" : "topic");
    }
  } catch (error) {
    $("bankInfo").textContent = "Data load nahi hua";
    $("setupPanel").innerHTML = `<div class="card"><p role="alert">Question data load nahi hua (${esc(error.message)}). Internet check karke dobara try karein.</p><button class="button primary" id="retryInitButton" type="button">Dobara load karo</button></div>`;
    $("retryInitButton").addEventListener("click", () => window.location.reload());
  }
}

window.addEventListener("ekguru:account", () => {
  if (!$("playerPanel").hidden) return;
  state.sessions = readLocal(sessionKey(window.EkGuruAccount?.user?.id), []); renderHistory();
});
init();
