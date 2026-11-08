"""Bounded free OLS ontology clarification; no authentication or provider credits."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import datetime,hashlib,json,time,urllib.request,urllib.error
D=Path(__file__).resolve().parent;O=D/'fresh-primary';O.mkdir()
base='https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_03315306'
jobs=[('foodon-parents.json',base+'/parents'),('foodon-ancestors.json',base+'/ancestors'),('peptone-search.json','https://www.ebi.ac.uk/ols4/api/search?q=peptone&ontology=chebi%2Cmicro%2Cfoodon&rows=50&exact=false')]
def get(job):
 n,url=job;r={'url':url,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'GET','no_authentication':True};req=urllib.request.Request(url,headers={'Accept':'application/json','User-Agent':'MediaIngredientMech-source-review/1.0'})
 try:
  with urllib.request.urlopen(req,timeout=30) as x:b=x.read();r.update(status=x.status,final_url=x.url,headers=dict(x.headers))
 except urllib.error.HTTPError as x:b=x.read();r.update(status=x.code,error=str(x),headers=dict(x.headers))
 except Exception as x:b=b'';r.update(status=None,error=repr(x))
 with (O/n).open('xb') as f:f.write(b)
 r.update(finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),path=str((O/n).relative_to(D)))
 with (O/(n+'.receipt.json')).open('x') as f:json.dump(r,f,indent=2);f.write('\n')
 return r
with ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(get,jobs))
with (D/'fresh-primary-receipts.json').open('x') as f:json.dump(results,f,indent=2);f.write('\n')
print(json.dumps([{k:r.get(k) for k in ['url','status','sha256','bytes','error']} for r in results],indent=2))
