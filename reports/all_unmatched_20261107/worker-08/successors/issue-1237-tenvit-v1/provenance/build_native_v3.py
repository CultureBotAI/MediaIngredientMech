"""Native envelope shape correction; prior rejected drafts remain immutable."""
import datetime,hashlib,importlib.util,json,shutil
from pathlib import Path
R=Path.cwd();P=R/'.temp/all-unmatched-worker-08/tenvit-dependent-v1';O=R/'reports/all_unmatched_20261107/worker-08/successors/issue-1237-tenvit-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p):return str(p.relative_to(R))
def save(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
spec=importlib.util.spec_from_file_location('native_review_v3',R/'scripts/record_review.py');n=importlib.util.module_from_spec(spec);spec.loader.exec_module(n)
shutil.copy2(P/'build_native_v3.py',O/'provenance/build_native_v3.py');shutil.copy2(P/'native-build-v2.log',O/'provenance/native-build-attempt2.log')
review=json.loads((O/'native/review-content-v2.json').read_text());assert review['actions'][0]['finding_ids']==[] and isinstance(review['notes'],str)
review['notes']=[review['notes'],'The second draft failed because notes must be a list, not a scalar. This third draft changes only that native envelope shape and refreshes actual inspection provenance; both rejected drafts/logs remain. No source/payload or native gate is changed.']
now=datetime.datetime.now(datetime.timezone.utc);review['review_id']=now.strftime('%Y%m%dT%H%M%SZ')+'-w08-tenvit-dependent-successor';review['finished_at']=now.isoformat().replace('+00:00','Z')
inputs={x['path'] for x in review['source']['inputs']}|{rel(f) for f in O.rglob('*') if f.is_file()}
inspection=n.inspect_source(R,review['targets'],sorted(inputs));save(O/'native/inspection-v3.json',inspection);review['source']=inspection['source']
save(O/'native/review-content-v3.json',review);n.validate_review(review);path=n.save_review(R,review);assert n.read_review(R,rel(path))==review;md=path.with_name('review.md');assert md.read_text()==n.render_markdown(review)
save(O/'native/receipt.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','review_id':review['review_id'],'review_yaml':{'path':rel(path),'sha256':sha(path)},'review_markdown':{'path':rel(md),'sha256':sha(md)},'native_inspect_validate_save_read_render':True,'source_base':inspection['source']['git_revision'],'source_state':inspection['source']['state'],'input_count':len(inspection['source']['inputs']),'rejected_drafts_preserved':[{'path':rel(O/'native/review-content.json'),'sha256':sha(O/'native/review-content.json'),'reason':'required action finding_ids absent; corrected to [] without inventing a finding'},{'path':rel(O/'native/review-content-v2.json'),'sha256':sha(O/'native/review-content-v2.json'),'reason':'notes scalar instead of required list'}],'scientific_scope':'One full composed proposal and six-occurrence source case; no other owner approval.'})
print(json.dumps(json.loads((O/'native/receipt.json').read_text()),indent=2))
