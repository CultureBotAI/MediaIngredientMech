#!/usr/bin/env python3
"""Mechanical, read-only preservation audit; writes only its new immutable receipt."""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

assert os.environ.get('PYTHONDONTWRITEBYTECODE') == '1'
R=Path.cwd()
S=R/'reports/all_unmatched_20261107/worker-10/successor-v2'
P=R/'.temp/all-unmatched-worker-10/successor-v2/preservation-baseline.json'
OUT=S/'preservation-check.json'
assert not OUT.exists(), 'Refusing to overwrite immutable receipt'
BASE='468766d941e35a74eb2de3c95096660987277d9b'
NATIVE='reviews/structured/20261108T072255Z-w10-completeness-c001-c002/'
started=dt.datetime.now(dt.timezone.utc).isoformat()
t0=time.monotonic()
commands=[]
failures=[]
sha=lambda b:hashlib.sha256(b).hexdigest()

def run(args,stdin=None):
    p=subprocess.run(args,cwd=R,input=stdin,capture_output=True)
    commands.append({'argv':args,'exit_code':p.returncode,'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr),'stdout_bytes':len(p.stdout),
                     'stdin_sha256':sha(stdin) if stdin is not None else None})
    if p.returncode:
        raise RuntimeError((args,p.returncode,p.stderr.decode(errors='replace')))
    return p.stdout

def check(ok,why):
    if not ok:failures.append(why)
    return bool(ok)

baseline_bytes=P.read_bytes()
baseline=json.loads(baseline_bytes)
initial_status=run(['git','status','--porcelain=v1','--untracked-files=all']).decode()
head=run(['git','rev-parse','HEAD']).decode().strip()
check(head==BASE,'HEAD differs from declared frozen base')

groups={}
for name,expected_count in [('old_artifact_files',1880),('owners',2956)]:
    rows=[]
    for rel,expected in sorted(baseline[name].items()):
        p=R/rel
        actual=sha(p.read_bytes()) if p.is_file() and not p.is_symlink() else None
        rows.append({'path':rel,'expected_sha256':expected,'actual_sha256':actual,
                     'match':check(actual==expected,f'{name}: {rel} missing/changed/symlink')})
    groups[name]={'expected_count':expected_count,'count':len(rows),'matches':sum(x['match'] for x in rows),
                  'count_match':check(len(rows)==expected_count,f'{name} count mismatch'),
                  'path_and_expected_hash_inventory_sha256':sha(json.dumps(baseline[name],sort_keys=True,separators=(',',':')).encode()),
                  'files':rows}

# Direct filesystem inventory includes ignored files; no rg/gitignore filtering.
owner_paths={str(p.relative_to(R)) for p in (R/'data/ingredients').rglob('*.yaml')}
expected_owners=set(baseline['owners'])
owner_inventory={'method':'Complete pathlib.rglob data/ingredients/**/*.yaml, including ignored and hidden paths.',
    'actual_count':len(owner_paths),'missing':sorted(expected_owners-owner_paths),'added':sorted(owner_paths-expected_owners)}
check(owner_paths==expected_owners,'Maintained owner path set changed')

# Compare every pre-existing canonical review file to exact Git bytes at BASE.
tree=run(['git','ls-tree','-r','-z',BASE,'--','reviews/structured'])
entries=[]
for item in tree.split(b'\0'):
    if not item:continue
    metadata,path=item.split(b'\t',1)
    mode,typ,oid=metadata.decode().split()
    assert typ=='blob',(typ,path)
    entries.append((mode,oid,path.decode()))
request=''.join(oid+'\n' for _,oid,_ in entries).encode()
data=run(['git','cat-file','--batch'],request)
pos=0
canonical=[]
for mode,oid,rel in entries:
    end=data.index(b'\n',pos);header=data[pos:end].decode().split();pos=end+1
    assert header[0]==oid and header[1]=='blob'
    size=int(header[2]);content=data[pos:pos+size];pos+=size+1
    p=R/rel;actual=sha(p.read_bytes()) if p.is_file() and not p.is_symlink() else None
    expected=sha(content)
    canonical.append({'path':rel,'git_blob_oid':oid,'git_mode':mode,'expected_head_sha256':expected,'actual_sha256':actual,
                      'match':check(actual==expected,f'Canonical review changed: {rel}')})
