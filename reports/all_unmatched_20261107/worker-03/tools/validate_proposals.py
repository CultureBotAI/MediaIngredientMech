"""Worker03 isolated proposal validation; no canonical writes or exports.

Uses the maintained closed-schema and component-partonomy validators, then
checks the frozen owner hashes and collisions against the actual catalog.
The result is structural validation, never scientific or release approval.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import sys
import yaml

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'MAPPING_SEMANTICS.md').is_file())
sys.path.insert(0, str(ROOT / 'src'))
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

OUT = ROOT / 'reports/all_unmatched_20261107/worker-03'


def main():
    proposals = json.loads((OUT / 'proposals.json').read_text())['proposals']
    # The maintained catalog consists of direct-child records only; backup or
    # nested research files must not acquire owner status (#699).
    baseline = {str(p.relative_to(ROOT)): yaml.safe_load(p.read_text())
                for folder in ('mapped', 'unmapped')
                for p in sorted((ROOT / 'data/ingredients' / folder).glob('*.yaml'))}
    overlay = dict(baseline)
    rows, errors, touched = [], [], set()
    for proposal in proposals:
        target = proposal['owner_path']
        payload = OUT / proposal['after_capture']['path']
        actual = hashlib.sha256(payload.read_bytes()).hexdigest()
        assert actual == proposal['after_capture']['sha256'], payload
        assert target not in touched, ('multiple competing proposals for owner', target)
        touched.add(target)
        if proposal['kind'] == 'edit_existing_owner':
            assert hashlib.sha256((ROOT / target).read_bytes()).hexdigest() == proposal['before_sha256']
        else:
            assert target not in baseline and not (ROOT / target).exists(), target
        record = yaml.safe_load(payload.read_text())
        if proposal['kind'] == 'edit_existing_owner':
            before = baseline[target]
            old_history = before.get('curation_history', [])
            history = record.get('curation_history', [])
            assert len(history) > len(old_history) and history[:len(old_history)] == old_history, ('history not appended', target)
            fields = {'roles', 'causal_graphs'} | {k for k in before.keys() | record.keys() if k.endswith('_roles')}
            for field in fields:
                assert record.get(field) == before.get(field), ('out-of-scope biological assertion change', target, field)
        else:
            assert record.get('curation_history'), ('new owner lacks history', target)
        failures = [str(result) for result in validate_ingredient(record)]
        rows.append({'proposal_id': proposal['proposal_id'], 'owner_path': target,
                     'after_sha256': actual, 'schema_errors': failures})
        errors.extend(failures)
        overlay[target] = record
    prior = [str(v) for v in validate_component_partonomy(baseline.values())]
    after = [str(v) for v in validate_component_partonomy(overlay.values())]
    new = sorted(set(after) - set(prior))
    errors.extend(new)
    collisions = []
    for target in sorted(touched):
        record = overlay[target]
        if record.get('mapping_status') == 'REJECTED':
            continue
        identifier = record.get('identifier')
        for other, candidate in overlay.items():
            if other == target or candidate.get('mapping_status') == 'REJECTED':
                continue
            if candidate.get('identifier') != identifier:
                continue
            if target in baseline and baseline[target].get('identifier') == identifier and other in baseline and baseline[other].get('identifier') == identifier:
                continue
            collisions.append({'owner_path': target, 'other_owner_path': other, 'identifier': identifier})
    if collisions:
        errors.append('New active primary-identifier collisions require explicit ownership resolution.')
    result = {'proposal_count': len(rows), 'baseline_owner_count': len(baseline),
              'input_proposals_sha256': hashlib.sha256((OUT / 'proposals.json').read_bytes()).hexdigest(),
              'validator_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'proposals': rows,
              'baseline_partonomy_violations': prior, 'overlay_partonomy_violations': after,
              'introduced_partonomy_violations': new,
              'new_identifier_collisions': collisions,
              'maintained_files_written': 0, 'scientific_approval': False,
              'status': 'PASS' if not errors else 'FAIL'}
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
