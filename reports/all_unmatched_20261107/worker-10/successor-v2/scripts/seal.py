from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path.cwd();S=R/'reports/all_unmatched_20261107/worker-10/successor-v2';P=R/'.temp/all-unmatched-worker-10/successor-v2';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
peer=S/'reviews/skeptic/final-handoff-review-v1.json';assert peer.is_file();assert load(S/'native-check-v2-command.json')['exit_code']==0
copies=[]
for src in sorted(P.glob('*.py')):
 dest=S/'scripts'/src.name
 if dest.exists():assert sha(dest)==sha(src);continue
 with dest.open('xb') as f:f.write(src.read_bytes())
 copies.append({'source':str(src.relative_to(R)),'copy':str(dest.relative_to(R)),'sha256':sha(src)})
save(S/'reproduction-copy-receipt-v2.json',{'at':datetime.now(timezone.utc).isoformat(),'new_exact_copies':copies,'prior_receipt_preserved':sha(S/'reproduction-copy-receipt.json')})
files=[f for f in S.rglob('*') if f.is_file() and f.name!='SHA256SUMS']
for name in ['native/saved-pair.json','native-v2/saved-pair.json']:
 for x in load(S/name)['files']:
  f=R/x['path'];assert sha(f)==x['sha256'];files.append(f)
files=sorted(set(files),key=lambda p:str(p.relative_to(R)));lines=[sha(f)+'  '+str(f.relative_to(R)) for f in files]
with (S/'SHA256SUMS').open('x') as f:f.write('\n'.join(lines)+'\n')
for line in lines:
 expected,path=line.split('  ',1);assert sha(R/path)==expected
receipt={'sealed_at':datetime.now(timezone.utc).isoformat(),'status':'PASS','manifest':{'path':str((S/'SHA256SUMS').relative_to(R)),'sha256':sha(S/'SHA256SUMS')},'manifest_member_count':len(files),'successor_files':len([f for f in files if f.is_relative_to(S)]),'new_native_files':len([f for f in files if not f.is_relative_to(S)]),'total_bytes':sum(f.stat().st_size for f in files),'handoff_sha256':sha(S/'HANDOFF.json'),'handoff_md_sha256':sha(S/'HANDOFF.md'),'final_peer_sha256':sha(peer),'member_paths':[str(f.relative_to(R)) for f in files],'stage_expected_paths':[str(f.relative_to(R)) for f in files]+[str((S/'SHA256SUMS').relative_to(R))],'note':'Manifest excludes itself only. Nothing in the sealed report/native packet may be changed after this receipt; publication receipts are separate worker-local files.'};save(P/'seal-receipt.json',receipt);print(json.dumps({k:v for k,v in receipt.items() if k not in ['member_paths','stage_expected_paths']},indent=2))
