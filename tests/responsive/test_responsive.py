import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
CSS = ROOT / "assets/css/ekguru.css"
ROUTES_FILE = ROOT / "data/catalog/site-routes.txt"
PAGES = [
    ROOT / "index.html",
    ROOT / "subjects/index.html",
    ROOT / "subjects/computer-network/index.html",
    ROOT / "subjects/computer-network/material/index.html",
    ROOT / "subjects/computer-network/test/index.html",
    ROOT / "subjects/rajasthan-geography/index.html",
    ROOT / "404.html",
]
# chhote phone ka sabse aam size
PHONE_WIDTHS = (360, 390, 414)


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

    def test_phone_first_rules_exist_for_layout_type_and_scrolling(self):
        """Mobile zaruri hai: chhote phone par padding, type, buttons aur scroll sab set ho."""
        self.assertRegex(self.css, r"@media\s*\(max-width:\s*380px\)", "very small phones ka block")
        self.assertIn("overflow-x: hidden", self.css, "sideways scroll kabhi na ho")
        self.assertRegex(self.css, r"html\s*\{[^}]*text-size-adjust:\s*100%")
        self.assertRegex(self.css, r"h1,\s*h2,\s*h3,\s*h4,\s*p,\s*li[^{]*\{[^}]*overflow-wrap:\s*anywhere")
        self.assertIn("scroll-margin-top", self.css, "sticky header ke neeche heading na chhupe")
        self.assertIn(".footer-bottom { flex-direction: column", self.css)

    def test_form_controls_are_16px_so_iphone_does_not_zoom(self):
        self.assertRegex(self.css, r"\.field select,[^{]*\{[^}]*font-size:\s*16px")
        self.assertIn('font: inherit; font-size: 16px;', self.css)

    def test_buttons_stay_tappable_and_full_width_on_phones(self):
        self.assertRegex(self.css, r"\.hero-actions\s+\{\s*flex-direction:\s*column")
        self.assertRegex(self.css, r"\.material-actions\s+\.button\s*\{[^}]*min-height:\s*44px")
        self.assertRegex(self.css, r"\.year-chip\s*\{[^}]*min-height:\s*(?:4[0-9]|[5-9][0-9])px")
        self.assertRegex(self.css, r"\.button\s*\{[^}]*min-height:\s*44px")

    def test_every_published_page_is_phone_ready(self):
        """Har generated page: viewport, ek stylesheet, koi fixed width nahi."""
        routes = [line.strip() for line in ROUTES_FILE.read_text(encoding="utf-8").splitlines()
                  if line.strip() and not line.strip().startswith("#")]
        self.assertGreater(len(routes), 10, "route list padhi jaani chahiye")
        for rel in routes:
            source = (ROOT / rel).read_text(encoding="utf-8")
            with self.subTest(page=rel):
                self.assertIn('name="viewport" content="width=device-width, initial-scale=1"', source)
                self.assertIn("assets/css/ekguru.css", source)
                self.assertNotRegex(source, r'width="\d{4,}"\s+(?![^>]*height)', "4-digit fixed width")
                self.assertNotIn("<table", source, "tables ko wrapper chahiye — abhi koi publish nahi hota")

    def test_quiz_buttons_are_big_enough_for_a_thumb(self):
        self.assertRegex(self.css, r"\.option\s*\{[^}]*min-height:\s*48px")
        self.assertRegex(self.css, r"\.palette-grid\s+button\s*\{[^}]*min-height:\s*44px")
        self.assertRegex(self.css, r"\.mode-switch\s*\{[^}]*flex-wrap:\s*wrap")

    def test_nav_rule_has_enough_specificity_for_phones(self):
        """`.site-nav { display:flex }` ki wajah se phone par desktop nav dikh raha tha —
        isliye hide rule `.site-nav.desktop-nav` hona chahiye (dono jagah)."""
        self.assertRegex(self.css, r"\.site-nav\.desktop-nav\s*\{\s*display:\s*none")
        self.assertRegex(
            self.css,
            r"@media\s*\(min-width:\s*951px\)\s*\{[^@]*\.site-nav\.desktop-nav\s*\{[^}]*display:\s*flex")
        self.assertNotRegex(self.css, r"(?<![\.\w])\.desktop-nav\s*\{\s*display:\s*none")

    def test_every_published_image_reserves_its_box(self):
        """Image par width/height — load hone se pehle bhi layout theek rehta hai."""
        import html.parser

        class Images(html.parser.HTMLParser):
            def __init__(self):
                super().__init__(convert_charrefs=True)
                self.items = []

            def handle_starttag(self, tag, attrs):
                if tag == "img":
                    self.items.append(dict(attrs))

        routes = [line.strip() for line in ROUTES_FILE.read_text(encoding="utf-8").splitlines()
                  if line.strip() and not line.strip().startswith("#")]
        checked = 0
        for rel in routes:
            parser = Images()
            parser.feed((ROOT / rel).read_text(encoding="utf-8"))
            for image in parser.items:
                with self.subTest(page=rel, src=image.get("src")):
                    self.assertTrue(image.get("width") and image.get("height"),
                                    "image needs width and height attributes")
                    self.assertTrue((image.get("alt") or "").strip(), "alt text")
                    self.assertNotIn("http://", image.get("src", ""))
                checked += 1
        self.assertGreater(checked, 0, "kuch image to publish hoti hai")

    def test_no_page_ships_a_fixed_wide_element(self):
        """360px phone par kuch bhi screen se bahar ya fixed chaudi width ka nahi."""
        routes = [line.strip() for line in ROUTES_FILE.read_text(encoding="utf-8").splitlines()
                  if line.strip() and not line.strip().startswith("#")]
        for rel in routes:
            source = (ROOT / rel).read_text(encoding="utf-8")
            for style in re.findall(r'style="([^"]*)"', source):
                with self.subTest(page=rel, style=style):
                    self.assertNotRegex(style, r"width:\s*(?:3[6-9]\d|[4-9]\d\d|\d{4,})px")
                    self.assertNotRegex(style, r"min-width:\s*(?:2[8-9]\d|[3-9]\d\d|\d{4,})px")
                    self.assertNotIn("position: fixed", style)
            with self.subTest(page=rel):
                self.assertNotIn("<pre", source, "pre blocks phones par overflow karte hain")

    def test_phone_breakpoints_cover_620_and_400(self):
        self.assertRegex(self.css, r"@media\s*\(max-width:\s*620px\)")
        self.assertRegex(self.css, r"@media\s*\(max-width:\s*400px\)|@media\s*\(max-width:\s*380px\)")

    def test_row_cards_do_not_keep_a_height_basis_on_phones(self):
        """`.material-item` column ban jata hai — `flex: 1 1 260px` (width basis) wahan
        height basis ban ke khali jagah chhod deta hai, isliye reset zaroori hai."""
        block = re.search(r"@media\s*\(max-width:\s*720px\)\s*\{(.*?)\n\}", self.css, flags=re.S)
        self.assertIsNotNone(block, "720px block missing")
        self.assertIn(".material-main", block.group(1))
        self.assertRegex(block.group(1), r"\.material-main\s*\{\s*flex:\s*0 0 auto")

    def test_map_previews_go_full_width_on_phones(self):
        """620px se neeche map ka preview poori chaudai leta hai (kata hua nahi)."""
        blocks = re.findall(r"@media\s*\(max-width:\s*620px\)\s*\{(.*?)\n\}", self.css, flags=re.S)
        self.assertTrue(blocks, "620px block missing")
        joined = "\n".join(blocks)
        self.assertIn(".material-item.is-image", joined)
        self.assertIn("aspect-ratio", joined)


    def test_question_text_and_options_wrap_on_small_screens(self):
        self.assertRegex(self.css, r"\.question-stem\s*\{[^}]*white-space:\s*pre-line")
        self.assertRegex(self.css, r"\.option\s*\.opt-text\s*\{[^}]*overflow-wrap:\s*anywhere")
        self.assertIn("@media (max-width: 520px)", self.css)


if __name__ == "__main__":
    unittest.main()
