from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,os,argparse
W=Path.cwd();S=W/'.temp/w05-tellurium-polypeptone-v1';B=W/'reports/all_unmatched_20261107/worker-05';O=B/'postseal-source-corrections-v1';P=B/'tellurium-polypeptone-v1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('--selection',type=Path,required=True);a=ap.parse_args();sel=json.loads(a.selection.read_text());PS=json.loads((O/'core/proposals.json').read_text());ix={p['proposal_id']:i for i,p in enumerate(PS['proposals'])};reviewed=[]
for lane,paths in sel.items():
 x=json.loads((W/paths['proposals']).read_text());rows=x['proposals'] if isinstance(x,dict) else x
 for p in rows:
  assert p['proposal_id'] in ix and p['proposal_id'] not in reviewed;reviewed.append(p['proposal_id']);PS['proposals'][ix[p['proposal_id']]]=p
V=P/'validation';V.mkdir(exist_ok=True,parents=True);inputfile=V/'input-proposals.json';assert not inputfile.exists();inputfile.write_text(json.dumps(PS,indent=2,ensure_ascii=False)+'\n')
py=str(W/'.temp/all-unmatched-worker-05/venv/bin/python');env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='src');receipts=[]
cmd=[py,str(B/'final-correction-v1/control/validate_overlay_v2.py'),'--proposals',str(inputfile),'--out',str(V/'full-overlay')]
r=subprocess.run(cmd,capture_output=True,text=True,env=env);(V/'full-overlay.stdout.log').write_text(r.stdout);(V/'full-overlay.stderr.log').write_text(r.stderr);receipts.append(dict(command=cmd,exit_code=r.returncode));assert r.returncode==0,r.stdout+r.stderr
strict=V/'full-strict';strict.mkdir();cmd=[py,'scripts/validate_strict.py']+[str((B/p['after_capture']['path']).relative_to(W)) for p in PS['proposals']]+['--workers','1','--out',str(strict/'failures.tsv')]
r=subprocess.run(cmd,capture_output=True,text=True,env=env);(strict/'stdout.log').write_text(r.stdout);(strict/'stderr.log').write_text(r.stderr);receipt=dict(at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=r.returncode,payloads=len(PS['proposals']),input_proposals_sha256=sha(inputfile));(strict/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');assert r.returncode==0,r.stdout+r.stderr
receipts.append(dict(command=cmd,exit_code=r.returncode));(V/'selected-native-checks.json').write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),status='PASS',candidate_payloads=len(PS['proposals']),reviewed_proposal_ids=reviewed,proposals_sha256=sha(inputfile),commands=receipts,scope='Guarded/closed schema on all selected full payloads and full baseline substitution; no maintained changes.'),indent=2)+'\n');print(json.dumps(dict(status='PASS',full_selected_payloads=len(PS['proposals']),reviewed=len(reviewed))))
