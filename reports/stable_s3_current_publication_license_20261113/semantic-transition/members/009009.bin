from pathlib import Path
import copy,csv,datetime,hashlib,io,json,subprocess,sys,zipfile
import yaml
O=Path(__file__).resolve().parent;C=O.parents[1];R=C.parents[1];W=C/'workers/w03/worktree';A=W/'.temp/peptone-final-dependencies-v1';P='reports/all_unmatched_20261107/worker-03/successors/issue1176-dependencies-v1';D=W/P
H='784ee2541506c914b4c34f091de688d39784d548';B='fe31a02850932a7bdf2fe65c93cb636a86f82a2c'
sha=lambda b:hashlib.sha256(b).hexdigest();h=lambda p:sha(p.read_bytes());load=lambda p:json.loads(p.read_text());canon=lambda x:json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
def git(w,*args):return subprocess.check_output(['git','-C',str(w),*args])
def save(n,v):
 with (O/n).open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
pins={}
def pin(p):
 p=p.absolute();assert p.is_file() and not p.is_symlink();pins[str(p.relative_to(R))]=h(p);return p
def tree(rev):
 out={}
 for raw in git(W,'ls-tree','-rz',rev).split(b'\0'):
  if raw:
   hdr,path=raw.split(b'\t',1);out[path.decode()]=hdr.decode()
 return out
assert git(W,'rev-parse','HEAD').decode().strip()==H and git(W,'rev-parse',H+'^').decode().strip()==B
assert not git(W,'status','--porcelain');assert (O/'remote-head-retry.txt').read_text().split()[0]==H
beforetree=tree(B);aftertree=tree(H);assert all(aftertree.get(k)==v for k,v in beforetree.items())
added=set(aftertree)-set(beforetree);assert len(added)==200 and all(p.startswith(P+'/') for p in added)
for p in sorted(added):assert git(W,'show',H+':'+p)==pin(W/p).read_bytes()
man=load(D/'MANIFEST.json')
for x in man['members']:assert h(pin(D/x['path']))==x['sha256']
sel=load(D/'dependency-selection.json');plan=load(D/'author-plan-v2.json');assert h(D/'dependency-selection.json')=='b1e181a1dfbbc2d0588b377f00e5922c6b5340e86b171b9ebf8233d963f0ad92'
for key in ['active_writer','active_plan','active_native_write_receipts']:assert h(D/sel[key]['path'])==sel[key]['sha256']
assert sel['new_frozen_source_cases']==0 and sel['type']=='accountable_dependency_sidecar_not_frozen_source_core' and not sel['maintained_application_authorized']
cores=[]
for x in sel['preserved_W03_source_core']:
 p=pin(W/x['path']);assert p.read_bytes()==git(W,'show',B+':'+x['path']) and h(p)==x['sha256'];assert len(load(p)[x['object_key']])==x['entries'];cores.append(x)
assert [x['entries'] for x in cores]==[188,74,868]
for x in plan['primary_captures']+plan['selected_parent_inputs']:assert h(pin(D/x['path']))==x['sha256']
for x in load(D/'input-freeze.json')['prior_seals']:assert h(pin(W/x['path']))==x['sha256']
inventory=load(D/'lineage-review/verified-origin-inventory-v1.json');coremap={}
for x in inventory['core_inventory']:
 w=C/'workers'/f"w{x['worker']:02}"/'worktree';b=git(w,'show',x['head']+':'+x['proposal_core']['git_path']);assert sha(b)==x['proposal_core']['sha256'];coremap[x['worker']]=json.loads(b)['proposals']
