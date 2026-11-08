"""Execute the native builder's unchanged AST prefix through its actual gates.

The prefix ends before evidence/report construction, so these deliberately small
fixtures test validation refusal without producing a native scientific report.
"""
import ast
import copy
import datetime
import hashlib
import json
from pathlib import Path
from unittest.mock import patch
import sys

ROOT = Path(__file__).resolve().parents[4]
ART = ROOT / 'reports/all_unmatched_20261107/worker-04'
SCRIPT = ART / 'scripts/build_native_review.py'
SOURCE = SCRIPT.read_bytes()
SHA = lambda b: hashlib.sha256(b).hexdigest()
STAMP = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
WORK = ROOT / '.temp/all-unmatched-worker-04/biological' / ('native-controls-' + STAMP)
WORK.mkdir(parents=True, exist_ok=False)
tree = ast.parse(SOURCE)
stop = next(i for i, node in enumerate(tree.body) if isinstance(node, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == 'timestamp' for t in node.targets))
prefix = ast.Module(body=tree.body[:stop], type_ignores=[])
code = compile(prefix, str(SCRIPT), 'exec')


def check(name, mutation, expected):
    root = WORK / name
    art = root / 'reports/all_unmatched_20261107/worker-04'
    (art / 'scripts').mkdir(parents=True)
    (art / 'validation').mkdir()
    inputs = {'decisions.json': {'decisions': []}, 'evidence.json': {'evidence': []},
        'proposals.json': {'proposals': []}, 'validation/native-inspection.json': {'targets': []},
        'validation/assembly-bindings.json': {},
        'structural-audit-v1.json': {'structural_accounting': 'PASS', 'scientific_adequacy_or_approval_established': False,
            'accounted_case_count': 188, 'assigned_shard_case_count': 188, 'independent_review_status_counts': {'complete': 188}},
        'validation/proposal-overlay.json': {'status': 'PASS'},
        'validation/final-command-receipts.json': {},
        'fixture-input.json': {'fixture': 'original'},
        'validation/final-input-bindings.json': {'files': []}}
    inputs['validation/final-input-bindings.json']['files'].append({
        'path': str(art / 'fixture-input.json'),
        'sha256': SHA(json.dumps(inputs['fixture-input.json']).encode())})
    binding_sha = SHA(json.dumps(inputs['validation/final-input-bindings.json']).encode())
    receipts = inputs['validation/final-command-receipts.json']
    for key in ['structural', 'schema', 'overlay', 'auditor-controls']:
        log = f'validation/fixture-{key}.log'
        (art / log).write_bytes(b'fixture valid output\n')
        receipts[key] = {'exit_code': 0, 'log': log, 'log_sha256': SHA((art / log).read_bytes()),
                         'input_bindings_sha256': binding_sha}
    mutation(inputs)
    for path, content in inputs.items():
        (art / path).write_text(json.dumps(content))
    error = None
    with patch.object(sys, 'argv', [str(SCRIPT), 'content']):
        try:
            exec(code, {'__file__': str(art / 'scripts/build_native_review.py'), '__name__': '__main__'})
        except AssertionError as exc:
            error = str(exc)
    observed = 'FAIL' if error is not None else 'PASS'
    return {'name': name, 'expected_status': expected, 'observed_status': observed,
            'assertion': error, 'passed': expected == observed,
            'native_output_not_created': not (art / 'native-review-content.json').exists()}


rows = [
    check('valid_gates', lambda x: None, 'PASS'),
    check('nonzero_schema_exit', lambda x: x['validation/final-command-receipts.json']['schema'].update(exit_code=1), 'FAIL'),
    check('changed_check_output', lambda x: x['validation/final-command-receipts.json']['structural'].update(log_sha256='0' * 64), 'FAIL'),
    check('structural_fail', lambda x: x['structural-audit-v1.json'].update(structural_accounting='FAIL'), 'FAIL'),
    check('mechanical_audit_claims_scientific_approval', lambda x: x['structural-audit-v1.json'].update(scientific_adequacy_or_approval_established=True), 'FAIL'),
    check('overlay_fail', lambda x: x['validation/proposal-overlay.json'].update(status='FAIL'), 'FAIL'),
    check('changed_native_targets', lambda x: x['validation/native-inspection.json'].update(targets=[{'target_id': 'unexpected'}]), 'FAIL'),
    check('changed_bound_input', lambda x: x['fixture-input.json'].update(fixture='changed'), 'FAIL'),
    check('wrong_input_binding_receipt', lambda x: x['validation/final-command-receipts.json']['schema'].update(input_bindings_sha256='0' * 64), 'FAIL'),
    check('missing_independent_case', lambda x: x['structural-audit-v1.json'].update(independent_review_status_counts={'complete': 187, 'pending': 1}), 'FAIL'),
]
report = {'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'script': str(SCRIPT.relative_to(ROOT)), 'script_sha256': SHA(SOURCE),
    'harness_sha256': SHA(Path(__file__).read_bytes()),
    'scope': 'Unchanged AST prefix of actual native builder through all validation assertions; isolated inputs; no scientific report produced or production artifact modified.',
    'controls': rows, 'status': 'PASS' if all(row['passed'] and row['native_output_not_created'] for row in rows) else 'FAIL'}
out = ART / 'independent-review' / ('native-gate-negative-controls-' + STAMP + '.json')
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'path': str(out.relative_to(ROOT)), 'status': report['status']}))
