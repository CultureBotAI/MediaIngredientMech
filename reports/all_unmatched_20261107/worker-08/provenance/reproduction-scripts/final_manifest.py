"""Write/verify only this worker's report and newly authored native reviews."""
from pathlib import Path
import hashlib
import sys

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'reports/all_unmatched_20261107/worker-08'
MANIFEST=OUT/'SHA256SUMS'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def selected():
    paths={p for p in OUT.rglob('*') if p.is_file() and p!=MANIFEST}
    for dirname in (ROOT/'reviews/structured').glob('20261108T*-w08-*'):
        paths.update(p for p in dirname.rglob('*') if p.is_file())
    assert all(not p.is_symlink() for p in paths)
    return sorted(paths)

if '--write' in sys.argv:
    MANIFEST.write_text(''.join(f'{sha(p)}  {p.relative_to(ROOT)}\n' for p in selected()))

entries={}
for line in MANIFEST.read_text().splitlines():
    digest,path=line.split('  ',1)
    assert path not in entries and len(digest)==64
    entries[path]=digest
actual={str(p.relative_to(ROOT)):sha(p) for p in selected()}
assert entries==actual, 'manifest membership or content differs'
print(f'PASS: {len(entries)} exact files; SHA256SUMS {sha(MANIFEST)}')
