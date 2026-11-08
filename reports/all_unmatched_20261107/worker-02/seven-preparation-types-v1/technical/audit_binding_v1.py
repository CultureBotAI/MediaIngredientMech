"""Independent read-only proof/metadata bridge; does not import the author's binder."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,hashlib,yaml
HERE=Path(__file__).resolve().parent;R=HERE.parent;A=R.parent;W=R.parents[3]
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(v):return sha(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
def main():
 ap=argparse.ArgumentParser();ap.add_argument('selection');ap.add_argument('output');args=ap.parse_args()
 if '/' in args.selection or '/' in args.output or '..' in args.selection or '..' in args.output:raise ValueError('Simple private names only')
 output=HERE/args.output
 if output.exists():raise FileExistsError(output)
 inputs=[]
 def read(p):
  raw=p.read_bytes();inputs.append({'path':str(p.relative_to(W)),'sha256':sha(raw)});return json.loads(raw),raw
 before={};after={}
 for name in ['decisions','proposals','evidence']:
  before[name],br=read(R/'review-input-v1'/(name+'.json'));after[name],ar=read(R/args.selection/(name+'.json'));_,v1=read(R/'selected-v1'/(name+'.json'));assert ar==v1
  if name=='proposals':assert br==ar
 proof,proofraw=read(R/'independent/scientific-review-v1.json');binding,_=read(R/args.selection/'review-binding.json');author,_=read(R/'review-input-v1/author-preservation-receipt.json')
 assert binding['proof_sha256']==sha(proofraw);assert proof['reviewer']=='/root/final_reviewer';assert author['author']=='worker02 /root'
 pins={x['path']:x['sha256'] for x in proof['input_hash_manifest']};assert len(pins)==len(proof['input_hash_manifest'])
 for path,digest in pins.items():
  p=Path(path);p=p if p.is_absolute() else W/p;assert sha(p.read_bytes())==digest
 for n in ['decisions','proposals','evidence']:assert sha((R/'review-input-v1'/(n+'.json')).read_bytes())==pins[str((R/'review-input-v1'/(n+'.json')).absolute())]
 ds=before['decisions']['decisions'];ns=after['decisions']['decisions'];assert len(ds)==len(ns)==188
 assert len(proof['case_reviews'])==1;cr=proof['case_reviews'][0];assert cr['case_id']==ds[58]['case_id'] and cr['decision_canonical_sha256']==canonical(ds[58]) and cr['case_input_sha256']==ds[58]['case_input_sha256'];assert cr['occurrence_ids']==ds[58]['occurrence_ids'] and len(cr['occurrence_ids'])==24
 def authorcheck(row):
  assert row['reviewer']=='/root/final_reviewer' and row['current_correction_author']=='worker02 /root' and row['authorship_conflict'] is False and row['status']=='approve_bounded_correction' and row['full_owner_or_release_approval'] is False
 authorcheck(cr);eid='w02-seven-preparations-independent-exact-review-v1';case_rows=[]
 for i,(b,n,x) in enumerate(zip(ds,ns,binding['case_bindings'],strict=True)):
  delta=sorted(k for k in set(b)|set(n) if b.get(k)!=n.get(k));assert delta==(['independent_review'] if i==58 else [])
  if i==58:assert b['independent_review']=={'status':'pending','evidence_ids':[]} and n['independent_review']=={'status':'complete','evidence_ids':[eid]}
  assert x['case_id']==b['case_id']==n['case_id'] and x['reviewed_input_sha256']==canonical(b) and x['selected_sha256']==canonical(n) and x['metadata_only_change']==(i==58)
  case_rows.append({'case_id':b['case_id'],'reviewed_input_sha256':canonical(b),'selected_sha256':canonical(n),'changed_fields':delta})
 assert binding['metadata_updates']==1
 ps=after['proposals']['proposals'];assert len(ps)==117;pr={x['proposal_id']:x for x in proof['proposal_reviews']};assert len(pr)==7
 targets={x['proposal_id'] for x in json.loads((HERE/'intake-v1.json').read_bytes())['targets']};assert set(pr)==targets
 payloads=[]
 for p in ps:
  cap=p['after_capture'];path=A/cap['path'];assert sha(path.read_bytes())==cap['sha256']
  if p['proposal_id'] in pr:
   row=pr[p['proposal_id']];authorcheck(row);assert row['proposal_canonical_sha256']==canonical(p) and row['after_capture']==cap
   value=yaml.safe_load(path.read_bytes());assert value['curation_history'][-1]['curator']==row['current_correction_author'] and value['curation_history'][-1]['llm_assisted'] is True
   assert canonical(value['curation_history'][:-1])==row['prior_history_canonical_sha256']
  payloads.append({'proposal_id':p['proposal_id'],'after_capture':cap})
 oe=before['evidence']['evidence'];ne=after['evidence']['evidence'];assert ne[:-1]==oe and len(ne)==len(oe)+1
 ev=ne[-1];assert ev['evidence_id']==eid and ev['kind']=='independent_review' and ev['capture']['sha256']==sha(proofraw) and A/ev['capture']['path']==R/'independent/scientific-review-v1.json'
 result={'reviewer':'/root/research_b','reviewed_at':datetime.now(timezone.utc).isoformat(),'scope':'Technical binding only; actual scientific judgments remain D reviewer scope','status':'PASS','selection':args.selection,'input_bindings':inputs,'proof_inputs_reverified':len(pins),'counts':{'cases':188,'occurrences':sum(len(x['occurrence_ids']) for x in ns),'proposals':117,'whole_case58_occurrences':24,'review_metadata_updates':1,'payload_changes_during_binding':0},'selected_core_bytes_equal_selected_v1':True,'actual_current_author_fields_match_new_events':True,'case_rows':case_rows,'payloads':payloads,'whole_predecessor_preservation_receipt':'independent-preservation-final-v1.json','no_chemistry_or_release_approval':True}
 with output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'status':'PASS','receipt':str(output.relative_to(W)),'sha256':sha(output.read_bytes()),'proof_inputs':len(pins),'counts':result['counts']}))
if __name__=='__main__':main()
