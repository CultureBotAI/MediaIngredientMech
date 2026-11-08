"""Read-only proof against exact Git baseline and accepted canary; no source mutations."""
from pathlib import Path
import subprocess,hashlib,os,json,datetime,sys
R=Path.cwd();O=R/'reports/all_unmatched_20261107/worker-01/shard';base='e000d66dd26ab053e9b17ce7bf8d3c873c3dde99';canary='58d67db32a86a359869819624568d625e7051358'
def oid(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def check(commit,scope=None):
 cmd=['git','ls-tree','-rz',commit]
 if scope:cmd+=['--',scope]
 rows=[]
 for line in subprocess.check_output(cmd).split(b'\0'):
  if not line:continue
  meta,path=line.split(b'\t',1);mode,kind,expected=meta.decode().split();p=R/os.fsdecode(path)
  b=os.fsencode(os.readlink(p)) if mode=='120000' else p.read_bytes()
  rows.append({'path':str(p.relative_to(R)),'mode':mode,'expected_git_blob':expected,'actual_git_blob':oid(b),'sha256':hashlib.sha256(b).hexdigest(),'equal':oid(b)==expected})
 return rows
rows=check(base);cr=check(canary,'reports/all_unmatched_20261107/worker-01/canary');links=[x for x in rows if x['mode']=='120000'];regular=[x for x in rows if x['mode']!='120000'];assert all(x['equal'] for x in rows+cr)
receipt={'at':datetime.datetime.now(datetime.UTC).isoformat(),'baseline':base,'actual_head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'baseline_git_entry_count':len(rows),'git_regular_file_count':len(regular),'file_content_hash_count':len(regular)+1,'file_content_hash_definition':'Git regular files plus dereferenced CLAUDE.md file-symlink target; both tracked symlink targets are verified separately against baseline Git blobs.','dereferenced_claude_content_sha256':hashlib.sha256((R/'CLAUDE.md').read_bytes()).hexdigest(),'tracked_symlink_proof':links,'baseline_all_equal':True,'accepted_canary_commit':canary,'accepted_canary_file_count':len(cr),'canary_all_equal':True,'canary_sha256_manifest_hash':hashlib.sha256((R/'reports/all_unmatched_20261107/worker-01/canary/sha256-manifest.json').read_bytes()).hexdigest(),'coordinator_original_symlink_proof_reference':'canary/captures/coordinator-mim-preservation-v2.json','detailed_current_regular_file_hashes':regular,'detailed_current_canary_hashes':cr,'scientific_approval_established':False}
p=O/'validation'/sys.argv[1];assert not p.exists();p.write_text(json.dumps(receipt,indent=2)+'\n');print(len(regular),'Git regular files;',len(regular)+1,'file-content hashes;',len(links),'symlink targets;',len(cr),'canary files unchanged')
