"""Read-only rehash of prior sealed packets; write one new receipt here only."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import sys

O = Path(__file__).resolve().parent
W = O.parents[1]
names = [
    'positive-six-candidates-independent-v1',
    'w08-mc-final-independent-v1',
    'central31-native-composition-v1',
    'bsa1222-successor-independent-v1',
    'campaign-evidence-provenance-audit-v1',
    'w10-two-case-successor-independent-v1',
]
expected_handoffs = {
    names[0]: '497e690a4514c50c57caf75ff377aa9a62b587be909052da90158b07701c563a',
    names[1]: '603b243d02cd87e3027c11839b27d32dfa361e2b880c7b62bec6dee9e1533b55',
    names[2]: 'a36ee6a01e6129a9f832dc737daad516578f516e4b29184fa9924e788852ac10',
}
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

checks = []
for name in names:
    base = W / '.temp' / name
    manifest = base / 'MANIFEST.json'
    doc = json.loads(manifest.read_text())
    rows = doc.get('members', doc.get('files', doc.get('entries')))
    assert rows is not None
    regular = links = 0
    for row in rows:
        p = base / row['path']
        assert p.is_relative_to(base)
        if 'symlink' in row.get('kind', ''):
            assert p.is_symlink() and os.readlink(p) == row['target'], str(p)
            links += 1
        else:
            assert p.is_file() and not p.is_symlink(), str(p)
            assert digest(p) == row['sha256'], str(p)
            regular += 1
    outer = {}
    for leaf in ['HANDOFF.json', 'HANDOFF.md', 'SELECTOR.json', 'SHA256SUMS']:
        p = base / leaf
        if p.is_file():
            outer[leaf] = digest(p)
    if name in expected_handoffs:
        assert outer['HANDOFF.json'] == expected_handoffs[name], name
    checks.append({'packet': str(base), 'manifest_sha256': digest(manifest),
                   'regular_members_verified': regular, 'diagnostic_links_verified': links,
                   'outer_hashes': outer})

out = O / (sys.argv[1] if len(sys.argv) > 1 else 'prior-packets-before-publication.json')
assert out.parent == O and not out.exists()
receipt = {'checked_at': datetime.now(timezone.utc).isoformat(),
           'reviewer': 'Codex worker02 /root', 'scope': 'Integrity only; no new science or prior-packet edits',
           'packets': checks, 'status': 'PASS'}
with out.open('x') as f:
    json.dump(receipt, f, indent=2); f.write('\n')
print(json.dumps({'receipt': str(out), 'sha256': digest(out),
                  'regular_members_verified': sum(c['regular_members_verified'] for c in checks)}))
