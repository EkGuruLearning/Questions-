"""Navigation checks for the plain-HTML site.

The pages are generated as static HTML (tools/build_pages.py), so everything a
visitor needs — subject lists, folder lists, breadcrumbs with a way back up,
nav and footer links — must be present in the HTML itself. No renderer, no
`fetch`, no JavaScript required to read a page.
"""

import html
import html.parser
import json
import pathlib
import re
import unittest
import urllib.parse
from urllib.parse import unquote, urlsplit

ROOT = pathlib.Path(__file__).resolve().parents[2]
ROUTES_FILE = ROOT / "data/catalog/site-routes.txt"

FORBIDDEN = ("maintainer/", "tools/", "tests/", "README.md", "SITE_GUIDE.md", ".md")


class PageParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.buttons = []
        self.images = []
        self.scripts = []
        self.meta = []
        self.titles = []
        self.anchor_text = {}
        self._in_title = False
        self._anchor = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "a":
            self.links.append(attrs)
            self._anchor = attrs.get("href", "")
            self.anchor_text.setdefault(self._anchor, "")
        elif tag == "button":
            self.buttons.append(attrs)
        elif tag == "img":
            self.images.append(attrs)
        elif tag == "script":
            self.scripts.append(attrs)
        elif tag == "meta":
            self.meta.append(attrs)
        elif tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "a":
            self._anchor = None

    def handle_data(self, data):
        if self._in_title:
            self.titles.append(data.strip())
        if self._anchor is not None:
            self.anchor_text[self._anchor] += data


def repo_target(page: str, href: str) -> str:
    """Repo path a link points at ('' when it leaves the site)."""
    split = urllib.parse.urlsplit(href)
    if split.scheme or not split.path:
        return ""
    target = (ROOT / page).parent / urllib.parse.unquote(split.path)
    try:
        return target.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return ""


