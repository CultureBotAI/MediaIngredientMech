from concurrent.futures import ThreadPoolExecutor
import datetime,hashlib,json
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode
ROOT=Path(__file__).resolve().parent/'sources'
queries={
 'ncit-C61946.json':'https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C61946?include=full',
 'chebi-parent.json':'https://www.ebi.ac.uk/chebi/backend/api/public/compound/34683/',
 'pubchem-517013-properties.json':'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/517013/property/MolecularFormula,MolecularWeight,InChI,InChIKey/JSON',
}
for tag,q in [('heptahydrate','heptahydrate'),('hydrogenphosphate','hydrogenphosphate'),('phosphate','sodium phosphate')]:
 queries[f'ols-chebi-{tag}.json']='https://www.ebi.ac.uk/ols4/api/search?'+urlencode({'q':q,'ontology':'chebi','rows':'500','exact':'false'})
queries['ols-ncit-heptahydrate.json']='https://www.ebi.ac.uk/ols4/api/search?'+urlencode({'q':'heptahydrate','ontology':'ncit','rows':'100'})
def fetch(item):
 name,url=item;stamp=datetime.datetime.now(datetime.timezone.utc).isoformat();status=None;error=None;headers={}
 try:
  with urlopen(Request(url,headers={'User-Agent':'MediaIngredientMech scientific record audit','Accept':'application/json,text/html'}),timeout=45) as r:status=r.status;body=r.read();headers=dict(r.headers)
 except HTTPError as e:status=e.code;body=e.read();error=str(e);headers=dict(e.headers)
 except Exception as e:body=str(e).encode();error=str(e)
 (ROOT/name).write_bytes(body)
 return {'file':name,'url':url,'retrieved_at':stamp,'status':status,'error':error,'sha256':hashlib.sha256(body).hexdigest(),'bytes':len(body),'headers':headers}
with ThreadPoolExecutor(max_workers=5) as pool:results=list(pool.map(fetch,queries.items()))
(ROOT/'exact-terms-fetch-manifest.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps([{k:r[k] for k in ['file','status','error','bytes']} for r in results],indent=2))
