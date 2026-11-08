"""Independent read-only assembly check; no native saver or corpus validators."""
from pathlib import Path
import json
import hashlib
import importlib.util
import datetime
import subprocess

W = Path.cwd()
O = W / 'reports/all_unmatched_20261107/worker-08/successors/issue-1237-tenvit-v1'
P = W / '.temp/all-unmatched-worker-08/tenvit-dependent-v1/independent-components'
N = W / 'reviews/structured/20261108T091922Z-w08-tenvit-dependent-successor'
private_technical = W / '.temp/all-unmatched-worker-08/tenvit-dependent-v1/validation'
inputs = {}
checks = []


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    path = Path(path)
    data = path.read_bytes()
    inputs[str(path)] = sha(data)
    return data


def load(path):
    return json.loads(read(path))


def ck(label, truth, detail=None):
    checks.append({'check': label, 'passed': bool(truth), 'detail': detail})


def pin(path, expected):
    data = read(path)
    ck('hash ' + str(path), sha(data) == expected)
    return data


selection = load(O / 'selection.json')
bindings = load(P / 'final-bindings.json')
ck('sealed final bindings pin', inputs[str(P / 'final-bindings.json')] ==
   '32751d2a956b2adedeb1385a23d93db0065bb9d71f2cae2977d18e801540b1ba')
ck('selection unchanged since independent readback',
   inputs[str(O / 'selection.json')] == bindings['selection']['sha256'])
native_receipt = load(O / 'native/receipt.json')
content = load(O / 'native/review-content-v3.json')
inspection = load(O / 'native/inspection-v3.json')
yaml_bytes = pin(N / 'review.yaml', '4234f107b81eb50ba711f32cdb446292f1e63e734d821a4f60f718a86d596dff')
markdown = pin(N / 'review.md', 'e3ed592bba293cec70072b0898e6555cbf2df6553e8afda2d0aa52913521ef25')
read(W / 'scripts/record_review.py')
read(W / 'schema/record_review.yaml')
read(W / 'docs/record-reviews.md')
read(W / 'docs/record-review-profile.md')
spec = importlib.util.spec_from_file_location('independent_native_review_helper', W / 'scripts/record_review.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
review = helper.load_document(yaml_bytes)
helper.validate_review(review)
ck('actual native validate_review', True)
rendered = helper.render_markdown(review).encode()
ck('actual native render_markdown exact saved bytes', rendered == markdown)
ck('saved YAML equals final content object', review == content)
ck('final inspection source and target objects exact',
   review['source'] == inspection['source'] and review['targets'] == inspection['targets'])
for key in ('review_yaml', 'review_markdown'):
    cap = native_receipt[key]
    pin(W / cap['path'], cap['sha256'])
ck('actual native source input count', len(review['source']['inputs']) == native_receipt['input_count'] == 351)
ck('native source working-tree provenance honest', review['source']['state'] == 'working_tree'
   and review['source']['git_revision'] == '79d44c84fe550741bbd8de00c119c48560f30bc1')
head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=W, capture_output=True, check=True, text=True).stdout.strip()
ck('current Git base equals inspected base', head == review['source']['git_revision'])
source_map = {}
for row in review['source']['inputs']:
    pin(W / row['path'], row['sha256'])
    source_map[row['path']] = row['sha256']
ck('source input uniqueness', len(source_map) == 351)
for e in review['evidence']:
    path = e['locator']
    pin(W / path, e['snapshot_sha256'])
    ck('native evidence input binding ' + e['evidence_id'], source_map[path] == e['snapshot_sha256'])

pid = selection['new_dependent_proposal']
cid = selection['changed_case_id']
ck('one formal record target, case carried in evidence and assessment',
   review['kind'] == 'record' and review['scope']['population_size'] == 1 and
   review['scope']['reviewed_target_ids'] == [pid] and
   [t['target_id'] for t in review['targets']] == [pid])
ck('target exact selected full payload', review['targets'][0]['path'] ==
   'reports/all_unmatched_20261107/worker-08/' + selection['payload']['path'])
ck('native positive scoped outcome and retained limits',
   review['completion'] == 'completed' and review['verdict'] == 'pass_with_limitations' and
   review['scientific_review'] is True and review['findings'] == [] and
   len(review['assessments']) == 5 and all(a['outcome'] == 'supported' for a in review['assessments']))
ck('no fabricated historical finding disposition',
   review['actions'][0]['finding_ids'] == [] and all('previous_occurrences' not in x for x in review['findings']))
for cap in selection['authoritative_inputs'].values():
    path = W / 'reports/all_unmatched_20261107/worker-08' / cap['path']
    pin(path, cap['sha256'])
    ck('authoritative selection present in native source ' + cap['path'],
       source_map[str(path.relative_to(W))] == cap['sha256'])

evid_by_id = {e['evidence_id']: e for e in review['evidence']}
primary_bindings = load(O / 'primary/capture-bindings.json')
for i, b in enumerate(primary_bindings):
    e = evid_by_id[f'PRIMARY-{i}']
    ck('native primary timestamp preserves actual acquisition ' + str(i),
       datetime.datetime.fromisoformat(e['accessed_at'].replace('Z', '+00:00')) ==
       datetime.datetime.fromisoformat(b['original_accessed_at']))
    ck('native primary hash preserves copied source ' + str(i),
       e['snapshot_sha256'] == b['published_capture']['sha256'])

