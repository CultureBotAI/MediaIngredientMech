from pathlib import Path
import json,hashlib,sys,yaml
R=Path('reports/all_unmatched_20261107/worker-08');I=R/'successors/issue-1227-v1/research/inorganic_forms';O=R/'successors/issue-1227-v1/independent-review/inorganic_forms';D=json.loads((I/'decisions.json').read_text());p=R/'provenance/shard-08.json';B=json.loads(p.read_text());C={c['case_id']:c for c in B['cases']};seen={};out=[]
def rec(x,loc):
 raw=json.dumps(x,ensure_ascii=False,sort_keys=True)
 if isinstance(x,(str,dict,list)) and len(raw)>100:
  if raw in seen:return {'$identical_previously_displayed':seen[raw]}
  seen[raw]=loc
 if isinstance(x,dict):return {k:rec(v,loc+'/'+k) for k,v in x.items()}
 if isinstance(x,list):return [rec(v,loc+'/'+str(j)) for j,v in enumerate(x)]
 return x
def seed(x,loc):
 raw=json.dumps(x,ensure_ascii=False,sort_keys=True)
 if isinstance(x,(str,dict,list)) and len(raw)>100:seen[raw]=loc
 if isinstance(x,dict):
  for k,v in x.items():seed(v,loc+'/'+k)
 if isinstance(x,list):
  for j,v in enumerate(x):seed(v,loc+'/'+str(j))
for j,d in enumerate(D):
 for k,c in enumerate(d['occurrence_context']):seed(c,'read-final-occurrence-context/'+str(j)+'/'+str(k))
for j,p0 in enumerate(json.loads((I/'proposals.json').read_text())):
 seed(yaml.safe_load((R/p0['after_capture']['path']).read_text()),'read-entire-payload/'+str(j))
 if p0['before_sha256']:seed(yaml.safe_load(Path(p0['owner_path']).read_text()),'read-original-beforeimage/'+str(j))
for j,d in enumerate(D):
 c=C[d['case_id']];out.append({'index':j,'frozen':rec(c,'case'+str(j))})
lo,hi=map(int,sys.argv[1:]);print(json.dumps(out[lo:hi],ensure_ascii=False,separators=(',',':')))
