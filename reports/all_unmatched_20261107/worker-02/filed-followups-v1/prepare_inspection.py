"""Capture exact six-target native review input after technical validation."""
import json,hashlib,subprocess,sys
from pathlib import Path
import yaml
R=Path(__file__).resolve().parent;W=R.parents[3];A=R.parent;O=W/'.temp/w02-filed-followups-v1'
def load(p):return json.loads(p.read_text())
def rel(p):return str(p.relative_to(W))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 out=R/'native-inspection-v1';out.mkdir(exist_ok=False)
 for src,dst in [(O/'native-v1/receipt.json',R/'validation/native-receipt-v1.json'),(O/'tests/tests-v1.log',R/'validation/tests-v1.log'),(O/'tests/results-v1.xml',R/'validation/tests-v1.xml')]:
  with dst.open('xb') as f:f.write(src.read_bytes())
 primary=load(R/'independent/primary-review-v1.json');inputs=set()
 copies=[];folder=R/'context/frozen-recipes';folder.mkdir(exist_ok=False)
 for entry in primary['input_hash_manifest']:
  p=Path(entry['path']);assert sha(p)==entry['sha256']
  if p.is_relative_to(W):inputs.add(rel(p))
  else:
   target=folder/(entry['sha256'][:16]+'-'+p.name)
   if target.exists():assert target.read_bytes()==p.read_bytes()
   else:
    with target.open('xb') as f:f.write(p.read_bytes())
   copies.append({'original_path':str(p),'copy_path':rel(target),'sha256':sha(target),'timestamp_policy':'Exact original frozen bytes; no new primary-access timestamp asserted.'});inputs.add(rel(target))
 with (R/'context/frozen-recipe-copies.json').open('x') as f:json.dump(copies,f,indent=2);f.write('\n')
 ds=load(R/'review-input-v2/decisions.json')['decisions'];ps=load(R/'review-input-v2/proposals.json')['proposals'];targets=[]
 for i in [88,93,114,118]:
  d=ds[i];targets.append({'target_id':d['case_id'],'path':rel(R/'review-input-v2/decisions.json'),'selector':f'decisions[case_id={d["case_id"]}]','label':d['source']['source_label'],'kind':'snapshot_row','ownership_note':'Bounded frozen source-case correction only; source/owner/role/release holds unchanged.'})
 for pid in ['b2-proposal-sodium_resazurin_01_percent_wv_jcm363_1023','b2-proposal-sulfuric_acid_10n_named_sources']:
  p=next(x for x in ps if x['proposal_id']==pid);targets.append({'target_id':'PROPOSAL:'+pid,'path':rel(A/p['after_capture']['path']),'label':pid,'kind':'source','ownership_note':'Complete isolated candidate for '+p['owner_path']+'; new owner remains unintegrated and no owner/release approval follows.'})
 with (out/'targets.yaml').open('x') as f:yaml.safe_dump({'targets':targets},f,sort_keys=False,allow_unicode=True)
 inputs.update(rel(p) for p in R.rglob('*') if p.is_file() and not p.is_relative_to(out))
 inputs.update(rel(A/'final-corrections-v1'/p) for p in ['review-bound-v1/decisions.json','review-bound-v1/proposals.json','review-bound-v1/evidence.json','MANIFEST.json','SHA256SUMS','HANDOFF.json','independent/scientific-review-v1.json','lineage-v1/retained-holds.json'])
 inputs.update(['MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','schema/record_review.yaml','conf/record_review.yaml','docs/record-reviews.md','docs/record-review-profile.md','src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/curate/curation_event.py','src/mediaingredientmech/curate/publication_guard.py','src/mediaingredientmech/ingredient_bundle_refresh.py','reviews/structured/20261108T083222Z-w02-final-corrections-independent/review.yaml'])
 cmd=[sys.executable,'-B','scripts/record_review.py','inspect','--targets',rel(out/'targets.yaml')]
 for p in sorted(inputs):cmd+=['--input',p]
 process=subprocess.run(cmd,cwd=W,capture_output=True,text=True)
 for name,text in [('inspection.json',process.stdout),('inspect.stderr',process.stderr),('command.json',json.dumps({'argv':cmd,'exit_code':process.returncode},indent=2))]:
  with (out/name).open('x') as f:f.write(text)
 assert process.returncode==0,process.stderr
 result=json.loads(process.stdout);print(json.dumps({'targets':len(targets),'inputs':len(result['source']['inputs']),'inspection_sha256':sha(out/'inspection.json')}))
if __name__=='__main__':main()
