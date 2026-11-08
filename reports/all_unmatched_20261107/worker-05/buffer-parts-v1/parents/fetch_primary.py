from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,urllib.request,urllib.error

S=Path(__file__).resolve().parent;O=S/'captures';O.mkdir(exist_ok=True,parents=True)
queries={
 'micro181':'https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?obo_id=MICRO:0000181',
 'micro178':'https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?obo_id=MICRO:0000178',
 'micro172':'https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?obo_id=MICRO:0000172',
 'foodon15306':'https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON:03315306',
 'foodon15720':'https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON:03315720',
 'mediadive75':'https://mediadive.dsmz.de/rest/ingredient/75',
 'micro-peptone-search':'https://www.ebi.ac.uk/ols4/api/search?q=peptone&ontology=micro&rows=100',
 'foodon-peptone-search':'https://www.ebi.ac.uk/ols4/api/search?q=peptone&ontology=foodon&rows=100',
}
def fetch(item):
 name,url=item;dest=O/(name+'.json');receipt=O/(name+'.receipt.json');assert not dest.exists() and not receipt.exists()
 at=datetime.now(timezone.utc).isoformat();result=dict(url=url,accessed_at=at,author='/root/buffer_hepes',provider='Free public primary endpoint',path=dest.name)
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'MediaIngredientMech source review','Accept':'application/json'})
  with urllib.request.urlopen(req,timeout=45) as r:body=r.read();result.update(http_status=r.status,final_url=r.geturl(),content_type=r.headers.get('Content-Type'))
 except urllib.error.HTTPError as e:body=e.read();result.update(http_status=e.code,error=str(e))
 except Exception as e:body=str(e).encode();result.update(error=repr(e),http_status=None)
 dest.write_bytes(body);result.update(sha256=hashlib.sha256(body).hexdigest(),bytes=len(body));receipt.write_text(json.dumps(result,indent=2)+'\n');return result
results=list(ThreadPoolExecutor(max_workers=4).map(fetch,queries.items()));out=S/'capture-index.json';assert not out.exists();out.write_text(json.dumps(results,indent=2)+'\n');print(json.dumps([{'name':x['path'],'status':x.get('http_status'),'bytes':x['bytes'],'sha256':x['sha256']} for x in results]))
