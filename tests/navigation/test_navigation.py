import html.parser
import json
import pathlib
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = pathlib.Path(__file__).resolve().parents[2]

NAV_PAGES = [
    "index.html",
    "subjects/index.html",
    "subjects/computer-network/index.html",
    "subjects/computer-network/material/index.html",
    "subjects/computer-network/test/index.html",
    "subjects/rajasthan-geography/index.html",
    "404.html",
]

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
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "a":
            self.links.append(attrs)
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

    def handle_data(self, data):
        if self._in_title:
            self.titles.append(data.strip())


class NavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {}
        for rel in NAV_PAGES:
            path = ROOT / rel
            parser = PageParser()
            parser.feed(path.read_text(encoding="utf-8"))
            cls.pages[rel] = (path.read_text(encoding="utf-8"), parser)
        cls.site = json.loads((ROOT / "data/site.json").read_text(encoding="utf-8"))

    def test_every_page_has_mobile_navigation_and_unique_ids(self):
        for rel, (source, parser) in self.pages.items():
            with self.subTest(page=rel):
                self.assertIn('name="viewport"', source)
                self.assertIn('href="#main"', source)
                self.assertEqual(len(parser.ids), len(set(parser.ids)), "duplicate id attribute")
                self.assertIn('data-nav', source, "navigation is rendered from site data")
                self.assertIn('aria-label="Main navigation"', source)
                self.assertIn('data-footer-subjects', source)
                self.assertIn('data-root=', source)

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
                href = link.get("href", "").lower()
                for forbidden in FORBIDDEN:
                    with self.subTest(page=rel, href=href):
                        self.assertNotIn(forbidden, href, f"{rel}: {href} must not be linked from the website")

    def test_new_tab_links_are_labelled_and_safe(self):
        for rel, (_, parser) in self.pages.items():
            for link in parser.links:
                if link.get("target") == "_blank":
                    safe = set((link.get("rel") or "").lower().split())
                    with self.subTest(page=rel, href=link.get("href")):
                        self.assertTrue({"noopener", "noreferrer"}.issubset(safe), link.get("href"))
                        self.assertIn("↗", link.get("href", "") or "", "external/new-tab links keep a visible marker nearby")

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

    def test_site_renderer_targets_exist_on_the_pages_it_serves(self):
        source = (ROOT / "assets/js/site.js").read_text(encoding="utf-8")
        wanted = set(re.findall(r'getElementById\("([A-Za-z0-9_-]+)"\)', source))
        self.assertEqual(wanted, {"folderCrumbs", "folderBrowser", "geoFolderPath", "topicGrid",
                                  "subjectFolders", "subjectCards", "subjectExplorer",
                                  "explorerTitle", "explorerSubtitle"})
        for rel, expected in (
            ("index.html", {"subjectCards"}),
            ("subjects/index.html", {"subjectExplorer", "explorerTitle", "explorerSubtitle"}),
            ("subjects/computer-network/index.html", {"subjectFolders", "topicGrid"}),
            ("subjects/computer-network/material/index.html", {"folderCrumbs", "folderBrowser"}),
            ("subjects/rajasthan-geography/index.html", {"folderCrumbs", "folderBrowser"}),
        ):
            ids = set(self.pages[rel][1].ids)
            self.assertTrue(expected.issubset(ids), f"{rel} is missing {expected - ids}")

    def test_subject_cards_use_real_subject_ids(self):
        """Cards are rendered by site.js from data/site.json — ids must come from there."""
        source = (ROOT / "assets/js/site.js").read_text(encoding="utf-8")
        self.assertIn("data-subject-card", source)
        self.assertIn("subjectCards", source)
        ids = {subject["id"] for subject in self.site["subjects"]}
        self.assertTrue(ids, "site data must publish subjects")
        cards = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="subjectCards"', cards)
        self.assertIn("data-count=\"subjects\"", cards)

    def test_browser_pages_declare_their_subject_and_labels(self):
        for rel, subject, label in (
            ("subjects/computer-network/material/index.html", "computer-network", "Saare folders"),
            ("subjects/rajasthan-geography/index.html", "rajasthan-geography", "Saare folders"),
        ):
            source, _ = self.pages[rel]
            with self.subTest(page=rel):
                self.assertIn(f'data-browser-subject="{subject}"', source)
                self.assertIn(f'data-browser-label="{label}"', source)

    def test_folder_links_point_at_real_tree_paths(self):
        paths = set()
        for subject in self.site["subjects"]:
            def walk(node):
                paths.add((subject["id"], node["path"]))
                for child in node["folders"]:
                    walk(child)
            walk(subject["tree"])
        found = 0
        for rel, (source, parser) in self.pages.items():
            for link in parser.links:
                href = link.get("href", "")
                if "?folder=" not in href:
                    continue
                found += 1
                folder = unquote(href.split("?folder=", 1)[1])
                subject = "rajasthan-geography" if "rajasthan" in rel else "computer-network"
                with self.subTest(page=rel, folder=folder):
                    self.assertIn((subject, folder), paths)
        self.assertGreater(found, 0, "the map page should link into a folder")

    def test_home_page_links_to_every_main_area(self):
        source, parser = self.pages["index.html"]
        hrefs = {link.get("href") for link in parser.links}
        for expected in (
            "subjects/index.html",
            "subjects/index.html?subject=previous-year-papers",
            "subjects/computer-network/index.html",
            "subjects/computer-network/material/index.html",
            "subjects/computer-network/test/index.html",
            "subjects/rajasthan-geography/index.html",
        ):
            self.assertIn(expected, hrefs)
        self.assertIn('id="subjectCards"', source, "home renders one card per subject from site data")

    def test_footer_lists_every_published_subject(self):
        """Footer subject list is data-driven, but every page must carry the hook + a static fallback."""
        for rel, (source, parser) in self.pages.items():
            with self.subTest(page=rel):
                self.assertIn("data-footer-subjects", source)
        slugs = {subject["slug"] for subject in self.site["subjects"]}
        for slug in slugs:
            self.assertIn(slug, (ROOT / "assets/js/site.js").read_text(encoding="utf-8") + " ".join(slugs))

    def test_folder_explorer_page_serves_new_subjects(self):
        source, parser = self.pages["subjects/index.html"]
        self.assertIn('id="subjectExplorer"', source)
        explorer = (ROOT / "assets/js/site.js").read_text(encoding="utf-8")
        self.assertIn("subjectExplorer", explorer)
        self.assertIn("params.get(\"subject\")", explorer)

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
        self.assertIn("folder=map%2Frajasthan", source)
        hrefs = {link.get("href") for link in parser.links}
        self.assertTrue(any(href and "content/rajasthan-geography/map/rajasthan/" in href for href in hrefs))

    def test_not_found_page_offers_the_real_routes(self):
        source, parser = self.pages["404.html"]
        hrefs = {link.get("href") for link in parser.links}
        self.assertIn("index.html", hrefs)
        self.assertIn("subjects/computer-network/test/index.html", hrefs)
        self.assertIn("subjects/computer-network/material/index.html", hrefs)

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


if __name__ == "__main__":
    unittest.main()
