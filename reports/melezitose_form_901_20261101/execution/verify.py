"""Explicit Step6 evidence packaging, with immutable durable-Git references.

Verification checks selected bytes and command bindings, not scientific truth.
Only explicit publish writes the new production evidence directory.
"""
from pathlib import Path
from datetime import datetime, timezone
from contextlib import ExitStack
import argparse
import gzip
import hashlib
import io
import json
import os
import re
import stat
import subprocess
import tarfile

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
ROOT = RUN / "step6-melezitose"
DEST = Path("reports/melezitose_form_901_20261101/execution")
BASE = "e568dbf0e0f759431ed317b973675680f031dd1d"
KIND = "step6_melezitose_execution_evidence"
DENIED = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".venv"}

# Reused Step5 primitives are inserted verbatim below, with their donor hash
# retained in implementation-provenance.json. No dynamic import of the donor.
def require(ok,message):
 if not ok:raise ValueError(message)

def digest(data):return hashlib.sha256(data).hexdigest()

def encoded(value):return (json.dumps(value,indent=2,sort_keys=True)+'\n').encode()

def hexsha(value):return isinstance(value,str) and len(value)==64 and all(c in '0123456789abcdef' for c in value)

def key(ref):return ref['identity'],ref['sha256']

def safe(path):
 p=Path(path)
 require(p.parts and '..' not in p.parts and not any(part.casefold() in DENIED for part in p.parts),'Unsafe/excluded path: '+str(p))
 return p

def relative(path):
 p=safe(path);require(not p.is_absolute(),'Expected relative member');return p

def read(path):
 p=safe(path).absolute()
 require(p.is_file() and not any(member.is_symlink() for member in (p,*p.parents)),'Nonregular/aliased file: '+str(p))
 require(p.suffix not in {'.pyc','.db','.sqlite','.sqlite3'},'Excluded cache/database payload')
 return p.read_bytes()

def payload_archive(originals):
 by_hash={digest(data):data for data in originals.values()};raw_container=io.BytesIO();separate={}
 with tarfile.open(fileobj=raw_container,mode='w',format=tarfile.USTAR_FORMAT) as archive:
  for sha,data in sorted(by_hash.items()):
   if data.startswith(b'\x1f\x8b') and len(data)>1_000_000:
    separate['blobs/'+sha+'.bin']=data;continue
   item=tarfile.TarInfo(sha);item.size=len(data);item.mtime=0;item.mode=0o644;item.uid=item.gid=0;item.uname=item.gname='';archive.addfile(item,io.BytesIO(data))
 decoded=raw_container.getvalue();packed=gzip.compress(decoded,mtime=0)
 return {'payloads.tar.gz':packed,**separate},{'decoded_sha256':digest(decoded),'decoded_bytes':len(decoded)},set(by_hash)

def write_new_package(destination,payloads,manifest_bytes,final_input_check):
 """Create through retained directory handles; never follow a late path alias.

 Failed owned output is retained. Existing/replacement paths are never removed.
 Route and inode checks detect concurrent replacement; retained file handles
 prevent a replacement from redirecting bytes even between those checks.
 """
 destination=safe(destination).absolute();root=safe(ROOT).absolute()
 require(destination.is_relative_to(root),'Package destination is outside owned root')
 flags=os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW
 with ExitStack() as stack:
  directories={};opened_files=[]
  def retain(fd):stack.callback(os.close,fd);return fd
  directories[Path('/')]=retain(os.open('/',flags))
  def identity(status):return status.st_dev,status.st_ino
  def check():
   for path,fd in directories.items():
    actual=os.stat(path,follow_symlinks=False)
    require(stat.S_ISDIR(actual.st_mode) and identity(actual)==identity(os.fstat(fd)),'Publication directory route changed: '+str(path))
   for parent,name,fd in opened_files:
    actual=os.stat(name,dir_fd=directories[parent],follow_symlinks=False)
    require(stat.S_ISREG(actual.st_mode) and identity(actual)==identity(os.fstat(fd)),'Publication file reservation changed: '+name)
  def directory(path,*,exclusive=False):
   if path in directories:return directories[path]
   parent_fd=directory(path.parent);check()
   if exclusive:os.mkdir(path.name,0o755,dir_fd=parent_fd)
   else:
    try:fd=os.open(path.name,flags,dir_fd=parent_fd)
    except FileNotFoundError:
     require(path.is_relative_to(root),'Owned repository root/ancestor is absent')
     os.mkdir(path.name,0o755,dir_fd=parent_fd);fd=os.open(path.name,flags,dir_fd=parent_fd)
    directories[path]=retain(fd);check();return fd
   directories[path]=retain(os.open(path.name,flags,dir_fd=parent_fd));check();return directories[path]
  directory(destination,exclusive=True)
  def write(name,data):
   target=destination/relative(name);parent_fd=directory(target.parent);check()
   fd=retain(os.open(target.name,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o644,dir_fd=parent_fd));opened_files.append((target.parent,target.name,fd));check()
   with os.fdopen(os.dup(fd),'wb') as stream:stream.write(data);stream.flush()
   check()
  for name,data in payloads.items():write(name,data)
  final_input_check();check();write('manifest.json',manifest_bytes);check()


