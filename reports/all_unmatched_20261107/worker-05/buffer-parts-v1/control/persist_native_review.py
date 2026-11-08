from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,os
W=Path.cwd();P=W/'reports/all_unmatched_20261107/worker-05/buffer-parts-v1';V=P/'validation';py=str(W/'.temp/all-unmatched-worker-05/venv/bin/python');content=str(P/'native-review-preparation/review-content.json')
commands=[('native-content-validation',[py,'scripts/record_review.py','validate',content]),('native-save',[py,'scripts/record_review.py','save','--content',content]),('native-retained-review-check',[py,'scripts/record_review.py','check','--base','0bac12cabfd1f67f212631d8eef9aa46379f6b41','--require-reviews'])]
for n,cmd in commands:
 q=V/(n+'.json');assert not q.exists();r=subprocess.run(cmd,text=True,capture_output=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='src'));(V/(n+'.stdout.log')).write_text(r.stdout);(V/(n+'.stderr.log')).write_text(r.stderr);q.write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=r.returncode),indent=2)+'\n');print(n,r.returncode,r.stdout[:2000],r.stderr[:500]);assert r.returncode==0
