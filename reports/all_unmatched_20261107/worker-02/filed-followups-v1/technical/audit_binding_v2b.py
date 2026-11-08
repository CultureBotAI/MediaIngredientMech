"""Independent read-only input/proof/selected bridge check; no binder imported."""
from pathlib import Path
import json,hashlib,copy
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent;R=HERE.parent;A=R.parent;W=R.parents[3]
def digest(raw):return hashlib.sha256(raw).hexdigest()
def canonical(value):return digest(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
inputs=[]
def read(p):
 raw=p.read_bytes();inputs.append({'path':str(p.relative_to(W)),'sha256':digest(raw)});return json.loads(raw),raw

def main():
 out=HERE/'binding-preservation-v2.json'
 if out.exists():raise FileExistsError(out)
 old={};new={};prior={}
 for name in ['decisions','proposals','evidence']:
  old[name],oldraw=read(R/'review-input-v2'/(name+'.json'))
  new[name],raw=read(R/'selected-v2'/(name+'.json'))
  prior[name],priorraw=read(R/'selected-v1'/(name+'.json'));assert priorraw==raw
  if name=='proposals':assert raw==oldraw
 proof,proofraw=read(R/'independent/scientific-review-v2.json');receipt,_=read(R/'selected-v2/review-binding.json')
 assert receipt['proof_sha256']==digest(proofraw)
 assert proof['reviewer']=='/root/final_reviewer' and proof['full_owner_or_release_approval'] is False
 pins={x['path']:x['sha256'] for x in proof['input_hash_manifest']};assert len(pins)==len(proof['input_hash_manifest'])
 for p,h in pins.items():assert digest(Path(p).read_bytes())==h
 for n in ['decisions','proposals','evidence']:assert digest((R/'review-input-v2'/(n+'.json')).read_bytes())==pins[str((R/'review-input-v2'/(n+'.json')).absolute())]
 ds=old['decisions']['decisions'];ns=new['decisions']['decisions'];assert len(ds)==len(ns)==188
 assert {k:v for k,v in old['decisions'].items() if k!='decisions'}=={k:v for k,v in new['decisions'].items() if k!='decisions'}
 cr={x['case_id']:x for x in proof['case_reviews']};assert len(cr)==4
 indices={88,93,114,118};assert set(cr)=={ds[i]['case_id'] for i in indices}
 eid='w02-filed-followups-independent-exact-review-v2';rows=[]
 for i,(b,n,x) in enumerate(zip(ds,ns,receipt['case_bindings'],strict=True)):
  assert b['case_id']==n['case_id']==x['case_id']
  delta=sorted(k for k in set(b)|set(n) if b.get(k)!=n.get(k))
  assert delta==(['independent_review'] if i in indices else [])
  if i in indices:
   assert b['independent_review']=={'status':'pending','evidence_ids':[]};assert n['independent_review']=={'status':'complete','evidence_ids':[eid]}
   q=cr[b['case_id']];assert q['decision_canonical_sha256']==canonical(b) and q['case_input_sha256']==b['case_input_sha256']
   assert q['reviewer']=='/root/final_reviewer' and q['authorship_conflict'] is False and q['full_owner_or_release_approval'] is False and q['status']=='approve_bounded_correction'
   assert all(a.removeprefix('worker02 ').strip()!='/root/final_reviewer' for a in q['original_authors'])
  assert x['reviewed_input_sha256']==canonical(b) and x['selected_sha256']==canonical(n) and x['metadata_only_change']==(i in indices)
  rows.append({'index':i,'case_id':b['case_id'],'input_canonical_sha256':canonical(b),'selected_canonical_sha256':canonical(n),'changed_fields':delta})
 assert receipt['metadata_updates']==4
 props=new['proposals']['proposals'];assert len(props)==117;pr={q['proposal_id']:q for q in proof['proposal_reviews']};assert len(pr)==2
 pid='b2-proposal-sodium_resazurin_01_percent_wv_jcm363_1023';acid='b2-proposal-sulfuric_acid_10n_named_sources';assert set(pr)=={pid,acid}
 payloads=[]
 for p in props:
  cap=p['after_capture'];actual=digest((A/cap['path']).read_bytes());assert actual==cap['sha256']
  if p['proposal_id'] in pr:
   q=pr[p['proposal_id']];assert q['proposal_canonical_sha256']==canonical(p) and q['after_capture']==cap
   assert q['reviewer']=='/root/final_reviewer' and q['authorship_conflict'] is False and q['full_owner_or_release_approval'] is False
   assert q['status']==('approve_bounded_correction' if p['proposal_id']==pid else 'preserved_unchanged_context')
   if p['proposal_id']==pid:
    assert all(a.removeprefix('worker02 ').strip()!='/root/final_reviewer' for a in q['original_authors'])
   else:assert q['fresh_whole_payload_science_approval'] is False
  payloads.append({'proposal_id':p['proposal_id'],'after_capture':cap})
 olde=old['evidence']['evidence'];newe=new['evidence']['evidence'];assert newe[:-1]==olde and len(newe)==len(olde)+1
 ev=newe[-1];assert ev['evidence_id']==eid and ev['kind']=='independent_review' and ev['capture']['sha256']==digest(proofraw) and A/ev['capture']['path']==R/'independent/scientific-review-v2.json'
 assert len({x['evidence_id'] for x in newe})==len(newe)
 # The preceding sealed audit establishes116 unchanged payloads and184 exact historicalcase objects; prove that bridge still holds directly.
 baseline,_=read(A/'final-corrections-v1/review-bound-v1/decisions.json')
 for i,d in enumerate(baseline['decisions']):
  if i not in indices:assert d==ns[i]
 result={'reviewer':'/root/research_b','reviewed_at':datetime.now(timezone.utc).isoformat(),'scope':'Technical metadata/provenance binding only; no chemistry approval','status':'PASS','input_bindings':inputs,'whole_independent_proof_input_hashes_verified':len(pins),'counts':{'cases':188,'occurrences':sum(len(x['occurrence_ids']) for x in ns),'proposals':117,'only_review_metadata_changed_cases':4,'unchanged_complete_prior_cases':184,'payload_changes_during_review_binding':0,'new_independent_evidence_entries':1},'selected_v1_and_v2_three_core_file_bytes_identical':True,'case_rows':rows,'payload_bindings':payloads,'prior116payload_preservation_proof':'independent-preservation-v2.json','actual_scientific_reviewer':'/root/final_reviewer','no_chemistry_or_release_approval_by_this_receipt':True}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'status':'PASS','receipt':str(out.relative_to(W)),'sha256':digest(out.read_bytes()),'counts':result['counts']}))
if __name__=='__main__':main()
