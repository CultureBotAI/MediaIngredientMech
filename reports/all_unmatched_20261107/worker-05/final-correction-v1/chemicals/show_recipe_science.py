from pathlib import Path
import json,sys,re
V=json.loads((Path(__file__).parent/'full-frozen-recipes-read-view.json').read_text())
def walk(x,path=''):
 if isinstance(x,dict):
  if 'preferred_term' in x:print(path,x['preferred_term'],':'.join(str(x.get('concentration',{}).get(k,'')) for k in ['value','unit']),re.sub(r'^(?:Role:.*?; )?Properties:[^\n]*','',x.get('notes','')))
  for k,v in x.items():
   if k in ['preparation','preparation_steps','protocol','description','stock_preparation','final_ph','ph','notes'] and 'preferred_term' not in x: print(path+'/'+k,json.dumps(v,ensure_ascii=False))
   if k in ['ingredients','composition','solutions','medium','solution','steps']:walk(v,path+'/'+k)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,path+'/'+str(i))
for i in range(int(sys.argv[1]),int(sys.argv[2])):
 print('RECIPE',i,V[i]['path'].split('/')[-1],V[i]['record'].get('name'));walk(V[i]['record'])
