/* EkGuru Learning — page renderer.
   Every page carries <body data-root="..."> so the same file works from any folder
   depth under the GitHub Pages project path. All content comes from data/site.json. */
(function () {
  "use strict";

  var root = document.body.getAttribute("data-root") || "";
  var siteUrl = new URL(root + "data/site.json", window.location.href).href;
  var cache = null;

  function esc(value) {
    return String(value == null ? "" : value).replace(/[&<>"']/g, function (char) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[char];
    });
  }

  function el(tag, className, html) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (html != null) node.innerHTML = html;
    return node;
  }

  function loadSite() {
    if (cache) return Promise.resolve(cache);
    return fetch(siteUrl, { cache: "no-cache" })
      .then(function (response) {
        if (!response.ok) throw new Error("site data " + response.status);
        return response.json();
      })
      .then(function (data) {
        cache = data;
        return data;
      });
  }

  function subjectOf(data, id) {
    return (data.subjects || []).filter(function (subject) { return subject.id === id; })[0];
  }

  function number(value) {
    return Number(value || 0).toLocaleString("en-IN");
  }

  function topicLabel(topic) {
    return topic.id + " · " + topic.title_en;
  }

  function materialHref(item) {
    return root + item.url;
  }

  function materialRow(item, options) {
    var opts = options || {};
    var topicChip = item.topic_id ? '<span class="chip neutral">' + esc(item.topic_id) + "</span>" : "";
    var row = el("li", "material-item");
    row.innerHTML =
      '<div class="material-main">' +
        "<h4>" + esc(item.title_en) + "</h4>" +
        '<p class="muted small" style="margin:0">' + esc(item.title_hi) + "</p>" +
        (item.note_en ? '<p class="small" style="margin:0.25rem 0 0">' + esc(item.note_en) + "</p>" : "") +
        '<div class="material-meta">' + topicChip +
          '<span class="chip neutral">' + esc(item.file_type) + "</span>" +
          '<span class="chip neutral">' + esc(item.size_label) + "</span>" +
        "</div>" +
      "</div>" +
      '<div class="material-actions">' +
        '<a class="button secondary small" href="' + esc(materialHref(item)) + '" target="_blank" rel="noopener noreferrer">Open PDF ↗</a>' +
        '<a class="button primary small" href="' + esc(materialHref(item)) + '" download>Download</a>' +
      "</div>";
    if (opts.hideTopic) row.querySelector(".chip.neutral").remove();
    return row;
  }

  function renderTopicGrid(container, subject) {
    container.innerHTML = "";
    subject.topics.forEach(function (topic) {
      var card = el("article", "card topic-card");
      var sectionChips = topic.sections.slice(0, 4).map(function (section) {
        return '<span class="chip neutral">' + esc(section.short) + " · " + section.count + "</span>";
      }).join("");
      var more = topic.sections.length > 4
        ? '<span class="chip neutral">+' + (topic.sections.length - 4) + " more</span>"
        : "";
      card.innerHTML =
        '<div class="topic-head">' +
          '<span class="topic-badge">' + esc(topic.id) + "</span>" +
          "<div><h3 style=\"margin:0\">" + esc(topic.title_en) + "</h3>" +
          '<p class="muted small" style="margin:0">' + esc(topic.title_hi) + "</p></div>" +
        "</div>" +
        '<div class="topic-meta">' +
          '<span class="chip green">' + number(topic.question_count) + " online questions</span>" +
          '<span class="chip neutral">' + topic.section_count + " sections</span>" +
        "</div>" +
        '<div class="topic-meta">' + sectionChips + more + "</div>" +
        '<div class="topic-actions">' +
          '<a class="button primary small" href="' + root + "subjects/computer-network/test/index.html?topic=" + esc(topic.id) + '">Start topic test</a>' +
          (topic.material.theory[0]
            ? '<a class="button secondary small" href="' + esc(materialHref(topic.material.theory[0])) + '" download>Theory PDF (' + esc(topic.material.theory[0].size_label) + ")</a>"
            : "") +
          (topic.material.practice[0]
            ? '<a class="button secondary small" href="' + esc(materialHref(topic.material.practice[0])) + '" download>Practice PDF</a>'
            : "") +
        "</div>";
      container.appendChild(card);
    });
  }

  function renderMaterialGroups(container, subject, filterTopic) {
    container.innerHTML = "";
    subject.groups.forEach(function (group) {
      var items = group.items.filter(function (item) {
        return !filterTopic || filterTopic === "all" || item.topic_id === filterTopic;
      });
      if (!items.length) return;
      var block = el("section", "card");
      block.innerHTML = '<div class="section-head"><h2 style="margin:0;font-size:1.25rem">' + esc(group.title_en) +
        '</h2><span class="muted small">' + esc(group.title_hi) + "</span></div>";
      var list = el("ul", "material-list");
      items.forEach(function (item) { list.appendChild(materialRow(item)); });
      block.appendChild(list);
      container.appendChild(block);
    });
    if (!container.children.length) {
      container.appendChild(el("p", "empty-state", "Is topic/section ke liye koi file registered nahi hai."));
    }
  }

  function renderFilters(container, subject, active) {
    var topics = [{ id: "all", title_en: "All files" }].concat(
      subject.topics.map(function (topic) { return { id: topic.id, title_en: topic.id + " " + topic.title_en }; })
    );
    container.innerHTML = "";
    topics.forEach(function (topic) {
      var button = el("button", "chip", esc(topic.title_en));
      button.type = "button";
      button.setAttribute("aria-pressed", String(active === topic.id));
      button.addEventListener("click", function () {
        renderFilters(container, subject, topic.id);
        renderMaterialGroups(document.getElementById("materialGroups"), subject, topic.id);
        if (history.replaceState) {
          var url = new URL(window.location.href);
          if (topic.id === "all") url.searchParams.delete("topic");
          else url.searchParams.set("topic", topic.id);
          history.replaceState({}, "", url);
        }
      });
      container.appendChild(button);
    });
  }

  function renderMapGrid(container, subject) {
    var maps = subject.groups.reduce(function (all, group) { return all.concat(group.items); }, []);
    container.innerHTML = "";
    maps.forEach(function (item) {
      var card = el("article", "card");
      card.innerHTML =
        "<h3>" + esc(item.title_en) + "</h3>" +
        '<p class="muted small" style="margin-top:-0.3rem">' + esc(item.title_hi) + "</p>" +
        "<p>" + esc(item.note_en) + "</p>" +
        '<div class="material-meta"><span class="chip neutral">' + esc(item.file_type) + "</span>" +
        '<span class="chip neutral">' + esc(item.size_label) + "</span>" +
        '<span class="chip neutral">' + esc(item.file_name) + "</span></div>" +
        '<div class="material-actions" style="margin-top:0.7rem">' +
          '<a class="button secondary small" href="' + esc(materialHref(item)) + '" target="_blank" rel="noopener noreferrer">View full size ↗</a>' +
          '<a class="button primary small" href="' + esc(materialHref(item)) + '" download>Download</a>' +
        "</div>";
      container.appendChild(card);
    });
  }

  function setText(selector, value) {
    document.querySelectorAll(selector).forEach(function (node) { node.textContent = value; });
  }

  function init() {
    loadSite().then(function (data) {
      var cn = subjectOf(data, "computer-network");
      var geo = subjectOf(data, "rajasthan-geography");
      var downloads = data.subjects.reduce(function (total, subject) { return total + subject.file_count; }, 0);

      setText("[data-count='topics']", cn && cn.test ? cn.test.topic_count : 7);
      setText("[data-count='questions']", cn && cn.test ? number(cn.test.question_count) : "1,554");
      setText("[data-count='downloads']", number(downloads));
      setText("[data-count='maps']", geo ? geo.file_count : 6);
      setText("[data-build]", data.bank_build_id || "");

      document.querySelectorAll("[data-subject-card]").forEach(function (card) {
        var subject = subjectOf(data, card.getAttribute("data-subject-card"));
        if (!subject) return;
        card.querySelectorAll("[data-count='subject-files']").forEach(function (node) { node.textContent = subject.file_count; });
        if (subject.test) {
          card.querySelectorAll("[data-count='subject-questions']").forEach(function (node) {
            node.textContent = number(subject.test.question_count);
          });
        }
      });

      var topicGrid = document.getElementById("topicGrid");
      if (topicGrid && cn) renderTopicGrid(topicGrid, cn);

      var materialGroups = document.getElementById("materialGroups");
      if (materialGroups && cn) {
        var params = new URLSearchParams(window.location.search);
        var initial = params.get("topic") || "all";
        renderFilters(document.getElementById("materialFilters"), cn, initial);
        renderMaterialGroups(materialGroups, cn, initial);
      }

      var mapGrid = document.getElementById("mapGrid");
      if (mapGrid && geo) renderMapGrid(mapGrid, geo);

      var plainLists = document.querySelectorAll("[data-material-group]");
      plainLists.forEach(function (list) {
        var subject = subjectOf(data, list.getAttribute("data-subject"));
        var kind = list.getAttribute("data-material-group");
        if (!subject) return;
        var group = subject.groups.filter(function (item) { return item.id === kind; })[0];
        if (!group) return;
        var wrapper = el("ul", "material-list");
        group.items.forEach(function (item) { wrapper.appendChild(materialRow(item)); });
        list.appendChild(wrapper);
      });
    }).catch(function (error) {
      document.querySelectorAll("[data-loading]").forEach(function (node) {
        node.textContent = "List load nahi ho payi. Page refresh karein. (" + error.message + ")";
      });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
