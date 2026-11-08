import datetime,hashlib,json,urllib.request,concurrent.futures
from pathlib import Path
B=Path('reports/all_unmatched_20261107/worker-04/successors/issue-1201-v1/captures/chemistry');B.mkdir(parents=True,exist_ok=True)
urls={
'icsc-citrate-pentahydrate.html':'https://inchem.org/documents/icsc/icsc/eics1220.htm',
'jecfa-citrate.pdf':'https://www.fao.org/fileadmin/user_upload/jecfa_additives/docs/Monograph1/Additive-481.pdf',
's-medium-1985.pdf':'https://www.jstage.jst.go.jp/article/bbb1961/49/11/49_11_3331/_pdf',
'pubchem-citrate-trihydrate.json':'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/18421636/JSON',
'ols-citrate-pentahydrate.json':'https://www.ebi.ac.uk/ols4/api/search?q=trisodium%20citrate%20pentahydrate&ontology=chebi&rows=20',
'ols-citrate-trihydrate.json':'https://www.ebi.ac.uk/ols4/api/search?q=trisodium%20citrate%20trihydrate&ontology=chebi&rows=20',
'ols-sodium-glutamate-hydrate.json':'https://www.ebi.ac.uk/ols4/api/search?q=sodium%20glutamate%20hydrate&ontology=chebi&rows=50',
'dsmz354.pdf':'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium354.pdf',
'mediadive-p5.html':'https://mediadive.dsmz.de/medium/P5'
}
def get(item):
 n,u=item;r={'name':n,'url':u,'accessed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'urllib GET timeout30s'}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as q:v=q.read();r.update(status=q.status,final_url=q.url)
  (B/n).write_bytes(v);r.update(path=str((B/n).relative_to(Path('reports/all_unmatched_20261107/worker-04'))),sha256=hashlib.sha256(v).hexdigest(),size=len(v))
 except Exception as e:r['error']=repr(e)
 print(json.dumps(r),flush=True);return r
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(get,urls.items()))
(B/'retrievals.json').write_text(json.dumps(rows,indent=2)+'\n')
