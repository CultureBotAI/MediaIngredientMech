from pathlib import Path
from datetime import datetime,timezone
import json,subprocess
S=Path('reports/all_unmatched_20261107/worker-10/successor-v2');cmd=['.temp/all-unmatched-worker-10/venv/bin/python','scripts/record_review.py','check','--base','468766d941e35a74eb2de3c95096660987277d9b','--require-reviews'];start=datetime.now(timezone.utc).isoformat();r=subprocess.run(cmd,text=True,capture_output=True)
for suffix,txt in [('stdout',r.stdout),('stderr',r.stderr)]:
 with (S/('native-check-v2.'+suffix)).open('x') as f:f.write(txt)
with (S/'native-check-v2-command.json').open('x') as f:json.dump({'started_at':start,'finished_at':datetime.now(timezone.utc).isoformat(),'argv':cmd,'exit_code':r.returncode},f,indent=2);f.write('\n')
print(r.stdout);print(r.stderr);assert r.returncode==0
