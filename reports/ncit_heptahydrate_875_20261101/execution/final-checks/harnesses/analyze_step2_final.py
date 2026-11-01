"""Independently bound the approved #875 product delta against its durable base."""
from pathlib import Path
from collections import Counter
import csv, hashlib, io, json, subprocess

run = Path(__file__).resolve().parent
root = run / 'step2-mim'
base = '40b787d37d33d544551389ff019f2d64ad63d7cc'
def old(path):
    return subprocess.check_output(['git', 'show', base + ':' + path], cwd=root)
def table(data, *, sssom=False):
    lines = data.decode().splitlines()
    if sssom:
        lines = [x for x in lines if not x.startswith('#')]
    return list(csv.DictReader(lines, delimiter='\t'))
def sha(data):
    return hashlib.sha256(data).hexdigest()

path = 'UNIFIED_INGREDIENT_MAPPING.tsv'
before = {r['ingredient_name']: r for r in table(old(path))}
after = {r['ingredient_name']: r for r in table((root / path).read_bytes())}
assert before.keys() == after.keys()
changed = {n: {k: [before[n][k], after[n][k]] for k in after[n] if before[n][k] != after[n][k]} for n in before if before[n] != after[n]}
assert set(changed) == {'Na2HPO4 x 7 H2O', 'Na2HPO4.7H2O', 'Na2HPO4·7H2O'}, changed
assert all(set(v) == {'mim_id', 'synonyms'} for v in changed.values()), changed
assert all(v['mim_id'] == ['kgmicrobe.compound:na2hpo4_x_7_h2o', 'NCIT:C61946'] for v in changed.values())
assert all(v['synonyms'][1] == v['synonyms'][0] + '|Sodium Phosphate, Dibasic, Heptahydrate' for v in changed.values())
path = 'mappings/ingredient_mappings.sssom.tsv'
sssom = (root / path).read_bytes()
old_sssom = old(path)
subject = 'MIM:Na2hpo4_X_7_H2o'
outside = lambda b: b''.join(l for l in b.splitlines(keepends=True) if not l.startswith((subject + '\t').encode()))
assert outside(old_sssom) == outside(sssom)
path = 'reports/semantic_review_20260921/resolution/current-review.json'
baseline_review = json.loads(old(path))
current_review = json.loads((root / path).read_bytes())
assert baseline_review['blocking_finding_ids'] == current_review['blocking_finding_ids']
path = 'reports/semantic_review_20260921/resolution/finding-dispositions.tsv'
findings_before = table(old(path)); findings_after = table((root / path).read_bytes())
assert len(findings_before) == len(findings_after)
for a, b in zip(findings_before, findings_after):
    if a != b:
        assert b['current_record'] == 'data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml'
        assert {k: v for k, v in a.items() if k != 'current_record_sha256'} == {k: v for k, v in b.items() if k != 'current_record_sha256'}
refresh = json.loads((root / 'reports/ingredient_bundle_20261101_ncit875/dependency-refresh.json').read_bytes())
locations = [r['base_decision_locations'] for r in refresh['selected_mapping_evidence_unchanged']]
result = {
    'baseline': base, 'unified_rows': len(after), 'unified_rows_changed': len(changed),
    'unified_rows_unchanged': len(after) - len(changed), 'unified_delta': changed,
    'unified_sha256': sha((root / 'UNIFIED_INGREDIENT_MAPPING.tsv').read_bytes()),
    'occurrences': sum(int(r['occurrence_count']) for r in after.values()),
    'sssom_before_rows': len(table(old_sssom, sssom=True)), 'sssom_after_rows': len(table(sssom, sssom=True)),
    'sssom_sha256': sha(sssom), 'non_target_sssom_bytes_unchanged': True,
    'blocking_finding_ids_unchanged': len(current_review['blocking_finding_ids']),
    'blocking_assertions_before': len(baseline_review['blocking_assertion_ids']),
    'blocking_assertions_after': len(current_review['blocking_assertion_ids']),
    'finding_dispositions_unchanged_except_target_record_hashes': True,
    'selected_companion_mapping_locators_relocated': sum(p['before'] != p['after'] for p in locations),
    'companion_claims_and_evidence_unchanged': True,
    'rejected_empty_identity': sum(r['mapping_status'] == 'REJECTED' and not r['mim_id'] for r in after.values()),
    'local_compound_chebi_leaks': sum(r['mim_id'].startswith('kgmicrobe.compound:') and any(r[k].startswith('CHEBI:') for k in ('culturemech_term_id', 'chebi_id', 'kg_microbe_node_id')) for r in after.values()),
}
assert result['rejected_empty_identity'] == result['local_compound_chebi_leaks'] == 0
with (run / 'step2-unified-evidence/final-comparison-v2.json').open('x') as f:
    json.dump(result, f, indent=2); f.write('\n')
print(json.dumps(result, indent=2))
