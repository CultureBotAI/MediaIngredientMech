"""2026-11-08: capture public primary source pages for worker-02 block b.
Inputs: frozen full-contexts.json. Outputs only block b captures and retrieval ledger.
No maintained data writes; byte captures are immutable within this run.
"""
import concurrent.futures, datetime, hashlib, json, pathlib, re, subprocess
ROOT=pathlib.Path.cwd()
OUT=ROOT/'reports/all_unmatched_20261107/worker-02/b/captures'
contexts=json.loads((ROOT/'.temp/all-unmatched-worker-02/b/full-contexts.json').read_text())
urls={}
def add(u,cid):
    if u.startswith('http'):
        urls.setdefault(u.rstrip('.,'),set()).add(cid)
for x in contexts:
    cid=x['case']['case_id']
    for rec in x['recipes']:
        r=rec['complete_recipe']
        for u in re.findall(r'https?://[^\s<>\"\']+',r.get('notes','')): add(u,cid)
        for ref in r.get('references',[]):
            u=ref.get('reference','')
            if any(s in u for s in ('mediadive','jcm.riken','utex.org','togomedium','dsmz.de','nite.go.jp','mcc.nies')): add(u,cid)
    for o in x['case']['occurrences']:
        for entry in o['source_identifiers']:
            m=re.fullmatch(r'mediadive.compound:(\d+)',entry['value'])
            if m: add('https://mediadive.dsmz.de/rest/compound/'+m[1],cid)
def fetch(pair):
    url,ids=pair; name='source-'+hashlib.sha256(url.encode()).hexdigest()[:20]+'.bin'; p=OUT/name
    at=datetime.datetime.now(datetime.timezone.utc).isoformat()
    res=subprocess.run(['curl','-L','--fail','--retry','2','--retry-delay','1','--connect-timeout','12','--max-time','35','-sS',url,'-o',str(p)],capture_output=True,text=True)
    b=p.read_bytes() if p.exists() else b''
    return {'url':url,'accessed_at':at,'path':'b/captures/'+name,'sha256':hashlib.sha256(b).hexdigest() if b else None,'bytes':len(b),'exit_code':res.returncode,'stderr':res.stderr,'case_ids':sorted(ids)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    results=list(pool.map(fetch,sorted(urls.items())))
(OUT/'retrievals.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'total':len(results),'ok':sum(x['exit_code']==0 for x in results),'failed':[{'url':x['url'],'code':x['exit_code']} for x in results if x['exit_code']!=0]}))
