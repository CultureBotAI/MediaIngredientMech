"""Native whole-catalog proposal overlay and explicit borax dependency regression."""
from pathlib import Path
import json,yaml,hashlib,datetime,sys,dataclasses
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
R=Path.cwd();W=R/'reports/all_unmatched_20261107/worker-01';O=W/'shard';V=O/'validation';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
P=json.loads((O/'proposals.json').read_text())['proposals'];baseline={str(p.relative_to(R)):yaml.safe_load(p.read_text()) for p in (R/'data/ingredients').rglob('*.yaml')}
focus=next(p for p in P if p['proposal_id']=='KG26-PROP-175-STRUCTURAL-IDENTITY')
dep_paths={'data/ingredients/mapped/UW_Concentrated_Base.yaml','data/ingredients/mapped/UW_Concentrated_Base_No_Mo.yaml','data/ingredients/mapped/UW_Concentrated_Base_No_Sulfur.yaml'}
deps=[p for p in P if p['owner_path'] in dep_paths]
def overlay(props):
 records=dict(baseline);targets=set()
 for p in props:
  old=p['owner_path'];target=p.get('integration_target_path') or p.get('new_owner_path') or p.get('destination_path') or old
  assert target not in targets;targets.add(target)
  if p['kind']=='edit_existing_owner':
   assert old in records and sha(R/old)==p['before_sha256'];del records[old]
  else:assert old not in records
  cap=W/p['after_capture']['path'];assert sha(cap)==p['after_capture']['sha256'];assert target not in records
  records[target]=yaml.safe_load(cap.read_text())
 return list(records.values())
def native(records):return [dataclasses.asdict(v) for v in validate_component_partonomy(records)]
scenarios={'baseline':native(list(baseline.values())),'borax_only':native(overlay([focus])),'other_proposals_without_borax_or_dependencies':native(overlay([p for p in P if p is not focus and p not in deps])),'all_without_dependency_proposals':native(overlay([p for p in P if p not in deps])),'all_proposals':native(overlay(P))}
expected_ids={baseline[p]['identifier'] for p in dep_paths}
def exact_three(v):return len(v)==3 and {x['record_id'] for x in v}==expected_ids and all(x['code']=='UNRESOLVED_MIM_REFERENCE' and 'CHEBI:131366' in x['message'] for x in v)
assert not scenarios['baseline'];assert not scenarios['other_proposals_without_borax_or_dependencies'];assert exact_three(scenarios['borax_only']);assert exact_three(scenarios['all_without_dependency_proposals'])
phase=sys.argv[2] if len(sys.argv)>2 else 'final'
if phase=='before-dependencies':
 assert not deps and exact_three(scenarios['all_proposals']);result='EXPECTED_FAILURE_REPRODUCED'
else:
 assert phase=='final';assert {p['owner_path'] for p in deps}==dep_paths;assert not scenarios['all_proposals'];result='PASS'
out=V/(sys.argv[1]+'.json');assert not out.exists()
out.write_text(json.dumps({'at':datetime.datetime.now(datetime.UTC).isoformat(),'phase':phase,'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1168','validator':'src/mediaingredientmech/validation/component_partonomy.py','validator_sha256':sha(R/'src/mediaingredientmech/validation/component_partonomy.py'),'proposals_sha256':sha(O/'proposals.json'),'baseline_record_count':len(baseline),'proposal_count':len(P),'dependent_proposal_count':len(deps),'overlay_method':'Remove each edited exact before owner_path; validate original before hash; add its exact after record under intended target path. New owners must not replace existing paths. Never retain an old identifier by keying the replacement on the after identifier. Native validator runs on every record, without filtering to proposed IDs.','scenarios':scenarios,'prior_receipt_scope_correction':'combined-proposals-content-final-v1.json checked only proposed-parent errors. Its unrelated_baseline_partonomy_violation_count=3 was incorrectly called baseline: this actual baseline has zero, and those three errors are induced by borax identifier retirement. That limited PASS is superseded for integration integrity, with its original bytes preserved.','result':result},indent=2)+'\n')
print(result, {k:len(v) for k,v in scenarios.items()})
