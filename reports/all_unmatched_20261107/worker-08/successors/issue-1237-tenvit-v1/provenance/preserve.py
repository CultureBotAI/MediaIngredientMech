import datetime,hashlib,importlib.util,json,subprocess,shutil
from pathlib import Path
R=Path.cwd();P=R/'.temp/all-unmatched-worker-08/tenvit-dependent-v1';O=R/'reports/all_unmatched_20261107/worker-08/successors/issue-1237-tenvit-v1'
spec=importlib.util.spec_from_file_location('pres',R/'.temp/crosswalk1247-v3-independent-v1/verify_preservation.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rows=[]
packets=[('.temp/w05-published-head-independent-review-v1','MANIFEST.sha256',False),('.temp/w06-residual-successor-independent-v1','MANIFEST.json',False),('.temp/crosswalk1247-v3-independent-v1','MANIFEST.json',False),('.temp/all-unmatched-worker-08/plain-flour-method-v1','MANIFEST.sha256',True),('reports/all_unmatched_20261107/worker-08/successors/issue-1227-plain-flour-v1','MANIFEST.sha256',True),('reports/all_unmatched_20261107/worker-08/successors/issue-1227-v1','MANIFEST.sha256',True),('.temp/all-unmatched-worker-08/issue-1227-v1/referral-confirmation-v1','MANIFEST.sha256',True)]
(P/'preservation').mkdir()
for i,(path,name,repo) in enumerate(packets):
 result=m.verify_manifest(R/path,name,member_base=R if repo else None);assert result['all_match']
 m.dump(P/'preservation'/f'members-{i}.json',result)
 rows.append({'path':path,'manifest':name,'sha256':result['manifest_sha256'],'members_verified':len(result['members'])})
inv=m.inventory(R/'.temp/crosswalk1247-v3-independent-v1');m.dump(P/'preservation/helper-inventory.json',inv)
subprocess.run(['git','diff','--exit-code','HEAD','--'],check=True,capture_output=True)
receipt={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'all_original_tracked_bytes_unchanged':True,'packets':rows,'helper_regular_files':len(inv['files']),'helper_symlinks_not_followed':inv['symlinks_not_followed'],'method':'Every named prior manifest member rehashed with O_NOFOLLOW and ancestor symlink check; fixture symlinks lstat/readlink only. Ignored files included. No writes to old packets. git diff HEAD confirms no prior tracked change.'}
m.dump(O/'preservation.json',receipt);shutil.copy2(P/'preserve.py',O/'provenance/preserve.py')
print(json.dumps({'status':'PASS','packets':rows,'symlinks_unfollowed':len(inv['symlinks_not_followed'])},indent=2))
