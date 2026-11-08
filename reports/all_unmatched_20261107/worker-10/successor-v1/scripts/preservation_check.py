from pathlib import Path
import hashlib,json,subprocess
from datetime import datetime,timezone
R=Path.cwd();P=R/'reports/all_unmatched_20261107/worker-10';S=P/'successor-v1';sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
checks=[]
for line in (P/'SHA256SUMS').read_text().splitlines():
 h,n=line.split(None,1);f=R/n.lstrip('*');assert sha(f)==h,n;checks.append({'path':n,'sha256':h})
paths=['data','mappings','UNIFIED_INGREDIENT_MAPPING.tsv','docs/data','conf','src','schema','scripts','justfile','MAPPING_SEMANTICS.md']
r=subprocess.run(['git','diff','--name-only','e000d66dd26ab053e9b17ce7bf8d3c873c3dde99','--',*paths],capture_output=True,text=True);assert r.returncode==0 and not r.stdout,r.stdout
old=subprocess.run(['git','diff','--name-only','dbaf4629f3b93d3bd8a78028e243abfe90c7a922','--','reports/all_unmatched_20261107/worker-10','reviews/structured/20261108T052619Z-w10-source-owner-identity-review'],capture_output=True,text=True);assert old.returncode==0
allowed='reports/all_unmatched_20261107/worker-10/successor-v1/'
assert all(p.startswith(allowed) for p in old.stdout.splitlines()),old.stdout
(S/'predecessor-preservation.json').write_text(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'head':'dbaf4629f3b93d3bd8a78028e243abfe90c7a922','prior_manifest_sha256':sha(P/'SHA256SUMS'),'verified_prior_manifest_entries':len(checks),'all_old_capture_hashes_match':True,'maintained_path_diff_against_frozen_base':r.stdout,'maintained_paths_checked':paths,'new_files_only_under_successor_root':True,'prior_native_review_yaml_sha256':sha(R/'reviews/structured/20261108T052619Z-w10-source-owner-identity-review/review.yaml'),'prior_native_review_md_sha256':sha(R/'reviews/structured/20261108T052619Z-w10-source-owner-identity-review/review.md'),'qualification':'Append-only successor; original rejections, successful issue receipts and scientific reviews remain byte-identical. No reset/amend/forcepush.'},indent=2)+'\n');print('prior',len(checks),'preserved; maintaineddiff empty')
