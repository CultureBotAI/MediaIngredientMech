from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
W=Path.cwd();S=W/'.temp/w05-final-correction-v1';P=W/'reports/all_unmatched_20261107/worker-05/final-correction-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
for name,key in [('protected-inputs.json','inputs'),('maintained-baseline-preservation-start.json','records'),('predecessor-manifest-start.json','rows'),('campaign-ownership.json','shards')]:
 p=S/'control'/name;x=json.loads(p.read_text());rows=x[key]
 for row in rows:
  q=Path(row['path']);q=q if q.is_absolute() else W/q
  assert sha(q)==row['sha256'],q
 checks.append(dict(inventory=str(p.relative_to(W)),inventory_sha256=sha(p),verified_members=len(rows)))
q=W/'.temp/final-preparation-comparison-v1';m=q/'MANIFEST.json';x=json.loads(m.read_text())
rows=x.get('files',x.get('artifacts'))
assert isinstance(rows,list),x.keys()
for r in rows:
 p=q/r['path'];assert sha(p)==r['sha256'],p
checks.append(dict(inventory=str(m.relative_to(W)),inventory_sha256=sha(m),verified_members=len(rows)))
# Entire tracked tree outside this new report/native bundle must equal the preserved source head.
raw=subprocess.check_output(['git','diff','--name-status','43f7cf6e8681fa617b5d6d3529d94d537ca01f0d'],text=True)
allowed=['reports/all_unmatched_20261107/worker-05/final-correction-v1/']
content=P/'native-review-preparation/review-content.json'
if content.exists():allowed.append('reviews/structured/'+json.loads(content.read_text())['review_id']+'/')
for line in raw.splitlines():
 status,path=line.split('\t',1)
 assert status=='A' and any(path.startswith(p) for p in allowed),(status,path)
# Git-independent inventory includes ignored owner files.
actual={str(p.relative_to(W)) for p in (W/'data/ingredients').rglob('*.yaml')}
expected={r['path'] for r in json.loads((S/'control/maintained-baseline-preservation-start.json').read_text())['records']}
assert actual==expected,(actual-expected,expected-actual)
out=P/'validation/final-preservation.json';assert not out.exists()
out.write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),verifier='/root',source_head='43f7cf6e8681fa617b5d6d3529d94d537ca01f0d',inventories=checks,
 ignored_files_included=True,maintained_owner_inventory_exact=True,tracked_changes_outside_successor=[],git_diff=raw,status='PASS'),indent=2)+'\n')
print(json.dumps(dict(status='PASS',inventories=len(checks),owners=len(actual))))
