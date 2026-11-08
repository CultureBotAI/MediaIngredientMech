from pathlib import Path
import json,hashlib,datetime,subprocess
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1';R=S/'assembly-review';B=W/'reports/all_unmatched_20261107/worker-05';j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();start=j(S/'control/preservation-start.json');errors=[];members=[]
for inv in start['inventories']:
 m=Path(inv['manifest']);assert sha(m)==inv['sha256'];data=j(m)
 for f in data['files']:
  q=m.parent/f['path'];assert sha(q)==f['sha256'],q
 for f in data.get('native_review',[]):assert sha(W/f['path'])==f['sha256']
 members.append(dict(manifest=str(m.relative_to(W)),sha256=sha(m),verified_members=len(data['files']),native_pair_members=len(data.get('native_review',[]))))
for f in start['contracts']:assert sha(W/f['path'])==f['sha256']
maint=j(W/'.temp/w05-final-correction-v1/control/maintained-baseline-preservation-start.json');actual={str(p.relative_to(W)) for p in (W/'data/ingredients').rglob('*.yaml')};assert actual=={x['path'] for x in maint['records']}
for f in maint['records']:assert sha(W/f['path'])==f['sha256']
contracts=j(B/'contracts/frozen-baseline.json');owners={};shards=[]
for n,x in contracts['queue']['shards'].items():
 q=Path(x['path']);assert sha(q)==x['sha256'];rows=j(q)['cases'];shards.append(dict(shard=n,path=str(q),sha256=sha(q),cases=len(rows)))
 for row in rows:assert row['case_id'] not in owners;owners[row['case_id']]=n
handoffs=j(S/'control/protected-private-handoffs.json')
for f in handoffs:assert sha(W/f['path'])==f['sha256']
tracked=subprocess.check_output(['git','diff','--name-only',start['base']],text=True).splitlines();bad=[p for p in tracked if not p.startswith('reports/all_unmatched_20261107/worker-05/buffer-parts-v1/') and not p.startswith('reviews/structured/')];assert not bad,bad
x=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),reviewer='/root/assembly_audit',status='PASS',scope='Independent file/ownership preservation audit; no scientific approval. Current exact files, including ignored files, before final seal.',manifest_members=members,maintained_count=len(actual),maintained_inventory=dict(path='.temp/w05-final-correction-v1/control/maintained-baseline-preservation-start.json',sha256=sha(W/'.temp/w05-final-correction-v1/control/maintained-baseline-preservation-start.json')),shards=shards,source_case_count=len(owners),source_shards=len(shards),contract_bindings=start['contracts'],private_handoffs=handoffs,unexpected_tracked_paths=bad,git_base=start['base'],includes_ignored_files=True)
q=R/'preservation-independent-v1.json';assert not q.exists();q.write_text(json.dumps(x,indent=2)+'\n');print(json.dumps(dict(status='PASS',members=sum(z['verified_members'] for z in members),maintained=len(actual),cases=len(owners),shards=len(shards),sha256=sha(q))))
