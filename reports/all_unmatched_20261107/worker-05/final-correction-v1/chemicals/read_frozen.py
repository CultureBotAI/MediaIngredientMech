from pathlib import Path
import json,yaml,hashlib
O=Path(__file__).resolve().parent;Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
D=json.loads((O/'input-decisions.json').read_text());C={c['case_id']:c for c in json.loads((Q/'shards/shard-05.json').read_text())['cases']}
def sh(b):return hashlib.sha256(b).hexdigest()
seen={};V=[]
for i,d in enumerate(D):
 c=C[d['case_id']]
 for o in c.get('occurrences',[]):
  r=o['full_recipe_snapshot'];p=Q/r;b=p.read_bytes();assert sh(b)==o['source_file_sha256'];y=yaml.safe_load(b)
  if r not in seen:seen[r]=len(V);V.append({'case_indices':[i],'path':r,'sha256':sh(b),'record':y})
  elif i not in V[seen[r]]['case_indices']:V[seen[r]]['case_indices'].append(i)
(O/'full-frozen-recipes-read-view.json').write_text(json.dumps(V,ensure_ascii=False,indent=2)+'\n')
print('complete snapshots',len(V),'bytes',sum(len((Q/v['path']).read_bytes()) for v in V))
