"""Counterfactual boundary probe: native identity binding is not shard/claim review."""
import copy,datetime,json,pathlib,shutil
from run_native_fixture_v2 import T,R,C,I,native,crosswalk,sha,canon,ref,put,git
F=T/'false-assignment-fixture-v1';assert not F.exists();shutil.copytree(T/'fixture-v2',F)
ledger=json.loads((F/'intake/proposals.json').read_bytes());original=copy.deepcopy(ledger);proposal=ledger['proposals'][0];cid=proposal['case_ids'][0]
assert proposal['assigned_W03_case_ids']==[] and proposal['case_relationships'][0]['is_assigned_W03_case'] is False
proposal['assigned_W03_case_ids']=[cid];proposal['case_relationships'][0]['is_assigned_W03_case']=True;proposal['case_relationships'][0]['assigned_worker_slot']='worker-03'
put(F,'intake/proposals.json',ledger);git(F,'add','intake/proposals.json');git(F,'-c','user.name=Native fixture','-c','user.email=fixture@example.invalid','commit','-qm','Counterfactual false assignment; private negative only')
head=git(F,'rev-parse','HEAD');plan=json.loads((F/'positive/plan.json').read_bytes());plan['baseline_commit']=head;plan['intake_heads']={'worker-03':head}
for b in plan['bindings']:
 if b['published_head'] is not None:b['published_head']=head
 if b['binding_id']=='new-proposal':b['sha256']=sha((F/b['path']).read_bytes())
plan['records'][0]['origins'][0]['head_sha']=head
p=put(F,'false-assignment/plan.json',plan);acceptance=json.loads((F/'positive/acceptance.json').read_bytes());acceptance['plan_sha256']=sha(p.read_bytes());acceptance['baseline_commit']=head;acceptance['intake_heads']=plan['intake_heads'];acceptance['binding_sha256']={b['binding_id']:b['sha256'] for b in plan['bindings']};a=put(F,'false-assignment/acceptance.json',acceptance)
prepared=native.prepare(F,p,a)
oid='w03::'+proposal['proposal_id'];payload_path=next(b['path'] for b in plan['bindings'] if b['binding_id']=='original-payload')
row={'origin_id':oid,'worker_slot':3,'published_head':head,'proposal':proposal,'proposal_object_sha256':sha(canon(proposal)),'payload_sha256':proposal['after_capture']['sha256'],'case_hashes':plan['records'][0]['origins'][0]['case_hashes']}
binding={'origin_id':oid,'proposal_ledger':{**ref(F,'intake/proposals.json'),'published_path':'intake/proposals.json'},'payload':{**ref(F,payload_path),'published_path':payload_path}}
resolution={'origin_id':oid,'status':'apply','evidence_refs':[ref(F,'intake/route.json')],'operation_id':'FIXTURE-GYPS-NATIVE','payload_sha256':proposal['after_capture']['sha256'],'independent_review_refs':[ref(F,'intake/independent-review.json')]}
proof=crosswalk.validate_resolution_crosswalk([row],[resolution],root=F,origin_bindings=[binding],native_plan={'plan':ref(F,str(p.relative_to(F))),'acceptance':ref(F,str(a.relative_to(F)))})
# Independent semantic check uses actual frozen memberships; no newnativegate/rule.
shard3=json.loads((C/'queue/preliminary-v5/shards/shard-03.json').read_bytes());shard5=json.loads((C/'queue/preliminary-v5/shards/shard-05.json').read_bytes())
def cases(d):return d['cases'] if isinstance(d,dict) else d
members3={c['case_id'] for c in cases(shard3)};members5={c['case_id'] for c in cases(shard5)};assert cid not in members3 and cid in members5
rejected=not (proposal['assigned_W03_case_ids']==[] and proposal['case_relationships'][0]['is_assigned_W03_case'] is False and proposal['case_relationships'][0]['assigned_worker_slot']=='worker-05');assert rejected
assert sha((F/proposal['owner_path']).read_bytes())==proposal['before_sha256'];assert not git(F,'diff','--name-only','HEAD','--')
summary={'reviewer':'/root/gyps_native_technical','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'EXPECTED_NATIVE_BOUNDARY_AND_SEMANTIC_REFUSAL','actual_root_ledger_sha256':sha((R/'.temp/gyps-native-origin-v1/proposals.json').read_bytes()),'counterfactual_ledger_sha256':sha((F/'intake/proposals.json').read_bytes()),'counterfactual_changes':{'assigned_W03_case_ids':proposal['assigned_W03_case_ids'],'case_relationships[0].assigned_worker_slot':'worker-03','case_relationships[0].is_assigned_W03_case':True},'fixture_git_head':head,'fixture_only':True,'native_prepare_result':'PASS','crosswalk_result':proof,'independent_semantic_lineage_check':'REFUSED_FALSE_ASSIGNED_W03_CLAIM','actual_frozen_membership':{'W03':False,'W05':True,'case_id':cid},'owner_bytes_unchanged':True,'apply_called':False,'full_campaign_prepared':False,'interpretation':'Native operator and crosswalk bind exact originals and globalcasehashes but do not promise semantic assigned-worker truth. This is an expected scope boundary, not a new gate defect. Actualledger correctforeigncausal scope remains required and unchanged.'}
put(T,'false-assignment-boundary-v1.json',summary);print(json.dumps({k:summary[k] for k in ['status','native_prepare_result','independent_semantic_lineage_check','fixture_git_head','owner_bytes_unchanged']},indent=2))
