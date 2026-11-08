"""Seal independent process-only findings and exact current provenance bindings."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import yaml

W = Path.cwd()
A = W / 'reports/all_unmatched_20261107/worker-08'
P = A / 'process-replays/plain-flour-v1'
O = W / '.temp/all-unmatched-worker-08/plain-flour-process-replay-v1/independent'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
read = lambda p: json.loads(Path(p).read_text())
def bind(p):
    p = Path(p)
    return {'path': str(p.relative_to(W)) if p.is_relative_to(W) else str(p), 'sha256': sha(p)}
def save(name, value):
    with (O / name).open('x') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')

before_path = P / 'inputs/predecessor.yaml'
selected_path = P / 'inputs/selected-payload.yaml'
before = yaml.safe_load(before_path.read_text())
selected = yaml.safe_load(selected_path.read_text())
reexecution = read(O / 'reexecution/receipt.json')
assert reexecution['status'] == 'PASS'
assert reexecution['executor'] == 'worker08:/root/inorganics'
assert reexecution['replay_script_sha256'] == sha(P / 'provenance/replay.py')
assert reexecution['replay_payload_sha256'] == '884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873'
assert sha(O / 'reexecution/Plain_Flour.yaml') == sha(P / 'replay/Plain_Flour.yaml') == sha(selected_path) == reexecution['replay_payload_sha256']
assert yaml.safe_load((O / 'reexecution/Plain_Flour.yaml').read_text()) == selected
assert selected['curation_history'][:-1] == before['curation_history']
assert reexecution['historical_event'] == selected['curation_history'][-1]
assert [c['function'] for c in reexecution['actual_calls']] == ['record_curation_event', 'write_validated_ingredient']
assert reexecution['actual_calls'][0]['kwargs']['llm_assisted'] is True
assert reexecution['actual_calls'][0]['kwargs']['timestamp'] == selected['curation_history'][-1]['timestamp']
assert [c['history_length_before_call'] for c in reexecution['actual_calls']] == [5, 6]
probes = read(O / 'independent-probes.json')
root_probes = read(O / 'root-replay-probes.json')
assert probes['status'] == root_probes['status'] == 'PASS'
assert (probes['positive_count'], probes['negative_count']) == (2, 10)
assert len(root_probes['actual_root_entry_and_gate_negatives']) == 7
author_controls = read(P / 'controls/receipt.json')
assert author_controls['status'] == 'PASS' and len(author_controls['controls']) == 9
assert all(c['rejected'] for c in author_controls['controls'])

# Independent transport check of the explicitly named preservation groups only.
preservation = read(P / 'preservation.json')
manifest_checks = []
for group in preservation['manifest_groups']:
    manifest = W / group['path']
    assert sha(manifest) == group['sha256']
    members = manifest.read_text().splitlines()
    assert len(members) == group['members']
    for line in members:
        digest, relative = line.split('  ', 1)
        assert sha(W / relative) == digest, relative
    manifest_checks.append({**bind(manifest), 'members': len(members), 'all_hashes_match': True})
selection = A / 'successors/issue-1237-tenvit-v1/selection.json'
assert sha(selection) == preservation['source_selector_sha256'] == 'fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699'
sel = read(selection)
for cap in sel['authoritative_inputs'].values():
    assert sha(A / cap['path']) == cap['sha256']
props = read(A / sel['authoritative_inputs']['proposals.json']['path'])['proposals']
assert len(props) == 114
for row in props:
    assert sha(A / row['after_capture']['path']) == row['after_capture']['sha256']
subprocess.run(['git', 'diff', '--exit-code', 'HEAD', '--'], check=True, capture_output=True)
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
assert head == preservation['head']

full_reads = [
    W / '.claude/skills/curate-yaml-record/SKILL.md',
    W / 'src/mediaingredientmech/curate/curation_event.py',
    W / 'src/mediaingredientmech/validation/write_validated.py',
    P / 'inputs/original-author.py', before_path, selected_path,
    P / 'inputs/issue1227-comment6719637789.json',
    P / 'inputs/original-label-resolution.json',
    P / 'inputs/input-bindings.json',
    P / 'provenance/replay.py', P / 'replay/receipt.json',
    P / 'provenance/checks.py', P / 'controls/receipt.json',
    P / 'provenance/preflight_v2.py', P / 'provenance/preflight-attempt1.json',
    P / 'preservation.json',
    *[P / 'inputs/w09' / name for name in ['HANDOFF.json', 'HANDOFF.md', 'REPORT.md', 'machine-findings.json', 'actual-reviewer-scopes.json', 'bridge/workflow-and-independence-review.json', 'skeptic/process-referral.json']],
]
ledger = [{'input': bind(p), 'read_scope': 'Complete actual file read for this bounded workflow/provenance review; historical scientific conclusions are attribution, not newly rerun science.'} for p in full_reads]
for name in ['MANIFEST.json', 'native/review.yaml', 'native/review.md']:
    ledger.append({'input': bind(P / 'inputs/w09' / name), 'read_scope': 'Exact original/copy transport hashes independently checked through input-bindings; W09 native pair and full manifest science not reexecuted or newly approved here.'})
save('read-ledger.json', {'reviewer': 'worker08:/root/inorganics', 'scope': 'Only process-replay and provenance review', 'entries': ledger})
save('command-receipt.json', {
    'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'status': 'PASS',
    'runtime': subprocess.check_output([str(W / '.temp/all-unmatched-worker-08/venv/bin/python'), '--version'], text=True).strip(),
    'environment': {'PYTHONDONTWRITEBYTECODE': '1', 'python_flag': '-B'},
    'executions': [
        {'script': bind(O / 'probe_native_replay.py'), 'log': bind(O / 'independent-probes-command.log'), 'result': bind(O / 'independent-probes.json'), 'exit_code': 0, 'actual_positive_count': 2, 'actual_negative_count': 10},
        {'script': bind(P / 'provenance/replay.py'), 'arguments': ['--output-dir', str((O / 'reexecution').relative_to(W)), '--executor', 'worker08:/root/inorganics'], 'log': bind(O / 'reexecution-command.log'), 'result': bind(O / 'reexecution/receipt.json'), 'exit_code': 0, 'actual_positive_count': 1},
        {'script': bind(O / 'probe_root_replay.py'), 'log': bind(O / 'root-replay-probes-command.log'), 'result': bind(O / 'root-replay-probes.json'), 'exit_code': 0, 'actual_negative_count': 7},
    ],
    'author_nine_controls': {'receipt': bind(P / 'controls/receipt.json'), 'execution_claim': 'Author execution read and code independently inspected; separately exercised equivalent and additional controls above.'},
    'no_mocked_native_functions': True,
})
findings = [{
    'finding_id': 'W08-PF-PROCESS-001', 'alias': 'W08-PF-WORKFLOW-001',
    'issue_key': 'w08-plain-flour-native-history-helper-bypass', 'severity': 'minor',
    'historical_fact': 'The published author.py directly appended the truthful event instead of calling the required native helper. That immutable historical fact remains disclosed.',
    'current_disposition': 'BOUNDED_WORKFLOW_REPLAY_SUPPORTED',
    'resolution_evidence': [bind(P / 'provenance/replay.py'), bind(O / 'reexecution/receipt.json'), bind(O / 'independent-probes.json'), bind(O / 'root-replay-probes.json')],
    'reason': 'Actual new replay starts from the exact five-event predecessor, invokes native record_curation_event once with llm_assisted=True and original event fields, invokes native guarded writer once, and produces the entire selected payload byte for byte. The old sixth event is reconstructed, not a seventh event invented. The execution timestamp is kept separately from the historical event timestamp.',
    'issue_closure_performed': False, 'scientific_reapproval': False,
}]
save('findings.json', {'new_findings': [], 'bounded_existing_finding_disposition': findings, 'unrelated_historical_referral': {'id': 'PF-LINEAGE-001', 'status': 'UNCHANGED_AND_OUT_OF_SCOPE', 'reason': 'The prior reviewer quotation discrepancy remains a separately filed historical referral; this process replay does not repair or retire it.'}})
review = {
    'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'status': 'PASS',
    'reviewer': 'worker08:/root/inorganics', 'author': 'worker08:/root',
    'scope': 'Independent native-helper replay, full event/history/payload equivalence, provenance and negative controls only.',
    'prior_involvement': 'I previously reviewed the Plain Flour scientific successor as a skeptical reviewer. That earlier review did not identify the native history-helper bypass. W09 independently identified this workflow deviation. I did not author the published Plain Flour mutation or this root replay. My separate PF-LINEAGE-001 historical quotation referral remains unchanged. This receipt is a fresh process check, not fresh independent approval of the scientific mapping.',
    'scientific_review': False, 'whole_owner_approval': False, 'role_export_approval': False,
    'predecessor': bind(before_path), 'selected_payload': bind(selected_path), 'replayed_payload': bind(O / 'reexecution/Plain_Flour.yaml'),
    'original_maintained_owner_before_sha256': 'becb2e4860868161607a709d6c4b5cbef56c2b4a3e06c9a4fc9214e35e4e9a8e',
    'preimage_distinction': 'The immediate five-event proposal predecessor aa8390 is the replay input. It does not replace the original maintained owner beforeimage becb2e used by the source proposal.',
    'full_equivalence': {'payload_bytes': True, 'payload_object': True, 'complete_final_event': True, 'complete_history': True, 'original_history_prefix': True, 'events_before': 5, 'events_after': 6, 'events_added_to_selected_record': 0},
    'native_execution': {'actual_root_script_reexecuted': True, 'helper_calls': 1, 'writer_calls': 1, 'llm_assisted': True, 'original_timestamp': selected['curation_history'][-1]['timestamp'], 'reexecution_timestamp': reexecution['replayed_at'], 'mocked': False},
    'assessment': [
        'The replay parses exact pinned original author literals without executing the old mutator, reconstructs only its four reviewed non-history mutations, and passes the preserved historical sixth event through the native helper. No new ontology/source lookup is claimed.',
        'Full object and exact serialized-byte comparison detect changes outside the event, including an unreviewed occurrence counter. A deliberate direct-append fixture is rejected by an independent actual-call invariant even though its event could equal the selected one.',
        'Root entry guards independently refused a different valid YAML predecessor and an existing output directory. Full root equivalence checks refused timestamp, curator, status, duplicate-event and counter changes. Real native schema controls refused an unknown field and malformed action before output.',
        'The original source capture timestamps, historical author attribution and previous five events are retained. Receipt timestamps correctly record the new execution. Replay does not claim the old author used the helper.',
        'Root controls and preservation code were fully read. The initial failed sibling-path preflight is retained as a harness failure; corrected preflight pins original inputs. No failed scientific gate is reclassified.',
    ],
    'independent_controls': {'native_reconstruction_positive': 2, 'native_reconstruction_negative': 10, 'actual_root_reexecution_positive': 1, 'actual_root_entry_and_equivalence_negative': 7},
    'input_bindings': [bind(p) for p in full_reads],
    'supporting_receipts': [bind(O / p) for p in ['read-ledger.json', 'command-receipt.json', 'findings.json', 'independent-probes.json', 'root-replay-probes.json', 'reexecution/receipt.json']],
    'preservation': {'observed_head': head, 'tracked_diff_empty': True, 'manifest_checks': manifest_checks, 'selector': bind(selection), 'core_indices_exact': True, 'selected_payload_hashes_verified': 114, 'new_source_cases': 0, 'new_proposals': 0, 'selected_payload_changes': 0, 'scope': 'Transport-only checks of the named groups and active selected payloads; no rerun of unchanged scientific validations.'},
    'finding_dispositions': findings, 'open_new_findings': [],
    'limitations_and_holds': ['Scientific selection remains the current vitamin successor unchanged.', 'All prior source, material-specificity, role, owner, integration and export holds remain in force; Trypticase owner admission remains held.', 'PF-LINEAGE-001 is outside this replay and is not retired.', 'No maintained YAML, SSSOM, source artifact, old review, GitHub object or native helper was edited; no merge, release or downstream rebuild is authorized by this review.', 'Only new files in the assigned private independent directory were written. No full W09 895-input/scientific rerun is claimed.'],
}
save('review.json', review)
save('HANDOFF.json', {'status': 'SEALED_PROCESS_REVIEW_PASS', 'review': bind(O / 'review.json'), 'findings': bind(O / 'findings.json'), 'command_receipt': bind(O / 'command-receipt.json'), 'read_ledger': bind(O / 'read-ledger.json'), 'root_script': bind(P / 'provenance/replay.py'), 'payload_sha256': sha(O / 'reexecution/Plain_Flour.yaml'), 'next_step': 'Coordinator may bind this process-only receipt to its native workflow disposition. No scientific selector or payload correction is needed.'})
print(json.dumps({'status': 'PASS', 'review': bind(O / 'review.json'), 'handoff': bind(O / 'HANDOFF.json')}, indent=2))
