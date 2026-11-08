"""Capture primary chemistry evidence for worker04; authored 2026-11-08.

Read-only HTTP GETs; immutable evidence bytes and retrieval receipt under the
assigned artifact root. No ontology/data/lockfile mutations.
"""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import urllib.request

ROOT = pathlib.Path('reports/all_unmatched_20261107/worker-04/captures/chemistry')
ROOT.mkdir(parents=True, exist_ok=True)
CODES = [63125,64734,64758,53426,17754,15956,506227,8006,15377,232425,64220,27470,17268,144421,30729,78292,31604,26493,41131,15966,29377,40947,115156,91249,86477,131839,131391,132112,42334,16810,30915,63037,53258,63939,63940,17772,3311]
IDS = [942,2178,825,650,803,1992,143,1352,706,120,104,839,399,1188,404,1201,1291,1743,676,2384,415,1566,890,1492,276]
JOBS = [(f'ols-CHEBI-{c}.json',f'https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:{c}') for c in CODES]
JOBS += [(f'mediadive-compound-{i}.json', f'https://mediadive.dsmz.de/rest/compound/{i}') for i in IDS]
JOBS += [('ccap-MR_TAP.pdf','https://www.ccap.ac.uk/wp-content/uploads/MR_TAP.pdf'),('ccap-MR_Waris_H.pdf','https://www.ccap.ac.uk/wp-content/uploads/MR_Waris_H.pdf')]

def capture(job):
    name,url=job
    path=ROOT/name
    if path.exists():
        return {'path':name,'url':url,'status':'already_exists_not_refetched','sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    at=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'MIM-source-review/1.0'})
        with urllib.request.urlopen(req,timeout=45) as resp:
            data=resp.read(); status=resp.status; final_url=resp.url
        path.write_bytes(data)
        return {'path':name,'url':url,'final_url':final_url,'accessed_at':at,'http_status':status,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
    except Exception as e:
        return {'path':name,'url':url,'attempted_at':at,'error':str(e)}

if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        receipts=list(pool.map(capture,JOBS))
    p=ROOT/'retrieval-receipts.json'
    if p.exists(): raise SystemExit('Refusing to overwrite retrieval receipts')
    p.write_text(json.dumps(receipts,indent=2)+'\n')
    print(json.dumps(receipts,indent=2))
