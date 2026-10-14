import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
CSS = ROOT / "assets/css/ekguru.css"
PAGES = [
    ROOT / "index.html",
    ROOT / "subjects/index.html",
    ROOT / "subjects/computer-network/index.html",
    ROOT / "subjects/computer-network/material/index.html",
    ROOT / "subjects/computer-network/test/index.html",
    ROOT / "subjects/rajasthan-geography/index.html",
    ROOT / "404.html",
]


class ResponsiveStructuralTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.css = CSS.read_text(encoding="utf-8")
        cls.pages = {path.relative_to(ROOT).as_posix(): path.read_text(encoding="utf-8") for path in PAGES}

    def test_every_page_has_viewport_and_the_shared_stylesheet(self):
        for path, source in self.pages.items():
            with self.subTest(page=path):
                self.assertRegex(source, r'<meta\s+name="viewport"\s+content="width=device-width, initial-scale=1"')
                self.assertIn("assets/css/ekguru.css", source)
        self.assertIn("prefers-reduced-motion", self.css)

    def test_mobile_breakpoints_and_fluid_columns_are_present(self):
        for width in (950, 720, 520):
            self.assertRegex(self.css, rf"@media\s*\(max-width:\s*{width}px\)")
        self.assertIn("grid-template-columns: minmax(0, 1fr)", self.css)
        self.assertIn("grid-template-columns: repeat(2, minmax(0, 1fr))", self.css)
        self.assertIn("min-width: 0", self.css)
        self.assertNotRegex(self.css, r"body\s*\{[^}]*min-width:\s*(?:[4-9]\d\d|\d{4,})px")
        self.assertNotIn("width: 100vw", self.css)

    def test_images_and_long_text_cannot_break_the_layout(self):
        self.assertRegex(self.css, r"img,\s*svg,\s*video\s*\{[^}]*max-width:\s*100%")
        self.assertRegex(self.css, r"\.map-frame\s+img\s*\{[^}]*height:\s*auto")
        self.assertIn("overflow-wrap: anywhere", self.css)

    def test_touch_targets_and_keyboard_focus_are_visible(self):
        self.assertRegex(self.css, r"\.button\s*\{[^}]*min-height:\s*44px")
        self.assertRegex(self.css, r"\.site-menu-toggle\s*\{[^}]*min-height:\s*44px")
        self.assertRegex(self.css, r"\.site-nav a\s*\{[^}]*min-height:\s*44px")
        self.assertIn(":focus-visible", self.css)
        self.assertIn("outline-offset", self.css)
        self.assertIn(".site-menu:not([open]) .site-nav { display: none", self.css)

    def test_mobile_menu_is_a_dropdown_and_desktop_nav_is_always_visible(self):
        # small screens: <details> menu; 951px+: a normal nav row, menu hidden
        self.assertRegex(self.css, r"\.desktop-nav\s*\{\s*display:\s*none")
        self.assertRegex(self.css, r"@media\s*\(min-width:\s*951px\)\s*\{[^@]*\.desktop-nav\s*\{[^}]*display:\s*flex")
        self.assertRegex(self.css, r"@media\s*\(min-width:\s*951px\)\s*\{[^@]*\.site-menu\s*\{\s*display:\s*none")
        self.assertRegex(self.css, r"\.site-menu\[open\]\s+\.site-nav\s*\{")
        self.assertRegex(self.css, r'\.site-nav\s+a\[aria-current="page"\]')

    def test_folder_tiles_and_breadcrumbs_are_responsive(self):
        self.assertIn(".folder-grid", self.css)
        self.assertIn(".folder-card", self.css)
        self.assertIn(".folder-open", self.css)
        self.assertIn(".crumbs", self.css)
        self.assertIn(".file-thumb", self.css)
        self.assertRegex(self.css, r"\.file-thumb\s+img\s*\{[^}]*object-fit:\s*cover")
        self.assertRegex(self.css, r"@media\s*\(min-width:\s*720px\)\s*\{[^@]*folder-grid\s*\{\s*grid-template-columns:\s*repeat\(2")

    def test_test_app_keeps_its_mobile_quiz_states(self):
        self.assertIn(".option[aria-pressed=\"true\"]", self.css)
        self.assertIn(".option.correct", self.css)
        self.assertIn(".option.wrong", self.css)
        self.assertIn(".palette-grid", self.css)
        self.assertIn(".progress-track", self.css)
        self.assertIn(".score-ring", self.css)
        source = self.pages["subjects/computer-network/test/index.html"]
        self.assertIn('id="paletteGrid"', source)
        self.assertIn('id="optionList"', source)
        self.assertIn('id="progressFill"', source)

    def test_question_text_and_options_wrap_on_small_screens(self):
        self.assertRegex(self.css, r"\.question-stem\s*\{[^}]*white-space:\s*pre-line")
        self.assertRegex(self.css, r"\.option\s*\.opt-text\s*\{[^}]*overflow-wrap:\s*anywhere")
        self.assertIn("@media (max-width: 520px)", self.css)


if __name__ == "__main__":
    unittest.main()
