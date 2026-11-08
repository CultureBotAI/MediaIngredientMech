from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,os
W=Path.cwd();Q=W/'reports/all_unmatched_20261107/worker-05/dependency-route-a-confirmation-v1';V=Q/'validation';py=str(W/'.temp/all-unmatched-worker-05/venv/bin/python');content=str(Q/'native-review-preparation/review-content.json')
for n,cmd in [('native-content-validation',[py,'scripts/record_review.py','validate',content]),('native-save',[py,'scripts/record_review.py','save','--content',content]),('native-retained-review-check',[py,'scripts/record_review.py','check','--base','108e213e96f7d423ee345ce265d692e79063127c','--require-reviews'])]:
 q=V/(n+'.receipt.json');assert not q.exists()
 r=subprocess.run(cmd,text=True,capture_output=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='src'))
 for suffix,text in [('stdout.log',r.stdout),('stderr.log',r.stderr)]: (V/(n+'.'+suffix)).write_text(text)
 q.write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=r.returncode),indent=2)+'\n');print(n,r.returncode,r.stdout[:1200],r.stderr[:500],flush=True);assert r.returncode==0
