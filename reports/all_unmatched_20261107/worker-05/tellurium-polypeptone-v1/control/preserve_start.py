from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,shutil
W=Path.cwd();S=W/'.temp/w05-tellurium-polypeptone-v1';C=W.parents[2];B=W/'reports/all_unmatched_20261107/worker-05';P=B/'tellurium-polypeptone-v1';T=C/'preflight/tellurium-grade-triage-v1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();j=lambda p:json.loads(p.read_text())
assert C.name=='all-unmatched-20261107',str(C)
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()=='76bca688b4f55e8bdf791079df8d4156cded6c4c'
P.mkdir(exist_ok=False);(S/'inputs').mkdir(exist_ok=True)
assert sha(T/'HANDOFF.json')=='fa8ad3c1b629807eac958d6bc7077e90201c869ff54716b45f95e54ec87468c0';tm=j(T/'MANIFEST.json');print('triage keys',list(tm));print(str(tm)[:800])
shutil.copytree(T,S/'inputs/tellurium-grade-triage-v1')
inventories=[]
for m in [B/'postseal-source-corrections-v1/MANIFEST.json',B/'final-correction-v1/MANIFEST.json',W/'.temp/final-preparation-comparison-v1/MANIFEST.json']:
 x=j(m)
 for r in x['files']:assert sha(m.parent/r['path'])==r['sha256']
 for r in x.get('native_review',[]):assert sha(W/r['path'])==r['sha256']
 inventories.append(dict(manifest=str(m),sha256=sha(m),members=len(x['files']),verified=True))
inv=j(W/'.temp/w05-final-correction-v1/control/maintained-baseline-preservation-start.json');actual={str(p.relative_to(W)) for p in (W/'data/ingredients').rglob('*.yaml')};assert actual=={r['path'] for r in inv['records']}
for r in inv['records']:assert sha(W/r['path'])==r['sha256']
orig=j(B/'contracts/frozen-baseline.json');owners={}
for k,r in orig['queue']['shards'].items():
 p=Path(r['path']);assert sha(p)==r['sha256']
 for d in j(p)['cases']:assert d['case_id'] not in owners;owners[d['case_id']]=k
contracts=j(W/'.temp/w05-postseal-source-corrections-v1/control/preservation-start.json')['contracts']
for r in contracts:assert sha(W/r['path'])==r['sha256']
out=dict(at=datetime.now(timezone.utc).isoformat(),base='76bca688b4f55e8bdf791079df8d4156cded6c4c',inventories=inventories,maintained_records_verified=len(actual),ownership_cases=len(owners),ownership_shards=len(orig['queue']['shards']),contracts=contracts,triage_handoff_filename_resolution=dict(requested='HANDOFF.md',actual='HANDOFF.json',requested_sha256=sha(T/'HANDOFF.json'),gitignore_independent_search=True,exact_hash_match=True),protection='Old manifests/reviews/captures and maintained sources remain immutable.')
(S/'control/preservation-start.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(maintained=len(actual),ownership=len(owners),packets=inventories)))