for oldname in ['review-content.json', 'review-content-v2.json']:
    old = load(O / 'native' / oldname)
    for key in ['targets', 'scope', 'checks', 'assessments', 'findings', 'limitations', 'reviewer', 'evidence']:
        ck('rejected draft science retained ' + oldname + ':' + key, old[key] == review[key])
    before_actions = [dict(a) for a in old['actions']]
    for action in before_actions:
        action.setdefault('finding_ids', [])
    ck('draft only action required-list normalization ' + oldname, before_actions == review['actions'])
for cap in native_receipt['rejected_drafts_preserved']:
    pin(W / cap['path'], cap['sha256'])
for filename, expected_text in [('native-build-attempt1.log', 'finding_ids'),
                                ('native-build-attempt2.log', 'notes')]:
    log = read(O / 'provenance' / filename).decode()
    ck('actual rejected draft diagnostic ' + filename, expected_text in log)

technical = load(O / 'validation/receipt.json')
ck('pinned completed technical receipt', inputs[str(O / 'validation/receipt.json')] ==
   '7a82818fd370e88b9954d718449c40742b97eb2d05f5c1863163ef5d15df59e5' and technical['status'] == 'PASS')
ck('technical selection binding', technical['selection']['sha256'] == bindings['selection']['sha256']
   and technical['authoritative_inputs'] == selection['authoritative_inputs'])
ck('114 schema checks retained without rerun', technical['strict']['payloads'] == 114
   and technical['strict']['exit_code'] == 0 and technical['strict']['violations'] == 0)
technical_manifest = load(O / 'validation/MANIFEST.json')
for row in technical_manifest['files']:
    private_path = W / row['path']
    relative = private_path.relative_to(private_technical)
    public_path = O / 'validation' / relative
    original = pin(private_path, row['sha256'])
    ck('technical public copy exact ' + str(relative), read(public_path) == original)
for path, digest in technical['native_input_hashes'].items():
    pin(W / path, digest)
overlay = load(O / 'validation/full-attempt-v2/full-overlay.json')
ck('complete overlay receipt scope', overlay['baseline_record_count'] == 2956 and
   overlay['selected_payload_count'] == 114 and overlay['overlay_record_count'] == 3037 and
   overlay['baseline_partonomy_violations'] == [] and overlay['overlay_partonomy_violations'] == []
   and overlay['owner_admission_status'] == 'HELD')
identity = load(O / 'validation/full-attempt-v2/identity-obligations.json')
ck('native identity scope/counts', identity['status'] == 'PASS' and identity['selected_count'] == 114 and
   identity['projected_rows'] == 121 and len(identity['entries']) == 114 and
   all(v == [] for v in identity['native_failures'].values()))
ck('112 actual degraded Rule D inputs and outputs', len(identity['actual_rule_d_negative_inputs']) ==
   len(identity['actual_rule_d_rejections']) == identity['negative_rule_d_count'] == 112)
selected = {p['proposal_id']: p for p in load(O / 'proposals.json')['proposals']}
for row in identity['entries']:
    ck('identity fixture exact selected payload ' + row['proposal_id'],
       row['sha256'] == selected[row['proposal_id']]['after_capture']['sha256'])
payload_controls = load(O / 'validation/payload-attempt-v2/payload-checks.json')
ck('guarded replay exact payload', payload_controls['status'] == 'PASS' and
   payload_controls['payload_sha256'] == payload_controls['guarded_replay_sha256'] == selection['payload']['sha256'])
ck('actual two guard and ten invariant negatives', len(payload_controls['controls']) == 12
   and all(c['rejected'] for c in payload_controls['controls']) and
   sum(c['type'] == 'actual_native_guard' for c in payload_controls['controls']) == 2)
for c in payload_controls['controls']:
    if c['type'] == 'actual_native_guard':
        ck('negative guard no-write target ' + c['name'], c['target_absent'] is True)
qualification = load(O / 'validation/projection-qualification.json')
projection = load(O / 'validation/full-attempt-v2/claw-actual-projections.json')
old_row = projection['previous']['rows'][0]
new_row = projection['current']['rows'][0]
projection_delta = {k: {'before': old_row[k], 'after': new_row[k]}
                    for k in old_row if old_row[k] != new_row[k]}
ck('actual full rows differ only truthful curator/date',
   set(projection_delta) == {'source', 'mapping_date'} and
   projection_delta == qualification['exact_expected_history_provenance_delta'] ==
   technical['wolfe_expected_provenance_delta'])
ck('identity and lexical projection remain exact', new_row['subject_id'] == 'MIM:Wolfes_Vitamin_Mix' and
   new_row['object_id'] == 'kgmicrobe.ingredient:wolfes_vitamin_mix' and
   new_row['predicate_id'] == 'skos:exactMatch' and qualification['actual_rule_d_failures'] == [])
