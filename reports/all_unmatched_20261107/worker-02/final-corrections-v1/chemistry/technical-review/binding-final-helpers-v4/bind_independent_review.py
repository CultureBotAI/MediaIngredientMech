"""Bind actual independent review completion, never infer scientific approval.

Writes an immutable selection whose only decision delta is independent_review.
Open scientific findings remain open in the exact referenced review proof.
"""
from copy import deepcopy
from datetime import datetime,timezone
import argparse,hashlib,json,sys
from pathlib import Path
W=Path(__file__).resolve().parents[4];R=Path(__file__).resolve().parent;A=R.parent
sys.path.insert(0,str(W/'src'))
from mediaingredientmech.curate.publication_guard import FrozenFile,no_alias
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files

def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def unique(rows,key):
 result={}
 for x in rows:
  if x[key] in result:raise ValueError('Duplicate review target')
  result[x[key]]=x
 return result
def normalize(name):return name.removeprefix('worker02 ').strip()
def validate_reviews(ds,ps,routing,proof):
 cases=unique(ds,'case_id');props=unique(ps,'proposal_id');cr=unique(proof['case_reviews'],'case_id');pr=unique(proof['proposal_reviews'],'proposal_id')
 if set(cr)!=set(cases) or set(pr)!=set(props):raise ValueError('Missing or unexpected review target')
 routes=unique(routing['cases'],'case_id');proutes=unique(routing['payloads'],'proposal_id')
 if set(routes)!=set(cases) or set(proutes)!=set(props):raise ValueError('Incomplete author routing')
 for key,row in cr.items():
  case=cases[key]
  if row['case_input_sha256']!=case['case_input_sha256'] or row['decision_canonical_sha256']!=digest(case):raise ValueError('Stale case review')
  verify_reviewer(row,routes[key]['authors'])
 for key,row in pr.items():
  p=props[key]
  if row['proposal_canonical_sha256']!=digest(p) or row['after_capture']!=p['after_capture']:raise ValueError('Stale complete proposal review')
  verify_reviewer(row,proutes[key]['authors'])
 return cr,pr
def verify_reviewer(row,authors):
 reviewer=normalize(row['reviewer'])
 if reviewer!='/root/final_reviewer' or reviewer in {normalize(x) for x in authors+row['original_authors']} or row['authorship_conflict'] is not False:raise ValueError('Reviewer author conflict or unsupported attribution')
 if row['status'] not in ['approve','findings_open'] or not row['reasoning'].strip() or not row['review_mode'].strip():raise ValueError('Incomplete review disposition')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--selection',type=Path,required=True);ap.add_argument('--proof',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
 out=args.out.absolute()
 if '..' in args.out.parts or out!=out.resolve() or not out.is_relative_to(R):raise ValueError('Output escapes report root')
 no_alias(out)
 if out.exists():raise FileExistsError(out)
 held=[FrozenFile.capture(args.selection/(n+'.json')) for n in ['decisions','proposals','evidence','review-routing']]+[FrozenFile.capture(args.proof)]
 docs=[json.loads(x.content) for x in held];ds,ps,es,routing,proof=docs
 cr,pr=validate_reviews(ds['decisions'],ps['proposals'],routing,proof)
 for p in ps['proposals']:
  cap=p['after_capture'];path=A/cap['path'];f=FrozenFile.capture(path)
  if hashlib.sha256(f.content).hexdigest()!=cap['sha256']:raise ValueError('Stale full payload bytes')
  held.append(f)
 eid='w02-final-exact-independent-review-v1';proofsha=hashlib.sha256(held[4].content).hexdigest()
 if eid in {e['evidence_id'] for e in es['evidence']}:raise ValueError('Review evidence ID already present')
 es=deepcopy(es);es['evidence'].append({'evidence_id':eid,'kind':'independent_review','capture':{'root':'artifact','path':str(args.proof.absolute().relative_to(A)),'sha256':proofsha},'url':None,'locator':'Exact188case/117completepayload author-independent review rows; per-target statuses, sources, hashes and inheritedW04 scopes','supports_or_contradicts':'Actual worker02 /root/final_reviewer review completion. Status findings_open remains an unresolved finding, not approval. Changed scientific fields and provenance-only deltas are distinguished; no whole-owner or release clearance.'})
 result=deepcopy(ds);bindings=[];routes={x['case_id']:x for x in routing['cases']}
 for old,new in zip(ds['decisions'],result['decisions'],strict=True):
  if routes[old['case_id']]['affected']:new['independent_review']={'status':'complete','evidence_ids':[eid]}
  a=deepcopy(old);b=deepcopy(new);a.pop('independent_review',None);b.pop('independent_review',None)
  if a!=b:raise ValueError('Scientific decision changed during review binding')
  bindings.append({'case_id':old['case_id'],'reviewed_decision_sha256':digest(old),'bound_decision_sha256':digest(new),'only_independent_review_metadata_changed':old!=new,'scientific_review_disposition':cr[old['case_id']]['status'],'reviewer':cr[old['case_id']]['reviewer']})
 receipt={'bound_at':datetime.now(timezone.utc).isoformat(),'author':'worker02 /root','actual_independent_reviewer':'/root/final_reviewer','review_proof_sha256':proofsha,'case_bindings':bindings,'source_selection':str(args.selection),'proposal_ledger_sha256_unchanged':hashlib.sha256(held[1].content).hexdigest(),'all_payloads_unchanged':True,'counts':{'cases':len(cr),'proposals':len(pr),'completed_review_metadata_updates':sum(x['only_independent_review_metadata_changed'] for x in bindings),'case_findings_open':sum(x['status']=='findings_open' for x in cr.values()),'proposal_findings_open':sum(x['status']=='findings_open' for x in pr.values())},'limits':'Completion records review work, not scientific acceptance; exact open findings and every source/owner/release obligation remain. Native review independently attests exact immutable reviewed input; this receipt is a metadata-only bridge awaiting final independent assembly check.'}
 out.mkdir(exist_ok=False)
 outputs=[(out/'decisions.json',(json.dumps(result,indent=2,ensure_ascii=False)+'\n').encode()),(out/'proposals.json',held[1].content),(out/'evidence.json',(json.dumps(es,indent=2,ensure_ascii=False)+'\n').encode()),(out/'review-binding-receipt.json',(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n').encode())]
 def verify():
  for f in held:f.verify()
 publish_new_files(outputs,verify);verify();print(json.dumps(receipt['counts']))
if __name__=='__main__':main()
