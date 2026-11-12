from pathlib import Path
import contextlib, hashlib, importlib.util, json, os, sys
T=Path(__file__).resolve().parents[1]
W=T/'worktree'; R=T/'reviewer'/'publication-boundaries-recheck-v3'; R.mkdir(exist_ok=False)
REPORT=W/'reports/kgm_unmapped_chemicals_20261107'
def h(b): return hashlib.sha256(b).hexdigest()
def load(name,path):
 s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
alias=load('alias_writer',W/'scripts/curate_mediadive_acetate_alias.py')
pub=load('alias_publisher',W/'scripts/publish_mediadive_acetate_alias.py')
results=[]
def call(mod,args):
 old=sys.argv; sys.argv=[str(mod.__file__),*map(str,args)]
 try: mod.main(); return {'returned_success':True}
 except Exception as e: return {'returned_success':False,'exception':type(e).__name__,'message':str(e)}
 finally: sys.argv=old
root=R/'owner-hardlink'; owner=root/alias.OWNER; owner.parent.mkdir(parents=True)
before=(REPORT/'sodium-acetate/write/owner-before.yaml').read_bytes(); owner.write_bytes(before)
unrelated=root/'unrelated-preserved-copy.yaml'; os.link(owner,unrelated)
r=call(alias,['--root',root,'--evidence',REPORT/'sodium-acetate/sources','--receipt-dir',root/'receipts','--apply'])
r.update(case='owner_hardlink',before_sha256=h(before),owner_after_sha256=h(owner.read_bytes()),unrelated_after_sha256=h(unrelated.read_bytes()),unrelated_modified=unrelated.read_bytes()!=before)
results.append(r)
def setup(name):
 root=R/name; cp=root/pub.SOURCE; cp.parent.mkdir(parents=True); cp.write_bytes((REPORT/'sodium-acetate/publication/canonical-before.tsv').read_bytes())
 op=root/pub.OWNER; op.parent.mkdir(parents=True); op.write_bytes((W/pub.OWNER).read_bytes())
 c=root/'candidate.tsv'; c.write_bytes((REPORT/'native-generation/native-candidate.sssom.tsv').read_bytes())
 m=root/'manifest.json'; doc=json.loads((REPORT/'native-generation/native-candidate.sssom.tsv.manifest.json').read_bytes())
 for x in doc['source_inputs']:
  if x['path'].endswith('/'+pub.OWNER): x['path']=str(op)
 m.write_text(json.dumps(doc)); return root,cp,c,m
root,cp,c,m=setup('canonical-hardlink'); before=cp.read_bytes(); unrelated=root/'unrelated-canonical-copy.tsv'; os.link(cp,unrelated)
r=call(pub,['--root',root,'--candidate',c,'--manifest',m,'--receipt-dir',root/'receipts','--apply']);r.update(case='canonical_hardlink',before_sha256=h(before),canonical_after_sha256=h(cp.read_bytes()),unrelated_after_sha256=h(unrelated.read_bytes()),unrelated_modified=unrelated.read_bytes()!=before);results.append(r)
root,cp,c,m=setup('late-manifest-change'); initial=m.read_bytes(); native_reserve=pub.reserve_receipt_outputs
@contextlib.contextmanager
def changed_manifest(*args,**kwargs):
 with native_reserve(*args,**kwargs) as handles:
  doc=json.loads(m.read_bytes()); doc['source_revisions']['claw']='0'*40; doc['external_sssom_validation']='FAILED'; m.write_text(json.dumps(doc)); yield handles
pub.reserve_receipt_outputs=changed_manifest
r=call(pub,['--root',root,'--candidate',c,'--manifest',m,'--receipt-dir',root/'receipts','--apply']);r.update(case='late_manifest_change',original_manifest_sha256=h(initial),mutated_manifest_sha256=h(m.read_bytes()),mutated_manifest_declares_validation=json.loads(m.read_bytes())['external_sssom_validation'])
if (root/'receipts/projection.json').exists():
 raw=(root/'receipts/projection.json').read_bytes(); r['receipt']=json.loads(raw) if raw else None; r['empty_receipt_preserved']=not bool(raw)
results.append(r)
report={'scripts':{str(Path(x.__file__).relative_to(W)):h(Path(x.__file__).read_bytes()) for x in (alias,pub)},'results':results,'all_fixture_paths':str(R),'maintained_files_modified':False}
(R/'result.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
