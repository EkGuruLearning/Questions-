#!/usr/bin/env python3
"""Opt-in, pinned, license-audited text import. NEVER run by a normal build.

Uses GitHub's authenticated API via gh, verifies Git blob SHA-1 and records SHA-256.
Copies only selected English teaching Markdown + required Rust code includes and
license notices. NO third-party images, videos, datasets or executable build steps.
Downloaded source is data; it is never executed. Subsequent builds are offline.
"""
from __future__ import annotations
import argparse
import base64
import concurrent.futures
import hashlib
import json
import pathlib
import posixpath
import re
import subprocess
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
CACHE = ROOT / '.cache/library-sources'
BLOBS = ROOT / '.cache/open-course-blobs'
INCLUDE = re.compile(r'\{\{#(?:rustdoc_)?include\s+([^}\s]+)\s*\}\}')
EXCLUDED = {('microsoft/IoT-For-Beginners', '2-farm/lessons/6-keep-your-plant-secure/README.md')}
# Reject credential-shaped literals before a source blob can enter the checkout.
# This is a conservative local guard, not a replacement for GitHub push protection.
SENSITIVE_LITERAL = re.compile(
    rb'SharedAccessKey=[A-Za-z0-9+/]{30,}={0,2}|gh[pousr]_[A-Za-z0-9]{30,}|'
    rb'github_pat_[A-Za-z0-9_]{60,}|GOCSPX-[A-Za-z0-9_-]{20,}|'
    rb'(?:AKIA|ASIA)[A-Z0-9]{16}|-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----'
)
SOURCES = [
    ('microsoft/Web-Dev-For-Beginners', 'MIT', 'LICENSE'),
    ('microsoft/ML-For-Beginners', 'MIT', 'LICENSE'),
    ('microsoft/Data-Science-For-Beginners', 'MIT', 'LICENSE'),
    ('microsoft/AI-For-Beginners', 'MIT', 'LICENSE'),
    ('microsoft/IoT-For-Beginners', 'MIT', 'LICENSE'),
    ('microsoft/generative-ai-for-beginners', 'MIT', 'LICENSE'),
    ('microsoft/Security-101', 'CC0-1.0', 'LICENSE'),
    ('rust-lang/book', 'MIT', 'LICENSE-MIT'),
    ('trekhleb/javascript-algorithms', 'MIT', 'LICENSE'),
]


def blob(repo, sha):
    file = BLOBS / sha
    if file.exists(): data = file.read_bytes()
    else:
        for attempt in range(3):
            result = subprocess.run(['gh', 'api', f'repos/{repo}/git/blobs/{sha}'], text=True, capture_output=True)
            if result.returncode == 0: break
            if not re.search(r'HTTP (429|50\d)', result.stderr) or attempt == 2: raise RuntimeError(result.stderr)
            time.sleep(attempt + 1)
        response = json.loads(result.stdout)
        if response.get('encoding') != 'base64': raise ValueError('Expected a base64 Git blob')
        data = base64.b64decode(response['content'])
        if len(data) > 2_000_000: raise ValueError('Teaching source unexpectedly exceeds 2 MB')
        file.parent.mkdir(parents=True, exist_ok=True); file.write_bytes(data)
    if hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() != sha: raise ValueError(f'Git blob hash mismatch: {repo}/{sha}')
    return data


