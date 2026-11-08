"""Bind exact qualified five-payload reviews and complete predecessor/c9 bridges."""
from pathlib import Path
import copy,datetime,hashlib,json
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v6';B=A/'successor-v5';C=S/'author-core';F=S/'final-core';BASE='3e190a0f6c5a978ca8ed7e3bc7b6a2d66935548b'
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest();at=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def bind(p):return {'path':str(p.relative_to(A)),'sha256':sha(p)}
science=S/'reviews/skeptic/scientific-review-v1.json';retention=S/'reviews/retention/author-core-retention-review-v1.json';sr=load(science);rr=load(retention)
assert sr['status']=='PASS_BOUNDED_CORRECTION' and sr['author_independent'] and not sr['new_unexpected_findings'];assert rr['verdict']=='pass_with_limitations' and not rr.get('findings',[])
D=load(C/'decisions.json');P=load(C/'proposals.json');E=load(C/'evidence.json');oldD=load(B/'final-core/decisions.json')['decisions'];oldP=load(B/'final-core/proposals.json')['proposals'];oldE=load(B/'final-core/evidence.json')['evidence'];proof=load(S/'payload-change-proof.json')['rows'];pids={x['proposal_id'] for x in proof};indices={i for x in proof for i in x['case_indices']};caseids=sorted({c for x in proof for c in x['case_ids']})
specs=[('sv6-independent-assertions',science,'independent_review','Fresh exact source-relative method/closure review of all five changed payloads only; prior identity/source/role/export judgments not renewed.'),('sv6-independent-retention',retention,'independent_review','Complete selected cohort and original history/source retention, with original HCl authorship disclosed; metadata only.'),('sv6-native-narrow-validation',S/'validation/narrow-native.json','local_validation','Five closed-schema guarded byte roundtrips, full overlay partonomy and unchanged identity/alias/component projections.')]
for eid,path,kind,summary in specs:E['evidence'].append({'evidence_id':eid,'kind':kind,'capture':{'root':'artifact',**bind(path)},'url':None,'accessed_at':at,'locator':'Complete exact artifact; local reading, not fresh primary retrieval','supports_or_contradicts':summary,'case_ids':caseids})
ids=[x[0] for x in specs]
for obj in [p for p in P['proposals'] if p['proposal_id'] in pids]+[D['decisions'][i] for i in sorted(indices)]:
 obj['independent_review']={'status':'complete','evidence_ids':ids[:2]};obj['evidence_ids']+=ids;obj['component_assertion_successor']['review_state']='complete_for_exact_qualified_source_assertion_correction';obj['component_assertion_successor']['independent_review_bindings']=[bind(science),bind(retention)]
for p in P['proposals']:
 if p['proposal_id'] in pids:p['review_status_explanation']='Exact source-relative component assertion correction and retained whole payload independently reviewed. The original W09 findings retain their qualified split: four HCl UNKNOWN, Difco COMPLETE only for nominal 2009 seven immediate ingredient names under CURATED_INTERPRETATION. Historical identity/source/role/export judgments and prior carbonate/calf scopes are not blanket-transferred.'
assert E['evidence'][:len(oldE)]==oldE
F.mkdir()
for n,d in [('decisions.json',D),('proposals.json',P),('evidence.json',E)]:save(F/n,d)
def bridge(priorD,priorP,allowedcases,allowedpids):
 cases=[];props=[];assert len(priorD)==len(D['decisions'])
 for i,(old,new) in enumerate(zip(priorD,D['decisions'])):
  for k in ['case_id','case_input_sha256','source','occurrence_ids','disposition','applicability','missing_requirement','proposal_ids','owner_records']:assert old.get(k)==new.get(k),(i,k)
  assert i in allowedcases or old==new
  cases.append({'source_index':i,'case_id':new['case_id'],'before_object_sha256':canon(old),'after_object_sha256':canon(new),'complete_object_exact':old==new,'source_identity_occurrence_owner_hashes_exact':True,'reasoning_exact':old['reasoning']==new['reasoning'],'occurrence_ids':new['occurrence_ids'],'proposal_ids':new['proposal_ids']})
 oldby={p['proposal_id']:p for p in priorP};assert set(oldby)=={p['proposal_id'] for p in P['proposals']}
 for new in P['proposals']:
  old=oldby[new['proposal_id']]
  for k in ['case_ids','owner_path','before_sha256','kind']:assert old[k]==new[k]
  assert new['proposal_id'] in allowedpids or new==old
  assert sha(A/new['after_capture']['path'])==new['after_capture']['sha256']
  props.append({'proposal_id':new['proposal_id'],'before_proposal_sha256':canon(old),'after_proposal_sha256':canon(new),'proposal_object_exact':new==old,'old_capture':old['after_capture'],'selected_capture':new['after_capture'],'payload_byte_exact':old['after_capture']==new['after_capture'],'owner_path':new['owner_path'],'before_owner_sha256':new['before_sha256'],'case_ids':new['case_ids'],'whole_owner_approval':False})
 return {'all_cases':cases,'all_proposals':props,'scope':'Exact bounded correction/retention bridge only; no blanket science, owner, role or export approval.'}
