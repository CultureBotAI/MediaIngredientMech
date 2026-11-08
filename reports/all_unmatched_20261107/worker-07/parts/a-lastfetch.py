"""Bounded low-concurrency retry of primary sources needed for exact batch A outcomes."""
import urllib.request,pathlib,json,datetime,hashlib,concurrent.futures
R=pathlib.Path('reports/all_unmatched_20261107/worker-07'); urls={'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id='+m:ix for m,ix in [('M915',[39]),('M3265',[66]),('M2215',[49]),('M2277',[58]),('M3213',[53]),('M2785',[56]),('M2653',[45])]}
def f(it):
 u,ix=it;e={'url':u,'indices':ix,'accessed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=urllib.request.urlopen(u,timeout=25);b=r.read();p=R/'captures'/('a-last-'+hashlib.sha256(u.encode()).hexdigest()[:16]+('.pdf' if b.startswith(b'%PDF') else '.json'));p.write_bytes(b);e.update(path=str(p.relative_to(R)),sha256=hashlib.sha256(b).hexdigest(),status=r.status)
 except Exception as ex:e['error']=str(ex)
 return e
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as p:out=list(p.map(f,urls.items()))
(R/'parts/a-last-results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
