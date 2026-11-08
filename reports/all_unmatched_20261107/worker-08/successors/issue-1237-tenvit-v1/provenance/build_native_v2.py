"""Correct required native action shape only; preserve first rejected review draft."""
import datetime,hashlib,importlib.util,json,shutil
from pathlib import Path
R=Path.cwd();P=R/'.temp/all-unmatched-worker-08/tenvit-dependent-v1';O=R/'reports/all_unmatched_20261107/worker-08/successors/issue-1237-tenvit-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p):return str(p.relative_to(R))
def save(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
spec=importlib.util.spec_from_file_location('native_review_v2',R/'scripts/record_review.py');n=importlib.util.module_from_spec(spec);spec.loader.exec_module(n)
shutil.copy2(P/'build_native_v2.py',O/'provenance/build_native_v2.py');shutil.copy2(P/'native-build.log',O/'provenance/native-build-attempt1.log')
review=json.loads((O/'native/review-content.json').read_text());assert len(review['actions'])==1 and 'finding_ids' not in review['actions'][0]
review['actions'][0]['finding_ids']=[]
now=datetime.datetime.now(datetime.timezone.utc);review['review_id']=now.strftime('%Y%m%dT%H%M%SZ')+'-w08-tenvit-dependent-successor';review['finished_at']=now.isoformat().replace('+00:00','Z')
review['notes']='The first native draft failed validation because the coordinator follow-up action omitted the required finding_ids list. That rejected draft and actual error log are preserved; this draft adds the empty list because no new finding is claimed or closed. Scientific content and all reviewed payload/selection bytes are unchanged. Actual Claw projection retains identity/label/predicate/aliases but correctly changes only curator/date provenance with the appended history; no canonical export was written.'
inputs={x['path'] for x in review['source']['inputs']}|{rel(f) for f in O.rglob('*') if f.is_file()}
inspection=n.inspect_source(R,review['targets'],sorted(inputs));save(O/'native/inspection-v2.json',inspection);review['source']=inspection['source']
save(O/'native/review-content-v2.json',review);n.validate_review(review);path=n.save_review(R,review);assert n.read_review(R,rel(path))==review;md=path.with_name('review.md');assert md.read_text()==n.render_markdown(review)
save(O/'native/receipt.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','review_id':review['review_id'],'review_yaml':{'path':rel(path),'sha256':sha(path)},'review_markdown':{'path':rel(md),'sha256':sha(md)},'native_inspect_validate_save_read_render':True,'source_base':inspection['source']['git_revision'],'source_state':inspection['source']['state'],'input_count':len(inspection['source']['inputs']),'first_rejected_draft_preserved':{'path':rel(O/'native/review-content.json'),'sha256':sha(O/'native/review-content.json'),'reason':'missing required action finding_ids list; corrected to [] without inventing a finding'},'scientific_scope':'One full composed proposal and six-occurrence source case; no other owner approval.'})
print(json.dumps(json.loads((O/'native/receipt.json').read_text()),indent=2))
