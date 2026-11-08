from pathlib import Path
import json,yaml,hashlib,datetime,collections,copy
A=Path('reports/all_unmatched_20261107/worker-07');N=A/'successors/issues1226-1237-v1';S=Path('.temp/worker07-issues1226-1237-v1/skeptic')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def csha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def read(p):return json.loads(p.read_text())
def diff(a,b,p=''):
 if type(a)!=type(b):return [{'path':p,'before':a,'after':b}]
 if isinstance(a,dict):return sum([diff(a[k],b[k],p+'/'+k) if k in a and k in b else [{'path':p+'/'+k,'before':a.get(k),'after':b.get(k),'op':'added' if k not in a else 'removed'}] for k in sorted(a.keys()|b.keys())],[])
 if isinstance(a,list):
  if len(a)!=len(b):return [{'path':p,'before':a,'after':b}]
  return sum([diff(x,y,p+'/'+str(i)) for i,(x,y) in enumerate(zip(a,b))],[])
 return [] if a==b else [{'path':p,'before':a,'after':b}]
OP={r['proposal_id']:r for r in read(A/'successors/issue1203-v1/proposals.json')['proposals']};NP={r['proposal_id']:r for r in read(N/'draft-v1/proposals.json')['proposals']};assert OP.keys()==NP.keys()
M={r['proposal_id']:r for r in read(N/'mutation-ledger.json')['changed_payloads']};ALLOW=collections.defaultdict(list)
for r in read(S/'independent-provenance-recomputation-v1.json')['rows']:ALLOW[r['proposal_id']].append(r)
rows=[];changed=0;unchanged=0;mutations=0
for pid,oldp in OP.items():
 newp=NP[pid];oldpath=A/oldp['after_capture']['path'];newpath=A/newp['after_capture']['path'];old=yaml.safe_load(oldpath.read_text());new=yaml.safe_load(newpath.read_text());assert sha(oldpath)==oldp['after_capture']['sha256'];assert sha(newpath)==newp['after_capture']['sha256'];ds=diff(old,new);propdiff=diff(oldp,newp)
 if ds:
  changed+=1;assert pid in M;assert oldpath.read_bytes()==(A/M[pid]['before']['path']).read_bytes();assert newpath.read_bytes()==(A/M[pid]['after']['path']).read_bytes();h=old.get('curation_history',[]);hn=new.get('curation_history',[]);assert hn[:-1]==h;assert len(hn)==len(h)+1;assert hn[-1]==M[pid]['history_appended'];assert hn[-1]['llm_assisted'] is True
  meta_expected=set()
  for e in ALLOW[pid]:
   i=int(e['pointer'].split('/')[-1]);bef=old['ontology_mapping']['evidence'][i];aft=new['ontology_mapping']['evidence'][i];assert bef==e['complete_object'];exp=copy.deepcopy(bef);exp['evidence_type']='LLM_SUGGESTION';assert aft==exp;meta_expected.add(e['pointer']+'/evidence_type');mutations+=1
  metadata_diffs={d['path'] for d in ds if d['path'].startswith('/ontology_mapping/evidence/')};assert metadata_diffs==meta_expected
  other=[d for d in ds if d['path']!='/curation_history' and d['path'] not in meta_expected];assert bool(other)==bool(M[pid]['science_correction']),(pid,other)
 else:
  unchanged+=1;assert oldpath.read_bytes()==newpath.read_bytes();assert pid not in M;other=[]
 rows.append({'proposal_id':pid,'before_path':str(oldpath),'before_sha256':sha(oldpath),'after_path':str(newpath),'after_sha256':sha(newpath),'all_field_diffs':ds,'science_diffs':other,'proposal_ledger_diffs':propdiff,'changed':bool(ds),'historical_events_preserved':True,'full_payloads_read':True})
OD={d['case_id']:d for d in read(A/'successors/issue1203-v1/decisions.json')['decisions']};ND={d['case_id']:d for d in read(N/'draft-v1/decisions.json')['decisions']};assert OD.keys()==ND.keys();cases=[]
for cid,old in OD.items():
 n=ND[cid];assert all(n[k]==old[k] for k in ['case_id','case_input_sha256','source','occurrence_ids','disposition','proposal_ids','owner_records']);ds=diff(old,n)
 if ds:cases.append({'case_id':cid,'diffs':ds})
OE=read(A/'successors/issue1203-v1/evidence.json')['evidence'];NE=read(N/'draft-v1/evidence.json')['evidence'];assert NE[:len(OE)]==OE;assert len({e['evidence_id'] for e in NE})==len(NE)
out={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/successor1226_1237_skeptic','scope':'Exact full draft objects/diffs and complete metadata assertions, not renewed primary chemical evidence for unchanged fields','counts':{'proposals':len(rows),'changed':changed,'unchanged':unchanged,'metadata_scalars':mutations,'decisions':len(ND),'changed_decisions':len(cases),'evidence':len(NE),'original_evidence_retained':len(OE)},'payload_reviews':rows,'decision_diffs':cases,'added_evidence':NE[len(OE):],'bindings':[{'path':str(p),'sha256':sha(p)} for p in [N/'draft-v1/decisions.json',N/'draft-v1/evidence.json',N/'draft-v1/proposals.json',N/'mutation-ledger.json',N/'retention.json']]}
p=S/'draft-v1-full-diff-review.json';assert not p.exists();p.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(json.dumps(out['counts']));
for r in rows:
 if r['science_diffs']: print(r['proposal_id'],json.dumps(r['science_diffs'],ensure_ascii=False,indent=2))
print('DECISION_DIFFERENCES',json.dumps(cases,indent=2,ensure_ascii=False));print('ADDED_EVIDENCE',json.dumps(NE[len(OE):],indent=2))
