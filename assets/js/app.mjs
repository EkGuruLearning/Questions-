import {
  STATUS,
  SOURCE_TYPE,
  answerLabel,
  filterQuestions,
  gradeAttempt,
  isPracticeEligible,
  localizeText,
  sampleQuestions,
  sourceTypeLabel,
  verificationLabel,
} from "./engine.mjs";

const STORAGE = Object.freeze({
  history: "ekguru.portal.history.v1",
  bookmarks: "ekguru.portal.bookmarks.v1",
  resume: "ekguru.portal.resume.v1",
});
const SOURCE_TYPES = [
  SOURCE_TYPE.VERIFIED_OFFICIAL,
  SOURCE_TYPE.CLAIMED_PYQ,
  SOURCE_TYPE.INTERNAL,
  SOURCE_TYPE.TEXTBOOK,
  SOURCE_TYPE.ORIGINAL,
];
const TOPIC_FALLBACK_NAMES = {
  T01: "Introduction of Data Communication",
  T02: "Network Models (OSI & TCP/IP)",
  T03: "Addressing (MAC, IPv4, IPv6, Port, DNS)",
  T04: "Networking Devices",
  T05: "Transmission Medium",
  T06: "OSI Layers in Detail",
  T07: "Network Security",
};

const state = {
  catalog: null,
  cnSubject: null,
  manifest: null,
  topicById: new Map(),
  chunkPromises: new Map(),
  sourceRegister: null,
  sourceRegisterPromise: null,
  session: null,
  lastResult: null,
  timer: null,
  toastTimer: null,
};

const $ = (id) => document.getElementById(id);
const clone = (value) => JSON.parse(JSON.stringify(value));

function element(tag, className = "", text = null) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== null && text !== undefined) node.textContent = String(text);
  return node;
}

function appendText(parent, tag, value, className = "") {
  const node = element(tag, className, value);
  parent.append(node);
  return node;
}

function readLocal(key, fallback) {
  try {
    const value = localStorage.getItem(key);
    return value ? JSON.parse(value) : fallback;
  } catch {
    return fallback;
  }
}

function writeLocal(key, value) {
  try {
    localStorage.setItem(key, JSON.stringify(value));
    return true;
  } catch {
    return false;
  }
}

function removeLocal(key) {
  try {
    localStorage.removeItem(key);
  } catch {
    // Private browsing and storage-disabled contexts are supported as memory-only sessions.
  }
}

function showToast(message) {
  const toast = $("toast");
  toast.textContent = message;
  toast.classList.add("show");
  clearTimeout(state.toastTimer);
  state.toastTimer = setTimeout(() => toast.classList.remove("show"), 3500);
}

async function fetchJSON(path) {
  const response = await fetch(path, { cache: "no-cache" });
  if (!response.ok) throw new Error(`Request failed (${response.status}) for ${path}`);
  return response.json();
}

function countRecords(record) {
  return Number.isInteger(record) ? record : 0;
}

function setSummary() {
  const liveSubjects = (state.catalog.subjects || []).filter((subject) => subject.available);
  const counts = state.manifest.by_verification || {};
  $("publishedSubjects").textContent = String(liveSubjects.length);
  $("totalQuestions").textContent = Number(state.manifest.question_count || 0).toLocaleString("en-IN");
  $("totalTopics").textContent = String(state.manifest.topic_count || 0);
  $("officialCount").textContent = String(counts[STATUS.OFFICIAL] || 0);
  $("answerCheckedCount").textContent = String(counts[STATUS.ANSWER_CHECKED] || 0);
  $("buildInfo").textContent = `Build ${state.manifest.bank_build_id} · ${String(state.manifest.generated_on || "date not recorded")}`;
}

function setSubjectCards() {
  const container = $("subjectGrid");
  container.replaceChildren();
  for (const subject of state.catalog.subjects || []) {
    const card = element("article", "card subject-card");
    const status = element("span", `status-chip ${subject.available ? "live" : subject.status === "planned" ? "planned" : "unavailable"}`,
      subject.available ? "Available" : subject.status === "planned" ? "Planned · unavailable" : `${subject.status} · unavailable`);
    card.append(status);
    appendText(card, "h3", subject.name);
    if (subject.name_hi) appendText(card, "p", subject.name_hi, "muted");
    appendText(card, "p", subject.summary || (subject.available ? "Published practice bank." : "No published question bank is available."));

    if (subject.available) {
      const count = Number(subject.question_count || 0);
      const details = element("div", "meta-row");
      details.append(element("span", "meta-chip", `${count.toLocaleString("en-IN")} records`));
      details.append(element("span", "meta-chip", `${subject.topic_count || 0} topics`));
      details.append(element("span", "meta-chip", `${subject.verification_summary?.[STATUS.OFFICIAL] || 0} official paper + key checked`));
      card.append(details);
      const link = element("a", "button primary small", "Practice this subject");
      link.href = "#practice";
      link.addEventListener("click", () => {
        $("subjectSelect").value = subject.id;
        refreshPoolStatus();
      });
      card.append(link);
    } else {
      const topics = Array.isArray(subject.syllabus_topics) ? subject.syllabus_topics : [];
      if (topics.length) {
        const details = element("details", "disclosure");
        appendText(details, "summary", "Catalog scope (not a question bank)");
        const list = element("ul");
        topics.forEach((topic) => appendText(list, "li", topic));
        details.append(list);
        card.append(details);
      }
      const unavailable = element("button", "button secondary small", "Tests not available");
      unavailable.type = "button";
      unavailable.disabled = true;
      card.append(unavailable);
    }
    container.append(card);
  }
}

function fillSelect(select, items, emptyLabel = null) {
  const first = select.querySelector("option");
  select.replaceChildren();
  if (first && emptyLabel !== null) {
    first.value = "all";
    first.textContent = emptyLabel;
    select.append(first);
  } else if (emptyLabel !== null) {
    const option = element("option", "", emptyLabel);
    option.value = "all";
    select.append(option);
  }
  for (const item of items) {
    const option = element("option", "", item.label);
    option.value = item.value;
    if (item.disabled) option.disabled = true;
    select.append(option);
  }
}

