from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
S=Path('.temp/w05-buffer-parts-v1');O=S/'issues';jobs=[]
for n in [1237,1226]:
    jobs.append((f'issue{n}.json',['gh','api',f'repos/CultureBotAI/MediaIngredientMech/issues/{n}']))
    jobs.append((f'issue{n}-comments.json',['gh','api',f'repos/CultureBotAI/MediaIngredientMech/issues/{n}/comments','--paginate','--slurp']))
jobs.append(('comment6718873227.json',['gh','api','repos/CultureBotAI/MediaIngredientMech/issues/comments/6718873227']))
receipts=[]
for name,cmd in jobs:
    at=datetime.now(timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True);q=O/name;assert not q.exists();q.write_bytes(r.stdout);(O/(name+'.stderr')).write_bytes(r.stderr)
    receipts.append(dict(path=name,sha256=hashlib.sha256(r.stdout).hexdigest(),accessed_at=at,command=cmd,exit_code=r.returncode));assert r.returncode==0,(name,r.stderr.decode())
(O/'capture-receipt.json').write_text(json.dumps(receipts,indent=2)+'\n');print(json.dumps(receipts,indent=2))
