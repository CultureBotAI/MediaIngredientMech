"""Read-only native pair and process-scope readback; no scientific rerun."""
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import yaml

W = Path.cwd()
P = W / 'reports/all_unmatched_20261107/worker-08/process-replays/plain-flour-v1'
O = W / '.temp/all-unmatched-worker-08/plain-flour-process-replay-v1/independent'
R = W / 'reviews/structured/20261108T092753Z-w08-plain-flour-process-replay'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
read = lambda p: json.loads(Path(p).read_text())
def bind(p):
    return {'path': str(Path(p).relative_to(W)), 'sha256': sha(p)}
checks = []
def check(label, condition):
    assert condition, label
    checks.append(label)

start_head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
private_review_hash = sha(O / 'review.json')
private_handoff_hash = sha(O / 'HANDOFF.json')
check('initial private review exact', private_review_hash == '4dbffabeca9fc6d4664c691497bee3af7dff61224f8f470d0526a66363c180bd')
check('initial private handoff exact', private_handoff_hash == '1c75608a27cb496e5fd43a1ce2a4be6777e87c586f411f34762509992460f6d4')
check('pair YAML expected hash', sha(R / 'review.yaml') == '8c70a3697e5d044de9215ed2da67bf566e20866af72e19000a0addfd05f83c47')
check('pair Markdown expected hash', sha(R / 'review.md') == 'ce4480d0a1512305228234782622b2213fd9b631f0d3deec41a198d0ca72a37a')
spec = importlib.util.spec_from_file_location('actual_native_review', W / 'scripts/record_review.py')
n = importlib.util.module_from_spec(spec)
spec.loader.exec_module(n)
review = n.read_review(W, str((R / 'review.yaml').relative_to(W)))
n.validate_review(review)
checks.append('actual native read_review and validate_review succeeded')
n.assert_current_source(W, review)
checks.append('actual native assert_current_source succeeded')
check('actual native render exactly matches saved Markdown', n.render_markdown(review) == (R / 'review.md').read_text())
provenance = n.source_provenance(W, review)
check('working-tree attestation accurately scoped', provenance['status'] == 'working_tree_attestation' and review['source']['state'] == 'working_tree')
check('base equals actual current HEAD', review['source']['git_revision'] == start_head)
check('root receipt exact authoritative pair', read(P / 'native/receipt.json')['review_yaml'] == bind(R / 'review.yaml') and read(P / 'native/receipt.json')['review_markdown'] == bind(R / 'review.md'))
check('native content and inspection match saved pair', read(P / 'native/review-content.json') == review and read(P / 'native/inspection.json')['source'] == review['source'])
check('exact 70 inputs', len(review['source']['inputs']) == 70 == read(P / 'native/receipt.json')['input_count'])
for item in review['source']['inputs']:
    check('current input: ' + item['path'], sha(W / item['path']) == item['sha256'])
    path = W / item['path']
    if path.is_relative_to(P / 'independent'):
        original = O / path.relative_to(P / 'independent')
        check('private peer artifact equals public copy: ' + str(original.relative_to(O)), original.read_bytes() == path.read_bytes())
check('single process target', len(review['targets']) == 1 and review['targets'][0]['target_id'] == 'author-workflow' and review['targets'][0]['kind'] == 'source')
check('scope is full only for one workflow', review['scope']['population_size'] == 1 and review['scope']['reviewed_target_ids'] == ['author-workflow'])
check('scientific review explicitly false', review['scientific_review'] is False)
check('verdict limited', review['verdict'] == 'pass_with_limitations')
check('reviewer and author independence disclosure', 'worker08:/root/inorganics' in review['reviewer']['identity'] and 'Replay authored by worker08:/root' in review['reviewer']['independence_basis'] and 'prior Plain Flour' in review['reviewer']['independence_basis'])

prior = yaml.safe_load((P / 'inputs/w09/native/review.yaml').read_text())
previous = next(f for f in prior['findings'] if f['finding_id'] == 'W08-PF-PROCESS-001')
check('exact one finding', len(review['findings']) == 1)
finding = review['findings'][0]
check('native historical identity', finding['previous_occurrences'] == [{'repository': prior['repository'], 'review_id': prior['review_id'], 'finding_id': previous['finding_id']}])
for key in ['finding_id', 'issue_key', 'category', 'severity', 'certainty', 'target_ids']:
    check('prior finding preserved: ' + key, finding[key] == previous[key])
