"""Revalidate active proposed payloads through the native writer into private scratch."""
import datetime,hashlib,json,sys
from pathlib import Path
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient
S=Path(__file__).resolve().parents[1];W=Path(__file__).resolve().parents[3];R=Path(__file__).resolve().parents[6]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def replay():
 ps=json.loads((S/'proposals.json').read_text())['proposals'];out=R/'.temp/all-unmatched-worker-04/issue-1201-v1/guarded-replay';out.mkdir(parents=True,exist_ok=True);rows=[]
 for p in ps:
  source=W/p['after_capture']['path'];assert sha(source)==p['after_capture']['sha256'];record=yaml.safe_load(source.read_text());target=out/(hashlib.sha256(p['proposal_id'].encode()).hexdigest()+'.yaml')
  write_validated_ingredient(record,target)
  assert yaml.safe_load(target.read_text())==record
  assert sha(source)==p['after_capture']['sha256']
  rows.append({'proposal_id':p['proposal_id'],'input':str(source.relative_to(R)),'input_sha256':sha(source),'scratch_output':str(target.relative_to(R)),'output_sha256':sha(target),'semantic_roundtrip_identical':True})
 result={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','payload_count':len(rows),'scope':'Native guarded writer replay to private scratch only; no maintained or published proposal bytes changed. No extra curation event is added during replay.','rows':rows};(S/'validation/guarded-writer-replay.json').write_text(json.dumps(result,indent=2)+'\n');print('guarded writer replay PASS',len(rows))
if __name__=='__main__':replay()
