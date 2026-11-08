from pathlib import Path
import json,subprocess,shutil,hashlib
R=Path('reports/all_unmatched_20261107/worker-06');T=Path('.temp/all-unmatched-worker-06/invariant-controls');T.mkdir(exist_ok=True);(T/'logs').mkdir(exist_ok=True)
for f in ['decisions.json','evidence.json','proposals.json','source-holds.json']:shutil.copyfile(R/f,T/f)
for p in json.loads((R/'proposals.json').read_text())['proposals']:
 dst=T/p['after_capture']['path'];dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(R/p['after_capture']['path'],dst)
src=Path('.temp/all-unmatched-worker-06/final_invariants.py');code=src.read_text();assert code.count("Path('reports/all_unmatched_20261107/worker-06')")==1
script=T/'fixture_checker.py';script.write_text(code.replace("Path('reports/all_unmatched_20261107/worker-06')",repr(str(T)) if False else 'Path('+repr(str(T))+')'))
PY='/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.venv/bin/python';results=[]
def run(label,expected,needle=None):
 r=subprocess.run([PY,str(script)],capture_output=True,text=True);out=json.loads((T/'logs/final-invariants.json').read_text());assert (r.returncode==0)==expected,(label,r.stdout,r.stderr)
 if needle:assert any(needle in e for e in out['errors']),out
 results.append({'control':label,'exit_code':r.returncode,'expected_pass':expected,'observed_errors':out['errors'],'result':'PASS'})
run('unchanged final bundle',True)
h=json.loads((T/'source-holds.json').read_text());h['cases'][0]['frozen_case_sha256']='0'*64;(T/'source-holds.json').write_text(json.dumps(h));run('tampered full source-case digest rejected',False,'Hold full-case digest');shutil.copyfile(R/'source-holds.json',T/'source-holds.json')
d=json.loads((T/'decisions.json').read_text());d['decisions'].pop();(T/'decisions.json').write_text(json.dumps(d));run('missing assigned case rejected',False,'Case cardinality')
p={'status':'PASS','checker_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'source_bundle_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['decisions.json','evidence.json','proposals.json','source-holds.json']},'fixture_location':str(T),'maintained_files_changed':False,'controls':results}
(R/'logs/invariant-controls.json').write_text(json.dumps(p,indent=2)+'\n');shutil.copyfile(Path(__file__),R/'validation-scripts/invariant_controls.py');print('3 invariant controls PASS; fixtures only')
