"""Record completed Step 4 checks, retaining their exact logs and limitations."""
from pathlib import Path
import datetime
import hashlib
import json
import re

RUN = Path(__file__).resolve().parent
ROOT = RUN / 'step4-mim'
checks = {}
for stage, tag in [('build', 'step4-chain-v2-build'), ('exports', 'step4-exports-v1-exports'), ('gates', 'step4-gates-v1-gates')]:
    group = RUN / 'step4-native-chain-plan/executions' / tag
    complete = json.loads((group / 'complete.json').read_bytes())
    assert complete['complete'] is True and complete['scientific_approval_added'] is False
    for line in (group / 'commands.jsonl').read_text().splitlines():
        declaration = json.loads(line)
        path = RUN / 'logs' / (declaration['name'] + '.json')
        value = json.loads(path.read_bytes())
        assert value['argv'] == declaration['argv'] and value['exit_code'] == 0 and value['finished_at']
        raw = Path(value['log']).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == value['log_sha256']
        checks[declaration['name']] = {'receipt': str(path.relative_to(RUN)), 'receipt_sha256': hashlib.sha256(path.read_bytes()).hexdigest(), **value}

suite = Path(checks['step4-gates-v1-full-suite']['log']).read_text()
summary = re.search(r'(?m)^(\d+ passed(?:, \d+ skipped)?(?:, \d+ warnings)? in [^\n]+)$', suite)
assert summary, 'Missing full-suite success summary'
focused = Path(checks['step4-gates-v1-focused-regressions']['log']).read_text()
assert '351 passed' in focused
state = json.loads((RUN / 'step4-native-chain-plan/executions/step4-gates-v1-gates/verified-output.json').read_bytes())
independent = json.loads((RUN / 'step4-independent/actual-generated-state.json').read_bytes())
assert independent['verdict'] == 'PASS_ACTUAL_GENERATED_SURFACES_WITHOUT_SCIENTIFIC_APPROVAL'
paths = ['mappings/ingredient_mappings.sssom.tsv', 'mappings/other_cross_record_baseline.tsv', 'UNIFIED_INGREDIENT_MAPPING.tsv', 'UNIFIED_INGREDIENT_MAPPING.provenance.json', 'scripts/curate_lithium_glycerophosphate.py', 'tests/test_curate_lithium_glycerophosphate.py']
value = {
    'recorded_at': datetime.datetime.now(datetime.UTC).isoformat(),
    'base': '838d0c2627552b0094545ebb580b5bb9b1a84d57',
    'scope': 'Completed precommit validation of the Step 4 correction; final committed-head and integration reviews follow separately.',
    'full_suite_summary': summary.group(1),
    'focused_tests_passed': 351,
    'checks': checks,
    'native_state': state,
    'independent_generated_surface_check': independent,
    'current_artifact_sha256': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
    'limitations': [
        'Full scientific release retains its native FAIL with 1,732 blocking findings; this structural check grants no scientific approval.',
        'Product labels retain 101 non-blocking warnings and 5,303 no-adapter skips; not every pair was validated.',
        'Native actual-KG label checks had no BTO or MICRO transform files.',
        'Six existing cross-prefix KG node warnings remain for the later #870 step.',
        'The full suite disables default addopts; no local coverage percentage is claimed.',
        'MIM-only tests intentionally skip optional Claw integrations; separate native-enabled lithium regressions ran all 49 cases.'
    ],
    'scientific_approval_added': False,
    'supervisor_binding': None
}
out = RUN / 'step4-final-validation.json'
with out.open('x') as stream:
    json.dump(value, stream, indent=2)
    stream.write('\n')
print(summary.group(1))
print(hashlib.sha256(out.read_bytes()).hexdigest())
