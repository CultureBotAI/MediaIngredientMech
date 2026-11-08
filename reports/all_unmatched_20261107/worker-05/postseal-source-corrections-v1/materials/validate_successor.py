"""Read-only checks of the isolated BSA successor and its exact source bindings."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys

import yaml

W = Path.cwd()
sys.path.insert(0, str(W / 'src'))
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.validation.write_validated import validate_ingredient

L = Path(__file__).resolve().parent
R = W / 'reports/all_unmatched_20261107/worker-05'
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
PREFIX = 'postseal-source-corrections-v1/materials/'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def obj(x):
    return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def load(name):
    return json.loads((L / name).read_text())

def save(name, x):
    p = L / name
    assert not p.exists()
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')

def resolve(c):
    if c['root'] == 'source':
        return C / c['path']
    if c['path'].startswith(PREFIX):
        return L / c['path'][len(PREFIX):]
    return R / c['path']

new = yaml.safe_load((L / 'proposed/Bovine_Serum_Albumin.yaml').read_text())
old = yaml.safe_load((L / 'inputs/predecessor.yaml').read_text())
baseline = yaml.safe_load((L / 'inputs/maintained-before.yaml').read_text())
errors = validate_ingredient(new, schema_path=W / 'src/mediaingredientmech/schema/mediaingredientmech.yaml')
assert not errors, errors
assert new['curation_history'][:-1] == old['curation_history']
assert new['supplied_form'][5]['name'] == old['supplied_form'][5]['name']
for k in new:
    if k not in ['curation_history', 'supplied_form']:
        assert new[k] == old[k], k
assert len(new['supplied_form']) == len(old['supplied_form'])
for i in range(len(new['supplied_form'])):
    if i != 5:
        assert new['supplied_form'][i] == old['supplied_form'][i]

prior_d = load('inputs/decisions.json')
ds = load('decisions.json')
ps = load('proposals.json')
new_es = load('evidence.json')
reused_es = load('inputs/evidence-reused.json')
assert len(ds) == 5 and len(ps) == 1 and len(new_es) == 3 and len(reused_es) == 29
assert [d['case_id'] for d in ds] == ps[0]['case_ids']
assert [d['case_index'] for d in ds] == [11, 20, 70, 118, 120]
assert sum(len(d['occurrence_ids']) for d in ds) == 7
assert len({o for d in ds for o in d['occurrence_ids']}) == 7
for before, after in zip(prior_d, ds):
    assert after['postseal_reassessment']['predecessor_decision_object_sha256'] == obj(before)
    assert after['independent_review']['status'] == 'pending'
    for k in ['case_id', 'case_input_sha256', 'source', 'occurrence_ids', 'disposition', 'proposal_ids', 'owner_records', 'preserved_source_holds', 'preserved_downstream_holds']:
        assert before[k] == after[k]
    if after['case_index'] != 70:
        assert before['reasoning'] == after['reasoning']
        assert before['applicability'] == after['applicability']
    else:
        assert '50 g batch' in after['reasoning'] or '50 g, as a main batch' in after['reasoning']
        assert 'do not assert 50 g/L' in after['reasoning']
        assert 'BSK' in after['reasoning']
all_es = reused_es + new_es
assert len({e['evidence_id'] for e in all_es}) == len(all_es)
assert {eid for d in ds for eid in d['evidence_ids']} <= {e['evidence_id'] for e in all_es}
assert set(ps[0]['evidence_ids']) <= {e['evidence_id'] for e in all_es}
checked = []
for e in all_es:
    c = e['capture']
    assert sha(resolve(c)) == c['sha256']
    assert e.get('supports_or_contradicts') and e.get('locator')
    checked.append({'evidence_id': e['evidence_id'], 'capture': c})
assert sha(resolve(ps[0]['after_capture'])) == ps[0]['after_capture']['sha256']
assert sha(W / ps[0]['owner_path']) == ps[0]['before_sha256']
assert ps[0]['before_sha256'] == load('inputs/proposal.json')['before_sha256']

preflight = load('preflight.json')
for c in preflight['source_inputs']:
    assert sha(W / c['path']) == c['sha256']
canonical_es = json.loads((R / 'final-correction-v1/core/evidence.json').read_text())['evidence']
assert len(canonical_es) == 1537
ce = {e['evidence_id']: e for e in canonical_es}
assert all(ce[e['evidence_id']] == e for e in reused_es)

individuals = []
individual_inventory = []
for p in sorted((W / 'data/ingredients').rglob('*.yaml')):
    x = yaml.load(p.read_text(), Loader=yaml.CSafeLoader)
    individuals.append((p, x))
    individual_inventory.append({'path': str(p.relative_to(W)), 'sha256': sha(p)})
matches = [(p, x) for p, x in individuals if p == W / ps[0]['owner_path']]
assert len(matches) == 1 and matches[0][1] == baseline
full_before = validate_component_partonomy([x for _, x in individuals])
full_after = validate_component_partonomy([new if p == W / ps[0]['owner_path'] else x for p, x in individuals])
assert not full_before and not full_after
save('maintained-individual-inventory.json', individual_inventory)

collections = []
aggregate_matches = []
for name in ['mapped_ingredients.yaml', 'unmapped_ingredients.yaml']:
    p = W / 'data/curated' / name
    coll = yaml.load(p.read_text(), Loader=yaml.CSafeLoader)
    collections.append({'path': str(p.relative_to(W)), 'sha256': sha(p)})
    aggregate_matches.extend(x for x in coll['ingredients'] if x.get('identifier') == baseline['identifier'])
assert len(aggregate_matches) == 1 and aggregate_matches[0] == baseline
sssom = W / 'mappings/ingredient_mappings.sssom.tsv'
lines = [line for line in sssom.read_text().splitlines() if line and not line.startswith('#')]
fields = lines[0].split('\t')
rows = [dict(zip(fields, line.split('\t'))) for line in lines[1:] if line.split('\t')[0] == 'MIM:Bovine_Serum_Albumin']
assert len(rows) == 1
assert rows[0]['object_id'] == 'NCIT:C85253' and rows[0]['predicate_id'] == 'skos:exactMatch'
save('maintained-surfaces.json', {
    'scope': 'Read-only baseline surface correspondence. No new scientific endorsement of inherited mappings or metadata; no SSSOM rebuild performed.',
    'individual': {'path': ps[0]['owner_path'], 'sha256': sha(W / ps[0]['owner_path'])},
    'aggregate_collections': collections, 'matching_aggregate_records': 1,
    'aggregate_record_equals_individual': True,
    'sssom': {'path': str(sssom.relative_to(W)), 'sha256': sha(sssom), 'rows': rows},
    'identity_predicate_synonyms_and_partonomy_inputs_equal_to_predecessor': True,
    'full_proposed_corpus_not_run': 'The full campaign proposal overlay and native compilation are coordinator responsibilities. This check substitutes only the isolated BSA successor into the unchanged maintained baseline.',
})

native = load('native-inspect-after.json')
assert native['status'] == 'inspection_only'
assert native['source']['inputs'][0]['sha256'] == ps[0]['after_capture']['sha256']
assert len(native['targets']) == 1
assert len((L / 'strict-errors.tsv').read_text().splitlines()) == 1
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
assert head == preflight['head']
status = subprocess.check_output(['git', 'status', '--short'], text=True)
save('validation.json', {
    'author': '/root/materials_research', 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status': 'passed', 'scope': 'Author mechanical checks, not an independent scientific review.',
    'counts': {'cases': 5, 'occurrences': 7, 'proposals': 1, 'additive_evidence': 3, 'reused_exact_evidence': 29, 'unchanged_canonical_evidence': 1537},
    'payload_sha256': ps[0]['after_capture']['sha256'],
    'closed_schema_errors': 0,
    'native_inspect': {'path': 'native-inspect-after.json', 'sha256': sha(L / 'native-inspect-after.json'), 'status': 'inspection_only'},
    'strict_cli': {'errors_path': 'strict-errors.tsv', 'errors_sha256': sha(L / 'strict-errors.tsv'), 'error_rows': 0},
    'partonomy': {'maintained_records': len(individuals), 'before_violations': len(full_before), 'isolated_BSA_substitution_violations': len(full_after), 'inventory': 'maintained-individual-inventory.json', 'inventory_sha256': sha(L / 'maintained-individual-inventory.json')},
    'preserved': ['All seven prior history entries as an exact prefix.', 'All seven other supplied-form entries.', 'Identity, mapping evidence, synonyms, chemical properties, ingredient type, source history, notes and occurrence statistics.', 'All five source cases, seven occurrences and their original holds.', 'All 1537 original canonical evidence objects and all three sealed canonical core files.'],
    'capture_checks': checked, 'git_head': head, 'git_status_short': status,
    'limitations': ['Independent scientific review remains pending.', 'No term lookup, new external request, full campaign overlay, export rebuild or release gate was performed by this author.', 'A current complete-owner or coordinator-union approval is not implied.'],
})
print(json.dumps({'status': 'passed', 'maintained_records': len(individuals), 'full_baseline_and_isolated_overlay_partonomy_violations': [len(full_before), len(full_after)], 'payload_sha256': ps[0]['after_capture']['sha256'], 'cases': 5, 'evidence_checks': len(checked), 'git_status_short': status}))
