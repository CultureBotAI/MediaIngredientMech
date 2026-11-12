"""Offline synthetic extraction/CLI/native Rule F integration; no repository edits."""
from pathlib import Path
from unittest.mock import patch
import contextlib
import datetime
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
OUT = HERE / 'rule-f-integration'
OUT.mkdir(exist_ok=True)
INPUTS = OUT / 'records'
INPUTS.mkdir(exist_ok=True)
sys.path.insert(0, str(RUN / 'claw/scripts'))

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

builder_path = RUN / 'claw/scripts/build_mim_ingredient_sssom.py'
validator_path = RUN / 'mim/scripts/validate_sssom_invariants.py'
builder = load('followup_rule_f_builder', builder_path)
validator = load('followup_rule_f_validator', validator_path)
base = ('identifier: CHEBI:15377\nmapping_status: MAPPED\n'
        'ontology_mapping:\n  ontology_id: CHEBI:15377\n'
        '  ontology_label: water\n  mapping_quality: EXACT_MATCH\n')
for name in ('Dated', 'Dateless_One', 'Dateless_Two'):
    history = 'curation_history:\n  - timestamp: "2026-10-15T00:00:00Z"\n' if name == 'Dated' else ''
    (INPUTS / f'{name}.yaml').write_text(base + f'preferred_term: {name}\n' + history)
output = OUT / 'synthetic.sssom.tsv'
assert not output.exists(), 'Append-only fixture must not overwrite an earlier result'
with contextlib.ExitStack() as stack:
    for attr, value in {
        'MIM_INGREDIENTS_DIR': INPUTS,
        '_load_residual_categorization': lambda: {},
        '_load_kgm_source_index': lambda: {},
        '_load_kgm_labels': lambda: {},
        '_load_chebi_labels': lambda *args: {'CHEBI:15377': 'water'},
    }.items():
        stack.enter_context(patch.object(builder, attr, value))
    stack.enter_context(patch.object(sys, 'argv', ['builder', '--no-validate',
        '--no-preserve-validation', '--output', str(output)]))
    builder.main()
prelude, fields, rows = validator._read_sssom(output)
rejects = list(validator.evaluate_rule_f(rows))
assert len(rows) == 3
assert {row['subject_id']: row['mapping_date'] for row in rows} == {
    'MIM:Dated': '2026-10-15', 'MIM:Dateless_One': '', 'MIM:Dateless_Two': ''}
assert {row['subject_id'] for _, row, _ in rejects} == {'MIM:Dateless_One', 'MIM:Dateless_Two'}
assert not list(validator.evaluate_rule_g(prelude, rows))
reject_path = OUT / 'native-rule-f-rejects.tsv'
validator._write_reject_tsv(reject_path, prelude, fields, [(row, reason) for _, row, reason in rejects])
receipt = {
    'captured_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status': 'PASS', 'row_count': len(rows), 'rule_f_reject_count': len(rejects),
    'rejects': [{'row_number': n, 'row': row, 'reason': reason} for n, row, reason in rejects],
    'rule_g_findings': 0,
    'scope': 'Native YAML extraction and CLI writer with synthetic offline label/KG inputs, then unmodified native Rule F evaluation and reject writer. Real corpus and generator source unchanged. This proves diagnostic rejection routing, not scientific validity of fixture labels.',
    'artifacts': [{'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
        for p in [builder_path, validator_path, output, reject_path, *sorted(INPUTS.glob('*.yaml'))]],
}
(OUT / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