proof=[];rows={};cases_seen=[];receipts=load(D/'write-receipts-v2.json')['rows']
sys.path.insert(0,str(W/'src'))
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
for prop,row in zip(sel['dependency_proposals'],plan['rows'],strict=True):
 assert prop['dependency_id']==row['dependency_id'] and not prop['native_source_core_member'] and prop['frozen_W03_case_ids']==[]
 before=pin(W/row['owner_path']).read_bytes();assert before==pin(D/row['maintained_before']['path']).read_bytes();assert sha(before)==prop['before_sha256']==row['maintained_before']['sha256']
 oldraw=pin(D/row['current_payload']['path']).read_bytes();assert sha(oldraw)==row['current_payload']['sha256']
 raw=pin(D/prop['payload']['path']).read_bytes();assert sha(raw)==prop['payload']['sha256']
 old=yaml.safe_load(oldraw);new=yaml.safe_load(raw);assert not validate_ingredient(new)
 assert old['components'][row['component_index']]==row['original_component'] and new['components'][row['component_index']]==row['new_component']
 normalized=copy.deepcopy(new);normalized['components'][row['component_index']]=old['components'][row['component_index']]
 assert new['curation_history'][:-1]==old['curation_history'];ev=new['curation_history'][-1];assert ev['changes']==row['event_text'] and ev['llm_assisted'] is True and ev['previous_status']==ev['new_status']==old['mapping_status']
 normalized['curation_history']=old['curation_history'];app=row['append_evidence'];assert new['component_assertion']['evidence'][-len(app):]==app
 normalized['component_assertion']['evidence']=new['component_assertion']['evidence'][:-len(app)];assert normalized==old
 assert all((x.get('concentration_value'),x.get('concentration_unit'))==(y.get('concentration_value'),y.get('concentration_unit')) for x,y in zip(old['components'],new['components'],strict=True))
 origin=row['predecessor_origin'];assert prop['preserved_foreign_source_origin']==origin
 if origin:
  peer=C/'workers'/f"w{origin['worker']:02}"/'worktree';assert git(peer,'show',origin['head']+':'+origin['git_path'])==oldraw
  original=[x for x in coremap[origin['worker']] if x['proposal_id']==origin['proposal']['proposal_id']];assert original==[origin['proposal']]
  assert sha(canon(origin))==row['predecessor_origin_object_sha256'] and sha(canon(original[0]))==origin['proposal_object_sha256']
  assert original[0]['owner_path']==row['owner_path'] and original[0]['before_sha256']==sha(before)
  decraw=git(peer,'show',origin['head']+':'+origin['current_decisions_git_path']);assert sha(decraw)==origin['current_decisions_sha256'];decisions=json.loads(decraw)['decisions']
  shardp=pin(Path(origin['frozen_shard_path']));assert h(shardp)==origin['frozen_shard_sha256'];shard=load(shardp);shard=shard['cases'] if isinstance(shard,dict) else shard
  for case in origin['cases']:
   matches=[x for x in shard if x['case_id']==case['case_id']];assert matches==[case['frozen_case']];assert sha(canon(matches[0]))==case['case_input_sha256']
   assert [x for x in decisions if x['case_id']==case['case_id']]==[case['current_decision']];assert sha(canon(case['current_decision']))==case['decision_object_sha256']
   cases_seen.append({'dependency_id':prop['dependency_id'],'original_worker':origin['worker'],'case_id':case['case_id'],'case_sha256':case['case_input_sha256'],'original_proposal_id':original[0]['proposal_id']})
 else:assert row['owner_path'].endswith('/GYPS.yaml') and oldraw==before and row['predecessor_origin_object_sha256'] is None
 causal=row['causal_parent'];parent=[x for x in coremap[5] if x['proposal_id']==causal['proposal_id']];assert len(parent)==1 and causal['case_id'] in parent[0]['case_ids'] and parent[0]['after_capture']['sha256']==causal['parent_payload_sha256']
 receipt=next(x for x in receipts if x['dependency_id']==row['dependency_id']);assert receipt['payload']==prop['payload'] and receipt['history_appended']==ev
 proof.append({'dependency_id':row['dependency_id'],'owner_path':row['owner_path'],'before_sha256':sha(before),'predecessor_payload_sha256':sha(oldraw),'after_sha256':sha(raw),'changed_component':row['component_index'],'history_append':1,'evidence_append':len(app),'all_unlisted_fields_and_quantities_exact':True,'actual_original_cases':origin['proposal']['case_ids'] if origin else [],'causal_parent':causal,'native_core_member':False});rows[row['owner_path']]=new
