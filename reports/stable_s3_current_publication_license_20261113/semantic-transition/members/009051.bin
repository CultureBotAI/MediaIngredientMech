from pathlib import Path
import datetime,hashlib,importlib.util,json,shutil,sys
O=Path(__file__).resolve().parent;C=O.parents[1];W=C/'workers/w03/worktree';D=W/'reports/all_unmatched_20261107/worker-03/successors/issue1176-dependencies-v1'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();out=[]
for version in ['v1','v2']:
 f=O/'fixtures'/('independent-corrected-'+version);f.mkdir(parents=True);shutil.copy2(D/'author-plan-v2.json',f/'author-plan-v2.json');shutil.copytree(D/'inputs',f/'inputs')
 pth=D/'scripts'/('guarded_writer_'+version+'.py');spec=importlib.util.spec_from_file_location('independent_serial_'+version,pth);m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);m.O=f
 w=m.Writer();prepared=w.prepare('W03-DEP-1176-PYGS');parent=f/'inputs/targets/Peptone.yaml';old=parent.read_bytes();new=old.replace(b'identifier: mesh:D010461',b'identifier: mesh:D011492',1);assert old!=new;parent.write_bytes(new)
 dest=f/('payloads' if version=='v1' else 'payloads-v2')/'PYGS.yaml';error=None;receipt=None
 try:receipt=w.write(prepared,dest)
 except Exception as e:error={'type':type(e).__name__,'message':str(e)}
 if version=='v1':assert dest.is_file() and error is None
 else:assert not dest.exists() and error and error['message']=='pinned input drift'
 out.append({'writer':version,'writer_sha256':h(pth),'parent_before_sha256':hashlib.sha256(old).hexdigest(),'parent_after_sha256':h(parent),'output_exists':dest.exists(),'output_sha256':h(dest) if dest.exists() else None,'error':error,'receipt':receipt,'result':'ORIGINAL_FAILURE_REPRODUCED' if version=='v1' else 'REFUSED_BEFORE_OUTPUT'})
result={'at':datetime.datetime.now(datetime.UTC).isoformat(),'finding_id':'W03-PEPTONE-GUARD-001','results':out,'initial_probe_correction':'Original review probe used v2 output directory for v1, so its output-scope guard refused. Both exact writer versions now use their declared output scopes; original failed run and33 passing author-control results preserved.','actual_source_inputs_unchanged':True,'scope':'Single-author serial change after prepare; no hostile concurrency claim.'}
with (O/'independent-serial-parent-probe.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print('PASS independently reproduced v1 stale-parent write and v2 refusal using exact version-specific output scopes.')
