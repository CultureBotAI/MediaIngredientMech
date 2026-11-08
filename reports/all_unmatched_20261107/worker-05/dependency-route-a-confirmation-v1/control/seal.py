from pathlib import Path
from datetime import datetime,timezone
import argparse,json,hashlib,shutil,subprocess
W=Path.cwd();S=W/'.temp/w05-dependency-route-a-confirmation-v1';Q=W/'reports/all_unmatched_20261107/worker-05/dependency-route-a-confirmation-v1';P=Q.parent/'buffer-parts-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();j=lambda p:json.loads(p.read_text())
def bind(p):return dict(path=str(p.relative_to(W)),sha256=sha(p))
a=argparse.ArgumentParser();a.add_argument('--scientific-wrapper',type=Path,required=True);a.add_argument('--assembly-review',type=Path,required=True);a=a.parse_args()
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()=='108e213e96f7d423ee345ce265d692e79063127c'
for folder in ['assembly-audit','native-wrapper-review-v1']:
 for f in (S/folder).rglob('*'):
  if f.is_file():
   p=Q/folder/f.relative_to(S/folder);p.parent.mkdir(parents=True,exist_ok=True)
   if p.exists():assert p.read_bytes()==f.read_bytes(),p
   else:shutil.copy2(f,p)
for f in (S/'control').glob('*.py'):
 p=Q/'control'/f.name
 if p.exists():assert p.read_bytes()==f.read_bytes()
 else:shutil.copy2(f,p)
assert j(Q/'validation/native-retained-review-check.receipt.json')['exit_code']==0
assert j(Q/'validation/native-save.receipt.json')['exit_code']==0
sel=j(Q/'selector.json')
for r in sel['canonical_core']:assert sha(W/r['path'])==r['sha256']
for r in sel['dependency_proposals']:assert sha(Q.parent/r['after_capture']['path'])==r['after_capture']['sha256']
assert sha(P/'MANIFEST.json')=='658b1f73e31eb07c562ad61acf54bc3f968e3fd4412389d48881a4da0433a6c6'
for r in j(P/'MANIFEST.json')['files']:assert sha(P/r['path'])==r['sha256']
native_id=j(Q/'native-review-preparation/review-content.json')['review_id'];n=W/'reviews/structured'/native_id
sw=Q/a.scientific_wrapper.resolve().relative_to(S);ar=Q/a.assembly_review.resolve().relative_to(S)
assert sw.is_file() and ar.is_file()
files=[dict(path=str(f.relative_to(Q)),sha256=sha(f),bytes=f.stat().st_size) for f in sorted(Q.rglob('*')) if f.is_file()]
m=dict(schema_version=1,sealed_at=datetime.now(timezone.utc).isoformat(),compiler='/root',branch='review/all-unmatched-w05-source-review-20261107',predecessor_head='108e213e96f7d423ee345ce265d692e79063127c',original_source_head='43f7cf6e8681fa617b5d6d3529d94d537ca01f0d',scope='Immutable report-only confirmation of already published route-A origins; no selected payload, source or proposal changes.',authoritative_selector=bind(Q/'selector.json'),canonical_core=sel['canonical_core'],counts=sel['counts'],route_A=dict(authentic_child_origins=12,generic_conditional=5,ambiguous_new=7,composed_existing=3,full_reviewed_payloads=15,claims_accounted=20,other_origin_generic_pending=3),new_cases=0,new_proposals=0,payload_changes=0,scientific_review=bind(Q/'review/main-review.json'),scientific_wrapper_review=bind(sw),assembly_review=bind(ar),native_review=[bind(n/'review.yaml'),bind(n/'review.md')],native_verdict='needs_curation',source_ledger=bind(Q/'source-scope-ledger.json'),predecessor_manifest=bind(P/'MANIFEST.json'),old_private_packets=bind(Q/'validation/preservation.json'),final_published_head='Recorded after ordinary commit/push in private HANDOFF.json; not a self-referential hash.',source_owner_export_approval=False,self_exclusion='This manifest excludes itself; all listed files are sealed. Final published commit and remote verification are separate private handoff evidence.',files=files)
f=Q/'MANIFEST.json';assert not f.exists();f.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n');print(json.dumps(dict(manifest=bind(f),member_count=len(files),native_id=native_id)))
