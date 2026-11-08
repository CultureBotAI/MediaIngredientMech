"""Bind actual independent review completion; only four review metadata objects change."""
from copy import deepcopy
from datetime import datetime,timezone
import json,sys
from pathlib import Path
import build_successor_v2 as b
R=b.R;S=R/'review-input-v2'
def unique(rows,key):
 result={}
 for row in rows:
  if row[key] in result:raise ValueError('Duplicate review target')
  result[row[key]]=row
 return result
def validate(ds,ps,proof):
 dc=unique(ds,'case_id');pc=unique(ps,'proposal_id');cr=unique(proof['case_reviews'],'case_id');pr=unique(proof['proposal_reviews'],'proposal_id')
 if len(dc)!=188 or len(pc)!=117 or set(cr)!={b.IDS[i] for i in b.AFFECTED} or set(pr)!={b.PID,b.ACID}:raise ValueError('Incomplete or unexpected review scope')
 for key,row in cr.items():
  if row['decision_canonical_sha256']!=b.digest(dc[key]) or row['case_input_sha256']!=dc[key]['case_input_sha256']:raise ValueError('Stale case proof')
  require_reviewer(row,'approve_bounded_correction')
 for key,row in pr.items():
  if row['proposal_canonical_sha256']!=b.digest(pc[key]) or row['after_capture']!=pc[key]['after_capture']:raise ValueError('Stale complete proposal proof')
  require_reviewer(row,'approve_bounded_correction' if key==b.PID else 'preserved_unchanged_context')
 return cr,pr
def require_reviewer(row,status):
 if row['reviewer']!='/root/final_reviewer' or row['authorship_conflict'] is not False or row['status']!=status or not row['reasoning'].strip() or row.get('full_owner_or_release_approval') is not False:raise ValueError('Invalid reviewer/disposition/approval scope')
 if any(x.removeprefix('worker02 ').strip()=='/root/final_reviewer' for x in row.get('original_authors',[])):raise ValueError('Self review')
def main():
 out=b.require_output(R/'selected-v1');proof_path=R/'independent/scientific-review-v2.json'
 held=[b.FrozenFile.capture(S/(n+'.json')) for n in ['decisions','proposals','evidence']]+[b.FrozenFile.capture(proof_path)]
 ds,ps,es,proof=[json.loads(x.content) for x in held];validate(ds['decisions'],ps['proposals'],proof)
 for p in ps['proposals']:
  f=b.FrozenFile.capture(b.A/p['after_capture']['path']);held.append(f)
  b.require_pin(f.content,p['after_capture']['sha256'])
 original=deepcopy(ds);eid='w02-filed-followups-independent-exact-review-v2';cases=[]
 for i,d in enumerate(ds['decisions']):
  if i in b.AFFECTED:d['independent_review']={'status':'complete','evidence_ids':[eid]}
  left=deepcopy(original['decisions'][i]);right=deepcopy(d);left.pop('independent_review');right.pop('independent_review');assert left==right
  cases.append({'case_id':d['case_id'],'reviewed_input_sha256':b.digest(original['decisions'][i]),'selected_sha256':b.digest(d),'metadata_only_change':d!=original['decisions'][i]})
 oldraw=b.raw_array_objects(held[0].content,'decisions');newraw=b.raw_array_objects(b.encode(ds),'decisions');assert all(oldraw[i]==newraw[i] for i in range(188) if i not in b.AFFECTED)
 es['evidence'].append({'evidence_id':eid,'kind':'independent_review','capture':{'root':'artifact','path':str(proof_path.relative_to(b.A)),'sha256':b.sha(proof_path)},'url':None,'locator':'Four complete case decisions, complete resazurin candidate and unchanged shared acid context; scoped author-independent proof','supports_or_contradicts':'Both filed corrections supported at exact bounded scope. No inherited whole-owner/role/release hold cleared, and no fresh review of unrelated candidates claimed.'})
 receipt={'bound_at':datetime.now(timezone.utc).isoformat(),'author':'worker02 /root','reviewer':'/root/final_reviewer','proof_sha256':b.sha(proof_path),'case_bindings':cases,'metadata_updates':sum(x['metadata_only_change'] for x in cases),'proposal_ledger_sha256_unchanged':b.sha(S/'proposals.json'),'all117payload_bytes_unchanged_from_independent_input':True,'scope':'Only independent_review completion metadata changed on four cases. Shared payload and all scientific fields remain the exact independently reviewed bytes.'}
 def verify():
  for f in held:f.verify()
 out.mkdir();b.publish_new_files([(out/'decisions.json',b.encode(ds)),(out/'proposals.json',held[1].content),(out/'evidence.json',b.encode(es)),(out/'review-binding.json',b.encode(receipt))],verify);verify();print(json.dumps({'cases':188,'proposals':117,'review_metadata_updates':receipt['metadata_updates']}))
if __name__=='__main__':main()