def published_pages():
    return [line.strip() for line in ROUTES_FILE.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")]


class NavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.routes = published_pages()
        cls.pages = {}
        for rel in cls.routes:
            source = (ROOT / rel).read_text(encoding="utf-8")
            parser = PageParser()
            parser.feed(source)
            cls.pages[rel] = (source, parser)
        cls.site = json.loads((ROOT / "data/site.json").read_text(encoding="utf-8"))
        cls.slugs = [subject["slug"] for subject in cls.site["subjects"]]

    def test_every_page_loads_without_javascript(self):
        """Plain HTML: no runtime renderer, no fetch, no remote asset."""
        for rel, (source, parser) in self.pages.items():
            with self.subTest(page=rel):
                self.assertIn('name="viewport"', source)
                self.assertIn('href="#main"', source)
                self.assertNotIn("assets/js/site.js", source)
                self.assertNotIn("fetch(", source)
                for script in parser.scripts:
                    src = script.get("src", "")
                    self.assertTrue(src == "" or src.startswith(("assets/", "../", "../../")),
                                    f"{rel}: unexpected script {src}")

    def test_every_page_has_unique_ids_and_mobile_navigation(self):
        for rel, (source, parser) in self.pages.items():
            with self.subTest(page=rel):
                self.assertEqual(len(parser.ids), len(set(parser.ids)), "duplicate id attribute")
                self.assertIn('aria-label="Main navigation"', source)
                self.assertIn("site-menu", source, "mobile menu markup")
                self.assertNotIn("data-nav", source, "nav is written out, not rendered")
                self.assertNotIn("data-root", source, "no leftover renderer hooks")
                self.assertNotIn("data-footer-subjects", source)

    def test_navigation_and_footer_list_every_subject_as_real_links(self):
        for rel, (source, parser) in self.pages.items():
            if rel == "404.html":
                continue  # the not-found page is served from the site root with root-relative links
            targets = {repo_target(rel, link.get("href", "")) for link in parser.links}
            with self.subTest(page=rel):
                for slug in self.slugs:
                    expected = f"subjects/{slug}/index.html"
                    self.assertIn(expected, targets, f"{rel}: nothing links to {expected}")
                self.assertIn("footer-grid", source)

    def test_internal_links_and_anchors_resolve(self):
        for rel, (source, parser) in self.pages.items():
            ids = set(parser.ids)
            for link in parser.links:
                href = link.get("href", "")
                with self.subTest(page=rel, href=href):
                    self.assertTrue(href, f"{rel}: empty link")
                    if href.startswith("#"):
                        self.assertIn(href[1:], ids, f"{rel}: missing anchor {href}")
                        continue
                    if urlsplit(href).scheme or href.startswith("data:"):
                        continue
                    target = (ROOT / rel).parent / unquote(urlsplit(href).path)
                    self.assertTrue(target.is_file() or target.is_dir(), f"{rel}: broken link {href}")

    def test_no_audit_or_markdown_links_are_published(self):
        for rel, (source, parser) in self.pages.items():
            for link in parser.links:
                href = link.get("href", "")
                resolved = repo_target(rel, href)
                with self.subTest(page=rel, href=href):
                    if resolved.startswith(("maintainer/", "tools/", "tests/", "data/schemas/")):
                        self.fail(f"{rel}: {href} points at repo-only material")
                    self.assertNotIn(resolved, ("README.md", "SITE_GUIDE.md"), f"{rel}: {href} is a repo document")
                    self.assertNotIn(".md", resolved.lower(), f"{rel}: {href} is a markdown file")
                    self.assertNotIn("http://localhost", href)

    def test_no_build_instructions_or_build_ids_leak_to_visitors(self):
        for rel, (source, _) in self.pages.items():
            with self.subTest(page=rel):
                self.assertNotIn("python3 ", source, f"{rel}: shows a build command")
                self.assertNotIn("bank_build_id", source)
                self.assertNotIn("cn-014b0aa5", source)
                self.assertNotIn("content/", re.sub(r"href=\"[^\"]*\"", "", source).split("<code>", 1)[0]
                                 if "content/" in source else source)

    def test_new_tab_links_are_labelled_and_safe(self):
        for rel, (_, parser) in self.pages.items():
            for link in parser.links:
                if link.get("target") == "_blank":
                    safe = set((link.get("rel") or "").lower().split())
                    href = link.get("href", "")
                    with self.subTest(page=rel, href=href):
                        self.assertTrue({"noopener", "noreferrer"}.issubset(safe), href)
                        label = parser.anchor_text.get(href, "")
                        self.assertIn("↗", label, "external/new-tab links keep a visible marker on the label")

    def test_buttons_declare_a_type(self):
        for rel, (_, parser) in self.pages.items():
            for button in parser.buttons:
                with self.subTest(page=rel):
                    self.assertIn(button.get("type"), ("button", "submit", "reset"))

    def test_every_test_app_id_exists_on_the_test_page(self):
        source = (ROOT / "assets/js/test.mjs").read_text(encoding="utf-8")
        wanted = set(re.findall(r'\$\("([A-Za-z0-9_-]+)"\)', source))
        self.assertGreater(len(wanted), 20, "test app should reference its controls by id")
        # ids created at runtime by the app itself (section picker "all sections" box)
        runtime_created = {"allSections"}
        ids = set(self.pages["subjects/computer-network/test/index.html"][1].ids)
        self.assertEqual(wanted - ids - runtime_created, set(), "test.mjs references ids that the page does not provide")

    def test_cards_come_from_site_data(self):
        """Every card and file row on a page must come from data/site.json."""
        home = (ROOT / "index.html").read_text(encoding="utf-8")
        subtitle_by_slug = {subject["slug"]: subject.get("subtitle_en", "") for subject in self.site["subjects"]}
        for slug, subtitle in subtitle_by_slug.items():
            if subtitle:
                self.assertIn(subtitle, home, f"home is missing the {slug} description")
        stats = re.findall(r'<span class="hero-stat[^"]*">(.*?)</span>\s*</div>|'
                           r'<span class="hero-stat[^"]*">.*?</span>', home, flags=re.S)
        self.assertTrue(stats, "home must show its headline numbers")
        files = sum(len(node["files"]) for subject in self.site["subjects"] for node in _walk(subject["tree"]))
        plain = html.unescape(re.sub(r"<[^>]+>", " ", home))
        self.assertIn(f"{files}", plain, "home numbers should match the published files")

    def test_subject_pages_list_their_folders_and_topics(self):
        for subject in self.site["subjects"]:
            rel = f"subjects/{subject['slug']}/index.html"
            source, parser = self.pages[rel]
            hrefs = {link.get("href") for link in parser.links}
            with self.subTest(page=rel):
                for node in subject["tree"]["folders"]:
                    suffix = f"{node['path']}/index.html"
                    self.assertTrue(any(href and href.endswith(suffix) for href in hrefs),
                                    f"{rel}: missing folder link {suffix}")
                if subject.get("topics"):
                    self.assertIn("topic-grid", source)
                    for topic in subject["topics"]:
                        self.assertIn(topic["id"], source)

    def test_every_folder_has_its_own_page_with_a_way_back_up(self):
        for subject in self.site["subjects"]:
            for node in _walk(subject["tree"]):
                if not node["path"]:
                    continue
                rel = f"subjects/{subject['slug']}/{node['path']}/index.html"
                with self.subTest(page=rel):
                    self.assertIn(rel, self.routes, "every folder gets a page")
                    source, parser = self.pages[rel]
                    crumbs = re.search(r'<nav class="crumbs".*?</nav>', source, flags=re.S)
                    self.assertIsNotNone(crumbs, f"{rel}: no breadcrumb")
                    up = re.search(r'class="crumb-up" href="([^"]+)"', source)
                    self.assertIsNotNone(up, f"{rel}: no way back up")
                    target = (ROOT / rel).parent / up.group(1)
                    self.assertTrue(target.is_file() or target.is_dir(), f"{rel}: up link {up.group(1)} is broken")
                    self.assertLessEqual(up.group(1).count(".."), 2, "the back link should stay short")
                    crumb_text = html.unescape(re.sub(r"<[^>]+>", " ", crumbs.group(0)))
                    self.assertIn(subject["title_en"], crumb_text)
                    self.assertIn(node["title_en"], crumb_text)
                    if node["path"].count("/") == 0:
                        self.assertEqual(up.group(1), "../index.html")
                    files = re.findall(r'class="material-item', source)
                    self.assertEqual(len(files), len(node["files"]))
                    if node["files"]:
                        self.assertIn("Download", source)

    def test_exam_pages_show_every_year_from_2000_to_2026(self):
        """Saal-wise grid: jis saal ka paper hai wo link, baaki saal muted chip."""
        self.assertIn("year-grid", pathlib.Path("assets/css/ekguru.css").read_text(encoding="utf-8"))
        pyq = next(subject for subject in self.site["subjects"] if subject["slug"] == "previous-year-papers")
        years = pyq["year_folders"]
        expected = [str(year) for year in range(years["to"], years["from"] - 1, -1)]
        for exam in ("rpsc", "dsssb", "computer-operator"):
            rel = f"subjects/previous-year-papers/{exam}/index.html"
            source, parser = self.pages[rel]
            with self.subTest(page=rel):
                self.assertIn("year-grid", source)
                chips = re.findall(r'class="chip (?:neutral )?year-chip[^"]*"[^>]*>(\d{4})', source)
                self.assertEqual(chips, expected, "har saal ka chip maujood hona chahiye")
                ready = re.findall(r'class="chip year-chip ready" href="([^"]+)"', source)
                for href in ready:
                    target = (ROOT / rel).parent / href
                    self.assertTrue(target.is_file() or target.is_dir(), f"{rel}: {href} broken")

    def test_year_page_offers_the_other_years(self):
        rel = "subjects/previous-year-papers/rpsc/2024/index.html"
        source, parser = self.pages[rel]
        self.assertIn("ke doosre saal", source)
        current = re.findall(r'class="chip year-chip ready" href="[^"]+" aria-current="page">(\d{4})', source)
        self.assertEqual(current, ["2024"], "khuli hui saal ki chip par nishaan hona chahiye")

    def test_home_page_links_to_every_main_area(self):
        source, parser = self.pages["index.html"]
        hrefs = {link.get("href") for link in parser.links}
        for expected in (
            "subjects/index.html",
            "subjects/computer-network/index.html",
            "subjects/computer-network/test/index.html",
            "subjects/rajasthan-geography/index.html",
            "subjects/previous-year-papers/index.html",
            "subjects/reasoning/index.html",
        ):
            self.assertIn(expected, hrefs)
        self.assertIn("subject-card", source, "home lists every subject in the HTML")

    def test_folder_explorer_serves_new_subjects(self):
        source, parser = self.pages["subjects/index.html"]
        self.assertIn("subject-card", source)
        hrefs = {link.get("href") for link in parser.links}
        for slug in self.slugs:
            self.assertTrue(any(href and href.endswith(f"subjects/{slug}/index.html") for href in hrefs))

    def test_home_page_carries_no_map_banner(self):
        source, parser = self.pages["index.html"]
        self.assertNotIn("rajasthan-border-atlas-preview", source)
        self.assertNotIn("map-frame", source)
        self.assertTrue(all((image.get("alt") or "").strip() for image in parser.images))

    def test_geography_page_shows_the_map_image_and_folder_links(self):
        source, parser = self.pages["subjects/rajasthan-geography/index.html"]
        self.assertIn("assets/img/rajasthan-border-atlas-preview.webp", source)
        self.assertIn("map-frame", source)
        self.assertTrue(all((image.get("alt") or "").strip() for image in parser.images))
        self.assertIn("map/rajasthan/index.html", source)
        hrefs = {link.get("href") for link in parser.links}
        self.assertTrue(any(href and href.startswith("../../content/rajasthan-geography/") for href in hrefs),
                        "the map page must expose the downloadable prints")

    def test_not_found_page_offers_the_real_routes(self):
        source, parser = self.pages["404.html"]
        hrefs = {link.get("href") for link in parser.links}
        self.assertIn("index.html", hrefs)
        self.assertIn("subjects/computer-network/test/index.html", hrefs)
        self.assertIn("subjects/index.html", hrefs)

    def test_geography_page_carries_border_district_seo(self):
        source, parser = self.pages["subjects/rajasthan-geography/index.html"]
        meta = next((tag for tag in parser.meta if tag.get("name") == "description"), None)
        self.assertIsNotNone(meta, "the map page needs a meta description")
        text = meta.get("content", "")
        for needle in ("41", "36", "A4", "A1"):
            self.assertIn(needle, text)
        self.assertIn("सीमावर्ती", source + text)
        self.assertIn("application/ld+json", source)
        title = " ".join(parser.titles)
        self.assertIn("Rajasthan", title)

    def test_deep_links_use_relative_paths_for_the_pages_project_base(self):
        for rel, (source, _) in self.pages.items():
            with self.subTest(page=rel):
                self.assertNotIn('src="/assets', source)
                self.assertNotIn('href="/assets', source)
                self.assertNotIn("http://localhost", source)


def _walk(node):
    yield node
    for child in node["folders"]:
        yield from _walk(child)


if __name__ == "__main__":
    unittest.main()
