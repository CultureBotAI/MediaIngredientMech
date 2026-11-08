"""Discover frozen cross-shard owner hints without editing any shard or owner."""
from pathlib import Path
import json,hashlib,datetime,re
R=Path.cwd();O=R/'reports/all_unmatched_20261107/worker-05';Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
D=[d for n in ['root','media','materials','chemicals'] for d in json.loads((O/n/'decisions.json').read_text())['decisions']]
P=[p for n in ['root','media','materials','chemicals'] for p in json.loads((O/n/'proposals.json').read_text())['proposals']]
refsets={}
for d in D:
 for o in d['owner_records']:refsets.setdefault(o['path'],set()).add(o['sha256'])
assert all(len(v)==1 for v in refsets.values()), 'Conflicting before-owner hashes'
refs={p:next(iter(hs)) for p,hs in refsets.items()};pby={p['owner_path']:p['proposal_id'] for p in P}
def walk(x):
 if isinstance(x,dict):
  for v in x.values():yield from walk(v)
 elif isinstance(x,list):
  for v in x:yield from walk(v)
 elif isinstance(x,str) and re.fullmatch(r'data/ingredients/(?:mapped|unmapped)/[^/]+\.yaml',x):
  yield x
hints={}
for sp in sorted((Q/'shards').glob('shard-*.json')):
 s=json.loads(sp.read_text())
 for c in s['cases']:
  for op in set(walk(c)):
   if op in refs:hints.setdefault(op,[]).append({'worker_slot':s['worker_slot'],'case_id':c['case_id'],'source_label':c['source_label']})
dep=[]
for op,sha in refs.items():
 outside=[x for x in hints.get(op,[]) if x['worker_slot']!=5]
 if outside:dep.append({'owner_path':op,'before_sha256':sha,'worker05_proposal_id':pby.get(op),'other_frozen_case_hints':outside,'action':'Coordinator must inspect actual other-worker proposed paths, reconcile exact changed-owner payload and preserve all source-specific holds; hint alone is not an edit or ownership approval.'})
receipt={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'referenced_owner_count':len(refs),'proposed_owner_count':len(pby),'frozen_hint_cross_shard_dependencies':dep,'known_explicit_dependency':{'owner_path':'data/ingredients/mapped/Thiamine_pyrophosphate.yaml','workers':[5,9],'source':'contracts/thiamine-coordinator-context-v1.json','requirements':'Preserve exact9532 WITHHOLD and CAS136-09-4; reject chloride-specific carryover only with source evidence. Distinct0.2%stock andJCM403stock are separate. No shared writes.'},'limitations':'Search of all10 immutable shards includes ignored input files via explicit paths. These frozen source hints are not a complete proposed-owner inventory: source-only cases can expose other owners. Coordinator must compare every worker proposals.json before integration.'}
(O/'cross-shard-dependencies.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n');print('referenced',len(refs),'proposed',len(pby),'shared hints',len(dep))
