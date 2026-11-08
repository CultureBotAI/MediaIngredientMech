from pathlib import Path
import json,hashlib,importlib.util,sys,shutil,datetime
R=Path.cwd(); A=R/'.temp/peptone-final-dependencies-v1'; O=A/'skeptical-review'; F=O/'guard-drift-fixture-v2'; assert not F.exists(); F.mkdir()
plan=json.loads((A/'author-plan-v2.json').read_text())
paths={'author-plan-v2.json'}
for x in plan['primary_captures']+plan['selected_parent_inputs']:paths.add(x['path'])
for row in plan['rows']:
 paths.add(row['maintained_before']['path']);paths.add(row['current_payload']['path'])
for rel in paths:
 dst=F/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(A/rel,dst)
spec=importlib.util.spec_from_file_location('guarded_dep_probe',A/'scripts/guarded_writer_v2.py');m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);m.O=F
w=m.Writer();p=w.prepare('W03-DEP-1176-PYGS');parent=F/'inputs/targets/Peptone.yaml';before=parent.read_bytes();parent.write_bytes(before.replace(b'identifier: mesh:D010461',b'identifier: mesh:D011492',1));dest=F/'payloads-v2/PYGS.yaml';exc=None;receipt=None
try:receipt=w.write(p,dest)
except Exception as e:exc={'type':type(e).__name__,'message':str(e)}
sha=lambda b:hashlib.sha256(b).hexdigest()
result={'reviewer':'/root/peptone_final_skeptic','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'Import exact immutable guarded_writer_v1 in isolated copied fixture; rebind only its task output root O. Actual source/author inputs never altered. Prepare genuine PYGS payload, then mutate only fixture-selected generic parent identifier before write.','writer_sha256':sha((A/'scripts/guarded_writer_v2.py').read_bytes()),'plan_sha256':sha((A/'author-plan-v2.json').read_bytes()),'parent_before_sha256':sha(before),'parent_after_sha256':sha(parent.read_bytes()),'destination':str(dest.relative_to(R)),'output_exists':dest.exists(),'output_sha256':sha(dest.read_bytes()) if dest.exists() else None,'exception':exc,'receipt':receipt,'expected':'Refuse fresh selected-parent input mismatch with no output.','actual':'WRITE_SUCCEEDED_DESPITE_STALE_SELECTED_PARENT' if dest.exists() else 'REFUSED_NO_OUTPUT','finding_id':'W03-PEPTONE-GUARD-001','classification':'Bounded private producer integrity gap; report before repair. No maintained data affected.'}
assert not dest.exists() and exc and exc['message']=='pinned input drift', 'fixed helper must refuse before any output'
(O/'guard-drift-probe-v2.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['receipt','method']},indent=2))
