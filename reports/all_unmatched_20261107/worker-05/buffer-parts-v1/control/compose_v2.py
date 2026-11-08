"""Compose disjoint author deltas without replacing any original evidence or proposal origin."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,copy,hashlib
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1';B=W/'reports/all_unmatched_20261107/worker-05';O=B/'tellurium-polypeptone-v1';j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();oh=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
a=argparse.ArgumentParser();a.add_argument('--selection',type=Path,required=True);a.add_argument('--out',type=Path,required=True);a=a.parse_args();sel=j(a.selection);out=a.out;assert not out.exists();out.mkdir(parents=True)
base={k:j(O/'core'/f'{k}.json') for k in ['decisions','proposals','evidence','proposal-lineage']};D=copy.deepcopy(base['decisions']);P=copy.deepcopy(base['proposals']);E=copy.deepcopy(base['evidence']);L=copy.deepcopy(base['proposal-lineage']);di={d['case_id']:d for d in D['decisions']};pi={p['proposal_id']:p for p in P['proposals']};ei={e['evidence_id']:e for e in E['evidence']};oldD={d['case_id']:d for d in base['decisions']['decisions']};oldP={p['proposal_id']:p for p in base['proposals']['proposals']};affected={};selectedP={};fragments=[];operations=[]
def union(a,b):
 r=copy.deepcopy(a)
 for x in b:
  if x not in r:r.append(copy.deepcopy(x))
 return r
for lane,files in sel.items():
 for kind,rel in files.items():
  q=W/rel;x=j(q);fragments.append(dict(lane=lane,kind=kind,path=rel,sha256=sha(q)))
  if kind=='decisions':
   for d in x['decisions']:
    cid=d['case_id'];old=oldD[cid];current=di[cid];affected.setdefault(cid,[]).append(lane)
    for k in ['case_id','case_input_sha256','source','occurrence_ids','owner_records','preserved_source_holds','preserved_downstream_holds']:assert d.get(k)==old.get(k),(lane,cid,k)
    for k in set(old)|set(d):
     if d.get(k)==old.get(k):continue
     if k in ['evidence_ids','proposal_ids','issue_refs']:
      assert all(t in d.get(k,[]) for t in old.get(k,[])),(lane,k);current[k]=union(current.get(k,[]),d[k])
     else:
      assert current.get(k)==old.get(k) or current.get(k)==d.get(k),('conflicting edits',cid,k,lane)
      if k in d:current[k]=copy.deepcopy(d[k])
      else:current.pop(k,None)
     operations.append(dict(lane=lane,case_id=cid,field=k,authored_value_sha256=oh(d.get(k))))
  elif kind=='case_deltas':
   for d in x['case_deltas']:
    cid=d['case_id'];current=di[cid];assert current['case_input_sha256']==d['case_input_sha256'];affected.setdefault(cid,[]).append(lane)
    for k in ['proposal_ids','evidence_ids','issue_refs','owner_records']:
     current[k]=union(current.get(k,[]),d.get('union_'+k,[]))
    for k,v in d['set_distinct_field'].items():assert k not in current;current[k]=copy.deepcopy(v)
    operations.append(dict(lane=lane,case_id=cid,delta_object_sha256=oh(d)))
  elif kind=='proposals':
   for p in x['proposals']:
    pid=p['proposal_id'];assert pid not in selectedP,(pid,lane);selectedP[pid]=lane
    if pid in pi:
     old=oldP[pid]
     for k in ['proposal_id','kind','owner_path','before_sha256','case_ids','applies_to_occurrence_ids','destination_owner_path']:assert p.get(k)==old.get(k),(pid,k)
     pi[pid].clear();pi[pid].update(copy.deepcopy(p));lr=next(z for z in L['rows'] if z['proposal_id']==pid);lr['consolidated_predecessor_capture']=copy.deepcopy(lr['successor_after_capture']);lr['successor_after_capture']=copy.deepcopy(p['after_capture'])
    else:
     assert p['kind']=='edit_existing_owner' and sha(W/p['owner_path'])==p['before_sha256'];assert set(p['case_ids'])<=set(di)
     P['proposals'].append(copy.deepcopy(p));pi[pid]=P['proposals'][-1];L['rows'].append(dict(proposal_id=pid,lane=lane,predecessor_proposal_id=None,predecessor_proposal_sha256=None,predecessor_after_capture=None,successor_after_capture=p['after_capture'],owner_path=p['owner_path'],original_before_sha256=p['before_sha256'],case_ids=p['case_ids'],classification='authorized_authentic_dependent_origin',causal_case_is_not_child_recipe_observation=True))
  elif kind=='evidence':
   for e in x['evidence']:
    eid=e['evidence_id']
    if eid in ei:assert e==ei[eid]
    else:E['evidence'].append(copy.deepcopy(e));ei[eid]=E['evidence'][-1]
  else:raise ValueError(kind)
for d in D['decisions']:
 if d['case_id'] not in affected:assert d==oldD[d['case_id']]
for p in P['proposals']:
 cap=p['after_capture'];q=B/cap['path']
 if not q.exists() and cap['path'].startswith('buffer-parts-v1/'):q=S/cap['path'].removeprefix('buffer-parts-v1/')
 assert sha(q)==cap['sha256'],q
L['successor_count']=len(P['proposals']);L['consolidated_predecessor_manifest']=dict(path=str((O/'MANIFEST.json').relative_to(W)),sha256=sha(O/'MANIFEST.json'));L['consolidated_original_lineage_preserved']=True
assert E['evidence'][:len(base['evidence']['evidence'])]==base['evidence']['evidence'];assert len(D['decisions'])==len(oldD)
for n,x in [('decisions',D),('proposals',P),('evidence',E),('proposal-lineage',L)]: (out/f'{n}.json').write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
r=dict(at=datetime.now(timezone.utc).isoformat(),compiler='/root',base_head='0bac12cabfd1f67f212631d8eef9aa46379f6b41',fragments=fragments,operations=operations,case_reviews=[dict(case_id=c,lanes=lanes,selected_decision_object_sha256=oh(di[c])) for c,lanes in affected.items()],payload_reviews=[dict(proposal_id=p,primary_lane=lane,after_capture=pi[p]['after_capture'],new_authentic_origin=p not in oldP,payload_changed=p not in oldP or pi[p]['after_capture']['sha256']!=oldP[p]['after_capture']['sha256']) for p,lane in selectedP.items()],counts=dict(cases=len(D['decisions']),proposals=len(P['proposals']),evidence=len(E['evidence']),original_lineages=L['original_count'],reviewed_cases=len(affected),reviewed_payloads=len(selectedP),new_authentic_origins=sum(p not in oldP for p in selectedP),changed_existing_payloads=sum(p in oldP and pi[p]['after_capture']['sha256']!=oldP[p]['after_capture']['sha256'] for p in selectedP)),scope='Complete current source selector composed from exact author fragments; scientific review pending. Existing source ownership unchanged; child origins are explicitly causal repairs, not new source observations.')
(out/'composition-receipt.json').write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n');print(json.dumps(r['counts']))
