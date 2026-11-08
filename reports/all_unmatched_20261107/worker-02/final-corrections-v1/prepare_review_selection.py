"""Freeze exact post-typing candidates for independent final review."""
from copy import deepcopy
from datetime import datetime,timezone
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent;A=R.parent
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def main():
 out=R/'review-selection-v1';out.mkdir(exist_ok=False)
 original_d=load(A/'continuation-1201-v1/decisions.json')['decisions'];original_p={p['proposal_id']:p for p in load(A/'continuation-1201-v1/proposals.json')['proposals']}
 ds=load(R/'pretype-v2/decisions.json');ps=load(R/'typed-v1/proposals.json');es=load(R/'pretype-v2/evidence.json');composition=load(R/'pretype-v2/composition.json');typing=load(R/'typed-v1/type-correction-receipt.json');typed={p['proposal_id'] for p in typing['changed_candidates']}
 eid='w02-final-58-claim-specific-type-correction'
 es['evidence'].append({'evidence_id':eid,'kind':'local_validation','capture':{'root':'artifact','path':'final-corrections-v1/typed-v1/type-correction-receipt.json','sha256':sha(R/'typed-v1/type-correction-receipt.json')},'url':None,'locator':'All58 original full-value MappingEvidence objects mapped to51 exact composed candidate payloads; native guarded type-only write receipts and truthful append-only history','supports_or_contradicts':'Provenance correction only: original new-agent entries use LLM_SUGGESTION. Historical human evidence, ComponentEvidence enums, all scientific notes, citations and fields remain unchanged by this typing step. Original W02 authors do not independently approve their own science.'})
 payloads=[];changed_payloads=set()
 for p in ps['proposals']:
  if p['proposal_id'] in typed:p['evidence_ids'].append(eid)
  old=original_p.get(p['proposal_id']);changed=old is None or old['after_capture']!=p['after_capture']
  if changed:changed_payloads.add(p['proposal_id'])
  authors=composition['proposal_authors'].get(p['proposal_id'],[])
  if p['proposal_id'] in typed:authors=list(dict.fromkeys(authors+['worker02 /root']))
  payloads.append({'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'old_selected_proposal':old,'complete_payload_changed':changed,'authors':authors,'scope':'fresh_complete_candidate_review' if changed else 'W04 unchanged complete payload by exact hash; original holds retained','required_review':'pending' if changed else 'exact_historical_binding'})
 case_rows=[]
 for old,d in zip(original_d,ds['decisions'],strict=True):
  assert all(old[k]==d[k] for k in ['case_id','case_input_sha256','source','occurrence_ids'])
  affected=bool(changed_payloads.intersection(d['proposal_ids'])) or d!=old
  if typed.intersection(d['proposal_ids']):
   if eid not in d['evidence_ids']:d['evidence_ids'].append(eid)
  if affected:d['independent_review']={'status':'pending','evidence_ids':[]}
  case_rows.append({'case_id':d['case_id'],'case_input_sha256':d['case_input_sha256'],'old_decision_sha256':digest(old),'review_input_decision_sha256':digest(d),'affected':affected,'authors':composition['case_authors'].get(d['case_id'],[])+(['worker02 /root'] if typed.intersection(d['proposal_ids']) else []),'proposal_ids':d['proposal_ids'],'original_decision':old,'review_scope':'Full affected decision and complete source context with fresh exact candidate review; scientific fields unchanged by type-only edits where applicable.' if affected else 'Exact unchanged W04-reviewed decision and source context; no new approval beyond its precise disposition/holds.'})
 routing={'created_at':datetime.now(timezone.utc).isoformat(),'actual_reviewer':'worker02 /root/final_reviewer','cases':case_rows,'payloads':payloads,'counts':{'cases':188,'selected_proposals':len(ps['proposals']),'changed_complete_payloads':len(changed_payloads),'affected_source_decisions':sum(r['affected'] for r in case_rows)},'independent_approval_established':False}
 for name,value in [('decisions',ds),('proposals',ps),('evidence',es),('review-routing',routing)]:
  with (out/(name+'.json')).open('x') as f:json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
 print(json.dumps(routing['counts']))
if __name__=='__main__':main()
