import json,pathlib,subprocess,hashlib,datetime,concurrent.futures
r=pathlib.Path(__file__).resolve().parents[1]
targets=[('togo-'+n,'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id='+n) for n in ['M2809','M2760','M2499','M3120','M2601','M2367']]+[('chebi64758','https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64758')]
def fetch(x):
 name,url=x;p=r/'captures'/('b-final-'+name+'.json');at=datetime.datetime.now(datetime.timezone.utc).isoformat();q=subprocess.run(['curl','--location','--silent','--show-error','--fail','--connect-timeout','6','--max-time','18',url],capture_output=True);e={'url':url,'accessed_at':at,'success':q.returncode==0,'error':q.stderr.decode(errors='replace')}
 if q.returncode==0:p.write_bytes(q.stdout);e.update(path=p.relative_to(r).as_posix(),sha256=hashlib.sha256(q.stdout).hexdigest())
 return e
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:out=list(ex.map(fetch,targets))
(r/'parts/b-final-retrievals.json').write_text(json.dumps(out,indent=2))
print([(x['url'],x['success']) for x in out])
