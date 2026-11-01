from pathlib import Path
import datetime,hashlib,json,subprocess,sys

def verified_changed_paths(root, base, head, merge):
    raw = subprocess.check_output(["git", "diff", "--no-renames", "--name-only", "-z", base, head, "--"], cwd=root)
    files = [p.decode() for p in raw.split(b"\0") if p]
    assert files, "No reviewed changed paths"
    difference = subprocess.check_output(["git", "--literal-pathspecs", "diff", head, merge, "--", *files], cwd=root)
    assert not difference, "Merged files differ from reviewed head; inspect before cleanup"
    return files

r=Path(__file__).resolve().parent
step,number,branch,head,base=sys.argv[1:]
assert Path(step).name==step and branch.startswith("fix/") and int(number)>0
w=r/step
out=r/(step+"-verified-merge-cleanup.json")
assert not out.exists()
def cmd(*args,check=True):return subprocess.run(args,cwd=w,text=True,capture_output=True,check=check)
def git(*args):return cmd("git",*args).stdout.strip()
pr=json.loads(cmd("gh","pr","view",number,"-R","CultureBotAI/MediaIngredientMech","--json","state,baseRefName,headRefName,headRefOid,headRepository,mergeCommit,mergedAt").stdout)
assert pr["state"]=="MERGED" and pr["mergedAt"]
assert pr["baseRefName"]=="main" and pr["headRefName"]==branch and pr["headRefOid"]==head
assert pr["headRepository"]["nameWithOwner"]=="CultureBotAI/MediaIngredientMech"
assert git("remote","get-url","origin")=="https://github.com/CultureBotAI/MediaIngredientMech.git"
assert Path(git("rev-parse","--git-common-dir")).resolve()==r/"control/.git"
assert not git("status","--porcelain","--untracked-files=all")
assert git("rev-parse","HEAD")==head and git("branch","--show-current")==branch
merge=pr["mergeCommit"]["oid"]
cmd("git","fetch","origin","main")
cmd("git","merge-base","--is-ancestor",merge,"origin/main")
assert len(git("rev-list","--parents","-n","1",merge).split())==2
files=verified_changed_paths(w,base,head,merge)
remote=cmd("git","ls-remote","--exit-code","--heads","origin","refs/heads/"+branch,check=False)
if remote.returncode==0:
    assert remote.stdout.strip()==head+"\trefs/heads/"+branch
    cmd("git","push","origin","--force-with-lease=refs/heads/"+branch+":"+head,":refs/heads/"+branch)
elif remote.returncode!=2:
    raise RuntimeError("remote branch check failed; do not infer absence")
remote_after=cmd("git","ls-remote","--exit-code","--heads","origin","refs/heads/"+branch,check=False)
assert remote_after.returncode==2 and not remote_after.stdout
cmd("git","checkout","--detach",merge)
cmd("git","update-ref","-d","refs/heads/"+branch,head)
assert cmd("git","show-ref","--verify","--quiet","refs/heads/"+branch,check=False).returncode==1
tracking="refs/remotes/origin/"+branch
tracked=cmd("git","rev-parse","--verify",tracking,check=False)
if tracked.returncode==0:
    assert tracked.stdout.strip()==head
    cmd("git","update-ref","-d",tracking,head)
assert not git("status","--porcelain","--untracked-files=all")
receipt={"checked_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"pull_request":pr,"reviewed_head":head,"verified_merge":merge,"base":base,"verified_file_count":len(files),"verified_files":{f:hashlib.sha256((w/f).read_bytes()).hexdigest() for f in files if (w/f).is_file()},"origin_main_contains_merge":True,"single_parent_squash":True,"remote_branch_absence_exit_code":remote_after.returncode,"local_branch_deleted":True,"remote_tracking_deleted":True,"detached_worktree":str(w),"supervisor_binding":None}
with out.open("x") as f:json.dump(receipt,f,indent=2);f.write("\n")
print(json.dumps({k:v for k,v in receipt.items() if k!="verified_files"},indent=2))
