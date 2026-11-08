import json,pathlib,subprocess,hashlib,datetime,concurrent.futures,urllib.parse
R=pathlib.Path(__file__).resolve().parents[1]
targets=[(116, 'OLSall:ammonium sodium phosphate', 'https://www.ebi.ac.uk/ols4/api/search?q=ammonium%20sodium%20phosphate&rows=50'), (116, 'OLSall:"7783-13-3"', 'https://www.ebi.ac.uk/ols4/api/search?q=%227783-13-3%22&rows=50'), (116, 'OLSall:sodium ammonium hydrogen phosphate', 'https://www.ebi.ac.uk/ols4/api/search?q=sodium%20ammonium%20hydrogen%20phosphate&rows=50')]
def fetch(t):
 i,fam,url=t;p=R/'captures'/('b-remediation-'+hashlib.sha256(url.encode()).hexdigest()[:16]+'.body');at=datetime.datetime.now(datetime.timezone.utc).isoformat();q=subprocess.run(['curl','-L','-sS','--connect-timeout','5','--max-time','18','-o',str(p),'-w','%{http_code}\n%{url_effective}\n%{content_type}',url],capture_output=True);s=q.stdout.decode(errors='replace').splitlines();e={'case_index':i,'family':fam,'url':url,'accessed_at':at,'transport_success':q.returncode==0,'http_status':s[0] if s else None,'final_url':s[1] if len(s)>1 else None,'content_type':s[2] if len(s)>2 else None,'error':q.stderr.decode(errors='replace')}
 if p.exists():
  ext='.pdf' if p.read_bytes().startswith(b'%PDF') else '.json' if 'json' in str(e['content_type']) else '.xml' if 'xml' in str(e['content_type']) else '.html';dest=p.with_suffix(ext);p.rename(dest);e.update(path=dest.relative_to(R).as_posix(),sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),bytes=dest.stat().st_size)
 return e
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:out=list(ex.map(fetch,targets))
(R/'parts/b-remediation4-retrievals.json').write_text(json.dumps(out,indent=2))
print([(x['case_index'],x['family'],x['http_status'],x.get('bytes')) for x in out])
