"""Immutable report transport; fixture repositories remain private evidence.
No scientific YAML is serialized or changed. Fresh pins and old packet members
are rechecked before any publication-directory write.
"""
import pathlib,json,hashlib,os,datetime,subprocess,sys
O=pathlib.Path(__file__).resolve().parents[1];R=next(p for p in O.parents if (p/'MAPPING_SEMANTICS.md').is_file());P=R/'reports/all_unmatched_20261107/worker-03/successors/issue1176-gyps-native-v1'
sys.path.insert(0,str(O/'scripts'));from verify_representation_v1 import verify

def sha(b):return hashlib.sha256(b).hexdigest()
def is_fixture(rel):return any('fixture' in q for q in rel.parts[:-1])
assert not P.exists(),'immutable publication directory exists'
verify(json.loads((O/'proposals.json').read_text()))
assert sha((O/'proposals.json').read_bytes())=='582ea36dd479b8ecd244d996a6eb772569eb232b1631f87ef5f4aa143a20ce67'
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()=='784ee2541506c914b4c34f091de688d39784d548'
for x in json.loads((O/'input-freeze.json').read_text())['inputs']:
 assert sha((O/x['path']).read_bytes())==x['sha256'];assert sha(pathlib.Path(x['source_path']).read_bytes())==x['sha256']
old=R/'reports/all_unmatched_20261107/worker-03/successors/issue1176-dependencies-v1'
for x in json.loads((old/'MANIFEST.json').read_text())['members']:assert sha((old/x['path']).read_bytes())==x['sha256']
rows=[];excluded=[]
for dirpath,dirs,files in os.walk(O,followlinks=False):
 dirs[:]=[d for d in dirs if d not in ['.git','__pycache__']]
 for name in sorted(files):
  src=pathlib.Path(dirpath)/name;rel=src.relative_to(O);s=str(rel)
  if s in ['MANIFEST.json','SHA256SUMS','PUBLICATION-RECEIPT.json','publication-copy-index.json']:continue
  if src.is_symlink():excluded.append({'path':s,'kind':'symlink_descriptor','target':os.readlink(src)});continue
  b=src.read_bytes();item={'path':s,'sha256':sha(b),'bytes':len(b)}
  if is_fixture(rel):excluded.append(dict(item,reason='isolated test fixture; durable private only, not source/candidate/publication'));continue
  rows.append(item)
index={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'private_root':str(O),'report_root':str(P.relative_to(R)),'copies':sorted(rows,key=lambda x:x['path']),'private_fixture_exclusions':sorted(excluded,key=lambda x:x['path']),'excluded_directory_classes':['.git: fixture implementation bookkeeping, not source proof; never credential-scanned','__pycache__: runtimecache'],'scope':'Allselectedledger,payload,before/case/sourceproof,reviewpair,controls/receipts/scripts copiedexactly; fixture heads remain explicitly nonpublication. One native origin only; oldcores untouched.'}
(O/'publication-copy-index.json').write_text(json.dumps(index,indent=2)+'\n');rows.append({'path':'publication-copy-index.json','sha256':sha((O/'publication-copy-index.json').read_bytes()),'bytes':(O/'publication-copy-index.json').stat().st_size})
for row in rows:
 src=O/row['path'];dst=P/row['path'];dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(src.read_bytes());assert sha(dst.read_bytes())==row['sha256']
print(json.dumps({'copied':len(rows),'bytes':sum(x['bytes'] for x in rows),'excluded_fixture_regulars':len(excluded),'report':str(P.relative_to(R))}))
