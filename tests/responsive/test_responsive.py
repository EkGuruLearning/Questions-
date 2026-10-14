import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITE_CSS = ROOT / "assets/css/site.css"
PORTAL_CSS = ROOT / "assets/css/portal.css"
PUBLIC_PAGES = [
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


class ResponsiveStructuralTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.site_css = SITE_CSS.read_text(encoding="utf-8")
        cls.portal_css = PORTAL_CSS.read_text(encoding="utf-8")
        cls.pages = {path.relative_to(ROOT).as_posix(): path.read_text(encoding="utf-8") for path in PUBLIC_PAGES}

    def test_every_route_has_viewport_and_shared_site_css(self):
        for path, source in self.pages.items():
            with self.subTest(path=path):
                self.assertRegex(source, r'<meta\s+name="viewport"\s+content="width=device-width, initial-scale=1"')
                self.assertRegex(source, r'<link\s+rel="stylesheet"\s+href="[^"]*site\.css"')
        self.assertIn("prefers-reduced-motion", self.site_css)
        self.assertIn("prefers-reduced-motion", self.portal_css)

    def test_mobile_breakpoints_and_fluid_columns_are_present(self):
        for width in (950, 720, 520):
            self.assertRegex(self.site_css, rf"@media\s*\(max-width:\s*{width}px\)")
        self.assertIn("grid-template-columns: minmax(0, 1fr)", self.site_css)
        self.assertIn("grid-template-columns: repeat(2, minmax(0, 1fr))", self.site_css)
        self.assertIn("min-width: 0", self.site_css)
        self.assertNotRegex(self.site_css, r"body\s*\{[^}]*min-width:\s*(?:[4-9]\d\d|\d{4,})px")
        self.assertNotRegex(self.portal_css, r"body\s*\{[^}]*min-width:\s*(?:[4-9]\d\d|\d{4,})px")

    def test_maps_keep_aspect_ratio_and_tables_scroll_inside_their_wrapper(self):
        self.assertRegex(self.site_css, r"img,\s*svg,\s*video\s*\{[^}]*max-width:\s*100%")
        self.assertRegex(self.site_css, r"\.map-frame\s+img\s*\{[^}]*height:\s*auto")
        self.assertIn("overflow-x: auto", self.site_css)
        self.assertIn("overscroll-behavior-x: contain", self.site_css)
        self.assertIn("overflow-wrap: anywhere", self.site_css)
        for path in ("subjects/rajasthan-geography/index.html", "maps/index.html", "maps/rajasthan/index.html"):
            source = self.pages[path]
            self.assertRegex(source, r'<img[^>]*\balt="[^"]+"')

    def test_touch_targets_and_keyboard_focus_are_visible(self):
        self.assertRegex(self.site_css, r"\.button\s*\{[^}]*min-height:\s*44px")
        self.assertRegex(self.site_css, r"\.site-menu-toggle\s*\{[^}]*min-height:\s*44px")
        self.assertRegex(self.site_css, r"\.site-nav a\s*\{[^}]*min-height:\s*44px")
        self.assertIn(":focus-visible", self.site_css)
        self.assertIn("outline-offset", self.site_css)
        self.assertIn(".site-menu:not([open]) .site-nav { display: none", self.site_css)
        self.assertIn(".site-menu[open] .site-nav { position: absolute", self.site_css)

    def test_wide_tables_are_not_wide_pages_and_long_names_can_wrap(self):
        self.assertIn(".table-scroll { max-width: 100%; overflow-x: auto", self.site_css)
        self.assertIn("overflow-wrap: anywhere", self.site_css)
        self.assertNotIn("width: 100vw", self.site_css)
        self.assertNotIn("min-width: 1000px", self.site_css)

    def test_practice_app_retains_its_mobile_quiz_states(self):
        source = self.pages["practice/index.html"]
        self.assertIn("portal.css", source)
        self.assertIn('id="navToggle"', source)
        self.assertRegex(self.portal_css, r"@media\s*\(max-width:\s*900px\)")
        self.assertRegex(self.portal_css, r"@media\s*\(max-width:\s*720px\)")
        self.assertRegex(self.portal_css, r"@media\s*\(max-width:\s*520px\)")
        self.assertIn(".quiz-layout", self.portal_css)
        self.assertIn(".form-grid", self.portal_css)
        self.assertIn("overflow-x: auto", self.portal_css)


if __name__ == "__main__":
    unittest.main()
