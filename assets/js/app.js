const SITE_ROOT = new URL("../../", import.meta.url);
const PATHS = Object.freeze({
  subjects: "assets/catalog/subjects.json",
  resources: "assets/catalog/resources.json",
  maps: "assets/catalog/maps.json",
  cnManifest: "assets/banks/cn/manifest.json",
});
const TOPIC_LABELS = Object.freeze({
  T01: "Introduction of Data Communication",
  T02: "Network Models: OSI & TCP/IP",
  T03: "Addressing: MAC, IPv4, IPv6, Ports, DNS",
  T04: "Networking Devices",
  T05: "Transmission Medium",
  T06: "OSI Layers in Detail",
  T07: "Network Security",
});

const cache = { subjects: null, resources: null, maps: null, cn: null };
const $ = (selector, parent = document) => parent.querySelector(selector);
const $$ = (selector, parent = document) => [...parent.querySelectorAll(selector)];

function safeSiteUrl(value) {
  if (!value) return "";
  if (/^https?:\/\//i.test(value)) return value;
  return new URL(value, SITE_ROOT).href;
}

async function loadJSON(path) {
  const url = safeSiteUrl(path);
  const response = await fetch(url, { cache: "no-cache" });
  if (!response.ok) throw new Error(`Could not load ${path} (${response.status}).`);
  return response.json();
}

function make(tag, className = "", text = null) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== null && text !== undefined) node.textContent = String(text);
  return node;
}

function resourceHref(resource) {
  return safeSiteUrl(resource.url || resource.repo_path || "");
}

function addResourceAnchor(parent, resource, label = resource.title) {
  if (!resource || resource.availability_status === "unavailable") {
    parent.append(make("span", "unavailable", "Unavailable / being checked"));
    return null;
  }
  const anchor = make("a", "", label);
  anchor.href = resourceHref(resource);
  if (resource.open_behavior === "new_tab") {
    anchor.target = "_blank";
    anchor.rel = "noopener noreferrer";
    anchor.append(document.createTextNode(` (${resource.external_open_label || "opens in new tab"})`));
  }
  parent.append(anchor);
  return anchor;
}

function setStatus(selector, message, isError = false) {
  const node = $(selector);
  if (!node) return;
  node.textContent = message;
  node.classList.toggle("error-state", isError);
  node.classList.toggle("status-line", !isError);
}

function resourceList(subjectId = null, category = null, topicId = null) {
  let items = cache.resources?.resources || [];
  if (subjectId) items = items.filter((item) => item.subject_id === subjectId || item.subject_id === "shared");
  if (topicId) items = items.filter((item) => item.topic_id === topicId);
  if (category) {
    const categories = category.split("|").map((value) => value.trim()).filter(Boolean);
    items = items.filter((item) => categories.includes(item.category));
  }
  return items.filter((item) => item.availability_status !== "unavailable");
}

function resourceCard(resource, { showCategory = false } = {}) {
  const item = make("article", "resource-item");
  if (showCategory) item.append(make("span", "resource-type", resource.category));
  const heading = make("h3");
  addResourceAnchor(heading, resource);
  item.append(heading);
  if (resource.notes) item.append(make("p", "", resource.notes));
  if (resource.source_status) {
    const warning = ["needs_verification", "warning"].includes(resource.source_status_state);
    item.append(make("span", `status-chip ${warning ? "warning" : "neutral"}`, resource.source_status_label || resource.source_status));
  }
  return item;
}

function renderResourceList(element, resources) {
  element.replaceChildren();
  const group = make("div", "resource-list");
  if (!resources.length) {
    element.append(make("p", "empty-state", "Unavailable / being checked — no matching, validated resource is published in this group."));
    return;
  }
  resources.forEach((resource) => group.append(resourceCard(resource)));
  element.append(group);
}

function renderResourceSections() {
  $$('[data-resource-list]').forEach((element) => {
    renderResourceList(element, resourceList(
      element.dataset.subject || null,
      element.dataset.category || null,
      element.dataset.topic || null,
    ));
  });
}

