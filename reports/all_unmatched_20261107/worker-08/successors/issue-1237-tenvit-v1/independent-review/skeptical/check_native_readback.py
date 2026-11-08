"""Bounded final native serialization/binding check, without native writes."""
from pathlib import Path
import datetime
import hashlib
import json
import yaml

W = Path.cwd()
A = W / 'reports/all_unmatched_20261107/worker-08'
S = A / 'successors/issue-1237-tenvit-v1'
N = S / 'native'
O = W / '.temp/all-unmatched-worker-08/tenvit-dependent-v1/independent-skeptical'
R = W / 'reviews/structured/20261108T091922Z-w08-tenvit-dependent-successor'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
js = lambda p: json.loads(Path(p).read_text())
def ref(p):
    return {'path': str(Path(p).relative_to(W)), 'sha256': sha(p)}
checks = []
def ck(name, condition):
    checks.append({'check': name, 'pass': bool(condition)})
    assert condition, name

d = yaml.safe_load((R / 'review.yaml').read_text())
md = (R / 'review.md').read_text()
receipt = js(N / 'receipt.json')
content = [js(N / p) for p in ['review-content.json', 'review-content-v2.json', 'review-content-v3.json']]
inspection = js(N / 'inspection-v3.json')
selector = js(S / 'selection.json')
final = js(O / 'final-bindings.json')
tech = js(S / 'validation/receipt.json')
ck('native YAML exact supplied hash', sha(R / 'review.yaml') == '4234f107b81eb50ba711f32cdb446292f1e63e734d821a4f60f718a86d596dff')
ck('native Markdown exact supplied hash', sha(R / 'review.md') == 'e3ed592bba293cec70072b0898e6555cbf2df6553e8afda2d0aa52913521ef25')
ck('native receipt exact pair bindings', receipt['review_yaml'] == ref(R / 'review.yaml') and receipt['review_markdown'] == ref(R / 'review.md'))
ck('saved YAML exactly equals final content object', d == content[2])
embedded = md.split('```yaml\n', 1)[1].rsplit('```', 1)[0]
ck('complete Markdown structured record equals YAML', yaml.safe_load(embedded) == d)
ck('source inspected exact', d['source'] == inspection['source'])
ck('351 input entries with unique paths', len(d['source']['inputs']) == len({x['path'] for x in d['source']['inputs']}) == receipt['input_count'] == 351)
input_rows = []
for row in d['source']['inputs']:
    ck('actual current native input hash: ' + row['path'], sha(W / row['path']) == row['sha256'])
    input_rows.append(row)
ck('working tree state is accurately bounded', d['source']['git_revision'] == '79d44c84fe550741bbd8de00c119c48560f30bc1' and d['source']['state'] == 'working_tree')
pid = 'vm1237-prop-wolfe-cb-dependent'
ck('one exact proposed target only', len(d['targets']) == 1 and d['targets'][0]['target_id'] == pid and d['targets'][0]['path'] == str((S/'payloads/Wolfes_Vitamin_Mix.yaml').relative_to(W)))
ck('scope does not review all prior payloads', d['scope']['population_size'] == 1 and d['scope']['reviewed_target_ids'] == [pid] and 'preservation bridge only' in d['scope']['description'])
ck('bounded verdict with no fabricated new findings', d['completion'] == 'completed' and d['verdict'] == 'pass_with_limitations' and d['findings'] == [])
ck('actual reviewer authorship separated', 'worker08:/root/inorganics' in d['reviewer']['identity'] and 'worker08:/root/organics' in d['reviewer']['identity'] and 'root composed-successor author' in d['reviewer']['independence_basis'])
ck('coordinator follow-up invents no finding closure', d['actions'][0]['finding_ids'] == [] and 'preserve all scientific and export holds' in d['actions'][0]['description'])

ev = {x['evidence_id']: x for x in d['evidence']}
ck('unique native evidence IDs', len(ev) == len(d['evidence']))
for row in d['evidence']:
    path = W / row['locator']
    ck('actual native evidence capture hash: ' + row['evidence_id'], sha(path) == row['snapshot_sha256'])
for row in d['assessments'] + d['checks']:
    ck('native cited evidence IDs exist: ' + row.get('assessment_id', row.get('check_id')), set(row['evidence_ids']) <= set(ev))
    ck('native assessment/check only scoped target: ' + row.get('assessment_id', row.get('check_id')), row['target_ids'] == [pid])
ck('initial skeptical receipt exact', ev['SKEPTIC']['snapshot_sha256'] == sha(O / 'review.json') == '9add6d629ec5529d46aec5e82a31d12d7898d85638157cfec8b16eb912eb8649')
ck('final skeptical binding receipt exact', ev['SKEPTIC-FINAL']['snapshot_sha256'] == sha(O / 'final-bindings.json') == '24f852243954e6bb1e165e95eae62bbb79810eef8284b53c3095ee31298c3a45')
ck('selector unchanged from independently checked final selection', sha(S / 'selection.json') == final['selection']['sha256'] == 'fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699')
for path, expected in final['input_hashes'].items():
    ck('prior final input binding remains exact: ' + path, sha(A / path) == expected)
ck('native full target payload remains reviewed exact bytes', sha(S / 'payloads/Wolfes_Vitamin_Mix.yaml') == final['final_payload_sha256'] == 'b64eccf46c271520c27c73bc0a5863e2bc56447d1acf7461a90e3d72f9f4384f')
for i, row in enumerate(js(S / 'primary/capture-bindings.json')):
    native = ev[f'PRIMARY-{i}']
    ck(f'primary {i} actual capture hash unchanged', native['snapshot_sha256'] == row['published_capture']['sha256'])
    t1 = datetime.datetime.fromisoformat(native['accessed_at'].replace('Z', '+00:00'))
    t2 = datetime.datetime.fromisoformat(row['original_accessed_at'])
    ck(f'primary {i} exact original instant', t1 == t2)