function buildSelectors() {
  const subjects = (state.catalog.subjects || []).map((subject) => ({
    value: subject.id,
    label: `${subject.name} — ${subject.available ? "available" : "not available"}`,
    disabled: !subject.available,
  }));
  fillSelect($("subjectSelect"), subjects);
  $("subjectSelect").value = state.cnSubject.id;

  const topics = [
    { value: "all", label: `All topics (${state.manifest.question_count})` },
    ...state.manifest.topics.map((topic) => ({
      value: topic.topic_id,
      label: `${topic.topic_id} · ${topic.topic_name} (${topic.published_question_count} practice / ${topic.record_count} canonical)`,
    })),
  ];
  fillSelect($("topicSelect"), topics);

  const profileItems = (state.catalog.exam_profiles || [])
    .filter((profile) => profile.exam_tag)
    .map((profile) => ({
      value: profile.id,
      label: `${profile.name} — ${profile.tagged_record_count || 0} tag matches (not proof of PYQ)`,
    }));
  fillSelect($("examSelect"), profileItems, "All exam/practice tags");

  const sourceCounts = state.manifest.by_source_type || {};
  const sourceItems = SOURCE_TYPES.map((sourceType) => ({
    value: sourceType,
    label: `${sourceTypeLabel(sourceType)} (${sourceCounts[sourceType] || 0})`,
    disabled: !(sourceCounts[sourceType] || 0),
  }));
  fillSelect($("sourceTypeSelect"), sourceItems, "All source types");

  const statusCounts = state.manifest.by_verification || {};
  const statusSelect = $("verificationSelect");
  statusSelect.querySelector('option[value="reviewed_answers"]').textContent = `Answer-checked + official evidence (${(statusCounts[STATUS.ANSWER_CHECKED] || 0) + (statusCounts[STATUS.OFFICIAL] || 0)})`;
  statusSelect.querySelector('option[value="all_practice"]').textContent = `Reviewed + unverified claimed answers (${(statusCounts[STATUS.ANSWER_CHECKED] || 0) + (statusCounts[STATUS.OFFICIAL] || 0) + (statusCounts[STATUS.CLAIMED_UNVERIFIED] || 0)})`;
  statusSelect.querySelector('option[value="claimed_answer_unverified"]').textContent = `Unverified claimed answers only (${statusCounts[STATUS.CLAIMED_UNVERIFIED] || 0})`;
  statusSelect.querySelector('option[value="paper_and_key_checked"]').textContent = `Official paper + final key checked only (${statusCounts[STATUS.OFFICIAL] || 0})`;
  statusSelect.querySelector('option[value="disputed"]').textContent = `Disputed — review only (${statusCounts[STATUS.DISPUTED] || 0})`;
  statusSelect.querySelector('option[value="pending_review"]').textContent = `Pending review — not test-eligible (${statusCounts[STATUS.PENDING] || 0})`;
}

function buildLibrary() {
  const root = $("libraryContent");
  root.replaceChildren();
  const cnBooks = state.cnSubject.books || [];
  if (!cnBooks.length) {
    root.append(element("p", "empty-state", "No library files are attached to this catalog yet."));
    return;
  }
  for (const topic of state.cnSubject.topics || []) {
    const details = element("details", "card library-topic");
    const summary = element("summary");
    summary.textContent = `${topic.id} · ${topic.name} — ${topic.question_count} canonical records`;
    details.append(summary);
    const links = element("div", "library-links");
    const books = cnBooks.filter((book) => book.topic_id === topic.id);
    for (const book of books) {
      const anchor = element("a", "library-link");
      anchor.href = book.href;
      anchor.textContent = book.label;
      if (book.opens_in_new_tab) {
        anchor.target = "_blank";
        anchor.rel = "noopener noreferrer";
      }
      const note = book.note || "Repository material.";
      const small = element("small", "", `${book.status}: ${note}`);
      anchor.append(small);
      if (book.kind === "standalone_cbt") {
        anchor.setAttribute("aria-label", `${book.label}; opens a new tab and launches the shared topic practice portal`);
      }
      links.append(anchor);
    }
    details.append(links);
    root.append(details);
  }
}

function renderVerificationSummary() {
  const wrapper = $("verificationSummary");
  const sourceCounts = state.manifest.by_source_type || {};
  const statusCounts = state.manifest.by_verification || {};
  wrapper.replaceChildren();
  const h = appendText(wrapper, "h3", "Current counts — not a blanket verification claim");
  h.id = "verificationSummaryHeading";
  const tableWrap = element("div", "table-wrap");
  const table = element("table");
  const thead = element("thead");
  const headRow = element("tr");
  ["Answer-verification status", "Records", "Meaning"].forEach((title) => appendText(headRow, "th", title));
  thead.append(headRow);
  const tbody = element("tbody");
  const statusRows = [
    [STATUS.OFFICIAL, "Official paper + final key checked", "Requires exact question-level official paper and final/corrected key evidence."],
    [STATUS.ANSWER_CHECKED, "Answer checked", "Answer-level curation; not official exam/key matching."],
    [STATUS.CLAIMED_UNVERIFIED, "Claimed answer — unverified", "Opt-in practice only; displayed with this label."],
    [STATUS.DISPUTED, "Disputed", "Excluded from practice tests."],
    [STATUS.PENDING, "Pending review", "Excluded from practice tests."],
  ];
  for (const [key, label, meaning] of statusRows) {
    const row = element("tr");
    appendText(row, "td", label);
    appendText(row, "td", statusCounts[key] || 0);
    appendText(row, "td", meaning);
    tbody.append(row);
  }
  table.append(thead, tbody);
  tableWrap.append(table);
  wrapper.append(tableWrap);

  const sourceHeading = appendText(wrapper, "h3", "Source types");
  sourceHeading.style.marginTop = "1rem";
  const sourceList = element("div", "meta-row");
  for (const sourceType of SOURCE_TYPES) {
    sourceList.append(element("span", "source-chip", `${sourceTypeLabel(sourceType)}: ${sourceCounts[sourceType] || 0}`));
  }
  wrapper.append(sourceList);
  appendText(wrapper, "p", `Generated build ${state.manifest.bank_build_id}; official evidence entries are question-level, not inferred from exam names.`, "field-help");
}

function activeExamTag() {
  const profileId = $("examSelect").value;
  if (!profileId || profileId === "all") return "all";
  const profile = (state.catalog.exam_profiles || []).find((item) => item.id === profileId);
  return profile?.exam_tag || "all";
}

function currentFilters() {
  return {
    topic: $("topicSelect").value || "all",
    examTag: activeExamTag(),
    verificationStatus: $("verificationSelect").value || "reviewed_answers",
    sourceType: $("sourceTypeSelect").value || "all",
    difficulty: $("difficultySelect").value || "all",
  };
}

