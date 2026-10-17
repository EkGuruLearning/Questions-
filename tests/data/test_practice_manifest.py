"""Paper uploads, key provenance, safe paths and deterministic room manifests."""
import hashlib
import importlib.util
import json
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("build_practice", ROOT / "tools/build_practice.py")
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class PracticeManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)
        self.paper = self.root / "content/previous-year-papers/exam/2024/My-Paper.pdf"
        self.paper.parent.mkdir(parents=True)
        self.paper.write_bytes(b"%PDF-1.7\nscanned-paper-placeholder-for-discovery-test")

    def metadata(self, **changes):
        doc = {"schema_version": 1, "question_count": 3,
               "paper_sha256": hashlib.sha256(self.paper.read_bytes()).hexdigest(), **changes}
        metadata = self.root / "data/practice/papers/exam/2024/My-Paper.paper.json"
        metadata.parent.mkdir(parents=True, exist_ok=True)
        metadata.write_text(json.dumps(doc), encoding="utf-8")

    def test_scanned_pdf_needs_no_ocr_or_manual_catalogue_registration(self):
        result = builder.generate(self.root)
        self.assertEqual(len(result["papers"]), 1)
        paper = result["papers"][0]
        self.assertIsNone(paper["question_count"])
        self.assertEqual(paper["answer_key"], {})
        self.assertIn("unscored", paper["key_label"])
        self.assertEqual(paper["year"], "2024")
        self.assertEqual(builder.generate(self.root), result)

    def test_key_pdfs_never_become_question_papers(self):
        self.paper.with_name("My-Paper-Answer-Key.pdf").write_bytes(b"%PDF-key")
        self.assertEqual(len(builder.generate(self.root)["papers"]), 1)

    def test_nonstandard_referenced_key_is_not_discovered_as_a_test(self):
        key = self.paper.with_name("unusual.pdf")
        key.write_bytes(b"%PDF-key")
        self.metadata(key_pdf=key.relative_to(self.root).as_posix(), answer_key={"1": "A"})
        result = builder.generate(self.root)
        self.assertEqual(len(result["papers"]), 1)
        self.assertEqual(result["papers"][0]["answer_key"], {"1": ["A"]})

    def test_multiple_accepted_options_and_dropped_questions_are_preserved(self):
        self.metadata(answer_key={"1": ["B", "A"], "2": "DROP"})
        result = builder.generate(self.root)["papers"][0]
        self.assertEqual(result["answer_key"], {"1": ["A", "B"], "2": "DROP"})

    def test_changed_question_paper_cannot_silently_reuse_an_old_answer_key(self):
        self.metadata(answer_key={"1": "A"})
        original = builder.generate(self.root)
        self.paper.write_bytes(b"%PDF-new-question-order")
        with self.assertRaisesRegex(ValueError, "paper_sha256"):
            builder.generate(self.root)
        self.assertEqual(len(original["papers"]), 1)

    def test_changed_key_pdf_requires_review_before_publishing(self):
        key = self.paper.with_name("Answer-Key.pdf")
        key.write_bytes(b"%PDF-old-key")
        self.metadata(answer_key={"1": "A"}, key_pdf=key.relative_to(self.root).as_posix(),
                      key_sha256=hashlib.sha256(key.read_bytes()).hexdigest())
        builder.generate(self.root)
        key.write_bytes(b"%PDF-new-final-key")
        with self.assertRaisesRegex(ValueError, "key_pdf hash changed"):
            builder.generate(self.root)

    def test_answer_key_cannot_escape_the_public_paper_folder(self):
        outside = self.root / "private.pdf"
        outside.write_bytes(b"%PDF-private")
        for value in ("private.pdf", "../private.pdf", str(outside), "https://evil.test/key.pdf", "content\\private.pdf"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.metadata(key_pdf=value)
                builder.generate(self.root)

    def test_malformed_key_and_out_of_range_questions_fail_the_build(self):
        for key in ({"4": "A"}, {"0": "A"}, {"1": "Z"}, {"1": []}, {"1": ["A", "A"]}):
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.metadata(answer_key=key)
                builder.generate(self.root)

    def test_skip_option_cannot_be_a_correct_key_entry(self):
        self.metadata(options_count=5, skip_option="E", answer_key={"1": "E"})
        with self.assertRaises(ValueError):
            builder.generate(self.root)

    def test_paper_update_invalidates_the_resume_fingerprint_even_without_a_key(self):
        before = builder.generate(self.root)["papers"][0]
        self.paper.write_bytes(b"%PDF-other-scanned-paper")
        after = builder.generate(self.root)["papers"][0]
        self.assertEqual(before["id"], after["id"])
        self.assertNotEqual(before["fingerprint"], after["fingerprint"])

    def test_missing_paper_for_metadata_and_duplicate_ids_fail_early(self):
        self.metadata()
        orphan = self.root / "data/practice/papers/exam/2024/orphan.paper.json"
        orphan.write_text('{"schema_version":1}')
        with self.assertRaisesRegex(ValueError, "matching paper PDF"):
            builder.generate(self.root)
        orphan.unlink()
        self.metadata(id="same-id")
        another = self.paper.with_name("Another.pdf")
        another.write_bytes(b"%PDF-other")
        (self.root / "data/practice/papers/exam/2024/Another.paper.json").write_text('{"schema_version":1,"id":"same-id"}')
        with self.assertRaisesRegex(ValueError, "duplicate"):
            builder.generate(self.root)

    def test_repository_manifest_is_current(self):
        expected = builder.generate(ROOT)
        actual = json.loads((ROOT / "data/practice/manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(expected, actual)
        all_pdfs = [p for p in (ROOT / "content/previous-year-papers").rglob("*.pdf") if not builder.KEY_NAME.search(p.stem)]
        self.assertEqual(len(expected["papers"]), len(all_pdfs))


if __name__ == "__main__":
    unittest.main()
