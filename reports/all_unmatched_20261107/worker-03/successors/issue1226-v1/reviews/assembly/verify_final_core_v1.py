"""Independent core/capture/accounting audit. Never imports the author's producer."""
from pathlib import Path
import copy
import datetime
import hashlib
import json
import os
import sys

R = Path.cwd()
A = R/'.temp/w03-provenance-successor-v1/assembly'
P = R/'reports/all_unmatched_20261107/worker-03'
OLD = P/'successors/issue1224-v1/publication-v1'
NEW = R/sys.argv[1]
SOURCE = R.parents[2]/'queue/preliminary-v5'
sha = lambda b: hashlib.sha256(b).hexdigest()
canon = lambda value: json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()
read = lambda p: json.loads(p.read_text())
old_decisions = read(OLD/'decisions.json')
old_proposals = read(OLD/'proposals.json')
old_evidence = read(OLD/'evidence.json')
decisions = read(NEW/'decisions.json')
proposals = read(NEW/'proposals.json')
evidence = read(NEW/'evidence.json')
shard = read(SOURCE/'shards/shard-03.json')
assert (OLD/'decisions.json').read_bytes() == (NEW/'decisions.json').read_bytes()
assert len(decisions['decisions']) == len(shard['cases']) == 188
assert len(proposals['proposals']) == 74
oldp = {p['proposal_id']: p for p in old_proposals['proposals']}
newp = {p['proposal_id']: p for p in proposals['proposals']}
olde = {e['evidence_id']: e for e in old_evidence['evidence']}
newe = {e['evidence_id']: e for e in evidence['evidence']}
assert len(newe) == len(evidence['evidence'])
assert set(oldp) == set(newp) and len(oldp) == len(newp) == 74
assert len(olde) == 863 and all(newe[key] == value for key, value in olde.items())
bridge = read(P/'successors/issue1226-v1/payload-bridge.json')
changes = {r['proposal_id']: r for r in bridge['entries']}
payload_proof = read(A/'payload-scope-verification-v1.json')
payload_rows = {r['proposal_id']: r for r in payload_proof['all74_payload_rows']}
proposal_rows = []
for pid, current in newp.items():
    previous = oldp[pid]
    changed_keys = [k for k in sorted(set(previous)|set(current)) if previous.get(k) != current.get(k)]
    if pid in changes:
        assert set(changed_keys) <= {'after_capture', 'independent_review', 'evidence_ids'}
        assert current['after_capture'] == changes[pid]['after_capture']
        assert current['independent_review']['reviewed_after_sha256'] == current['after_capture']['sha256']
        assert current['independent_review']['reviewer'] != previous['independent_review']['reviewer']
        assert current['independent_review'].get('scientific_review') is False
        assert set(previous['evidence_ids']) <= set(current['evidence_ids'])
        assert changes[pid]['original_proposal'] == previous
    else:
        assert current == previous
    assert current['after_capture']['sha256'] == payload_rows[pid]['new_sha256']
    assert all(e in newe for e in current['evidence_ids'])
    assert all(e in newe for e in current['independent_review']['evidence_ids'])
    proposal_rows.append({'proposal_id': pid, 'changed_keys': changed_keys, 'after_sha256': current['after_capture']['sha256'],
                          'before_sha256': current['before_sha256'], 'kind': current['kind'],
                          'reviewer': current['independent_review']['reviewer'],
                          'review_scope': current['independent_review'].get('scope'),
                          'original_proposal_and_review_retained': True})
frozen = {x['case_id']: x for x in shard['cases']}
assert len(frozen) == 188 and {x['case_id'] for x in decisions['decisions']} == set(frozen)
case_rows = []
for case in decisions['decisions']:
    cid = case['case_id']
    assert case['case_input_sha256'] == sha(canon(frozen[cid]))
    assert all(pid in newp for pid in case['proposal_ids'])
    assert all(e in newe for e in case['evidence_ids'])
    changed = [pid for pid in case['proposal_ids'] if pid in changes]
    if changed:
        assert 'reviewed_after_sha256' not in case['independent_review']
    scope = {k: case[k] for k in ('review_scope', 'scope_limitations', 'publication_admission') if k in case}
    assert scope
    case_rows.append({'case_id': cid, 'case_input_sha256': case['case_input_sha256'],
                      'case_object_sha256': sha(canon(case)), 'disposition': case['disposition'],
                      'linked_changed_proposal_ids': changed, 'scientific_scope_fields': scope,
                      'complete_object_unchanged': True, 'source_science_reapproved': False})
