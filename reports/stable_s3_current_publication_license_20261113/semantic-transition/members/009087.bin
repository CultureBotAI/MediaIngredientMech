"""Seal the additive report transport after independent assembly review.

No scientific record is serialized; all selected payload and evidence bytes
are copied and rehashed. Prior packets and source cores are only read.
Fixture Git bookkeeping is excluded before traversal and is never inspected.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'MAPPING_SEMANTICS.md').is_file())
PRIVATE = ROOT / '.temp/gyps-native-origin-v1'
REPORT = ROOT / 'reports/all_unmatched_20261107/worker-03/successors/issue1176-gyps-native-v1'
BASE = '784ee2541506c914b4c34f091de688d39784d548'
EXCLUDED_FILES = {'MANIFEST.json', 'SHA256SUMS', 'PUBLICATION-RECEIPT.json'}
EXCLUDED_DIRS = {'.git', '__pycache__'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def immutable_json(path, obj):
    assert not path.exists(), f'immutable output already exists: {path}'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')


def check_members(base, rows):
    for row in rows:
        path = base / row['path']
        assert path.is_file() and not path.is_symlink(), str(path)
        data = path.read_bytes()
        assert sha(data) == row['sha256'], str(path)
        if 'bytes' in row:
            assert len(data) == row['bytes'], str(path)


def inventory(base):
    rows, links = [], []
    for dirname, dirs, files in os.walk(base, followlinks=False):
        parent = Path(dirname)
        for name in list(dirs):
            path = parent / name
            if name in EXCLUDED_DIRS:
                dirs.remove(name)
            elif path.is_symlink():
                links.append({'path': str(path.relative_to(base)), 'target': os.readlink(path), 'kind': 'directory_symlink'})
                dirs.remove(name)
        for name in files:
            path = parent / name
            rel = str(path.relative_to(base))
            if rel in EXCLUDED_FILES:
                continue
            if path.is_symlink():
                links.append({'path': rel, 'target': os.readlink(path), 'kind': 'file_symlink'})
                continue
            data = path.read_bytes()
            rows.append({'path': rel, 'sha256': sha(data), 'bytes': len(data)})
    return sorted(rows, key=lambda r: r['path']), sorted(links, key=lambda r: r['path'])


def main():
    assert subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip() == BASE
    assert not subprocess.check_output(['git', '-C', str(ROOT), 'status', '--porcelain'], text=True).strip()
    assert sha((PRIVATE / 'proposals.json').read_bytes()) == '582ea36dd479b8ecd244d996a6eb772569eb232b1631f87ef5f4aa143a20ce67'
    assert sha((PRIVATE / 'payloads/GYPS.yaml').read_bytes()) == 'fa98f361a39dcaf0bea1f4046829287581bc45e2813044696e5070de58708aa1'
    for root in [PRIVATE, REPORT]:
        assert not (root / 'MANIFEST.json').exists()
        assert not (root / 'SHA256SUMS').exists()
    assembly = read(PRIVATE / 'assembly/final-content-review.json')
    assert str(assembly['status']).startswith('PASS'), 'assembly did not pass'
    assert not assembly.get('findings'), 'unresolved assembly findings'
    copied = read(PRIVATE / 'publication-copy-index.json')['copies']
    check_members(PRIVATE, copied)
    check_members(REPORT, copied)
    assert (REPORT / 'publication-copy-index.json').read_bytes() == (PRIVATE / 'publication-copy-index.json').read_bytes()
    for item in read(PRIVATE / 'HANDOFF.json')['preserved_source_cores']:
        assert sha((ROOT / item['path']).read_bytes()) == item['sha256']
    previous = ROOT / 'reports/all_unmatched_20261107/worker-03/successors/issue1176-dependencies-v1'
    check_members(previous, read(previous / 'MANIFEST.json')['members'])
    for subdir in ['skeptical-review', 'inputs/distinct-head-review']:
        check_members(REPORT / subdir, read(REPORT / subdir / 'MANIFEST.json')['members'])
    additions = []
    for rel in ['assembly/final-content-review.json', 'scripts/seal_native_publication_v1.py']:
        src, dst = PRIVATE / rel, REPORT / rel
        assert not dst.exists(), str(dst)
        data = src.read_bytes()
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
        additions.append({'path': rel, 'sha256': sha(data), 'bytes': len(data)})
    extra = {
        'schema_version': 1,
        'scope': 'Additions after the initial 130-member copy index plus the copy index itself. Selected ledger, payload, handoff, and review bytes unchanged.',
        'additions': additions,
        'outer_seal_files': ['MANIFEST.json', 'SHA256SUMS'],
        'source_or_science_changes': False,
        'actual_publication_head': 'Bound after ordinary commit and push in excluded private PUBLICATION-RECEIPT.json; no prospective head invented.'
    }
    immutable_json(PRIVATE / 'publication-additions-v1.json', extra)
    (REPORT / 'publication-additions-v1.json').write_bytes((PRIVATE / 'publication-additions-v1.json').read_bytes())
    report_rows, report_links = inventory(REPORT)
    expected = {r['path'] for r in copied} | {'publication-copy-index.json', 'publication-additions-v1.json'} | {r['path'] for r in additions}
    assert {r['path'] for r in report_rows} == expected
    assert not report_links
    for row in report_rows:
        assert (PRIVATE / row['path']).read_bytes() == (REPORT / row['path']).read_bytes(), row['path']
    seals = []
    for base, scope in [(REPORT, 'published portable report'), (PRIVATE, 'durable private proof including isolated fixture files')]:
        rows, links = inventory(base)
        manifest = {
            'schema_version': 1,
            'created_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'scope': scope,
            'root_relative': str(base.relative_to(ROOT)),
            'parent_published_head': BASE,
            'members': rows,
            'member_count': len(rows),
            'symlinks': links,
            'exclusions': ['MANIFEST.json (self)', 'SHA256SUMS (binds manifest and members)', 'PUBLICATION-RECEIPT.json (private post-publication exact-head receipt only)', '**/.git/** (private fixture bookkeeping, excluded before traversal)', '**/__pycache__/** (runtime cache)'],
            'fixture_scope': 'Fixture files are durable private evidence only; native fixture preparation is not full-campaign preparation or actual worker publication. No native apply was called.',
            'no_source_changes_or_approval_transfer': True
        }
        immutable_json(base / 'MANIFEST.json', manifest)
        manifest_sha = sha((base / 'MANIFEST.json').read_bytes())
        sums = ''.join(f"{r['sha256']}  {r['path']}\n" for r in rows) + f'{manifest_sha}  MANIFEST.json\n'
        (base / 'SHA256SUMS').write_text(sums)
        check_members(base, rows)
        seals.append({'root': str(base.relative_to(ROOT)), 'members': len(rows), 'symlinks': len(links), 'handoff_sha256': sha((base / 'HANDOFF.json').read_bytes()), 'manifest_sha256': manifest_sha, 'transport_sha256': sha((base / 'SHA256SUMS').read_bytes())})
    print(json.dumps({'status': 'SEALED', 'seals': seals}, indent=2))


if __name__ == '__main__':
    main()
