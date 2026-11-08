from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,urllib.request,urllib.parse
O=Path('.temp/w05-buffer-parts-v1/media');j=lambda p:json.loads(p.read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
terms=sorted({r['ontology_mapping']['ontology_id'] for r in j(O/'inputs/component-owner-search.json')['rows'] if r.get('ontology_mapping') and r['ontology_mapping']['ontology_id'].startswith(('CHEBI:','FOODON:','MICRO:'))})
def fetch(term):
    url='https://www.ebi.ac.uk/ols4/api/ontologies/'+term.split(':')[0].lower()+'/terms?'+urllib.parse.urlencode({'obo_id':term});at=datetime.now(timezone.utc).isoformat();q=O/'captures'/('ols-'+term.replace(':','-')+'.json');assert not q.exists()
    req=urllib.request.Request(url,headers={'User-Agent':'MediaIngredientMech scientific source review (public ontology evidence)'})
    with urllib.request.urlopen(req,timeout=45) as response:raw=response.read();status=response.status;final=response.url
    q.write_bytes(raw);data=json.loads(raw);rows=data.get('_embedded',{}).get('terms',[]);assert len(rows)==1 and rows[0]['obo_id']==term
    return dict(term=term,url=url,final_url=final,status=status,accessed_at=at,path=str(q.relative_to(O)),sha256=sha(raw),review_fields={k:rows[0].get(k) for k in ['iri','obo_id','label','description','synonyms','annotation','is_obsolete']})
with ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(fetch,terms))
q=O/'read/ontology-primary-index.json';assert not q.exists();q.write_text(json.dumps(results,indent=2)+'\n');print(json.dumps({'primary_terms':len(results),'index':str(q)}))
