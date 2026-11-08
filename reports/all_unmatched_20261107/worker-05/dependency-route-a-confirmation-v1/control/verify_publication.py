from pathlib import Path
from datetime import datetime,timezone
import argparse,json,hashlib,subprocess
W=Path.cwd();S=W/'.temp/w05-dependency-route-a-confirmation-v1';Q=W/'reports/all_unmatched_20261107/worker-05/dependency-route-a-confirmation-v1';sha=lambda b:hashlib.sha256(b).hexdigest();j=lambda p:json.loads(p.read_text())
a=argparse.ArgumentParser();a.add_argument('--phase',choices=['staged','committed'],required=True);a=a.parse_args();m=j(Q/'MANIFEST.json');base=m['predecessor_head'];n=j(Q/'native-review-preparation/review-content.json')['review_id'];nr=W/'reviews/structured'/n
expected={str((Q/r['path']).relative_to(W)):r['sha256'] for r in m['files']};expected[str((Q/'MANIFEST.json').relative_to(W))]=sha((Q/'MANIFEST.json').read_bytes())
for f in nr.glob('*'):expected[str(f.relative_to(W))]=sha(f.read_bytes())
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
if a.phase=='staged':
 assert head==base;cmd=['git','diff','--cached','--name-status'];spec=lambda p:':'+p
else:
 assert subprocess.check_output(['git','rev-parse','HEAD^'],text=True).strip()==base
 cmd=['git','diff','--name-status',base,head];spec=lambda p:head+':'+p
changes=[x.split('\t',1) for x in subprocess.check_output(cmd,text=True).splitlines()]
assert all(t=='A' for t,p in changes),changes
assert {p for t,p in changes}==set(expected),(set(expected)-{p for t,p in changes},{p for t,p in changes}-set(expected))
for p,h in expected.items():
 assert sha((W/p).read_bytes())==h,p
 assert sha(subprocess.check_output(['git','show',spec(p)]))==h,p
for old in ['43f7cf6e8681fa617b5d6d3529d94d537ca01f0d','0bac12cabfd1f67f212631d8eef9aa46379f6b41',base]:subprocess.run(['git','merge-base','--is-ancestor',old,'HEAD'],check=True)
out=S/'publication';out.mkdir(exist_ok=True);f=out/(a.phase+'-verification.json');assert not f.exists();f.write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),status='PASS',phase=a.phase,head=head,base=base,files=len(expected),manifest_sha256=sha((Q/'MANIFEST.json').read_bytes()),only_additive_report_and_native_review=True,verified_blobs=expected),indent=2)+'\n')
print(json.dumps(dict(status='PASS',phase=a.phase,head=head,exact_blobs=len(expected))))
