"""Freeze authorized residual correction inputs; do not alter any predecessor."""
from pathlib import Path
import datetime,hashlib,json,os,shutil,subprocess,sys
T=Path(__file__).resolve().parent;W=T.parents[1];C=W.parents[2];R=W/'reports/all_unmatched_20261107/worker-06';OLD=R/'successor-v3';S=R/'successor-v4';P=C/'preflight/w06-successor-residual-triage-v1';Q=C/'queue/preliminary-v5'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rd(p):return json.loads(p.read_text())
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,ensure_ascii=False,indent=2);f.write('\n')
assert not S.exists();S.mkdir()
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip();branch=subprocess.check_output(['git','branch','--show-current'],cwd=W,text=True).strip();status=subprocess.check_output(['git','status','--short'],cwd=W,text=True)
assert head=='82dce85aea7810941dfdf0bde7480bcdaa0c5826' and branch=='review/all-unmatched-w06-source-review-20261107' and not status
assert sha(P/'author-correction-task.md')=='8fdc345bbdc41dfeb653461d9ef5590ef36a73f2540b7adad53bf2288ca55524'
assert sha(P/'MANIFEST.json')=='e25ba4e8b80cf8764e2b849087f09852f6d769d68a2fc5d3759d70c3bce5ea2b'
manifest=rd(P/'MANIFEST.json')
for f in manifest['files']:assert sha(P/f['path'])==f['sha256'] and (P/f['path']).stat().st_size==f['bytes']
assert len(manifest['files'])==106
preserved=[]
for rel,expected in [('.temp/four-family-independent-v1','0cbe08ffff0c2bd671457b9e367b066a2ce1ad883625cd4de00e4437eddb01ec'),('.temp/ten-unions-independent-v1','b41367c5e50e158df637dcf8def37f1b59f59c8223f4eddeca260482b5f396d5')]:
 d=W/rel;assert sha(d/'MANIFEST.json')==expected;m=rd(d/'MANIFEST.json')
 for f,x in m['files'].items():assert sha(d/f)==x['sha256'] and (d/f).stat().st_size==x['size']
 preserved.append({'path':str(d),'manifest_sha256':expected,'member_count':len(m['files'])})
historical=[]
for manifest_path in [R/'SHA256SUMS',R/'successor-v2/SHA256SUMS',OLD/'SHA256SUMS']:
 count=0
 for line in manifest_path.read_text().splitlines():
  h,p=line.split('  ',1);assert sha(W/p)==h,p;count+=1
 assert hashlib.sha256(subprocess.check_output(['git','show',head+':'+str(manifest_path.relative_to(W))],cwd=W)).hexdigest()==sha(manifest_path)
 historical.append({'path':str(manifest_path.relative_to(W)),'sha256':sha(manifest_path),'members':count})
proposals=rd(OLD/'proposals.json')['proposals'];assert len(proposals)==103
for p in proposals:assert sha(R/p['after_capture']['path'])==p['after_capture']['sha256']
selection=rd(OLD/'selection.json')
for rel in ['decisions.json','proposals.json','evidence.json','source-holds.json','selection.json']:
 assert hashlib.sha256(subprocess.check_output(['git','show',head+':'+str((OLD/rel).relative_to(W))],cwd=W)).hexdigest()==sha(OLD/rel)
copies=[]
def cp(src,rel):
 dst=S/rel;dst.parent.mkdir(parents=True,exist_ok=True);assert not dst.exists();shutil.copyfile(src,dst);assert sha(dst)==sha(src);copies.append({'source':str(src),'path':str(dst.relative_to(R)),'sha256':sha(src)})
for rel in ['author-correction-task.md','MANIFEST.json','HANDOFF.json','README.md','actionable-matrix.json','original-residuals.json','original-resolved12.json','primary-index.json','payload-index.json','positive-water-control.json','additional-inputs.json','pectin-catalog-scope.json','bounded-pectin-proposal-leads.json']:
 cp(P/rel,'triage-provenance/'+rel)
# Exact selected source bodies and original beforeimages; no unrelated fixture tree copied.
for p in sorted((P/'inputs').iterdir()):
 if p.is_file():cp(p,'triage-provenance/inputs/'+p.name)
