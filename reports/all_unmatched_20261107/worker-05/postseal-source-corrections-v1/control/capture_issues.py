from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib
S=Path('.temp/w05-postseal-source-corrections-v1');rows=[]
for name,ep,pages in [('issue1238','issues/1238',False),('issue1238-comments','issues/1238/comments',True),('issue1237','issues/1237',False),('issue1237-comments','issues/1237/comments',True),('issue1226','issues/1226',False),('bsa-comment','issues/comments/6718748704',False),('marine-comment','issues/comments/6718748333',False)]:
 p=S/'issues'/f'{name}.json';assert not p.exists();cmd=['gh','api','repos/CultureBotAI/MediaIngredientMech/'+ep]+(['--paginate','--slurp'] if pages else []);at=datetime.now(timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True);assert r.returncode==0,(name,r.stderr.decode());json.loads(r.stdout);p.write_bytes(r.stdout);rows.append(dict(name=name,command=cmd,accessed_at=at,exit_code=r.returncode,path=str(p),sha256=hashlib.sha256(r.stdout).hexdigest()))
(S/'issues/receipt.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps([dict(name=r['name'],sha256=r['sha256']) for r in rows]))
