"""Copy exact independent review files; record, never follow, control symlinks."""
from pathlib import Path
import os, sys, hashlib, json, datetime
R=next(p for p in Path(__file__).resolve().parents if (p/'MAPPING_SEMANTICS.md').is_file())
A=R/'.temp/w03-provenance-successor-v1'
O=R/'reports/all_unmatched_20261107/worker-03/successors/issue1226-v1'
src=Path(sys.argv[1]).resolve(strict=True);dst=Path(sys.argv[2]).absolute();receipt=Path(sys.argv[3]).absolute()
assert src.is_relative_to(A) and dst.is_relative_to(O) and receipt.is_relative_to(O)
assert not dst.exists() and not receipt.exists()
files=[];links=[]
for root,dirs,names in os.walk(src,followlinks=False):
 root=Path(root)
 for name in sorted(dirs+names):
  p=root/name;rel=p.relative_to(src)
  if p.is_symlink():links.append({'path':str(rel),'target':os.readlink(p),'disposition':'Historical control path descriptor only; no symlink installed in report'})
  elif p.is_file():
   data=p.read_bytes();d=dst/rel;d.parent.mkdir(parents=True,exist_ok=True)
   with d.open('xb') as f:f.write(data)
   assert p.read_bytes()==d.read_bytes()
   files.append({'source_path':str(p.relative_to(R)),'archived_path':str(d.relative_to(R)),'sha256':hashlib.sha256(data).hexdigest()})
receipt.parent.mkdir(parents=True,exist_ok=True)
with receipt.open('x') as f:json.dump({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':files,'symlink_descriptors':links,'file_count':len(files),'symlinks_installed':0},f,indent=2);f.write('\n')
print(json.dumps({'files':len(files),'symlinks_described':len(links),'receipt':str(receipt.relative_to(R))}))
