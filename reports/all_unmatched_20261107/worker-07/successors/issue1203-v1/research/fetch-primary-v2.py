from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from datetime import datetime,timezone
import urllib.request,hashlib,json
out=Path(__file__).parent
urls={**{f'mediadive-solution-{i}':f'https://mediadive.dsmz.de/rest/solution/{i}' for i in [5518,5736,5775,5781,5782,6448]}}
def one(item):
 name,url=item;now=datetime.now(timezone.utc).isoformat();ext='.pdf' if url.endswith('.pdf') else '.json';p=out/(name+'-v2'+ext)
 assert not p.exists(),str(p)
 try:
  with urllib.request.urlopen(url,timeout=90) as response:
   raw=response.read();status=response.status;headers=dict(response.headers)
  p.write_bytes(raw)
  return {'evidence_id':'MG1203-PRIMARY-'+name.upper()+'-V2','url':url,'accessed_at':now,'http_status':status,'headers':headers,'capture':{'root':'artifact','path':str(p.relative_to(Path('reports/all_unmatched_20261107/worker-07').resolve())),'sha256':hashlib.sha256(raw).hexdigest()}}
 except Exception as exc: return {'url':url,'accessed_at':now,'error':repr(exc)}
rows=list(ThreadPoolExecutor(6).map(one,urls.items()))
(out/'new-primary-index-v2.json').write_text(json.dumps(rows,indent=2)+'\n')
for row in rows:print(row['url'],row.get('http_status'),row.get('error'))