function renderSubjectCards() {
  const grid = $("#subjectGrid");
  if (!grid || !cache.subjects) return;
  grid.replaceChildren();
  for (const subject of cache.subjects.subjects || []) {
    const card = make("article", "card subject-card");
    const status = subject.status === "live" ? (subject.kind === "resource-library" ? "Live resources · no quiz bank" : "Live question bank") : "Planned · unavailable";
    card.append(make("span", `status-chip ${subject.status === "live" ? "" : "neutral"}`, status));
    card.append(make("span", "subject-mark", subject.id === "computer-network" ? "01" : "02"));
    card.append(make("h3", "", subject.title));
    if (subject.title_hi) card.append(make("p", "muted", subject.title_hi));
    card.append(make("p", "", subject.description));
    if (subject.status === "live" && subject.question_count !== undefined) {
      const meta = make("div", "meta-row");
      meta.append(make("span", "meta-chip", `${Number(subject.question_count).toLocaleString("en-IN")} canonical records`));
      meta.append(make("span", "meta-chip", `${Number(subject.practice_question_count || 0).toLocaleString("en-IN")} in practice payload`));
      meta.append(make("span", "meta-chip", `${subject.topic_count || 0} topics`));
      card.append(meta);
    }
    const link = make("a", "button accent", subject.status === "live" ? subject.action_label : "Unavailable");
    link.href = subject.status === "live" ? safeSiteUrl(subject.route) : "";
    if (subject.status !== "live") {
      link.removeAttribute("href");
      link.setAttribute("aria-disabled", "true");
    }
    card.append(link);
    grid.append(card);
  }
}

function renderRecentUpdates() {
  const target = $("#recentUpdates");
  if (!target) return;
  const dated = (cache.subjects?.subjects || []).filter((subject) => subject.updated_at).map((subject) => ({
    date: subject.updated_at,
    title: subject.title,
    note: subject.update_note || "Checked-in source/build metadata date.",
    route: subject.route,
  }));
  if (!dated.length) {
    target.replaceChildren(make("p", "empty-state", "No dated source/build updates are recorded in the current manifests."));
    return;
  }
  target.replaceChildren();
  const list = make("div", "resource-list");
  for (const item of dated) {
    const article = make("article", "resource-item");
    article.append(make("span", "resource-type", item.date));
    const heading = make("h3");
    const link = make("a", "", item.title);
    link.href = safeSiteUrl(item.route);
    heading.append(link);
    article.append(heading, make("p", "", item.note));
    list.append(article);
  }
  target.append(list);
}

function getResource(id) {
  return (cache.resources?.resources || []).find((item) => item.id === id);
}

function topicCounts(topic) {
  const canonical = Number(topic.record_count || topic.canonical_question_count || 0);
  const published = Number(topic.published_question_count || topic.practice_question_count || 0);
  return { canonical, published };
}

function renderTopicCards() {
  const grid = $("#topicCards");
  if (!grid || !cache.cn) return;
  grid.replaceChildren();
  const subject = (cache.subjects?.subjects || []).find((item) => item.id === "computer-network");
  for (const topic of subject?.topics || []) {
    const id = topic.id || topic.topic_id;
    const entry = cache.cn.topics.find((item) => item.topic_id === id) || topic;
    const title = topic.title || TOPIC_LABELS[id] || topic.name || id;
    const { canonical, published } = topicCounts(entry);
    const card = make("article", "topic-card");
    const heading = make("h3");
    heading.append(make("span", "topic-code", id), document.createTextNode(title));
    card.append(heading);
    const counts = make("div", "meta-row");
    counts.append(make("span", "meta-chip", `${canonical.toLocaleString("en-IN")} canonical records`));
    counts.append(make("span", "meta-chip", `${published.toLocaleString("en-IN")} available for practice`));
    card.append(counts);
    const links = make("div", "topic-resource-links");
    const current = getResource(`cn-${id.toLowerCase()}-cbt-current`);
    const topicResources = (cache.resources?.resources || []).filter((item) => item.subject_id === "computer-network" && item.topic_id === id && item.availability_status !== "unavailable");
    const practice = topicResources.filter((item) => item.category === "Practice PDF");
    const theory = topicResources.filter((item) => item.category === "Theory/Notes");
    if (current) addResourceAnchor(links, current, "Start topic CBT (shared engine; same tab)");
    else links.append(make("span", "unavailable", "Interactive CBT — Unavailable / being checked"));
    if (practice.length) practice.forEach((item) => addResourceAnchor(links, item));
    else links.append(make("span", "unavailable", "Practice PDF — Unavailable / being checked"));
    if (theory.length) theory.forEach((item) => addResourceAnchor(links, item));
    else links.append(make("span", "unavailable", "Theory/solutions — Unavailable / being checked"));
    const source = make("a", "", "Topic sources and verification policy");
    source.href = safeSiteUrl("sources/index.html#cn-source-register");
    links.append(source);
    card.append(links);
    grid.append(card);
  }
  if (!grid.children.length) grid.append(make("p", "empty-state", "No topic metadata is available. Check the source bank manifest."));
}

