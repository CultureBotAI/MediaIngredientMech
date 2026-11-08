"""Inspect eight exact final targets with original-source hash provenance."""
import json,hashlib,subprocess,sys
from pathlib import Path
import yaml
R=Path(__file__).resolve().parent;W=R.parents[3];A=R.parent
sys.path.insert(0,str(R));import build_successor_v2 as b
def load(p):return json.loads(p.read_text())
def rel(p):return str(p.relative_to(W))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 out=R/'native-inspection-v1';out.mkdir(exist_ok=False);inputs=set();copies=[];folder=R/'context/native-external-inputs';folder.mkdir(exist_ok=False)
 already={x['original_path']:W/x['copy_path'] for x in load(R/'context/frozen-recipe-copies.json')}
 for row in load(R/'independent/scientific-review-v1.json')['input_hash_manifest']:
  p=Path(row['path']);p=p if p.is_absolute() else W/p;assert sha(p)==row['sha256']
  if p.is_relative_to(W):inputs.add(rel(p));continue
  target=already.get(str(p)) or folder/(row['sha256'][:16]+'-'+p.name)
  if target.exists():assert target.read_bytes()==p.read_bytes()
  else:
   with target.open('xb') as f:f.write(p.read_bytes())
  copies.append({'original_path':str(p),'copy_path':rel(target),'sha256':sha(target),'timestamp_policy':'Original exact source bytes and original retrieval provenance retained; this local copy is not a fresh primary capture.'});inputs.add(rel(target))
 with (R/'context/native-external-copy-receipt.json').open('x') as f:json.dump(copies,f,indent=2);f.write('\n')
 ds=load(R/'selected-v1/decisions.json')['decisions'];ps=load(R/'selected-v1/proposals.json')['proposals'];d=ds[58]
 targets=[{'target_id':d['case_id'],'path':rel(R/'selected-v1/decisions.json'),'selector':f'decisions[case_id={d["case_id"]}]','label':d['source']['source_label'],'kind':'snapshot_row','ownership_note':'Frozen case58, all24 occurrences retained; only seven bounded category corrections re-reviewed; source/owner/release holds remain.'}]
 for pid in b.TARGET_IDS:
  p=next(x for x in ps if x['proposal_id']==pid);targets.append({'target_id':'PROPOSAL:'+pid,'path':rel(A/p['after_capture']['path']),'label':pid,'kind':'source','ownership_note':'Complete isolated candidate for '+p['owner_path']+'; only category/history correction assessed, not maintained application or full owner/component/release approval.'})
 with (out/'targets.yaml').open('x') as f:yaml.safe_dump({'targets':targets},f,sort_keys=False,allow_unicode=True)
 inputs.update(rel(p) for p in R.rglob('*') if p.is_file() and not p.is_relative_to(out) and p.suffix!='.pyc' and '__pycache__' not in p.parts)
 inputs.update(rel(A/'filed-followups-v1'/p) for p in ['selected-v3/decisions.json','selected-v3/proposals.json','selected-v3/evidence.json','MANIFEST.json','SHA256SUMS','HANDOFF.json','native-pair-binding.json'])
 inputs.update(['MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','schema/record_review.yaml','conf/record_review.yaml','docs/record-reviews.md','docs/record-review-profile.md','src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/curate/curation_event.py','src/mediaingredientmech/curate/publication_guard.py','src/mediaingredientmech/ingredient_bundle_refresh.py','reviews/structured/20261108T085805Z-w02-filed-followups-independent/review.yaml'])
 cmd=[sys.executable,'-B','scripts/record_review.py','inspect','--targets',rel(out/'targets.yaml')]
 for p in sorted(inputs):cmd+=['--input',p]
 process=subprocess.run(cmd,cwd=W,capture_output=True,text=True)
 for name,text in [('inspection.json',process.stdout),('inspect.stderr',process.stderr),('command.json',json.dumps({'argv':cmd,'exit_code':process.returncode},indent=2))]:
  with (out/name).open('x') as f:f.write(text)
 assert process.returncode==0,process.stderr
 result=json.loads(process.stdout);print(json.dumps({'targets':len(targets),'inputs':len(result['source']['inputs']),'inspection_sha256':sha(out/'inspection.json')}))
if __name__=='__main__':main()