def selected(repo, path):
    if (repo, path) in EXCLUDED: return False
    parts = path.split('/')
    if any(p.lower() in ('translations', 'translated', 'node_modules', '.github', 'quiz-app', 'sketchnotes') for p in parts): return False
    if repo == 'rust-lang/book': return bool(re.fullmatch(r'src/ch\d\d-\d\d-[^/]+\.md', path))
    if repo == 'trekhleb/javascript-algorithms': return path.startswith(('src/algorithms/', 'src/data-structures/')) and path.endswith('/README.md')
    if repo == 'microsoft/Security-101': return bool(re.fullmatch(r'\d\.\d [^/]+\.md', path)) and 'quiz' not in path.lower()
    if not path.endswith('/README.md'): return False
    if repo == 'microsoft/AI-For-Beginners': return path.startswith('lessons/') and len(parts) in (3, 4) and '/lab/' not in path
    if repo == 'microsoft/IoT-For-Beginners': return '/lessons/' in path and len(parts) == 4
    if repo == 'microsoft/generative-ai-for-beginners': return len(parts) == 2 and bool(re.match(r'^\d\d-', parts[0]))
    if repo == 'microsoft/Data-Science-For-Beginners': return bool(re.match(r'^\d-', parts[0])) and (len(parts) == 3 and re.match(r'^\d', parts[1]) or len(parts) == 4 and parts[1] == 'R')
    if repo == 'microsoft/ML-For-Beginners': return len(parts) == 3 and bool(re.match(r'^\d-', parts[0])) and bool(re.match(r'^\d-', parts[1]))
    return bool(re.match(r'^\d', parts[0])) and (len(parts) == 3 and re.match(r'^\d-', parts[1]) or parts[0] == '4-typing-game' and len(parts) == 2)


def classify(repo, path):
    p = path.lower()
    if repo == 'rust-lang/book':
        n = int(re.search(r'/ch(\d\d)', p)[1]); return 'rust-programming', 0 if n <= 3 else 1 if n <= 9 else 2
    if repo == 'trekhleb/javascript-algorithms':
        if p.startswith('src/data-structures/'):
            return 'data-structures', 0 if any('/'+s+'/' in p for s in ['linked-list','doubly-linked-list','queue','stack']) else 1 if any(s in p for s in ['tree','heap','trie']) else 2
        if any(s in p for s in ['/math/matrix', '/math/complex-number']): return 'linear-algebra', 1
        if '/math/' in p: return 'discrete-mathematics', 2
        if '/cryptography/' in p: return 'cyber-security', 2
        return 'algorithms', 0 if '/search/' in p else 1 if any(s in p for s in ['/sorting/', '/string/']) else 2
    if repo == 'microsoft/Security-101':
        n = int(p[0]); return ('computer-network', 2) if n == 3 else ('professional-ethics', 2) if 'responsible' in p else ('cyber-security', 0 if n == 1 else 1 if n <= 4 else 2)
    if repo == 'microsoft/Web-Dev-For-Beginners':
        if 'github' in p: return 'version-control-devops', 0
        if 'accessibility' in p: return 'professional-ethics', 2
        if p.startswith('2-js-basics'): return 'javascript', 0 if any(s in p for s in ['data-types','functions']) else 1
        return 'web-development', 0 if 'intro-to-html' in p else 1 if any(s in p for s in ['intro-to-css','intro-to-dom']) else 2
    if repo == 'microsoft/ML-For-Beginners':
        if p.startswith('6-nlp'): return 'artificial-intelligence', 1
        if 'fairness' in p: return 'professional-ethics', 1
        return 'machine-learning', 0 if p.startswith(('1-', '2-')) else 1 if p.startswith(('4-', '5-')) else 2
    if repo == 'microsoft/Data-Science-For-Beginners':
        if 'ethics' in p: return 'professional-ethics', 1
        if 'stats-and-probability' in p: return 'probability-statistics', 2
        if 'relational-databases' in p: return 'dbms', 0
        if 'non-relational' in p: return 'dbms', 2
        if '07-python' in p: return 'python-programming', 2
        if p.startswith('5-'): return 'cloud-computing', 2
        return 'data-science', 0 if p.startswith('1-') else 1 if p.startswith(('2-', '3-')) else 2
    if repo == 'microsoft/AI-For-Beginners':
        if 'ethics' in p: return 'professional-ethics', 2
        if '3-neuralnetworks' in p: return 'machine-learning', 2
        return 'artificial-intelligence', 0 if any(s in p for s in ['1-intro','2-symbolic']) else 1 if '/5-nlp/' in p else 2
    if repo == 'microsoft/IoT-For-Beginners':
        if 'cloud' in p: return 'cloud-computing', 1
        if 'secure' in p: return 'cyber-security', 2
        return 'internet-of-things', 0 if p.startswith('1-') else 1 if p.startswith('2-') else 2
    return 'generative-ai', 0 if p.startswith(('00-','01-','02-','03-','04-','05-')) else 1 if p.startswith(('06-','07-','08-','09-','10-','11-','12-','15-')) else 2


