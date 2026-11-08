"""Read-only checks on the frozen authored proposal; outputs stay private."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import sys
import yaml

P = Path(__file__).resolve().parent
W = P.parents[3]
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
R = C / 'preflight/tenvit-final-application-route-v1'
A = W / 'reports/all_unmatched_20261107/worker-08'
O = A / 'successors/issue-1237-tenvit-v1'
sys.path.insert(0, str(W / 'src'))
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
canonical_sha = lambda obj: hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()).hexdigest()
checks = []
def check(name, condition, detail=None):
    checks.append({'name': name, 'passed': bool(condition), 'detail': detail})

expected = {
    'payloads/Wolfes_Vitamin_Mix.yaml': 'b64eccf46c271520c27c73bc0a5863e2bc56447d1acf7461a90e3d72f9f4384f',
    'author/proposal.json': '73e8fdf31d13a2891482f2ec3ab3b51910a9f902cceea8adef30008071550cb7',
    'author/decision.json': 'f1475252112e3608db55f9e441b9d93248c1e73701bf0dbf9ecf32ea5b0d4d29',
}
for f, h in expected.items(): check('final_hash:' + f, sha(O/f) == h)
final = yaml.safe_load((O / 'payloads/Wolfes_Vitamin_Mix.yaml').read_text())
before = yaml.safe_load((R / 'captures/before-Wolfes_Vitamin_Mix.yaml').read_text())
w09 = yaml.safe_load((R / 'captures/candidate-fe607027.yaml').read_text())
proposal = json.loads((O / 'author/proposal.json').read_text())
decision = json.loads((O / 'author/decision.json').read_text())
matrix = json.loads((R / 'ten-child-identity-matrix.json').read_text())
rows = list(csv.reader((R / 'captures/w09/history/captures/Mixes.csv').read_text().splitlines()))[41:51]
allowed = {'curation_history', 'notes', 'components', 'component_assertion'}
changed = [k for k in set(before) | set(final) if before.get(k) != final.get(k)]
check('only_four_changed_fields', set(changed) == allowed, sorted(changed))
for k in set(before) - allowed: check('unchanged_complete_field:' + k, final[k] == before[k] == w09[k])
check('five_original_and_W09_sixth_history_retained', final['curation_history'][:6] == w09['curation_history'] and w09['curation_history'][:5] == before['curation_history'])
check('one_truthful_W08_event_added', len(final['curation_history']) == 7 and final['curation_history'][-1]['curator'].startswith('worker08:/root ') and final['curation_history'][-1]['llm_assisted'] is True)
check('same_real_existing_beforeimage', proposal['kind'] == 'edit_existing_owner' and proposal['owner_path'] == 'data/ingredients/mapped/Wolfes_Vitamin_Mix.yaml' and proposal['before_sha256'] == sha(R/'captures/before-Wolfes_Vitamin_Mix.yaml'))
for base in [W, C/'integration/worktree']:
    check('current_before:' + str(base), sha(base/proposal['owner_path']) == proposal['before_sha256'])
check('exact_after_capture', sha(A/proposal['after_capture']['path']) == proposal['after_capture']['sha256'])
check('ten_literal_parts', len(final['components']) == 10)
check('recipe_method_unknown_closure', final['component_assertion']['method'] == 'RECIPE_TRANSCRIPTION' and final['component_assertion']['completeness'] == 'UNKNOWN')
check('no_new_mapping_evidence', final['ontology_mapping'] == before['ontology_mapping'])
owner_records = []
auth_children = json.loads((O/'author/child-bindings.json').read_text())['owner_checks']
primary = json.loads((R/'captures/w08/component-ontology-lookup.json').read_text())['rows']
for i, (component, row, planned, authored) in enumerate(zip(final['components'], rows, matrix['children'], auth_children, strict=True)):
    check(f'component_{i}_literal_name_mass_unit', [component['component_name'], component['concentration_value'], component['concentration_unit']] == [row[0], row[1], 'MG_PER_L'])
    check(f'component_{i}_reference', component['reference_scope'] == ('UNMAPPED' if i == 6 else 'MIM_CATALOG') and component.get('component_id') == (None if i == 6 else planned['active_identity']))
    check(f'component_{i}_author_binding_exact', component == authored['selected_component'] and authored['primary_rows'] == planned['primary_ontology_rows'])
    check(f'component_{i}_ontology_rows_rebound', all(x in primary for x in authored['primary_rows']))
    for base in [W, C/'integration/worktree']:
        path = base / authored['current_owner']['path']
        check(f'component_{i}_catalog:' + str(base), sha(path) == authored['current_owner']['sha256'] == planned['active_owner']['sha256'])
    owner_records.append(yaml.safe_load((W / authored['current_owner']['path']).read_text()))
errors = [str(e.message) for e in validate_ingredient(final)]
check('native_strict_one_complete_payload', not errors, errors)
violations = [str(e) for e in validate_component_partonomy([final] + owner_records)]
check('native_partonomy_target_and_ten_exact_children', not violations, violations)
old_cases = json.loads((R/'captures/w08/decisions.json').read_text())
if isinstance(old_cases, dict): old_cases = old_cases['decisions']
prior = next(x for x in old_cases if x['case_id'] == decision['case_id'])
for field in ['case_id','case_input_sha256','source','occurrence_ids','disposition','no_change_reason','missing_requirement','publication_scope']:
    check('case_invariant:' + field, decision[field] == prior[field])
for field in ['reasoning','applicability']:
    check('prior_case_text_preserved:' + field, decision[field].startswith(prior[field]))
check('all_prior_proposal_links_retained', set(prior['proposal_ids']).issubset(decision['proposal_ids']))
check('exact_new_proposal_link_only', set(decision['proposal_ids'])-set(prior['proposal_ids']) == {proposal['proposal_id']})
check('one_trigger_not_six_CB_occurrences', proposal['source_occurrence_ids'] == ['CM_OCC:a181b24b7eb91c50c771bd1c1fc3012fd0cf28f45b49f2750c3d43bda9cdd531'] and proposal['cb_campaign_occurrence_count'] == 0 and len(decision['occurrence_ids']) == 6)
dep = json.loads((O/'author/dependency-dispositions.json').read_text())
old = dep['original_nbrc903_proposal']
check('original_nbrc903_null_before_retained', old['kind']=='new_owner' and old['before_sha256'] is None and sha(A/old['after_capture']['path'])==old['after_capture']['sha256']=='e4a7c5d611dd36f449da97ec674100f58679ab5a5871996e79ca9837e73b2802')
check('dependent_proposal_reproduced_exactly', dep['new_dependent_proposal']==proposal)
for fn,h in json.loads((O/'research/HANDOFF.json').read_text())['files'].items():
    check('copied_research_exact:' + fn, sha(O/'research'/fn)==h)
for entry in json.loads((O/'research/source-read-ledger.json').read_text())['entries']:
    check('research_input_hash:' + entry['path'], sha(Path(entry['path'])) == entry['sha256'])

result = {'at': datetime.now(timezone.utc).isoformat(), 'reviewer':'/root/organics', 'status':'PASS' if all(x['passed'] for x in checks) else 'FAIL',
          'check_count':len(checks), 'failed':[x for x in checks if not x['passed']], 'checks':checks,
          'scope':'One complete final payload and six-occurrence case; native strict one payload and partonomy of that payload plus ten current exact children. Not full corpus QC, whole-child science, source routing or release approval.',
          'case_canonical_sha256':canonical_sha(decision), 'payload_sha256':sha(O/'payloads/Wolfes_Vitamin_Mix.yaml'),
          'native_source_hashes':{str(W/p):sha(W/p) for p in ['src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/validation/component_partonomy.py','src/mediaingredientmech/schema/mediaingredientmech.yaml']}}
(P/'final-validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','check_count','failed','case_canonical_sha256','payload_sha256']}))
raise SystemExit(0 if result['status']=='PASS' else 1)
