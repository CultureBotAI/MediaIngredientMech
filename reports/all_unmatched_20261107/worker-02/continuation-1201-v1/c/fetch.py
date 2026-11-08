import urllib.request,urllib.parse,json,hashlib,datetime,concurrent.futures
from pathlib import Path
C=Path('reports/all_unmatched_20261107/worker-02/continuation-1201-v1/c'); (C/'captures').mkdir(exist_ok=True)
urls={}
for n in [498,511,766,534,796,399,519,718,'718a',404,985,1752,1753,514]:urls['medium-'+str(n)]='https://mediadive.dsmz.de/rest/medium/'+str(n)
for q in ['Pulp of sour stone cherries','lipoprotein concentrate','desiccated ox bile','poly hexamethylene carbonate','Leptospira Enrichment EMJH','magnesium sulfate hexahydrate','manganese sulfate heptahydrate','congocidin','maltose monohydrate','copper sulfate monohydrate','sodium silicate']:
 urls['ols-'+q.replace(' ','-')]='https://www.ebi.ac.uk/ols4/api/search?'+urllib.parse.urlencode({'q':q,'rows':100,'ontology':'chebi,ncit,foodon,mesh,envo,micro,bto,uberon'})
for n in [277,1555,885,492,1113,1580,375,1107]:urls['dsmz-'+str(n)]='https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium'+str(n)+'.pdf'
urls['mesh-netropsin']='https://id.nlm.nih.gov/mesh/D009429.json'
urls['chebi-polycarbonate']='https://www.ebi.ac.uk/ols4/api/search?q=polycarbonate&ontology=chebi&rows=50'
def f(kv):
 k,u=kv;t=datetime.datetime.now(datetime.timezone.utc).isoformat();p=C/'captures'/(k+('.pdf' if u.endswith('pdf') else '.json'))
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 source-review-1201'}),timeout=40) as z:b=z.read();status=z.status;typ=z.headers.get('content-type','')
  p.write_bytes(b);return {'key':k,'url':u,'accessed_at':t,'http_status':status,'content_type':typ,'path':str(p.relative_to(C.parents[1])),'sha256':hashlib.sha256(b).hexdigest()}
 except Exception as e:return {'key':k,'url':u,'accessed_at':t,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:r=list(ex.map(f,urls.items()))
(C/'retrieval-log.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps([{k:v for k,v in x.items() if k in ['key','http_status','error']} for x in r],indent=2))
