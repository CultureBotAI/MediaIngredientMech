from pathlib import Path
import copy, datetime, hashlib, importlib.util, json, sys
import yaml

R = Path.cwd()
C = R / '.temp/all-unmatched-20261107'
O = C / 'preflight/polypeptone-owl-reassessment-v1'
D = C / 'preflight/polypeptone-final-grounding-decision-v1'
I = C / 'integration/worktree'
T = R / '.temp/kgm-unmapped-20261107'
H = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
sys.path.insert(0, str(I / 'src'))
from mediaingredientmech.validation.write_validated import validate_ingredient
builder = T / 'claw/scripts/build_mim_ingredient_sssom.py'
spec = importlib.util.spec_from_file_location('owl_review_native_builder', builder)
b = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = b
spec.loader.exec_module(b)
source = D / 'snapshot/w05-Polypeptone.yaml'
assert H(source) == 'be254d39d8edd3664f74f0ecb76dd0cfdd5d8c597930b088fba3f55e84d18525'
before = yaml.safe_load(source.read_text())
bd = ['Polypeptone peptone (BD-BBL)', 'Polypeptone Peptone (BD 211910)', 'Polypeptone (BBL)']
results = []
for oid, label, ont in [('FOODON:03315306', 'protein hydrolyzates', 'FOODON'), ('mesh:D011492', 'Protein Hydrolysates', 'MESH'), ('mesh:D010461', 'Peptones', 'MESH')]:
    record = copy.deepcopy(before)
    record['ontology_mapping'].update(ontology_id=oid, ontology_label=label, ontology_source=ont, mapping_quality='NARROW_MATCH')
    for synonym in record['synonyms']:
        if synonym['synonym_text'] in bd:
            synonym['synonym_type'] = 'REJECTED_LABEL'
    validate_ingredient(record)
    rows = b._row_from_yaml(R / 'data/ingredients/mapped/Polypeptone.yaml', {}, {}, {}, {}, record=record, owners={})
    assert len(rows) == 2
    assert {(x['predicate_id'], x['object_id']) for x in rows} == {('skos:broadMatch', oid), ('skos:exactMatch', 'kgmicrobe.ingredient:polypeptone')}
    assert all(x not in row['other'].split('|') for x in bd for row in rows)
    assert record['identifier'] == before['identifier']
    assert record['nutritional_roles'] == before['nutritional_roles']
    assert record['curation_history'] == before['curation_history']
    results.append({'ontology_id': oid, 'schema': 'PASS', 'rows': rows, 'science_approval_from_validation': False})
# A finite interpretation of the isolated disputed axiom, not a consistency proof
# or reasoner execution over FoodOn's full import closure.
P, F, member = {'x'}, {'y'}, {('x', 'y')}
existential = {x for x in {'x', 'y'} if any((x, y) in member and y in F for y in {'x', 'y'})}
assert P <= existential
assert not P <= F
out = {'at': datetime.datetime.now(datetime.UTC).isoformat(), 'source': {'path': str(source.relative_to(R)), 'sha256': H(source)}, 'builder': {'path': str(builder.relative_to(R)), 'sha256': H(builder)}, 'schema_sha256': H(I / 'src/mediaingredientmech/schema/mediaingredientmech.yaml'), 'in_memory_only': True, 'maintained_or_candidate_writes': False, 'results': results, 'isolated_axiom_countermodel': {'class_P': ['x'], 'class_F': ['y'], 'member_of': [['x', 'y']], 'P_subclass_exists_member_F': True, 'P_subclass_F': False, 'scope': 'Disproves the implication of this isolated existential axiom to P is_a F; not a full ontology consistency proof, role assertion or legal conclusion.'}}
with (O / 'native-mechanism-checks.json').open('x') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(json.dumps({'native_variants': len(results), 'rows_each': 2, 'status': 'PASS', 'no_science_by_schema': True}))
