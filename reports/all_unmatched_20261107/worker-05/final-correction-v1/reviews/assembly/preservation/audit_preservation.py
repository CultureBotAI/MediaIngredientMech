from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, collections

W = Path.cwd()
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
B = W/'reports/all_unmatched_20261107/worker-05'
N = B/'correction-1193-v1'
F = W/'.temp/final-preparation-comparison-v1'
O = W/'.temp/w05-final-correction-v1/review-assembly/preservation'
HEAD = '43f7cf6e8681fa617b5d6d3529d94d537ca01f0d'
WHO = '/root/final_skeptical/preservation_audit'
errors=[]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def hbytes(b): return hashlib.sha256(b).hexdigest()
def objsha(x): return hbytes(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def load(p): return json.loads(p.read_text())
def run(*args):
    p=subprocess.run(args,cwd=W,capture_output=True)
    if p.returncode: raise RuntimeError((args,p.returncode,p.stderr.decode()))
    return p.stdout
def check(value,message):
    if not value: errors.append(message)
def save(name,obj):
    p=O/name
    assert not p.exists(),p
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')

at=datetime.now(timezone.utc).isoformat()
githead=run('git','rev-parse','HEAD').decode().strip()
branch=run('git','branch','--show-current').decode().strip()
status=run('git','status','--porcelain=v1').decode()
changed=run('git','diff','--name-status',HEAD,'--').decode()
check(githead==HEAD,'current source head differs')
check(branch=='review/all-unmatched-w05-source-review-20261107','branch differs')
check(not status,'git status contains tracked/unignored changes')
check(not changed,'tracked working tree changes against source head')

# These two source-head tracked artifacts authenticate the original frozen boundary
# and the historical report manifest; no filesystem assumption replaces Git bytes.
authenticated=[]
for rel in ['reports/all_unmatched_20261107/worker-05/contracts/shard-05.json',
            'reports/all_unmatched_20261107/worker-05/correction-1193-v1/MANIFEST.sha256']:
    old=run('git','show',HEAD+':'+rel)
    cur=(W/rel).read_bytes()
    check(old==cur,'source-head artifact changed: '+rel)
    authenticated.append(dict(path=rel,source_head=HEAD,source_head_sha256=hbytes(old),current_sha256=hbytes(cur),exact=old==cur))

ownership={};shards=[];all_cases=[]
for p in sorted((C/'queue/preliminary-v5/shards').glob('shard-*.json')):
    data=load(p);slot=data['worker_slot'];cases=data['cases']
    for case in cases:
        cid=case['case_id']
        check(cid not in ownership,'duplicate campaign case: '+cid)
        ownership[cid]=dict(worker=slot,case_input_sha256=objsha(case))
        all_cases.append(case)
    shards.append(dict(path=str(p),sha256=sha(p),worker=slot,cases=len(cases)))
check(len(shards)==10,'campaign shard count differs')
check(len(ownership)==len(all_cases)==1879,'campaign ownership count differs')
queue5=C/'queue/preliminary-v5/shards/shard-05.json'
contract=B/'contracts/shard-05.json'
expected='457c957af21271b120190093dd311bf4044b82a3ad26b54e2fc5b52083dec1c4'
check(sha(queue5)==sha(contract)==expected,'W05 shard SHA differs')
check(len(load(queue5)['cases'])==188,'W05 case count differs')
old_ownership=load(N/'validation/campaign-ownership.json')['ownership']
comparison_ownership=load(F/'control/campaign-ownership-accounting-v1.json')['ownership']
check({k:v['worker'] for k,v in ownership.items()}==old_ownership,'ownership differs from published source-head report')
check(ownership==comparison_ownership,'ownership/content differs from sealed comparison')

historical_members=[]
seen=set()
for line in (N/'MANIFEST.sha256').read_text().splitlines():
    digest,rel=line.split(None,1);rel=rel.lstrip('*')
    p=N/rel
    check(rel not in seen,'duplicate historical manifest member: '+rel);seen.add(rel)
    got=sha(p) if p.is_file() else None
    check(got==digest,'historical member hash mismatch: '+rel)
    historical_members.append(dict(path=rel,expected_sha256=digest,actual_sha256=got,bytes=p.stat().st_size if p.is_file() else None))

fm=load(F/'MANIFEST.json');comparison_members=[]
for row in fm['files']:
    p=F/row['path'];got=sha(p) if p.is_file() else None
    check(got==row['sha256'],'comparison member hash mismatch: '+row['path'])
    check(p.is_file() and p.stat().st_size==row['bytes'],'comparison member size mismatch: '+row['path'])
    comparison_members.append(dict(path=row['path'],expected_sha256=row['sha256'],actual_sha256=got,bytes=p.stat().st_size if p.is_file() else None))
expected_files={x['path'] for x in fm['files']}|{'MANIFEST.json'}
actual_files={str(p.relative_to(F)) for p in F.rglob('*') if p.is_file()}
check(expected_files==actual_files,'private comparison file set changed')
check(fm['counts']['families']==22,'comparison family count differs')
check(fm['published_source_head_preserved']==HEAD,'comparison source head differs')
assignment=Path(fm['assignment'])
check(sha(assignment)==fm['assignment_sha256']=='1e781cb9b681e3d229501cb97376f8e7e922ee5c2b8e3d9d4b14a3755320d7a9','comparison assignment hash differs')
comparison_git_entry=run('git','ls-tree','-r','--name-only',HEAD,'--','.temp/final-preparation-comparison-v1/MANIFEST.json').decode().strip()

save('campaign-ownership.json',dict(reviewer=WHO,at=at,scope='Mechanical source ownership and frozen case-content preservation only',shards=shards,ownership=ownership,total_unique_cases=len(ownership),worker05_cases=sum(v['worker']==5 for v in ownership.values()),published_ownership_exact=({k:v['worker'] for k,v in ownership.items()}==old_ownership),comparison_ownership_and_content_exact=(ownership==comparison_ownership)))
save('historical-manifest-member-checks.json',dict(reviewer=WHO,manifest=dict(path=str(N/'MANIFEST.sha256'),sha256=sha(N/'MANIFEST.sha256')),members=historical_members))
save('comparison-manifest-member-checks.json',dict(reviewer=WHO,manifest=dict(path=str(F/'MANIFEST.json'),sha256=sha(F/'MANIFEST.json')),members=comparison_members,actual_file_set_exact=expected_files==actual_files))
receipt=dict(reviewer=WHO,completed_at=datetime.now(timezone.utc).isoformat(),scope='Narrow independent mechanical preservation audit; no chemical identity or final canonical assembly approval',git=dict(head=githead,branch=branch,status_porcelain=status,diff_from_source_head=changed),authenticated_source_head_artifacts=authenticated,campaign=dict(shards=len(shards),unique_cases=len(ownership),worker05_cases=sum(v['worker']==5 for v in ownership.values()),source_case_content_sha_algorithm='SHA256 compact sorted-key UTF-8 JSON, ensure_ascii=false',ownership_exact_to_published_and_comparison=True),historical_report=dict(manifest_sha256=sha(N/'MANIFEST.sha256'),members=len(historical_members),hash_mismatches=sum(x['actual_sha256']!=x['expected_sha256'] for x in historical_members),git_authenticated=True),comparison=dict(manifest_sha256=sha(F/'MANIFEST.json'),members=len(comparison_members),families=fm['counts']['families'],assignment_sha256=sha(assignment),hash_mismatches=sum(x['actual_sha256']!=x['expected_sha256'] for x in comparison_members),all_private_files_accounted=expected_files==actual_files,source_head_binding=fm['published_source_head_preserved'],git_tracked_at_original_head=bool(comparison_git_entry),git_authentication_limit='The private comparison packet is gitignored and absent from the original source-head tree. It is bound by its current immutable manifest and frozen assignment, not claimed to have been committed in source head.'),limitations=['No chemical, source-applicability, owner, export, role or final-canonical review approval follows from this audit.','Source-head Git status/diff checks concern tracked files; the separately enumerated private comparison inventory includes ignored files.','The final mutable canonical assembly and its native review artifacts are outside this delegated scope.'],errors=errors,status='PASS' if not errors else 'FAIL')
save('PRESERVATION-RECEIPT.json',receipt)
save('MANIFEST.json',dict(reviewer=WHO,completed_at=receipt['completed_at'],files=[dict(path=str(p.relative_to(O)),sha256=sha(p),bytes=p.stat().st_size) for p in sorted(O.rglob('*')) if p.is_file() and p.name!='MANIFEST.json']))
print(json.dumps(dict(status=receipt['status'],errors=errors,campaign_cases=len(ownership),w05_cases=188,historical_members=len(historical_members),comparison_members=len(comparison_members),receipt_sha256=sha(O/'PRESERVATION-RECEIPT.json'),manifest_sha256=sha(O/'MANIFEST.json')),indent=2))
