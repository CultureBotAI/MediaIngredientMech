from pathlib import Path
import subprocess,hashlib,json,datetime,sys,concurrent.futures
A=Path(__file__).resolve().parent
def get(row):
 name,url=row;dest=A/'captures'/name;dest.parent.mkdir(exist_ok=True)
 if dest.exists():raise ValueError('immutable capture already exists: '+str(dest))
 at=datetime.datetime.now(datetime.timezone.utc).isoformat()
 p=subprocess.run(['curl','--location','--retry','1','--connect-timeout','10','--max-time','30','--silent','--show-error','--output',str(dest),'--write-out','%{http_code}\t%{content_type}\t%{url_effective}',url],capture_output=True,text=True)
 meta={'url':url,'accessed_at':at,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'curl_returncode':p.returncode,'curl_result':p.stdout,'stderr':p.stderr,'path':str(dest.relative_to(A)),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest() if dest.exists() else None,'bytes':dest.stat().st_size if dest.exists() else 0,'read_extent':'Captured bytes only; assessment records actual inspection separately.'}
 with (A/'captures'/(name+'.capture.json')).open('x') as f:json.dump(meta,f,indent=2);f.write('\n')
 return meta
rows=json.loads(Path(sys.argv[1]).read_text())
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(get,rows):print(json.dumps(r))
