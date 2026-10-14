import html.parser
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]


class PageParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "a":
            self.links.append(attrs)
        if tag == "button":
            self.buttons.append(attrs)


class NavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = ROOT / "index.html"
        cls.parser = PageParser()
        cls.parser.feed(cls.path.read_text(encoding="utf-8"))

    def test_root_has_mobile_accessible_navigation(self):
        html = self.path.read_text(encoding="utf-8")
        self.assertIn('name="viewport"', html)
        self.assertIn('id="navToggle"', html)
        self.assertIn('aria-expanded="false"', html)
        self.assertIn('aria-controls="siteNav"', html)
        self.assertIn('aria-label="Main navigation"', html)
        self.assertIn('href="#main"', html)

    def test_in_page_links_resolve_and_ids_are_unique(self):
        self.assertEqual(len(self.parser.ids), len(set(self.parser.ids)), "duplicate id attribute")
        ids = set(self.parser.ids)
        for link in self.parser.links:
            href = link.get("href", "")
            if href.startswith("#") and href != "#":
                self.assertIn(href[1:], ids, f"missing in-page target {href}")

    def test_buttons_have_explicit_type_and_actions_are_not_fake_notifications(self):
        for button in self.parser.buttons:
            self.assertIn(button.get("type"), ("button", "submit", "reset"), button)
        html = self.path.read_text(encoding="utf-8").lower()
        self.assertNotIn("notify me", html)
        self.assertNotIn("subscribe", html)
        self.assertIn("push/email notifications", html)
        self.assertIn("saved in this browser", html)

    def test_external_new_tab_links_are_safe(self):
        for link in self.parser.links:
            if link.get("target") == "_blank":
                rel = set((link.get("rel") or "").lower().split())
                self.assertTrue({"noopener", "noreferrer"}.issubset(rel), link)


if __name__ == "__main__":
    unittest.main()