roots = {'artifact': P, 'source': SOURCE, 'mim': R}
capture_rows = []
for row in evidence['evidence']:
    cap = row['capture']
    root = roots[cap['root']]
    relative = Path(cap['path'])
    assert not relative.is_absolute() and '..' not in relative.parts
    path = root/relative
    assert path.resolve().is_relative_to(root.resolve())
    assert path.is_file() and sha(path.read_bytes()) == cap['sha256']
    capture_rows.append({'evidence_id': row['evidence_id'], 'root': cap['root'], 'path': cap['path'],
                         'sha256': cap['sha256'], 'kind': row['kind'], 'historical_unchanged': row['evidence_id'] in olde})
preflight = read(A/'preflight-inputs-v1.json')
for row in preflight['tracked_files']:
    path = R/row['path']
    data = os.readlink(path).encode() if row['mode'] == '120000' else path.read_bytes()
    assert sha(data) == row['sha256']
maintained = preflight['maintained_search_boundary']['files']
for row in maintained:
    path = R/row['path']
    if 'symlink_target' in row:
        assert path.is_symlink() and os.readlink(path) == row['symlink_target']
    else:
        assert path.is_file() and sha(path.read_bytes()) == row['sha256']
observed = set()
for relroot in preflight['maintained_search_boundary']['roots']:
    for directory, dirs, names in os.walk(R/relroot, followlinks=False):
        for name in names:
            path = Path(directory)/name
            if path.is_file() or path.is_symlink():
                observed.add(str(path.relative_to(R)))
assert observed == {x['path'] for x in maintained}
result = {'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'reviewer': '/root/provenance_assembly',
          'scope': 'Complete exact selector, full-value preservation, provenance and capture integrity; no new scientific review',
          'core': {n: {'path': str((NEW/n).relative_to(R)), 'sha256': sha((NEW/n).read_bytes())}
                   for n in ['decisions.json', 'proposals.json', 'evidence.json']},
          'counts': {'cases': len(case_rows), 'proposals': len(proposal_rows), 'changed_payloads': len(changes),
                     'unchanged_payloads': 74-len(changes), 'evidence': len(capture_rows), 'original_evidence': 863,
                     'new_evidence': len(capture_rows)-863, 'source_cases_linking_changed_proposals': sum(bool(x['linked_changed_proposal_ids']) for x in case_rows)},
          'all188_case_rows': case_rows, 'all74_proposal_rows': proposal_rows, 'all_evidence_capture_rows': capture_rows,
          'original_tracked_blobs_unchanged': len(preflight['tracked_files']),
          'original_tracked_regular_files': sum(x['mode'] != '120000' for x in preflight['tracked_files']),
          'original_tracked_symlinks': sum(x['mode'] == '120000' for x in preflight['tracked_files']),
          'ignored_inclusive_maintained_files_unchanged': len(maintained),
          'source_decisions_file_byte_identical': True, 'findings': [],
          'limitations': ['Original source reviews retain their original historical scope and never bind the 49 changed payload bytes.',
                          'Exact captures were hashed for preservation; this metadata review does not claim renewed primary-source scientific inspection.',
                          'No whole-owner, role, export, integration or cross-shard coalescence approval.',
                          'No absence claim outside the declared maintained roots; credentials and unrelated private directories were not searched.']}
destination = A/'final-core-verification-v1.json'
with destination.open('x') as stream:
    json.dump(result, stream, indent=2, ensure_ascii=False)
    stream.write('\n')
print(json.dumps({'status': 'PASS', 'counts': result['counts'], 'sha256': sha(destination.read_bytes())}, indent=2))
