import hashlib,json,shutil,subprocess
from pathlib import Path
R=Path.cwd();P=R/'.temp/mc-dependent-successor-v1';A=R/'reports/all_unmatched_20261107/worker-08';O=A/'successors/issue-1237-mc-dependent-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n')
checks=[]
for row in read(P/'entry.json')['prior_seals']:
 assert sha(Path(row['path']))==row['sha256'];checks.append(row)
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==read(P/'entry.json')['head']
subprocess.run(['git','diff','--exit-code','HEAD'],check=True,capture_output=True)
refs=[];T=P/'final-review'
for source in T.iterdir():
 if source.is_file() and source.suffix in ['.py','.json','.log']:
  dst=O/'validation'/source.name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dst);refs.append({'original_path':str(source),'published_path':str(dst.relative_to(R)),'sha256':sha(dst)})
for folder in ['native-attempt-v1','native-attempt-v2','projection-attempt-v3']:
 for source in (T/folder).iterdir():
  if not source.is_file() or source.suffix not in ['.json','.yaml']:continue
  dst=O/'validation'/folder/source.name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dst);refs.append({'original_path':str(source),'published_path':str(dst.relative_to(R)),'sha256':sha(dst)})
save(O/'validation/capture-bindings.json',refs)
save(O/'preservation.json',{'head':read(P/'entry.json')['head'],'tracked_diff_against_entry':'empty before new report staging','old_seal_top_level_pins_rehashed':checks,'old_full_archive_revalidation':'Not rerun; no old packet was edited. Prior exact seals and original source/core byte checks bridge prior complete validations.','source_evidence_prefix_verified_by_current_native_audit':1101,'old_payload_bytes_verified_current':114,'new_work_paths_only':['.temp/mc-dependent-successor-v1','reports/all_unmatched_20261107/worker-08/successors/issue-1237-mc-dependent-v1','reports/all_unmatched_20261107/worker-08/ACTIVE-SUCCESSOR-mc-v1.json','new reviews/structured native pair'],'maintained_owner_sha256':sha(R/'data/ingredients/mapped/Mc_vitamins.yaml'),'old_CB_payload_sha256':sha(A/'successors/issue-1237-tenvit-v1/payloads/Wolfes_Vitamin_Mix.yaml'),'scope':'Preservation checks, not renewed science or maintained owner application.'})
shutil.copy2(Path(__file__),O/'provenance/prepare_native.py')
print(json.dumps({'copied_technical_evidence':len(refs),'old_seals_rehashed':len(checks)}))
