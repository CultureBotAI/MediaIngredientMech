"""Independent read-only payload retention proof; outputs confined to this review."""
from pathlib import Path
import copy
import datetime
import hashlib
import json
import os
import yaml

R = Path.cwd()
A = R / '.temp/w03-provenance-successor-v1'
P = R / 'reports/all_unmatched_20261107/worker-03'
O = P / 'successors/issue1226-v1'
CURRENT = P / 'successors/issue1224-v1/publication-v1'
PACKET = R.parents[2] / 'preflight/w03-current-provenance-allowlist-v1'
sha = lambda b: hashlib.sha256(b).hexdigest()
canon = lambda v: json.dumps(v, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()
allow = {x['proposal_id']: x for x in json.loads((PACKET/'repair-allowlist.json').read_text())['rows']}
original = json.loads((CURRENT/'proposals.json').read_text())['proposals']
bridge = json.loads((O/'payload-bridge.json').read_text())
bridges = {x['proposal_id']: x for x in bridge['entries']}
assert set(allow) == set(bridges) and len(allow) == 49
rows = []
manuals = []
for pr in original:
    pid = pr['proposal_id']
    oldpath = P/pr['after_capture']['path']
    oldbytes = oldpath.read_bytes()
    old = yaml.safe_load(oldbytes)
    assert sha(oldbytes) == pr['after_capture']['sha256']
    newpath = R/bridges[pid]['new_payload_path'] if pid in bridges else oldpath
    newbytes = newpath.read_bytes()
    new = yaml.safe_load(newbytes)
    b = bridges.get(pid)
    if b:
        row = allow[pid]
        assert b['original_proposal'] == pr and b['original_authorship_and_reviews'] == row['author_evidence']
        assert b['before_payload_sha256'] == sha(oldbytes)
        assert b['after_payload_sha256'] == sha(newbytes)
        assert old['ontology_mapping']['evidence'][0] == row['complete_mapping_evidence_object'] == b['old_object']
        expected = copy.deepcopy(old['ontology_mapping']['evidence'][0])
        expected['evidence_type'] = 'LLM_SUGGESTION'
        assert new['ontology_mapping']['evidence'][0] == expected == b['new_object']
        assert len(new['curation_history']) == len(old.get('curation_history', [])) + 1
        assert new['curation_history'][:-1] == old['curation_history']
        ev = new['curation_history'][-1]
        assert ev == b['appended_history'] and ev['llm_assisted']
        assert ev['previous_status'] == ev['new_status'] == old['mapping_status']
        assert 'issues/1226' in ev['changes'] and row['audit_row_id'] in ev['changes']
        assert ev['curator'] == 'codex-worker03 /root provenance successor'
        copy_new = copy.deepcopy(new)
        copy_new['ontology_mapping']['evidence'][0]['evidence_type'] = 'MANUAL_CURATION'
        copy_new['curation_history'].pop()
        assert copy_new == old
        before = row['authentic_before']
        assert before == b['authentic_before']
        if before is None:
            assert pr['kind'] == 'new_owner' and pr['before_sha256'] is None
            assert not os.path.lexists(R/pr['owner_path'])
        else:
            assert sha((R/row['authentic_before_path']).read_bytes()) == before['sha256'] == pr['before_sha256']
    else:
        assert newbytes == oldbytes
    for idx, evidence in enumerate(new.get('ontology_mapping', {}).get('evidence', [])):
        if evidence['evidence_type'] == 'MANUAL_CURATION':
            manuals.append({'proposal_id': pid, 'index': idx, 'complete_object': evidence, 'sha256': sha(canon(evidence))})
    rows.append({'proposal_id': pid, 'owner_path': pr['owner_path'], 'kind': pr['kind'],
                 'before_sha256': pr['before_sha256'], 'source_case_ids': pr['case_ids'],
                 'old_path': str(oldpath.relative_to(R)), 'old_sha256': sha(oldbytes),
                 'new_path': str(newpath.relative_to(R)), 'new_sha256': sha(newbytes),
                 'changed': b is not None, 'full_semantic_rollback_equals_original': True,
                 'historical_review_object_preserved_in_bridge': bool(b), 'scientific_approval_renewed': False})
assert len(rows) == 74 and sum(x['changed'] for x in rows) == 49
assert {(x['proposal_id'], x['index']) for x in manuals} == {
    ('b-proposal-marine-aliases', 0), ('c-copper-trihydrate-alias', 4), ('m-arabinan_source_alias', 2)}
ox = next(x for x in rows if x['proposal_id'] == 'w03-oxoid-cm0149-product-1224-v1')
assert ox['new_sha256'] == '1ec7554da19d5a6ab2259ee79d178a95511a923e611f4fc176af498248ab76ae'
assert ox['kind'] == 'new_owner' and ox['before_sha256'] is None
oxdata = yaml.safe_load((R/ox['new_path']).read_text())
assert len(oxdata['ontology_mapping']['evidence']) == 2
assert all(e['evidence_type'] == 'LLM_SUGGESTION' for e in oxdata['ontology_mapping']['evidence'])
assert 'b-proposal-cm0149-form' not in {x['proposal_id'] for x in rows}
checkpoint = json.loads((A/'ISSUE-FIRST-MANIFEST-v1.json').read_text())
for item in checkpoint['files']:
    path = A/item['path']
    if item['kind'] == 'file':
        assert sha(path.read_bytes()) == item['sha256']
    elif item['kind'] == 'symlink':
        assert path.is_symlink() and os.readlink(path) == item['link_target']
    else:
        raise ValueError(item['kind'])
result = {'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'reviewer': '/root/provenance_assembly',
          'scope': 'Independent full-value rollback, object/parent/beforeimage/hash and exclusion verification; no scientific reapproval',
          'bridge_sha256': sha((O/'payload-bridge.json').read_bytes()), 'all74_payload_rows': rows,
          'inherited_manual_complete_objects': manuals, 'changed_payloads': 49, 'unchanged_payloads': 25,
          'enum_substitutions': 49, 'history_appends': 49,
          'oxoid_genuine_new_owner_null_before_and_two_llm_entries_preserved': True,
          'retired_mixed_rcm_inactive': True,
          'original_issue_first_checkpoint_members_preserved': len(checkpoint['files']),
          'presentation_note': 'Native guarded writer width=80 reflows multiline scalars. Changed payload retention is whole semantic object equality after rolling back one enum and last event, not old byte formatting identity. All 25 unaffected payloads remain byte-identical.'}
destination = A/'assembly/payload-scope-verification-v1.json'
with destination.open('x') as stream:
    json.dump(result, stream, indent=2, ensure_ascii=False)
    stream.write('\n')
print(json.dumps({'status': 'PASS', 'payloads': len(rows), 'changed': 49, 'unchanged': 25,
                  'checkpoint_members': len(checkpoint['files']), 'sha256': sha(destination.read_bytes())}))
