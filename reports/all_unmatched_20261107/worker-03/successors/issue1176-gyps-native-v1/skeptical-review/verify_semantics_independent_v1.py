from pathlib import Path
import json, hashlib, subprocess, copy, datetime as dt
R=Path.cwd(); B=R/'.temp/gyps-native-origin-v1'; S=B/'skeptical-review'; C=R.parents[2]
sha=lambda b:hashlib.sha256(b).hexdigest()
canon=lambda o:sha(json.dumps(o,sort_keys=True,separators=(',',':')).encode())
def get(p):return json.loads(p.read_bytes())
def git(w,h,p):return subprocess.check_output(['git','-C',str(w),'show',h+':'+p])
def put(p,o):
 assert not p.exists(),p
 p.write_text(json.dumps(o,indent=2)+'\n')
base='784ee2541506c914b4c34f091de688d39784d548'; W05=C/'workers/w05/worktree'
L=get(B/'proposals.json'); P=L['proposals'][0]; O=get(B/'origin-binding-context.json')
assert sha((B/'proposals.json').read_bytes())=='582ea36dd479b8ecd244d996a6eb772569eb232b1631f87ef5f4aa143a20ce67'
assert canon(P)=='66bb10da3a73e57a473ad1cb9ba0c852ca1aef7fc41c888cc2b012a8a32661cf'
caseid=P['case_ids'][0]; cases=get(B/'inputs/frozen/union-ledger.json'); matches=[c for c in cases if c['case_id']==caseid]
assert len(cases)==1879 and len(matches)==1
case=matches[0]; ch=canon(case)
assert ch=='d42806e437d2e4c72f3e148314c5ef72e8c21f08c78b7b70eebe3d32c83b67d6'
assert case['source_case_id']=='kgmicrobe.compound:peptones' and case['source_label']=='peptones' and not case['source_identity_claimed']
shards={x:get(B/f'inputs/frozen/shard-{x}.json') for x in ['03','05']}
assert caseid not in [c['case_id'] for c in shards['03']['cases']]
assert [c for c in shards['05']['cases'] if c['case_id']==caseid]==matches
F=P['causal_parent_provenance']; bridge=[]
for k,v in F['current_unchanged_head_bridge'].items():
 a=git(W05,v['old_head'],v['published_path']);b=git(W05,v['observed_current_local_head'],v['published_path'])
 assert a==b and sha(a)==v['old_sha256']==v['current_sha256']
 bridge.append({'kind':k,'path':v['published_path'],'old_head':v['old_head'],'observed_head':v['observed_current_local_head'],'sha256':sha(a),'exact':True})
originalP=json.loads(git(W05,F['original_published_head'],bridge[0]['path']))['proposals']
originalP=next(p for p in originalP if p['proposal_id']==F['proposal_id'])
originalD=json.loads(git(W05,F['original_published_head'],bridge[1]['path']))['decisions']
originalD=next(d for d in originalD if d['case_id']==caseid)
assert originalP==F['complete_original_proposal'] and canon(originalP)==F['proposal_object_sha256']
assert canon(originalD)==F['source_decision_object_sha256']
assert originalD['proposal_ids']==F['original_proposal_backlinks'] and P['proposal_id'] not in originalD['proposal_ids']
oldrel=P['predecessor_sidecar']['published_path'];oldbytes=git(R,base,oldrel);old=get(B/'inputs/prior-sidecar/dependency-selection.json')
assert oldbytes==(B/'inputs/prior-sidecar/dependency-selection.json').read_bytes() and sha(oldbytes)==P['predecessor_sidecar']['ledger_sha256']
oldP=next(x for x in old['dependency_proposals'] if x['dependency_id']==P['proposal_id'])
assert canon(oldP)==P['predecessor_sidecar']['complete_dependency_object_sha256']
oldroot=str(Path(oldrel).parent);payload=(B/P['after_capture']['path']).read_bytes();oldpayload=git(R,base,oldroot+'/'+oldP['payload']['path'])
assert payload==oldpayload and sha(payload)==P['after_capture']['sha256']=='fa98f361a39dcaf0bea1f4046829287581bc45e2813044696e5070de58708aa1'
before=(R/P['owner_path']).read_bytes()
assert before==(B/'inputs/before/GYPS.yaml').read_bytes()==git(R,base,P['owner_path']) and sha(before)==P['before_sha256']
assert P['source_and_application_holds']==oldP['application_conditions'] if 'application_conditions' in oldP else P['source_and_application_holds']==oldP['source_and_application_holds']
cores=[]
for v in L['source_core_preservation']:
 p=R/v['path'];bb=p.read_bytes();gg=git(R,base,v['path']);data=json.loads(bb);key=Path(v['path']).stem
 assert bb==gg and sha(bb)==v['sha256'] and len(data[key])==v['count']
 cores.append({**v,'git_and_current_byte_identical':True})
