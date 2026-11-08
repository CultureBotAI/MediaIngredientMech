from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,argparse
W=Path.cwd();S=W/'.temp/w05-postseal-source-corrections-v1';B=W/'reports/all_unmatched_20261107/worker-05';P=B/'postseal-source-corrections-v1'
ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
j=lambda p:json.loads(p.read_text())
start=j(S/'control/preservation-start.json');result=[]
for inv in start['inventories']:
 m=Path(inv['manifest']);assert sha(m)==inv['sha256'];data=j(m)
 for member in data['files']:assert sha(m.parent/member['path'])==member['sha256']
 for member in data.get('native_review',[]):assert sha(W/member['path'])==member['sha256']
 result.append(dict(manifest=str(m),sha256=sha(m),members=len(data['files']),verified=True))
old_inventory=W/'.temp/w05-final-correction-v1/control/maintained-baseline-preservation-start.json';inventory=j(old_inventory)
actual={str(p.relative_to(W)) for p in (W/'data/ingredients').rglob('*.yaml')};assert actual=={r['path'] for r in inventory['records']}
for r in inventory['records']:assert sha(W/r['path'])==r['sha256']
contract=B/'contracts/frozen-baseline.json';baseline=j(contract);members={};shards=[]
for k,b in baseline['queue']['shards'].items():
 p=Path(b['path']);assert sha(p)==b['sha256'];rows=j(p)['cases'];shards.append(dict(path=str(p),sha256=sha(p),cases=len(rows)))
 for row in rows:assert row['case_id'] not in members;members[row['case_id']]=k
for c in start['contracts']:assert sha(W/c['path'])==c['sha256']
tracked=subprocess.check_output(['git','diff','--name-only','5156d92bec6bd885ca8bae3c5e18bfdce0069176'],text=True).splitlines()
assert all(x.startswith(str(P.relative_to(W))+'/') or x.startswith('reviews/structured/') for x in tracked),tracked
out=dict(at=datetime.now(timezone.utc).isoformat(),status='PASS',maintained_path_set_and_hashes_equal=True,includes_ignored_files=True,maintained_records=len(actual),maintained_inventory=dict(path=str(old_inventory),sha256=sha(old_inventory)),historical_packets=result,campaign_cases=len(members),shards=shards,contracts=start['contracts'],git_changes_outside_authorized_report_review_paths=[],scope='File/ownership preservation only; no identity or export approval.')
assert not a.out.exists();a.out.parent.mkdir(exist_ok=True,parents=True);a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['status','maintained_records','campaign_cases']}))