function basePoolCount(filters) {
  const topicChunks = state.manifest.topics || [];
  const selected = filters.topic === "all" ? topicChunks : topicChunks.filter((topic) => topic.topic_id === filters.topic);
  const statusKeys = filters.verificationStatus === "reviewed_answers"
    ? [STATUS.OFFICIAL, STATUS.ANSWER_CHECKED]
    : filters.verificationStatus === "all_practice"
      ? [STATUS.OFFICIAL, STATUS.ANSWER_CHECKED, STATUS.CLAIMED_UNVERIFIED]
      : [filters.verificationStatus];
  return selected.reduce((total, topic) => {
    const counts = topic.by_verification || {};
    return total + statusKeys.reduce((subtotal, key) => subtotal + countRecords(counts[key]), 0);
  }, 0);
}

function refreshPoolStatus() {
  if (!state.manifest) return;
  const filters = currentFilters();
  const baseCount = basePoolCount(filters);
  const testableStatus = ![STATUS.DISPUTED, STATUS.PENDING].includes(filters.verificationStatus);
  const subjectAvailable = state.cnSubject?.available && $("subjectSelect").value === state.cnSubject.id;
  const hasBasePool = baseCount > 0 && testableStatus && subjectAvailable;
  $("startButton").disabled = !hasBasePool;
  $("randomButton").disabled = !hasBasePool;
  $("startButton").textContent = hasBasePool ? "Start practice" : "No test-eligible questions in this selection";
  const countValue = $("questionCountSelect").value;
  const countLabel = countValue === "all" ? "all matching records" : `up to ${countValue} questions`;
  $("poolStatus").textContent = hasBasePool
    ? `At least ${baseCount.toLocaleString("en-IN")} records match this topic and verification status before source, exam-tag and difficulty filters; exact matches are calculated after loading the selected topic chunk(s). Requested: ${countLabel}.`
    : `No test-eligible records for the selected status/subject. Disputed and pending records cannot be started.`;
  if (filters.verificationStatus === "all_practice" || filters.verificationStatus === STATUS.CLAIMED_UNVERIFIED) {
    $("poolDisclosure").textContent = "Unverified claimed-answer records are included only because you selected an opt-in status filter. Each item keeps its unverified source/answer label; it is not counted as an official PYQ.";
  } else if (filters.verificationStatus === STATUS.OFFICIAL) {
    $("poolDisclosure").textContent = "This filter requires question-level official paper and final/corrected answer-key evidence. If the count is zero, no verified-PYQ session can be started.";
  } else if (filters.verificationStatus === STATUS.DISPUTED || filters.verificationStatus === STATUS.PENDING) {
    $("poolDisclosure").textContent = "Disputed and pending-review questions are available for audit labels only and are excluded from practice sessions.";
  } else {
    $("poolDisclosure").textContent = "Answer-checked records are answer-level reviewed only; they are not automatically official PYQs. Topic data is fetched only after you start a set.";
  }
}

async function loadTopicChunk(topicId) {
  const chunk = state.topicById.get(topicId);
  if (!chunk) throw new Error(`Topic ${topicId} is not present in the generated manifest.`);
  if (state.chunkPromises.has(topicId)) return state.chunkPromises.get(topicId);
  const promise = fetchJSON(chunk.file).then((questions) => {
    if (!Array.isArray(questions) || questions.length !== chunk.published_question_count) {
      throw new Error(`Topic ${topicId} chunk count does not match its manifest.`);
    }
    if (questions.some((question) => question.topic_id !== topicId)) {
      throw new Error(`Topic ${topicId} chunk contains a different topic.`);
    }
    return questions;
  }).catch((error) => {
    state.chunkPromises.delete(topicId);
    throw error;
  });
  state.chunkPromises.set(topicId, promise);
  return promise;
}

async function loadQuestions(topicIds) {
  const uniqueTopicIds = [...new Set(topicIds)];
  const chunks = await Promise.all(uniqueTopicIds.map(loadTopicChunk));
  return chunks.flat();
}

function resolveTopicIds(selection) {
  if (selection && selection !== "all") return [selection];
  return (state.manifest.topics || []).map((topic) => topic.topic_id);
}

function selectedCount(pool, requested) {
  if (requested === "all") return pool.length;
  return Math.min(pool.length, Math.max(0, Number(requested) || 0));
}

function shuffleAndLimit(pool, requested) {
  return sampleQuestions(pool, requested);
}

async function startFromForm({ randomTwenty = false } = {}) {
  const filters = currentFilters();
  const subject = state.catalog.subjects.find((item) => item.id === $("subjectSelect").value);
  if (!subject?.available) {
    showToast("This subject has no published question bank yet.");
    return;
  }
  if ([STATUS.DISPUTED, STATUS.PENDING].includes(filters.verificationStatus)) {
    showToast("Disputed and pending-review records are not eligible for practice.");
    return;
  }
  const startButton = $("startButton");
  const randomButton = $("randomButton");
  startButton.disabled = true;
  randomButton.disabled = true;
  startButton.textContent = "Loading selected topic data…";
  $("poolStatus").textContent = "Loading only the selected topic chunk(s); applying exact source, exam-tag and difficulty filters…";
  try {
    const data = await loadQuestions(resolveTopicIds(filters.topic));
    const pool = filterQuestions(data, filters);
    if (!pool.length) {
      $("poolStatus").textContent = "No questions match all selected filters. Change one or more filters and try again.";
      showToast("No questions match this exact filter combination.");
      return;
    }
    const requested = randomTwenty ? Math.min(20, pool.length) : selectedCount(pool, $("questionCountSelect").value);
    const questions = shuffleAndLimit(pool, requested);
    if (!questions.length) {
      showToast("Choose at least one question.");
      return;
    }
    const mode = document.querySelector('input[name="sessionMode"]:checked')?.value || "learn";
    const language = $("languageSelect").value || "both";
    const timerMinutes = Math.min(180, Math.max(1, Number($("timeLimit").value) || 15));
    beginSession(questions, { mode, language, timerMinutes });
  } catch (error) {
    console.error(error);
    $("poolStatus").textContent = "Question data could not be loaded. Check the generated asset files and try again.";
    showToast(error.message || "Unable to load the selected question data.");
  } finally {
    refreshPoolStatus();
  }
}

