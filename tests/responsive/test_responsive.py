import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
CSS_PATH = ROOT / "assets/css/portal.css"
HTML_PATH = ROOT / "index.html"


class ResponsiveStructuralTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.css = CSS_PATH.read_text(encoding="utf-8")
        cls.html = HTML_PATH.read_text(encoding="utf-8")

    def test_viewport_and_css_breakpoints_are_present(self):
        self.assertRegex(self.html, r'<meta\s+name="viewport"\s+content="width=device-width, initial-scale=1"')
        self.assertRegex(self.css, r"@media\s*\(max-width:\s*900px\)")
        self.assertRegex(self.css, r"@media\s*\(max-width:\s*720px\)")
        self.assertRegex(self.css, r"@media\s*\(max-width:\s*520px\)")
        self.assertIn("prefers-reduced-motion", self.css)

    def test_layout_grids_can_collapse_without_forced_wide_columns(self):
        self.assertIn("grid-template-columns: minmax(0, 1.45fr)", self.css)
        self.assertIn(".hero-inner { grid-template-columns: minmax(0, 1fr);", self.css)
        self.assertIn(".quiz-layout { grid-template-columns: minmax(0, 1fr); }", self.css)
        self.assertIn(".form-grid { grid-template-columns: minmax(0, 1fr); }", self.css)
        self.assertIn("overflow-x: auto", self.css)
        self.assertIn("overflow-wrap: anywhere", self.css)
        self.assertNotRegex(self.css, r"body\s*\{[^}]*min-width:\s*(?:[4-9]\d\d|\d{4,})px")

    def test_navigation_and_touch_controls_have_mobile_states(self):
        nav_rule = self.css.index(".nav-toggle { display: inline-flex")
        self.assertLess(nav_rule, self.css.index("@media (max-width: 720px)"), "compact navigation should also cover tablet widths")
        self.assertIn(".site-nav.open { display: grid", self.css)
        self.assertRegex(self.css, r"\.button(?:\.small)?\s*\{[^}]*min-height:\s*44px")
        self.assertRegex(self.css, r"\.palette-button\s*\{[^}]*min-height:\s*44px")

    def test_mobile_sections_reorder_and_single_column(self):
        mobile = re.search(r"@media\s*\(max-width:\s*520px\)\s*\{(.*?)\n\}", self.css, re.S)
        self.assertIsNotNone(mobile)
        self.assertIn("grid-template-columns: minmax(0, 1fr)", mobile.group(1))
        self.assertIn("flex: 1 1 100%", mobile.group(1))


if __name__ == "__main__":
    unittest.main()
