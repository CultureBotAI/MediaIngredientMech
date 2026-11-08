from pathlib import Path
import json,sys,hashlib,datetime
R=Path('reports/all_unmatched_20261107/worker-08');I=R/'successors/issue-1227-v1/research/inorganic_forms';O=R/'successors/issue-1227-v1/independent-review/inorganic_forms';D=json.loads((I/'decisions.json').read_text());seen={}
lo,hi=map(int,sys.argv[1:])
for n,d in list(enumerate(D))[lo:hi]:
 print('\nCASE',n,d['case_id'])
 for c in d['occurrence_context']:
  print(c['source_file'],c.get('component_path'),c.get('native_scope'))
  for k,v in c.items():
   if k in ['source_file','component_path','native_scope','occurrence_id']:continue
   v=json.dumps(v,ensure_ascii=False)
   if v in seen:print(k,'identical to',seen[v])
   else:print(k,v);seen[v]=[n,c['occurrence_id'],k]
with (O/'read-log.jsonl').open('a') as f:f.write(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'path':str(I/'decisions.json'),'sha256':hashlib.sha256((I/'decisions.json').read_bytes()).hexdigest(),'scope':f'Every complete frozen occurrence context for cases {lo}:{hi}; repeated identical fields displayed once then exact reference; occurrence IDs bound in input'})+'\n')