# Verify envelope-only changes in the preserved failed-draft lineage.
a, b, c = content
ck('draft1 to draft2 only stated envelope keys', {k for k in a.keys() | b.keys() if a.get(k) != b.get(k)} == {'finished_at', 'source', 'actions', 'review_id', 'notes'})
ck('draft1 action only adds required empty finding list', b['actions'] == [{**a['actions'][0], 'finding_ids': []}])
ck('draft2 to draft3 only stated envelope keys', {k for k in b.keys() | c.keys() if b.get(k) != c.get(k)} == {'finished_at', 'source', 'review_id', 'notes'})
ck('draft3 converts notes and preserves first note', isinstance(b['notes'], str) and c['notes'][0] == b['notes'] and len(c['notes']) == 2)
for i, (old, new) in enumerate(zip(content, content[1:])):
    oldmap = {x['path']: x for x in old['source']['inputs']}
    newmap = {x['path']: x for x in new['source']['inputs']}
    ck(f'draft{i+1} input bytes unchanged in successor', all(newmap.get(k) == v for k, v in oldmap.items()))
    ck(f'draft{i+1} only four preserved failure-envelope inputs added', len(set(newmap)-set(oldmap)) == 4 and all('/native/' in x or '/provenance/' in x for x in set(newmap)-set(oldmap)))
ck('actual first failure matches explanation', "'finding_ids' is a required property" in (S/'provenance/native-build-attempt1.log').read_text())
ck('actual second failure matches explanation', "is not of type 'array', 'null'" in (S/'provenance/native-build-attempt2.log').read_text())
for row in receipt['rejected_drafts_preserved']:
    ck('rejected draft exact bytes retained: ' + row['path'], sha(W / row['path']) == row['sha256'])

ck('technical receipt binds actual final selector', tech['selection']['sha256'] == sha(S / 'selection.json'))
ck('technical execution is not scientific approval', tech['independent_scientific_review'] is False and tech['scientific_approval'] is False and tech['owner_admission_approval'] is False and tech['release_approval'] is False)
ck('failed admission stays held', tech['owner_admission_status'] == 'FAILED/HELD' and all(x['gate_status'] == 'failed' and x['maintained_admission'] == 'HELD' for x in tech['owner_admission_failures']))
ck('full SSSOM equality not falsely asserted', tech['wolfe_full_sssom_row_equal'] is False and tech['wolfe_sssom_identity_predicate_alias_projection_unchanged'] is True and set(tech['wolfe_expected_provenance_delta']) == {'source','mapping_date'})
limits = '\n'.join(d['limitations'])
for phrase in ['does not close issue1237', 'calcium-pantothenate D/DL', 'approval of whole child records', 'carrier/preparation remains unknown', 'TSB/Bacto FAILED/HELD', 'release approval']:
    ck('native explicit limit: ' + phrase, phrase in limits)

out = {
    'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'status': 'PASS', 'reviewer': 'worker08:/root/inorganics', 'assembler_author': 'worker08:/root',
    'scope': 'Bounded exact saved-native-pair readback against this reviewer\'s sealed whole-payload/source-case receipt and final aggregate receipt. This is serialization, evidence, current-input and scope verification, not a new scientific approval or a rerun of the technical executor\'s validators.',
    'native_yaml': ref(R/'review.yaml'), 'native_markdown': ref(R/'review.md'), 'native_receipt': ref(N/'receipt.json'),
    'selection': ref(S/'selection.json'), 'initial_review': ref(O/'review.json'), 'final_bindings': ref(O/'final-bindings.json'),
    'check_count': len(checks), 'checks': checks, 'actual_native_input_count': len(input_rows), 'actual_native_input_hashes': input_rows,
    'assessment': 'The actual saved native record has one proposed full-payload target and the six-occurrence W08 source-case scope. It accurately cites both independent reviewers and the final selected indices. Its five scientific/accounting assessments preserve generic lipoic-acid scope, CB-only cyanocobalamin, calcium D/DL uncertainty, UNKNOWN carrier/preparation, W09/root authorship, authentic original NBRC903 null-before origin, zero CB campaign observations and central W06/W08 duplicate reconciliation. The other 113 payloads and 187 cases receive only preservation continuity. Empty findings is explicitly not issue closure. Legacy roles, child whole-owner approval and failed TSB/Bacto admission remain held.',
    'failed_draft_assessment': 'Both rejected drafts and actual validation errors are preserved. V2 adds the required empty finding_ids list and explanatory note; V3 changes notes to the required list. Review ID/time and actual inspection provenance change with those attempts. All scientific assessments, evidence objects, payloads and selected indices remain unchanged across the envelope corrections.',
    'technical_receipt_assessment': 'The technical executor truthfully distinguishes bounded checks from scientific and admission approval. Full-row SSSOM equality is false because the appended history changes curator/date provenance; identity, label, predicate and aliases remain unchanged. The review does not claim a canonical export, whole maintained SSSOM pass or owner admission.',
    'new_findings': [], 'maintained_application_approved': False, 'whole_owner_role_export_approval': False,
    'limitations': ['No native validator or full catalog validator was rerun by this reviewer.', 'All 351 native input files were hashed as exact binding checks; this does not claim fresh scientific inspection of every preserved artifact or this reviewer\'s own inorganic payloads.', 'No commit, push, live remote state or coordinator final-head acceptance is attested here.']
}
dest = O / 'native-readback.json'
assert not dest.exists()
dest.write_text(json.dumps(out, indent=2, ensure_ascii=False, allow_nan=False)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'native_inputs':len(input_rows),'receipt':str(dest),'sha256':sha(dest)},indent=2))
