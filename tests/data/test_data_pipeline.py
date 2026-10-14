import hashlib
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]


class GeneratedDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank_path = ROOT / "Computer Network/data/cn_questions.json"
        cls.bank_raw = cls.bank_path.read_bytes()
        cls.bank = json.loads(cls.bank_raw)
        cls.questions = cls.bank["questions"]
        cls.manifest = json.loads((ROOT / "assets/banks/cn/manifest.json").read_text(encoding="utf-8"))
        cls.catalog = json.loads((ROOT / "assets/catalog.min.json").read_text(encoding="utf-8"))
        cls.sources = json.loads((ROOT / "assets/source-register.min.json").read_text(encoding="utf-8"))
        cls.public_bank = json.loads((ROOT / "assets/cn-questions.min.json").read_text(encoding="utf-8"))
        cls.evidence = json.loads((ROOT / "data/sources/official_paper_key_evidence.json").read_text(encoding="utf-8"))

    def test_canonical_build_identity_and_counts_are_current(self):
        sha = hashlib.sha256(self.bank_raw).hexdigest()
        build_id = "cn-" + sha[:16]
        self.assertEqual(self.bank["schema_version"], 2)
        self.assertEqual(self.manifest["canonical_sha256"], sha)
        self.assertEqual(self.manifest["bank_build_id"], build_id)
        self.assertEqual(self.catalog["bank_build_id"], build_id)
        self.assertEqual(self.manifest["question_count"], len(self.questions))
        self.assertEqual(sum(self.manifest["topics"][i]["record_count"] for i in range(len(self.manifest["topics"]))), len(self.questions))

    def test_question_ids_options_keys_and_source_ids_are_stable(self):
        ids = [question["id"] for question in self.questions]
        self.assertEqual(len(ids), len(set(ids)))
        for question in self.questions:
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

    def test_public_payloads_omit_internal_notes_and_preserve_source_references(self):
        ids = {q["id"] for q in self.questions if q["verification_status"] not in ("disputed", "pending_review")}
        public_ids = {q["id"] for q in self.public_bank}
        self.assertSetEqual(ids, public_ids)
        source_ids = {item["id"] for item in self.sources["records"]}
        self.assertTrue(all(q["source_id"] in source_ids for q in self.public_bank))
        for question in self.public_bank:
            self.assertNotIn("answer_verified_by", question)
            self.assertNotIn("why_wrong", question)
            self.assertNotIn("duplicate_group", question)

    def test_only_cn_is_live_and_catalog_books_resolve(self):
        live = [subject["id"] for subject in self.catalog["subjects"] if subject["available"]]
        self.assertEqual(live, ["cn"])
        for subject in self.catalog["subjects"]:
            if subject["id"] != "cn":
                self.assertEqual(subject["question_count"], 0)
                self.assertIsNone(subject["bank_manifest_url"])
        for book in self.catalog["subjects"][0]["books"]:
            self.assertTrue((ROOT / book["file"]).is_file(), book["file"])
            if book["kind"] == "standalone_cbt":
                self.assertIn("/v6/", book["file"].replace("\\", "/"))

    def test_public_chunks_are_hashed_and_partition_canonical_ids(self):
        seen = []
        for chunk in self.manifest["topics"]:
            path = ROOT / chunk["file"]
            raw = path.read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), chunk["sha256"])
            rows = json.loads(raw)
            self.assertEqual(len(rows), chunk["published_question_count"])
            self.assertTrue(all(row["topic_id"] == chunk["topic_id"] for row in rows))
            seen.extend(row["id"] for row in rows)
        self.assertEqual(len(seen), len(set(seen)))
        self.assertEqual(set(seen), {q["id"] for q in self.questions if q["verification_status"] not in ("disputed", "pending_review")})

    def test_legacy_source_and_pre_audit_snapshot_are_preserved(self):
        self.assertTrue((ROOT / "archive/pre-audit-2026-10-14/index.html.snapshot").is_file())
        self.assertEqual(list((ROOT / "archive").rglob("*.html")), [], "archived HTML is preserved only as non-runnable snapshots")
        self.assertTrue((ROOT / "archive/pre-audit-2026-10-14/assets/cn-questions.min.json").is_file())
        for number in range(1, 8):
            name = f"Topic {number} - Online Quiz & Exam (by PRAKASH - EkGuru).html"
            current = ROOT / "Computer Network/Online Quiz" / name
            preserved = ROOT / "archive/pre-audit-2026-10-14/Computer Network/Online Quiz" / f"{name}.snapshot"
            self.assertTrue(current.is_file())
            self.assertTrue(preserved.is_file())
            self.assertIn("legacy CBT snapshot has been retired", current.read_text(encoding="utf-8"))
            self.assertIn("const QUESTIONS", preserved.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
