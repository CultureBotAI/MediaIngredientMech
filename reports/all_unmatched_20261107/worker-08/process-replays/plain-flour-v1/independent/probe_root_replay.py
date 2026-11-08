"""Target the actual published root replay without monkeypatching native code."""
import copy
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import yaml

W = Path.cwd()
P = W / 'reports/all_unmatched_20261107/worker-08/process-replays/plain-flour-v1'
O = W / '.temp/all-unmatched-worker-08/plain-flour-process-replay-v1/independent'
script = P / 'provenance/replay.py'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
spec = importlib.util.spec_from_file_location('root_plain_flour_replay', script)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
before, expected, literals, event = mod.inputs()
rows = []

def refused(name, fn, expected_message):
    try:
        fn()
    except AssertionError as exc:
        assert expected_message in str(exc), (name, str(exc))
        rows.append({'name': name, 'observed': 'REFUSED', 'diagnostic': str(exc)})
    else:
        raise AssertionError(name + ': unexpectedly accepted')

# Actual entry point refuses an alternate valid YAML predecessor with wrong bytes.
bad = copy.deepcopy(before)
bad['notes'] += '\nUnreviewed predecessor modification.'
badpath = O / 'wrong-predecessor.yaml'
with badpath.open('x') as f:
    yaml.safe_dump(bad, f, sort_keys=False, allow_unicode=True)
dest = O / 'refused-wrong-predecessor'
refused('wrong_predecessor_bytes', lambda: mod.replay(dest, executor='worker08:/root/inorganics', predecessor_path=badpath), 'wrong predecessor')
assert not dest.exists()
receipt_before = sha(O / 'reexecution/receipt.json')
refused('existing_immutable_output', lambda: mod.replay(O / 'reexecution', executor='worker08:/root/inorganics'), 'immutable replay output already exists')
assert sha(O / 'reexecution/receipt.json') == receipt_before

# Actual reconstruction still calls the real helper with mutated event arguments;
# actual complete equivalence gate must refuse even schema-valid discrepancies.
for key, value in [('timestamp', '2026-11-08T08:38:46.690887+00:00'), ('curator', 'unrelated actor'), ('previous_status', 'UNMAPPED')]:
    variant = copy.deepcopy(event)
    variant[key] = value
    rec = mod.reconstruct(before, literals, variant)
    refused('root_gate_' + key, lambda rec=rec: mod.require_equivalent(rec, expected, before), 'complete_payload_differences')
rec = mod.reconstruct(before, literals, event)
rec['curation_history'].append(copy.deepcopy(event))
refused('root_gate_duplicate_event', lambda: mod.require_equivalent(rec, expected, before), 'complete_payload_differences')
rec = mod.reconstruct(before, literals, event)
rec['occurrence_statistics']['total_occurrences'] = 1
refused('root_gate_unreviewed_counter', lambda: mod.require_equivalent(rec, expected, before), 'complete_payload_differences')
assert len(rows) == 7

bindings = json.loads((P / 'inputs/input-bindings.json').read_text())
copies = []
for row in bindings['files']:
    original = Path(row['original_path'])
    if not original.is_absolute():
        original = W / original
    public = W / row['public_path']
    assert sha(original) == sha(public) == row['sha256']
    copies.append({'original': str(original), 'public_path': row['public_path'], 'sha256': row['sha256'], 'exact_bytes_equal': original.read_bytes() == public.read_bytes()})
assert len(copies) == 14

out = {'status': 'PASS', 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'reviewer': 'worker08:/root/inorganics', 'author': 'worker08:/root', 'root_script': {'path': str(script.relative_to(W)), 'sha256': sha(script)}, 'actual_root_entry_and_gate_negatives': rows, 'exact_original_copy_bindings': copies, 'reexecution_receipt_preserved_sha256': receipt_before, 'scope': 'Actual root entry point and equivalence gates, no native mocks. Process/provenance only; no scientific reapproval.'}
with (O / 'root-replay-probes.json').open('x') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
    f.write('\n')
print(json.dumps({'status': 'PASS', 'actual_root_negative_count': len(rows), 'exact_copy_count': len(copies), 'receipt_sha256': sha(O / 'root-replay-probes.json')}, indent=2))