function beginSession(questions, { mode = "learn", language = "both", timerMinutes = 15, resumeData = null } = {}) {
  if (!Array.isArray(questions) || !questions.length) {
    showToast("No questions are available in this session.");
    return;
  }
  stopTimer();
  const answers = Object.create(null);
  const marks = new Set();
  const seen = new Set();
  if (resumeData) {
    Object.assign(answers, resumeData.answers || {});
    (resumeData.marked || []).forEach((id) => marks.add(id));
    (resumeData.seen || []).forEach((id) => seen.add(id));
  }
  state.session = {
    questions,
    answers,
    marks,
    seen,
    currentIndex: Math.min(Math.max(0, Number(resumeData?.currentIndex) || 0), questions.length - 1),
    mode,
    language,
    startedAt: resumeData?.startedAt || Date.now(),
    timerLimitSeconds: resumeData?.timerLimitSeconds || Math.max(1, Number(timerMinutes) || 15) * 60,
    remainingSeconds: resumeData?.remainingSeconds ?? Math.max(1, Number(timerMinutes) || 15) * 60,
    completed: false,
  };
  $("setupPanel").hidden = true;
  $("resultsPanel").hidden = true;
  $("playerPanel").hidden = false;
  $("playerTitle").textContent = mode === "timed" ? "Timed practice" : "Learn mode";
  $("timerDisplay").hidden = mode !== "timed";
  $("palette").hidden = false;
  $("paletteToggle").setAttribute("aria-expanded", "true");
  $("paletteToggle").textContent = "Hide question list";
  if (mode === "timed") state.timer = setInterval(tickTimer, 1000);
  renderQuestion();
  saveResume();
  $("playerTitle").focus?.();
  $("playerPanel").scrollIntoView({ behavior: "smooth", block: "start" });
}

function formatTime(seconds) {
  const safe = Math.max(0, Number(seconds) || 0);
  const minutes = Math.floor(safe / 60);
  const remainder = safe % 60;
  return `${String(minutes).padStart(2, "0")}:${String(remainder).padStart(2, "0")}`;
}

function tickTimer() {
  const session = state.session;
  if (!session || session.completed) return;
  session.remainingSeconds = Math.max(0, session.remainingSeconds - 1);
  $("timerDisplay").textContent = `Personal timer ${formatTime(session.remainingSeconds)}`;
  if (session.remainingSeconds === 0) {
    finishSession({ automatic: true });
  } else if (session.remainingSeconds % 10 === 0) {
    saveResume();
  }
}

function stopTimer() {
  if (state.timer) clearInterval(state.timer);
  state.timer = null;
}

function renderLocalized(container, english, hindi, language) {
  const localized = localizeText(english, hindi, language);
  container.replaceChildren();
  container.lang = localized.language === "hi" ? "hi" : "en";
  container.append(document.createTextNode(localized.primary || ""));
  if (localized.secondary) {
    const secondary = element("span", "localized-secondary", localized.secondary);
    secondary.lang = "hi";
    container.append(secondary);
  }
  return localized.fallback;
}

function setTranslationNote(usedFallback) {
  const note = $("translationNote");
  note.hidden = !usedFallback;
  note.textContent = usedFallback
    ? "Hindi wording is not supplied for one or more fields; English is shown as a fallback."
    : "";
}

function renderQuestion() {
  const session = state.session;
  if (!session) return;
  const question = session.questions[session.currentIndex];
  if (!question) return;
  session.seen.add(question.id);
  $("questionNumber").textContent = `Question ${session.currentIndex + 1} of ${session.questions.length}`;
  $("questionProgress").textContent = `${Object.keys(session.answers).length} answered · ${session.questions.length} total`;
  $("answerProgress").value = Math.round((Object.keys(session.answers).length / session.questions.length) * 100);
  $("questionTopic").textContent = `${question.topic_id} · ${question.topic_name || TOPIC_FALLBACK_NAMES[question.topic_id] || "Topic"}`;
  $("questionDifficulty").textContent = `${question.difficulty || "Unrated"} · estimate`;
  $("questionVerification").textContent = verificationLabel(question.verification_status);
  $("questionId").textContent = `Question ID: ${question.id} · Source type: ${sourceTypeLabel(question.source_type)}`;
  $("sourceDetailsButton").dataset.sourceId = question.source_id || "";

  let fallbackUsed = renderLocalized($("questionStem"), question.stem_en, question.stem_hi, session.language);
  const options = $("optionList");
  options.replaceChildren();
  const selected = session.answers[question.id];
  for (const option of question.options || []) {
    const button = element("button", "option-button");
    button.type = "button";
    button.dataset.optionId = option.id;
    button.setAttribute("aria-pressed", String(selected === option.id));
    button.disabled = session.completed;
    const optionLetter = element("span", "option-letter", option.id);
    const optionText = element("span");
    fallbackUsed = renderLocalized(optionText, option.text_en, option.text_hi, session.language) || fallbackUsed;
    button.append(optionLetter, optionText);
    if (session.mode === "learn" && selected != null && option.id === question.answer_option_id) button.classList.add("is-correct");
    if (session.mode === "learn" && selected != null && selected === option.id && selected !== question.answer_option_id) button.classList.add("is-wrong");
    options.append(button);
  }
  setTranslationNote(fallbackUsed);

  $("previousButton").disabled = session.currentIndex === 0;
  $("nextButton").textContent = session.currentIndex === session.questions.length - 1 ? "Last question" : "Next";
  $("clearAnswerButton").disabled = selected == null || session.completed;
  $("markButton").disabled = session.completed;
  $("bookmarkButton").disabled = session.completed;
  const marked = session.marks.has(question.id);
  $("markButton").setAttribute("aria-pressed", String(marked));
  $("markButton").textContent = marked ? "Marked for review" : "Mark for review";
  const bookmarks = new Set(readLocal(STORAGE.bookmarks, []));
  const bookmarked = bookmarks.has(question.id);
  $("bookmarkButton").setAttribute("aria-pressed", String(bookmarked));
  $("bookmarkButton").textContent = bookmarked ? "Saved · remove" : "Save for later";
  if (session.mode === "timed") $("timerDisplay").textContent = `Personal timer ${formatTime(session.remainingSeconds)}`;
  renderFeedback(question, selected);
  renderPalette();
}

function appendLocalizedBlock(parent, english, hindi, language) {
  const block = element("p");
  const fallback = renderLocalized(block, english, hindi, language);
  parent.append(block);
  return fallback;
}

