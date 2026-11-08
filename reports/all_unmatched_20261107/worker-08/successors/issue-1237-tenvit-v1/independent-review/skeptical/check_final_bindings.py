"""Independent aggregate readback; never writes author or maintained files."""
import datetime
import hashlib
import json
from pathlib import Path

W = Path.cwd()
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
A = W / 'reports/all_unmatched_20261107/worker-08'
S = A / 'successors/issue-1237-tenvit-v1'
OLD = A / 'successors/issue-1227-plain-flour-v1'
O = W / '.temp/all-unmatched-worker-08/tenvit-dependent-v1/independent-skeptical'

def no_duplicates(pairs):
    d = {}
    for key, value in pairs:
        if key in d:
            raise AssertionError('duplicate JSON key: ' + key)
        d[key] = value
    return d

def js(p):
    return json.loads(Path(p).read_text(), object_pairs_hook=no_duplicates)

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def canon(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()).hexdigest()

checks = []
def ck(name, condition):
    checks.append({'check': name, 'pass': bool(condition)})
    assert condition, name

def ref(p):
    return {'root': 'artifact', 'path': str(Path(p).relative_to(A)), 'sha256': sha(p)}

selection = js(S / 'selection.json')
ck('exact immutable final selection', sha(S / 'selection.json') == 'fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699')
ck('predecessor selector bound', selection['predecessor_selection'] == ref(OLD / 'selection.json'))
for name, row in selection['authoritative_inputs'].items():
    ck('selection input exact: ' + name, row == ref(S / name))
for role, row in selection['independent_reviews'].items():
    ck('exact copied peer receipt: ' + role, sha(A / row['path']) == row['sha256'])
ck('own initial peer receipt exact copy', sha(O / 'review.json') == selection['independent_reviews']['skeptical']['sha256'] == '9add6d629ec5529d46aec5e82a31d12d7898d85638157cfec8b16eb912eb8649')

d = js(S / 'decisions.json')
p = js(S / 'proposals.json')
e = js(S / 'evidence.json')
old_d = js(OLD / 'decisions.json')
old_p = js(OLD / 'proposals.json')
old_e = js(OLD / 'evidence.json')
lineage = js(S / 'lineage.json')
cid = selection['changed_case_id']
pid = selection['new_dependent_proposal']
for new, old, key in [(d, old_d, 'decisions'), (p, old_p, 'proposals'), (e, old_e, 'evidence')]:
    ck('unchanged container metadata: ' + key, {k:v for k,v in new.items() if k != key} == {k:v for k,v in old.items() if k != key})
ck('exact final/old case counts', len(d['decisions']) == len(old_d['decisions']) == 188)
ck('exact final/old proposal counts', len(p['proposals']) == 114 and len(old_p['proposals']) == 113)
ck('exact final/old evidence counts', len(e['evidence']) == 1101 and len(old_e['evidence']) == 1082)
ck('entire original evidence prefix preserved', e['evidence'][:1082] == old_e['evidence'])
ck('entire original proposal prefix preserved', p['proposals'][:113] == old_p['proposals'])
ck('all case IDs and original order preserved', [x['case_id'] for x in d['decisions']] == [x['case_id'] for x in old_d['decisions']])
decision_index = {x['case_id']: x for x in d['decisions']}
proposal_index = {x['proposal_id']: x for x in p['proposals']}
evidence_index = {x['evidence_id']: x for x in e['evidence']}
ck('unique case IDs', len(decision_index) == 188)
ck('unique proposal IDs', len(proposal_index) == 114)
ck('unique evidence IDs', len(evidence_index) == 1101)
shard = js(C / 'queue/preliminary-v5/shards/shard-08.json')
cases = shard['cases']
frozen = {x['case_id']: x for x in cases}
ck('exact frozen shard byte binding', sha(C / 'queue/preliminary-v5/shards/shard-08.json') == selection['frozen_shard_sha256'])
ck('exact frozen case coverage', set(frozen) == set(decision_index))
case_rows = []
lineage_cases = {x['case_id']: x for x in lineage['cases']}
for before, after in zip(old_d['decisions'], d['decisions'], strict=True):
    key = after['case_id']
    ck('case frozen digest: ' + key, after['case_input_sha256'] == canon(frozen[key]))
    ck('case original occurrences: ' + key, after['occurrence_ids'] == before['occurrence_ids'])
    ck('case original source: ' + key, after['source'] == before['source'])
    ck('case lineage hashes: ' + key, lineage_cases[key]['before_sha256'] == canon(before) and lineage_cases[key]['after_sha256'] == canon(after))
    ck('case lineage frozen evidence: ' + key, lineage_cases[key]['case_input_sha256'] == after['case_input_sha256'] and lineage_cases[key]['occurrence_ids'] == after['occurrence_ids'])
    ck('case intended change only: ' + key, (before == after) == (key != cid) == lineage_cases[key]['unchanged'])
    ck('case proposal backlinks exist: ' + key, set(after['proposal_ids']) <= set(proposal_index))
    ck('case evidence backlinks exist: ' + key, set(after['evidence_ids']) <= set(evidence_index))
    case_rows.append({'case_id': key, 'canonical_sha256': canon(after), 'frozen_input_sha256': after['case_input_sha256'], 'unchanged_from_published_original': before == after, 'review_scope': 'Exact full-object preservation and frozen-input binding; fresh scientific appraisal is only the changed case.'})
