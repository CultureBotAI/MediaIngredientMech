"""Independent whole-value comparison for the bounded W03 #1226 successor.

This script does not import the author writer or use its retention assertion.
Only this review directory is writable; source and candidate bytes are read.
"""
from pathlib import Path
import collections, copy, datetime, hashlib, json, subprocess, sys
import yaml

R = Path.cwd()
O = R / '.temp/w03-provenance-successor-v1/review'
W = R / 'reports/all_unmatched_20261107/worker-03'
S = W / 'successors/issue1224-v1/publication-v1'
N = W / 'successors/issue1226-v1'
Q = R.parents[2] / 'preflight/w03-current-provenance-allowlist-v1'
HEAD = 'f6bfbf3c185f705484aa106405f813209146c766'
BASE = 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
sys.path.insert(0, str(R / 'src'))
from mediaingredientmech.validation.write_validated import validate_ingredient

def sha(b): return hashlib.sha256(b).hexdigest()
def canon(x): return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()
def read(p): return json.loads(p.read_bytes())
def git(*args): return subprocess.check_output(['git', *args])
def save(name, obj):
    with (O / name).open('x') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write('\n')

assert git('rev-parse', 'HEAD').decode().strip() == HEAD
allow = read(Q / 'repair-allowlist.json')
assert sha((Q / 'repair-allowlist.json').read_bytes()) == '9b8283520ab7f9911f4997d62a85aea798f634bd8e8ed69c60dd77a26cdeec9d'
allowrows = {x['proposal_id']: x for x in allow['rows']}
bridge = read(N / 'payload-bridge.json')
entries = {x['proposal_id']: x for x in bridge['entries']}
oldprops = read(S / 'proposals.json')['proposals']
assert len(allowrows) == len(entries) == 49
assert set(entries) == set(allowrows)
assert len(oldprops) == 74
assert bridge['selected_predecessor_head'] == HEAD
assert bridge['new_source_science_approval'] is False
inputs = {}
rows = []
manuals = []
history_events = []
all_schema_errors = []
for p in oldprops:
    pid = p['proposal_id']
    oldpath = W / p['after_capture']['path']
    oldbytes = oldpath.read_bytes()
    assert oldbytes == git('show', HEAD + ':' + str(oldpath.relative_to(R)))
    assert sha(oldbytes) == p['after_capture']['sha256']
    old = yaml.safe_load(oldbytes)
    inputs[str(oldpath.relative_to(R))] = sha(oldbytes)
    authentic = None
    if p['kind'] == 'edit_existing_owner':
        before = git('show', BASE + ':' + p['owner_path'])
        assert before == (R / p['owner_path']).read_bytes()
        assert sha(before) == p['before_sha256']
        authentic = sha(before)
    else:
        assert p['kind'] == 'new_owner'
        assert p['before_sha256'] is None
        assert not (R / p['owner_path']).exists()
    if pid in entries:
        b = entries[pid]
        a = allowrows[pid]
        newpath = R / b['new_payload_path']
        assert newpath.parent == N / 'payloads'
        assert newpath.name == pid + '.yaml'
        newbytes = newpath.read_bytes()
        new = yaml.safe_load(newbytes)
        assert b['before_payload_sha256'] == sha(oldbytes) == a['payload']['sha256']
        assert b['after_payload_sha256'] == sha(newbytes) == b['after_capture']['sha256']
        assert W / b['after_capture']['path'] == newpath
        assert b['original_proposal'] == p
        assert b['original_authorship_and_reviews'] == a['author_evidence']
        assert b['authentic_before'] == a['authentic_before']
        assert old['ontology_mapping']['evidence'][0] == b['old_object'] == a['complete_mapping_evidence_object']
        assert new['ontology_mapping']['evidence'][0] == b['new_object']
        assert sha(canon(b['old_object'])) == b['old_object_sha256'] == a['complete_object_canonical_sha256']
        assert sha(canon(b['new_object'])) == b['new_object_sha256']
        expected = copy.deepcopy(old)
        expected['ontology_mapping']['evidence'][0]['evidence_type'] = 'LLM_SUGGESTION'
        assert len(new['curation_history']) == len(old['curation_history']) + 1
        event = new['curation_history'][-1]
        assert event == b['appended_history']
        assert event['action'] == 'CORRECTED_EVIDENCE_PROVENANCE'
        assert event['curator'] == 'codex-worker03 /root provenance successor'
        assert event['llm_assisted'] is True
        assert event['previous_status'] == event['new_status'] == old['mapping_status'] == 'MAPPED'
        assert 'issues/1226' in event['changes'] and a['audit_row_id'] in event['changes']
        assert 'no identity, role or export reapproval' in event['changes']
        timestamp = datetime.datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00'))
        assert timestamp.tzinfo and timestamp <= datetime.datetime.now(datetime.timezone.utc)
        expected['curation_history'].append(event)
        assert new == expected, pid + ': unauthorized complete-value difference'
        # Independently compute scientific/full-field invariance; do not trust author projection.
        restored = copy.deepcopy(new)
        restored['ontology_mapping']['evidence'][0]['evidence_type'] = 'MANUAL_CURATION'
        restored['curation_history'].pop()
        assert restored == old
        parent = {k: v for k, v in new['ontology_mapping'].items() if k != 'evidence'}
        assert parent == b['parent_context'] == a['parent_context']
        assert sha(canon(old['curation_history'])) == b['before_history_sha256'] == a['history_prefix_sha256']
        errors = [str(x) for x in validate_ingredient(new)]
        assert not errors, (pid, errors)
        all_schema_errors.extend(errors)
        history_events.append({'proposal_id': pid, 'event': event})
        changed = True
    else:
        newpath, newbytes, new = oldpath, oldbytes, old
        changed = False
    inputs[str(newpath.relative_to(R))] = sha(newbytes)
    for i, ev in enumerate(new.get('ontology_mapping', {}).get('evidence', [])):
        if ev.get('evidence_type') == 'MANUAL_CURATION':
            manuals.append({'proposal_id': pid, 'index': i, 'object': ev, 'sha256': sha(canon(ev))})
    rows.append({'proposal_id': pid, 'owner_path': p['owner_path'], 'kind': p['kind'],
                 'authentic_before_sha256': authentic, 'case_ids': p['case_ids'],
                 'old_path': str(oldpath.relative_to(R)), 'old_sha256': sha(oldbytes),
                 'new_path': str(newpath.relative_to(R)), 'new_sha256': sha(newbytes),
                 'changed': changed, 'complete_record_retention': 'PASS',
                 'old_complete_record_sha256': sha(canon(old)),
                 'restored_complete_record_sha256': sha(canon(restored)) if changed else sha(canon(new)),
                 'new_complete_record_sha256': sha(canon(new)),
                 'scientific_review': False,
                 'bounded_disposition': 'Accept exact enum correction and honest appended history only' if changed else 'Byte-identical selection retained, not scientifically reapproved'})