function renderFeedback(question, selected) {
  const panel = $("feedbackPanel");
  panel.hidden = true;
  if (state.session.mode !== "learn" || selected == null) return;
  panel.hidden = false;
  const isCorrect = selected === question.answer_option_id;
  $("feedbackTitle").textContent = isCorrect ? "Correct" : `Not correct · correct answer: ${question.answer_option_id}`;
  const content = $("feedbackContent");
  content.replaceChildren();
  const answer = (question.options || []).find((option) => option.id === question.answer_option_id);
  appendText(content, "p", `Correct option ${question.answer_option_id}: ${answer?.text_en || answer?.text_hi || ""}`);
  let fallback = false;
  if (question.explanation_en || question.explanation_hi) {
    const heading = appendText(content, "strong", "Explanation");
    heading.setAttribute("aria-label", "Explanation");
    fallback = appendLocalizedBlock(content, question.explanation_en, question.explanation_hi, state.session.language) || fallback;
  }
  if (question.nukta_en || question.nukta_hi) {
    const nukta = element("div", "nukta");
    appendText(nukta, "strong", "Nukta · exam point");
    fallback = appendLocalizedBlock(nukta, question.nukta_en, question.nukta_hi, state.session.language) || fallback;
    content.append(nukta);
  }
  const label = appendText(content, "p", `${verificationLabel(question.verification_status)} · ${sourceTypeLabel(question.source_type)}`, "field-help");
  label.setAttribute("aria-label", "Answer and source verification");
  if (fallback) {
    // One clear fallback notice covers the complete rendered question and feedback.
    $("translationNote").hidden = false;
    $("translationNote").textContent = "Hindi wording is not supplied for one or more question, option or explanation fields; English is shown as a fallback.";
  }
}

function renderPalette() {
  const session = state.session;
  if (!session) return;
  const grid = $("paletteGrid");
  grid.replaceChildren();
  session.questions.forEach((question, index) => {
    const button = element("button", "palette-button", index + 1);
    button.type = "button";
    button.setAttribute("aria-label", `Go to question ${index + 1}${session.answers[question.id] ? ", answered" : ""}${session.marks.has(question.id) ? ", marked for review" : ""}`);
    if (session.answers[question.id] != null) button.classList.add("answered");
    else if (session.seen.has(question.id)) button.classList.add("seen");
    if (session.marks.has(question.id)) button.classList.add("marked");
    if (index === session.currentIndex) button.classList.add("current");
    button.addEventListener("click", () => {
      session.currentIndex = index;
      renderQuestion();
      $("questionNumber").focus?.();
      saveResume();
    });
    grid.append(button);
  });
}

function saveResume() {
  const session = state.session;
  if (!session || session.completed) return;
  const resume = {
    bank_build_id: state.manifest.bank_build_id,
    question_ids: session.questions.map((question) => question.id),
    topic_ids: [...new Set(session.questions.map((question) => question.topic_id))],
    answers: session.answers,
    marked: [...session.marks],
    seen: [...session.seen],
    currentIndex: session.currentIndex,
    mode: session.mode,
    language: session.language,
    startedAt: session.startedAt,
    timerLimitSeconds: session.timerLimitSeconds,
    remainingSeconds: session.remainingSeconds,
  };
  writeLocal(STORAGE.resume, resume);
}

function updateResumePrompt() {
  const resume = readLocal(STORAGE.resume, null);
  const row = $("resumeRow");
  const button = $("resumeButton");
  if (!resume) {
    row.hidden = true;
    return;
  }
  row.hidden = false;
  const validBuild = resume.bank_build_id === state.manifest.bank_build_id;
  button.disabled = !validBuild;
  $("resumeMessage").textContent = validBuild
    ? `A saved local ${resume.mode === "timed" ? "timed" : "learn"} session has ${resume.question_ids?.length || 0} question(s).`
    : "A saved session belongs to a different bank build and cannot be resumed safely. Discard it or keep it for reference.";
}

async function resumeSession() {
  const resume = readLocal(STORAGE.resume, null);
  if (!resume || resume.bank_build_id !== state.manifest.bank_build_id) {
    showToast("This saved session does not match the current bank build.");
    return;
  }
  try {
    const data = await loadQuestions(resume.topic_ids || []);
    const byId = new Map(data.map((question) => [question.id, question]));
    const questions = (resume.question_ids || []).map((id) => byId.get(id)).filter(Boolean);
    if (questions.length !== resume.question_ids.length) throw new Error("Some saved question IDs no longer exist in this build.");
    beginSession(questions, { mode: resume.mode, language: resume.language, resumeData: resume });
  } catch (error) {
    showToast(error.message || "Could not resume this local session.");
  }
}

function getHistory() {
  const history = readLocal(STORAGE.history, []);
  return Array.isArray(history) ? history : [];
}

function getBookmarks() {
  const bookmarks = readLocal(STORAGE.bookmarks, []);
  return Array.isArray(bookmarks) ? [...new Set(bookmarks)] : [];
}

function updateLocalPanels() {
  const history = getHistory();
  const bookmarks = getBookmarks();
  $("localAttemptCount").textContent = String(history.length);
  $("localBestScore").textContent = history.length ? `${Math.max(...history.map((item) => Number(item.percent) || 0))}%` : "—";
  $("localBookmarkCount").textContent = String(bookmarks.length);
  $("bookmarkSummary").textContent = bookmarks.length ? `${bookmarks.length} question(s) saved in this browser.` : "No questions saved yet.";
  $("practiceSavedButton").disabled = !bookmarks.length || !state.manifest;
  $("clearBookmarksButton").disabled = !bookmarks.length;
  $("clearHistoryButton").disabled = !history.length;
  const list = $("historyList");
  list.replaceChildren();
  if (!history.length) {
    appendText(list, "p", "No sessions saved yet.", "muted");
  } else {
    history.slice(-5).reverse().forEach((item) => {
      const line = element("p", "muted", `${new Date(item.endedAt).toLocaleString()} · ${item.percent}% (${item.correct}/${item.total} correct) · ${item.mode === "timed" ? "Timed practice" : "Learn mode"}`);
      list.append(line);
    });
  }
}

function toggleBookmark(questionId) {
  const bookmarks = new Set(getBookmarks());
  if (bookmarks.has(questionId)) bookmarks.delete(questionId);
  else bookmarks.add(questionId);
  writeLocal(STORAGE.bookmarks, [...bookmarks]);
  updateLocalPanels();
  renderQuestion();
  showToast(bookmarks.has(questionId) ? "Question saved in this browser." : "Question removed from saved questions.");
}

