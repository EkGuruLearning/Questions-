"""Offline integrity gates for the licensed source-import checkpoint.

These do NOT claim that student reading pages or complete syllabuses exist.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location('open_course_import', ROOT / 'tools/import_open_courses.py')
IMPORTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(IMPORTER)


def git_hash(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


class OpenCourseCheckpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / 'library/catalog.json').read_text())
        cls.sources = {s['id']: s for s in cls.catalog['sources']}

    def local_file(self, value, namespace):
        file = ROOT / value
        self.assertTrue(file.resolve().is_relative_to((ROOT / namespace).resolve()), value)
        self.assertFalse(file.is_symlink(), value)
        self.assertTrue(file.is_file(), value)
        return file

    def test_import_is_honestly_labelled_unpublished_not_a_complete_syllabus(self):
        self.assertEqual(self.catalog['publication_status'], 'source-import-checkpoint')
        self.assertIs(self.catalog['student_reader_published'], False)
        self.assertIn('NOT 200 independently reviewed websites', self.catalog['scope'])
        self.assertIn('NOT implemented yet', self.catalog['transformation'])
        self.assertGreaterEqual(len(self.catalog['readings']), 200)

    def test_only_explicitly_reviewed_sources_and_permissive_notices(self):
        self.assertEqual({s['repository'] for s in self.sources.values()}, {r[0] for r in IMPORTER.SOURCES})
        for source in self.sources.values():
            with self.subTest(repo=source['repository']):
                self.assertIn(source['license'], ['MIT', 'CC0-1.0'])
                self.assertRegex(source['commit'], r'^[a-f0-9]{40}$')
                self.assertRegex(source['tree_sha'], r'^[a-f0-9]{40}$')
                data = self.local_file(source['license_file'], 'assets/library/licenses').read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), source['license_sha256'])
                self.assertEqual(git_hash(data), source['license_blob'])
                self.assertIn(b'Permission is hereby granted' if source['license'] == 'MIT' else b'CC0 1.0 Universal', data)
                self.assertTrue(source['authors'])

    def test_every_chapter_is_an_exact_verified_blob_not_rewritten_text(self):
        for row in self.catalog['readings']:
            with self.subTest(file=row['file']):
                source = self.sources[row['source_id']]
                namespace = 'library/third_party/' + source['id']
                data = self.local_file(row['file'], namespace).read_bytes()
                self.assertEqual(len(data), row['bytes'])
                self.assertEqual(hashlib.sha256(data).hexdigest(), row['sha256'])
                self.assertEqual(git_hash(data), row['blob'])
                self.assertTrue(IMPORTER.selected(source['repository'], row['source_path']))

    def test_required_code_includes_are_pinned_data_not_executed(self):
        total = 0
        for row in self.catalog['readings']:
            text = (ROOT / row['file']).read_text(encoding='utf-8-sig')
            markers = [m[0] for m in IMPORTER.INCLUDE.finditer(text)]
            self.assertEqual(markers, [i['marker'] for i in row.get('includes', [])])
            for include in row.get('includes', []):
                data = self.local_file(include['file'], 'library/third_party/' + row['source_id']).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), include['sha256'])
                self.assertEqual(git_hash(data), include['blob'])
                total += 1
        self.assertGreater(total, 0)

    def test_identifiers_classification_and_source_counts_are_consistent(self):
        seen = set()
        for row in self.catalog['readings']:
            self.assertIn(row['source_id'], self.sources)
            self.assertRegex(row['id'], r'^[a-z0-9-]+$')
            self.assertRegex(row['subject_id'], r'^[a-z0-9-]+$')
            self.assertIn(row['unit_index'], (0, 1, 2))
            self.assertTrue(row['title'].strip())
            key = (row['source_id'], row['id'])
            self.assertNotIn(key, seen)
            seen.add(key)
        for source in self.sources.values():
            self.assertEqual(source['reading_count'], sum(r['source_id'] == source['id'] for r in self.catalog['readings']))

    def test_importer_does_not_select_translations_nonlessons_or_arbitrary_files(self):
        for repo, path in IMPORTER.EXCLUDED:
            self.assertFalse(IMPORTER.selected(repo, path), 'Quarantined sources must not be re-imported')
        for repo, _, _ in IMPORTER.SOURCES:
            for path in ['AGENTS.md', 'SECURITY.md', '.github/workflows/build.yml', 'translations/README.md', 'assets/picture.png']:
                self.assertFalse(IMPORTER.selected(repo, path), (repo, path))

    def test_raw_book_html_is_not_discovered_as_a_student_page(self):
        spec = importlib.util.spec_from_file_location('site_routes_checkpoint', ROOT / 'tools/build_site_routes.py')
        module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        self.assertIn('library', module.SKIP_TOP)
        self.assertFalse(any(p.startswith('library/') for p in module.published_pages()))

    def test_source_directory_contains_only_manifest_referenced_files(self):
        expected = {r['file'] for r in self.catalog['readings']}
        expected.update(i['file'] for r in self.catalog['readings'] for i in r.get('includes', []))
        actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'library/third_party').rglob('*') if p.is_file()}
        self.assertEqual(actual, expected)
        for file in actual:
            self.assertIsNone(IMPORTER.SENSITIVE_LITERAL.search((ROOT / file).read_bytes()), 'Credential-shaped literal in ' + file)


if __name__ == '__main__':
    unittest.main()