evidence=[]
for e in get(B/'evidence.json')['evidence']:
 cap=B/e['capture']['path'];assert sha(cap.read_bytes())==e['capture']['sha256']
 evidence.append({'evidence_id':e['evidence_id'],'path':e['capture']['path'],'sha256':sha(cap.read_bytes()),'interpretation':'selector is record content, not an independent reviewer verdict' if e['evidence_id']=='GYPS-REVIEWED-SIDECAR' else e['applicability']})
# Exact whole-payload identity preserves every source/assertion, component, quantity, role, event and hold.
# This checker independently validates scope against committed objects rather than approving chemistry.
def check(l,o):
 def require(cond,msg):
  if not cond:raise ValueError(msg)
 require(len(l['proposals'])==1,'one GYPS origin only')
 p=l['proposals'][0]; f=p['causal_parent_provenance']; rel=p['case_relationships']
 require(p['proposal_id']=='W03-DEP-1176-GYPS' and p['kind']=='edit_existing_owner','authentic existing-owner proposal required')
 require(p['owner_path']=='data/ingredients/mapped/GYPS.yaml' and p['before_sha256']==sha(before),'real GYPS preimage required')
 require(p['after_capture']==P['after_capture'],'exact unchanged reviewed payload binding required')
 require(p['case_ids']==[caseid] and len(rel)==1 and rel[0]['case_id']==caseid and rel[0]['case_input_sha256']==ch,'actual causal case/hash required')
 require(not p['native_source_core_member'],'new dependency is outside original source core')
 for k in ['assigned_W03_case_ids','observed_GYPS_case_ids','added_source_case_ids','added_occurrence_ids']:
  require(p[k]==[],f'false assignment/observation/occurrence claim: {k}')
 require(rel[0]['assigned_worker_slot']=='worker-05' and rel[0]['is_assigned_W03_case'] is False,'actual foreign W05 assignment required')
 require(rel[0]['relationship']=='causal_parent_identity_transition_only' and rel[0]['is_GYPS_recipe_observation'] is False and rel[0]['adds_occurrence'] is False,'causal context is not a GYPS observation')
 require(f['complete_original_proposal']==originalP and f['proposal_object_sha256']==canon(originalP),'complete foreign proposal changed')
 require(f['original_authors']=={k:originalP[k] for k in ['primary_author','parent_successor_author','direct_term_successor_author']},'foreign authors must remain original')
 require(f['original_published_head']=='108e213e96f7d423ee345ce265d692e79063127c' and f['case_input_sha256']==ch,'foreign original head/case changed')
 require(f['original_proposal_backlinks']==originalD['proposal_ids'] and not f['new_GYPS_backlink_in_foreign_decision_claimed'],'foreign decision cannot claim new GYPS backlink')
 require(p['predecessor_sidecar']==P['predecessor_sidecar'],'published predecessor/relationship differs')
 require(p['scientific_payload_changes'] is False and p['history_changes'] is False and p['source_scope_additions']==0,'representation cannot imply new science/history/source scope')
 require(p['source_and_application_holds']==P['source_and_application_holds'] and p['conditional_Bacto_requirement']==P['conditional_Bacto_requirement'],'conditional Bacto/fallback constraints changed')
 require(not p['application_authorized'] and not p['whole_owner_role_export_approved'],'no application or whole-owner approval')
 require(l['source_core_preservation']==cores0,'old core objects/counts must be retained')
 for k in ['new_assigned_source_cases','new_observed_recipe_cases','new_occurrences']:require(l[k]==0,f'false count increase: {k}')
 require(o['publication_binding_pending_actual_commit'] is True and o['no_retirement'] is True and o['all_case_ids_causal_only'] is True,'no invented publication/retirement/observed case')
 require(o['case_hashes']=={caseid:ch},'binding case hash differs')
 return True
cores0=copy.deepcopy(L['source_core_preservation']);check(L,O)
controls=[]
def trial(name,fn):
 l=copy.deepcopy(L);o=copy.deepcopy(O);fn(l,o)
 try:check(l,o)
 except ValueError as e:controls.append({'control':name,'status':'REFUSED','reason':str(e),'mutated_ledger_sha256':canon(l),'mutated_binding_sha256':canon(o),'actual_source_writes':0})
 else:raise AssertionError('unexpected acceptance: '+name)