async function practiceBookmarks() {
  const ids = getBookmarks();
  if (!ids.length) return;
  const topicIds = [...new Set(ids.map((id) => id.split("-")[1]).filter((topic) => state.topicById.has(topic)))];
  try {
    const data = await loadQuestions(topicIds);
    const byId = new Map(data.map((question) => [question.id, question]));
    const questions = ids.map((id) => byId.get(id)).filter(Boolean);
    if (!questions.length) {
      showToast("No saved questions match this build. You can clear the old local list.");
      return;
    }
    beginSession(questions, { mode: "learn", language: $("languageSelect").value || "both" });
  } catch (error) {
    showToast(error.message || "Could not load saved questions.");
  }
}

function saveCompletedSession(session, result) {
  const history = getHistory();
  history.push({
    endedAt: new Date().toISOString(),
    total: result.total,
    correct: result.correct,
    wrong: result.wrong,
    unanswered: result.unanswered,
    percent: result.percent,
    mode: session.mode,
    bank_build_id: state.manifest.bank_build_id,
  });
  writeLocal(STORAGE.history, history.slice(-30));
  removeLocal(STORAGE.resume);
  updateLocalPanels();
}

function renderResults(session, result) {
  const stats = $("resultStats");
  stats.replaceChildren();
  const values = [
    ["Score", `${result.correct}/${result.total}`],
    ["Correct", result.correct],
    ["Incorrect", result.wrong],
    ["Unanswered", result.unanswered],
    ["Percent correct", `${result.percent}%`],
    ["Session", session.mode === "timed" ? "Timed practice" : "Learn mode"],
  ];
  for (const [label, value] of values) {
    const stat = element("div", "result-stat");
    appendText(stat, "strong", value);
    appendText(stat, "span", label);
    stats.append(stat);
  }
  const statusSummary = Object.entries(result.verificationBreakdown)
    .map(([status, count]) => `${count} × ${verificationLabel(status)}`).join("; ");
  $("resultsIntro").textContent = `${statusSummary}. Score is correct answers divided by questions in the set; no negative marking is applied.`;
  const body = $("topicResultsTable").querySelector("tbody");
  body.replaceChildren();
  for (const [topicId, valuesForTopic] of Object.entries(result.topicBreakdown)) {
    const row = element("tr");
    appendText(row, "td", `${topicId} · ${state.topicById.get(topicId)?.topic_name || TOPIC_FALLBACK_NAMES[topicId] || "Topic"}`);
    appendText(row, "td", valuesForTopic.correct);
    appendText(row, "td", valuesForTopic.wrong);
    appendText(row, "td", valuesForTopic.unanswered);
    body.append(row);
  }
  $("retryWrongButton").disabled = !session.questions.some((question) => session.answers[question.id] != null && session.answers[question.id] !== question.answer_option_id);
  $("reviewAnswersButton").setAttribute("aria-expanded", "false");
  $("reviewList").hidden = true;
  $("reviewList").replaceChildren();
}

function finishSession({ automatic = false } = {}) {
  const session = state.session;
  if (!session || session.completed) return;
  const result = gradeAttempt(session.questions, session.answers);
  if (!automatic && result.unanswered > 0 && !window.confirm(`${result.unanswered} question(s) are unanswered. Finish the session anyway?`)) return;
  session.completed = true;
  stopTimer();
  state.lastResult = { session, result };
  saveCompletedSession(session, result);
  renderResults(session, result);
  $("playerPanel").hidden = true;
  $("resultsPanel").hidden = false;
  $("setupPanel").hidden = false;
  $("resultsPanel").scrollIntoView({ behavior: "smooth", block: "start" });
  if (automatic) showToast("Your personal timer reached zero; the practice session was submitted.");
}

function renderReviewList() {
  const saved = state.lastResult;
  if (!saved) return;
  const root = $("reviewList");
  root.replaceChildren();
  saved.session.questions.forEach((question, index) => {
    const selected = saved.session.answers[question.id];
    const correct = selected === question.answer_option_id;
    const review = element("article", "review-item");
    appendText(review, "h4", `Question ${index + 1} · ${question.id} · ${correct ? "Correct" : selected == null ? "Unanswered" : "Incorrect"}`);
    const stem = element("p");
    let fallback = renderLocalized(stem, question.stem_en, question.stem_hi, saved.session.language);
    review.append(stem);
    appendText(review, "p", `Your answer: ${answerLabel(question, selected)} · Correct answer: ${answerLabel(question, question.answer_option_id)}`);
    appendText(review, "p", `${verificationLabel(question.verification_status)} · ${sourceTypeLabel(question.source_type)}`, "field-help");
    if (question.explanation_en || question.explanation_hi) {
      appendText(review, "strong", "Explanation");
      fallback = appendLocalizedBlock(review, question.explanation_en, question.explanation_hi, saved.session.language) || fallback;
    }
    if (question.nukta_en || question.nukta_hi) {
      appendText(review, "strong", "Nukta · exam point");
      fallback = appendLocalizedBlock(review, question.nukta_en, question.nukta_hi, saved.session.language) || fallback;
    }
    if (fallback) appendText(review, "p", "Hindi wording is not supplied for one or more fields; English is shown as a fallback.", "translation-note");
    const sourceButton = element("button", "button secondary small", "Source details");
    sourceButton.type = "button";
    sourceButton.addEventListener("click", () => openSourceDialog(question.source_id));
    review.append(sourceButton);
    root.append(review);
  });
}

function sessionSummaryText() {
  if (!state.lastResult) return "No completed session is available.";
  const { session, result } = state.lastResult;
  return [
    "EkGuru Learning — local practice result",
    `Build: ${state.manifest.bank_build_id}`,
    `Mode: ${session.mode === "timed" ? "Timed practice" : "Learn mode"}`,
    `Result: ${result.correct}/${result.total} correct (${result.percent}%)`,
    `Incorrect: ${result.wrong}; unanswered: ${result.unanswered}`,
    `Scoring: correct answers only; no negative marking; not an official exam simulation.`,
  ].join("\n");
}

async function copySummary() {
  const text = sessionSummaryText();
  try {
    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(text);
      showToast("Session summary copied to clipboard.");
      return;
    }
  } catch {
    // Fall through to a user-selectable text field.
  }
  const box = element("textarea");
  box.value = text;
  box.setAttribute("aria-label", "Session summary to copy manually");
  $("resultsPanel").append(box);
  box.focus();
  box.select();
  showToast("Clipboard access is unavailable; select and copy the summary text.");
}

