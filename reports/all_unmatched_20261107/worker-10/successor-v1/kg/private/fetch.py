import concurrent.futures,hashlib,json,sys,urllib.request,urllib.error
from pathlib import Path
from datetime import datetime,timezone
R=Path(__file__).parents[1]
jobs=json.loads(Path(sys.argv[1]).read_text())
(R/'captures').mkdir(parents=True,exist_ok=True)
def fetch(k,u):
 start=datetime.now(timezone.utc).isoformat();p=R/'captures'/f'{k}.bin'
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'MIM source review; primary-evidence capture','Accept':'*/*'})
  with urllib.request.urlopen(req,timeout=45) as x: raw=x.read();status=x.status;ctype=x.headers.get('Content-Type');final=x.url
 except urllib.error.HTTPError as x:raw=x.read();status=x.code;ctype=x.headers.get('Content-Type');final=u
 except Exception as x:return {'id':k,'url':u,'accessed_at':start,'error':str(x)}
 p.write_bytes(raw)
 return {'id':k,'url':u,'accessed_at':start,'http_status':status,'content_type':ctype,'final_url':final,'capture':{'root':'artifact','path':str(p.relative_to(R.parents[1])),'sha256':hashlib.sha256(raw).hexdigest()}}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e: results=list(e.map(lambda a:fetch(*a),jobs.items()))
(R/(Path(sys.argv[1]).stem+'-receipt.json')).write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps([{'id':x['id'],'status':x.get('http_status'),'error':x.get('error')} for x in results]))
