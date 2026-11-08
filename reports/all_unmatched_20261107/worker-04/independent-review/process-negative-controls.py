"""Exercise exact overlay script bytes in isolated, durable fixture trees.

Git metadata calls are mocked: git-show returns the retained fixture before
bytes and diff/untracked results are injected for baseline guard controls.
The production script's parsing, overlay, collisions, native partonomy,
registry checks, output and exit behavior execute without rewriting production
artifacts or maintained records. These fixtures are not scientific evidence.
"""
import contextlib
import copy
import datetime
import hashlib
import io
import json
from pathlib import Path
import runpy
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[4]
ART = ROOT / 'reports/all_unmatched_20261107/worker-04'
SCRIPT = ART / 'scripts/validate_proposal_overlay.py'
STAMP = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
WORK = ROOT / '.temp/all-unmatched-worker-04/biological' / ('process-controls-' + STAMP)
WORK.mkdir(parents=True, exist_ok=False)
SOURCE = SCRIPT.read_bytes()
SHA = lambda b: hashlib.sha256(b).hexdigest()

A = {'identifier': 'TEST:A', 'preferred_term': 'Alpha'}
B = {'identifier': 'TEST:B', 'preferred_term': 'Beta'}
PA = 'data/ingredients/mapped/Alpha.yaml'
PB = 'data/ingredients/mapped/Beta.yaml'
PC = 'data/ingredients/mapped/New.yaml'
REGISTRY = {'identifier': 'kgmicrobe.ingredient:fixture', 'preferred_term': 'Fixture',
            'ontology_mapping': {'ontology_id': 'kgmicrobe.ingredient:fixture',
                                 'ontology_label': 'Fixture',
                                 'mapping_quality': 'FALLBACK_REGISTRY'}}


def execute(name, baseline, proposed, expected, expected_error=None, bad_hash=False, drift=None):
    root = WORK / name
    art = root / 'reports/all_unmatched_20261107/worker-04'
    (art / 'scripts').mkdir(parents=True)
    (art / 'validation').mkdir()
    (art / 'payloads').mkdir()
    script = art / 'scripts/validate_proposal_overlay.py'
    script.write_bytes(SOURCE)
    originals = {}
    for path, record in baseline.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        body = yaml.safe_dump(record).encode()
        target.write_bytes(body)
        originals[path] = body
    ps = []
    for i, (path, record) in enumerate(proposed):
        body = yaml.safe_dump(record).encode()
        capture = f'payloads/{i}.yaml'
        (art / capture).write_bytes(body)
        ps.append({'proposal_id': f'fixture-{i}', 'owner_path': path,
                   'kind': 'edit_existing_owner' if path in baseline else 'new_owner',
                   'before_sha256': SHA(originals[path]) if path in baseline else None,
                   'after_capture': {'path': capture, 'sha256': '0' * 64 if bad_hash else SHA(body)}})
    (art / 'proposals.json').write_text(json.dumps({'proposals': ps}))

    def git_show(args, **kwargs):
        assert kwargs['cwd'] == root
        if args[:2] == ['git', 'diff']:
            return b'data/ingredients/mapped/Drift.yaml\n' if drift == 'tracked' else b''
        if args[:3] == ['git', 'ls-files', '--others']:
            assert '--exclude-standard' not in args
            return b'data/ingredients/mapped/Ignored.yaml\n' if drift == 'untracked' else b''
        assert args[:2] == ['git', 'show']
        commit, path = args[2].split(':', 1)
        assert commit == 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
        return originals[path]

    rejected = None
    with patch('subprocess.check_output', side_effect=git_show), contextlib.redirect_stdout(io.StringIO()):
        try:
            runpy.run_path(str(script), run_name='__main__')
        except SystemExit as exc:
            exit_code = int(exc.code)
        except AssertionError as exc:
            rejected = str(exc)
            exit_code = 1
        else:
            exit_code = 0
    result = ({'status': 'FAIL', 'errors': [rejected]} if rejected else
              json.loads((art / 'validation/proposal-overlay.json').read_text()))
    unchanged = all((root / p).read_bytes() == b for p, b in originals.items())
    correct = result['status'] == expected and exit_code == (0 if expected == 'PASS' else 1)
    if expected_error:
        correct = correct and any(expected_error in error for error in result['errors'])
    correct = correct and unchanged
    return {'name': name, 'expected_status': expected, 'observed_status': result['status'],
            'exit_code': exit_code, 'expected_error': expected_error, 'errors': result['errors'],
            'fixture_maintained_bytes_unchanged': unchanged, 'passed': correct,
            'result_path': str((art / 'validation/proposal-overlay.json').relative_to(ROOT))}


