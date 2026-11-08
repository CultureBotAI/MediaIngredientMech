"""Select exact reviewed wording bytes and bind current/cumulative complete bridges."""
from pathlib import Path
import copy,datetime,hashlib,json
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v5';B=A/'successor-v4';C=S/'author-core';F=S/'final-core';PID='sv1-bio-calf_blood_togo_m2854';BASE='82fc29d837a223edb9c436445ec7ea13d2840c7b'
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest();at=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def bind(p):return {'path':str(p.relative_to(A)),'sha256':sha(p)}
science=S/'reviews/skeptic/scientific-review-v1.json';retention=S/'reviews/retention/author-core-retention-review-v1.json'
sr=load(science);rr=load(retention);assert sr['status']=='PASS_BOUNDED_CORRECTION' and sr['author_independent'] and not sr['new_unexpected_findings'];assert rr['verdict']=='pass_with_limitations' and not rr.get('findings',[])
D=load(C/'decisions.json');P=load(C/'proposals.json');E=load(C/'evidence.json');oldD=load(B/'final-core/decisions.json')['decisions'];oldP=load(B/'final-core/proposals.json')['proposals'];oldE=load(B/'final-core/evidence.json')['evidence'];target=next(p for p in P['proposals'] if p['proposal_id']==PID)
assert target['after_capture']['sha256']=='7a54c5bb03008949dec5ced0fbb8da9deee348fd4ad2473e66d41655db975b9d'
specs=[('sv5-independent-wording',science,'independent_review','Fresh independent exact explanatory-field/source assessment only; no owner or broader scientific approval.'),('sv5-independent-retention',retention,'independent_review','Full127proposal/188case/304occurrence retained-byte comparison; unchanged science not reapproved.'),('sv5-native-narrow-validation',S/'validation/narrow-native.json','local_validation','Guarded closed-schema byte roundtrip, full overlay partonomy and unchanged native identifier/mapping/alias projections.')]
for eid,path,kind,summary in specs:E['evidence'].append({'evidence_id':eid,'kind':kind,'capture':{'root':'artifact',**bind(path)},'url':None,'accessed_at':at,'locator':'Complete exact artifact; local reading, not new primary retrieval','supports_or_contradicts':summary,'case_ids':target['case_ids']})
ids=[x[0] for x in specs]
for row in [target,D['decisions'][44]]:
 row['independent_review']={'status':'complete','evidence_ids':ids[:2]};row['evidence_ids']+=ids;row['wording_successor']['review_state']='complete_for_exact_bounded_wording_correction';row['wording_successor']['independent_review_bindings']=[bind(science),bind(retention)]
target['review_status_explanation']='Exact two-note explanatory correction, appended history and case/proposal dependencies independently reviewed. Original identity/mapping/source judgments remain within their original attribution. The preserved carbonate correction has its own exact S4 reviews. Separate W09 c9a review and coordinator whole-owner/source/role/export acceptance are not blanket-transferred.'
assert E['evidence'][:len(oldE)]==oldE
F.mkdir()
for n,d in [('decisions.json',D),('proposals.json',P),('evidence.json',E)]:save(F/n,d)
def bridge(priorD,priorP,allowedcases,allowedpids):
 cases=[];props=[]
 assert len(priorD)==len(D['decisions'])
 for i,(old,new) in enumerate(zip(priorD,D['decisions'])):
  for k in ['case_id','case_input_sha256','source','occurrence_ids','disposition','applicability','missing_requirement','proposal_ids','owner_records']:assert old.get(k)==new.get(k),(i,k)
  assert i in allowedcases or old==new
  cases.append({'source_index':i,'case_id':new['case_id'],'before_object_sha256':canon(old),'after_object_sha256':canon(new),'complete_object_exact':old==new,'source_identity_occurrence_owner_hashes_exact':True,'reasoning_exact':old['reasoning']==new['reasoning'],'occurrence_ids':new['occurrence_ids'],'proposal_ids':new['proposal_ids']})
 prior_by={p['proposal_id']:p for p in priorP};assert set(prior_by)=={p['proposal_id'] for p in P['proposals']}
 for new in P['proposals']:
  old=prior_by[new['proposal_id']]
  for k in ['case_ids','owner_path','before_sha256','kind']:assert old[k]==new[k]
  assert new['proposal_id'] in allowedpids or old==new
  assert sha(A/new['after_capture']['path'])==new['after_capture']['sha256']
  props.append({'proposal_id':new['proposal_id'],'before_proposal_sha256':canon(old),'after_proposal_sha256':canon(new),'proposal_object_exact':old==new,'old_capture':old['after_capture'],'selected_capture':new['after_capture'],'payload_byte_exact':old['after_capture']==new['after_capture'],'owner_path':new['owner_path'],'before_owner_sha256':new['before_sha256'],'case_ids':new['case_ids'],'whole_owner_approval':False})
 return {'all_cases':cases,'all_proposals':props,'scope':'Exact successor retention bridge; no blanket source, owner, role, scientific or export approval.'}
