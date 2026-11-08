from pathlib import Path
import ast, collections, datetime, hashlib, json, os, subprocess

R=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/integration/worktree')
W=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/workers/w01/worktree')
O=W/'.temp/infrastructure-pr1205-final-head-review-v1/skeptical'
B=R/'reports/unmatched_campaign_operators_1174_20261108/independent-review'
BASE='e000d66dd26ab053e9b17ce7bf8d3c873c3dde99';HEAD='4c8a987da40d48cceeb4390550f1ff7545927a0b'
commands=[]
def run(argv,cwd=R):
    p=subprocess.run(argv,cwd=cwd,capture_output=True)
    commands.append({'argv':argv,'cwd':str(cwd),'exit_code':p.returncode,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest(),'stdout_bytes':len(p.stdout),'stderr_bytes':len(p.stderr)})
    assert p.returncode==0,(argv,p.returncode,p.stderr.decode(errors='replace'))
    return p.stdout
def git(*a):return run(['git',*a])
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def save(name,v):
    p=O/name;assert not p.exists(),str(p);p.write_text(json.dumps(v,indent=2)+'\n');return p
assert git('rev-parse','HEAD').decode().strip()==HEAD
assert not git('status','--porcelain=v1','--untracked-files=all')
git('merge-base','--is-ancestor',BASE,HEAD)
remote={x.split()[1]:x.split()[0] for x in (O/'remote-heads-live-v1.txt').read_text().splitlines()}
assert remote['refs/heads/curate/all-unmatched-source-integration-20261107']==HEAD
assert remote['refs/heads/curate/kgm-unmapped-chemicals-20261107']==BASE
pr=read(O/'pr1205-live-v1.json');draft=read(O/'pr1205-draft-state-v1.json')
assert pr['headRefOid']==draft['headRefOid']==HEAD
assert pr['baseRefOid']==draft['baseRefOid']==BASE
assert pr['headRefName']=='curate/all-unmatched-source-integration-20261107'
assert pr['baseRefName']=='curate/kgm-unmapped-chemicals-20261107'
assert pr['state']=='OPEN' and draft['isDraft'] is True
def tree(ref):
    d={}
    for line in git('ls-tree','-r','--full-tree','-z',ref).split(b'\0'):
        if not line:continue
        meta,path=line.split(b'\t',1);mode,kind,blob=meta.split();d[path.decode()]=(mode.decode(),kind.decode(),blob.decode())
    return d
base=tree(BASE);head=tree(HEAD)
assert all(head.get(p)==v for p,v in base.items())
regular=symlinks=0
for p,(mode,kind,blob) in base.items():
    assert kind=='blob'
    if mode=='120000':data=os.readlink(R/p).encode();symlinks+=1
    else:data=(R/p).read_bytes();regular+=1
    assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==blob,p
raw=git('diff','--name-status','-z',BASE,HEAD).split(b'\0')[:-1]
diff=[(a.decode(),b.decode()) for a,b in zip(raw[::2],raw[1::2])]
assert len(diff)==249 and all(a=='A' for a,b in diff)
prefix=str(B.relative_to(R))+'/'
code=sorted(p for _,p in diff if not p.startswith(prefix))
expected=sorted(['scripts/apply_unmatched_campaign_owners.py','scripts/publish_unmatched_campaign.py','scripts/validate_unmatched_campaign_publication.py','src/mediaingredientmech/campaign_publication.py','src/mediaingredientmech/curate/campaign_owner_apply.py','tests/test_campaign_owner_apply.py','tests/test_campaign_publication.py'])
assert code==expected
git('diff','--check',BASE,HEAD,'--',*code)
selection=read(B/'SELECTION.json')['original_to_archive']
source=read(B/'independent-v3/source-snapshot-v2.json')['files'];publisher=read(B/'independent-v3/publisher-snapshot-v2.json')['files']
review=read(B/'independent-v3/COMBINED-REVIEW-v1.json')
bindings=[]
for p in code:
    expected_hash=(source if p in source else publisher)[p]
    assert h(R/p)==expected_hash
    matched=[x for x in selection if x['source_path'].endswith('/'+p) and x['source_sha256']==expected_hash]
    assert matched
    paths=sorted({x['archive_relative_path'] for x in matched})
    assert all(h(B/q)==expected_hash for q in paths)
    ast.parse((R/p).read_text(),filename=p)
    bindings.append({'path':p,'sha256':expected_hash,'git_blob':head[p][2],'archive_paths':[prefix+q for q in paths],'final_snapshot_manifests':[n for n,m in [('independent-v3/source-snapshot-v2.json',source),('independent-v3/publisher-snapshot-v2.json',publisher)] if p in m],'matches_archived_final_review':True})
