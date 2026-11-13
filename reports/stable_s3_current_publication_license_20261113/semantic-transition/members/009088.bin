"""Bounded representation checks for this one report; not a new native gate.
Native operator proves exact artifacts/cases, not causal meaning. This complements
that structural proof without modifying native code or source membership.
"""
import pathlib,json,hashlib,subprocess,copy
R=next(p for p in pathlib.Path(__file__).resolve().parents if (p/'MAPPING_SEMANTICS.md').is_file());O=pathlib.Path(__file__).resolve().parents[1]
CID='KG_CASE:ba039f9e4a33baf69eb111ceb979cf6c9ad8fe788c13488f256336508ce94151';CASE_SHA='d42806e437d2e4c72f3e148314c5ef72e8c21f08c78b7b70eebe3d32c83b67d6';BEFORE='36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e';AFTER='fa98f361a39dcaf0bea1f4046829287581bc45e2813044696e5070de58708aa1'
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
def need(ok,msg):
 if not ok:raise ValueError(msg)
def verify(ledger, root=O):
 need(isinstance(ledger,dict) and len(ledger.get('proposals',[]))==1,'exactly one additive GYPS proposal required')
 p=ledger['proposals'][0];need(p['proposal_id']=='W03-DEP-1176-GYPS' and p['kind']=='edit_existing_owner','real dependency identity/kind')
 need(p['owner_path']=='data/ingredients/mapped/GYPS.yaml' and p['before_sha256']==BEFORE,'real maintained preimage required')
 need(sha((root/'inputs/before/GYPS.yaml').read_bytes())==BEFORE and sha((R/p['owner_path']).read_bytes())==BEFORE,'beforeimage bytes drift')
 need(p['after_capture']=={'root':'artifact','path':'payloads/GYPS.yaml','sha256':AFTER},'wrong payload reference')
 need(sha((root/'payloads/GYPS.yaml').read_bytes())==AFTER,'wrong payload bytes')
 need(p['case_ids']==[CID],'wrong causal case set')
 need(p['native_source_core_member'] is False,'foreign case falsely claimed native W03 core')
 for key in ['assigned_W03_case_ids','observed_GYPS_case_ids','added_source_case_ids','added_occurrence_ids']:need(p[key]==[],'false source/observation/occurrence membership: '+key)
 for key in ['new_assigned_source_cases','new_observed_recipe_cases','new_occurrences']:need(ledger[key]==0,'false new source count')
 rel=p['case_relationships'];need(len(rel)==1,'causal relation cardinality')
 rel=rel[0];need(rel['case_id']==CID and rel['case_input_sha256']==CASE_SHA,'wrong causal case hash')
 need(rel['relationship']=='causal_parent_identity_transition_only' and rel['assigned_worker_slot']=='worker-05','foreign assignment changed')
 need(all(rel[k] is False for k in ['is_assigned_W03_case','is_GYPS_recipe_observation','adds_occurrence']),'false assignment/observation assertion')
 global_cases=json.loads((root/'inputs/frozen/union-ledger.json').read_text());hits=[x for x in global_cases if x['case_id']==CID];need(len(hits)==1 and sha(canon(hits[0]))==CASE_SHA,'full frozen global case mismatch')
 for n,expected in [('03',False),('05',True)]:
  shard=json.loads((root/f'inputs/frozen/shard-{n}.json').read_text());need(any(x['case_id']==CID for x in shard['cases']) is expected,'actual frozen assignment mismatch')
 foreign=p['causal_parent_provenance'];proof=json.loads((root/'lineage-review/lineage-proof-v1.json').read_text())['foreign_causal_origin'];original=json.loads((root/'lineage-review/original-W05-parent-proposal.json').read_text());decision=json.loads((root/'lineage-review/original-W05-parent-decision.json').read_text())
 need(foreign['complete_original_proposal']==original and foreign['proposal_object_sha256']==sha(canon(original)),'foreign complete proposal changed')
 need(foreign['original_authors']=={k:original[k] for k in ['primary_author','parent_successor_author','direct_term_successor_author']},'foreign author changed')
 need(foreign['original_proposal_backlinks']==decision['proposal_ids'] and original['proposal_id'] in decision['proposal_ids'],'foreign backlink changed')
 need(foreign['new_GYPS_backlink_in_foreign_decision_claimed'] is False,'invented foreign backlink')
 need(foreign['source_decision_object_sha256']==sha(canon(decision))==proof['decision_object_sha256'],'foreign decision hash changed')
 need(foreign['case_id']==CID and foreign['case_input_sha256']==CASE_SHA,'foreign case binding drift')
 need(foreign['original_published_head']==proof['original_published_head']=='108e213e96f7d423ee345ce265d692e79063127c','foreign original head changed')
 need(foreign['current_unchanged_head_bridge']==proof['unchanged_head_bridge'],'head bridge changed')
 work=R.parents[2]/'workers/w05/worktree'
 for b in foreign['current_unchanged_head_bridge'].values():
  old=subprocess.check_output(['git','-C',str(work),'show',b['old_head']+':'+b['published_path']]);current=subprocess.check_output(['git','-C',str(work),'show',b['observed_current_local_head']+':'+b['published_path']]);need(old==current and sha(old)==b['old_sha256']==b['current_sha256'],'actual foreign Git bridge mismatch')
 need(p['scientific_payload_changes'] is False and p['history_changes'] is False and p['source_scope_additions']==0,'false scientific successor')
 need(p['application_authorized'] is False and p['whole_owner_role_export_approved'] is False,'approval inflation')
 need('conditionally' in p['conditional_Bacto_requirement'] and 'UNMAPPED' in p['conditional_Bacto_requirement'],'Bacto condition lost')
 for b in ledger['source_core_preservation']:
  need(sha((R/b['path']).read_bytes())==b['sha256'],'original W03 core changed')
 return {'status':'PASS_BOUNDED_REPRESENTATION','proposals':1,'global_ledger_cases':len(global_cases),'W03_assignment':False,'W05_assignment':True,'new_observations':0,'new_occurrences':0,'exact_scientific_payload':AFTER,'native_operator_semantic_enforcement_claimed':False}