function renderCNBankStatus() {
  const target = $("#cnBankStatus");
  if (!target || !cache.cn) return;
  const counts = cache.cn.by_verification || {};
  const source = cache.cn.by_source_type || {};
  const summary = make("div", "callout info");
  const record = make("p");
  record.append(document.createTextNode("Canonical bank: "));
  record.append(make("strong", "", `${Number(cache.cn.question_count).toLocaleString("en-IN")} records`));
  record.append(document.createTextNode(`; ${Number(cache.cn.published_question_count).toLocaleString("en-IN")} in practice payload; ${Number(cache.cn.review_only_excluded_count).toLocaleString("en-IN")} pending/review-only records excluded. Build ${cache.cn.bank_build_id}, generated ${cache.cn.generated_on}.`));
  summary.append(record);
  const verification = make("p", "", `Answer verification: ${counts.paper_and_key_checked || 0} official paper + final-key checked; ${counts.answer_checked || 0} answer-checked (not official-key matched); ${counts.claimed_answer_unverified || 0} claimed answers unverified; ${counts.pending_review || 0} pending review.`);
  summary.append(verification);
  const sourceNote = make("p", "", `Source types include ${source.claimed_pyq_unverified || 0} claimed PYQ records (not proven official), ${source.repository_internal || 0} repository/internal, ${source.textbook_paraphrase || 0} textbook paraphrases and ${source.original_practice || 0} original practice. These are source labels, not verification labels.`);
  summary.append(sourceNote);
  target.replaceChildren(summary);
}

function renderMapHero() {
  const map = cache.maps?.maps?.find((item) => item.id === "rajasthan-border-atlas-preview");
  if (!map) return;
  const image = $("#mapPreviewImage");
  if (image) {
    image.src = safeSiteUrl(map.preview_image_url);
    image.alt = map.image_alt;
  }
  const full = $("#fullSizeMapLink");
  if (full) {
    full.href = safeSiteUrl(map.full_size_url);
    full.textContent = "Open full-size A1 PNG";
    if (map.image_open_behavior === "new_tab") {
      full.target = "_blank";
      full.rel = "noopener noreferrer";
      full.append(document.createTextNode(` (${map.external_open_label || "opens in new tab"})`));
    } else {
      full.removeAttribute("target");
      full.removeAttribute("rel");
    }
  }
  const status = $("#mapReviewStatus");
  if (status) status.textContent = map.source_status_label;
  const note = $("#mapImageCaption");
  if (note) note.textContent = map.caption;
}

function renderMapCards() {
  const grid = $("#mapGrid");
  if (!grid || !cache.maps) return;
  grid.replaceChildren();
  for (const map of cache.maps.maps.filter((item) => item.display_in_gallery)) {
    const card = make("article", "map-card");
    const figure = make("figure");
    const imageLink = make("a");
    imageLink.href = safeSiteUrl(map.detail_route || "maps/rajasthan/index.html");
    imageLink.setAttribute("aria-label", `${map.title}; open map details`);
    const image = document.createElement("img");
    image.src = safeSiteUrl(map.preview_image_url || map.original_url);
    image.alt = map.image_alt;
    image.loading = "lazy";
    imageLink.append(image);
    figure.append(imageLink);
    card.append(figure, make("h3", "", map.title), make("p", "", map.caption));
    card.append(make("span", `status-chip ${map.review_status === "needs_verification" ? "warning" : "neutral"} map-status`, map.source_status_label));
    const actions = make("div", "card-actions");
    if (map.full_size_url) addResourceAnchor(actions, {
      url: map.full_size_url,
      open_behavior: map.image_open_behavior || "same_tab",
      external_open_label: map.external_open_label,
      title: "Open full-size image",
    }, "Open full-size image");
    if (map.detail_route) {
      const link = make("a", "button secondary small", "Map details and data");
      link.href = safeSiteUrl(map.detail_route);
      actions.append(link);
    }
    card.append(actions);
    grid.append(card);
  }
}

function renderMapFiles() {
  const target = $("#mapFiles");
  if (!target || !cache.maps) return;
  const resources = resourceList("rajasthan-geography", "Map/Atlas");
  renderResourceList(target, resources);
}

