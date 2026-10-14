import hashlib
import json
import pathlib
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
                self.assertTrue((ROOT / subject["route"]).is_file(), subject["route"])
                self.assertGreaterEqual(subject["folder_count"], 1)
                self.assertTrue(subject["tree"]["folders"], "subject page needs at least one folder tile")
                labels = self.subjects["subjects"]
                configured = [item for item in labels if item["id"] == subject["id"]][0]["folders"]
                self.assertEqual({node["path"] for node in walk(subject["tree"]) if node["path"]}, set(configured))

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

    def test_every_content_file_is_registered_and_every_record_resolves(self):
        registered = [item["file"] for item in self.materials["materials"]]
        self.assertEqual(len(registered), len(set(registered)), "duplicate registration")
        on_disk = sorted(
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "content").rglob("*")
            if path.is_file() and not path.name.startswith(".") and path.suffix.lower() in CONTENT_SUFFIXES
        )
        self.assertEqual(sorted(registered), on_disk)
        subject_ids = {subject["id"] for subject in self.subjects["subjects"]}
        topic_ids = {"T%02d" % number for number in range(1, 8)}
        for record in self.materials["materials"]:
            with self.subTest(record=record["file"]):
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
