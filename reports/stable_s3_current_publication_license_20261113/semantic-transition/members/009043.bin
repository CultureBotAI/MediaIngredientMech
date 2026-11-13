"""Run exact published private controls in reviewer-only fixtures."""
from pathlib import Path
import datetime,hashlib,importlib.util,json,os,runpy,shutil,sys
O=Path(__file__).resolve().parent;C=O.parents[1];R=C.parents[1];W=C/'workers/w03/worktree';D=W/'reports/all_unmatched_20261107/worker-03/successors/issue1176-dependencies-v1'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):
 with (O/n).open('x') as f:json.dump(v,f,indent=2);f.write('\n')
def fixture(name):
 f=O/'fixtures'/name;f.mkdir(parents=True)
 for n in ['author-plan-v2.json']:shutil.copy2(D/n,f/n)
 shutil.copytree(D/'inputs',f/'inputs');shutil.copytree(D/'payloads-v2',f/'payloads-v2');(f/'scripts').mkdir()
 for n in ['guarded_writer_v1.py','guarded_writer_v2.py']:shutil.copy2(D/'scripts'/n,f/'scripts'/n)
 return f
def module(version,name,root):
 p=D/'scripts'/('guarded_writer_'+version+'.py');s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);m.O=root;assert m.R==W;return m
pins={str(p.relative_to(R)):h(p) for p in D.rglob('*') if p.is_file() and not p.is_symlink()}
F=fixture('published-controls-final');m=module('v2','guarded_writer_v2',F)
for name in ['focused_controls_v2.py','dependency_drift_controls_v2.py']:
 source=D/'scripts'/name;exec(compile(source.read_bytes(),str(source),'exec'),{'__name__':'__main__','__file__':str(source)})
focused=json.loads((F/'validation/focused-controls-v2.json').read_text());drift=json.loads((F/'validation/dependency-drift-controls-v2.json').read_text())
assert focused['status']==drift['status']=='PASS' and focused['control_count']==28 and len(drift['controls'])==5
save('reproduced-author-controls-final.json',{'focused':focused,'drift':drift,'total':33,'exact_control_sources':{n:h(D/'scripts'/n) for n in ['focused_controls_v2.py','dependency_drift_controls_v2.py']},'rebinding':'Only task output root O is replaced with isolated reviewer fixture. Actual source R stays W03 and is read-only.'})

for p,digest in pins.items():assert h(R/p)==digest,p
print("PASS clean33-controls-only execution; published packet unchanged")