def prop(k,val):return lambda l,o:l['proposals'][0].__setitem__(k,val)
def relation(k,val):return lambda l,o:l['proposals'][0]['case_relationships'][0].__setitem__(k,val)
def foreign(k,val):return lambda l,o:l['proposals'][0]['causal_parent_provenance'].__setitem__(k,val)
trial('wrong_causal_case_hash',relation('case_input_sha256','0'*64))
trial('wrong_maintained_preimage',prop('before_sha256','0'*64))
trial('wrong_payload_hash',prop('after_capture',{**P['after_capture'],'sha256':'0'*64}))
trial('foreign_case_claimed_W03_assigned_array',prop('assigned_W03_case_ids',[caseid]))
trial('foreign_case_claimed_W03_assigned_flag',relation('is_assigned_W03_case',True))
trial('foreign_case_relabelled_worker03',relation('assigned_worker_slot','worker-03'))
trial('causal_case_claimed_GYPS_observation_array',prop('observed_GYPS_case_ids',[caseid]))
trial('causal_case_claimed_GYPS_observation_flag',relation('is_GYPS_recipe_observation',True))
trial('invented_frozen_case',prop('added_source_case_ids',['GYPS invented frozen case']))
trial('invented_occurrence',prop('added_occurrence_ids',['GYPS invented occurrence']))
trial('invented_source_core_membership',prop('native_source_core_member',True))
trial('foreign_authorship_claimed_W03',foreign('original_authors',{**F['original_authors'],'primary_author':'codex-worker03 /root'}))
trial('fabricated_foreign_GYPS_backlink',foreign('original_proposal_backlinks',originalD['proposal_ids']+[P['proposal_id']]))
trial('false_GYPS_backlink_flag',foreign('new_GYPS_backlink_in_foreign_decision_claimed',True))
trial('conditional_Bacto_requirement_removed',prop('conditional_Bacto_requirement','approved generic peptone'))
trial('source_application_holds_removed',prop('source_and_application_holds',[]))
trial('duplicate_Marine_origin',lambda l,o:l['proposals'].append({**P,'proposal_id':'invented-Marine','owner_path':'data/ingredients/mapped/Marine_agar_2216.yaml'}))
trial('false_retirement',lambda l,o:o.__setitem__('no_retirement',False))
trial('future_head_claimed_published',lambda l,o:o.__setitem__('publication_binding_pending_actual_commit',False))
trial('occurrence_count_inflation',lambda l,o:l.__setitem__('new_occurrences',1))
trial('whole_owner_approval_leak',prop('whole_owner_role_export_approved',True))
trial('new_history_claim',prop('history_changes',True))
result={'reviewer':'/root/gyps_native_skeptic','at':dt.datetime.now(dt.timezone.utc).isoformat(),'status':'PASS_EXACT_REPRESENTATION_WITH_LIMITS','ledger_sha256':sha((B/'proposals.json').read_bytes()),'proposal_object_sha256':canon(P),'payload_sha256':sha(payload),'before_sha256':sha(before),'old_sidecar_full_object_sha256':canon(oldP),'foreign_original_full_proposal_sha256':canon(originalP),'foreign_original_source_decision_sha256':canon(originalD),'global_case_count':len(cases),'real_case_id':caseid,'real_case_sha256':ch,'case_source':case['source'],'case_label':case['source_label'],'W05_assigned':True,'W03_assigned':False,'foreign_original_to_observed_bridge':bridge,'original_188_74_868_cores':cores,'evidence_captures':evidence,'complete_payload_bytes_equal_prior_published':True,'new_payload_or_case_or_occurrence_counts':{'native_dependency_proposals':1,'new_scientific_payloads':0,'added_frozen_cases':0,'added_observations':0,'added_occurrences':0},'source_science_authority':'No new science approval. Complete unchanged payload preserves prior conditional Bacto, PARTIAL recipe and source limits. Foreign generic parent is causal context only.','native_semantic_boundary':'Native operator verifies real global case binding but does not reject false W03-assignment/observation fields. This independent semantic checker is private and is not represented as native gate enforcement.','negative_controls':controls,'negative_count':len(controls),'new_confirmed_findings':[],'publication_pending':True,'whole_owner_role_export_approval':False,'full_campaign_prepared':False}
put(S/'independent-semantics-controls-v1.json',result)
print(json.dumps({k:result[k] for k in ['status','ledger_sha256','proposal_object_sha256','global_case_count','negative_count','new_confirmed_findings']},indent=2))
