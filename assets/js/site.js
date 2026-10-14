/* EkGuru Learning — page renderer.
 *
 * Every page carries <body data-root="..."> so the same file works from any folder
 * depth under the GitHub Pages project path. All content comes from data/site.json,
 * which is generated from the folders in `content/`.
 *
 * The website shows the real folder tree of `content/`:
 *   subject -> folder -> subfolder -> files
 * A new PDF in `content/reasoning/practice/` appears inside "Reasoning > Practice
 * questions"; a new year folder such as `content/previous-year-papers/dsssb/2019/`
 * becomes its own tile. No page code changes when material is added.
 *
 * Hooks used by the pages (all optional):
 *   [data-nav]              main navigation, built from the subjects
 *   [data-footer-subjects]  footer subject list
 *   #subjectCards           home: one card per subject with its folder tiles
 *   #subjectExplorer        subjects/index.html: subject list, or one subject (`?subject=`)
 *   #subjectFolders         subject page: folder tiles for `data-subject`
 *   #topicGrid              subject page: topic cards for `data-subject` (needs a test bank)
 *   [data-browser-subject]  folder browser page (breadcrumbs + folder/file list)
 */
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
      .then(function (data) { cache = data; return data; });
  }

  function number(value) { return Number(value || 0).toLocaleString("en-IN"); }
  function plural(count, one, many) { return count + " " + (count === 1 ? one : many); }

  function subjectOf(data, id) {
    return (data.subjects || []).filter(function (subject) { return subject.id === id; })[0];
  }

  function fileHref(item) { return root + item.url; }
  function previewHref(item) { return root + (item.thumb_url || item.url); }
  function isImage(item) { return ["PNG", "JPG", "JPEG", "WEBP", "SVG"].indexOf(item.file_type) >= 0; }

  /* Links that stay honest whether the target is a dedicated page or the explorer. */
  function pageHref(page, params) {
    var url = root + page;
    var query = Object.keys(params || {})
      .filter(function (key) { return params[key]; })
      .map(function (key) { return key + "=" + encodeURIComponent(params[key]); })
      .join("&");
    return query ? url + (url.indexOf("?") >= 0 ? "&" : "?") + query : url;
  }

  function exploreHref(subject, folder) {
    return pageHref("subjects/index.html", { subject: subject.slug, folder: folder || "" });
  }

  function folderHref(subject, path) {
    if (subject.id === "computer-network" || subject.id === "rajasthan-geography") {
      // these two have their own pretty page
      var base = root + (subject.material_route || subject.route);
      return path ? base + "?folder=" + encodeURIComponent(path) : base;
    }
    return exploreHref(subject, path);
  }

  /* ------------------------------------------------------------ folders ---- */
  function findNode(node, path) {
    if ((node.path || "") === (path || "")) return node;
    for (var index = 0; index < node.folders.length; index += 1) {
      var found = findNode(node.folders[index], path);
      if (found) return found;
    }
    return null;
  }

  function folderMeta(folder) {
    var bits = [];
    if (folder.file_count) bits.push(plural(folder.file_count, "file", "files"));
    if (folder.folder_count) bits.push(plural(folder.folder_count, "subfolder", "subfolders"));
    if (folder.file_types.length) bits.push(folder.file_types.join(" / "));
    return bits.join(" · ");
  }

  function folderTile(subject, folder, compact) {
    var tile = el("a", "folder-card" + (compact ? " compact" : "") + (folder.empty ? " is-empty" : ""));
    var key = subject.id === "computer-network" || subject.id === "rajasthan-geography"
      ? encodeURIComponent(folder.path)
      : folder.path;
    tile.href = folderHref(subject, key);
    tile.innerHTML =
      '<span class="folder-icon" aria-hidden="true">' + esc(folder.icon) + "</span>" +
      '<span class="folder-body">' +
        "<strong>" + esc(folder.title_en) + "</strong>" +
        '<span class="folder-hi">' + esc(folder.title_hi) + "</span>" +
        (compact || !folder.note_en ? "" : '<span class="folder-note">' + esc(folder.note_en) + "</span>") +
        '<span class="folder-meta">' + esc(folderMeta(folder) || "Khali folder — file daalte hi dikh jayega") + "</span>" +
      "</span>" +
      (compact ? "" : '<span class="folder-open">' + (folder.empty ? "Khali" : "Kholo →") + "</span>");
    return tile;
  }

  function folderGrid(subject, node, compact) {
    var grid = el("div", "folder-grid");
    node.folders.forEach(function (folder) { grid.appendChild(folderTile(subject, folder, compact)); });
    return grid;
  }

  /* -------------------------------------------------------------- files ---- */
  function fileRow(item) {
    var row = el("li", "material-item" + (isImage(item) ? " is-image" : ""));
    var topicChip = item.topic_id ? '<span class="chip neutral">' + esc(item.topic_id) + "</span>" : "";
    var thumb = isImage(item)
      ? '<a class="file-thumb" href="' + esc(fileHref(item)) + '" target="_blank" rel="noopener noreferrer">' +
        '<img src="' + esc(previewHref(item)) + '" alt="' + esc(item.alt_en || item.title_en) + '" loading="lazy" decoding="async">' +
        '<span class="file-thumb-open">Poora dekho</span></a>'
      : "";
    var description = isImage(item) && item.description_en
      ? '<p class="file-description" lang="en">' + esc(item.description_en) + "</p>" +
        (item.description_hi ? '<p class="file-description" lang="hi">' + esc(item.description_hi) + "</p>" : "")
      : "";
    row.innerHTML =
      thumb +
      '<div class="material-main">' +
        "<h4>" + esc(item.title_en) + "</h4>" +
        '<p class="muted small" style="margin:0">' + esc(item.title_hi) + "</p>" +
        (item.note_en ? '<p class="small" style="margin:0.2rem 0 0">' + esc(item.note_en) + "</p>" : "") +
        description +
        '<div class="material-meta">' + topicChip +
          '<span class="chip neutral">' + esc(item.file_type) + "</span>" +
          '<span class="chip neutral">' + esc(item.size_label) + "</span>" +
        "</div>" +
      "</div>" +
      '<div class="material-actions">' +
        '<a class="button secondary small" href="' + esc(fileHref(item)) + '" target="_blank" rel="noopener noreferrer">' +
          (isImage(item) ? "Poora dekho ↗" : "PDF kholo ↗") + "</a>" +
        '<a class="button primary small" href="' + esc(fileHref(item)) + '" download>Download</a>' +
      "</div>";
    return row;
  }

  function renderFiles(mount, files) {
    if (!files.length) {
      mount.appendChild(el("p", "empty-state", "Is folder me abhi koi file nahi hai. PDF yahan daal do — page khud update ho jayega."));
      return;
    }
    var list = el("ul", "material-list");
    files.forEach(function (item) { list.appendChild(fileRow(item)); });
    mount.appendChild(list);
  }

  /* --------------------------------------------------------- breadcrumbs --- */
  function renderCrumbs(mount, subject, node, label) {
    var parts = (node.path || "").split("/").filter(Boolean);
    var html = '<a href="' + esc(folderHref(subject, "")) + '">' + esc(label || "Saare folders") + "</a>";
    var walked = "";
    parts.forEach(function (part, index) {
      walked = walked ? walked + "/" + part : part;
      var child = findNode(subject.tree, walked);
      var name = child ? child.title_en : part;
      html += '<span class="crumb-sep" aria-hidden="true">›</span>';
      html += index === parts.length - 1
        ? '<span class="crumb-current">' + esc(name) + "</span>"
        : '<a href="' + esc(folderHref(subject, walked)) + '">' + esc(name) + "</a>";
    });
    mount.innerHTML = html;
  }

  /* ------------------------------------------------- folder page browser -- */
  function renderBrowser(subject, folderPath, label) {
    var crumbs = document.getElementById("folderCrumbs");
    var mount = document.getElementById("folderBrowser");
    if (!mount) return;
    var node = findNode(subject.tree, folderPath || "") || subject.tree;
    mount.innerHTML = "";
    if (crumbs) renderCrumbs(crumbs, subject, node, label);

    var head = el("div", "folder-head");
    head.innerHTML =
      '<h2 style="margin:0">' + esc(node.icon || "📁") + " " + esc(node.title_en) + "</h2>" +
      '<p class="muted" style="margin:0">' + esc(node.title_hi) + (node.note_en ? " — " + esc(node.note_en) : "") + "</p>";
    mount.appendChild(head);

    if (node.folders.length) mount.appendChild(folderGrid(subject, node, false));
    if (node.files.length) renderFiles(mount, node.files);
    if (!node.folders.length && !node.files.length) {
      mount.appendChild(el("p", "empty-state", "Ye folder abhi khali hai. File daalte hi yahin dikh jayegi."));
    }
  }

  /* ----------------------------------------------------------- topic grid -- */
  function renderTopicGrid(container, subject) {
    container.innerHTML = "";
    subject.topics.forEach(function (topic) {
      var card = el("article", "card topic-card");
      var sectionChips = topic.sections.slice(0, 3).map(function (section) {
        return '<span class="chip neutral">' + esc(section.short) + " · " + section.count + "</span>";
      }).join("");
      var more = topic.sections.length > 3
        ? '<span class="chip neutral">+' + (topic.sections.length - 3) + " more</span>"
        : "";
      var theory = (topic.material && topic.material.theory && topic.material.theory[0]) || null;
      card.innerHTML =
        '<div class="topic-head">' +
          '<span class="topic-badge">' + esc(topic.id) + "</span>" +
          '<div><h3 style="margin:0">' + esc(topic.title_en) + "</h3>" +
          '<p class="muted small" style="margin:0">' + esc(topic.title_hi) + "</p></div>" +
        "</div>" +
        '<div class="topic-meta">' +
          '<span class="chip green">' + number(topic.question_count) + " online questions</span>" +
          '<span class="chip neutral">' + topic.section_count + " sections</span>" +
        "</div>" +
        '<div class="topic-meta">' + sectionChips + more + "</div>" +
        '<div class="topic-actions">' +
          '<a class="button primary small" href="' + root + "subjects/computer-network/test/index.html?topic=" + esc(topic.id) + '">Test do</a>' +
          (theory ? '<a class="button secondary small" href="' + esc(fileHref(theory)) + '" download>Theory PDF</a>' : "") +
        "</div>";
      container.appendChild(card);
    });
  }

  /* --------------------------------------------------------- subject card -- */
  function subjectCard(subject) {
    var card = el("article", "card subject-card");
    card.setAttribute("data-subject-card", subject.id);
    var stats = [];
    stats.push(plural(subject.folder_count, "folder", "folders"));
    stats.push(plural(subject.file_count, "file", "files"));
    if (subject.test) stats.push(number(subject.test.question_count) + " online questions");
    var actions =
      '<a class="button primary" href="' + esc(root + subject.route) + '">Folder kholo</a>' +
      (subject.test_route
        ? '<a class="button secondary" href="' + esc(root + subject.test_route) + '">Test do</a>'
        : "");
    card.innerHTML =
      '<div class="card-title-row">' +
        "<h3 style=\"margin:0\">" + esc(subject.title_en) + "</h3>" +
        '<span class="chip neutral">' + esc(subject.title_hi) + "</span>" +
      "</div>" +
      '<p class="muted small" style="margin:0.3rem 0 0.7rem">' + esc(stats.join(" · ")) + "</p>" +
      (subject.tagline_en ? '<p class="small" style="margin:0 0 0.7rem">' + esc(subject.tagline_en) + "</p>" : "");
    if (subject.tree.folders.length) card.appendChild(folderGrid(subject, subject.tree, true));
    var buttons = el("div", "button-row", actions);
    buttons.style.marginTop = "0.9rem";
    card.appendChild(buttons);
    return card;
  }

  /* ---------------------------------------------------------- explorer ----- */
  function renderExplorer(data, mount) {
    var params = new URLSearchParams(window.location.search);
    var wanted = params.get("subject");
    mount.innerHTML = "";
    if (!wanted) {
      var grid = el("div", "subject-grid");
      data.subjects.forEach(function (subject) { grid.appendChild(subjectCard(subject)); });
      mount.appendChild(grid);
      return;
    }
    var subject = subjectOf(data, wanted) || data.subjects.filter(function (item) { return item.slug === wanted; })[0];
    if (!subject) {
      mount.appendChild(el("p", "empty-state", "Ye subject nahi mila. All subjects page kholo."));
      return;
    }
    document.title = subject.title_en + " — EkGuru Learning";
    var heading = document.getElementById("explorerTitle");
    if (heading) {
      heading.textContent = subject.title_en;
      var subtitle = document.getElementById("explorerSubtitle");
      if (subtitle) subtitle.textContent = subject.title_hi + " · " + subject.tagline_hi;
    }
    var head = el("div", "folder-head");
    head.innerHTML = '<p class="muted" style="margin:0">' + esc(subject.intro_en || subject.tagline_en || "") + "</p>";
    mount.appendChild(head);
    var node = findNode(subject.tree, params.get("folder") || "") || subject.tree;
    var crumbs = el("nav", "crumbs");
    crumbs.setAttribute("aria-label", "Folder path");
    mount.appendChild(crumbs);
    renderCrumbs(crumbs, subject, node, "Saare folders");
    var browser = el("div", "folder-browser");
    mount.appendChild(browser);
    if (node.folders.length) browser.appendChild(folderGrid(subject, node, false));
    if (node.files.length) renderFiles(browser, node.files);
    if (subject.topics.length) {
      var topicBlock = el("section", "section");
      topicBlock.appendChild(el("h2", null, "Topic-wise test"));
      var topics = el("div", "topic-grid");
      topicBlock.appendChild(topics);
      mount.appendChild(topicBlock);
      renderTopicGrid(topics, subject);
    }
  }

  /* ---------------------------------------------------------- nav/footer --- */
  function renderNav(data) {
    document.querySelectorAll("[data-nav]").forEach(function (nav) {
      var current = window.location.pathname;
      var html = '<a href="' + root + 'index.html">Home</a>' +
        '<a href="' + root + 'subjects/index.html">All Subjects</a>';
      data.subjects.forEach(function (subject) {
        var href = root + subject.route;
        var active = current.indexOf("/" + subject.slug + "/") >= 0;
        html += '<a href="' + esc(href) + '"' + (active ? ' aria-current="page"' : "") + ">" + esc(subject.title_en) + "</a>";
      });
      nav.innerHTML = html;
    });
  }

  function renderFooter(data) {
    var total = data.subjects.reduce(function (sum, subject) { return sum + subject.file_count; }, 0);
    document.querySelectorAll("[data-footer-subjects]").forEach(function (node) {
      node.innerHTML = data.subjects.map(function (subject) {
        var label = subject.title_en + (subject.file_count ? " (" + subject.file_count + ")" : "");
        return '<p><a href="' + esc(root + subject.route) + '">' + esc(label) + "</a></p>";
      }).join("");
    });
    document.querySelectorAll("[data-footer-stats]").forEach(function (node) {
      node.textContent = data.subjects.length + " subjects · " + total + " files · " + number(
        (subjectOf(data, "computer-network") || { test: { question_count: 0 } }).test
          ? subjectOf(data, "computer-network").test.question_count : 0
      ) + " online questions";
    });
    document.querySelectorAll("[data-build]").forEach(function (node) {
      node.textContent = data.bank_build_id || "";
    });
  }

  /* --------------------------------------------------------------- misc ---- */
  function setText(selector, value) {
    document.querySelectorAll(selector).forEach(function (node) { node.textContent = value; });
  }

  function init() {
    loadSite().then(function (data) {
      var cn = subjectOf(data, "computer-network");
      var downloads = data.subjects.reduce(function (total, subject) { return total + subject.file_count; }, 0);

      setText("[data-count='subjects']", data.subjects.length);
      setText("[data-count='topics']", cn && cn.test ? cn.test.topic_count : 0);
      setText("[data-count='questions']", cn && cn.test ? number(cn.test.question_count) : "0");
      setText("[data-count='downloads']", number(downloads));

      renderNav(data);
      renderFooter(data);

      var homeCards = document.getElementById("subjectCards");
      if (homeCards) {
        homeCards.innerHTML = "";
        data.subjects.forEach(function (subject) { homeCards.appendChild(subjectCard(subject)); });
      }

      var explorer = document.getElementById("subjectExplorer");
      if (explorer) renderExplorer(data, explorer);

      var subjectFolders = document.getElementById("subjectFolders");
      var pageSubject = subjectOf(data, document.body.getAttribute("data-subject")) || cn;
      if (subjectFolders && pageSubject) {
        subjectFolders.innerHTML = "";
        subjectFolders.appendChild(folderGrid(pageSubject, pageSubject.tree, false));
      }

      var topicGrid = document.getElementById("topicGrid");
      if (topicGrid && pageSubject && pageSubject.topics.length) renderTopicGrid(topicGrid, pageSubject);
      else if (topicGrid) {
        topicGrid.innerHTML = '<p class="empty-state">Is subject ka online test abhi ban raha hai — tab tak material folders dekho.</p>';
      }

      var geoPath = document.getElementById("geoFolderPath");
      if (geoPath) {
        var geo = subjectOf(data, "rajasthan-geography");
        if (geo) {
          var chain = [];
          (function descend(node) {
            node.folders.forEach(function (folder) { chain.push(folder.title_en); descend(folder); });
          })(geo.tree);
          geoPath.textContent = chain.join(" › ");
        }
      }

      var browserSubject = document.body.getAttribute("data-browser-subject");
      if (browserSubject) {
        var subject = subjectOf(data, browserSubject);
        if (subject) {
          var params = new URLSearchParams(window.location.search);
          renderBrowser(subject, params.get("folder") || "", document.body.getAttribute("data-browser-label"));
        }
      }
    }).catch(function (error) {
      document.querySelectorAll("[data-loading]").forEach(function (node) {
        node.textContent = "List load nahi ho payi. Page refresh karein. (" + error.message + ")";
      });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
