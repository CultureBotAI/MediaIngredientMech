"""Bounded unauthenticated primary-source retrieval; preserves bytes and failures."""
import concurrent.futures,datetime,hashlib,json,sys
from pathlib import Path
import requests
OUT=Path('reports/all_unmatched_20261107/worker-09/followups/hexahydrates-v1/captures')
def fetch(item):
 name,url=item;started=datetime.datetime.now(datetime.timezone.utc).isoformat();p=OUT/(name+'.capture');meta={'url':url,'started_at':started}
 try:
  r=requests.get(url,timeout=(15,45));p.write_bytes(r.content);meta.update(accessed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),status_code=r.status_code,effective_url=r.url,content_type=r.headers.get('Content-Type'),sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content),capture_path=str(p))
 except requests.RequestException as e:meta.update(accessed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),error=str(e))
 (OUT/(name+'.metadata.json')).write_text(json.dumps(meta,indent=2)+'\n');return meta
items=json.loads(Path(sys.argv[1]).read_text())
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for result in pool.map(fetch,items.items()):print(json.dumps(result))