def selection_valid(plan, *, allow_draft=False):
    require(type(plan.get("schema_version")) is int and plan["schema_version"] == 1, "Wrong selection schema")
    require(plan.get("state") == "final" and not plan.get("pending") or allow_draft and plan.get("state") == "draft", "Draft/incomplete selection")
    require(isinstance(plan.get("pending"), list), "Missing explicit pending list")
    require(isinstance(plan.get("base"), str) and re.fullmatch(r"[0-9a-f]{40}", plan["base"]), "Invalid durable base")
    require(plan.get("destination") == str(DEST), "Wrong package destination")
    require(Path(plan["run_root"]).is_absolute(), "Run root must retain its original absolute identity")
    require(isinstance(plan.get("package_readme"), str) and plan["package_readme"].strip(), "Missing selected README")
    require("supervisor_binding" in plan and plan["supervisor_binding"] is None and plan.get("scientific_approval_added") is False, "Package cannot invent approval/binding")
    require(isinstance(plan.get("files"), list) and plan["files"], "Missing selected artifacts")
    require(isinstance(plan.get("git_references"), list) and plan["git_references"], "Missing durable Git references")
    seen = set()
    for item in plan["files"] + plan["git_references"]:
        require(Path(item["identity"]).is_absolute() and hexsha(item["sha256"]), "Invalid original identity/hash")
        safe(item["identity"])
        require(type(item["bytes"]) is int and item["bytes"] >= 0, "Invalid byte count")
        require(key(item) not in seen, "Duplicate original identity/version")
        seen.add(key(item))
    for item in plan["files"]:
        require(Path(item["source_path"]).is_absolute() and item.get("category"), "Missing selected source/category")
        safe(item["source_path"])
    for item in plan["git_references"]:
        relative(item["repository_path"])
        require(isinstance(item.get("git_blob"), str) and re.fullmatch(r"[0-9a-f]{40}", item["git_blob"]), "Invalid Git blob identity")
    require(isinstance(plan.get("commands"), list) and plan["commands"], "Missing explicit command selection")
    command_keys = set()
    for item in plan["commands"]:
        ref = key(item["receipt"])
        require(ref not in command_keys and ref in seen, "Missing/duplicate selected command")
        command_keys.add(ref)
        require(type(item["expected_exit"]) is int, "Command exit must be an integer")
        require(item["classification"] in {"successful_check", "expected_negative_control", "failed_attempt", "interrupted_attempt"}, "Unqualified command status")
        require(item["expected_exit"] == 0 or bool(item.get("disposition")), "Nonzero command lacks disposition")
        require(item["classification"] != "successful_check" or item["expected_exit"] == 0, "Failed command labeled successful")
    omitted = set()
    for item in plan["omissions"]:
        require(Path(item["identity"]).is_absolute() and hexsha(item["sha256"]) and item.get("reason"), "Unqualified omission")
        require(key(item) not in seen and key(item) not in omitted, "Omission overlaps selected evidence")
        omitted.add(key(item))
    require(isinstance(plan.get("current_scope"), dict), "Missing explicit current scope")
    for name, expected in plan["current_scope"].items():
        relative(name)
        require(hexsha(expected), "Invalid current-scope hash")


def original_sources(plan):
    result = {}
    for item in plan["files"]:
        raw = read(Path(item["source_path"]))
        require(digest(raw) == item["sha256"] and len(raw) == item["bytes"], "Selected original changed: " + item["identity"])
        result[key(item)] = raw
    return result


