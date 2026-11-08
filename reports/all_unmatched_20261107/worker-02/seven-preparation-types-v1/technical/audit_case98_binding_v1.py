"""Independent combined selected-v3 metadata bridge; no root helper imported."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
T=Path(__file__).resolve().parent;R=T.parent;A=R.parent;W=R.parents[3]
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(x):return sha(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
def main():
 out=T/'case98-binding-preservation-v1.json'
 if out.exists():raise FileExistsError(out)
 inputs=[]
 def read(p):
  raw=p.read_bytes();inputs.append({'path':str(p.relative_to(W)),'sha256':sha(raw)});return json.loads(raw),raw
 before={};after={}
 for n in ['decisions','proposals','evidence']:
  before[n],br=read(R/'review-input-v2'/(n+'.json'));after[n],ar=read(R/'selected-v3'/(n+'.json'))
  assert {k:v for k,v in before[n].items() if k!=n}=={k:v for k,v in after[n].items() if k!=n}
  if n=='proposals':
   assert br==ar
   for parent in ['selected-v2','review-input-v1']:assert ar==(R/parent/(n+'.json')).read_bytes()
 proof,proofraw=read(R/'independent/scientific-review-v2.json');binding,_=read(R/'selected-v3/review-binding.json');assert binding['proof_sha256']==sha(proofraw)
 pins={x['path']:x['sha256'] for x in proof['input_hash_manifest']};assert len(pins)==len(proof['input_hash_manifest'])
 for name,digest in pins.items():
  path=Path(name);path=path if path.is_absolute() else W/path;assert sha(path.read_bytes())==digest
 for n in ['decisions','proposals','evidence']:assert sha((R/'review-input-v2'/(n+'.json')).read_bytes())==pins[str((R/'review-input-v2'/(n+'.json')).absolute())]
 ds=before['decisions']['decisions'];ns=after['decisions']['decisions'];assert len(ds)==len(ns)==188
 cr={x['case_id']:x for x in proof['case_reviews']};assert set(cr)=={ds[58]['case_id'],ds[98]['case_id']}
 def auth(row):assert row['reviewer']=='/root/final_reviewer' and row['current_correction_author']=='worker02 /root' and row['authorship_conflict'] is False and row['status']=='approve_bounded_correction' and row['full_owner_or_release_approval'] is False
 eid='w02-seven-preparations-case98-independent-exact-review-v2';rows=[]
 for i,(b,n,x) in enumerate(zip(ds,ns,binding['case_bindings'],strict=True)):
  delta=sorted(k for k in set(b)|set(n) if b.get(k)!=n.get(k));assert delta==(['independent_review'] if i in [58,98] else [])
  assert b['case_id']==n['case_id']==x['case_id'];assert x['reviewed_input_sha256']==canonical(b) and x['selected_sha256']==canonical(n) and x['metadata_only_change']==(i in [58,98])
  if i in [58,98]:
   assert b['independent_review']=={'status':'pending','evidence_ids':[]} and n['independent_review']=={'status':'complete','evidence_ids':[eid]}
   q=cr[b['case_id']];auth(q);assert q['decision_canonical_sha256']==canonical(b) and q['case_input_sha256']==b['case_input_sha256']
  rows.append({'index':i,'case_id':b['case_id'],'input_sha256':canonical(b),'selected_sha256':canonical(n),'changed_fields':delta})
 assert binding['metadata_updates']==2 and len(ns[58]['occurrence_ids'])==24 and len(ns[98]['occurrence_ids'])==1
 ps=after['proposals']['proposals'];assert len(ps)==117;pr={x['proposal_id']:x for x in proof['proposal_reviews']};targets={x['proposal_id'] for x in json.loads((T/'intake-v1.json').read_bytes())['targets']};assert set(pr)==targets and len(pr)==7
 payloads=[]
 for p in ps:
  cap=p['after_capture'];assert sha((A/cap['path']).read_bytes())==cap['sha256']
  if p['proposal_id'] in pr:
   q=pr[p['proposal_id']];auth(q);assert q['proposal_canonical_sha256']==canonical(p) and q['after_capture']==cap
  payloads.append({'proposal_id':p['proposal_id'],'after_capture':cap})
 oe=before['evidence']['evidence'];ne=after['evidence']['evidence'];assert len(oe)==1829 and len(ne)==1830 and ne[:-1]==oe
 last=ne[-1];assert last['evidence_id']==eid and last['capture']['sha256']==sha(proofraw) and A/last['capture']['path']==R/'independent/scientific-review-v2.json'
 baseline,_=read(A/'filed-followups-v1/selected-v3/decisions.json')
 for i,(b,n) in enumerate(zip(baseline['decisions'],ns,strict=True)):
  delta=sorted(k for k in set(b)|set(n) if b.get(k)!=n.get(k));assert delta==(['applicability','independent_review','reasoning'] if i==98 else ['independent_review'] if i==58 else [])
 result={'reviewer':'/root/research_b','reviewed_at':datetime.now(timezone.utc).isoformat(),'status':'PASS','scope':'Technical reviewbinding only; chemistry/sourceinterpretation attributed to actualDproof, not reviewerB','input_bindings':inputs,'actual_proof_input_hashes_verified':len(pins),'counts':{'cases':188,'occurrences':sum(len(x['occurrence_ids']) for x in ns),'proposals':117,'case58_occurrences':24,'case98_occurrences':1,'binding_review_metadata_changes':2,'case98_attribution_fields_since_predecessor':2,'unchanged_complete_predecessor_cases':186,'payload_changes_since_seven_review':0,'unchanged_baseline_payloads_via_exact_prior_proof':110,'evidence':1830},'all117proposal_ledger_bytes_equal_previous_sevenreview':True,'case_rows':rows,'payloads':payloads,'prior_complete_payload_preservation':'independent-preservation-final-v1.json','companion_two_field_preservation':'case98-preservation-review-v1.json','no_new_history_alias_ingredient_chemical_outcome_or_release_change':True}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'status':'PASS','receipt':str(out.relative_to(W)),'sha256':sha(out.read_bytes()),'counts':result['counts']}))
if __name__=='__main__':main()