for manifest in [source,publisher]:
    assert all((R/p).is_file() and h(R/p)==v for p,v in manifest.items())
assert h(R/'src/mediaingredientmech/curate/campaign_owner_apply.py')==review['source_sha256']
assert h(R/'src/mediaingredientmech/campaign_publication.py')==review['publisher_sha256']
assert h(R/'tests/test_campaign_owner_apply.py')==review['source_test_sha256']
assert h(R/'tests/test_campaign_publication.py')==review['publisher_test_sha256']
review_evidence=[]
for x in review['evidence']:
    matches=[e for e in selection if e['source_sha256']==x['sha256'] and e['source_path'].endswith('/'+x['path'])]
    assert matches,x
    paths=sorted({e['archive_relative_path'] for e in matches})
    assert all(h(B/q)==x['sha256'] for q in paths)
    review_evidence.append({'historical_path':x['path'],'sha256':x['sha256'],'archive_paths':[prefix+q for q in paths]})
inventory=[]
for status,p in diff:
    data=(R/p).read_bytes();mode,kind,blob=head[p]
    assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==blob
    inventory.append({'status':status,'path':p,'mode':mode,'git_blob':blob,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
history=git('log','--format=%H%x09%cI%x09%s',BASE+'..'+HEAD,'--',*code).decode().splitlines()
last=git('diff-tree','--no-commit-id','--name-only','-r',HEAD).decode().splitlines();assert all(p.startswith(prefix) for p in last)
assert not git('diff','HEAD','--',*code)
assert git('rev-parse','HEAD').decode().strip()==HEAD
assert not git('status','--porcelain=v1','--untracked-files=all')
worker_head=run(['git','rev-parse','HEAD'],cwd=W).decode().strip();assert worker_head=='26445f23b5a905ac26d864acfbd658570c88769c'
assert not run(['git','diff','HEAD','--','reports/all_unmatched_20261107/worker-01','reviews/structured'],cwd=W)
at=datetime.datetime.now(datetime.timezone.utc).isoformat()
ip=save('complete-diff-and-bindings-v1.json',{'at':at,'base':BASE,'head':HEAD,'full_diff':inventory,'seven_final_code_bindings':bindings,'final_review_evidence_resolution':review_evidence,'source_manifest_members':len(source),'publisher_manifest_members':len(publisher),'all_dependency_snapshot_members_equal_current':True,'code_commit_history':history,'last_commit_archive_only':True})
cp=save('commands-v1.json',{'at':at,'integration_shell_login':False,'read_only_subprocesses':commands,'earlier_live_commands':[{'argv':['gh','pr','view','1205','--repo','CultureBotAI/MediaIngredientMech','--json','number,url,state,title,body,headRefName,headRefOid,baseRefName,baseRefOid,statusCheckRollup,commits'],'capture':'pr1205-live-v1.json','sha256':h(O/'pr1205-live-v1.json'),'exit_code':0},{'argv':['git','ls-remote','origin','refs/heads/curate/all-unmatched-source-integration-20261107','refs/heads/curate/kgm-unmapped-chemicals-20261107'],'cwd':str(R),'capture':'remote-heads-live-v1.txt','sha256':h(O/'remote-heads-live-v1.txt'),'exit_code':0},{'argv':['gh','pr','view','1205','--repo','CultureBotAI/MediaIngredientMech','--json','number,isDraft,headRefOid,baseRefOid'],'capture':'pr1205-draft-state-v1.json','sha256':h(O/'pr1205-draft-state-v1.json'),'exit_code':0}],'no_project_code_import_or_execution':True,'syntax_only':'ast.parse on allseven bytes; no pycache writes','not_run':['pytest/fullsuite','just qc/fullQC','anyownerapplicationorpublication','anyGitHubmutation','commit/push/checkout']})
counts=collections.Counter((x.get('status'),x.get('conclusion')) for x in pr['statusCheckRollup'])
out=save('skeptical-final-head-review-v1.json',{
 'reviewer':'/root/skeptical_review','at':at,'verdict':'pass_with_explicit_scope_limits','pr':pr['url'],'head':HEAD,'base':BASE,'local_remote_pr_head_and_base_match':True,'open_draft_verified':True,
 'scope':'Read-only final-head, complete-diff and reviewed-byte transport verification. Separate reviewer owns fullSELECTION/privacy audit; parent owns operator review and final validation integration.',
 'diff':{'all_additions':249,'archive_files':242,'new_code_test_cli_files':7,'inventory_path':str(ip),'inventory_sha256':h(ip)},
 'preservation':{'all_baseline_git_entries_unchanged':True,'baseline_regular_files_byte_verified':regular,'baseline_symlink_targets_byte_verified':symlinks,'maintained_data_canonical_outputs_workflows_thresholds_pins_existing_gates_unchanged':True,'integration_worktree_clean_at_start_and_end':True,'worker01_accepted_head_preserved':worker_head},
 'review_transport':{'combined_review_sha256':h(B/'independent-v3/COMBINED-REVIEW-v1.json'),'combined_review_author':review['reviewer'],'all_seven_files_match_final_review_snapshots_and_Git_blobs':True,'all_12_source_and_98_publisher_snapshot_members_match_current':True,'all_seven_explicit_review_evidence_refs_resolved_through_selection':True,'no_code_delta_after_archived_final_review_bytes':True,'final_commit_adds_archive_only':True,'cli_dedup_note':'The three unchanged CLI files reside under archived independent-v1 paths becauseSELECTION deduplicates identical bytes; their hashes are explicitly bound by finalv3 snapshot manifests. This is not a stale-version substitution.'},
 'checks_run':['Exact local/remote/livePR head and base reads','Complete249-file diff and committed/worktree hash verification','Every baseline regular file and symlink target verified against frozenGitblob','Allseven finalcode/test/CLI snapshot bindings and syntax-only ASTparse','Narrow code whitespace check','Allfinalsnapshot dependencies and combined-review explicit evidence references verified'],
 'ci_observation':{'source':'Independent livePR capture','counts':[{'status':k[0],'conclusion':k[1],'count':n} for k,n in sorted(counts.items())],'all_green_claim':False},
 'new_findings':[],
 'limits':['No fullsuite/fullQC or adversarial programs were rerun; archived test results remain attributed to their original authors/reviewer.','No fresh complete operator semantic audit is claimed by byte-equivalence review; parent independently reviews owner/operator behavior.','FullSELECTION original-to-archive completeness and privacy inventory are separately delegated; this review verifies every finalcode dependency and explicit combined-review evidence binding.','Historical manifests may reference private fixtures intentionally excluded by the archive README; archive presence does not prove those fixtures were published or allhistorical commands immediately replayable.','No campaign scientific, owner, role, alias, mapping, supported-export, release or merge approval.','CI/fullQC final statuses are separate coordinator checks.'],
 'commands':{'path':str(cp),'sha256':h(cp)}
})
print(json.dumps({'receipt':str(out),'sha256':h(out),'baseline_regular':regular,'symlinks':symlinks,'new_findings':0,'diff_files':len(inventory)}))