def git_sources(plan, repository):
    """Read exact regular blobs from the durable base; never current-path fallback."""
    require(repository is not None, "Repository with durable base is required")
    repository = Path(repository).absolute()
    require(not any(p.is_symlink() for p in (repository, *repository.parents)), "Aliased repository")
    base = plan["base"]
    check = subprocess.run(["git", "cat-file", "-e", base + "^{commit}"], cwd=repository, capture_output=True)
    require(check.returncode == 0, "Durable base unavailable; fetch the declared public base commit before verification")
    inventory = subprocess.check_output(["git", "ls-tree", "-rz", base], cwd=repository)
    entries = {}
    for raw in inventory.split(b"\0"):
        if raw:
            meta, path = raw.split(b"\t", 1)
            entries[path.decode()] = meta.decode().split()
    result = {}
    with subprocess.Popen(["git", "cat-file", "--batch"], cwd=repository, stdin=subprocess.PIPE, stdout=subprocess.PIPE) as proc:
        for item in plan["git_references"]:
            entry = entries.get(item["repository_path"])
            require(entry is not None and entry[0] in {"100644", "100755"} and entry[1] == "blob" and entry[2] == item["git_blob"], "Durable Git path/blob differs: " + item["repository_path"])
            proc.stdin.write((item["git_blob"] + "\n").encode())
            proc.stdin.flush()
            header = proc.stdout.readline().decode().split()
            require(len(header) == 3 and header[0] == item["git_blob"] and header[1] == "blob", "Invalid Git blob response")
            raw = proc.stdout.read(int(header[2]))
            require(proc.stdout.read(1) == b"\n", "Truncated Git blob response")
            require(digest(raw) == item["sha256"] and len(raw) == item["bytes"], "Durable Git bytes differ: " + item["repository_path"])
            result[key(item)] = raw
        proc.stdin.close()
        require(proc.wait() == 0, "Git blob reader failed")
    return result


def validate_bindings(plan, originals, repository, *, allow_draft=False):
    selection_valid(plan, allow_draft=allow_draft)
    require(set(originals) == {key(x) for x in plan["files"]}, "Selected archived identity set differs")
    for item in plan["files"]:
        data = originals[key(item)]
        require(digest(data) == item["sha256"] and len(data) == item["bytes"], "Original bytes differ")
    git = git_sources(plan, repository)
    all_sources = originals | git
    for item in plan["commands"]:
        receipt = json.loads(all_sources[key(item["receipt"])])
        require(receipt.get("finished_at") and receipt.get("argv") and type(receipt.get("exit_code")) is int, "Unfinished command receipt")
        require(receipt["exit_code"] == item["expected_exit"], "Command exit differs from selected status")
        log = all_sources.get((receipt["log"], receipt["log_sha256"]))
        require(log is not None and digest(log) == receipt["log_sha256"], "Command log hash/original identity differs")
    return {"status": "PASS", "scope": "Explicit selected evidence bytes and command bindings; not scientific approval or complete external-input replay", "archived_originals": len(originals), "durable_git_references": len(git), "commands": len(plan["commands"]), "qualified_omissions": len(plan["omissions"]), "scientific_approval_added": False, "supervisor_binding": None}


def bound_selection(frozen, selection):
    require(frozen["kind"] == KIND, "Wrong frozen package kind")
    require(digest(selection) == frozen["selection_sha256"], "Selection hash differs")
    plan = json.loads(selection)
    require(plan == frozen["plan"], "Frozen plan differs semantically from selected plan")
    require(plan["run_root"] == frozen["run_root"], "Recorded run root differs")
    selection_valid(plan)
    return plan


def freeze(selection, output):
    raw = read(selection)
    plan = json.loads(raw)
    selection_valid(plan)
    require(plan["base"] == BASE and plan["run_root"] == str(RUN), "Wrong author base/run scope")
    require(output.parent == HERE and not output.exists(), "Freeze destination must be new and run-owned")
    originals = original_sources(plan)
    result = validate_bindings(plan, originals, ROOT)
    require(original_sources(plan) == originals and read(selection) == raw, "Input changed during freeze")
    frozen = {"kind": KIND, "captured_at": datetime.now(timezone.utc).isoformat(), "run_root": str(RUN), "selection_path": str(selection), "selection_sha256": digest(raw), "packager_sha256": digest(read(Path(__file__))), "plan": plan}
    with output.open("xb") as stream:
        stream.write(encoded(frozen))
    return {**result, "frozen": str(output), "sha256": digest(read(output))}


def publish(inputs):
    frozen_bytes = read(inputs)
    frozen = json.loads(frozen_bytes)
    require(frozen["run_root"] == str(RUN), "Wrong frozen author scope")
    require(digest(read(Path(__file__))) == frozen["packager_sha256"], "Packager changed since freeze")
    selection = read(Path(frozen["selection_path"]))
    plan = bound_selection(frozen, selection)
    originals = original_sources(plan)
    validate_bindings(plan, originals, ROOT)
    payloads, container, hashes = payload_archive(originals)
    payloads.update({"selection.final.json": selection, "final-inputs.json": frozen_bytes, "README.md": plan["package_readme"].encode(), "verify.py": read(Path(__file__))})
    manifest = {"schema_version": 1, "files": {name: {"sha256": digest(data), "bytes": len(data)} for name, data in payloads.items()}, "container": container, "originals": [{"identity": identity, "sha256": h, "bytes": len(data), "storage": "blobs/" + h + ".bin" if "blobs/" + h + ".bin" in payloads else "payloads.tar.gz", "member": h} for (identity, h), data in sorted(originals.items())], "unique_payloads": sorted(hashes), "scientific_approval_added": False, "supervisor_binding": None}
    destination = ROOT / DEST
    require(not destination.exists() and not destination.is_symlink() and not any(p.is_symlink() for p in destination.parents), "Publication requires a fresh unaliased directory")
    def final_input_check():
        require(original_sources(plan) == originals and read(Path(frozen["selection_path"])) == selection and digest(read(Path(__file__))) == frozen["packager_sha256"], "Publication inputs changed; partial evidence retained")
        validate_bindings(plan, originals, ROOT)
    write_new_package(destination, payloads, encoded(manifest), final_input_check)
    return verify(destination, ROOT)


