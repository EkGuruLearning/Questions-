import copy
import hashlib
import json
import pathlib
import sys
import tempfile
import unittest
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import build_quizzes

class AllSubjectCBT(unittest.TestCase):
    def test_committed_generated_banks_are_current_and_hashed(self):
        files = build_quizzes.build(ROOT)
        for name, content in files.items():
            self.assertEqual((ROOT / name).read_text(encoding="utf-8"), content, name)
            if name.endswith(".min.json"):
                self.assertEqual(hashlib.sha256(content.encode()).hexdigest()[:12], name.rsplit(".", 3)[1])
        self.assertLess(len(files["data/quizzes/manifest.json"].encode()), 2000)
        self.assertLess(len(files["data/banks/cn/topics.json"].encode()), 6000)
        self.assertNotIn("material", files["data/banks/cn/topics.json"])

    def test_550_tests_across_50_subjects_are_sharded_without_player_or_api_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            for n in range(550):
                subject = f"subject-{n % 50}"
                target = root / f"data/tests/{subject}/test-{n}.test.json"
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps({"schema_version": 1, "id": f"test-{n}", "title": f"Test {n}", "questions": [{"text": "A real author-supplied question", "options": ["One", "Two"], "answer": ["A"]}]}))
            files = build_quizzes.build(root)
            manifest = json.loads(files["data/quizzes/manifest.json"])
            self.assertEqual(manifest["test_count"], 550)
            self.assertEqual(len(manifest["subjects"]), 50)
            self.assertLess(len(files["data/quizzes/manifest.json"].encode()), 12000)
            for subject in manifest["subjects"]:
                index = json.loads(files[subject["file"]])
                self.assertEqual(len(index["tests"]), 11)
                self.assertLess(len(files[subject["file"]].encode()), 5000)
                self.assertNotIn('"questions"', files[subject["file"]])

    def test_invalid_keys_numeric_ranges_paths_counts_and_marks_are_rejected(self):
        document = {"schema_version": 1, "id": "test", "title": "A test", "questions": [{"text": "Prompt", "options": ["One", "Two"], "answer": ["A"]}]}
        invalid = []
        for patch in [{"answer": ["X"]}, {"answer": ["A", "A"]}, {"type": "other"}, {"marks": float("nan")}, {"marks": True}, {"skip_option": "A"}, {"image": "../secret.png"}, {"type": "numeric", "answer_range": [2, 1]}]:
            doc = copy.deepcopy(document); doc["questions"][0].update(patch); invalid.append(doc)
        invalid += [{**document, "duration_minutes": 361}, {**document, "questions": []}, {**document, "source": {"pdf": "../secret.pdf", "sha256": "bad"}}]
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp); path = root / "data/tests/subject/test.test.json"; path.parent.mkdir(parents=True)
            for doc in invalid:
                with self.subTest(doc=doc):
                    path.write_text(json.dumps(doc))
                    with self.assertRaises((ValueError, TypeError)): build_quizzes.build(root)

    def test_question_image_dimensions_are_bounded_and_not_invented(self):
        png_header = b"\x89PNG\r\n\x1a\n" + b"\x00\x00\x00\rIHDR" + (1200).to_bytes(4, "big") + (800).to_bytes(4, "big")
        self.assertEqual(build_quizzes.image_size(png_header), [1200, 800])
        with self.assertRaises(ValueError): build_quizzes.image_size(png_header[:16] + (9000).to_bytes(4, "big") + (800).to_bytes(4, "big"))
        with self.assertRaises(ValueError): build_quizzes.image_size(b"not a picture")

    def test_six_imported_pdfs_match_pinned_mirror_hashes_with_honest_labels(self):
        sources = json.loads((ROOT / "data/catalog/imported-papers.json").read_text())
        self.assertEqual(len(sources["papers"]), 6)
        for record in sources["papers"]:
            content = (ROOT / record["file"]).read_bytes()
            self.assertTrue(content.startswith(b"%PDF-"))
            self.assertEqual(len(content), record["bytes"])
            self.assertEqual(hashlib.sha256(content).hexdigest(), record["sha256"])
            self.assertEqual(hashlib.sha1(f"blob {len(content)}\0".encode() + content).hexdigest(), record["git_blob"])
            self.assertIn(record["commit"], record["source_url"])
            self.assertFalse(record["official_bytes_independently_verified"])
            self.assertTrue(record["render_review"]["every_page_rendered"])
            self.assertEqual(record["render_review"]["embedded_active_markers_detected"], [])
        manifest = json.loads((ROOT / "data/practice/manifest.json").read_text())
        for record in sources["papers"]:
            paper = next(p for p in manifest["papers"] if p["pdf"] == record["file"])
            self.assertTrue(paper["reader_only"])
            self.assertEqual(paper["answer_key"], {})
            self.assertNotIn("cbt_test", paper)

if __name__ == "__main__": unittest.main()
