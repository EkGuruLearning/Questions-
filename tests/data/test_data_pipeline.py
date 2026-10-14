import hashlib
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
BANK = ROOT / "data/banks/cn/cn_questions.json"
MANIFEST = ROOT / "data/banks/cn/manifest.json"
EVIDENCE = ROOT / "data/sources/official_paper_key_evidence.json"

PUBLIC_FIELDS = {
    "id", "subject_id", "topic_id", "topic_name", "subtopic", "stem_en", "stem_hi",
    "options", "answer_option_id", "explanation_en", "explanation_hi", "nukta_en", "nukta_hi",
    "question_style", "difficulty", "source_type", "verification_status", "exam_tags",
}
INTERNAL_FIELDS = {"answer_verified_by", "why_wrong", "duplicate_group", "provenance_note", "source_id"}


class GeneratedDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank_raw = BANK.read_bytes()
        cls.bank = json.loads(cls.bank_raw)
        cls.questions = cls.bank["questions"]
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.evidence = json.loads(EVIDENCE.read_text(encoding="utf-8"))

    def test_canonical_build_identity_and_counts_are_current(self):
        sha = hashlib.sha256(self.bank_raw).hexdigest()
        build_id = "cn-" + sha[:16]
        self.assertEqual(self.bank["schema_version"], 2)
        self.assertEqual(self.manifest["canonical_sha256"], sha)
        self.assertEqual(self.manifest["bank_build_id"], build_id)
        self.assertEqual(self.manifest["question_count"], len(self.questions))
        self.assertEqual(self.manifest["published_question_count"], len(self.questions) - 2)
        self.assertEqual(self.manifest["review_only_excluded_count"], 2)

    def test_question_ids_options_and_source_references_are_stable(self):
        ids = [question["id"] for question in self.questions]
        self.assertEqual(len(ids), len(set(ids)))
        for question in self.questions:
            with self.subTest(question=question["id"]):
                self.assertEqual(question["subject_id"], "cn")
                self.assertEqual(question["option_ids"], ["A", "B", "C", "D"])
                self.assertEqual(question["answer_option_id"], question["correct_option"])
                self.assertEqual(len(question["options_en"]), 4)
                self.assertEqual(len(question["options_hi"]), 4)
                expected = "src-" + hashlib.sha256(question["source_url_or_file"].encode("utf-8")).hexdigest()[:12]
                self.assertEqual(question["source_id"], expected)

    def test_official_evidence_gate_has_no_unsupported_records(self):
        official_ids = set()
        for item in self.evidence.get("records", []):
            official_ids.update(item["question_ids"])
        official = [q for q in self.questions if q["verification_status"] == "paper_and_key_checked"]
        self.assertEqual({q["id"] for q in official}, official_ids)
        self.assertEqual(len(official), 0)
        self.assertEqual(sum(q["source_type"] == "verified_official_pyq" for q in self.questions), 0)

    def test_topic_chunks_partition_the_published_bank(self):
        seen = []
        for chunk in self.manifest["topics"]:
            path = ROOT / chunk["file"]
            raw = path.read_bytes()
            with self.subTest(chunk=chunk["topic_id"]):
                self.assertTrue(chunk["file"].startswith("data/banks/cn/"))
                self.assertEqual(hashlib.sha256(raw).hexdigest(), chunk["sha256"])
                self.assertEqual(len(raw), chunk["bytes"])
                rows = json.loads(raw)
                self.assertEqual(len(rows), chunk["published_question_count"])
                self.assertTrue(all(row["topic_id"] == chunk["topic_id"] for row in rows))
                seen.extend(row["id"] for row in rows)
        expected = {q["id"] for q in self.questions if q["verification_status"] not in ("disputed", "pending_review")}
        self.assertEqual(len(seen), len(set(seen)))
        self.assertEqual(set(seen), expected)

    def test_browser_chunks_carry_no_internal_review_notes(self):
        chunk = json.loads((ROOT / self.manifest["topics"][0]["file"]).read_text(encoding="utf-8"))
        self.assertTrue(chunk)
        for record in chunk:
            with self.subTest(question=record["id"]):
                self.assertEqual(set(record), PUBLIC_FIELDS)
                self.assertEqual(set(record) & INTERNAL_FIELDS, set())
                self.assertEqual(len(record["options"]), 4)
                self.assertIn(record["answer_option_id"], {option["id"] for option in record["options"]})
                self.assertTrue(record["stem_en"].strip())

    def test_no_stale_topic_chunks_are_left_behind(self):
        expected = {chunk["file"].rsplit("/", 1)[-1] for chunk in self.manifest["topics"]}
        found = {path.name for path in (ROOT / "data/banks/cn").glob("T0*.min.json")}
        self.assertEqual(found, expected)

    def test_preserved_originals_stay_in_the_maintainer_area(self):
        archive = ROOT / "maintainer/archive/pre-audit-2026-10-14"
        self.assertTrue((archive / "index.html.snapshot").is_file())
        self.assertEqual(list(archive.rglob("*.html")), [], "archived HTML is only kept as non-runnable snapshots")
        for number in range(1, 8):
            legacy = ROOT / "maintainer/computer-network/legacy-apps/Online Quiz" / f"Topic {number} - Online Quiz & Exam (by PRAKASH - EkGuru).html"
            self.assertTrue(legacy.is_file(), legacy.as_posix())
        self.assertFalse((ROOT / "Computer Network").exists())

    def test_only_student_material_lives_under_content(self):
        suffixes = {".pdf", ".png", ".jpg", ".jpeg", ".webp", ".svg"}
        for path in (ROOT / "content").rglob("*"):
            if path.is_file():
                with self.subTest(path=path.as_posix()):
                    self.assertIn(path.suffix.lower(), suffixes)


if __name__ == "__main__":
    unittest.main()
