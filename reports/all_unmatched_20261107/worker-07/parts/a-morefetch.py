"""Bounded low-concurrency retry of primary sources needed for exact batch A outcomes."""
import urllib.request,pathlib,json,datetime,hashlib,concurrent.futures
R=pathlib.Path('reports/all_unmatched_20261107/worker-07'); urls={
'https://mediadive.dsmz.de/medium/J876':[39],
'https://pmc.ncbi.nlm.nih.gov/articles/PMC2901722/':[64],
'https://link.springer.com/article/10.1186/1752-0509-5-101':[64],
'https://pmc.ncbi.nlm.nih.gov/articles/PMC9431491/':[66],
'https://academic.oup.com/nar/article/29/10/2145/2383885':[49],
'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2567':[60],
'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3115':[40],
'https://mediadb.systemsbiology.net/defined_media/media/288/':[64],
'https://mediadb.systemsbiology.net/defined_media/media/32/':[64],
'https://mediadb.systemsbiology.net/defined_media/media/205/':[64]
}
def f(it):
 u,ix=it;e={'url':u,'indices':ix,'accessed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=urllib.request.urlopen(u,timeout=25);b=r.read();p=R/'captures'/('a-more-'+hashlib.sha256(u.encode()).hexdigest()[:16]+('.pdf' if b.startswith(b'%PDF') else '.json'));p.write_bytes(b);e.update(path=str(p.relative_to(R)),sha256=hashlib.sha256(b).hexdigest(),status=r.status)
 except Exception as ex:e['error']=str(ex)
 return e
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as p:out=list(p.map(f,urls.items()))
(R/'parts/a-more-results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
