/* EkGuru Learning — page renderer.
 *
 * Every page carries <body data-root="..."> so the same file works from any folder
 * depth under the GitHub Pages project path. All content comes from data/site.json.
 *
 * The website shows the real folder tree of `content/`:
 *   subject -> folder -> subfolder -> files
 * So a new PDF in `content/computer-network/theory/` appears inside the "Theory"
 * folder, and a new map tree in `content/rajasthan-geography/map/<name>/` becomes
 * its own subfolder on the page.
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

  function subjectOf(data, id) {
    return (data.subjects || []).filter(function (subject) { return subject.id === id; })[0];
  }

  function fileHref(item) { return root + item.url; }
  /* Previews point at data/thumbs/... so a folder of 3 MB maps still opens fast. */
  function previewHref(item) { return root + (item.thumb_url || item.url); }
  function isImage(item) { return ["PNG", "JPG", "JPEG", "WEBP", "SVG"].indexOf(item.file_type) >= 0; }

  /* ------------------------------------------------------------ folders ---- */
  function findNode(node, path) {
    if ((node.path || "") === (path || "")) return node;
    for (var index = 0; index < node.folders.length; index += 1) {
      var found = findNode(node.folders[index], path);
      if (found) return found;
    }
    return null;
  }

  function folderHref(subject, path) {
    var base = root + (subject.material_route || subject.route);
    return path ? base + "?folder=" + encodeURIComponent(path) : base;
  }

  function renderFolderTiles(mount, subject, node) {
    var grid = el("div", "folder-grid");
    node.folders.forEach(function (folder) {
      var tile = el("a", "folder-card");
      tile.href = folderHref(subject, folder.path);
      var meta = [];
      if (folder.folder_count) meta.push(folder.folder_count + (folder.folder_count === 1 ? " subfolder" : " subfolders"));
      if (folder.file_count) meta.push(folder.file_count + (folder.file_count === 1 ? " file" : " files"));
      if (folder.file_types.length) meta.push(folder.file_types.join(" / "));
      tile.innerHTML =
        '<span class="folder-icon" aria-hidden="true">' + esc(folder.icon) + "</span>" +
        '<span class="folder-body">' +
          '<strong>' + esc(folder.title_en) + "</strong>" +
          '<span class="folder-hi">' + esc(folder.title_hi) + "</span>" +
          (folder.note_en ? '<span class="folder-note">' + esc(folder.note_en) + "</span>" : "") +
          '<span class="folder-meta">' + esc(meta.join(" · ")) + "</span>" +
        "</span>" +
        '<span class="folder-open">Kholo →</span>';
      grid.appendChild(tile);
    });
    mount.appendChild(grid);
  }

  /* -------------------------------------------------------------- files ---- */
  function fileRow(item) {
    var row = el("li", "material-item" + (isImage(item) ? " is-image" : ""));
    var topicChip = item.topic_id ? '<span class="chip neutral">' + esc(item.topic_id) + "</span>" : "";
    // Pictures carry their own SEO alt text; the description is part of the page
    // content so a search engine (and the student) reads what the sheet shows.
    var thumb = isImage(item)
      ? '<a class="file-thumb" href="' + esc(fileHref(item)) + '" target="_blank" rel="noopener noreferrer">' +
        '<img src="' + esc(previewHref(item)) + '" alt="' + esc(item.alt_en || item.title_en) + '" loading="lazy" decoding="async">' +
        '<span class="file-thumb-open">Poora dekho</span></a>'
      : "";
    var description = isImage(item) && item.description_en
      ? '<p class="file-description" lang="en">' + esc(item.description_en) + '</p>' +
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

  function renderFiles(mount, files, emptyText) {
    if (!files.length) {
      mount.appendChild(el("p", "empty-state", emptyText || "Is folder me abhi koi file nahi hai."));
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
    if (!crumbs || !mount) return;
    var node = findNode(subject.tree, folderPath || "") || subject.tree;
    mount.innerHTML = "";
    renderCrumbs(crumbs, subject, node, label);

    var head = el("div", "folder-head");
    head.innerHTML =
      '<h2 style="margin:0">' + esc(node.icon || "📁") + " " + esc(node.title_en) + "</h2>" +
      '<p class="muted" style="margin:0">' + esc(node.title_hi) + (node.note_en ? " — " + esc(node.note_en) : "") + "</p>";
    mount.appendChild(head);

    if (node.folders.length) renderFolderTiles(mount, subject, node);
    if (node.files.length) renderFiles(mount, node.files, "Is folder me abhi koi file nahi hai.");
    if (!node.folders.length && !node.files.length) mount.appendChild(el("p", "empty-state", "Ye folder khaali hai."));
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
      var theory = topic.material.theory[0];
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

  /* ----------------------------------------------------------- home rows --- */
  function renderHomeFolders(container, subject) {
    container.innerHTML = "";
    var grid = el("div", "folder-grid");
    subject.tree.folders.forEach(function (folder) {
      var tile = el("a", "folder-card compact");
      tile.href = folderHref(subject, folder.path);
      var meta = [];
      if (folder.file_count) meta.push(folder.file_count + " file");
      if (folder.file_types.length) meta.push(folder.file_types.join(" / "));
      tile.innerHTML =
        '<span class="folder-icon" aria-hidden="true">' + esc(folder.icon) + "</span>" +
        '<span class="folder-body"><strong>' + esc(folder.title_en) + "</strong>" +
        '<span class="folder-hi">' + esc(folder.title_hi) + "</span>" +
        '<span class="folder-meta">' + esc(meta.join(" · ")) + "</span></span>";
      grid.appendChild(tile);
    });
    container.appendChild(grid);
  }

  /* --------------------------------------------------------------- misc ---- */
  function setText(selector, value) {
    document.querySelectorAll(selector).forEach(function (node) { node.textContent = value; });
  }

  function init() {
    loadSite().then(function (data) {
      var cn = subjectOf(data, "computer-network");
      var geo = subjectOf(data, "rajasthan-geography");
      var downloads = data.subjects.reduce(function (total, subject) { return total + subject.file_count; }, 0);

      setText("[data-count='topics']", cn && cn.test ? cn.test.topic_count : 7);
      setText("[data-count='questions']", cn && cn.test ? number(cn.test.question_count) : "0");
      setText("[data-count='downloads']", number(downloads));
      setText("[data-count='maps']", geo ? geo.file_count : 0);
      setText("[data-build]", data.bank_build_id || "");

      document.querySelectorAll("[data-subject-card]").forEach(function (card) {
        var subject = subjectOf(data, card.getAttribute("data-subject-card"));
        if (!subject) return;
        card.querySelectorAll("[data-count='subject-files']").forEach(function (node) { node.textContent = subject.file_count; });
        card.querySelectorAll("[data-count='subject-folders']").forEach(function (node) { node.textContent = subject.folder_count; });
        if (subject.test) {
          card.querySelectorAll("[data-count='subject-questions']").forEach(function (node) {
            node.textContent = number(subject.test.question_count);
          });
        }
      });

      var homeFolders = document.getElementById("cnFolders");
      if (homeFolders && cn) renderHomeFolders(homeFolders, cn);

      var homeMapPath = document.getElementById("geoFolderPath");
      if (homeMapPath && geo) {
        // Geo page ek hi chain dikhata hai: Map › Rajasthan › (aage jo folders aayenge)
        var chain = [];
        (function descend(node) {
          node.folders.forEach(function (folder) {
            chain.push(folder.title_en);
            descend(folder);
          });
        })(geo.tree);
        homeMapPath.textContent = chain.join(" › ");
      }

      var topicGrid = document.getElementById("topicGrid");
      if (topicGrid && cn) renderTopicGrid(topicGrid, cn);

      var cnFolders = document.getElementById("subjectFolders");
      if (cnFolders && cn) {
        var grid = el("div", "folder-grid");
        cn.tree.folders.forEach(function (folder) {
          var tile = el("a", "folder-card");
          tile.href = folderHref(cn, folder.path);
          var meta = [folder.file_count + " file" + (folder.file_count === 1 ? "" : "s")];
          if (folder.file_types.length) meta.push(folder.file_types.join(" / "));
          tile.innerHTML =
            '<span class="folder-icon" aria-hidden="true">' + esc(folder.icon) + "</span>" +
            '<span class="folder-body"><strong>' + esc(folder.title_en) + "</strong>" +
            '<span class="folder-hi">' + esc(folder.title_hi) + "</span>" +
            '<span class="folder-note">' + esc(folder.note_en) + "</span>" +
            '<span class="folder-meta">' + esc(meta.join(" · ")) + "</span></span>" +
            '<span class="folder-open">Kholo →</span>';
          grid.appendChild(tile);
        });
        cnFolders.appendChild(grid);
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