function renderBoundaryData() {
  const summaryNode = $("#boundarySummary");
  const districtsNode = $("#borderDistrictGroups");
  if (!cache.maps) return;
  if (summaryNode) {
    summaryNode.replaceChildren();
    const tableWrap = make("div", "table-scroll");
    tableWrap.setAttribute("role", "region");
    tableWrap.setAttribute("tabindex", "0");
    tableWrap.setAttribute("aria-label", "Horizontally scrollable summary of border-district CSV data");
    const table = document.createElement("table");
    const head = document.createElement("thead");
    const row = document.createElement("tr");
    ["Neighbour / province", "Districts listed in CSV", "Review status"].forEach((label) => row.append(make("th", "", label)));
    head.append(row);
    table.append(head);
    const body = document.createElement("tbody");
    for (const item of cache.maps.border_summary || []) {
      const tr = document.createElement("tr");
      tr.append(make("td", "", item.neighbour_state_province));
      tr.append(make("td", "", String(item.districts_touching)));
      tr.append(make("td", "", "Needs verification"));
      body.append(tr);
    }
    table.append(body);
    tableWrap.append(table);
    summaryNode.append(tableWrap);
  }
  if (districtsNode) {
    districtsNode.replaceChildren();
    for (const group of cache.maps.border_groups || []) {
      const details = make("details", "disclosure");
      const summary = make("summary", "", `${group.neighbour_state_province} — ${group.districts.length} names in checked-in CSV`);
      details.append(summary);
      const list = make("ul");
      for (const district of group.districts) {
        const item = make("li", "", district.district_en);
        if (district.district_hi) item.append(document.createTextNode(` — ${district.district_hi}`));
        list.append(item);
      }
      details.append(list);
      districtsNode.append(details);
    }
  }
}

function renderExternalSources() {
  const target = $("#officialSourceLinks");
  if (!target) return;
  target.replaceChildren();
  const sources = cache.maps?.official_sources || [];
  if (!sources.length) {
    target.append(make("p", "empty-state", "No external source links are included in the current map manifest."));
    return;
  }
  const list = make("ul");
  for (const source of sources) {
    const li = make("li");
    const anchor = make("a", "", source.title);
    anchor.href = source.url;
    if (source.open_behavior === "new_tab") {
      anchor.target = "_blank";
      anchor.rel = "noopener noreferrer";
      li.append(anchor, document.createTextNode(` (${source.external_open_label || "opens in new tab"})`));
    } else {
      li.append(anchor);
    }
    li.append(make("span", "muted", ` — ${source.note}`));
    list.append(li);
  }
  target.append(list);
}

function initMenu() {
  // Native details/summary navigation remains usable when JavaScript is unavailable.
  $$('details.site-menu').forEach((menu) => {
    menu.addEventListener("click", (event) => {
      if (event.target.closest("a")) menu.open = false;
    });
    menu.addEventListener("keydown", (event) => {
      if (event.key === "Escape") menu.open = false;
    });
  });
}

async function boot() {
  initMenu();
  const page = document.body.dataset.page || "";
  try {
    const [subjects, resources, maps] = await Promise.all([
      loadJSON(PATHS.subjects),
      loadJSON(PATHS.resources),
      loadJSON(PATHS.maps),
    ]);
    cache.subjects = subjects;
    cache.resources = resources;
    cache.maps = maps;

    if (page === "home" || page === "subjects") {
      renderSubjectCards();
      renderRecentUpdates();
      setStatus("#catalogStatus", "Subject and resource catalog loaded from checked-in, path-validated manifests.");
    }
    if (["computer-network", "rajasthan-geography", "maps", "map-detail", "study-material", "sources"].includes(page)) {
      renderResourceSections();
    }
    if (page === "computer-network") {
      cache.cn = await loadJSON(PATHS.cnManifest);
      renderCNBankStatus();
      renderTopicCards();
      setStatus("#cnCatalogStatus", "All displayed resources are linked from the validated catalogue.");
    }
    if (page === "rajasthan-geography") {
      setStatus("#geographyCatalogStatus", "Geography resources and CSV-derived values loaded; source and boundary claims still need verification.");
    }
    if (page === "maps") {
      setStatus("#mapCatalogStatus", "Map previews and resource metadata loaded from the checked-in catalogue.");
    }
    if (page === "study-material") {
      setStatus("#studyCatalogStatus", "Study material loaded from the checked-in, path-validated catalogue.");
    }
    if (page === "sources") {
      setStatus("#sourcesCatalogStatus", "Source registers and verification files loaded from the checked-in catalogue.");
    }
    if (page === "rajasthan-geography" || page === "maps" || page === "map-detail" || page === "home") {
      renderMapHero();
      renderMapCards();
      renderMapFiles();
      renderBoundaryData();
      renderExternalSources();
    }
  } catch (error) {
    console.error(error);
    const message = `Catalogue data could not be loaded: ${error.message} Static links and map previews remain available below.`;
    ["#catalogStatus", "#cnCatalogStatus", "#mapCatalogStatus", "#geographyCatalogStatus", "#studyCatalogStatus", "#sourcesCatalogStatus"].forEach((selector) => setStatus(selector, message, true));
    $$('[data-resource-list]').forEach((element) => {
      if (!element.children.length) element.append(make("p", "error-state", "Unavailable / being checked — catalogue loading failed. Use the static fallback links on this page."));
    });
  }
}

boot();
