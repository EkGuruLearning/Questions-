import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import build_catalog  # noqa: E402


class PortalResourceSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.available = set(build_catalog.repo_paths())
        cls.valid_record = {
            "id": "geo-test-source-audit",
            "subject_id": "rajasthan-geography",
            "title": "Test source audit",
            "category": "Audit/QA",
            "repo_path": "Rajasthan Geography Maps/SOURCE_AUDIT.md",
            "source_status": "Test record only; not a boundary claim.",
            "source_status_label": "Source audit · review only",
            "source_status_state": "warning",
            "notes": "Used to test catalogue validation without writing to any source file.",
        }

    def test_empty_checked_in_registry_is_a_valid_source(self):
        source = json.loads((ROOT / "data/catalog/portal_resources.json").read_text(encoding="utf-8"))
        self.assertEqual(source["schema_version"], 1)
        self.assertEqual(build_catalog.make_portal_resources(source, self.available), [])

    def test_registered_resource_receives_repository_hash_and_encoded_url(self):
        item, = build_catalog.make_portal_resources({"schema_version": 1, "resources": [self.valid_record]}, self.available)
        self.assertEqual(item["id"], self.valid_record["id"])
        self.assertEqual(item["url"], "Rajasthan%20Geography%20Maps/SOURCE_AUDIT.md")
        self.assertEqual(item["sha256"], build_catalog.sha256(ROOT / self.valid_record["repo_path"]))
        self.assertEqual(item["source_status_state"], "warning")

    def test_bad_paths_subjects_and_duplicate_ids_are_rejected(self):
        missing = {**self.valid_record, "repo_path": "Rajasthan Geography Maps/not-present.csv"}
        with self.assertRaises(FileNotFoundError):
            build_catalog.make_portal_resources({"schema_version": 1, "resources": [missing]}, self.available)

        unsupported = {**self.valid_record, "subject_id": "future-subject"}
        with self.assertRaises(ValueError):
            build_catalog.make_portal_resources({"schema_version": 1, "resources": [unsupported]}, self.available)

        duplicate = [self.valid_record, {**self.valid_record, "title": "Another title"}]
        with self.assertRaises(ValueError):
            build_catalog.make_portal_resources({"schema_version": 1, "resources": duplicate}, self.available)

    def test_geography_registry_keeps_the_two_audited_roots_distinct(self):
        misplaced = {**self.valid_record, "repo_path": "Geography/Map/Rajasthan/SOURCE_AUDIT.md"}
        item, = build_catalog.make_portal_resources({"schema_version": 1, "resources": [misplaced]}, self.available)
        self.assertTrue(item["repo_path"].startswith("Geography/Map/Rajasthan/"))
        self.assertNotEqual(item["repo_path"].split("/")[0], "Rajasthan Geography Maps")

    def test_new_geography_map_requires_explicit_alt_and_warning_status(self):
        image = {
            **self.valid_record,
            "id": "geo-map-test-preview",
            "title": "Test map image",
            "category": "Map/Atlas",
            "repo_path": "Geography/Map/Rajasthan/preview.webp",
            "source_status_state": "warning",
        }
        with self.assertRaises(ValueError):
            build_catalog.make_portal_resources({"schema_version": 1, "resources": [image]}, self.available)
        image["image_alt"] = "Accurate description of this separate reference preview; not a validated final GIS map."
        item, = build_catalog.make_portal_resources({"schema_version": 1, "resources": [image]}, self.available)
        self.assertEqual(item["image_alt"], image["image_alt"])

    def test_terminal_reader_explains_website_paths_and_merge_check(self):
        result = subprocess.run(
            [sys.executable, "tools/read_structure.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("Computer Network/Topics/T01/", result.stdout)
        self.assertIn("data/catalog/portal_resources.json", result.stdout)
        self.assertIn("python3 tools/read_structure.py --check", result.stdout)
        self.assertIn("Geography/Map/Rajasthan/", result.stdout)


if __name__ == "__main__":
    unittest.main()