assert pos==len(data)

tracked_delta=run(['git','diff','--name-status',BASE,'--']).decode()
check(not tracked_delta,'Tracked Git content differs from HEAD')
final_status=run(['git','status','--porcelain=v1','--untracked-files=all']).decode()
expected_new={NATIVE+'review.md',NATIVE+'review.yaml'}
status_rows=[{'status':line[:2],'path':line[3:]} for line in final_status.splitlines()]
check({r['path'] for r in status_rows}==expected_new,'Status path set is not exactly the new native review pair')
check(all(r['status']=='??' for r in status_rows),'Native review status differs from observed untracked-only state')
new_review=[{'path':rel,'sha256':sha((R/rel).read_bytes()),'status':'untracked'} for rel in sorted(expected_new)]
new_report_paths=sorted(str(p.relative_to(R)) for p in S.rglob('*') if p.is_file())
ignored_output=run(['git','check-ignore','--no-index','--',*new_report_paths]).decode().splitlines()
check(set(ignored_output)==set(new_report_paths),'Some successor-v2 report file is not ignored')
check(sha(P.read_bytes())==sha(baseline_bytes),'Preservation baseline changed during audit')
endhead=run(['git','rev-parse','HEAD']).decode().strip()
check(endhead==head,'HEAD advanced during audit')

report={'schema_version':1,'kind':'author_mechanical_preservation_check','scientific_review':False,'author':'/root/buffers_research',
    'scope':'Byte preservation of all1880 old worker10 artifact paths and all2956 maintained owner files listed in the explicit successor-v2 baseline, all existing canonical review files at HEAD468766d9, and current Git status. This is author mechanical validation, not independent source science, native review acceptance, staging, commit, or push.',
    'base_head':BASE,'observed_head_start':head,'observed_head_end':endhead,'started_at':started,
    'baseline':{'path':str(P),'sha256':sha(baseline_bytes)},'groups':groups,'owner_path_inventory':owner_inventory,
    'canonical_reviews':{'scope':'Every blob under reviews/structured in the exact frozen HEAD tree, including ignored tracked paths. New untracked review pair is assessed only as allowed new content.',
        'count':len(canonical),'matching_count':sum(x['match'] for x in canonical),'files':canonical},
    'git_status':{'initial_porcelain':initial_status,'final_porcelain':final_status,'tracked_diff_against_base':tracked_delta,
        'tracked_content_unchanged':not tracked_delta,'new_native_review_files':new_review,
        'precise_status':'No tracked modifications or staged additions at audit time. Exactly the new native review.yaml/review.md pair is untracked (??). The pair has not been staged by this audit.',
        'successor_reports_ignored':len(ignored_output)==len(new_report_paths),'ignored_successor_report_files_checked':len(new_report_paths),
        'ignored_successor_report_paths':new_report_paths},
    'limits':['Checks only the explicit old-artifact/owner inventories and canonical reviews; source-science judgments are supplied by separate reviews.',
              'Baseline old_comparison_manifest and independent_review_files sections were not re-audited in this narrowly assigned check. Prior dedicated preservation receipts remain separate.',
              'The observed Git status is time-bound. A later stage/commit requires the root final index/branch audit; this script performs no Git mutation.'],
    'failures':failures,'status':'PASS' if not failures else 'FAIL','commands':commands,
    'reproduction':{'script':str(Path(__file__).resolve()),'sha256':sha(Path(__file__).read_bytes()),
        'command':['env','PYTHONDONTWRITEBYTECODE=1','.temp/all-unmatched-worker-10/venv/bin/python',str(Path(__file__))],
        'immutable_output':'Exclusive creation; later reruns must use a new linked receipt/script, not overwrite this observation.'},
    'finished_at':dt.datetime.now(dt.timezone.utc).isoformat(),'runtime_seconds':round(time.monotonic()-t0,6)}
with OUT.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'path':str(OUT),'sha256':sha(OUT.read_bytes()),'status':report['status'],'old_artifacts':len(groups['old_artifact_files']['files']),
    'owners':len(groups['owners']['files']),'canonical_reviews':len(canonical),'failures':failures}))