cp(Q/'shards/shard-06.json','inputs/frozen-shard-06.json')
cp(W/'data/ingredients/mapped/Pectin.yaml','inputs/Pectin-current-before.yaml')
for rel in ['WORKER-CONTRACT.md','scripts/OUTCOME-CONTRACT-v1.md','frozen-baseline.json']:
 cp(C/rel,'contracts/'+Path(rel).name)
cp(Path('/Users/marcin/agent-work/XMechBay/briefs/mim-all-unmatched-ten-workers-20261107.md'),'contracts/user-brief.md')
at=datetime.datetime.now(datetime.timezone.utc).isoformat();save(S/'input-copy-bindings.json',{'at':at,'copies':copies,'original_capture_access_times_unchanged':True})
catalog={str(p.relative_to(W)):sha(p) for p in (W/'data/ingredients').rglob('*.yaml')}
save(T/'catalog-before.json',catalog)
save(S/'acceptance.json',{'at':at,'worker':'06 /root','phase':'immutable residual successor after four-family seal','head':head,'branch':branch,'frozen_shard':{'path':str(Q/'shards/shard-06.json'),'sha256':sha(Q/'shards/shard-06.json')},'triage_manifest_sha256':sha(P/'MANIFEST.json'),'triage_members_verified':106,'author_task_sha256':sha(P/'author-correction-task.md'),'output':str(S),'private_output':str(T),'historical_published_manifests':historical,'sealed_private_reviews':preserved,'predecessor_core':{f:sha(OLD/f) for f in ['decisions.json','proposals.json','evidence.json','source-holds.json','selection.json']},'predecessor_proposal_count':103,'catalogue_records':len(catalog),'catalogue_hash_inventory':{'path':str(T/'catalog-before.json'),'sha256':sha(T/'catalog-before.json')},'maintained_write_or_export_approval':False,'ordinary_commit_and_nonforce_push_authorized':True})
save(S/'progress.json',{'at':at,'state':'authoring pending independent review','residual_groups':['W06-S1217-NEW-001','W06-S1217-NEW-002','W06-S1217-NEW-003'],'retained_source_case_count':188,'retained_occurrence_count':310,'retained_downstream_hold_count':88,'scientific_release_approval':False})
targets=[]
matrix=rd(P/'actionable-matrix.json')
for water in matrix['water_corrections']:
 p=next(p for p in proposals if p['proposal_id']==water['proposal_id']);assert p['after_capture']['sha256']==water['before_payload_sha256']
 targets.append({'target_id':p['proposal_id'],'kind':'source','path':str((R/p['after_capture']['path']).relative_to(W)),'label':water['identity'],'ownership_note':'Uninstalled proposal. No maintained owner beforeimage exists; original proposal beforeimage is exact historical evidence.'})
targets += [{'target_id':'CASE-82','kind':'source','path':str((OLD/'decisions.json').relative_to(W)),'selector':'decisions[82]','label':'Apple-qualified pectin source case','ownership_note':'Source-qualified material assessment; genericPectin is only a comparison owner, never repurposed.'},{'target_id':'CASE-161','kind':'source','path':str((OLD/'decisions.json').relative_to(W)),'selector':'decisions[161]','label':'Yeast Nitrogen Base source contexts','ownership_note':'No exact formulation owner selected; occurrence-specific missing facts corrected only.'}]
save(T/'native-before-targets.json',{'targets':targets})
cmd=[sys.executable,str(W/'scripts/record_review.py'),'inspect','--targets',str(T/'native-before-targets.json')]
for rel in ['AGENTS.md','MAPPING_SEMANTICS.md','docs/record-reviews.md','docs/record-review-profile.md','schema/record_review.yaml','src/mediaingredientmech/schema/mediaingredientmech.yaml','src/mediaingredientmech/schema/mech_shared.yaml']:
 cmd+=['--input',rel]
for rel in ['actionable-matrix.json','author-correction-task.md','primary-index.json']:
 cmd+=['--input',str((S/'triage-provenance'/rel).relative_to(W))]
r=subprocess.run(cmd,cwd=W,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True)
save(S/'native-before-inspect-command.json',{'command':cmd,'cwd':str(W),'exit_code':r.returncode});(S/'native-before-inspect.log').write_text(r.stdout+r.stderr);assert r.returncode==0,r.stderr
save(S/'native-before-inspection.json',json.loads(r.stdout))
print(json.dumps({'triage_verified':106,'previous_reviews_preserved':preserved,'predecessor_payloads':103,'catalogue_records':len(catalog),'native_inspect':r.returncode}))