ck('actual Wolfe degraded Rule D rejected', len(qualification['rejections']) == 1 and
   'Rule D' in qualification['rejections'][0][-1])
ck('pre-existing TSB/Bacto admission remains failed and held',
   technical['owner_admission_status'] == 'FAILED/HELD' and
   len(technical['owner_admission_failures']) == 1 and
   technical['owner_admission_failures'][0]['gate_status'] == 'failed' and
   technical['owner_admission_failures'][0]['maintained_admission'] == 'HELD')
ck('four prior technical attempts retained', len(technical['retained_attempts']) == 4)
structural = load(O / 'structural-audit.json')
ck('structural full selection only, no scientific approval',
   structural['structural_accounting'] == 'PASS' and structural['accounted_case_count'] == 188 and
   structural['proposal_count'] == 114 and structural['evidence_count'] == 1101 and
   structural['scientific_adequacy_or_approval_established'] is False and
   set(structural['accounted_case_ids']) == set(bindings['case_hashes']))
for cap in selection['authoritative_inputs'].values():
    p = W / 'reports/all_unmatched_20261107/worker-08' / cap['path']
    if str(p) in structural['input_hashes']:
        ck('structural exact index ' + str(p), structural['input_hashes'][str(p)] == cap['sha256'])
preservation = load(O / 'preservation.json')
ck('root preservation receipt declares bounded exact checks', preservation['status'] == 'PASS'
   and preservation['all_original_tracked_bytes_unchanged'] is True and len(preservation['packets']) == 7)
for path, expected in list(inputs.items()):
    ck('read input stable at finish ' + path, sha(Path(path).read_bytes()) == expected)

failed = [c for c in checks if not c['passed']]
out = {
    'reviewer': '/root/organics', 'author': '/root', 'worker': 'worker08',
    'status': 'PASS' if not failed else 'FAIL', 'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': 'Independent native-pair assembly review and receipt/source binding only. Earlier author-independent full vitamin science remains in sealed review.json. No self-approval of historical organic proposals.',
    'native_review_id': review['review_id'], 'native_pair': native_receipt['review_yaml'] | {'markdown': native_receipt['review_markdown']},
    'actual_native_target_count': 1,
    'target_scope_explanation': 'The native record formally selects the complete Wolfe proposal. The mixed six-occurrence case is reviewed through CASE evidence and A-CASE assessment, not a second native target. No claim of two formal targets is made.',
    'native_validation_executed': ['load_document', 'validate_review', 'render_markdown'],
    'native_source_hashes_verified': len(source_map),
    'saved_markdown_exact': rendered == markdown,
    'case_ids': [cid], 'proposal_ids': [pid],
    'selection_sha256': bindings['selection']['sha256'],
    'payload_hashes': {pid: selection['payload']['sha256']},
    'checks_total': len(checks), 'checks_passed': len(checks) - len(failed), 'failures': failed,
    'new_findings': [], 'input_hashes': inputs,
    'assembly_appraisal': [
        'The five positive assessments accurately summarize the separate full-record science and skeptical receipts, without approving whole referenced child owners.',
        'Original 113 proposals and 187 other cases are explicitly preservation-only; the native formal population is one record.',
        'The original six occurrences and source forms remain partitioned, and only NBRC903 triggers the CB comparator dependency.',
        'The two rejected native drafts are preserved. Their repairs add an empty required finding_ids list and normalize notes to a list; scientific assessment/evidence content remains exact.',
        'Actual projection rows retain identity, labels, predicate and aliases, while curator/date change with the honest new history. Full-row equality is not claimed.',
        'Technical PASS denotes guarded/schema/overlay checks, not owner admission: the pre-existing TSB/Bacto FAILED/HELD result remains visible.',
        'Empty new findings does not retire prior finding groups or close issue1237. The coordinator action retains central nominal duplicate reconciliation and future application checks.'
    ],
    'limitations': [
        'Read existing full technical receipts and actual positive/negative artifacts; did not rerun schema, partonomy, SSSOM or Claw suites.',
        'Validated and rendered the new native pair in memory; did not invoke the saver or modify canonical review bytes.',
        'Rehashed every one of the 351 native inputs and all 164 technical manifest members/copies. The root preservation report for broader prior packets was inspected but not independently reexecuted here.',
        'No final-head acceptance, maintained application, whole-owner/role support, shared CB identity, procurement specificity or downstream export approval.',
        'All earlier scientific holds remain, including calcium-pantothenate D/DL, generic nominal B12, unspecified CB carrier/preparation, central W08/W06 nominal reconciliation and TSB/Bacto admission.'
    ],
    'writes': 'Only new private assembly script, checks, log and receipt; all earlier artifacts retained unchanged.'
}
for name, value in [('final-native-assembly-checks.json', checks), ('final-native-assembly.json', out)]:
    with (P / name).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
print(json.dumps({'status': out['status'], 'checks': len(checks), 'failed': failed,
                  'native_inputs': len(source_map), 'receipt_sha256': sha((P / 'final-native-assembly.json').read_bytes())}, indent=2))
raise SystemExit(bool(failed))
