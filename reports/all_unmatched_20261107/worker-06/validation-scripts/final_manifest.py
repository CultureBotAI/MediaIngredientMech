from pathlib import Path
import hashlib,json,datetime,subprocess
R=Path('reports/all_unmatched_20261107/worker-06');save=json.loads((R/'logs/native-save.json').read_text());native=[Path(v).relative_to(Path.cwd()) for v in save.values()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
review=json.loads((R/'research-a/final-diff-review.json').read_text())
print('Final diff review status',review.get('status',review.get('verdict')))
# Bind completion to the actual reviewer receipt; no source or owner release is inferred.
dump(R/'completion.json',{'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'worker_slot':6,'branch':subprocess.check_output(['git','branch','--show-current'],text=True).strip(),'frozen_base':'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99','assigned_count':188,'reviewed_count':188,'remaining_review_count':0,'selected_proposals':100,'evidence_records':1056,'preserved_downstream_hold_rows':88,'maintained_data_changes':False,'publication_status':'Reviewed evidence ready for authorized ordinary commit and push; commit identity is the enclosing Git commit, remote verification reported by session.','native_reviews':[{'path':str(p),'sha256':sha(p)} for p in native],'core_sha256':{f:sha(R/f) for f in ['decisions.json','evidence.json','proposals.json','source-holds.json']},'final_diff_review':{'path':'research-a/final-diff-review.json','sha256':sha(R/'research-a/final-diff-review.json')},'source_owner_export_approval':False,'merge_or_downstream_rebuild_performed':False,'extra_external_sessions_started':0})
source=Path(__file__);(R/'validation-scripts/final_manifest.py').write_bytes(source.read_bytes())
files=sorted([p for p in R.rglob('*') if p.is_file() and p.name!='SHA256SUMS']+native)
assert not any(p.is_symlink() for p in files)
manifest=R/'SHA256SUMS';manifest.write_text(''.join(sha(p)+'  '+str(p)+'\n' for p in files))
for line in manifest.read_text().splitlines():
 expected,path=line.split('  ',1);assert sha(Path(path))==expected,path
print('Manifest verified',len(files),'files; SHA256',sha(manifest))
