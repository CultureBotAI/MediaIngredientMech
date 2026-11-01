from concurrent.futures import ThreadPoolExecutor
import datetime, hashlib, json
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode
ROOT=Path(__file__).resolve().parent/'sources'
queries={
 'cas-commonchemistry.json':'https://commonchemistry.cas.org/api/detail?cas_rn=7782-85-6',
 'pubchem-properties.json':'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6096963/property/MolecularFormula,MolecularWeight,InChI,InChIKey,CanonicalSMILES/JSON',
 'pubchem-synonyms.json':'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6096963/synonyms/JSON',
 'pubchem-cas-resolve.json':'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/7782-85-6/cids/JSON',
 'fda-unii.html':'https://precision.fda.gov/uniisearch/srs/unii/70WT22SF4B',
}
for tag,q in [('cas','7782-85-6'),('name','disodium hydrogenphosphate heptahydrate'),('salt','sodium phosphate heptahydrate')]:
 queries[f'ols-chebi-{tag}.json']='https://www.ebi.ac.uk/ols4/api/search?'+urlencode({'q':q,'ontology':'chebi','rows':'100','exact':'false'})
queries['ols-all-cas.json']='https://www.ebi.ac.uk/ols4/api/search?'+urlencode({'q':'7782-85-6','rows':'100','exact':'false'})
def fetch(item):
 name,url=item;stamp=datetime.datetime.now(datetime.timezone.utc).isoformat();headers={};status=None;error=None
 try:
  with urlopen(Request(url,headers={'User-Agent':'MediaIngredientMech scientific record audit','Accept':'application/json,text/html'}),timeout=45) as r:status=r.status;body=r.read();headers=dict(r.headers)
 except HTTPError as e:status=e.code;body=e.read();error=str(e);headers=dict(e.headers)
 except Exception as e:body=str(e).encode();error=str(e)
 (ROOT/name).write_bytes(body)
 return {'file':name,'url':url,'retrieved_at':stamp,'status':status,'error':error,'sha256':hashlib.sha256(body).hexdigest(),'bytes':len(body),'headers':headers}
with ThreadPoolExecutor(max_workers=5) as pool:results=list(pool.map(fetch,queries.items()))
(ROOT/'primary-fetch-manifest.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps([{k:r[k] for k in ['file','status','error','bytes']} for r in results],indent=2))
