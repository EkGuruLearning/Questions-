/* EkGuru Learning — Computer Network online test.
   Loads data/banks/cn/manifest.json, fetches only the topic chunk(s) needed, and runs
   either a topic-wise test (with optional section filter) or a full mixed test. */
import { filterQuestions, gradeAttempt, sampleQuestions } from "./engine.mjs";

const ROOT = new URL("../../../", import.meta.url);
const STORAGE = { sessions: "ekguru.sessions.v2", saved: "ekguru.saved.v2" };
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
  index: 0,
  checked: new Set(),
  startedAt: 0,
  timerId: null,
  elapsed: 0,
  saved: new Map(),
  sessions: [],
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
  const response = await fetch(root(path), { cache: "no-cache" });
  if (!response.ok) throw new Error(`${response.status} for ${path}`);
  return response.json();
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

function updatePool() {
  const startButton = $("startButton");
  const status = $("poolStatus");
  if (state.mode === "topic" && !state.topicId) {
    status.textContent = "Pehle ek topic choose karein.";
    startButton.disabled = true;
    return;
  }
  const selectedIds = state.mode === "full"
    ? state.site.topics.map((topic) => topic.id)
    : [state.topicId];

  Promise.all(selectedIds.map(loadTopic))
    .then((sets) => {
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
  state.questions = questionList;
  state.answers = presetAnswers || {};
  state.marked = new Set();
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
  const card = $("questionCard");
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
  $("nextButton").hidden = state.index === state.questions.length - 1;

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
    if (state.answers[question.id]) button.classList.add("answered");
    if (state.marked.has(question.id)) button.classList.add("marked");
    if (index === state.index) button.classList.add("current");
    button.setAttribute("aria-label", `Question ${index + 1}${state.marked.has(question.id) ? " (marked)" : ""}`);
    button.addEventListener("click", () => {
      state.index = index;
      renderQuestion();
      renderPalette();
      updateProgress();
    });
    grid.appendChild(button);
  });
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
  if (!silent && answeredCount < state.questions.length) {
    const pending = state.questions.length - answeredCount;
    if (!window.confirm(`${pending} question abhi khaali hain. Test submit karein?`)) return;
  }
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
  writeLocal(STORAGE.sessions, state.sessions);

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
    const topicIds = state.mode === "full" ? state.site.topics.map((topic) => topic.id) : [state.topicId];
    const records = await loadTopics(topicIds);
    const pool = poolQuestions(records);
    const picked = sampleQuestions(pool, state.count === "all" ? pool.length : state.count);
    const label = state.mode === "full"
      ? "Full mixed test (all topics)"
      : `${state.topicId} test${state.sections ? ` · ${state.sections.length} section(s)` : " · all sections"}`;
    startTest(picked, label);
  });

  $("practiceSavedButton").addEventListener("click", async () => {
    const ids = [...state.saved.keys()];
    const topicIds = [...new Set(ids.map((id) => state.saved.get(id)))];
    const records = await loadTopics(topicIds);
    const picked = records.filter((question) => state.saved.has(question.id));
    if (!picked.length) { showToast("Saved questions abhi khaali hain."); return; }
    startTest(picked, `Saved questions (${picked.length})`);
  });
  $("clearSavedButton").addEventListener("click", () => {
    state.saved.clear();
    writeLocal(STORAGE.saved, []);
    renderSavedPanel();
    renderQuestion();
    showToast("Saved questions clear ho gaye.");
  });

  $("prevButton").addEventListener("click", () => { if (state.index > 0) { state.index -= 1; renderQuestion(); renderPalette(); } });
  $("nextButton").addEventListener("click", () => { if (state.index < state.questions.length - 1) { state.index += 1; renderQuestion(); renderPalette(); } });
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
      fetchJSON("data/site.json"),
      fetchJSON("data/banks/cn/manifest.json"),
    ]);
    state.site = site.subjects.find((subject) => subject.id === "computer-network");
    state.manifest = manifest;
    manifest.topics.forEach((topic) => state.manifestTopics.set(topic.topic_id, topic));
    state.site.topics.forEach((topic) => {
      state.topicNames.set(topic.id, topic.title_en);
      topic.sections.forEach((section) => state.sectionLabels.set(section.title, section.short));
    });
    state.saved = new Map(readLocal(STORAGE.saved, []));
    state.sessions = readLocal(STORAGE.sessions, []);
    $("bankInfo").textContent = `${number(manifest.published_question_count)} questions · 7 topics · build ${manifest.bank_build_id}`;
    bind();
    const params = new URLSearchParams(window.location.search);
    const topicParam = params.get("topic");
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
      setMode("topic");
    }
  } catch (error) {
    $("setupPanel").innerHTML = `<p class="empty-state">Question data load nahi hua (${esc(error.message)}). Page refresh karein.</p>`;
  }
}

init();
