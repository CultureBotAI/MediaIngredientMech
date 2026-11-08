from pathlib import Path
import csv, hashlib, io, json, shutil, zipfile
from datetime import datetime, timezone

W=Path.cwd(); C=W.parents[2]; S=W/'.temp/w05-buffer-parts-v1/dependencies'
V=C/'workers/w03/worktree/.temp/peptone-consumer-independent-v1'
B=W/'reports/all_unmatched_20261107/worker-05'
now=datetime.now(timezone.utc).isoformat()
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,o):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def cp(src,dst):
 dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst);assert h(src)==h(dst)

assert h(V/'HANDOFF.json')=='3733050169d1406798da748f4df5168015ea164bdc2cfe58afd86f09d4ae23aa'
assert h(V/'MANIFEST.json')=='f7df69ec006bf1bc2c344d12404c39385e04e8db2bc7050ce0c216cc610e52c2'
m=json.loads((V/'MANIFEST.json').read_text()); manifest=[]
for row in m['members']:
 p=V/row['path'];assert h(p)==row['sha256'],p
 cp(p,S/'inputs/w03-peer'/row['path']);manifest.append(row)
cp(V/'MANIFEST.json',S/'inputs/w03-peer/MANIFEST.json')
for folder in ['final-component-dependency-plan-v1','final-component-dependency-plan-v2','w05-consolidated-remaining-work-v1']:
 for p in sorted((C/'preflight'/folder).rglob('*')):
  if p.is_file(): cp(p,S/'inputs'/folder/p.relative_to(C/'preflight'/folder))
for name in ['comment6719248666.json','comment6719468092.json','remaining-capture-receipt.json']:
 cp(W/'.temp/w05-buffer-parts-v1/issues'/name,S/'inputs/issues'/name)
for p in ['MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','.claude/skills/add-media/SKILL.md','.claude/skills/curate-yaml-record/SKILL.md','docs/record-reviews.md','docs/record-review-profile.md']:
 cp(W/p,S/'inputs/contracts'/p)
for p in ['decisions.json','proposals.json','evidence.json']:
 cp(B/'tellurium-polypeptone-v1/core'/p,S/'inputs/current-core'/p)
ledger=json.loads((V/'machine-ledger.json').read_text())['rows']
owned=[r for r in ledger if r['target_id'] not in ['PC02','PC04','PC05','PC14','PC20']]
assert len(owned)==15
ps=json.loads((B/'tellurium-polypeptone-v1/core/proposals.json').read_text())['proposals']
bind=[]
for r in owned:
 b=r['beforeimage_binding'];op=b['owner_path'];p=W/op;assert h(p)==b['before_sha256'],op
 cp(p,S/'before'/Path(op).name)
 matches=[x for x in ps if x.get('owner_path')==op]
 assert len(matches)==(1 if r['target_id'] in ['PC01','PC08','PC15'] else 0)
 selected=p
 if matches:
  a=matches[0]['after_capture'];selected=B/a['path'];assert h(selected)==a['sha256'];cp(selected,S/'selected-before'/Path(op).name)
 bind.append({'target_id':r['target_id'],'owner_path':op,'before_sha256':h(p),'selected_before_path':str(selected.relative_to(W)),'selected_before_sha256':h(selected),'current_proposal':matches[0] if matches else None,'component_index':b['component_index']})
cp(W/'data/ingredients/mapped/GYPS.yaml',S/'negative-controls/GYPS.yaml')
z=zipfile.ZipFile(V/'other/captures/microbedecoder_database.zip');raw=z.read('database.csv');assert hashlib.sha256(raw).hexdigest()=='0c6ff730a108720a5d6972400f2bccf2eca8621713b62736abdf5df0fb188c95'
records=list(csv.DictReader(io.StringIO(raw.decode('latin-1'))))
observations=[]
for r in owned:
 a=r['primary_assessment'];obs=a.get('original_observations',a.get('source_observations'))
 for o in obs:
  row=records[o['record_index_zero_based']]
  assert row[o['field']]==o['literal'],(r['target_id'],o)
  assert row['Genus']==o['genus'] and row['Species']==o['species']
  for k,v in o['source_links'].items():assert row[k]==v
  observations.append({'target_id':r['target_id'],**o,'complete_database_row':row})
put(S/'source-observations.json',{'author':'/root/buffer_tris','reextracted_at':now,'archive_sha256':h(V/'other/captures/microbedecoder_database.zip'),'member':'database.csv','member_sha256':hashlib.sha256(raw).hexdigest(),'archive_acquired_at':None,'timestamp_limitation':'Original acquisition timestamp unavailable in inspected prior metadata; current re-extraction time is not acquisition time. Original zip member timestamp retained as packaging metadata only.','zip_member_timestamp':z.getinfo('database.csv').date_time,'encoding':'latin-1 (lossless byte mapping)','rows':observations,'scope':'Source observations only; no claim underlying complete source papers have all been read.'})
put(S/'input-bindings.json',{'at':now,'base_head':'0bac12cabfd1f67f212631d8eef9aa46379f6b41','prior_peer_manifest_members_verified':len(manifest),'prior_peer_manifest_sha256':h(V/'MANIFEST.json'),'targets':bind,'source_observation_count':len(observations),'prior_scientists':['/root/peptone_ambiguous_sources','/root/peptone_other_sources'],'prior_skeptic':'/root/peptone_skeptic','successor_author':'/root/buffer_tris','successor_skeptic':'pending root-assigned independent review','unrelated_context_targets':['PC02','PC04','PC05','PC14','PC20']})
print(json.dumps({'targets':len(bind),'observations':len(observations),'prior_members':len(manifest),'input_bindings_sha256':h(S/'input-bindings.json')}))
