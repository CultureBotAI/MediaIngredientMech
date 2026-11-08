from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,subprocess
W=Path.cwd();P=W/'reports/all_unmatched_20261107/worker-05/final-correction-v1';B=P.parent
f=P/'core/proposals.json';ps=json.loads(f.read_text())['proposals'];out=P/'validation/final-strict';out.mkdir(exist_ok=False)
cmd=[sys.executable,'scripts/validate_strict.py']+[str((B/p['after_capture']['path']).relative_to(W)) for p in ps]+['--workers','1','--out',str((out/'failures.tsv').relative_to(W))]
r=subprocess.run(cmd,text=True,capture_output=True)
(out/'stdout.log').write_text(r.stdout);(out/'stderr.log').write_text(r.stderr)
(out/'receipt.json').write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=r.returncode,payloads=len(ps),selected_manifest_sha256=hashlib.sha256(f.read_bytes()).hexdigest()),indent=2)+'\n')
print(json.dumps(dict(exit_code=r.returncode,payloads=len(ps),stdout=r.stdout[-1000:],stderr=r.stderr[-1000:])));sys.exit(r.returncode)
