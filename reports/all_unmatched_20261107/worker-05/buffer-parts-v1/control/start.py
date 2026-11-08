from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, shutil, subprocess
W=Path.cwd(); C=W.parents[2]; S=W/'.temp/w05-buffer-parts-v1'; B=W/'reports/all_unmatched_20261107/worker-05'; P=B/'buffer-parts-v1'; T=C/'preflight/buffer-source-parts-triage-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest(); j=lambda p:json.loads(p.read_text())
base='0bac12cabfd1f67f212631d8eef9aa46379f6b41'
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==base
assert not subprocess.check_output(['git','status','--porcelain'],text=True).strip()
assert sha(T/'ASSESSMENT.json')=='53e137bc1f567a810258a1d552fa001b5dd10ebffd83f3654695a5053a7b07b0'
for name,digest in j(T/'ASSESSMENT.json')['files'].items():assert sha(T/name)==digest
(S/'inputs').mkdir(exist_ok=True); shutil.copytree(T,S/'inputs/buffer-source-parts-triage-v1',copy_function=shutil.copy2)
P.mkdir(exist_ok=False)
old=j(W/'.temp/w05-tellurium-polypeptone-v1/control/preservation-start.json'); inventories=[]
for path in [B/'tellurium-polypeptone-v1/MANIFEST.json']+[Path(x['manifest']) for x in old['inventories']]:
    m=j(path)
    for r in m['files']:assert sha(path.parent/r['path'])==r['sha256']
    for r in m.get('native_review',[]):assert sha(W/r['path'])==r['sha256']
    inventories.append(dict(manifest=str(path),sha256=sha(path),members=len(m['files']),verified=True))
for r in old['contracts']:assert sha(W/r['path'])==r['sha256']
inv=j(W/'.temp/w05-final-correction-v1/control/maintained-baseline-preservation-start.json'); records={str(p.relative_to(W)):sha(p) for p in (W/'data/ingredients').rglob('*.yaml')};assert records=={r['path']:r['sha256'] for r in inv['records']}
owners={};contracts=j(B/'contracts/frozen-baseline.json')
for shard,r in contracts['queue']['shards'].items():
    path=Path(r['path']);assert sha(path)==r['sha256']
    for case in j(path)['cases']:assert case['case_id'] not in owners;owners[case['case_id']]=shard
handoffs=j(W/'.temp/w05-tellurium-polypeptone-v1/control/protected-private-handoffs.json')
handoffs.append(dict(path='.temp/w05-tellurium-polypeptone-v1/HANDOFF.json',sha256='b73288250d900c246065bdef2549ea7d427277de367117a0393faf564276e392'))
for r in handoffs:assert sha(W/r['path'])==r['sha256']
for name,data in [('preservation-start.json',dict(at=datetime.now(timezone.utc).isoformat(),base=base,inventories=inventories,contracts=old['contracts'],maintained_records_verified=len(records),ownership_cases=len(owners),ownership_shards=len(contracts['queue']['shards']),triage_assessment_sha256=sha(T/'ASSESSMENT.json'),includes_ignored_files=True)),('protected-private-handoffs.json',handoffs)]:
    q=S/'control'/name;assert not q.exists();q.write_text(json.dumps(data,indent=2)+'\n')
(S/'issues').mkdir(exist_ok=False)
print(json.dumps({'status':'PASS','base':base,'maintained':len(records),'campaign_cases':len(owners),'prior_packets':len(inventories)}))
