import pathlib,json,shutil,copy
import guarded_writer_v2 as mod
O=mod.O;R=mod.R;out=[]
for kind in ['parent','primary','plan','memory_plan','core']:
 fixture=O/'validation'/f'drift-v2-{kind}';fixture.mkdir(parents=True,exist_ok=False)
 shutil.copy2(O/'author-plan-v2.json',fixture/'author-plan-v2.json');shutil.copytree(O/'inputs',fixture/'inputs')
 mod.O=fixture;w=mod.Writer();p=w.prepare('W03-DEP-1176-PYGS')
 dest=fixture/'payloads-v2/PYGS.yaml';oldregular=mod.regular;target=None;before=None
 if kind in ['parent','primary','plan']:
  target=fixture/({'parent':'inputs/targets/Peptone.yaml','primary':'inputs/primary/atcc-2887.pdf','plan':'author-plan-v2.json'}[kind]);before=mod.sha(target.read_bytes());target.write_bytes(target.read_bytes()+b'\nDRIFT\n')
 elif kind=='memory_plan':w.plan['rows'][0]['application_authorized']=True
 else:
  key=R/w.plan['core_unchanged'][0]['path']
  def fake_regular(path):return b'false preserved core' if path==key else oldregular(path)
  mod.regular=fake_regular
 try:w.write(p,dest)
 except ValueError as e:
  assert not dest.exists();out.append({'case':kind,'status':'REFUSED_NO_OUTPUT','exception':str(e),'fixture_path':str(fixture.relative_to(O)),'input_before_sha256':before,'input_after_sha256':mod.sha(target.read_bytes()) if target else None,'output_exists':False,'mechanism':'actual isolated fixture bytes' if target else ('in-memory mutation' if kind=='memory_plan' else 'read interception for immutable source-core check; actual core never modified')})
 else:raise AssertionError(kind+' incorrectly wrote')
 finally:mod.regular=oldregular;mod.O=O
(O/'validation/dependency-drift-controls-v2.json').write_text(json.dumps({'writer_sha256':mod.sha((O/'scripts/guarded_writer_v2.py').read_bytes()),'finding':'W03-PEPTONE-GUARD-001','controls':out,'status':'PASS','actual_inputs_untouched':True},indent=2)+'\n');print('PASS fresh dependency controls',len(out))
