"""Recheck pinned inputs and preserve all private attempts in an outer seal."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

W = Path.cwd()
O = W / '.temp/nine-scope-candidates-independent-v1'
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
P = C / 'integration/final-same-target-reconciliation-v2'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bind(path):
    path = Path(path)
    if not path.is_absolute():
        path = O / path
    return {'path': str(path), 'sha256': sha(path)}


def load(name):
    return json.loads((O / name).read_text())


def save(name, obj):
    with (O/name).open('x') as f:
        f.write(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')


def git(repo, *args):
    return subprocess.check_output(['git','-C',str(repo),*args])


ref_count = 0
ref_paths = set()


def verify(v):
    global ref_count
    if isinstance(v, dict):
        if isinstance(v.get('path'), str) and v['path'].startswith('/') and isinstance(v.get('sha256'), str):
            q = Path(v['path'])
            assert q.is_file() and sha(q)==v['sha256'], q
            ref_count += 1
            ref_paths.add(str(q))
        for value in v.values(): verify(value)
    elif isinstance(v, list):
        for value in v: verify(value)


for name in ['HANDOFF.json','handoff-independent-check-v1.json','skeptical/final-nine-review-v1.json','technical/native-review-completion-v1.json']:
    verify(load(name))
assignment = C/'assignments/w01-nine-scope-candidates-independent-v1.json'
assert sha(assignment)=='dbde61cc31a77eb32c1ee7dcc344ed885c462ac99f5cbb233b54f69c3735d033'
a=json.loads(assignment.read_text())
assert sha(Path(a['final_candidate_summary']))=='05414067195a94abb078152ba6be1dc515734124fcfe1296350102558acf2aa6'
assert sha(P/'HANDOFF.json')=='fb4cb8972c815667e925b056cdb7797d1635b291a9fb3ba936061bdcfa3dac96'
assert sha(P/'MANIFEST.json')=='6c89863e292bf1b4333be602bf4a355c0219766456d16e1f574bb5412d956df9'
author=json.loads((P/'MANIFEST.json').read_text())
for path, entry in author['files'].items():
    q=P/path
    assert not q.is_symlink() and sha(q)==entry['sha256']
    assert q.stat().st_size==entry['size']
for r in a['candidates']:
    assert sha(P/r['candidate']['path'])==r['candidate']['sha256']

previous=W/'.temp/final-preparation-comparison-v1/MANIFEST.json'
assert sha(previous)=='dc258c1ebe39c8210e4a7925ed720790ecbcc4a91ec55db24760a58d6aca9773'
prev=json.loads(previous.read_text())
for f in prev['files']:
    assert sha(previous.parent/f['path'])==f['sha256']
science=load('science/MANIFEST-v1.json')
members=science['files']
if isinstance(members, dict):
    member_rows=[{'path':k,**v} for k,v in members.items()]
else:
    member_rows=members
for f in member_rows:
    assert sha(O/'science'/f['path'])==f['sha256']

old_currentness=load('root/source-currentness-and-beforeimages-v1.json')
origin_checks=[]
for r in old_currentness['origin_checks']:
    repo=Path(r['repository'])
    current_head=git(repo,'rev-parse','HEAD').decode().strip()
    current_blob=hashlib.sha256(git(repo,'show',f"HEAD:{r['repository_path']}")).hexdigest()
    working_sha=sha(repo/r['repository_path'])
    origin_checks.append({'entry_id':r['entry_id'],'selected_head':r['selected_head'],'observed_local_head':current_head,'selected_sha256':r['selected_sha256'],'current_git_blob_sha256':current_blob,'current_worktree_sha256':working_sha,'selected_bytes_still_current':current_blob==working_sha==r['selected_sha256']})
assert all(r['selected_bytes_still_current'] for r in origin_checks)
maintained=load('technical/final-maintained-boundary-v1.json')
I=C/'integration/worktree'
for path, expected in maintained['maintained_catalog_hashes'].items():
    assert sha(I/path)==expected
assert len(maintained['maintained_catalog_hashes'])==2956
head=git(W,'rev-parse','HEAD').decode().strip()
status=git(W,'status','--porcelain').decode()
assert head=='26445f23b5a905ac26d864acfbd658570c88769c' and status==''
integration_status=git(I,'status','--porcelain').decode()
assert integration_status==''

save('root/final-preservation-and-seal-check-v1.json',{
    'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reviewer':'OpenAI Codex worker01 /root; final read-only preservation and transport check',
    'active_handoff':bind('HANDOFF.json'),
    'independent_handoff_check':bind('handoff-independent-check-v1.json'),
    'review_reference_bindings_verified':ref_count,
    'unique_review_reference_paths':len(ref_paths),
    'author_manifest':bind(P/'MANIFEST.json'),
    'author_manifest_members_reverified':len(author['files']),
    'all_nine_assigned_hashes_unchanged':True,
    'prior26family_manifest':bind(previous),
    'prior26family_members_reverified':len(prev['files']),
    'primary_science_inner_manifest':bind('science/MANIFEST-v1.json'),
    'primary_science_inner_members_reverified':len(member_rows),
    'postseal_source_cue_addendum':bind('science/source-cue-semantics-addendum-v1.json'),
    'origin_currentness':origin_checks,
    'local_source_HEAD':head,'local_source_tracked_status':status,
    'integration_HEAD':git(I,'rev-parse','HEAD').decode().strip(),
    'integration_tracked_status':integration_status,
    'unchanged_maintained_catalog_files':2956,
    'remote_currentness_scope':'The earlier read-only ls-remote observation remains at its captured timestamp; no second remote query or later W06/W07 intake acceptance is claimed here.',
    'no_silent_repin':True,'all_checks_pass':True,
    'program':bind('root/seal_final_review_v1.py'),
})
files=[]
for q in sorted(O.rglob('*')):
    assert not q.is_symlink(), q
    if q.is_file():
        assert q.name!='MANIFEST.json'
        files.append({'path':str(q.relative_to(O)),'sha256':sha(q),'bytes':q.stat().st_size})
save('MANIFEST.json',{
    'schema_version':'worker01-nine-scope-private-review-manifest-v1',
    'sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'root':str(O),
    'active_handoff':bind('HANDOFF.json'),'readable_handoff':bind('HANDOFF.md'),
    'independent_final_review':bind('skeptical/final-nine-review-v1.json'),
    'independent_handoff_check':bind('handoff-independent-check-v1.json'),
    'final_preservation':bind('root/final-preservation-and-seal-check-v1.json'),
    'member_count':len(files),'total_member_bytes':sum(x['bytes'] for x in files),
    'files':files,
    'excluded':['MANIFEST.json itself; external source originals remain at their hash-bound original paths'],
    'scope':'Every private regular file, including failed helpers and native-report drafts, original finding receipts, append-only source-cue clarification, all active reviews and reproduction programs. No symlinks.',
    'open_unique_candidate_conditions':1,'existing_issue':1226,
    'resolved_report_only_observations':['W01-NINE-REPORT-001'],
    'unqualified_whole_candidate_acceptance':False,
    'whole_owner_approval':False,'role_approval':False,'export_approval':False,'merge_approval':False,
})
actual={str(q.relative_to(O)) for q in O.rglob('*') if q.is_file()}
assert actual=={x['path'] for x in files}|{'MANIFEST.json'}
for f in files: assert sha(O/f['path'])==f['sha256']
print(json.dumps({'manifest':bind('MANIFEST.json'),'handoff':bind('HANDOFF.json'),'readable':bind('HANDOFF.md'),'members':len(files),'final_verification':'PASS'},indent=2))