assert sum(x['changed'] for x in rows) == 49
assert {(x['proposal_id'], x['index']) for x in manuals} == {
    ('b-proposal-marine-aliases', 0), ('c-copper-trihydrate-alias', 4), ('m-arabinan_source_alias', 2)}
initial = read(O / 'original-provenance-reconstruction.json')
prior_manual = {(x['proposal_id'], x['index']): x['full_object'] for x in initial['inherited_exclusions']}
assert all(x['object'] == prior_manual[x['proposal_id'], x['index']] for x in manuals)
ox = next(x for x in rows if x['proposal_id'] == 'w03-oxoid-cm0149-product-1224-v1')
assert not ox['changed'] and ox['old_sha256'] == '1ec7554da19d5a6ab2259ee79d178a95511a923e611f4fc176af498248ab76ae'
assert ox['kind'] == 'new_owner' and ox['authentic_before_sha256'] is None
oxrec = yaml.safe_load((R / ox['new_path']).read_bytes())
assert [x['evidence_type'] for x in oxrec['ontology_mapping']['evidence']] == ['LLM_SUGGESTION', 'LLM_SUGGESTION']
assert 'b-proposal-cm0149-form' not in {x['proposal_id'] for x in rows}
for name in ['payload-bridge.json', 'scientific-field-retention.json', 'validation/native-payloads.json']:
    p = N / name
    inputs[str(p.relative_to(R))] = sha(p.read_bytes())
for name in ['repair-allowlist.json', 'AUTHOR-TASK.md', 'MANIFEST.json']:
    p = N / 'context/allowlist' / name
    assert p.read_bytes() == (Q / name).read_bytes()
    inputs[str(p.relative_to(R))] = sha(p.read_bytes())
result = {'reviewer': '/root/provenance_review', 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'head_observed': HEAD, 'frozen_baseline': BASE, 'scientific_review': False,
          'status': 'PASS_EXACT_METADATA_PAYLOADS_ONLY', 'all74_payloads': rows,
          '49_actual_appended_events': history_events, 'three_inherited_manual_exclusions': manuals,
          'counts': {'changed_payloads': 49, 'unchanged_payloads': 25, 'complete_selection': 74,
                     'native_schema_validated_changed_payloads': 49, 'native_schema_errors': len(all_schema_errors)},
          'oxoid_unchanged_new_origin': ox, 'retired_mixed_rcm_active': False,
          'input_hashes': inputs,
          'scope_limits': ['Full field equality is a retention proof, not chemistry validation.',
                           'Prior source reviewers did not inspect these new bytes and are not repinned.',
                           'No owner, role, export, application, coalescence or release approval.',
                           'Final 188-case/core selection and final assembly need separate exact receipt.']}
save('candidate-payload-retention-v1.json', result)
print(json.dumps({'status': result['status'], 'counts': result['counts'],
                  'receipt_sha256': sha((O / 'candidate-payload-retention-v1.json').read_bytes())}, indent=2))