def title_for(data, path):
    body = data.decode('utf-8-sig')
    headings = re.findall(r'^#{1,2}\s+(.+)', body, re.M)
    title = headings[0] if headings else pathlib.PurePosixPath(path).stem.replace('-', ' ')
    title = re.sub(r'!\[[^\]]*\]\([^)]*\)|<[^>]*>|\{#[^}]*\}', '', title)
    title = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', title).replace('*', '').replace('`', '').strip()
    return (title or path.split('/')[-2])[:180]


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--import-reviewed', action='store_true'); args = parser.parse_args()
    if not args.import_reviewed: parser.error('Network copying is opt-in: --import-reviewed')
    sources, readings, jobs, source_info = [], [], [], {}
    existing = ROOT / 'library/catalog.json'
    pinned = {s['repository']: s for s in json.loads(existing.read_text())['sources']} if existing.exists() else {}
    for repo, license_id, license_path in SOURCES:
        base = CACHE / repo.replace('/', '--')
        meta_file, tree_file = base.with_suffix('.meta.json'), base.with_suffix('.meta.tree.json')
        if meta_file.exists(): meta = json.loads(meta_file.read_text())
        elif repo in pinned: meta = {'repo': repo, 'sha': pinned[repo]['commit'], 'license': pinned[repo]['license']}
        else: raise ValueError('No reviewed commit pin for ' + repo)
        if not re.fullmatch(r'[a-f0-9]{40}', meta.get('sha', '')): raise ValueError('Invalid reviewed commit pin')
        if repo in pinned and meta['sha'] != pinned[repo]['commit']: raise ValueError('Source pin changed; review the catalogue before re-importing')
        if tree_file.exists(): tree_doc = json.loads(tree_file.read_text())
        else:
            tree_doc = json.loads(subprocess.check_output(['gh', 'api', f"repos/{repo}/git/trees/{meta['sha']}?recursive=1"], text=True))
            CACHE.mkdir(parents=True, exist_ok=True); tree_file.write_text(json.dumps(tree_doc))
        if repo in pinned and tree_doc.get('sha') != pinned[repo].get('tree_sha'): raise ValueError('Cached tree does not match the reviewed tree pin')
        if tree_doc.get('truncated'): raise ValueError('Incomplete GitHub tree; refuse unreviewable import')
        tree = {x['path']: x for x in tree_doc['tree'] if x['type'] == 'blob'}
        if license_id != meta['license'] and repo != 'rust-lang/book': raise ValueError('License metadata changed')
        sid = repo.replace('/', '--').lower(); lic = blob(repo, tree[license_path]['sha'])
        if license_id == 'MIT' and b'Permission is hereby granted' not in lic: raise ValueError('Missing MIT grant')
        if license_id == 'CC0-1.0' and b'CC0 1.0 Universal' not in lic: raise ValueError('Missing CC0 notice')
        lic_hash = hashlib.sha256(lic).hexdigest(); lic_file = f'assets/library/licenses/{sid}.{lic_hash[:12]}.txt'; dest = ROOT / lic_file; dest.parent.mkdir(parents=True, exist_ok=True); dest.write_bytes(lic)
        source = {'id': sid, 'repository': repo, 'commit': meta['sha'], 'tree_sha': tree_doc['sha'], 'license': license_id, 'license_file': lic_file, 'license_sha256': lic_hash, 'license_source_path': license_path, 'license_blob': tree[license_path]['sha'], 'authors': 'The Rust Project Developers and contributors' if repo == 'rust-lang/book' else 'Oleksii Trekhleb and contributors' if repo.startswith('trekhleb/') else 'Microsoft and contributors'}
        sources.append(source); source_info[repo] = (source, tree)
        for path in sorted(tree):
            if selected(repo, path): jobs.append((repo, path, tree[path]))
    def fetch(job):
        repo, path, record = job; source, _ = source_info[repo]; data = blob(repo, record['sha'])
        if SENSITIVE_LITERAL.search(data): raise ValueError('Credential-like literal in source; exclude and review: ' + repo + '/' + path)
        target = f"library/third_party/{source['id']}/{path}"; dest = ROOT / target; dest.parent.mkdir(parents=True, exist_ok=True); dest.write_bytes(data)
        return repo, path, record, data, target
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        fetched = list(pool.map(fetch, jobs))
    included_jobs, include_records = {}, {}
    for repo, path, record, data, target in fetched:
        sid = source_info[repo][0]['id']; subject, unit = classify(repo, path)
        identifier = re.sub('[^a-z0-9]+', '-', (path[:-10] if path.endswith('/README.md') else path[:-3]).lower()).strip('-')[-65:] + '-' + hashlib.sha256((repo+'/'+path).encode()).hexdigest()[:8]
        row = {'id': identifier, 'source_id': sid, 'subject_id': subject, 'unit_index': unit, 'title': title_for(data, path), 'source_path': path, 'file': target, 'sha256': hashlib.sha256(data).hexdigest(), 'blob': record['sha'], 'bytes': len(data)}
        includes = []
        for match in INCLUDE.finditer(data.decode('utf-8-sig')):
            spec = match[1].split(':'); include_path = posixpath.normpath(posixpath.join(posixpath.dirname(path), spec[0]))
            if include_path.startswith(('../','/')) or include_path not in source_info[repo][1]: raise ValueError('Unresolved or unsafe source include: '+include_path)
            included_jobs[(repo, include_path)] = (repo, include_path, source_info[repo][1][include_path]); includes.append({'marker': match[0], 'source_path': include_path, 'slice': spec[1:]})
        if includes: row['includes'] = includes
        readings.append(row)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for repo, path, record, data, target in pool.map(fetch, included_jobs.values()):
            include_records[(repo, path)] = {'file': target, 'source_path': path, 'sha256': hashlib.sha256(data).hexdigest(), 'blob': record['sha']}
    for row in readings:
        repo = next(s['repository'] for s in sources if s['id'] == row['source_id'])
        for include in row.get('includes', []): include.update(include_records[(repo, include['source_path'])])
    counts = {s['id']: sum(r['source_id'] == s['id'] for r in readings) for s in sources}
    for s in sources: s['reading_count'] = counts[s['id']]
    doc = {'schema_version': 1, 'reviewed_on': '2026-10-17', 'publication_status': 'source-import-checkpoint', 'student_reader_published': False, 'scope': 'English teaching chapters from nine explicitly licensed repositories, NOT 200 independently reviewed websites. No completeness claim for all IT subjects or exams.', 'transformation': 'Pinned source text copied without byte changes. Required Rust listing includes preserved separately. Student renderer, include expansion, navigation, mathematics and media-link handling are NOT implemented yet. No media/dataset binaries copied.', 'sources': sources, 'readings': readings, 'excluded_sources': [{'source_id': repo.replace('/', '--').lower(), 'source_path': path, 'reason': 'Credential-like literal in upstream tutorial; not copied or exposed. Do not bypass push protection.'} for repo, path in sorted(EXCLUDED)]}
    dest = ROOT / 'library/catalog.json'; dest.parent.mkdir(exist_ok=True); dest.write_text(json.dumps(doc, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'imported_chapters':len(readings),'repositories':len(sources),'source_bytes':sum(r['bytes'] for r in readings),'pinned_include_files':len(include_records),'by_source':counts}, indent=2))


if __name__ == '__main__': main()