ck('320 exact occurrence IDs', sum(len(x['occurrence_ids']) for x in d['decisions']) == 320)
ck('unique frozen occurrence IDs', len({oid for x in d['decisions'] for oid in x['occurrence_ids']}) == 320)

author_d = js(S / 'author/decision.json')
author_p = js(S / 'author/proposal.json')
final_d = decision_index[cid]
final_p = proposal_index[pid]
metadata_suffix = ['vm1237-source-partitions', 'vm1237-science', 'vm1237-skeptical'] + [f'vm1237-primary-{i:02}' for i in range(10)]
for label, author, final, allowed in [('decision', author_d, final_d, {'evidence_ids', 'independent_review'}), ('proposal', author_p, final_p, {'evidence_ids'})]:
    ck(label + ' only permitted metadata differs', {k for k in author.keys() | final.keys() if author.get(k) != final.get(k)} == allowed)
    ck(label + ' exact permitted evidence suffix', final['evidence_ids'] == author['evidence_ids'] + metadata_suffix)
ck('final current peer completion exact', final_d['independent_review'] == {'status': 'complete', 'evidence_ids': ['vm1237-science', 'vm1237-skeptical']})
ck('original NBRC903 new-owner kind/null before retained', proposal_index['vm1201-prop-nbrc903-vitamin']['kind'] == 'new_owner' and proposal_index['vm1201-prop-nbrc903-vitamin']['before_sha256'] is None)
ck('new dependent exact genuine beforeimage', final_p['kind'] == 'edit_existing_owner' and final_p['before_sha256'] == sha(S / 'beforeimages/Wolfes_Vitamin_Mix.yaml') == '709749bd7c83c38a09400fc1893885ead753847ff9d1cbbe4ec76b431d349738')
ck('only actual W08 case on new dependent', final_p['case_ids'] == [cid])
ck('only NBRC903 trigger and zero CB membership', final_p['source_occurrence_ids'] == ['CM_OCC:a181b24b7eb91c50c771bd1c1fc3012fd0cf28f45b49f2750c3d43bda9cdd531'] and final_p['cb_campaign_occurrence_count'] == 0)

payload_rows = []
lineage_payloads = {x['proposal_id']: x for x in lineage['payloads']}
for index, row in enumerate(p['proposals']):
    key = row['proposal_id']
    cap = row['after_capture']
    ck('payload capture scope: ' + key, cap['root'] == 'artifact')
    ck('actual entire payload SHA: ' + key, sha(A / cap['path']) == cap['sha256'])
    ck('proposal cases exist: ' + key, set(row['case_ids']) <= set(decision_index))
    ck('proposal evidence exists: ' + key, set(row['evidence_ids']) <= set(evidence_index))
    ck('proposal reverse case backlink: ' + key, all(key in decision_index[x]['proposal_ids'] for x in row['case_ids']))
    lin = lineage_payloads[key]
    ck('payload lineage capture: ' + key, lin['selected_capture'] == cap)
    ck('payload lineage owner/before: ' + key, lin['owner_path'] == row['owner_path'] and lin['original_before_sha256'] == row['before_sha256'])
    if key != pid:
        ck('original proposal lineage SHA: ' + key, lin['original_proposal_object_sha256'] == canon(row) and lin['unchanged_proposal_object'] and lin['unchanged_payload'])
    payload_rows.append({'proposal_id': key, 'canonical_proposal_sha256': canon(row), 'owner_path': row['owner_path'], 'before_sha256': row['before_sha256'], 'after_capture': cap, 'review_scope': 'Exact original bytes and provenance retained, without renewed scientific approval.' if key != pid else 'Exact full payload independently scientifically reviewed in sealed review.json.'})
ck('final full payload still exact reviewed bytes', final_p['after_capture']['sha256'] == 'b64eccf46c271520c27c73bc0a5863e2bc56447d1acf7461a90e3d72f9f4384f')

