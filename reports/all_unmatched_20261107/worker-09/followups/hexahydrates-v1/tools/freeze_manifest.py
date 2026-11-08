"""Bind the additive follow-up only; never rewrite the parent manifest."""
import datetime,hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
REPO=next(p for p in HERE.parents if (p/'MAPPING_SEMANTICS.md').is_file())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=json.loads((HERE/'native-review-reference.json').read_text())
archive=json.loads((HERE/'validation/native-archive-check.json').read_text())
assert archive['exit_code']==0
excluded={'MANIFEST.json','independent/final-assembly-review.json'}
files=[]
for p in sorted(HERE.rglob('*')):
    if p.is_file() and str(p.relative_to(HERE)) not in excluded:
        assert not p.is_symlink()
        files.append({'root':'followup','path':str(p.relative_to(HERE)),'sha256':sha(p),'bytes':p.stat().st_size})
for key in ('yaml','markdown'):
    p=REPO/ref[key];files.append({'root':'repository','path':ref[key],'sha256':sha(p),'bytes':p.stat().st_size})
manifest={'schema_version':1,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'published_parent':'d74ab6d48f6345260087cf973cadbe7b6269109f','branch':'review/all-unmatched-w09-source-review-20261107','scope':'Additive exact2case source follow-up; historical1050-entry manifest remains unchanged at published parent.','artifact_root':str(HERE.relative_to(REPO)),'excluded_paths':sorted(excluded),'exclusion_reason':'Manifest cannot hash itself; final independent assembly receipt binds this manifest and is committed separately to avoid a cycle.','file_count':len(files),'total_bytes':sum(f['bytes'] for f in files),'files':files}
p=HERE/'MANIFEST.json';p.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'sha256':sha(p),'file_count':len(files),'total_bytes':manifest['total_bytes']}))
