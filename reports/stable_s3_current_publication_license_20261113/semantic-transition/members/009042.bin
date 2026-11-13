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
F=fixture('published-controls');m=module('v2','guarded_writer_v2',F)
for name in ['focused_controls_v2.py','dependency_drift_controls_v2.py']:
 source=D/'scripts'/name;exec(compile(source.read_bytes(),str(source),'exec'),{'__name__':'__main__','__file__':str(source)})
focused=json.loads((F/'validation/focused-controls-v2.json').read_text());drift=json.loads((F/'validation/dependency-drift-controls-v2.json').read_text())
assert focused['status']==drift['status']=='PASS' and focused['control_count']==28 and len(drift['controls'])==5
save('reproduced-author-controls.json',{'focused':focused,'drift':drift,'total':33,'exact_control_sources':{n:h(D/'scripts'/n) for n in ['focused_controls_v2.py','dependency_drift_controls_v2.py']},'rebinding':'Only task output root O is replaced with isolated reviewer fixture. Actual source R stays W03 and is read-only.'})
counter=[]
for version in ['v1','v2']:
 f=fixture('independent-parent-'+version);m=module(version,'independent_guard_'+version,f);w=m.Writer();p=w.prepare('W03-DEP-1176-PYGS')
 parent=f/'inputs/targets/Peptone.yaml';old=parent.read_bytes();new=old.replace(b'identifier: mesh:D010461',b'identifier: mesh:D011492',1);assert old!=new;parent.write_bytes(new)
 dest=f/'payloads-v2/independent-PYGS.yaml';error=None;receipt=None
 try:receipt=w.write(p,dest)
 except Exception as e:error={'type':type(e).__name__,'message':str(e)}
 assert (dest.is_file() and error is None) if version=='v1' else (not dest.exists() and error and error['message']=='pinned input drift')
 counter.append({'writer':version,'sha256':h(D/'scripts'/('guarded_writer_'+version+'.py')),'parent_before_sha256':hashlib.sha256(old).hexdigest(),'parent_after_sha256':h(parent),'output_exists':dest.exists(),'output_sha256':h(dest) if dest.exists() else None,'error':error,'receipt':receipt,'result':'REPRODUCED_ORIGINAL_FAILURE' if version=='v1' else 'REFUSED_BEFORE_OUTPUT'})
for p,digest in pins.items():assert h(R/p)==digest,p
save('independent-serial-parent-probe.json',{'at':datetime.datetime.now(datetime.UTC).isoformat(),'finding_id':'W03-PEPTONE-GUARD-001','results':counter,'actual_published_packet_unchanged':True,'scope':'Single-author serial drift counterexample. Not a hostile concurrency guarantee.'})
save('controls-execution.json',{'at':datetime.datetime.now(datetime.UTC).isoformat(),'status':'PASS','author_controls_reproduced':33,'independent_original_and_fixed_cases':2,'published_packet_file_hashes_unchanged':len(pins),'fixtures_not_for_publication':True})
print('PASS 33 original controls; independent v1 bad write reproduced and v2 refusal reproduced; published inputs unchanged.')