new_e = e['evidence'][1082:]
ck('nineteen added evidence entries', len(new_e) == 19)
for row in new_e:
    cap = row['capture']
    ck('new evidence capture exact: ' + row['evidence_id'], cap['root'] == 'artifact' and sha(A / cap['path']) == cap['sha256'])
    ck('new evidence exact case scope: ' + row['evidence_id'], row['case_ids'] == [cid])
    ck('new evidence case/proposal backlinks: ' + row['evidence_id'], row['evidence_id'] in final_p['evidence_ids'] and row['evidence_id'] in final_d['evidence_ids'])

source_log = js(O / 'source-read-ledger.json')['primary_and_frozen_source_reads']
original_by_path = {x['capture']['path']: x for x in source_log}
capture_rows = []
cb = js(S / 'primary/capture-bindings.json')
ck('ten original primary copies', len(cb) == 10)
for row in cb:
    key = row['evidence_id']
    primary = original_by_path[row['original_path']]
    cap = row['published_capture']
    ev = evidence_index[key]
    ck('primary copy byte equality: ' + key, sha(row['original_path']) == sha(A / cap['path']) == cap['sha256'] == primary['capture']['sha256'])
    ck('primary timestamp exact: ' + key, row['original_accessed_at'] == primary['original_accessed_at'] == ev['original_acquisition_at'])
    ck('primary evidence capture exact: ' + key, ev['capture'] == cap)
    if key != 'vm1237-primary-09':
        ck('primary URL and access exact: ' + key, ev['url'] == primary['url'] and ev['accessed_at'] == primary['original_accessed_at'])
    else:
        ck('CB snapshot does not invent remote acquisition', ev['kind'] == 'source_snapshot' and ev['url'] is None and 'accessed_at' not in ev)
    capture_rows.append({**row, 'actual_read_scope': primary['read_scope'], 'no_new_retrieval_claim': True})

ck('selection preserves failure/hold boundary', selection['maintained_application'] is False and selection['whole_owner_role_export_approval'] is False and 'FAILED/HELD' in selection['prior_TSB_Bacto_admission'])
ck('lineage preserves release boundary', lineage['release_approval'] is False)
counts = {'cases': len(d['decisions']), 'proposals': len(p['proposals']), 'occurrence_ids': 320, 'evidence': len(e['evidence']), 'unchanged_original_payloads': 113, 'new_dependent_payloads': 1, 'changed_cases': 1, 'unchanged_cases': 187}
ck('selection counts independently reproduced', selection['counts'] == counts)
out = {
    'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'status': 'PASS', 'reviewer': 'worker08:/root/inorganics', 'author': 'worker08:/root',
    'scope': 'Final selected-index/source binding review after sealed independent scientific review. Every final case/proposal/evidence object was parsed; every original case/proposal/evidence object was compared in full. This is not a repeated scientific review or approval of the other 113 payloads, including this reviewer\'s authored inorganic proposals.',
    'selection': ref(S / 'selection.json'), 'input_hashes': {str(p.relative_to(A)):sha(p) for p in [S/'selection.json', S/'decisions.json', S/'proposals.json', S/'evidence.json', S/'lineage.json', S/'primary/capture-bindings.json']},
    'sealed_initial_review': {'path': str(O / 'review.json'), 'sha256': sha(O / 'review.json')},
    'counts': counts, 'check_count': len(checks), 'checks': checks,
    'final_case_canonical_sha256': canon(final_d), 'final_proposal_canonical_sha256': canon(final_p), 'final_payload_sha256': final_p['after_capture']['sha256'],
    'full_case_bindings': case_rows, 'full_proposal_payload_bindings': payload_rows, 'primary_capture_bindings': capture_rows,
    'changed_case_and_proposal_appraisal': 'Actual final scientific prose, six-occurrence partition, authentic existing-owner preimage, zero CB observation count, new-owner NBRC903 origin and hold/dependency text exactly match the reviewed author objects. Only the permitted source/peer evidence suffix and case review-completion object were added. The new raw captures are exact copies at their original acquisition times.',
    'source_preparation_and_owner_limits': 'All prior source, molecular-form, role, child-owner, exact-stock association and export holds remain. Current source correction does not approve the W06/W08 nominal duplicate candidates, declare CB stock equality or change any receiving dose. Unrelated whole-owner approval is not renewed.',
    'new_findings': [], 'native_pair_status': 'PENDING_SEPARATE_EXACT_READBACK', 'maintained_application': False, 'whole_owner_role_export_approval': False
}
dest = O / 'final-bindings.json'
assert not dest.exists()
dest.write_text(json.dumps(out, indent=2, ensure_ascii=False, allow_nan=False) + '\n')
print(json.dumps({'status':'PASS','checks':len(checks),'counts':counts,'receipt':str(dest),'sha256':sha(dest)},indent=2))
