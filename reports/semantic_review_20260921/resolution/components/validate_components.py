"""Verify the exact #710 component dispositions and edited record payloads."""
from pathlib import Path
import csv
import hashlib
import json
import yaml
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.validation.write_validated import validate_ingredient

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent


def main():
    plans = json.loads((OUT / 'applied-changes.json').read_text())
    results = {}
    for plan in plans:
        relative = plan.get('after_path', plan['source_record'])
        path = ROOT / relative
        record = yaml.safe_load(path.read_text())
        errors = validate_ingredient(record)
        assert not errors, (relative, errors)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == plan['after_sha256'], relative
        assert record == plan['after'], relative
        results[relative] = 'PASS'
    records = [yaml.safe_load(p.read_text()) for folder in ['mapped','unmapped']
               for p in sorted((ROOT / 'data/ingredients' / folder).glob('*.yaml'))]
    assert not validate_component_partonomy(records)
    before = json.loads((OUT / 'before-records.json').read_text())
    relative = 'data/ingredients/mapped/TYGVS_Glucose.yaml'
    previous = before[relative]['record']
    current = yaml.safe_load((ROOT / relative).read_text())
    assert current['components'] == previous['components']
    for field in ['method', 'completeness']:
        assert current['component_assertion'][field] == previous['component_assertion'][field]
    dispositions = list(csv.DictReader((OUT/'dispositions.tsv').open(), delimiter='\t'))
    baseline = list(csv.DictReader((ROOT/'reports/semantic_review_20260921/findings.tsv').open(), delimiter='\t'))
    expected = {r['finding_id'] for r in baseline if r['kind'] in {'component_source_scope','ambiguous_abbreviation','recipe_identity'}}
    assert len(dispositions) == len(expected) == 54
    assert {r['finding_id'] for r in dispositions} == expected
    for row in dispositions:
        assert hashlib.sha256((ROOT / row['current_record']).read_bytes()).hexdigest() == row['current_record_sha256']
        if row['source_record'] == relative:
            assert row['disposition'] == 'OPEN_SOURCE_VERIFICATION'
    results.update({'all_live_component_partonomy':'PASS', 'adversarial_tygvs_no_strengthening':'PASS', 'exact_finding_coverage_and_record_hashes':'PASS'})
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