if __name__=='__main__':
 ledger=json.loads((O/'proposals.json').read_text());positive=verify(ledger);checks=[]
 muts={'wrong_causal_hash':lambda p:p['case_relationships'][0].update(case_input_sha256='0'*64),'wrong_before':lambda p:p.update(before_sha256='0'*64),'wrong_payload':lambda p:p['after_capture'].update(sha256='0'*64),'false_assigned_W03':lambda p:p.update(assigned_W03_case_ids=[CID]),'false_native_core':lambda p:p.update(native_source_core_member=True),'false_GYPS_observation':lambda p:p.update(observed_GYPS_case_ids=[CID]),'false_occurrence':lambda p:p.update(added_occurrence_ids=['invented']),'false_assigned_flag':lambda p:p['case_relationships'][0].update(is_assigned_W03_case=True),'false_backlink':lambda p:p['causal_parent_provenance'].update(new_GYPS_backlink_in_foreign_decision_claimed=True),'foreign_author_changed':lambda p:p['causal_parent_provenance']['original_authors'].update(primary_author='W03'),'second_origin_duplication':None}
 for name,mut in muts.items():
  bad=copy.deepcopy(ledger)
  if mut:mut(bad['proposals'][0])
  else:bad['proposals'].append(copy.deepcopy(bad['proposals'][0]))
  try:verify(bad)
  except ValueError as e:checks.append({'control':name,'result':'PRIVATE_REPRESENTATION_CHECK_REFUSED','message':str(e),'native_refusal_claimed':False})
  else:raise AssertionError('failed negative '+name)
 report={'positive':positive,'negative_controls':checks,'negative_count':len(checks),'payload_or_ledger_writes':False,'scope':'Checks inspect actual global/shard membership and original Git bridge. Separate actualnativeprepare controls are in technical-review. This is not an operator or gate change.'}
 out=O/'validation/representation-controls-v1.json';need(not out.exists(),'immutable report exists');out.write_text(json.dumps(report,indent=2)+'\n');print('PASS private scopecontrols',len(checks))
