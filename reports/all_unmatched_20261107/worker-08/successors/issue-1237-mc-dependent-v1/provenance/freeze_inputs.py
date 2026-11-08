from pathlib import Path
import json,hashlib,shutil,subprocess,datetime
R=Path.cwd();P=R/'.temp/mc-dependent-successor-v1';C=R.parents[3];U=C/'workers/w09/worktree/.temp/tenvit-mc-continuity-decision-v1';O=R/'reports/all_unmatched_20261107/worker-08/successors/issue-1237-mc-dependent-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()=='a0190fed72b8f5119432003d1f9c84b8c1de7a48'
assert sha(U/'HANDOFF.json')=='55be71c0d3e12f780159cf62efb2b96f5cd37433fb2ad4cb794cafb25446b843'
assert sha(U/'MANIFEST.json')=='4369c762e0fd0c14b6d240a79870f61dcc8f2ec313295341160a8b939755dffa'
m=json.loads((U/'MANIFEST.json').read_text());pins={x['path']:x for x in m['files']}
for x in m['files']:
 f=U/x['path'];assert not f.is_symlink();assert sha(f)==x['sha256'],f
selected=['HANDOFF.json','MANIFEST.json','SEAL.json','decision-v2.json','candidate-suggestions.json','source-routing-and-origin-bindings.json','source-routing-inherited.json','input-pins.json','mc-primary/capture-register.json','mc-primary/additional-source-bindings.json','mc-primary/Mc-complete-source-occurrences.json','mc-primary/authentic-history-beforeimages.json','mc-primary/complete-mix-blocks.json','mc-primary/component-cas-full-rows.json','mc-primary/live-sheet-block-continuity.json','mc-primary/live-cas-claim-continuity.json','mc-primary/captures/Mixes.csv','mc-primary/captures/compounds_to_cas.csv','mc-primary/captures/Medias.csv','mc-primary/captures/mc-thesis2014.pdf','mc-primary/captures/mc-thesis2014.txt','mc-primary/probes/mc-thesis2014.pdf.retry.json','primary/captures/ols31345-retry.capture','primary/probes/ols31345-retry.json','primary/captures/sigma-c8731-web-response.json','inputs/primary/C-E-jcm-197.capture','inputs/primary/C-E-nbrc-837.capture','inputs/primary/vm-fetch-2630e40c26a0b155.capture','mc-primary/HANDOFF.json','primary/HANDOFF.json','primary/assessment-v2.json','primary/review-correction-v2.json','skeptic/peer-review-mc-primary.json','skeptic/peer-review-atcc-primary-v2.json','skeptic/final-assembly-review.json']
O.mkdir(exist_ok=False);copied=[]
for rel in selected:
 src=U/rel;dest=O/'inputs/w09-continuity'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest);assert sha(dest)==sha(src);copied.append({'original_path':str(src),'published_path':str(dest.relative_to(R)),'sha256':sha(src),'acquisition_timestamps':'Preserved in exact source receipts; copying is not new retrieval.'})
for f in (P/'inputs').iterdir():
 dest=O/'inputs'/f.name;shutil.copy2(f,dest)
owner=R/'data/ingredients/mapped/Mc_vitamins.yaml';assert sha(owner)=='59c53dfe4e273ebfc7c3fe86fd4244978868ff1879dcde97af64bbeb61c07123'
(O/'beforeimages').mkdir();shutil.copy2(owner,O/'beforeimages/Mc_vitamins.yaml')
assert sha(C/'integration/worktree/data/ingredients/mapped/Mc_vitamins.yaml')==sha(owner)
contracts=['AGENTS.md','MAPPING_SEMANTICS.md','.claude/skills/curate-yaml-record/SKILL.md','.claude/skills/add-media/SKILL.md','docs/record-reviews.md','docs/record-review-profile.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','src/mediaingredientmech/curate/curation_event.py','src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/validation/component_partonomy.py']
oldsealpaths=['.temp/four-source-acceptance-binding-audit-v1/SEAL.json','.temp/crosswalk1247-v3-independent-v1/SEAL.json','.temp/w06-residual-successor-independent-v1/SEAL.json','.temp/w05-published-head-independent-review-v1/SEAL.json','.temp/all-unmatched-worker-08/tenvit-dependent-v1/FINAL-SEAL.json','.temp/all-unmatched-worker-08/plain-flour-process-replay-v1/FINAL-SEAL.json']
oldseals=[]
for rel in oldsealpaths:
 p=R/rel
 if p.exists():oldseals.append({'path':str(p),'sha256':sha(p)})
save(O/'inputs/source-ref-index.json',{'upstream_manifest_sha256':sha(U/'MANIFEST.json'),'upstream_members_verified':len(m['files']),'selected_captures':copied,'native_contracts':[{'path':x,'sha256':sha(R/x)} for x in contracts],'retained_old_seals':oldseals,'scope':'Exact selected primary/context bytes only. This is not a copy or new acceptance of the full upstream archive.'})
save(P/'entry.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':'a0190fed72b8f5119432003d1f9c84b8c1de7a48','branch':subprocess.check_output(['git','branch','--show-current'],text=True).strip(),'owner_path':str(owner.relative_to(R)),'before_sha256':sha(owner),'upstream_manifest_members_verified':len(m['files']),'source_input_index_sha256':sha(O/'inputs/source-ref-index.json'),'prior_seals':oldseals,'network_failure':'Initial read-only gh API requests failed connecting toapi.github.com; empty initial files retained. Approved read-only retry returned both exact comments; no GitHub mutation.'})
(O/'provenance').mkdir();shutil.copy2(Path(__file__),O/'provenance/freeze_inputs.py');print(json.dumps({'copied':len(copied),'upstream_verified':len(m['files']),'before':sha(owner),'output':str(O)},indent=2))
