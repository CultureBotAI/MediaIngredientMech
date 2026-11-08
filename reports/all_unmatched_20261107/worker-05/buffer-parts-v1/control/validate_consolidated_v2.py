from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,os,argparse,sys,types,yaml,copy
W=Path.cwd();B=W/'reports/all_unmatched_20261107/worker-05';P=B/'buffer-parts-v1';O=B/'tellurium-polypeptone-v1';S=W/'.temp/w05-buffer-parts-v1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();j=lambda p:json.loads(p.read_text())
a=argparse.ArgumentParser();a.add_argument('--core',type=Path,required=True);a=a.parse_args();V=P/'validation';V.mkdir(parents=True,exist_ok=True);ps=j(a.core/'proposals.json')['proposals'];q=V/'input-proposals.json';assert not q.exists();q.write_bytes((a.core/'proposals.json').read_bytes());py=str(W/'.temp/all-unmatched-worker-05/venv/bin/python');env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='src')
def run(name,cmd):
 r=subprocess.run(cmd,text=True,capture_output=True,env=env);(V/(name+'.stdout.log')).write_text(r.stdout);(V/(name+'.stderr.log')).write_text(r.stderr);receipt=dict(at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=r.returncode);(V/(name+'.receipt.json')).write_text(json.dumps(receipt,indent=2)+'\n');assert r.returncode==0,(name,r.stdout,r.stderr)
run('full-overlay',[py,str(B/'final-correction-v1/control/validate_overlay_v2.py'),'--proposals',str(q),'--out',str(V/'full-overlay')])
(V/'full-strict').mkdir();run('full-strict',[py,'scripts/validate_strict.py']+[str((B/p['after_capture']['path']).relative_to(W)) for p in ps]+['--workers','1','--out',str(V/'full-strict/failures.tsv')])
builder=W.parents[4]/'.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py';assert sha(builder)=='38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc';sys.path[:0]=[str(builder.parent),str(builder.parent.parent/'src')];mod=types.ModuleType('w05_consolidated_native');mod.__file__=str(builder);sys.modules[mod.__name__]=mod;exec(compile(builder.read_bytes(),str(builder),'exec'),mod.__dict__)
base={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in (W/'data/ingredients').rglob('*.yaml')}
def overlay(proposals):
 o=dict(base)
 for p in proposals:o.pop(p['owner_path'],None);o[p.get('destination_owner_path',p['owner_path'])]=yaml.safe_load((B/p['after_capture']['path']).read_text())
 return o
def ix(o):return mod.build_owner_index({mod._mim_curie(Path(p).name):r for p,r in o.items()})
old=j(O/'core/proposals.json')['proposals'];oi={p['proposal_id']:p for p in old};bo=overlay(old);ao=overlay(ps);bi=ix(bo);ai=ix(ao);out=[]
for p in ps:
 pid=p['proposal_id'];path=p.get('destination_owner_path',p['owner_path']);before=bo.get(path);after=ao[path];br=[];ar=[];bs=[];ass=[]
 if before:br=mod._row_from_yaml(W/path,{}, {}, {}, {},record=before,owners=bi,suppressions=bs)
 ar=mod._row_from_yaml(W/path,{}, {}, {}, {},record=after,owners=ai,suppressions=ass)
 out.append(dict(proposal_id=pid,after_capture=p['after_capture'],before_capture=oi[pid]['after_capture'] if pid in oi else dict(root='worktree',path=p['owner_path'],sha256=p['before_sha256']),before_rows=br,after_rows=ar,before_suppressions=[str(x) for x in bs],after_suppressions=[str(x) for x in ass],before_identifier=before.get('identifier') if before else None,after_identifier=after.get('identifier')))
mod._check_producer_bindings();keys=lambda rows:[(r['predicate_id'],r['object_id']) for r in rows];index={x['proposal_id']:x for x in out}
assert keys(index['CHEM-C1193-Tris-HCl-salt']['after_rows'])==[('skos:broadMatch','CHEBI:9754'),('skos:exactMatch','cas:1185-53-1'),('skos:exactMatch','kgmicrobe.compound:tris_hydrochloride_salt')]
assert keys(index['CHEM-C1193-tellurium-dioxide']['after_rows'])==[('skos:broadMatch','CHEBI:33305'),('skos:exactMatch','cas:7446-07-3'),('skos:exactMatch','kgmicrobe.compound:tellurium_dioxide')]
assert keys(index['W05-FINAL-MAT-039']['after_rows'])==[('skos:exactMatch','mesh:D010461')]
assert keys(index['W05-FINAL-MAT-032']['after_rows'])==[('skos:exactMatch','MICRO:0000181')]
assert keys(index['W05-FINAL-MAT-030']['after_rows'])==[('skos:broadMatch','mesh:D010461'),('skos:exactMatch','kgmicrobe.ingredient:polypeptone')]
assert index['W05-PARENTS-BACTO-SOYTONE-CONTINUITY']['after_rows']==[]
assert ao['data/ingredients/mapped/Bacto_Soytone.yaml']['representative']==''
for lane in ['hepes','tris']:
 for p in j(S/lane/'proposals.json')['proposals']:
  assert len(index[p['proposal_id']]['after_rows'])==1
  assert not ao[p.get('destination_owner_path',p['owner_path'])].get('components')
  assert 'component_assertion' not in ao[p.get('destination_owner_path',p['owner_path'])]
q=V/'native-row-projections.json';assert not q.exists();q.write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),builder=dict(path=str(builder),sha256=sha(builder)),status='PASS',scope='All selected full payloads projected with complete substituted owner index and empty optional external dictionaries; no export or producer change.',before_overlay_records=len(bo),after_overlay_records=len(ao),reviewed_projections=out),indent=2)+'\n')
print(json.dumps(dict(status='PASS',all_payloads=len(ps),native_projection_rows=sum(len(x['after_rows']) for x in out),overlay_records=len(ao))))
