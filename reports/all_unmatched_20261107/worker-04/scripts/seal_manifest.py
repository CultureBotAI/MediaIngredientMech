"""Seal durable worker artifacts plus the new native review; exclude the manifest and the final independent receipt to avoid self-reference."""
import json,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];ART=ROOT/'reports/all_unmatched_20261107/worker-04';manifest=ART/'artifact-manifest.json'
paths=sorted(p for p in ART.rglob('*') if p.is_file() and p!=manifest and p!=ART/'independent-review/final-bundle-reviewed-by-biological-v1.json')
receipt=json.loads((ART/'validation/native-save.json').read_text());paths.extend([Path(receipt['review']),Path(receipt['markdown'])])
assert all(not p.is_symlink() for p in paths)
rows=[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in paths]
manifest.write_text(json.dumps({'sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'All durable worker04 artifacts and the new authoritative native review pair; excludes the manifest itself, the final independent bundle-review receipt (which attests this manifest), and private post-push receipt to avoid self-reference. The post-push receipt separately records hashes for the manifest and final independent receipt. Superseded/failed artifacts remain explicitly labeled and are not current approvals.','files':rows,'file_count':len(rows),'total_bytes':sum(x['bytes'] for x in rows)},indent=2)+'\n')
print(json.dumps({'file_count':len(rows),'total_bytes':sum(x['bytes'] for x in rows),'manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest()},indent=2))
