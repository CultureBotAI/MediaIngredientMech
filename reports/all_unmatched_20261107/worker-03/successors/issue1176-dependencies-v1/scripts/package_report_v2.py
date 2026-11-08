"""Copy selected report evidence without mutating inputs or duplicating disposable fixture roots.
The sealed skeptical subtree is copied whole, including its67members. Other duplicate
fixture bytes remain durably sealed in the private packet; exact report exclusions
are enumerated. Original failing output and changed-parent bytes are copied explicitly.
"""
import pathlib,json,hashlib,shutil,datetime,os
O=pathlib.Path(__file__).resolve().parents[1];R=next(p for p in O.parents if (p/'MAPPING_SEMANTICS.md').is_file())
P=R/'reports/all_unmatched_20261107/worker-03/successors/issue1176-dependencies-v1'
def sha(b):return hashlib.sha256(b).hexdigest()
assert not P.exists(),'immutable report destination already exists'
# Preserve irreducible failing reproduction bytes in the report as well as private fixture.
for src,dst in [('skeptical-review/guard-drift-fixture-v1/inputs/targets/Peptone.yaml','reproduction-evidence/v1-mutated-parent.yaml'),('skeptical-review/guard-drift-fixture-v1/payloads/PYGS.yaml','reproduction-evidence/v1-false-output-PYGS.yaml')]:
 p=O/dst;p.parent.mkdir(parents=True,exist_ok=True);assert not p.exists();p.write_bytes((O/src).read_bytes())
members=[];excluded=[]
for p in sorted(O.rglob('*')):
 rel=p.relative_to(O);s=str(rel)
 if p.is_symlink():excluded.append({'path':s,'kind':'symlink_descriptor','target':os.readlink(p),'reason':'negative-control alias preserved only in private sealed packet'});continue
 if not p.is_file():continue
 if rel.parts[0]!='skeptical-review' and any('fixture' in x or x.startswith('drift-v2-') or x=='__pycache__' for x in rel.parts):
  excluded.append({'path':s,'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size,'reason':'duplicate isolated control fixture; scripts and outcome evidence plus single exact primary/input copies published; full private bytes preserved'});continue
 if s in ['MANIFEST.json','SHA256SUMS','PUBLICATION-RECEIPT.json','publication-copy-index.json']:continue
 members.append({'path':s,'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size})
index={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_private_root':str(O),'publication_root':str(P.relative_to(R)),'copied_members':members,'excluded_private_fixture_members':excluded,'policy':'No prior packet changed or deleted; regular evidence bytes copied exactly. Only dependency-selection.json /payloads-v2 are active. All historical v1 artifacts unselected.'}
(O/'publication-copy-index.json').write_text(json.dumps(index,indent=2)+'\n');members.append({'path':'publication-copy-index.json','sha256':sha((O/'publication-copy-index.json').read_bytes()),'bytes':(O/'publication-copy-index.json').stat().st_size})
for x in members:
 src=O/x['path'];dest=P/x['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest);assert sha(dest.read_bytes())==x['sha256']
print(json.dumps({'report':str(P.relative_to(R)),'copied':len(members),'excluded_duplicate_fixture_members':len(excluded),'bytes':sum(x['bytes'] for x in members)},indent=2))