def verify(package,repository=None,require_tracked=False,current_scope=False):
 package=package.absolute();manifest=json.loads(read(package/'manifest.json'))
 require(manifest['schema_version']==1 and manifest['scientific_approval_added'] is False and 'supervisor_binding' in manifest and manifest['supervisor_binding'] is None,'Wrong package version/scope')
 require(not any(p.is_symlink() for p in package.rglob('*')),'Aliased package entry')
 actual={str(p.relative_to(package)) for p in package.rglob('*') if p.is_file()}
 require(actual==set(manifest['files'])|{'manifest.json'},'Package membership differs')
 for name,item in manifest['files'].items():
  data=read(package/relative(name));require(digest(data)==item['sha256'] and len(data)==item['bytes'],'Package bytes differ: '+name)
 frozen=json.loads(read(package/'final-inputs.json'));plan=bound_selection(frozen,read(package/'selection.final.json'))
 require(read(package/'README.md')==plan['package_readme'].encode(),'README differs from selected text')
 require(digest(read(package/'verify.py'))==frozen['packager_sha256'],'Verifier identity differs')
 decoded=gzip.decompress(read(package/'payloads.tar.gz'))
 require(digest(decoded)==manifest['container']['decoded_sha256'] and len(decoded)==manifest['container']['decoded_bytes'],'Decoded container differs')
 blobs={}
 with tarfile.open(fileobj=io.BytesIO(decoded),mode='r:') as archive:
  for item in archive:
   require(item.isfile() and hexsha(item.name) and item.name not in blobs,'Unsafe/duplicate archive member')
   data=archive.extractfile(item).read();require(digest(data)==item.name,'Container member identity differs');blobs[item.name]=data
 originals={}
 for item in manifest['originals']:
  identity=key(item);require(identity not in originals,'Duplicate archived original version')
  require(item['member']==item['sha256'],'Original/member SHA differs')
  if item['storage']=='payloads.tar.gz':data=blobs[item['member']]
  else:
   require(item['storage']=='blobs/'+item['sha256']+'.bin','Unexpected raw blob locator');data=read(package/relative(item['storage']))
  require(digest(data)==item['sha256'] and len(data)==item['bytes'],'Archived original bytes differ');originals[identity]=data
 require({digest(data) for data in originals.values()}==set(manifest['unique_payloads']),'Payload index differs')
 require(set(blobs)=={item['sha256'] for item in manifest['originals'] if item['storage']=='payloads.tar.gz'},'Unreferenced container payload')
 require({name for name in manifest['files'] if name.startswith('blobs/')}=={item['storage'] for item in manifest['originals'] if item['storage']!='payloads.tar.gz'},'Unreferenced standalone blob')
 result=validate_bindings(plan,originals,repository)
 require(not (require_tracked or current_scope) or repository is not None,'Repository required for requested scope check')
 if current_scope:
  for name,expected in plan['current_scope'].items():
   data=read(repository/relative(name));require(digest(data)==expected,'Current publication scope differs')
 if require_tracked:
  for name in sorted(actual):
   relative_name=(package/relative(name)).relative_to(repository).as_posix()
   committed=subprocess.check_output(['git','show','HEAD:'+relative_name],cwd=repository)
   require(committed==read(package/relative(name)),'Current committed package blob differs')
 return {'status':'PASS',**result,'archive_members':len(actual),'tracked_checked':require_tracked,'current_scope_checked':current_scope,'scientific_approval_added':False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_subparsers(dest="mode", required=True)
    f = modes.add_parser("freeze"); f.add_argument("--selection", type=Path, required=True); f.add_argument("--output", type=Path, required=True)
    p = modes.add_parser("publish"); p.add_argument("--inputs", type=Path, required=True)
    v = modes.add_parser("verify"); v.add_argument("--package", type=Path, required=True); v.add_argument("--repository", type=Path, required=True); v.add_argument("--require-tracked", action="store_true"); v.add_argument("--current-scope", action="store_true")
    a = parser.parse_args()
    if a.mode == "freeze": result = freeze(a.selection.absolute(), a.output.absolute())
    elif a.mode == "publish": result = publish(a.inputs.absolute())
    else: result = verify(a.package.absolute(), a.repository.absolute(), a.require_tracked, a.current_scope)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
