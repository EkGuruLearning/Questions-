import html.parser
import json
import pathlib
import unittest
from urllib.parse import unquote, urlsplit

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGES = [
    ROOT / "index.html",
    ROOT / "subjects/index.html",
    ROOT / "subjects/computer-network/index.html",
    ROOT / "subjects/rajasthan-geography/index.html",
    ROOT / "maps/index.html",
    ROOT / "maps/rajasthan/index.html",
    ROOT / "practice/index.html",
    ROOT / "study-material/index.html",
    ROOT / "sources/index.html",
    ROOT / "guides/repository-structure/index.html",
]


class PageParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.buttons = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "a":
            self.links.append(attrs)
        if tag == "button":
            self.buttons.append(attrs)
        if tag == "img":
            self.images.append(attrs)


class NavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {}
        for path in PAGES:
            parser = PageParser()
            parser.feed(path.read_text(encoding="utf-8"))
            cls.pages[path.relative_to(ROOT).as_posix()] = (path.read_text(encoding="utf-8"), parser)

    def test_every_public_route_has_mobile_semantic_navigation(self):
        for rel, (source, parser) in self.pages.items():
            with self.subTest(page=rel):
                self.assertIn('name="viewport"', source)
                self.assertIn('aria-label="Main navigation"', source)
                self.assertIn('href="#main"', source)
                self.assertIn('aria-current="page"', source)
                self.assertEqual(len(parser.ids), len(set(parser.ids)), "duplicate id attribute")

    def test_main_routes_are_real_same_tab_anchors(self):
        expected = {
            "Home": "index.html",
            "All Subjects": "subjects/index.html",
            "Computer Network": "subjects/computer-network/index.html",
            "Rajasthan Geography": "subjects/rajasthan-geography/index.html",
            "Maps &amp; Atlases": "maps/index.html",
            "Practice Tests": "practice/index.html",
            "Study Material": "study-material/index.html",
            "Sources &amp; Verification": "sources/index.html",
            "File Guide": "guides/repository-structure/index.html",
        }
        source, parser = self.pages["index.html"]
        for href in expected.values():
            self.assertIn(f'href="{href}"', source)
        for link in parser.links:
            href = link.get("href", "")
            if href in expected.values():
                self.assertNotEqual(link.get("target"), "_blank", f"internal route unexpectedly opens new tab: {href}")

    def test_breadcrumb_fragments_and_page_ids_resolve(self):
        for rel, (source, parser) in self.pages.items():
            ids = set(parser.ids)
            for link in parser.links:
                href = link.get("href", "")
                if href.startswith("#") and href != "#":
                    self.assertIn(href[1:], ids, f"{rel}: missing in-page target {href}")
                if not href or href == "#":
                    self.fail(f"{rel}: empty/dead anchor")

    def test_internal_subject_cards_and_breadcrumbs_do_not_force_new_tabs(self):
        for rel in ("index.html", "subjects/index.html", "subjects/computer-network/index.html", "subjects/rajasthan-geography/index.html"):
            _, parser = self.pages[rel]
            for link in parser.links:
                href = link.get("href", "")
                if any(route in href for route in ("subjects/", "maps/", "practice/", "study-material/", "sources/", "guides/")) and not urlsplit(href).scheme:
                    self.assertNotEqual(link.get("target"), "_blank", f"{rel}: internal navigation opened a new tab: {href}")

    def test_external_and_pdf_new_tabs_are_explicit_and_safe(self):
        for rel, (_, parser) in self.pages.items():
            for link in parser.links:
                href = link.get("href", "")
                if link.get("target") == "_blank":
                    safe = set((link.get("rel") or "").lower().split())
                    self.assertTrue({"noopener", "noreferrer"}.issubset(safe), (rel, link))
                if urlsplit(href).path.lower().endswith(".pdf"):
                    self.assertEqual(link.get("target"), "_blank", f"PDF should be labelled as opening separately: {rel} {href}")

    def test_real_map_previews_have_alt_and_same_tab_detail_actions(self):
        for rel in ("index.html", "subjects/rajasthan-geography/index.html", "maps/index.html", "maps/rajasthan/index.html"):
            _, parser = self.pages[rel]
            self.assertTrue(parser.images, rel)
            self.assertTrue(all((img.get("alt") or "").strip() for img in parser.images), rel)
        home_source, _ = self.pages["index.html"]
        self.assertIn("rajasthan-border-atlas-preview.webp", home_source)
        map_source, map_parser = self.pages["maps/rajasthan/index.html"]
        self.assertIn('id="fullSizeMapLink"', map_source)
        full_size = next(link for link in map_parser.links if link.get("id") == "fullSizeMapLink")
        self.assertNotEqual(full_size.get("target"), "_blank")

    def test_manifest_new_tab_resources_and_official_sources_are_labelled(self):
        resources = json.loads((ROOT / "assets/catalog/resources.json").read_text(encoding="utf-8"))["resources"]
        for item in resources:
            if item.get("repo_path", "").lower().endswith(".pdf"):
                self.assertEqual(item.get("open_behavior"), "new_tab", item["id"])
            if item.get("open_behavior") == "new_tab":
                self.assertIn("new tab", item.get("external_open_label", "").lower(), item["id"])
        maps = json.loads((ROOT / "assets/catalog/maps.json").read_text(encoding="utf-8"))
        for map_item in maps["maps"]:
            if map_item.get("image_open_behavior") == "new_tab":
                self.assertIn("new tab", map_item.get("external_open_label", "").lower(), map_item["id"])
        for source in maps["official_sources"]:
            self.assertEqual(source.get("open_behavior"), "new_tab")
            self.assertIn("new tab", source.get("external_open_label", "").lower())

    def test_static_fallbacks_and_truthful_subject_statuses(self):
        cn_source, _ = self.pages["subjects/computer-network/index.html"]
        geo_source, _ = self.pages["subjects/rajasthan-geography/index.html"]
        self.assertIn("canonical/build metadata", cn_source)
        self.assertIn("no question bank", geo_source.lower())
        self.assertIn("No usable Rajasthan Geography practice test", geo_source)
        self.assertIn("Computer Network practice app", cn_source)
        subjects = json.loads((ROOT / "assets/catalog/subjects.json").read_text(encoding="utf-8"))
        by_id = {item["id"]: item for item in subjects["subjects"]}
        self.assertEqual(by_id["computer-network"]["status"], "live")
        self.assertEqual(by_id["rajasthan-geography"]["status"], "live")
        self.assertNotIn("question_count", by_id["rajasthan-geography"])

    def test_repository_structure_guide_is_public_and_actionable(self):
        source, _ = self.pages["guides/repository-structure/index.html"]
        self.assertIn("python3 tools/read_structure.py --check", source)
        self.assertIn("Computer Network/Topics/T01/", source)
        self.assertIn("data/catalog/books.json", source)
        self.assertIn("Geography/Map/Rajasthan/", source)
        self.assertIn("Rajasthan Geography Maps/", source)
        self.assertIn('aria-current="page"', source)
        home_source, home_parser = self.pages["index.html"]
        self.assertTrue(any(link.get("href") == "guides/repository-structure/index.html" for link in home_parser.links))
        self.assertIn("same tab", source.lower())

    def test_practice_portal_preserves_real_interactive_controls(self):
        source, parser = self.pages["practice/index.html"]
        self.assertIn('id="startButton"', source)
        self.assertIn('id="topicSelect"', source)
        self.assertIn("saved in this browser", source.lower())
        self.assertIn('src="../assets/js/app.mjs"', source)
        self.assertTrue(any(link.get("href") == "../index.html" for link in parser.links))

    def test_all_buttons_have_explicit_types(self):
        for rel, (_, parser) in self.pages.items():
            for button in parser.buttons:
                self.assertIn(button.get("type"), ("button", "submit", "reset"), (rel, button))


if __name__ == "__main__":
    unittest.main()
