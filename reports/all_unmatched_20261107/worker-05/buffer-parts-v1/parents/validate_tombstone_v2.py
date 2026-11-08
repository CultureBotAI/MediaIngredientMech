from pathlib import Path
from datetime import datetime, timezone
import json,hashlib,os,subprocess,sys,types
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient,validate_ingredient

W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1/parents';T=S/'tombstone';V=T/'validation-v2';V.mkdir(exist_ok=False);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
f=T/'proposed-v2/Bacto_Soytone.yaml';r=yaml.safe_load(f.read_text());b=yaml.safe_load((T/'before/Bacto_Soytone.yaml').read_text());assert not validate_ingredient(r)
write_validated_ingredient(r,V/'guarded-readback/Bacto_Soytone.yaml');readback=yaml.safe_load((V/'guarded-readback/Bacto_Soytone.yaml').read_text());assert readback==r and 'representative' in readback and readback['representative']==''
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='src');py=str(W/'.temp/all-unmatched-worker-05/venv/bin/python')
commands=[('strict',[py,'scripts/validate_strict.py',str(f),'--workers','1','--out',str(V/'strict-failures.tsv')]),('native-existing-regression',[py,'-m','pytest','-o','addopts=','tests/test_sssom_other_cross_record.py::test_missing_explicit_target_never_credits_former_identifier_owner','--basetemp',str(V/'pytest-tmp'),'-q','-p','no:cacheprovider'])]
results=[]
for name,cmd in commands:
    p=subprocess.run(cmd,capture_output=True,text=True,env=env);(V/(name+'.stdout.log')).write_text(p.stdout);(V/(name+'.stderr.log')).write_text(p.stderr);results.append(dict(name=name,command=cmd,exit_code=p.returncode));assert p.returncode==0,p.stdout+p.stderr
builder=W.parents[4]/'.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py';assert sha(builder)=='38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc'
sys.path[:0]=[str(builder.parent),str(builder.parent.parent/'src')];m=types.ModuleType('w05_tombstone_native');m.__file__=str(builder);sys.modules[m.__name__]=m;exec(compile(builder.read_bytes(),str(builder),'exec'),m.__dict__)
path=W/'data/ingredients/mapped/Bacto_Soytone.yaml';before=m._row_from_yaml(path,{}, {}, {}, {},record=b,owners=m.build_owner_index({'MIM:Bacto_Soytone':b}),suppressions=[]);after=m._row_from_yaml(path,{}, {}, {}, {},record=r,owners=m.build_owner_index({'MIM:Bacto_Soytone':r}),suppressions=[])
assert before==[] and after==[];m._check_producer_bindings()
receipt=dict(at=datetime.now(timezone.utc).isoformat(),author='/root/buffer_hepes',status='PASS',after_sha256=sha(f),before_sha256=sha(T/'before/Bacto_Soytone.yaml'),explicit_empty_representative_survives_guarded_roundtrip=True,commands=results,native_tombstone_rows=dict(before=before,after=after),native_alias_reproduction=dict(path='tombstone/native-alias-reproduction.json',sha256=sha(T/'native-alias-reproduction.json')),builder=dict(path=str(builder),sha256=sha(builder)),scope='Authentic dependent tombstone full payload, existing native empty-target regression, and actual name-ownership behavior. No new test, maintained source, gate or generator change. Root full composed source decision and full-overlay review remain required.')
(V/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(dict(status='PASS',native_rows=0,tests='2 existing native empty/unresolved representative cases')))