assert len(cases_seen)==4 and len({x['case_id'] for x in cases_seen})==4
catalog={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for folder in ['mapped','unmapped'] for p in (W/'data/ingredients'/folder).glob('*.yaml')};assert len(catalog)==2956
incoming=[(p,i) for p,r in catalog.items() for i,c in enumerate(r.get('components',[])) if c.get('component_id')=='MICRO:0000178' and c.get('reference_scope')=='MIM_CATALOG'];ledger=load(D/'machine-ledger.json');assert sorted(incoming)==sorted((x['owner_path'],x['component_index']) for x in ledger['rows']) and len(incoming)==19
assert sum(bool(x['existing_W05_proposal']) for x in ledger['rows'])==16 and sum(bool(x['new_W03_dependency_id']) for x in ledger['rows'])==3
for name in ['Peptone','Bacto_Peptone']:
 target=pin(D/'inputs/targets'/f'{name}.yaml');r=yaml.safe_load(target.read_text());catalog[f'data/ingredients/mapped/{name}.yaml']=r
 parentprop=[x for x in coremap[5] if x['owner_path']==f'data/ingredients/mapped/{name}.yaml'];assert len(parentprop)==1 and parentprop[0]['after_capture']['sha256']==h(target)
 pp=parentprop[0]['after_capture']['path'];assert git(C/'workers/w05/worktree','show','108e213e96f7d423ee345ce265d692e79063127c:reports/all_unmatched_20261107/worker-05/'+pp)==target.read_bytes()
catalog.update(rows);errors=[str(x) for x in validate_component_partonomy(catalog.values())];assert not errors
with zipfile.ZipFile(D/'inputs/primary/microbedecoder_database.zip') as z:raw=z.read('database.csv');db=list(csv.DictReader(io.StringIO(raw.decode('latin1'))))
observations=[]
for n,label,species in [(3351,'GYPS','sporogenes'),(4105,'PYGS','frigidicarnis'),(4110,'PYGS','gasigenes'),(8884,'PYGS','algidixylanolytica')]:
 r=db[n-2];assert r['Bergey_Substrates_for_end_products']==label and r['Species']==species;observations.append({'csv_line':n,'literal':label,'species':species,'source_link':r['Bergey_Article_link']})
oldnative=yaml.safe_load((D/'skeptical-review/native/review.yaml').read_text())
for x in oldnative['source']['inputs']:assert h(pin(W/x['path']))==x['sha256']
for t in oldnative['targets']:assert h(pin(W/t['path']))==t['sha256']
assert git(W,'rev-parse','HEAD').decode().strip()==H and not git(W,'status','--porcelain')
for p,digest in pins.items():assert h(R/p)==digest,p
save('committed-head-audit.json',{'at':datetime.datetime.now(datetime.UTC).isoformat(),'head':H,'parent':B,'remote_head_verified':H,'prior_tree_entries_unchanged':len(beforetree),'added_report_paths':len(added),'manifest_members':len(man['members']),'maintained_code_data_tests_workflows_unchanged':True,'source_core':cores,'new_assigned_cases':0,'dependency_payloads':proof,'source_case_binding_count':len(cases_seen),'case_bindings':cases_seen,'baseline_incoming_references':len(incoming),'other_W05_bound':16,'native_schema_count':3,'full_context_partonomy_records':len(catalog),'partonomy_errors':errors,'primary_raw_contexts':observations,'prior_native_inputs_verified':len(oldnative['source']['inputs']),'prior_review_is_historical_working_tree_not_new_head':True,'full_native_campaign_prepare':False,'integration_limit':sel['structural_contract'],'actual_worker_source_untouched':True})
save('input-pins.json',pins)
print('PASS exact committed head;200 report-only additions;188/74/868 unchanged;3 whole payloads,4 original cases and genuine causal parent;19-reference accounting;native schema/partonomy.')
