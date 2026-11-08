"""Read-only cross-shard dependency snapshot; no transfer of source-case ownership."""
from pathlib import Path
import json,hashlib,datetime,re,yaml,subprocess
R=Path.cwd();B=R/'reports/all_unmatched_20261107/worker-05';O=B/'correction-1193-v1';CAM=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107');Q=CAM/'queue/preliminary-v5'
D=json.loads((O/'decisions.json').read_text())['decisions'];P=json.loads((O/'proposals.json').read_text())['proposals']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
refsets={}
for d in D:
 for x in d['owner_records']:refsets.setdefault(x['path'],set()).add(x['sha256'])
assert all(len(x)==1 for x in refsets.values()),'Conflicting before hashes for shared owner references'
refs={p:next(iter(h)) for p,h in refsets.items()};pby={p['owner_path']:p for p in P};ids={p['proposal_id']:yaml.safe_load((B/p['after_capture']['path']).read_text())['identifier'] for p in P}
def walk(x):
 if isinstance(x,dict):
  for v in x.values():yield from walk(v)
 elif isinstance(x,list):
  for v in x:yield from walk(v)
 elif isinstance(x,str) and re.fullmatch(r'data/ingredients/(?:mapped|unmapped)/[^/]+\.yaml',x):yield x
hints={};ownership={};shards=[]
for sp in sorted((Q/'shards').glob('shard-*.json')):
 s=json.loads(sp.read_text());shards.append({'worker_slot':s['worker_slot'],'sha256':sha(sp),'case_count':len(s['cases'])})
 for c in s['cases']:
  assert c['case_id'] not in ownership;ownership[c['case_id']]=s['worker_slot']
  for op in set(walk(c)):
   if op in refs:hints.setdefault(op,[]).append({'worker_slot':s['worker_slot'],'case_id':c['case_id'],'source_label':c['source_label']})
assert len(ownership)==1879 and {d['case_id'] for d in D}=={k for k,v in ownership.items() if v==5}
other=[];conflicts=[];missing=[]
for w in range(1,11):
 if w==5:continue
 wt=CAM/'workers'/f'w{w:02d}'/'worktree';ob=wt/'reports/all_unmatched_20261107'/f'worker-{w:02d}';f=ob/'proposals.json'
 if not f.exists():missing.append({'worker_slot':w,'checked_exact_path':str(f),'status':'No canonical top-level proposals file at snapshot time; no claim about other locations/completion.'});continue
 ps=json.loads(f.read_text())['proposals'];rows=[]
 for p in ps:
  cap=p.get('after_capture',{});ap=ob/cap.get('path','');rec={}
  if ap.is_file():
   assert sha(ap)==cap['sha256'];rec=yaml.safe_load(ap.read_text())
  row={'proposal_id':p['proposal_id'],'owner_path':p['owner_path'],'destination_owner_path':p.get('destination_owner_path',p['owner_path']),'before_sha256':p['before_sha256'],'after_capture':cap,'identifier':rec.get('identifier'),'description':p['description']};rows.append(row)
  for ours in P:
   ourpaths={ours['owner_path'].casefold(),ours.get('destination_owner_path',ours['owner_path']).casefold()};theirpaths={p['owner_path'].casefold(),p.get('destination_owner_path',p['owner_path']).casefold()}
   if ourpaths & theirpaths or rec.get('identifier')==ids[ours['proposal_id']]:
    conflicts.append({'worker05_proposal_id':ours['proposal_id'],'worker05_owner_path':ours['owner_path'],'worker05_destination_owner_path':ours.get('destination_owner_path',ours['owner_path']),'worker05_before_sha256':ours['before_sha256'],'other_worker':w,'other_proposal':row,'matching_owner_or_destination_paths':sorted(ourpaths & theirpaths),'matching_proposed_identifier':rec.get('identifier')==ids[ours['proposal_id']],'action':'Coordinator must reconcile exact changed-owner payloads before integration; no winner selected, no shared writes or source-case ownership reassignment.'})
 head=subprocess.run(['git','-C',str(wt),'rev-parse','HEAD'],capture_output=True,text=True)
 other.append({'worker_slot':w,'canonical_proposals_path':str(f),'canonical_proposals_sha256':sha(f),'worktree_head_at_observation':head.stdout.strip() if head.returncode==0 else None,'proposals':rows})
out={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'campaign_source_case_count':len(ownership),'worker05_case_count':len(D),'referenced_owner_count':len(refs),'proposed_owner_count':len(P),'all_frozen_shard_hashes':shards,'frozen_hint_cross_shard_dependencies':[{'owner_path':op,'before_sha256':h,'worker05_proposal_id':pby.get(op,{}).get('proposal_id'),'other_frozen_case_hints':[x for x in hints.get(op,[]) if x['worker_slot']!=5]} for op,h in refs.items() if any(x['worker_slot']!=5 for x in hints.get(op,[]))],'actual_proposal_dependencies':conflicts,'other_worker_snapshot':other,'unavailable_canonical_files':missing,'known_explicit_dependency':{'owner_path':'data/ingredients/mapped/Thiamine_pyrophosphate.yaml','workers':[5,9],'requirements':'Keep exact9532 WITHHOLD, preserve CAS136-09-4 distinct from chloride CAS154-87-0, separate0.2%stock and403bufferedstock, no shared writes.'},'limitations':'Read-only explicit-path search includes ignored files. Other-worker canonical proposal files are mutable snapshots, not scientific approvals. Coordinator must compare all latest final heads and successor manifests; unadvertised successor paths may not be represented here.'}
(O/'cross-shard-dependencies.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print('actual shared owner/identifier proposals',len(conflicts),'frozen hints',len(out['frozen_hint_cross_shard_dependencies']))