changed_a = dict(A, preferred_term='Alpha revised')
bad_registry = copy.deepcopy(REGISTRY)
bad_registry['ontology_mapping']['ontology_id'] = 'kgmicrobe.ingredient:other'
bad_label = copy.deepcopy(REGISTRY)
bad_label['ontology_mapping']['ontology_label'] = 'Wrong label'
bad_quality = copy.deepcopy(REGISTRY)
bad_quality['ontology_mapping']['mapping_quality'] = 'EXACT_MATCH'
bad_component = copy.deepcopy(REGISTRY)
bad_component.update({'ingredient_type': 'STOCK_SOLUTION',
    'components': [{'component_id': 'TEST:missing', 'component_name': 'Missing material',
                    'reference_scope': 'MIM_CATALOG'}],
    'component_assertion': {'evidence': [{'source': 'fixture'}]}})
cases = [
    ('valid_registry_without_external_adapter', {PA: A, PB: B}, [(PC, REGISTRY)], 'PASS', None, False),
    ('duplicate_existing_owner', {PA: A, PB: B}, [(PA, A), (PA, changed_a)], 'FAIL', 'duplicate proposed owner', False),
    ('edited_identifier_collision', {PA: A, PB: B}, [(PA, dict(A, identifier='TEST:B'))], 'FAIL', 'introduced identifier collision', False),
    ('new_identifier_collision', {PA: A, PB: B}, [(PC, dict(A))], 'FAIL', 'introduced identifier collision', False),
    ('registry_wrong_identity', {PA: A, PB: B}, [(PC, bad_registry)], 'FAIL', 'registry', False),
    ('registry_wrong_label', {PA: A, PB: B}, [(PC, bad_label)], 'FAIL', 'registry', False),
    ('registry_wrong_mapping_quality', {PA: A, PB: B}, [(PC, bad_quality)], 'FAIL', 'registry', False),
    ('introduced_unresolved_component', {PA: A, PB: B}, [(PC, bad_component)], 'FAIL', 'UNRESOLVED_MIM_REFERENCE', False),
    ('wrong_proposal_payload_hash', {PA: A, PB: B}, [(PC, REGISTRY)], 'FAIL', 'after hash mismatch', True),
    ('inherited_duplicate_unchanged', {PA: A, PB: dict(B, identifier='TEST:A')}, [(PA, changed_a)], 'PASS', None, False),
    ('tracked_maintained_drift', {PA: A}, [(PC, REGISTRY)], 'FAIL', 'maintained inputs differ', False, 'tracked'),
    ('ignored_untracked_maintained_input', {PA: A}, [(PC, REGISTRY)], 'FAIL', 'maintained inputs differ', False, 'untracked'),
]
rows = [execute(*case) for case in cases]
report = {'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'script': str(SCRIPT.relative_to(ROOT)), 'script_sha256': SHA(SOURCE),
          'harness_sha256': SHA(Path(__file__).read_bytes()),
          'scope': 'Actual exact overlay script in isolated fixtures; git metadata mocked to retained fixture bytes or explicit drift paths. Parsing, collision, registry, native partonomy and output code unchanged. No production artifacts or maintained files changed.',
          'controls': rows, 'status': 'PASS' if all(row['passed'] for row in rows) else 'FAIL'}
out = ART / 'independent-review' / ('process-negative-controls-' + STAMP + '.json')
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'path': str(out.relative_to(ROOT)), 'status': report['status'],
                  'failed_controls': [row['name'] for row in rows if not row['passed']]}))
