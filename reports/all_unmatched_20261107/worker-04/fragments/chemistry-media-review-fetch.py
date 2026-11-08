import datetime,hashlib,json,urllib.request
from pathlib import Path
base=Path('reports/all_unmatched_20261107/worker-04/independent-review/media-chemistry-captures');base.mkdir(exist_ok=True)
urls={'merck-czapek-manual.pdf':'https://www.mibius.de/out/oxbaseshop/html/0/images/wysiwigpro/Czapek_Dox_105460_engl.pdf','sigma-rca-datasheet.pdf':'https://www.sigmaaldrich.com/deepweb/assets/sigmaaldrich/product/documents/175/054/91365dat.pdf'}
rows=[]
for name,url in urls.items():
 row={'url':url,'accessed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'Python urllib.request GET with user-agent and45-second timeout'}
 try:
  request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(request,timeout=45) as response:
   content=response.read();row.update({'status':response.status,'final_url':response.url,'headers':dict(response.headers)})
  (base/name).write_bytes(content);row.update({'path':str((base/name).relative_to(Path('reports/all_unmatched_20261107/worker-04'))),'sha256':hashlib.sha256(content).hexdigest(),'bytes':len(content)})
 except Exception as e:row['error']=repr(e)
 rows.append(row)
 print(json.dumps(row))
(base/'retrievals.json').write_text(json.dumps(rows,indent=2)+'\n')