check('prior open and current coordinator-deferred statuses explicit', previous['status'] == 'open' and finding['status'] == 'deferred')
check('coordinator acceptance remains separate', 'coordinator final-head' in finding['disposition_reason'] and 'external finding closure are separate' in finding['disposition_reason'])
check('filed process comment exact', finding['external_issues'] == ['https://github.com/CultureBotAI/MediaIngredientMech/issues/1227#issuecomment-6719637789'])
check('action only coordinator readback', len(review['actions']) == 1 and review['actions'][0]['action_id'] == 'COORDINATOR-READBACK' and review['actions'][0]['finding_ids'] == ['W08-PF-PROCESS-001'])
for e in review['evidence']:
    check('exact evidence capture: ' + e['evidence_id'], sha(W / e['reference']) == e['snapshot_sha256'])
check('peer evidence pins actual sealed receipt', next(e for e in review['evidence'] if e['evidence_id'] == 'PEER')['snapshot_sha256'] == private_review_hash)
limitations = '\n'.join(review['limitations'])
for term in ['no fresh chemical', 'Original direct-append', 'actual replay time', 'PF-LINEAGE-001', 'does not correct or close', 'scientific, owner, role and export holds', 'FAILED/HELD', 'nominal vitamin reconciliation']:
    check('explicit retained limit: ' + term, term in limitations)

replay = read(P / 'replay/receipt.json')
check('no seventh event', replay['selected_record_events_added'] == 0 and replay['replay_history_events'] == 6)
check('exact replay payload unchanged', sha(P / 'replay/Plain_Flour.yaml') == '884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873')
check('active scientific selection remains exact', sha(W / 'reports/all_unmatched_20261107/worker-08/successors/issue-1237-tenvit-v1/selection.json') == 'fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699')
end_head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
check('HEAD stable across readback', end_head == start_head)
check('initial private review and handoff preserved after readback', sha(O / 'review.json') == private_review_hash and sha(O / 'HANDOFF.json') == private_handoff_hash)
result = {
    'status': 'PASS', 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reviewer': 'worker08:/root/inorganics', 'assembly_author': 'worker08:/root',
    'scope': 'Bounded independent native-pair validation, read/render parity, input/provenance bindings and claim-scope readback. No scientific rerun or broader approval.',
    'prior_involvement': 'Same reviewer as the sealed process-only receipt and earlier Plain Flour skeptical review; the disclosed historical miss and PF-LINEAGE-001 remain unchanged.',
    'native_yaml': bind(R / 'review.yaml'), 'native_markdown': bind(R / 'review.md'),
    'root_native_receipt': bind(P / 'native/receipt.json'), 'root_native_builder': bind(P / 'provenance/native_review.py'),
    'initial_review': bind(O / 'review.json'), 'initial_handoff': bind(O / 'HANDOFF.json'),
    'native_api': bind(W / 'scripts/record_review.py'), 'readback_script': bind(Path(__file__)),
    'native_operations_executed': ['read_review', 'validate_review', 'render_markdown', 'assert_current_source', 'source_provenance'],
    'native_operations_not_executed': ['save_review', 'inspect_source'],
    'source_provenance': provenance, 'entry_head': start_head, 'exit_head': end_head,
    'source_input_count': 70, 'target_count': 1, 'scientific_review': False,
    'checks_passed': len(checks), 'checks': checks,
    'assessment': [
        'The native pair accurately serializes the independently supported historical replay and preserves its process-only scope. It makes no claim that the old execution used the helper.',
        'The complete original minor finding identity is linked to the actual W09 native review. Its current deferred status explicitly reserves coordinator final-head acceptance and external closure; this does not contradict the supported bounded replay.',
        'Evidence access times describe the current local native assembly inspection. The underlying preserved event timestamp and earlier source research times remain in their immutable input records; no fresh source acquisition is implied.',
        'All 70 currently inspected inputs match, and every copied peer artifact among them matches the private sealed original. Native source remains a working-tree attestation, not a claim those new bytes were already committed.',
        'All source, owner, role, export, Trypticase and nominal vitamin holds are retained. PF-LINEAGE-001 remains separate. The one workflow target does not expand into ingredient science approval.',
    ],
    'new_findings': [], 'required_payload_changes': [],
    'writes': 'Only this new readback script, command log and final-bindings.json in the assigned private independent directory.',
}
with (O / 'final-bindings.json').open('x') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
    f.write('\n')
print(json.dumps({'status': 'PASS', 'checks': len(checks), 'final_bindings': bind(O / 'final-bindings.json')}, indent=2))
