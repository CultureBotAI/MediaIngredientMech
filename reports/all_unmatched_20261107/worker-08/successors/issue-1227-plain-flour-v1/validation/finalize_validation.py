"""Bind completed technical results; no rerun of scientific/native suites."""
from datetime import datetime, timezone
import csv
import hashlib
import json
from pathlib import Path
import sys
import yaml

ROOT = Path.cwd()
P = ROOT / '.temp/all-unmatched-worker-08/plain-flour-method-v1/validation'
A = P / 'attempt-v2'
ART = ROOT / 'reports/all_unmatched_20261107/worker-08'
OUT = ART / 'successors/issue-1227-plain-flour-v1'

def read(path): return json.loads(Path(path).read_text())
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def relative(path): return str(Path(path).relative_to(ROOT))

completion = read(A / 'completion.json')
assert completion['status'] == 'PASS'
for path, digest in completion['input_hashes'].items():
    assert sha(ROOT / path) == digest, path
claw = read(A / 'claw-producer-source-hashes.json')
for path, digest in claw['source_sha256_by_path'].items():
    assert sha(path) == digest, path
primary = read(OUT / 'research/primary-label-resolution.json')
assert sha(primary['database']['path']) == primary['database']['sha256']
assert Path(primary['database']['path']).stat().st_size == primary['database']['size']
assert sha(ART / primary['original_primary_capture']['path']) == primary['original_primary_capture']['sha256']
rows = list(csv.DictReader((A / 'strict.tsv').open(), delimiter='\t'))
assert not rows
obligations = read(A / 'identity-obligations.json')
no_identity_rows = []
for entry in obligations['entries']:
    path = ROOT / entry['fixture']
    assert sha(path) == entry['sha256']
    if not entry['projected_identity_obligations']:
        record = yaml.safe_load(path.read_text())
        no_identity_rows.append(dict(proposal_id=entry['proposal_id'], mapping_status=record['mapping_status'],
            identifier=record['identifier'], reason='Native obligation helper projects only MAPPED records; no row or identity approval was invented.'))
assert len(obligations['entries']) == 113 and len(no_identity_rows) == 2
assert obligations['negative_rule_d_count'] == 111
guard = read(A / 'guarded-replay.json')
assert guard['input_sha256'] == guard['replay_sha256'] == '884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873'
assert len(guard['controls']) == 2 and all(x['rejected'] and x['target_absent'] for x in guard['controls'])
bindings = {relative(path): sha(path) for path in sorted(P.rglob('*')) if path.is_file()}
receipt = dict(
    schema='w08-plain-flour-bounded-native-validation-v1', at=datetime.now(timezone.utc).isoformat(),
    executor='worker08:/root/organics', role='Non-independent technical executor; authored predecessor organic proposal.',
    status='PASS', command=[sys.executable, relative(P / 'run_validation_v2.py')],
    input_selection=dict(path=relative(OUT / 'selection.json'), sha256=sha(OUT / 'selection.json')),
    input_proposals=dict(path=relative(OUT / 'proposals.json'), sha256=sha(OUT / 'proposals.json')),
    changed_payload=dict(proposal_id='op1201-plain-flour', path=relative(OUT / 'payloads/Plain_Flour.yaml'),
        sha256=sha(OUT / 'payloads/Plain_Flour.yaml')),
    selected_payload_count=113, exact_unchanged_payload_count=112,
    native_guarded_replay=dict(count=1, exact_replay_bytes=True, invalid_enum_rejected=True, unknown_field_rejected=True),
    strict=dict(exit_code=0, selected_payloads=113, diagnostic_rows=0),
    full_native_partonomy=dict(baseline_records=2956, overlay_records=3037, baseline_violations=0, overlay_violations=0),
    native_identity_obligations=dict(selected_payloads=113, mapped_own_identity_rows=111, total_rows=120,
        predicate_counts=obligations['predicate_counts'], rule_failures=obligations['native_failures'],
        degraded_identity_rows_actually_rejected=111, other_controls=obligations['native_controls'],
        records_without_projected_identity=no_identity_rows),
    native_primary_label=dict(curie='FOODON:00004510', label='flour', grade='EXACT_MATCH',
        database=primary['database'], exact_database_hash_rechecked=True,
        mismatch_control_label='Plain flour', mismatch_control_rejected=True,
        scope='Mechanical label/method agreement; source applicability is assessed by separate independent reviewers.'),
    actual_Claw_projection=dict(payloads=2, producer_head=claw['head'], captured_source_files=14,
        true_file_compilation=True, native_binding_guard_before_and_after=True,
        full_overlay_owners=3037, ownership_keys=3034,
        subject_id='MIM:Plain_Flour', previous_subject_label='Plain flour', current_subject_label='flour',
        object_id='FOODON:00004510', object_label='flour', predicate_id='skos:exactMatch',
        mapping_justification='semapv:LexicalMatching', preserved_alias='Plain flour', invented_CAS=False,
        actual_new_row_native_Rule_D_pass=True, actual_new_row_degraded_Rule_D_rejected=True,
        source_hashes=claw['source_sha256_by_path'], maintained_export=False),
    owner_admission_status='FAILED/HELD', exact_failed_admission=read(A / 'owner-admission-failed-held.json'),
    prior_attempt=dict(path=relative(P / 'failure-attempt-v1.json'), sha256=sha(P / 'failure-attempt-v1.json'),
        disposition='Preserved exact first runner/error. It stopped before native execution because final assembly appended three evidence IDs to the author row. Attempt v2 requires precisely that suffix and unchanged remaining author fields; no native gate or payload was changed.'),
    result_and_script_hashes=bindings, input_hashes=completion['input_hashes'],
    scientific_approval=False, independent_scientific_review=False, maintained_writes=False,
    source_payload_changes=False, gate_changes=False, held_owner_release=False, release_approval=False,
    scope_limits=completion['limits'])
