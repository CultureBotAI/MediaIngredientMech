from pathlib import Path
import shutil,hashlib,json
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1';P=W/'reports/all_unmatched_20261107/worker-05/buffer-parts-v1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();copied=[]
for name in ['hepes','tris','dependencies','dependencies-direct-v1','chemical-reports','parents','parents-direct-v1','media','polypeptone-final','inputs','issues','review','assembly-review','control']:
 for q in sorted((S/name).rglob('*')):
  if not q.is_file() or '__pycache__' in q.parts:continue
  dst=P/q.relative_to(S);dst.parent.mkdir(parents=True,exist_ok=True)
  if dst.exists():assert sha(dst)==sha(q),dst
  else:shutil.copy2(q,dst);copied.append(str(dst.relative_to(P)))
# Canonical immutable authored composition input; separate canonical reviewed wrapper follows.
for q in (S/'control/composed-final-v5').iterdir():
 dst=P/'control/composed'/q.name;dst.parent.mkdir(exist_ok=True)
 if dst.exists():assert sha(dst)==sha(q)
 else:shutil.copy2(q,dst)
print(json.dumps({'copied_new_files':len(copied),'all_existing_public_bytes_unchanged':True}))
