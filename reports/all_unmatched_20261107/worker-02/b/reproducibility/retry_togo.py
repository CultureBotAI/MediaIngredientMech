"""2026-11-08 public TOGO API fallback after curl timeout; only block-b outputs."""
import concurrent.futures,datetime,hashlib,json,pathlib,urllib.request
out=pathlib.Path('reports/all_unmatched_20261107/worker-02/b/captures')
urls=[r['url'] for r in json.loads((out/'togo-retrievals.json').read_text()) if r['exit_code'] != 0]
def one(u):
 p=out/('retry-togo-'+u.split('=')[-1]+'.json'); at=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'MIM-source-review/1.0','Accept':'application/json'})
  with urllib.request.urlopen(req,timeout=35) as response:b=response.read()
  p.write_bytes(b)
  return {'url':u,'path':'b/captures/'+p.name,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'accessed_at':at,'exit_code':0}
 except Exception as e:return {'url':u,'accessed_at':at,'exit_code':1,'error':str(e)}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for x in ex.map(one,urls):
  rows.append(x);(out/'retry-togo-retrievals.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({'count':len(rows),'ok':sum(x['exit_code']==0 for x in rows)}))
