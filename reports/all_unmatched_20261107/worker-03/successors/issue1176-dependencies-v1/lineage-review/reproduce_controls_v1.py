"""Independent execution of exact author control sources in a reviewer-only fixture."""
from pathlib import Path
import json,hashlib,shutil,sys
O=Path(__file__).resolve().parent.parent
F=Path(__file__).resolve().parent/'final-controls-fixture'
F.mkdir(exist_ok=False)
for p in ['author-plan-v2.json']:
 shutil.copy2(O/p,F/p)
for p in ['inputs','payloads-v2','scripts']:
 shutil.copytree(O/p,F/p)
sys.path.insert(0,str(O/'scripts'))
import guarded_writer_v2 as m
m.O=F
for name in ['focused_controls_v2.py','dependency_drift_controls_v2.py']:
 raw=(O/'scripts'/name).read_bytes()
 exec(compile(raw,str(O/'scripts'/name),'exec'),{'__name__':'__main__','__file__':str(O/'scripts'/name)})
print('INDEPENDENT_EXACT_CONTROL_SOURCES_PASS')
