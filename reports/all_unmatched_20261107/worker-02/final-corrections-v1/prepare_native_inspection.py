"""Capture native exact review inputs only; scientific judgment is independent."""
from pathlib import Path
import json,hashlib,subprocess,sys
import yaml
R=Path(__file__).resolve().parent;W=R.parents[3];A=R.parent;O=W/'.temp/w02-final-corrections-v1'
def load(p):return json.loads(p.read_text())
def rel(p):return str(p.relative_to(W))
def copynew(src,dst):
 with dst.open('xb') as f:f.write(src.read_bytes())
def main():
 out=R/'native-v1';out.mkdir(exist_ok=False)
 copynew(O/'native-v1/receipt.json',R/'validation/native-v1-receipt.json')
 copynew(O/'helper-tests-v4.log',R/'validation/helper-tests-v4.log')
 copynew(O/'results-v4.xml',R/'validation/results-v4.xml')
 s=R/'review-selection-v1';ds=load(s/'decisions.json')['decisions'];ps=load(s/'proposals.json')['proposals'];es=load(s/'evidence.json')['evidence']
 targets=[]
 for d in ds:
  t={'target_id':d['case_id'],'path':rel(A/'context/frozen-shard-02.json'),'selector':f'cases[case_id={d["case_id"]}]','label':d['source']['source_label'],'kind':'snapshot_row','record_class':'Frozen source ingredient case'}
  if d['owner_records']:t['owner_paths']=[{'repository':'CultureBotAI/MediaIngredientMech','path':x['path'],'role':'Authentic baseline comparison only; candidate or full owner approval not implied'} for x in d['owner_records']]
  else:t['ownership_note']='Source-only case; no actual maintained owner established. Proposed paths remain candidates.'
  targets.append(t)
 for p in ps:
  t={'target_id':'PROPOSAL:'+p['proposal_id'],'path':rel(A/p['after_capture']['path']),'label':p['proposal_id'],'kind':'source','record_class':'Complete isolated candidate IngredientRecord','ownership_note':'Candidate only for '+p['owner_path']+'; no maintained write or release approval.'}
  if p['kind']=='edit_existing_owner':t['owner_paths']=[{'repository':'CultureBotAI/MediaIngredientMech','path':p['owner_path'],'role':'Current authentic preimage for proposed edit; does not approve whole owner'}]
  targets.append(t)
 with (out/'targets.yaml').open('x') as f:yaml.safe_dump({'targets':targets},f,sort_keys=False,allow_unicode=True)
 inputs=set()
 for folder in ['review-selection-v1','lineage-v1','context','chemistry','preparations','root-v2','water','typed-v1','independent','validation']:
  inputs.update(rel(p) for p in (R/folder).rglob('*') if p.is_file() and p.suffix not in ['.pyc'])
 inputs.update(rel(p) for p in R.glob('*.json'))
 inputs.update(rel(p) for p in R.glob('*.py'))
 inputs.update(rel(A/e['capture']['path']) for e in es if e['capture']['root']=='artifact')
 inputs.update(x['path'] for d in ds for x in d['owner_records'])
 inputs.update(['MAPPING_SEMANTICS.md','schema/record_review.yaml','conf/record_review.yaml','docs/record-reviews.md','docs/record-review-profile.md','docs/stock_components.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','uv.lock'])
 inputs.update(rel(p) for p in (W/'reviews/structured').glob('*/review.yaml'))
 command=[sys.executable,'-B','scripts/record_review.py','inspect','--targets',rel(out/'targets.yaml')]
 for x in sorted(inputs):command+=['--input',x]
 proc=subprocess.run(command,cwd=W,capture_output=True,text=True)
 with (out/'inspect.stdout').open('x') as f:f.write(proc.stdout)
 with (out/'inspect.stderr').open('x') as f:f.write(proc.stderr)
 with (out/'inspect-command.json').open('x') as f:json.dump({'argv':command,'exit_code':proc.returncode,'targets':len(targets),'extra_inputs':len(inputs)},f,indent=2)
 if proc.returncode:raise RuntimeError(proc.stderr)
 parsed=json.loads(proc.stdout)
 with (out/'inspection.json').open('x') as f:json.dump(parsed,f,indent=2);f.write('\n')
 print(json.dumps({'targets':len(targets),'inputs':len(parsed['source']['inputs']),'inspection_sha256':hashlib.sha256((out/'inspection.json').read_bytes()).hexdigest()}))
if __name__=='__main__':main()
