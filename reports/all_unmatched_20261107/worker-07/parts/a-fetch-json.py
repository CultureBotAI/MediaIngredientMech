"""Worker-07 batch A primary TOGO and ontology captures, 2026-11-08."""
import pathlib,json,re,urllib.request,hashlib,datetime,concurrent.futures
R=pathlib.Path('reports/all_unmatched_20261107/worker-07'); Q=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
cs=json.loads((R/'parts/a-input.json').read_text())['cases']; urls={}
for i,c in enumerate(cs):
 for o in c['occurrences']:
  t=(Q/o['full_recipe_snapshot']).read_text()
  for m in set(re.findall(r'togomedium.org/medium/(M\d+)',t)):
   urls.setdefault('https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id='+m,[]).append(i)
for num,inds in {'91248':[7,9,19,29],'91247':[13],'17439':[52],'39005':[61],'232798':[22],'32142':[41,51],'91261':[12,57],'91260':[57],'64734':[10],'750784':[63],'132766':[36,55],'37585':[53],'16651':[23],'53438':[8],'75213':[16,37,43]}.items():
 urls['https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:'+num]=inds
urls['https://mediadive.dsmz.de/download/ingredient/1930/json']=[55]
def f(item):
 u,ix=item; e={'url':u,'indices':sorted(set(ix)),'accessed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30); b=r.read(); p=R/'captures'/('a-json-'+hashlib.sha256(u.encode()).hexdigest()[:16]+'.json'); p.write_bytes(b); e.update(path=str(p.relative_to(R)),sha256=hashlib.sha256(b).hexdigest(),status=r.status)
 except Exception as ex: e['error']=str(ex)
 return e
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: out=list(pool.map(f,urls.items()))
(R/'parts/a-fetch-json-results.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({'requests':len(out),'success':sum('path' in x for x in out),'failures':[x for x in out if 'error' in x]},indent=2))
