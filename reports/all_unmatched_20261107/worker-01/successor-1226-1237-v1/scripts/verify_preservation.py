"""Recheck old committed inputs and immutable prior packets, without Git mutations."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

D=Path(__file__).resolve().parents[1]
W=Path(__file__).resolve().parents[5]


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    output=Path(sys.argv[1]);assert not output.exists()
    pre=json.loads((D/'checks/preflight-v1.json').read_text())
    pins=next(r for r in json.loads((D/'inputs/current-worker-bindings.json').read_text())['workers'] if r['worker']==1)
    checked=[]
    for pin in list(pins['core'].values())+pins['all_selected_payloads']:
        p=Path(pin['path']);assert sha(p)==pin['sha256']
        assert p.read_bytes()==subprocess.check_output(['git','show',pins['head']+':'+str(p.relative_to(W))],cwd=W)
        checked.append({'path':str(p.relative_to(W)),'sha256':sha(p)})
    packets=[]
    for pin in pre['preserved_packets']:
        p=W/pin['path'];assert sha(p)==pin['sha256'];m=json.loads(p.read_text());count=0
        for row in m.get('files',[]):
            if isinstance(row,dict) and 'path' in row and 'sha256' in row:
                q=p.parent/row['path'];assert q.is_file() and sha(q)==row['sha256'];count+=1
        links=0
        for row in m.get('symlinks',[]):
            q=p.parent/row['path'];assert q.is_symlink() and os.readlink(q)==row['target'];links+=1
        packets.append({'path':pin['path'],'sha256':sha(p),'file_members_rechecked':count,'original_symlink_targets_rechecked_without_traversal':links})
    diffs=subprocess.check_output(['git','diff','--name-only',pins['head']],cwd=W,text=True).splitlines()
    prefix=str(D.relative_to(W))+'/'
    assert all(p.startswith(prefix) for p in diffs),diffs
    # A new report may remain untracked before publication; every visible new path
    # still must be inside the bounded successor directory.
    status=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],cwd=W,text=True).splitlines()
    assert all(line[3:].startswith(prefix) for line in status),status[:5]
    symlinks=[str(p.relative_to(D)) for p in D.rglob('*') if p.is_symlink()]
    assert not symlinks,symlinks
    result={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'Codex /root (worker01)','result':'PASS','source_head':pins['head'],'current_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip(),'predecessor_core_and_payload_count':len(checked),'predecessor_inputs':checked,'preserved_private_packets':packets,'tracked_diff_paths':diffs,'new_or_changed_paths_are_only_successor':True,'visible_status_count':len(status),'successor_symlinks':symlinks,'limitations':['Ignored previous review artifacts were checked through their exact original manifest member lists; this is not a global cleanup inventory.','No assertion is made about unrelated concurrent coordinator work outside this worker checkout.'],'maintained_source_or_export_changes':False}
    with output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'result':'PASS','predecessor_inputs':len(checked),'prior_packets':len(packets),'only_new_report_paths':True,'current_head':result['current_head']}))


if __name__=='__main__':main()
