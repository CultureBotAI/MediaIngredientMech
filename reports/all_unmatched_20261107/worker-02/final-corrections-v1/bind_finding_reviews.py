"""Join exact author ledgers with actual independent outputs; no disposition inference."""
import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
R=Path(__file__).resolve().parent

def load(p):return json.loads((R/p).read_text())
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def ref(p):return {'path':str((R/p).relative_to(R.parent)),'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}
def main():
 author=load('family-dispositions-v1.json');peer=load('independent/family-ledger-review-v1.json');proof=load('independent/scientific-review-v1.json');binding=load('review-bound-v1/review-binding-receipt.json')
 cases={d['case_id']:d for d in load('review-bound-v1/decisions.json')['decisions']};props={p['proposal_id']:p for p in load('review-bound-v1/proposals.json')['proposals']};cr={d['case_id']:d for d in proof['case_reviews']};pr={p['proposal_id']:p for p in proof['proposal_reviews']};cb={x['case_id']:x for x in binding['case_bindings']};fr={x['family_id']:x for x in peer['family_reviews']}
 assert len(cases)==len(cr)==188 and len(props)==len(pr)==117 and len(author['families'])==len(fr)==16
 def casebindings(ids):
  result=[]
  for cid in sorted(set(ids)):
   assert cr[cid]['decision_canonical_sha256']==cb[cid]['reviewed_decision_sha256']
   assert digest(cases[cid])==cb[cid]['bound_decision_sha256']
   result.append({'case_id':cid,'case_input_sha256':cases[cid]['case_input_sha256'],'reviewed_input_sha256':cr[cid]['decision_canonical_sha256'],'final_bound_decision_sha256':digest(cases[cid]),'review_disposition':cr[cid]['status'],'reviewer':cr[cid]['reviewer'],'metadata_bridge':cb[cid]})
  return result
 families=[]
 for row in author['families']:
  rid=row['family_id'];ind=fr[rid];assert digest(row)==ind['family_row_sha256']
  pbindings=[]
  for p in row['current_complete_proposal_bindings']:
   pid=p['proposal_id'];assert digest(props[pid])==p['proposal_object_sha256']==pr[pid]['proposal_canonical_sha256'];assert props[pid]['after_capture']==pr[pid]['after_capture']==p['complete_after_capture']
   pbindings.append({'proposal_id':pid,'complete_after_capture':props[pid]['after_capture'],'review_disposition':pr[pid]['status'],'review_mode':pr[pid]['review_mode'],'reviewer':pr[pid]['reviewer']})
  families.append({'family_id':rid,'source_finding_ids':row['source_finding_ids'],'author_row_sha256':digest(row),'original_family_binding':{k:v for k,v in row['original_family_binding'].items() if k!='original_full_value'},'issue_urls':[x['url'] for x in row['issues_and_live_receipts']],'independent_family_review':ind,'current_cases':casebindings(x['case_id'] for x in row['current_complete_case_bindings']),'current_complete_payloads':pbindings,'retired_original_proposals':row['retired_original_proposals'],'residual_holds':row['residual_holds'],'current_owner_issue_or_release_closed':False})
 stable=load('lineage-v1/stable-finding-lineage.json')['groups'];groups=[]
 for i,g in enumerate(stable):
  groups.append({'finding_id':g['finding_id'],'complete_original_group_pointer':f'/groups/{i}','complete_group_sha256':digest(g),'publication_issue':g['publication_issue'],'current_cases':casebindings(x['case_id'] for x in g['source_case_bindings']),'disposition':'Exact historical scientific dispositions retained. Current cases connect to actual review and metadata-only binding; no old finding is globally reopened, retired, or relabeled current-owner approval.'})
 out={'assembled_at':datetime.now(timezone.utc).isoformat(),'assembly_author':'worker02 /root','actual_independent_reviewer':'/root/final_reviewer','inputs':{p:ref(p) for p in ['family-dispositions-v1.json','independent/family-ledger-review-v1.json','independent/scientific-review-v1.json','review-bound-v1/review-binding-receipt.json','review-bound-v1/decisions.json','review-bound-v1/proposals.json','lineage-v1/stable-finding-lineage.json','lineage-v1/historical-object-lineage.json','lineage-v1/retained-holds.json']},'families':families,'stable_finding_bindings':groups,'historical_objects_preserved':735,'original_frozen_holds_preserved':337,'additional58provenance_obligation':author['additional_scoped_obligations'],'additional_new_findings':peer['unfixed_new_findings'],'whole_owner_or_release_approval':False,'limits':'Author pending-review records remain immutable. This join cites later actual independent reviews; it does not handpatch old approvals or infer closure. New additional targets remain uncorrected pending coordinator filing; this publication dependency is not an unknown scientific fact.'}
 with (R/'issue-correction-independent-review-ledger-v1.json').open('x') as f:json.dump(out,f,indent=2,ensure_ascii=False);f.write('\n')
 print(json.dumps({'families':len(families),'stable_finding_bindings':len(groups),'sha256':ref('issue-correction-independent-review-ledger-v1.json')['sha256']}))
if __name__=='__main__':main()
