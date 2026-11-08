from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
W=Path.cwd();S=W/'.temp/w05-tellurium-polypeptone-v1';B=W/'reports/all_unmatched_20261107/worker-05';P=B/'tellurium-polypeptone-v1';j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();start=j(S/'control/preservation-start.json')
for inv in start['inventories']:
 m=Path(inv['manifest']);assert sha(m)==inv['sha256'];data=j(m)
 for r in data['files']:assert sha(m.parent/r['path'])==r['sha256']
 for r in data.get('native_review',[]):assert sha(W/r['path'])==r['sha256']
for r in start['contracts']:assert sha(W/r['path'])==r['sha256']
inv=j(W/'.temp/w05-final-correction-v1/control/maintained-baseline-preservation-start.json');paths={str(p.relative_to(W)) for p in (W/'data/ingredients').rglob('*.yaml')};assert paths=={r['path'] for r in inv['records']}
for r in inv['records']:assert sha(W/r['path'])==r['sha256']
contracts=j(B/'contracts/frozen-baseline.json');owners={}
for shard,r in contracts['queue']['shards'].items():
 p=Path(r['path']);assert sha(p)==r['sha256']
 for row in j(p)['cases']:assert row['case_id'] not in owners;owners[row['case_id']]=shard
for r in j(S/'control/protected-private-handoffs.json'):assert sha(W/r['path'])==r['sha256']
changes=subprocess.check_output(['git','diff','--name-only',start['base']],text=True).splitlines();assert all(p.startswith(str(P.relative_to(W))+'/') or p.startswith('reviews/structured/') for p in changes)
q=P/'validation/preservation-final.json';assert not q.exists();q.write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),status='PASS',historical_packets=start['inventories'],maintained_records=len(paths),campaign_cases=len(owners),all10shard_hashes_match=True,contracts_unchanged=True,protected_private_handoffs=j(S/'control/protected-private-handoffs.json'),includes_ignored_files=True,unexpected_tracked_changes=[],scope='Byte and ownership preservation only; no scientific approval.'),indent=2)+'\n');print(json.dumps(dict(status='PASS',maintained_records=len(paths),campaign_cases=len(owners))))