async function loadSourceRegister() {
  if (state.sourceRegister) return state.sourceRegister;
  if (state.sourceRegisterPromise) return state.sourceRegisterPromise;
  state.sourceRegisterPromise = fetchJSON(state.catalog.source_register_url).then((data) => {
    if (data.bank_build_id !== state.manifest.bank_build_id) throw new Error("Source register belongs to a different bank build.");
    state.sourceRegister = data;
    renderSourceRegister($("sourceSearch").value);
    return data;
  }).catch((error) => {
    state.sourceRegisterPromise = null;
    throw error;
  });
  return state.sourceRegisterPromise;
}

function safeReferenceHref(raw) {
  if (typeof raw !== "string") return null;
  try {
    const url = new URL(raw, window.location.href);
    if (!["http:", "https:"].includes(url.protocol) || url.username || url.password) return null;
    return url.href;
  } catch {
    return null;
  }
}

function renderSourceRegister(search = "") {
  const root = $("sourceRegister");
  if (!state.sourceRegister) return;
  const term = String(search).trim().toLowerCase();
  const records = (state.sourceRegister.records || []).filter((record) =>
    !term || `${record.id} ${record.reference}`.toLowerCase().includes(term));
  root.replaceChildren();
  if (!records.length) {
    root.append(element("p", "empty-state", "No source citations match this filter."));
    return;
  }
  const summary = element("p", "field-help", `Showing ${Math.min(records.length, 100)} of ${records.length} matching citation(s); search narrows the generated source register.`);
  root.append(summary);
  records.slice(0, 100).forEach((record) => {
    const item = element("article", "source-record");
    appendText(item, "h4", `${record.id} · ${record.reference}`);
    appendText(item, "p", `${record.question_count} question(s) · ${Object.entries(record.source_types || {}).filter(([, count]) => count).map(([key, count]) => `${sourceTypeLabel(key)} ${count}`).join("; ")}`);
    const statuses = Object.entries(record.verification_statuses || {}).filter(([, count]) => count).map(([key, count]) => `${verificationLabel(key)} ${count}`).join("; ");
    if (statuses) appendText(item, "p", statuses);
    if (record.audit_note) appendText(item, "p", record.audit_note);
    if (record.links?.length) {
      const links = element("div", "source-links");
      for (const link of record.links) {
        let href;
        if (link.external) href = safeReferenceHref(link.href);
        else {
          const decoded = decodeURI(link.href);
          const normalized = new URL(decoded, window.location.href);
          if (normalized.origin === window.location.origin) href = normalized.href;
        }
        if (!href) continue;
        const anchor = element("a", "", link.external ? `Open external source · ${link.label}` : `Open local file · ${link.label}`);
        anchor.href = href;
        anchor.target = "_blank";
        anchor.rel = "noopener noreferrer";
        links.append(anchor);
      }
      item.append(links);
    }
    root.append(item);
  });
}

async function openSourceDialog(sourceId) {
  if (!sourceId) {
    showToast("This question has no source-register ID.");
    return;
  }
  const content = $("sourceDialogContent");
  content.replaceChildren(element("p", "muted", "Loading citation…"));
  try {
    const register = await loadSourceRegister();
    const record = register.records.find((item) => item.id === sourceId);
    content.replaceChildren();
    if (!record) {
      content.append(element("p", "empty-state", "No public citation record was found for this source ID."));
    } else {
      appendText(content, "p", record.reference);
      appendText(content, "p", `${record.question_count} question(s) · ${Object.entries(record.source_types || {}).filter(([, count]) => count).map(([key, count]) => `${sourceTypeLabel(key)}: ${count}`).join("; ")}`);
      if (record.audit_note) appendText(content, "p", record.audit_note);
      const links = element("div", "source-links");
      for (const link of record.links || []) {
        let href;
        if (link.external) href = safeReferenceHref(link.href);
        else {
          const normalized = new URL(decodeURI(link.href), window.location.href);
          if (normalized.origin === window.location.origin) href = normalized.href;
        }
        if (!href) continue;
        const anchor = element("a", "", `Open ${link.external ? "external" : "local"} reference · ${link.label}`);
        anchor.href = href;
        anchor.target = "_blank";
        anchor.rel = "noopener noreferrer";
        links.append(anchor);
      }
      if (links.childElementCount) content.append(links);
    }
    const dialog = $("sourceDialog");
    if (typeof dialog.showModal === "function") dialog.showModal();
    else dialog.setAttribute("open", "");
  } catch (error) {
    content.replaceChildren(element("p", "error-banner", error.message || "Unable to load the source register."));
    const dialog = $("sourceDialog");
    if (typeof dialog.showModal === "function") dialog.showModal();
    else dialog.setAttribute("open", "");
  }
}

function updatePoolFiltersFromQuery() {
  const params = new URLSearchParams(window.location.search);
  const subject = params.get("subject");
  const topic = params.get("topic");
  const mode = params.get("mode");
  if (subject && state.catalog.subjects.some((item) => item.id === subject && item.available)) $("subjectSelect").value = subject;
  if (topic && state.topicById.has(topic)) $("topicSelect").value = topic;
  if (mode === "timed") $("modeTimed").checked = true;
  else if (mode === "learn" || mode === "practice") $("modeLearn").checked = true;
  $("timeLimitField").hidden = !$("modeTimed").checked;
}

function wireNavigation() {
  const button = $("navToggle");
  const nav = $("siteNav");
  const closeMenu = () => {
    nav.classList.remove("open");
    button.setAttribute("aria-expanded", "false");
  };
  button.addEventListener("click", () => {
    const open = button.getAttribute("aria-expanded") !== "true";
    button.setAttribute("aria-expanded", String(open));
    nav.classList.toggle("open", open);
  });
  nav.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeMenu();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeMenu();
  });
}

