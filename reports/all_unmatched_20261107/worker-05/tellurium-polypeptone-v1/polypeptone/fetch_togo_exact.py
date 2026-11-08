from pathlib import Path
from datetime import datetime, timezone
import json, subprocess, hashlib, concurrent.futures
S = Path('.temp/w05-tellurium-polypeptone-v1/polypeptone')
C = S / 'captures'
ids = [122,174,175,182,190,215,231,256,266,2,318,423,537,77,874,90,91]
def fetch(i):
    name = f'togo-gmdb-M{i}.json'
    url = f'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M{i}'
    p = C / name
    assert not p.exists()
    at = datetime.now(timezone.utc).isoformat()
    cmd = ['curl','-L','--retry','2','--connect-timeout','10','--max-time','45','--silent','--show-error','--output',str(p),'--write-out','%{http_code}',url]
    r = subprocess.run(cmd,capture_output=True,text=True)
    o = dict(url=url,accessed_at=at,completed_at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=r.returncode,http_status=r.stdout,stderr=r.stderr,path=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None,bytes=p.stat().st_size if p.exists() else 0)
    (C / (name+'.receipt.json')).write_text(json.dumps(o,indent=2)+'\n')
    return o
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    out = list(pool.map(fetch,ids))
(S / 'togo-exact-fetch-receipts.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{k:r[k] for k in ['path','http_status','exit_code','bytes']} for r in out],indent=2))
