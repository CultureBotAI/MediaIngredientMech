from pathlib import Path
import sys,json,hashlib,subprocess,copy,datetime
import yaml
W=Path.cwd();C=W.parents[2];O=W/'.temp/peptone-final-dependencies-v1';R=O/'lineage-review'
sha=lambda b:hashlib.sha256(b).hexdigest()
canon=lambda d:json.dumps(d,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
def load(p):return json.loads(p.read_bytes())
sel=load(O/'dependency-selection.json');plan=load(O/'author-plan-v2.json');inv=load(R/'verified-origin-inventory-v1.json');ledger=load(O/'machine-ledger.json');receipts=load(O/'write-receipts-v2.json')['rows'];draft=load(O/'inputs/draft-selection.json')
assert sha((O/'dependency-selection.json').read_bytes())=='b1e181a1dfbbc2d0588b377f00e5922c6b5340e86b171b9ebf8233d963f0ad92'
assert sel['type']=='accountable_dependency_sidecar_not_frozen_source_core' and sel['new_frozen_source_cases']==0
core=[]
for p in sel['preserved_W03_source_core']:
 b=(W/p['path']).read_bytes();g=subprocess.check_output(['git','show',sel['source_branch_parent']+':'+p['path']]);assert b==g and sha(b)==p['sha256'];assert len(json.loads(b)[p['object_key']])==p['entries'];core.append(p)
rows=[]
for prop in sel['dependency_proposals']:
 p=next(x for x in plan['rows'] if x['dependency_id']==prop['dependency_id']);before=(W/p['owner_path']).read_bytes();assert sha(before)==prop['before_sha256']==p['maintained_before']['sha256'];assert before==(O/p['maintained_before']['path']).read_bytes()
 old_raw=(O/p['current_payload']['path']).read_bytes();new_raw=(O/prop['payload']['path']).read_bytes();assert sha(old_raw)==p['current_payload']['sha256'];assert sha(new_raw)==prop['payload']['sha256'];old=yaml.safe_load(old_raw);new=yaml.safe_load(new_raw)
 owner=next(x for x in inv['owners'] if x['owner_path']==p['owner_path']);assert prop['native_source_core_member'] is False and prop['frozen_W03_case_ids']==[]
 origin=prop['preserved_foreign_source_origin'];assert origin==(owner['selected_origins'][0] if owner['selected_origins'] else None)
 if origin:
  assert sha(canon(origin))==p['predecessor_origin_object_sha256'];assert sha(canon(origin['proposal']))==origin['proposal_object_sha256']
  gitraw=subprocess.check_output(['git','-C',str(C/f"workers/w{origin['worker']:02d}/worktree"),'show',origin['head']+':'+origin['git_path']]);assert gitraw==old_raw
  for cb in origin['cases']:
   shard=load(Path(origin['frozen_shard_path']));case=next(x for x in shard['cases'] if x['case_id']==cb['case_id']);assert case==cb['frozen_case'] and sha(canon(case))==cb['case_input_sha256'];assert origin['proposal']['proposal_id'] in cb['current_decision']['proposal_ids']
 else:assert old_raw==before and p['owner_path'].endswith('/GYPS.yaml')
 norm=copy.deepcopy(new);norm['components'][p['component_index']]=old['components'][p['component_index']];assert new['components'][p['component_index']]==p['new_component'];assert new['component_assertion']['evidence'][-len(p['append_evidence']):]==p['append_evidence'];norm['component_assertion']['evidence']=norm['component_assertion']['evidence'][:-len(p['append_evidence'])];event=norm['curation_history'].pop();assert norm==old;assert event['changes']==p['event_text'] and event['llm_assisted'] is True and event['curator']=='codex-worker03 /root dependent-origin author';assert event['previous_status']==event['new_status']==old['mapping_status'];assert [(x.get('concentration_value'),x.get('concentration_unit')) for x in old['components']]==[(x.get('concentration_value'),x.get('concentration_unit')) for x in new['components']]
 receipt=next(x for x in receipts if x['dependency_id']==p['dependency_id']);assert receipt['payload']==prop['payload'] and receipt['history_appended']==event
 rows.append({'dependency_id':p['dependency_id'],'payload':prop['payload'],'before_sha256':sha(before),'selected_predecessor_sha256':sha(old_raw),'foreign_origin_retained':origin is not None,'foreign_case_ids':origin['proposal']['case_ids'] if origin else [],'prior_all_field_projection_sha256':sha(canon(norm)),'all_undeclared_fields_exact':True,'history_and_component_evidence_append_only':True,'quantities_and_absences_exact':True,'whole_owner_approval':False})
assert len(rows)==3
for old,new in zip(draft['parent_incoming_reference_closure'],ledger['rows']):
 assert all(old[k]==new[k] for k in ['owner_path','before_sha256','component_index','before_component'])
 assert old['published_w05_proposal']==new['existing_W05_proposal'] and old['published_after_component']==new['existing_W05_component']
 assert old['in37']==new['in_combined37']
assert len(ledger['rows'])==19 and sum(bool(x['existing_W05_proposal']) for x in ledger['rows'])==16 and sum(bool(x['new_W03_dependency_id']) for x in ledger['rows'])==3
incoming=[]
for f in (W/'data/ingredients').rglob('*.yaml'):
 d=yaml.safe_load(f.read_bytes())
 for i,c in enumerate(d.get('components',[])):
  if c.get('component_id')=='MICRO:0000178' and c.get('reference_scope')=='MIM_CATALOG':incoming.append((str(f.relative_to(W)),i))
assert sorted(incoming)==sorted((x['owner_path'],x['component_index']) for x in ledger['rows'])
parentcore=load(R/'inputs/cores/w05/proposals.json')['proposals']
for pid,fname in [('W05-FINAL-MAT-039','Peptone'),('W05-FINAL-MAT-001','Bacto_Peptone')]:
 p=next(x for x in parentcore if x['proposal_id']==pid);b=(O/f'inputs/targets/{fname}.yaml').read_bytes();assert sha(b)==p['after_capture']['sha256'];gp='reports/all_unmatched_20261107/worker-05/'+p['after_capture']['path'];assert b==subprocess.check_output(['git','-C',str(C/'workers/w05/worktree'),'show','108e213e96f7d423ee345ce265d692e79063127c:'+gp])
controls=load(R/'final-controls-fixture/validation/focused-controls-v2.json');drifts=load(R/'final-controls-fixture/validation/dependency-drift-controls-v2.json')
assert controls['status']=='PASS' and controls['control_count']==28 and drifts['status']=='PASS' and len(drifts['controls'])==5
assert controls['retention_proofs']==load(O/'validation/focused-controls-v2.json')['retention_proofs']
assert [x['control'] for x in controls['controls']]==[x['control'] for x in load(O/'validation/focused-controls-v2.json')['controls']]
for c in controls['controls']:
 if c['result']=='PASS_REFUSED_NO_OUTPUT_CHANGE':assert c['exception']=='ValueError' and c['no_output_change']
for d in drifts['controls']:assert d['status']=='REFUSED_NO_OUTPUT' and not d['output_exists']
assert sha((O/'scripts/guarded_writer_v1.py').read_bytes())=='7eb1aef40ff697e6688ce4f03e52a58016cbe50353cfd9e7ef5f0758971f4e72'
assert sha((O/'scripts/guarded_writer_v2.py').read_bytes())=='3ee4c4a5a4cd982c36da26dc8a811f56d34fbdfa4fa30735238d61369bb552d2'
sys.path.insert(0,str(W/'src'))
from mediaingredientmech.validation.write_validated import validate_ingredient
for p in sel['dependency_proposals']:assert not validate_ingredient(yaml.safe_load((O/p['payload']['path']).read_bytes()))
report={'reviewer':'/root/peptone_final_lineage','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS_EXACT_DEPENDENCY_LINEAGE_AND_CONTROL_REVIEW_WITH_INTAKE_LIMITS','independence':'Did not author any proposed payload, mutation plan, producer or author controls. Earlier work independently inventoried source lineages; this receipt independently reads complete new payloads/selector, recomputes projections and executes exact control scripts in a private fixture. Scientific source decisions and complete owner acceptance remain separate.','input_pins':[{'path':str(p.relative_to(O)),'sha256':sha(p.read_bytes())} for p in [O/'dependency-selection.json',O/'machine-ledger.json',O/'author-plan-v2.json',O/'write-receipts-v2.json',O/'scripts/guarded_writer_v1.py',O/'scripts/guarded_writer_v2.py',O/'scripts/focused_controls_v2.py',O/'scripts/dependency_drift_controls_v2.py',O/'validation/focused-controls-v2.json',O/'validation/dependency-drift-controls-v2.json']], 'preserved_source_core':core,'payload_assessments':rows,'incoming_accounting':{'fresh_maintained_reference_count':len(incoming),'existing_exact_W05':16,'new_W03_dependency_sidecar':3,'combined37_existing':3,'distinct_owner_component_pairs':len(set(incoming))},'controls':{'independent_execution':'Original exact author script bytes executed using Python3.13; only guarded_writer_v2.O rebound to reviewer fixture. Native runtime/R and actual maintained inputs stayed read-only. Positive outputs are test artifacts, not selected candidates.','original_controls':28,'new_drift_controls':5,'no_assertions_removed':True,'replay_reports':[{'path':str(p.relative_to(O)),'sha256':sha(p.read_bytes())} for p in [R/'reproduce_controls_v1.py',R/'final-controls-fixture/validation/focused-controls-v2.json',R/'final-controls-fixture/validation/dependency-drift-controls-v2.json']],'native_target_schema':'3PASS','native_focused_partonomy':'3targetsPASS in2956recordcontext; source-wrong counterfactual alsoPASS, missinggenericparentrefused','broad_qc_or_native_full_shard_rerun':False},'finding_dispositions':[{'finding_id':'W03-PEPTONE-GUARD-001','status':'REPAIRED_IN_V2_INDEPENDENTLY_REPRODUCED','detail':'Fresh plan/disk primary/parent/core validation now precedes every write; all5serial drift controls refuse without output; old writer/probe/false successfulfixture preserved. No native campaign operator changed.'},{'finding_id':'W03-PEPTONE-DRAFT-UNIT-001','status':'CORRECTED_IN_ACTIVE_PLAN_AND_PAYLOAD','detail':'Marine component and new prose both preserveG_PER_SOURCE_SCRATCH_FORMULA_BATCH; old privateplan retained.'}], 'new_findings':[], 'intake_limits':['This is3genuine W03 authored dependent corrections, not3newW03 frozen source cases;188/74/868native core bytes stayexact.','W04 Marine and W06 PYGS original identities, current complete proposal objects and all4frozen case relationships retained; W03 authors only dependent delta. GYPS is real maintained owner with causalW05 parent reference, no fabricatedoriginalselectedcase.','If native worker-core intake is demanded, actual W04/W06 must adopt their successors and W05 must bind GYPS to its genuine causalcase/owner/backlink. Explicit coordinator composition can instead retain distinct original+W03dependency origins; it requires separate finalcandidate review.','GYPS MICRO0000178 is conditional on separateBacto identity acceptance; it never redirects togenericmesh. LiteralUNMAPPEDfallback requires a separatelyreviewed successor if finalBacto identity unavailable.','PYGS and Marine genericpart references require exactgenericparentc0837946 inactual application. Allsource/role/wholeowner/export holds remain.'], 'source_scope_preservations':['Marine17drysourcebatch rows; MgUNMAPPED;55.2520gversus55.1g conflict; nofinalvolume orproductmassfraction claim.','PYGS fullpapersnotclaimedinspected; allunknownquantity andmaterial-edgeholds retained.','GYPS originalspecies/preparation/context kept; noquantityprojection orcatalog/lotassignment.','FAB Oxoid and16W05dependents not rewritten; MarineBroth/PYrumen combined dependencies not overwritten.'],'approval':'Exact report-sidecar lineage and focused controls acceptable for publication/integration planning only. No finalhead, source scientific selfapproval, wholeowner,role,maintainedapplication or supportedexport approval.'}
with (R/'final-lineage-control-review.json').open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print('PASS',sha((R/'final-lineage-control-review.json').read_bytes()))