with (P / 'receipt.json').open('x') as handle:
    json.dump(receipt, handle, indent=2, ensure_ascii=False)
    handle.write('\n')
with (P / 'HANDOFF.md').open('x') as handle:
    handle.write('Bounded native validation completed.\n\n')
    handle.write(f"Receipt: `receipt.json`, SHA256 `{sha(P / 'receipt.json')}`.\n\n")
    handle.write('The changed Flour payload passes guarded replay; all 113 selected payloads pass strict schema validation. The complete 2,956-record frozen baseline and 3,037-record overlay have no native partonomy violations. All 120 projected identity obligations pass B1/B2/B3/B5/D; 111 deliberately degraded own-identity rows are actually rejected. The two non-MAPPED records have no invented identity rows.\n\n')
    handle.write('The actual pinned Claw source was compiled from captured bytes with its true file path, and its binding guard ran before and after the two in-memory projections. The new row retains MIM:Plain_Flour, FOODON:00004510 and exactMatch, uses subject label flour with lexical justification, and retains Plain flour in other. No CAS was introduced.\n\n')
    handle.write('The exact TSB/Bacto collision remains FAILED/HELD. There is no scientific, maintained-admission or release approval. The executor authored the predecessor organic proposal and is not an independent scientific reviewer.\n\n')
    handle.write('Attempt v1 is retained unchanged: its pre-validation equality assertion stopped on three expected final assembly evidence IDs. The v2 runner binds exactly that metadata suffix; no native gate or scientific input changed. All scripts, commands, logs, invalid fixtures, exact selected-payload fixtures and source hashes are retained under this private directory. Root may copy the bounded technical result into a new publication artifact.\n')
with (P / 'MANIFEST.sha256').open('x') as handle:
    for path in sorted(P.rglob('*')):
        if path.is_file() and path.name != 'MANIFEST.sha256':
            handle.write(f'{sha(path)}  {path.relative_to(P)}\n')
print(json.dumps(dict(receipt=relative(P / 'receipt.json'), sha256=sha(P / 'receipt.json'),
                     manifest_sha256=sha(P / 'MANIFEST.sha256'), status='PASS')))
