"""Append-only successor capture helper; never changes predecessor artifacts."""
import concurrent.futures, hashlib, json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd()
OUT=ROOT/'reports/all_unmatched_20261107/worker-10/successor-v1/chemicals'
OUT.mkdir(parents=True,exist_ok=True)
def fetch(item):
    key,url=item
    dest=OUT/'captures'/(key+'.bin');dest.parent.mkdir(exist_ok=True)
    assert not dest.exists(),dest
    now=datetime.now(timezone.utc).isoformat()
    r=subprocess.run(['curl','-L','--fail','--retry','1','--connect-timeout','15','--max-time','60','-sS',url],capture_output=True)
    rec={'key':key,'url':url,'accessed_at':now,'exit_code':r.returncode,'stderr':r.stderr.decode(errors='replace')}
    if not r.returncode:
        dest.write_bytes(r.stdout)
        rec.update(path=str(dest.relative_to(OUT.parents[1])),sha256=hashlib.sha256(r.stdout).hexdigest(),bytes=len(r.stdout))
        if r.stdout.startswith(b'%PDF'):
            subprocess.run(['pdftotext','-layout',str(dest),str(dest.with_suffix('.txt'))],capture_output=True)
    return rec
if __name__=='__main__':
    p=Path(sys.argv[1]);out=OUT/(p.stem+'-receipts.json');assert not out.exists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: rs=list(pool.map(fetch,json.loads(p.read_text()).items()))
    out.write_text(json.dumps(rs,indent=2)+'\n')
    print(json.dumps({'receipts':str(out),'count':len(rs),'success':sum(r['exit_code']==0 for r in rs)}))
