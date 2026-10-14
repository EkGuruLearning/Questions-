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

KINDS = {"theory", "practice", "test", "reference", "map"}
CONTENT_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".webp", ".svg"}


class SiteDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.site = json.loads(SITE.read_text(encoding="utf-8"))
        cls.materials = json.loads(MATERIALS.read_text(encoding="utf-8"))
        cls.subjects = json.loads(SUBJECTS.read_text(encoding="utf-8"))
        cls.manifest = json.loads(BANK_MANIFEST.read_text(encoding="utf-8"))
        cls.by_id = {subject["id"]: subject for subject in cls.site["subjects"]}

    def test_every_published_subject_has_a_real_route(self):
        for subject in self.site["subjects"]:
            with self.subTest(subject=subject["id"]):
                self.assertTrue((ROOT / subject["route"]).is_file(), subject["route"])
                if subject["material_route"]:
                    self.assertTrue((ROOT / subject["material_route"]).is_file())
                if subject["test_route"]:
                    self.assertTrue((ROOT / subject["test_route"]).is_file())
                self.assertEqual(subject["topics"] == [], not subject["has_test"], subject["id"])

    def test_geography_publishes_maps_and_no_question_bank(self):
        geo = self.by_id["rajasthan-geography"]
        self.assertTrue(geo["has_maps"])
        self.assertFalse(geo["has_test"])
        self.assertFalse(geo["has_material"])
        self.assertIsNone(geo["test_route"])
        self.assertNotIn("test", geo)
        kinds = {group["id"] for group in geo["groups"]}
        self.assertEqual(kinds, {"map"})
        maps = geo["groups"][0]["items"]
        self.assertGreaterEqual(len(maps), 4)
        for item in maps:
            self.assertTrue(item["repo_path"].startswith("content/rajasthan-geography/maps/"))
            self.assertEqual(item["file_type"], "PNG")

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
                self.assertTrue(topic["material"]["theory"], "every topic needs its theory PDF")
                self.assertTrue(topic["material"]["practice"], "every topic needs its practice booklet")

    def test_download_hashes_sizes_and_paths_are_real(self):
        seen = set()
        for subject in self.site["subjects"]:
            for group in subject["groups"]:
                self.assertIn(group["id"], KINDS)
                for item in group["items"]:
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
                self.assertIn(record["kind"], KINDS)
                self.assertIn(record["topic"], topic_ids | {None})

    def test_material_keeps_english_and_hindi_labels(self):
        for subject in self.site["subjects"]:
            for group in subject["groups"]:
                self.assertTrue(group["title_en"] and group["title_hi"], group["id"])
                for item in group["items"]:
                    self.assertTrue(item["title_en"].strip(), item["id"])
                    self.assertTrue(item["title_hi"].strip(), item["id"])

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