current=bridge(oldD,oldP,indices,pids);current.update({'at':at,'predecessor_head':BASE,'previous_complete_bridge':bind(B/'complete-bridge.json'),'earlier_retirement_bridge':bind(A/'successor-v3/retirement-bridge.json'),'current_proposals_retired':[]});save(S/'complete-bridge.json',current)
priorids={'sv1-buffers-carbonate_co2_nominal4percent_togo_m202','sv1-bio-calf_blood_togo_m2854'}
joint=bridge(load(A/'successor-v3/decisions.json')['decisions'],load(A/'successor-v3/proposals.json')['proposals'],indices|{21,44,187},pids|priorids)
joint.update({'at':at,'baseline_head':'c9a96da71a1977014680e5a92e600dfc7e3874db','predecessor_head':BASE,'prior_bounded_corrections_preserved':{'carbonate':bind(A/'successor-v4/HANDOFF-v2.json'),'calf':bind(B/'HANDOFF.json'),'previous_cumulative_bridge':bind(B/'combined-c9-bridge.json')},'new_bounded_corrections':[{'proposal_id':x['proposal_id'],'selected_capture':x['after'],'scope':x['conclusion'],'finding_ids':x['finding_ids']} for x in proof],'no_blanket_w09_or_c9_approval_transfer':True});save(S/'combined-c9-bridge.json',joint)
occ=[x for d in D['decisions'] for x in d['occurrence_ids']];assert len(occ)==len(set(occ))==304 and len(D['decisions'])==188 and len(P['proposals'])==127
counts={'cases':len(D['decisions']),'unique_occurrences':len(set(occ)),'proposal_ids':len(P['proposals']),'changed_payloads_since_s5':len(pids),'byte_identical_other_payloads_since_s5':len(P['proposals'])-len(pids),'affected_case_indices':sorted(indices),'unchanged_complete_case_objects_since_s5':len(D['decisions'])-len(indices),'affected_cm_occurrences':sum(len(D['decisions'][i]['occurrence_ids']) for i in indices),'source_outcomes_changed':0,'changed_payloads_since_c9':len(pids|priorids),'unchanged_complete_case_objects_since_c9':len(D['decisions'])-len(indices|{21,44,187}),'prior_evidence_objects_exact':len(oldE),'evidence_objects':len(E['evidence']),'current_retirements':0};save(S/'accounting.json',counts)
selection=copy.deepcopy(load(B/'selection.json'));selection['at']=at;selection['predecessor_head']=BASE;selection['authoritative_core']={n:bind(F/n) for n in ['decisions.json','proposals.json','evidence.json']};selection['selected_payloads']=[{'proposal_id':p['proposal_id'],'owner_path':p['owner_path'],'destination_path':p.get('destination_path',p['owner_path']),'before_sha256':p['before_sha256'],'after_capture':p['after_capture'],'case_ids':p['case_ids']} for p in P['proposals']];selection['complete_retirement_bridge']=bind(S/'complete-bridge.json');selection['previous_authoritative_selection']=bind(B/'selection.json');selection['qualified_component_assertion_successor']=[{'proposal_id':x['proposal_id'],'after_capture':x['after'],'scope':x['conclusion']} for x in proof];selection['combined_c9_bridge']=bind(S/'combined-c9-bridge.json');selection['approval']=False;save(S/'selection.json',selection)
save(S/'finalization-binding.json',{'at':at,'author_freeze':bind(S/'author-freeze.json'),'final_core':{n:bind(F/n) for n in ['decisions.json','evidence.json','proposals.json']},'current_payloads':[{'proposal_id':x['proposal_id'],'capture':x['after']} for x in proof],'payloads_unchanged_after_author_freeze':True,'scope':'Only new exact independent review/validation evidence and scoped status/pointers finalized; no further payload or source interpretation changes.'})
print(json.dumps(counts,indent=2))
