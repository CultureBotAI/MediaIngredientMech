"""2026-11-08 primary_b: bounded additional primary capture (10s per URL)."""
import pathlib,json,datetime,hashlib,urllib.request,concurrent.futures,re,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1]
ctx=json.loads((ROOT/'parts/b-contexts.json').read_text());urls={}
for c in ctx:
 for o in c['occurrences']:
  d=o['complete_recipe']; text=str(d.get('notes',''))
  for mid in re.findall(r'togomedium.org/medium/(M\d+)',text):urls.setdefault('https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id='+mid,[]).append(c['case_id'])
  for jid in re.findall(r'GRMD=(\d+)',text):urls.setdefault('https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD='+jid,[]).append(c['case_id'])
for ident in ['CHEBI:91259','CHEBI:91260','CHEBI:91261','MICRO:0001611','MICRO:0000175','CHEBI:17883','CHEBI:32145']:
 urls['https://www.ebi.ac.uk/ols4/api/ontologies/'+ident.split(':')[0].lower()+'/terms?obo_id='+ident]=[]
urls['https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0957-V2.pdf']=[]
urls['https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-SR0090A-V4.pdf']=[]
urls['https://www.sigmaaldrich.com/US/en/product/sigma/p3850']=[]
urls['https://www.sigmaaldrich.com/US/en/product/sigma/c8654']=[]
def fetch(it):
 url,cids=it;ts=datetime.datetime.now(datetime.timezone.utc).isoformat();base='captures/b-curl-'+hashlib.sha256(url.encode()).hexdigest()[:16]
 try:
  proc=subprocess.run(['curl','--silent','--show-error','--location','--fail','--max-time','15','--connect-timeout','5',url],capture_output=True,timeout=20)
  if proc.returncode:raise RuntimeError(proc.stderr.decode(errors='replace'))
  raw=proc.stdout
  ext='.pdf' if raw.startswith(b'%PDF') else '.json' if raw[:1] in (b'{',b'[') else '.html';path=base+ext;(ROOT/path).write_bytes(raw)
  r={'url':url,'case_ids':list(set(cids)),'accessed_at':ts,'success':True,'path':path,'sha256':hashlib.sha256(raw).hexdigest()}
  if ext=='.pdf':
   out=ROOT/(base+'.txt');pr=subprocess.run(['pdftotext','-layout',str(ROOT/path),str(out)],capture_output=True);r['text_path']=str(out.relative_to(ROOT));r['pdftotext_returncode']=pr.returncode
  return r
 except Exception as e:return {'url':url,'case_ids':list(set(cids)),'accessed_at':ts,'success':False,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
 results=[]
 for r in pool.map(fetch,urls.items()):
  results.append(r)
  (ROOT/'parts/b-curl-retrievals.json').write_text(json.dumps(results,indent=2)+'\n')
print('Completed',len(results),'successful',sum(x['success'] for x in results))
