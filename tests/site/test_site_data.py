import hashlib
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITE = ROOT / "data/site.json"
MATERIALS = ROOT / "data/catalog/materials.json"
SUBJECTS = ROOT / "data/catalog/subjects.json"
ROUTES = ROOT / "data/catalog/site-routes.txt"
BANK_MANIFEST = ROOT / "data/banks/cn/manifest.json"

CONTENT_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".webp", ".svg"}
FOLDER_FIELDS = ("title_en", "title_hi", "icon", "file_count", "total_bytes", "file_types")


def walk(node):
    yield node
    for child in node["folders"]:
        yield from walk(child)


class SiteDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.site = json.loads(SITE.read_text(encoding="utf-8"))
        cls.materials = json.loads(MATERIALS.read_text(encoding="utf-8"))
        cls.subjects = json.loads(SUBJECTS.read_text(encoding="utf-8"))
        cls.manifest = json.loads(BANK_MANIFEST.read_text(encoding="utf-8"))
        cls.by_id = {subject["id"]: subject for subject in cls.site["subjects"]}

    def test_every_subject_has_real_routes_and_a_folder_tree(self):
        for subject in self.site["subjects"]:
            with self.subTest(subject=subject["id"]):
                route = subject["route"].split("?")[0]
                self.assertTrue((ROOT / route).is_file(), subject["route"])
                self.assertGreaterEqual(subject["folder_count"], 1, "subject needs at least one folder")
                self.assertTrue(subject["tree"]["folders"], "subject page needs at least one folder tile")
                configured = {item["id"]: item for item in self.subjects["subjects"]}[subject["id"]]["folders"]
                on_disk = {
                    path.relative_to(ROOT / "content" / subject["id"]).as_posix()
                    for path in (ROOT / "content" / subject["id"]).rglob("*")
                    if path.is_dir() and not path.name.startswith(".")
                }
                # every folder on disk shows up, and nothing extra is invented
                self.assertEqual(on_disk - {""}, {node["path"] for node in walk(subject["tree"]) if node["path"]})
                self.assertTrue(set(configured).issubset(on_disk | {""}), sorted(set(configured) - on_disk))

    def test_new_material_needs_no_code_change(self):
        """Naya folder/file daalo -> build chalao -> site par aa jata hai (naam se label ban ke)."""
        import subprocess

        folder = ROOT / "content" / "reasoning" / "practice" / "series"
        folder.mkdir(parents=True, exist_ok=True)
        sample = folder / "Seating-Arrangement-Basics.pdf"
        sample.write_bytes(b"%PDF-1.4\n% test fixture\n")
        try:
            result = subprocess.run([sys.executable, "tools/build_catalog.py"], cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            built = json.loads(SITE.read_text(encoding="utf-8"))
            reasoning = {item["id"]: item for item in built["subjects"]}["reasoning"]
            practice = next(node for node in walk(reasoning["tree"]) if node["path"] == "practice")
            series = next(node for node in walk(reasoning["tree"]) if node["path"] == "practice/series")
            self.assertEqual(series["title_en"], "Series", "folder label should come from its own name")
            self.assertEqual(series["files"][0]["title_en"], "Seating Arrangement Basics")
            self.assertEqual(series["files"][0]["file_type"], "PDF")
            self.assertEqual(practice["file_count"], 1, "parent folder counts the new file")
        finally:
            sample.unlink(missing_ok=True)
            for path in sorted(folder.parent.rglob("*"), key=lambda item: len(item.parts), reverse=True):
                if path.is_dir() and not any(path.iterdir()):
                    path.rmdir()
            subprocess.run([sys.executable, "tools/build_catalog.py"], cwd=ROOT, capture_output=True)

    def test_declared_empty_folders_are_published_as_empty(self):
        by_id = {item["id"]: item for item in self.site["subjects"]}
        pyq = by_id["previous-year-papers"]
        self.assertEqual(
            [folder["path"] for folder in pyq["tree"]["folders"]],
            ["ia", "sci", "computer-operator", "system-assistant", "dsssb", "ssc", "net", "rpsc"],
        )
        for folder in pyq["tree"]["folders"]:
            with self.subTest(folder=folder["path"]):
                self.assertTrue(folder["empty"])
                self.assertEqual(folder["file_count"], 0)
                self.assertTrue(folder["title_en"].strip())
        reasoning = by_id["reasoning"]
        self.assertEqual([folder["path"] for folder in reasoning["tree"]["folders"]],
                         ["theory", "practice", "answers", "tests"])
        self.assertTrue(all(folder["empty"] for folder in reasoning["tree"]["folders"]))

    def test_registry_entries_must_exist_but_extra_files_are_fine(self):
        registered = [item["file"] for item in self.materials["materials"]]
        on_disk = {
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "content").rglob("*")
            if path.is_file() and not path.name.startswith(".")
        }
        # registry is for nice titles/SEO: every entry must exist, extras are allowed
        self.assertEqual(set(registered) - on_disk, set())
        self.assertLessEqual(set(registered), on_disk)
        for item in self.site["subjects"]:
            for record in item["files"]:
                self.assertIn(record["repo_path"], on_disk)

    def test_folder_tree_mirrors_the_content_folder_on_disk(self):
        for subject in self.site["subjects"]:
            subject_dir = ROOT / "content" / subject["id"]
            on_disk = {
                path.relative_to(subject_dir).parent.as_posix()
                for path in subject_dir.rglob("*")
                if path.is_file() and path.suffix.lower() in CONTENT_SUFFIXES
            }
            on_disk.discard(".")
            in_tree = {node["path"] for node in walk(subject["tree"]) if node["path"]}
            # every leaf folder with files exists in the tree; parent nodes are included too
            with self.subTest(subject=subject["id"]):
                self.assertTrue(on_disk.issubset(in_tree), f"folders missing from tree: {sorted(on_disk - in_tree)}")
                for folder in on_disk:
                    node = next(item for item in walk(subject["tree"]) if item["path"] == folder)
                    self.assertTrue(node["files"], f"{folder} should list its files")

    def test_folders_carry_bilingual_labels_and_live_counts(self):
        for subject in self.site["subjects"]:
            for node in walk(subject["tree"]):
                if not node["path"]:
                    continue
                with self.subTest(folder=node["path"]):
                    for field in FOLDER_FIELDS:
                        self.assertIn(field, node)
                    self.assertTrue(node["title_en"].strip(), node["path"])
                    self.assertTrue(node["title_hi"].strip(), node["path"])
                    self.assertTrue(node["icon"].strip(), node["path"])
                    self.assertEqual(node["file_count"], len(node["files"]) + sum(child["file_count"] for child in node["folders"]))
                    self.assertEqual(node["total_bytes"], sum(item["bytes"] for item in node["files"])
                                     + sum(child["total_bytes"] for child in node["folders"]))
                    for item in node["files"]:
                        self.assertEqual(item["folder"], node["path"])

    def test_auto_and_curated_labels_are_not_confused(self):
        by_id = {item["id"]: item for item in self.site["subjects"]}
        self.assertFalse(by_id["computer-network"]["auto"])
        self.assertFalse(by_id["previous-year-papers"]["auto"])
        self.assertTrue(by_id["previous-year-papers"]["tree"]["folders"][0]["auto"] is False)
        for subject in self.site["subjects"]:
            for node in walk(subject["tree"]):
                if node["path"] == "":
                    continue
                self.assertTrue(node["title_en"].strip(), node["path"])
                self.assertTrue(node["title_hi"].strip(), node["path"])
                self.assertTrue(node["icon"].strip(), node["path"])

    def test_computer_network_folder_shape(self):
        cn = self.by_id["computer-network"]
        self.assertEqual([folder["path"] for folder in cn["tree"]["folders"]],
                         ["theory", "practice", "answers", "tests", "reference"])
        counts = {folder["path"]: folder["file_count"] for folder in cn["tree"]["folders"]}
        self.assertEqual(counts, {"theory": 8, "practice": 7, "answers": 5, "tests": 11, "reference": 1})
        self.assertEqual(cn["file_count"], 32)
        self.assertEqual([folder["title_en"] for folder in cn["tree"]["folders"]],
                         ["Theory", "Practice questions", "Answers & explanations", "Tests", "Reference book"])

    def test_geography_nests_map_then_rajasthan(self):
        geo = self.by_id["rajasthan-geography"]
        self.assertTrue(geo["has_maps"])
        self.assertFalse(geo["has_test"])
        self.assertIsNone(geo["test_route"])
        map_folder, = geo["tree"]["folders"]
        self.assertEqual((map_folder["path"], map_folder["title_en"]), ("map", "Map"))
        rajasthan, = map_folder["folders"]
        self.assertEqual((rajasthan["path"], rajasthan["title_en"]), ("map/rajasthan", "Rajasthan"))
        self.assertEqual(rajasthan["file_count"], 6)
        for item in rajasthan["files"]:
            self.assertTrue(item["repo_path"].startswith("content/rajasthan-geography/map/rajasthan/"))
            self.assertEqual(item["file_type"], "PNG")

    def test_download_hashes_sizes_and_paths_are_real(self):
        seen = set()
        for subject in self.site["subjects"]:
            for item in subject["files"]:
                with self.subTest(item=item["id"]):
                    self.assertNotIn(item["repo_path"], seen)
                    seen.add(item["repo_path"])
                    self.assertTrue(item["repo_path"].startswith("content/"), item["repo_path"])
                    path = ROOT / item["repo_path"]
                    self.assertTrue(path.is_file(), item["repo_path"])
                    raw = path.read_bytes()
                    self.assertEqual(len(raw), item["bytes"])
                    self.assertEqual(hashlib.sha256(raw).hexdigest(), item["sha256"])
                    self.assertFalse(item["title_en"].lower().endswith(".md"))
                    if item["file_type"] in {"PNG", "JPG", "JPEG", "WEBP", "SVG"}:
                        self.assertTrue(item["thumb_url"], f"{item['repo_path']} needs a light preview")
                        thumb = ROOT / item["thumb_url"]
                        self.assertTrue(thumb.is_file(), item["thumb_url"])
                        self.assertLess(thumb.stat().st_size, item["bytes"])
                        self.assertEqual(item["thumb_bytes"], thumb.stat().st_size)
                    else:
                        self.assertIsNone(item["thumb_url"])

    def test_registry_entries_resolve_to_real_files(self):
        registered = [item["file"] for item in self.materials["materials"]]
        self.assertEqual(len(registered), len(set(registered)), "duplicate registration")
        subject_ids = {subject["id"] for subject in self.subjects["subjects"]}
        topic_ids = {"T%02d" % number for number in range(1, 8)}
        for record in self.materials["materials"]:
            with self.subTest(record=record["file"]):
                self.assertTrue((ROOT / record["file"]).is_file(), record["file"])
                self.assertIn(record["subject"], subject_ids)
                self.assertIn(record["topic"], topic_ids | {None})
                self.assertTrue(record["title_en"].strip())
                self.assertTrue(record["title_hi"].strip())

    def test_computer_network_topics_match_the_question_bank(self):
        cn = self.by_id["computer-network"]
        self.assertTrue(cn["has_test"] and cn["has_material"])
        manifest_topics = {topic["topic_id"]: topic for topic in self.manifest["topics"]}
        self.assertEqual([topic["id"] for topic in cn["topics"]], sorted(manifest_topics))
        for topic in cn["topics"]:
            chunk = manifest_topics[topic["id"]]
            with self.subTest(topic=topic["id"]):
                self.assertEqual(topic["title_en"], chunk["topic_name"])
                self.assertEqual(topic["question_count"], chunk["published_question_count"])
                self.assertEqual(sum(section["count"] for section in topic["sections"]), topic["question_count"])
                self.assertTrue(topic["material"]["theory"], "every topic needs a theory PDF")
                self.assertTrue(topic["material"]["practice"] if topic["id"] != "T07" else True)
                self.assertEqual(topic["material"]["theory"][0]["folder"], "theory")
                for item in topic["material"]["practice"]:
                    self.assertEqual(item["folder"], "practice")

    def test_pictures_carry_real_seo_text(self):
        pictures = [item for subject in self.site["subjects"] for item in subject["files"]
                    if item["file_type"] in {"PNG", "JPG", "JPEG", "WEBP", "SVG"}]
        self.assertTrue(pictures)
        for item in pictures:
            with self.subTest(item=item["repo_path"]):
                for field in ("alt_en", "alt_hi", "description_en", "description_hi"):
                    text = item[field].strip()
                    self.assertTrue(text, f"{item['repo_path']} needs {field}")
                    self.assertNotIn(item["file_name"], text, "alt/description must describe the map, not repeat the file name")
                self.assertLessEqual(len(item["alt_en"]), 200)
                self.assertLessEqual(len(item["alt_hi"]), 200)
                self.assertGreaterEqual(len(item["description_en"]), 120)
                self.assertGreaterEqual(len(item["description_hi"]), 120)
        maps = [item for item in pictures if item["subject"] == "rajasthan-geography"]
        joined = " ".join(item["description_en"] + item["description_hi"] + item["alt_hi"] for item in maps)
        for needle in ("41", "36", "सीमावर्ती", "पाकिस्तान"):
            self.assertIn(needle, joined, f"map descriptions should mention {needle}")
        for district in ("बाड़मेर", "बीकानेर", "श्रीगंगानगर", "जैसलमेर", "फलौदी"):
            self.assertIn(district, joined, f"Pakistan-border districts should be named: {district}")
        a4 = {item["file_name"]: item for item in maps}
        portrait = a4["Rajasthan-Border-Districts-A4-Portrait.png"]
        landscape = a4["Rajasthan-Border-Districts-A4-Landscape.png"]
        self.assertIn("210 × 297", portrait["description_hi"])
        self.assertIn("297 × 210", landscape["description_hi"])
        self.assertIn("portrait", portrait["alt_en"].lower())
        self.assertIn("landscape", landscape["alt_en"].lower())

    def test_image_previews_are_current_and_light(self):
        thumbs = json.loads((ROOT / "data/thumbs/manifest.json").read_text(encoding="utf-8"))["thumbs"]
        images = [item for subject in self.site["subjects"] for item in subject["files"]
                  if item["file_type"] in {"PNG", "JPG", "JPEG", "WEBP", "SVG"}]
        self.assertTrue(images, "the site should publish at least one picture")
        self.assertEqual({item["repo_path"] for item in images}, set(thumbs))
        for item in images:
            entry = thumbs[item["repo_path"]]
            with self.subTest(item=item["repo_path"]):
                digest = hashlib.sha256((ROOT / item["repo_path"]).read_bytes()).hexdigest()
                self.assertEqual(entry["sha256"], digest, "preview is stale — run tools/build_thumbs.py")
                self.assertEqual(entry["thumb"], item["thumb_url"])
                self.assertLess(entry["bytes"], 600 * 1024, "previews must stay small enough for phones")

    def test_published_route_list_covers_every_html_page(self):
        listed = {
            line.strip()
            for line in ROUTES.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        }
        for route in listed:
            self.assertTrue((ROOT / route).is_file(), route)
        on_disk = {
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*.html")
            if path.relative_to(ROOT).parts[0] not in {"maintainer", "tools", "tests", ".git"}
        }
        self.assertEqual(on_disk - listed, set(), "every published page must be listed in data/catalog/site-routes.txt")


if __name__ == "__main__":
    unittest.main()