function wireSessionEvents() {
  $("subjectSelect").addEventListener("change", refreshPoolStatus);
  ["topicSelect", "examSelect", "verificationSelect", "sourceTypeSelect", "difficultySelect", "questionCountSelect"].forEach((id) => {
    $(id).addEventListener("change", refreshPoolStatus);
  });
  document.querySelectorAll('input[name="sessionMode"]').forEach((radio) => radio.addEventListener("change", () => {
    $("timeLimitField").hidden = !$("modeTimed").checked;
  }));
  $("startButton").addEventListener("click", () => startFromForm());
  $("randomButton").addEventListener("click", () => startFromForm({ randomTwenty: true }));
  $("resumeButton").addEventListener("click", resumeSession);
  $("discardResumeButton").addEventListener("click", () => {
    removeLocal(STORAGE.resume);
    updateResumePrompt();
    showToast("Saved local session discarded.");
  });
  $("optionList").addEventListener("click", (event) => {
    const button = event.target.closest("button[data-option-id]");
    if (!button || !state.session || state.session.completed) return;
    const question = state.session.questions[state.session.currentIndex];
    state.session.answers[question.id] = button.dataset.optionId;
    renderQuestion();
    saveResume();
  });
  $("previousButton").addEventListener("click", () => {
    if (!state.session || state.session.currentIndex <= 0) return;
    state.session.currentIndex -= 1;
    renderQuestion();
    saveResume();
  });
  $("nextButton").addEventListener("click", () => {
    if (!state.session) return;
    if (state.session.currentIndex < state.session.questions.length - 1) {
      state.session.currentIndex += 1;
      renderQuestion();
      saveResume();
    } else {
      showToast("You are at the last question. Finish the session when ready.");
    }
  });
  $("clearAnswerButton").addEventListener("click", () => {
    if (!state.session) return;
    const question = state.session.questions[state.session.currentIndex];
    delete state.session.answers[question.id];
    renderQuestion();
    saveResume();
  });
  $("markButton").addEventListener("click", () => {
    if (!state.session) return;
    const id = state.session.questions[state.session.currentIndex].id;
    if (state.session.marks.has(id)) state.session.marks.delete(id);
    else state.session.marks.add(id);
    renderQuestion();
    saveResume();
  });
  $("bookmarkButton").addEventListener("click", () => {
    if (!state.session) return;
    toggleBookmark(state.session.questions[state.session.currentIndex].id);
  });
  $("finishButton").addEventListener("click", () => finishSession());
  $("exitSession").addEventListener("click", () => {
    if (!state.session) return;
    const unanswered = state.session.questions.length - Object.keys(state.session.answers).length;
    if (unanswered && !window.confirm("Exit this unfinished session? Your progress will be saved locally for later.")) return;
    saveResume();
    stopTimer();
    state.session = null;
    $("playerPanel").hidden = true;
    $("setupPanel").hidden = false;
    updateResumePrompt();
    showToast("Session paused and saved in this browser.");
  });
  $("paletteToggle").addEventListener("click", () => {
    const expanded = $("paletteToggle").getAttribute("aria-expanded") !== "true";
    $("paletteToggle").setAttribute("aria-expanded", String(expanded));
    $("paletteToggle").textContent = expanded ? "Hide question list" : "Show question list";
    $("palette").hidden = !expanded;
  });
  $("sourceDetailsButton").addEventListener("click", () => openSourceDialog($("sourceDetailsButton").dataset.sourceId));
  $("closeSourceDialog").addEventListener("click", () => $("sourceDialog").close?.());
  $("sourceDialog").addEventListener("click", (event) => {
    if (event.target === $("sourceDialog")) $("sourceDialog").close?.();
  });
  $("reviewAnswersButton").addEventListener("click", () => {
    const expanded = $("reviewAnswersButton").getAttribute("aria-expanded") !== "true";
    $("reviewAnswersButton").setAttribute("aria-expanded", String(expanded));
    $("reviewAnswersButton").textContent = expanded ? "Hide answer review" : "Review answers";
    $("reviewList").hidden = !expanded;
    if (expanded) renderReviewList();
  });
  $("retryWrongButton").addEventListener("click", () => {
    if (!state.lastResult) return;
    const { session } = state.lastResult;
    const wrong = session.questions.filter((question) => session.answers[question.id] != null && session.answers[question.id] !== question.answer_option_id);
    if (!wrong.length) {
      showToast("There are no incorrect answered questions to retry.");
      return;
    }
    beginSession(wrong, { mode: "learn", language: session.language });
  });
  $("copySummaryButton").addEventListener("click", copySummary);
  $("backToSetupButton").addEventListener("click", () => {
    $("resultsPanel").hidden = true;
    $("setupPanel").hidden = false;
    $("practiceTitle").focus?.();
  });
  $("practiceSavedButton").addEventListener("click", practiceBookmarks);
  $("clearBookmarksButton").addEventListener("click", () => {
    if (!window.confirm("Clear the saved question list from this browser?")) return;
    removeLocal(STORAGE.bookmarks);
    $("bookmarkList").hidden = true;
    updateLocalPanels();
    showToast("Saved questions cleared from this browser.");
  });
  $("clearHistoryButton").addEventListener("click", () => {
    if (!window.confirm("Clear local session history from this browser?")) return;
    removeLocal(STORAGE.history);
    updateLocalPanels();
    showToast("Local session history cleared.");
  });
  $("sourceRegisterDetails").addEventListener("toggle", () => {
    if ($("sourceRegisterDetails").open) {
      loadSourceRegister().catch((error) => {
        $("sourceRegister").replaceChildren(element("p", "error-banner", error.message || "Unable to load citations."));
      });
    }
  });
  $("sourceSearch").addEventListener("input", () => renderSourceRegister($("sourceSearch").value));
}

async function init() {
  wireNavigation();
  wireSessionEvents();
  updateLocalPanels();
  try {
    state.catalog = await fetchJSON("assets/catalog.min.json");
    if (!Array.isArray(state.catalog.subjects)) throw new Error("Subject catalog is missing its subjects list.");
    state.cnSubject = state.catalog.subjects.find((subject) => subject.id === "cn");
    if (!state.cnSubject?.available) throw new Error("The CN subject is not marked as available in the generated catalog.");
    state.manifest = await fetchJSON(state.catalog.cn_bank_manifest_url);
    if (state.catalog.bank_build_id !== state.manifest.bank_build_id) throw new Error("Catalog and CN manifest belong to different data builds.");
    state.manifest.topics.forEach((topic) => state.topicById.set(topic.topic_id, topic));
    buildSelectors();
    setSummary();
    setSubjectCards();
    buildLibrary();
    renderVerificationSummary();
    updatePoolFiltersFromQuery();
    refreshPoolStatus();
    updateResumePrompt();
    updateLocalPanels();
  } catch (error) {
    console.error(error);
    $("subjectGrid").replaceChildren(element("p", "error-banner", "The generated catalog could not be loaded. Run the documented data builders and serve this repository over HTTP."));
    $("poolStatus").textContent = error.message || "Unable to load the catalog.";
    $("poolDisclosure").textContent = "This app needs generated catalog and manifest assets. The canonical question bank remains unchanged if asset loading fails.";
    $("startButton").disabled = true;
    $("randomButton").disabled = true;
    $("verificationSummary").replaceChildren(element("p", "error-banner", error.message || "Unable to load verification counts."));
  }
}

init();
