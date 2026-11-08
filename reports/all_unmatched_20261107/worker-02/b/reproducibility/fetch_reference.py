"""2026-11-08 public reference capture; URL-list input, immutable per-run files."""
import concurrent.futures,datetime,hashlib,json,pathlib,subprocess,sys
out=pathlib.Path('reports/all_unmatched_20261107/worker-02/b/captures')
urls=json.loads(pathlib.Path(sys.argv[1]).read_text()); label=sys.argv[2]
def one(u):
 p=out/(label+'-'+hashlib.sha256(u.encode()).hexdigest()[:16]+'.bin'); at=datetime.datetime.now(datetime.timezone.utc).isoformat()
 z=subprocess.run(['curl','-L','--fail','--retry','1','--connect-timeout','12','--max-time','40','-sS',u,'-o',str(p)],capture_output=True,text=True)
 b=p.read_bytes() if p.exists() else b''
 return {'url':u,'path':'b/captures/'+p.name,'sha256':hashlib.sha256(b).hexdigest() if b else None,'bytes':len(b),'accessed_at':at,'exit_code':z.returncode,'stderr':z.stderr}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: rows=list(ex.map(one,urls))
(out/(label+'-retrievals.json')).write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({'count':len(rows),'failures':[x for x in rows if x['exit_code']]}))
