from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,urllib.request,urllib.error
S=Path(__file__).resolve().parent;O=S/'captures'
queries={
 'chebi749541':'https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:749541',
 'micro172-descendants':'https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMICRO_0000172/descendants?size=1000',
 'chebi-peptone-search':'https://www.ebi.ac.uk/ols4/api/search?q=peptone&ontology=chebi&rows=100'
}

def fetch(item):
 name,url=item;dest=O/(name+'.json');receipt=O/(name+'.receipt.json');assert not dest.exists() and not receipt.exists()
 result=dict(url=url,accessed_at=datetime.now(timezone.utc).isoformat(),author='/root/buffer_hepes',provider='Free public primary ontology endpoint',path=dest.name)
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'MediaIngredientMech source review','Accept':'application/json'}),timeout=45) as r:body=r.read();result.update(http_status=r.status,final_url=r.geturl(),content_type=r.headers.get('Content-Type'))
 except urllib.error.HTTPError as e:body=e.read();result.update(http_status=e.code,error=str(e))
 except Exception as e:body=str(e).encode();result.update(http_status=None,error=repr(e))
 dest.write_bytes(body);result.update(sha256=hashlib.sha256(body).hexdigest(),bytes=len(body));receipt.write_text(json.dumps(result,indent=2)+'\n');return result
results=list(ThreadPoolExecutor(max_workers=4).map(fetch,queries.items()));(S/'adaptive-capture-index.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps([{'name':x['path'],'status':x['http_status'],'bytes':x['bytes']} for x in results]))
