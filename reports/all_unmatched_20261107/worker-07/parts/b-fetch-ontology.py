"""2026-11-08 primary_b: retrieve exact primary ontology records; no data edits."""
import urllib.request,json,pathlib,datetime,hashlib,concurrent.futures
ROOT=pathlib.Path(__file__).resolve().parents[1]
IDS=['CHEBI:32138','CHEBI:114249','CHEBI:31795','CHEBI:66870','CHEBI:17439','CHEBI:131531','CHEBI:33403','CHEBI:32599','CHEBI:32142','CHEBI:32954','CHEBI:176843','NCIT:C61946','CHEBI:91247','CHEBI:91248','CHEBI:44557','CHEBI:64734','CHEBI:131391','CHEBI:6637','CHEBI:31345','CHEBI:53438','CHEBI:30605','CHEBI:61278','CHEBI:15640','CHEBI:17890','CHEBI:114126','CHEBI:31340','CHEBI:17905','CHEBI:86416','CHEBI:62969','FOODON:00001282']
def fetch(ident):
    url='https://www.ebi.ac.uk/ols4/api/ontologies/'+ident.split(':')[0].lower()+'/terms?obo_id='+ident
    ts=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        with urllib.request.urlopen(url,timeout=45) as response:raw=response.read()
        p='captures/b-ontology-'+ident.replace(':','-')+'.json';(ROOT/p).write_bytes(raw)
        d=json.loads(raw);terms=d.get('_embedded',{}).get('terms',[])
        return {'identifier':ident,'url':url,'accessed_at':ts,'path':p,'sha256':hashlib.sha256(raw).hexdigest(),'terms':[{'obo_id':t.get('obo_id'),'label':t.get('label'),'description':t.get('description'),'synonyms':t.get('synonyms'),'annotation':t.get('annotation'),'is_obsolete':t.get('is_obsolete')} for t in terms],'success':bool(terms)}
    except Exception as e:return {'identifier':ident,'url':url,'accessed_at':ts,'error':str(e),'success':False}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(fetch,IDS))
(ROOT/'parts/b-ontology-retrievals.json').write_text(json.dumps(results,indent=2)+'\n')
for r in results: print(r['identifier'],r['success'],[(t['label'],t['description']) for t in r.get('terms',[])])
