from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
B=Path('reports/all_unmatched_20261107/worker-05');P=B/'final-correction-v1';S=Path('.temp/w05-postseal-source-corrections-v1');R=S/'review';C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def j(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def os(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def rows(p,k):
 d=j(p);return d if isinstance(d,list) else d[k]
oldD=rows(P/'core/decisions.json','decisions');oldP=rows(P/'core/proposals.json','proposals');ds={d['case_id']:d for d in oldD};ps={p['proposal_id']:p for p in oldP};members={};shards=[]
for p in sorted((C/'shards').glob('shard-*.json')):
 s=j(p);ids=[x['case_id'] for x in s['cases']];assert len(ids)==len(set(ids));shards.append({'path':str(p),'sha256':sha(p),'case_count':len(ids)})
 for x in s['cases']:assert x['case_id'] not in members;members[x['case_id']]=p.name
frozen={x['case_id']:x for x in j(C/'shards/shard-05.json')['cases']};assert set(ds)==set(frozen)
for d in oldD:assert os(frozen[d['case_id']])==d['case_input_sha256'];assert members[d['case_id']]=='shard-05.json'
newD=[];newP=[]
for lane in ['media','materials','chemicals']:
 newD+=rows(S/lane/'decisions.json','decisions');newP+=rows(S/lane/'proposals.json','proposals')
assert len({d['case_id'] for d in newD})==len(newD);assert len({p['proposal_id'] for p in newP})==len(newP)
casebindings=[]
for d in newD:
 o=ds[d['case_id']]
 for k in ['case_input_sha256','source','occurrence_ids','owner_records','preserved_source_holds','disposition','proposal_ids']:
  assert d.get(k)==o.get(k),(d['case_id'],k)
 casebindings.append({'case_id':d['case_id'],'raw_case_sha256':os(frozen[d['case_id']]),'predecessor_decision_object_sha256':os(o),'new_fragment_decision_object_sha256':os(d),'source_fields_and_hold_objects_unchanged':True})
newps={p['proposal_id']:p for p in newP};pb=[]
for p in oldP:
 before=B/p['after_capture']['path'];assert sha(before)==p['after_capture']['sha256'];n=newps.get(p['proposal_id']);after=(S/Path(n['after_capture']['path']).relative_to('postseal-source-corrections-v1')) if n else before
 if n:
  for k in ['proposal_id','case_ids','owner_path','kind','before_sha256']:assert n[k]==p[k],(p['proposal_id'],k)
  assert sha(after)==n['after_capture']['sha256']
 pb.append({'proposal_id':p['proposal_id'],'prior_capture':p['after_capture'],'selected_capture':n['after_capture'] if n else p['after_capture'],'payload_changed':sha(before)!=sha(after),'original_owner_guard':p.get('before_sha256'),'case_ids':p['case_ids']})
out={'reviewer':'/root/final_skeptical','at':datetime.now(timezone.utc).isoformat(),'status':'PASS','scope':'Mechanical frozen ownership and exact scientific-payload lineage before final root metadata assembly; not a new scientific assessment of all historical cases.','counts':{'campaign_unique_cases':len(members),'worker05_cases':len(oldD),'prior_proposals':len(oldP),'changed_decisions':len(newD),'changed_payloads':sum(x['payload_changed'] for x in pb),'unchanged_selected_payloads':sum(not x['payload_changed'] for x in pb)},'shards':shards,'case_bindings':casebindings,'all_prior_and_selected_payload_bindings':pb,'historical_core_bytes':[{'path':str(p),'sha256':sha(p)} for p in [P/'core/decisions.json',P/'core/proposals.json',P/'core/evidence.json']],'limits':['Final compiled core hashes and saved native review are root-owned later outputs.','Unchanged full payloads retain prior source/owner/export limits and actual prior scientific authorship; exact hashes alone do not confer chemical approval.']}
p=R/'postseal-lineage-mechanical-v1.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(out['counts']);print(sha(p))
