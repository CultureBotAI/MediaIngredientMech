"""Bind actual independent review to seven complete candidates and one full case.
Only review metadata changes after scientific review; every raw input is pinned.
"""
from copy import deepcopy
from datetime import datetime,timezone
import json
from pathlib import Path
import build_successor_v2 as b
R=b.R;S=R/'review-input-v1'
def require_reviewer(row):
 if row['reviewer']!='/root/final_reviewer' or row['authorship_conflict'] is not False or row['status']!='approve_bounded_correction' or not row['reasoning'].strip() or row.get('full_owner_or_release_approval') is not False:raise ValueError('Invalid reviewer or approval scope')
 if any(x.removeprefix('worker02 ').strip()=='/root/final_reviewer' for x in row.get('original_authors',[])):raise ValueError('Author cannot independently approve')
def validate_raw_context(contents,proof):
 pins=b.unique(proof['input_hash_manifest'],'path')
 for name,raw in zip(['decisions','proposals','evidence'],contents,strict=True):
  path=str((S/(name+'.json')).absolute())
  if path not in pins:raise ValueError('Missing raw context pin')
  b.require_pin(raw,pins[path]['sha256'])
def validate(doc,props,proof):
 pins=b.unique(proof['input_hash_manifest'],'path')
 for name,value in [('decisions',doc),('proposals',props)]:
  path=str((S/(name+'.json')).absolute())
  if path not in pins:raise ValueError('Missing full context proof')
  b.require_pin(b.encode(value),pins[path]['sha256'])
 dc=b.unique(doc['decisions'],'case_id');pc=b.unique(props['proposals'],'proposal_id');cr=b.unique(proof['case_reviews'],'case_id');pr=b.unique(proof['proposal_reviews'],'proposal_id')
 if len(dc)!=188 or len(pc)!=117 or set(cr)!={b.CID} or set(pr)!=set(b.TARGET_IDS):raise ValueError('Incomplete or unexpected proof scope')
 if len(dc[b.CID]['occurrence_ids'])!=24:raise ValueError('Incomplete source-case context')
 for key,row in cr.items():
  if row['decision_canonical_sha256']!=b.digest(dc[key]) or row['case_input_sha256']!=dc[key]['case_input_sha256']:raise ValueError('Stale case proof')
  require_reviewer(row)
 for key,row in pr.items():
  if row['proposal_canonical_sha256']!=b.digest(pc[key]) or row['after_capture']!=pc[key]['after_capture']:raise ValueError('Stale complete payload proof')
  require_reviewer(row)
 return cr,pr
def main():
 out=b.require_output(R/'selected-v1');proof_path=R/'independent/scientific-review-v1.json'
 held=[b.FrozenFile.capture(S/(n+'.json')) for n in ['decisions','proposals','evidence']]+[b.FrozenFile.capture(proof_path)]
 ds,ps,es,proof=[json.loads(x.content) for x in held]
 validate_raw_context([x.content for x in held[:3]],proof);validate(ds,ps,proof)
 for p in ps['proposals']:
  f=b.FrozenFile.capture(b.A/p['after_capture']['path']);held.append(f);b.require_pin(f.content,p['after_capture']['sha256'])
 def verify():
  for f in held:f.verify()
  for row in proof['input_hash_manifest']:
   path=Path(row['path']);path=path if path.is_absolute() else b.W/path
   b.require_pin(path.read_bytes(),row['sha256'])
 verify();original=deepcopy(ds);eid='w02-seven-preparations-independent-exact-review-v1';cases=[]
 for i,d in enumerate(ds['decisions']):
  if i==b.CASE_INDEX:d['independent_review']={'status':'complete','evidence_ids':[eid]}
  left=deepcopy(original['decisions'][i]);right=deepcopy(d);left.pop('independent_review');right.pop('independent_review');assert left==right
  cases.append({'case_id':d['case_id'],'reviewed_input_sha256':b.digest(original['decisions'][i]),'selected_sha256':b.digest(d),'metadata_only_change':d!=original['decisions'][i]})
 oldraw=b.raw_array_objects(held[0].content,'decisions');newraw=b.raw_array_objects(b.encode(ds),'decisions');assert all(oldraw[i]==newraw[i] for i in range(188) if i!=b.CASE_INDEX)
 es['evidence'].append({'evidence_id':eid,'kind':'independent_review','capture':{'root':'artifact','path':str(proof_path.relative_to(b.A)),'sha256':b.sha(proof_path)},'url':None,'locator':'One complete case58 retaining all24 occurrences; seven complete changed preparation payloads; author-independent bounded category review','supports_or_contradicts':'Supports seven exact OTHER category corrections and truthful history only. Other source dispositions and110payloads inherit predecessor scopes by exact hashes. No component, identity, owner, role or release hold cleared.'})
 receipt={'bound_at':datetime.now(timezone.utc).isoformat(),'author':'worker02 /root','reviewer':'/root/final_reviewer','proof_sha256':b.sha(proof_path),'case_bindings':cases,'metadata_updates':sum(x['metadata_only_change'] for x in cases),'proposal_ledger_sha256_unchanged':b.sha(S/'proposals.json'),'all117payload_bytes_unchanged_from_independent_input':True,'all_proof_input_hashes_verified':len(proof['input_hash_manifest']),'scope':'Only case58 independent_review completion metadata changed. All24 occurrences, source/hold fields and all117 full payloads are exact independently observed bytes. Seven category changes only;110 payloads inherit prior review scopes.'}
 out.mkdir();b.publish_new_files([(out/'decisions.json',b.encode(ds)),(out/'proposals.json',held[1].content),(out/'evidence.json',b.encode(es)),(out/'review-binding.json',b.encode(receipt))],verify);verify()
 print(json.dumps({'cases':188,'proposals':117,'whole_case58_occurrences':24,'review_metadata_updates':receipt['metadata_updates']}))
if __name__=='__main__':main()
