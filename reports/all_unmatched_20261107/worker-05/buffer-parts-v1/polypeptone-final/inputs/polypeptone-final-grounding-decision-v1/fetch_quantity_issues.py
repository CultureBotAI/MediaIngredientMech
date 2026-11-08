from pathlib import Path
import json,subprocess,hashlib,datetime
from concurrent.futures import ThreadPoolExecutor
D=Path(__file__).parent
def f(pair):
 n,k=pair;end=f"repos/CultureBotAI/CultureMech/issues/{n}"+("/comments?per_page=100" if k=="comments" else "");a=["gh","api",end];r=subprocess.run(a,capture_output=True);p=D/f"cm-issue{n}-{k}.json";p.write_bytes(r.stdout);p.with_suffix(".stderr").write_bytes(r.stderr);return {"argv":a,"at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"exit":r.returncode,"path":p.name,"sha256":hashlib.sha256(r.stdout).hexdigest()}
with ThreadPoolExecutor(max_workers=3) as x:rs=list(x.map(f,[(n,k) for n in (118,150,408) for k in ("body","comments")]))
(D/"quantity-issue-receipts.json").write_text(json.dumps(rs,indent=2)+"\n");print(json.dumps(rs))
