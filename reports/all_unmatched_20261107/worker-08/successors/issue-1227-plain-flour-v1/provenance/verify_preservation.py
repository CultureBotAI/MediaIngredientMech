import datetime,hashlib,json,subprocess
from pathlib import Path
ROOT=Path.cwd();P=ROOT/'.temp/all-unmatched-worker-08/plain-flour-method-v1';O=ROOT/'reports/all_unmatched_20261107/worker-08/successors/issue-1227-plain-flour-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lines_manifest(path):
    rows=[]
    for line in path.read_text().splitlines():
        if not line.strip():continue
        digest,name=line.split(None,1);name=name.lstrip('* ')
        f=ROOT/name
        if not f.is_file(): f=path.parent/name
        assert f.is_file() and sha(f)==digest,name
        rows.append({'path':str(f.relative_to(ROOT)),'sha256':digest})
    return rows
expected={
 'reports/all_unmatched_20261107/worker-08/successors/issue-1227-v1/MANIFEST.sha256':'82ad0dd30e4c967414b7cd961f235006ee3a30b6e13f63c34842b344f014c430',
 '.temp/all-unmatched-worker-08/issue-1227-v1/referral-confirmation-v1/MANIFEST.sha256':'2b994665b95ac9ecef1c799ae5905ff30d45468b3e288aa49bd51a43e2eceba9',
 '.temp/w05-published-head-independent-review-v1/MANIFEST.sha256':'ed37df619a208c16f9ad1180dc9aa800202e007de8eb0d7085e7ac45fc1e6166',
 '.temp/w06-residual-successor-independent-v1/MANIFEST.json':'bcdfe076dc1273e42278ac76c999fe75225c9619375414427476fd3ef04fb12c',
 '.temp/w06-residual-successor-independent-v1/SEAL.json':'b9eaf3bc9ef39dc36c440fb1330677fa267b1945ba1c65c2b24c4e8d4278226f',
 '.temp/w05-published-head-independent-review-v1/SEAL.json':'10cec75731185834ba19ec3705a00f63061dcc26e450fea82bdf620e3b8b5578',
}
groups=[]
for path,digest in expected.items():
    f=ROOT/path;assert sha(f)==digest,path
    if path.endswith('.sha256'):members=lines_manifest(f)
    elif f.name=='MANIFEST.json':
        members=json.loads(f.read_text())['members']
        for r in members:assert sha(f.parent/r['path'])==r['sha256'],r['path']
        assert {x.relative_to(f.parent).as_posix() for x in f.parent.rglob('*') if x.is_file()}-{'MANIFEST.json','SEAL.json'}=={r['path'] for r in members}
    else:members=[]
    groups.append({'path':path,'sha256':digest,'members_verified':len(members)})
subprocess.run(['git','diff','--exit-code','HEAD','--'],check=True,capture_output=True)
base=subprocess.check_output(['git','ls-tree','-r','--name-only','HEAD'],text=True).splitlines()
receipt={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'prior_tracked_files':len(base),'prior_tracked_changes':[],'method':'git diff HEAD verifies all tracked predecessor bytes; every named prior source/review/confirmation manifest and member separately rehashed. W06 manifest inventory checked exactly including ignored files.','manifest_groups':groups,'sealed_w06_review_modified':False,'sealed_w05_review_modified':False,'original_source_artifacts_modified':False,'full_root_1701_review':'Still separately owned by coordinator; this task reads only the filed immutable finding and does not edit or claim its final result.'}
f=O/'preservation.json'
with f.open('x') as out:json.dump(receipt,out,indent=2);out.write('\n')
print(json.dumps(receipt,indent=2))
