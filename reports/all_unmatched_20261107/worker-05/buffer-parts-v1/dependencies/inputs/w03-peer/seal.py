"""Seal this private review only, after both final assembly receipts exist."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

R = Path.cwd()
O = R / '.temp/peptone-consumer-independent-v1'
EXPECTED_HEAD = 'fe31a02850932a7bdf2fe65c93cb636a86f82a2c'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path):
    return json.loads(path.read_text())

def put(path, value):
    with path.open('x') as handle:
        json.dump(value, handle, indent=2)
        handle.write('\n')

assert not (O / 'MANIFEST.json').exists()
assert not (O / 'SHA256SUMS').exists()
for name in ['assembly/final-content-review.json', 'assembly/final-skeptical-readback.json']:
    assert (O / name).is_file(), name

peer_checks = []
for peer, field in [('ambiguous', 'members'), ('other', 'files'), ('skeptic', 'members')]:
    folder = O / peer
    manifest = load(folder / 'MANIFEST.json')
    members = manifest[field]
    paths = {m['path'] for m in members}
    assert len(paths) == len(members)
    actual = {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}
    assert actual == paths | {'MANIFEST.json'}, peer
    for member in members:
        path = folder / member['path']
        assert not path.is_symlink()
        assert digest(path) == member['sha256'], str(path)
        assert path.stat().st_size == member['bytes'], str(path)
    peer_checks.append({'peer': peer, 'members': len(members), 'manifest_sha256': digest(folder / 'MANIFEST.json')})

head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
status = subprocess.check_output(['git', 'status', '--porcelain'], text=True).strip()
assert head == EXPECTED_HEAD
assert not status
prior = load(O / 'context/input-receipt.json')['prior_seals_to_preserve']
for pin in prior:
    assert digest(R / pin['path']) == pin['sha256'], pin['path']
owners = load(O / 'context/owner-bindings-20.json')
assert len(owners) == 20 and sum(not row['new_owner'] for row in owners) == 19
for row in owners:
    assert digest(R / row['capture']['captured_path']) == row['owner_sha256']
    if not row['new_owner']:
        assert digest(R / row['owner_path']) == row['before_sha256']
ledger = load(O / 'machine-ledger.json')
assert len({row['claim_key'] for row in ledger['rows']}) == 20
assert all(row['candidate_created_or_edited'] is False for row in ledger['rows'])
assert all(row['whole_owner_form_role_or_export_approval'] is False for row in ledger['rows'])

put(O / 'assembly/preseal-preservation-check.json', {
    'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reviewer': '/root',
    'status': 'PASS',
    'head': head,
    'tracked_status': status,
    'peer_seals_rehashed': peer_checks,
    'prior_seals_rehashed': prior,
    'owner_snapshots_rehashed': 20,
    'maintained_beforeimages_rehashed': 19,
    'all_20_claims_accounted': True,
    'search_boundary': 'Recursive pathlib enumeration of this exact output root includes ignored files; no global historical or private-file absence claim.',
    'candidate_or_maintained_writes': False,
})

paths = sorted(O.rglob('*'))
assert not any(p.is_symlink() for p in paths)
files = [p for p in paths if p.is_file()]
members = [{'path': str(p.relative_to(O)), 'sha256': digest(p), 'bytes': p.stat().st_size} for p in files]
put(O / 'MANIFEST.json', {
    'algorithm': 'SHA256',
    'sealed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'root': str(O),
    'member_count': len(members),
    'members': members,
    'excluded': ['MANIFEST.json (self)', 'SHA256SUMS (transport, includes manifest)'],
    'scope': 'All regular files beneath the exact new output root, including ignored files. No candidate or maintained-data approval.',
})
transport_paths = sorted(files + [O / 'MANIFEST.json'])
with (O / 'SHA256SUMS').open('x') as handle:
    for path in transport_paths:
        handle.write(f'{digest(path)}  {path.relative_to(O)}\n')
actual = {str(p.relative_to(O)) for p in O.rglob('*') if p.is_file()}
assert actual == {m['path'] for m in members} | {'MANIFEST.json', 'SHA256SUMS'}
for member in members:
    assert digest(O / member['path']) == member['sha256']
print(json.dumps({
    'status': 'SEALED',
    'member_count': len(members),
    'transport_entries': len(transport_paths),
    'handoff_sha256': digest(O / 'HANDOFF.json'),
    'manifest_sha256': digest(O / 'MANIFEST.json'),
    'transport_sha256': digest(O / 'SHA256SUMS'),
    'head_preserved': head,
}, indent=2))
