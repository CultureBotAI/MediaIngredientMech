from pathlib import Path
import json,re
O=Path(__file__).parent
I=json.loads((O/'source-index.json').read_text())
views=[]
for n,v in enumerate(I):
 if not v.get('read_path'):continue
 t=Path(v['read_path']).read_text()
 try:
  j=json.loads(t)
  def clean(x):
   if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in ['properties','roles','gmo','gmo_id']}
   if isinstance(x,list):return [clean(v) for v in x]
   return x
  t=json.dumps(clean(j),ensure_ascii=False,separators=(',',':'))
 except Exception:t=re.sub(r'\n\s*\n+', '\n',t)
 (O/'read'/f'view-{n:03}.txt').write_text(t)
 views.append({'index':n,'length':len(t),'id':v['evidence']['evidence_id'],'url':v['evidence'].get('url'),'kind':v['evidence']['kind']})
(O/'source-view-index.json').write_text(json.dumps(views,indent=2)+'\n')
print(json.dumps([v for v in views if v['index']>=428],indent=2))
