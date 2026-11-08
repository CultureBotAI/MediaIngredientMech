from pathlib import Path
from datetime import datetime,timezone
import dataclasses, hashlib,json, shutil
import yaml
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1/dependencies';B=W/'reports/all_unmatched_20261107/worker-05'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,o):p.parent.mkdir(parents=True,exist_ok=True);assert not p.exists();p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
P=json.loads((S/'proposals.json').read_text())['proposals'];E=json.loads((S/'evidence.json').read_text())['evidence'];D=json.loads((S/'case-deltas.json').read_text())['case_deltas']
oldE=json.loads((S/'inputs/current-core/evidence.json').read_text())['evidence'];allids={x['evidence_id'] for x in oldE+E}
capture_checks=[]
for x in P+E:
 for slot in ['capture','after_capture']:
  if slot not in x:continue
  c=x[slot];s=c['path'];p=S/s.removeprefix('buffer-parts-v1/dependencies/') if s.startswith('buffer-parts-v1/dependencies/') else B/s
  assert h(p)==c['sha256'];capture_checks.append({'path':s,'sha256':h(p)})
for p in P:
 assert p['kind']=='edit_existing_owner' and h(W/p['owner_path'])==p['before_sha256']
 assert set(p['evidence_ids'])<=allids
 for cid in p['case_ids']:
  d=next(d for d in D if d['case_id']==cid)
  assert p['proposal_id'] in d['union_proposal_ids']
  assert {'path':p['owner_path'],'sha256':p['before_sha256']} in d['union_owner_records']
for e in E:
 assert e['kind'] in {'primary_source','source_snapshot','ontology','native_record_review','independent_review','unsuccessful_search','local_validation'}
 if e['url'] is not None:assert e['accessed_at']
paths=list((W/'data/ingredients/mapped').glob('*.yaml'))+list((W/'data/ingredients/unmapped').glob('*.yaml'))
by={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in paths}
parent=W/'.temp/w05-buffer-parts-v1/parents/proposed/Peptone.yaml';pcopy=S/'validation/provisional-parent-context-Peptone.yaml';shutil.copyfile(parent,pcopy);pr=yaml.safe_load(pcopy.read_text());assert pr['identifier']=='kgmicrobe.ingredient:peptone'
by['data/ingredients/mapped/Peptone.yaml']=pr
for p in P:by[p['owner_path']]=yaml.safe_load((S/'proposed'/Path(p['owner_path']).name).read_text())
violations=validate_component_partonomy(by.values());ids={by[p['owner_path']]['identifier'] for p in P};local=[v for v in violations if v.record_id in ids]
assert not local
afterparts=[by[p['owner_path']]['components'] for p in P]
assert sum(c.get('component_id')=='kgmicrobe.ingredient:peptone' for cs in afterparts for c in cs)==5
assert sum(c['component_name'].lower()=='peptone' and c['reference_scope']=='UNMAPPED' and 'component_id' not in c for cs in afterparts for c in cs)==10
g=yaml.safe_load((S/'negative-controls/GYPS.yaml').read_text());assert g['components'][2]['component_id']=='MICRO:0000178';assert h(S/'negative-controls/GYPS.yaml')==h(W/'data/ingredients/mapped/GYPS.yaml')
assert by['data/ingredients/mapped/Fastidious_Anaerobe_Broth_With_Meat_Granules.yaml']['components'][0]['reference_scope']=='UNMAPPED'
for fn in ['PY-glucose-rumen_Fluid.yaml','PYG_Rumen_Fluid.yaml']:assert by['data/ingredients/mapped/'+fn]['components'][3]['component_name']=='rumen fluid' and by['data/ingredients/mapped/'+fn]['components'][3]['reference_scope']=='UNMAPPED'
put(S/'validation/focused-referential-check.json',{'at':datetime.now(timezone.utc).isoformat(),'command':'PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src .temp/all-unmatched-worker-05/venv/bin/python .temp/w05-buffer-parts-v1/dependencies/check_focused.py','result':'PASS scoped 15 candidates','scope':'In-memory baseline plus 15 child replacements and provisional generic Peptone target. Focused reference-shape test only; root final full successor overlay and final parent exact-byte review are still required.','baseline_owner_count':len(paths),'provisional_parent':{'source_path':str(parent.relative_to(W)),'copied_path':str(pcopy.relative_to(S)),'sha256':h(pcopy),'identifier':pr['identifier'],'limitation':'Parent ontology scientific investigation remained active when this focused structural test ran. This capture is diagnostic, never a selectable parent proposal or approval.'},'all_overlay_violation_count':len(violations),'local_candidate_violation_count':len(local),'all_violations':[dataclasses.asdict(v) for v in violations],'capture_checks':capture_checks,'generic_target_count':5,'withdrawn_peptone_id_count':10,'GYPS_Bacto_unchanged':True,'existing_rumen_and_meat_withdrawals_preserved':True,'source_case_proposal_owner_backlinks_checked':True,'no_scientific_or_export_approval':True})
print(json.dumps({'all_overlay_violations':len(violations),'local_candidate_violations':len(local),'capture_checks':len(capture_checks),'generic':5,'withdrawals':10}))
