"""Read all frozen shards for owner overlap; never adopt another worker's proposal."""
import datetime, hashlib, json, re
from pathlib import Path
S=Path(__file__).resolve().parents[1]; W=S.parents[1]
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
Q=C/'queue/preliminary-v5'; sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ps=json.loads((S/'proposals.json').read_text())['proposals']; owners={p['owner_path']:p for p in ps}
shards=[]; overlaps=[]; candidates=[]
patterns={
 'CMRL':r'cmrl', 'catalase':r'catalase', 'V8':r'v.?8|vegetable juice',
 'magnesium_citrate':r'magnesium citrate', 'citrate_trihydrate':r'trisodium citrate x 3 h2o',
 'seawater':r'sea.?water', 'Wilkins_Chalgren':r'wilkins', 'Columbia_agar':r'columbia.*agar',
}
for p in sorted((Q/'shards').glob('shard-*.json')):
 d=json.loads(p.read_text());slot=d['worker_slot'];shards.append({'path':str(p),'sha256':sha(p)})
 if slot==4:continue
 for c in d['cases']:
  base={'worker_slot':slot,'case_id':c['case_id'],'source_case_id':c['source_case_id'],'raw_source_label':c['raw_source_label']}
  for o in (c.get('original_kg_entry') or {}).get('owners',[]):
   if o['path'] in owners:
    proposal=owners[o['path']];overlaps.append(dict(base,owner_path=o['path'],proposal_id=proposal['proposal_id'],worker04_before_sha256=proposal['before_sha256'],other_frozen_owner_sha256=o['sha256'],meaning='Same frozen owner occurs in another assignment. This is not evidence of that worker proposing a change or accepting our identity.'))
  for family,pattern in patterns.items():
   if re.search(pattern,c['raw_source_label'] or '',re.I):
    candidates.append(dict(base,family=family,source_record=(c.get('original_kg_entry') or {}).get('source_record'),meaning='Candidate coordination dependency from frozen source context; no equivalence or other-shard review claimed.'))
specific=[
 {'family':'CMRL','decision':'Worker04 case36 names Gibco042-1545; worker07 ingredient1680 explicitly has the same catalogue/10x/glutamine attribute and existing CMRL_1066 owner. Reconcile that owner using original bytes; no duplicate product owner. Worker05 CMRL/ATCC cases and worker04 case0 still need source applicability/version checks.'},
 {'family':'citrate_trihydrate','decision':'Worker04 cases60/150 reuse UNMAPPED_0852; worker07 source case has the same frozen owner. Coordinator must reconcile actual reviewed deltas and preserve every source case.'},
 {'family':'catalase','decision':'Worker04 C9322 supplied-form delta shares the generic Catalase owner with possible worker05 C-10 work; do not infer catalogue equivalence or restore the #312 excluded human-protein example.'},
 {'family':'V8','decision':'Worker04 NBRC15 treated clarified supernatant is a processing output; worker03 cannedV8 is a starting product. Do not merge the treated output into untreated juice or use starting amounts as retained constituents.'},
 {'family':'magnesium_citrate','decision':'Worker04 ingredient404 source-specific1:1 interpretation and worker07 generic magnesium citrate must not resolve broad-label3:2/1:1 ambiguity globally; issue1190 and source-specific holds persist.'},
 {'family':'seawater','decision':'Other-shard artificial/natural seawater labels do not select the preparation or prove equivalence to worker04 named/treated seawaters.'},
 {'family':'Wilkins_Chalgren','decision':'Prepared agar plates, dehydrated agar and anaerobe broth remain distinct preparation states; compare exact product/form before integration.'},
 {'family':'Columbia_agar','decision':'BD BBL5% sheep-blood prepared agar is not automatically equivalent to Columbia dry base or unspecified Columbia blood agar.'},
]
out={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'frozen_shard_inputs':shards,'same_owner_dependencies':overlaps,'source_context_candidates':candidates,'specific_coordination':specific,'rule':'Coordinator compares actual independently reviewed proposals against common original before hashes; no winner selected, external shard output adopted, global alias approved or hold lifted.','predecessor_ledger_preserved':{'path':str(W/'cross-shard-owner-conflicts.json'),'sha256':sha(W/'cross-shard-owner-conflicts.json')}}
(S/'cross-shard-dependencies.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'same_owner_dependencies':len(overlaps),'source_context_candidates':len(candidates)},indent=2))