current=bridge(oldD,oldP,{44},{PID});current.update({'at':at,'predecessor_head':BASE,'previous_complete_bridge':bind(B/'complete-bridge.json'),'earlier_retirement_bridge':bind(A/'successor-v3/retirement-bridge.json'),'current_proposals_retired':[]});save(S/'complete-bridge.json',current)
carbonate='sv1-buffers-carbonate_co2_nominal4percent_togo_m202';joint=bridge(load(A/'successor-v3/decisions.json')['decisions'],load(A/'successor-v3/proposals.json')['proposals'],{21,44,187},{PID,carbonate})
joint.update({'at':at,'baseline_head':'c9a96da71a1977014680e5a92e600dfc7e3874db','intermediate_published_head':BASE,'bounded_corrections':[{'proposal_id':carbonate,'scope':'PARTIAL to UNKNOWN plus one truthful history and exact dependent metadata, independently reviewed under successor-v4; retained here byte-exact','selected_payload_sha256':'135788bfd2a511671a90ff9b912092df789c9209995f88d11b4aa6134eca0625','handoff':bind(B/'HANDOFF-v2.json')},{'proposal_id':PID,'scope':'Two current explanatory notes plus one truthful history and exact case44/proposal reasoning/dependencies; original history retained','selected_payload':target['after_capture']}],'separate_w09_review':'Its exact c9a scope remains historical; neither bounded successor inherits blanket approval.'});save(S/'combined-c9-bridge.json',joint)
occ=[x for d in D['decisions'] for x in d['occurrence_ids']];assert len(occ)==len(set(occ))==304 and len(D['decisions'])==188 and len(P['proposals'])==127
counts={'cases':len(D['decisions']),'unique_occurrences':len(set(occ)),'proposal_ids':len(P['proposals']),'changed_payloads_since_s4':1,'byte_identical_other_payloads_since_s4':126,'unchanged_complete_case_objects_since_s4':187,'source_outcomes_changed':0,'changed_payloads_since_c9':2,'unchanged_complete_case_objects_since_c9':185,'prior_evidence_objects_exact':len(oldE),'evidence_objects':len(E['evidence']),'current_retirements':0};save(S/'accounting.json',counts)
selection=copy.deepcopy(load(B/'selection-v2.json'));selection['at']=at;selection['predecessor_head']=BASE;selection['authoritative_core']={n:bind(F/n) for n in ['decisions.json','evidence.json','proposals.json']};selection['selected_payloads']=[{'proposal_id':p['proposal_id'],'owner_path':p['owner_path'],'destination_path':p.get('destination_path',p['owner_path']),'before_sha256':p['before_sha256'],'after_capture':p['after_capture'],'case_ids':p['case_ids']} for p in P['proposals']];selection['complete_retirement_bridge']=bind(S/'complete-bridge.json');selection['previous_authoritative_selection']=bind(B/'selection-v2.json');selection['bounded_wording_successor']={'proposal_id':PID,'after_capture':target['after_capture'],'no_blanket_c9a_or_s4_review_transfer':True};selection['combined_c9_bridge']=bind(S/'combined-c9-bridge.json');selection['approval']=False;save(S/'selection.json',selection)
save(S/'finalization-binding.json',{'at':at,'author_freeze':bind(S/'author-freeze.json'),'final_core':{n:bind(F/n) for n in ['decisions.json','evidence.json','proposals.json']},'current_payload':target['after_capture'],'payload_unchanged_after_author_freeze':True,'scope':'Only exact reviewer/validation evidence pointers and scoped review status finalized; no further wording or scientific changes.'})
print(json.dumps(counts,indent=2))
