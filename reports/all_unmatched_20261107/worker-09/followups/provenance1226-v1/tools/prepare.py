import sys
sys.dont_write_bytecode = True
from pathlib import Path
import json, hashlib, subprocess, datetime, shutil

P=Path(__file__).resolve().parent
ROOT=P.parents[1]
C=ROOT.parents[2]
PLAN=C/'preflight/w01-w09-author-task-planning-v1'
OLD=ROOT/'reports/all_unmatched_20261107/worker-09'
R=OLD/'followups/provenance1226-v1'
HEAD='77d6beaea5793a0a763957b99e8141ff12b216d2'
sha=lambda b:hashlib.sha256(b).hexdigest()
canon=lambda x:sha(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
read=lambda p:json.loads(p.read_text())
def save(p,d):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def cp(a,b):
    b.parent.mkdir(parents=True,exist_ok=True)
    with b.open('xb') as f:f.write(a.read_bytes())

assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()==HEAD
assert not subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True).strip()
remote=read(P/'probes/remote-head-live.json')
assert remote['exit_code']==0 and remote['stdout'].split()[0]==HEAD
planning=[]
for r in read(PLAN/'MANIFEST.json')['files']:
    f=PLAN/r['path'];actual=sha(f.read_bytes());assert actual==r['sha256'],str(f)
    planning.append({'path':r['path'],'sha256':actual})
assert len(planning)==135
W=next(r for r in read(P/'inputs/current-worker-bindings.json')['workers'] if r['worker']==9)
for r in list(W['core'].values())+[W['effective_decisions']]+W['all_selected_payloads']:
    f=Path(r['path']);assert sha(f.read_bytes())==r['sha256']
    assert sha(subprocess.check_output(['git','show',HEAD+':'+str(f.relative_to(ROOT))],cwd=ROOT))==r['sha256']
assert len(W['all_selected_payloads'])==32
preserved=[]
for name,expected in [('fresh-campaign-companion-review-v1','09eb0b030135d9f7650c955ba72590d5445a7fdf9d9bda182999b81bde65c9b2'),('w04-authoritative-successor-science-v1','ea6638a88a33360e8ae68915026f0ba4060dc493c69886120c2e5614d88045b6'),('w06-successor1217-independent-v1','09e127dff38aa4e71edac4458038ef0990304af288768777953445c5487e7218')]:
    d=ROOT/'.temp'/name;m=read(d/'FINAL-MANIFEST.json');assert sha((d/'FINAL-MANIFEST.json').read_bytes())==expected
    for e in m['files']:assert sha((d/e['path']).read_bytes())==e['sha256'],str(d/e['path'])
    assert {str(f.relative_to(d)) for f in d.rglob('*') if f.is_file()}=={x['path'] for x in m['files']}|set(m['excludes'])
    preserved.append({'path':str(d),'manifest_sha256':expected,'members':len(m['files']),'exact_membership':True})
oldfiles=[{'path':str(f.relative_to(ROOT)),'sha256':sha(f.read_bytes())} for f in sorted(OLD.rglob('*')) if f.is_file()]
audit=C/'workers/w02/worktree/.temp/campaign-evidence-provenance-audit-v1/provenance'
auditproof=[];auditrows={}
for n,expected in [('entry-provenance-ledger-v1.json','98bfa525356aa223a08fcd2be11d9dc7476231aa6cd9efa4db1f85b2e66109e2'),('native-type-suggestions-v1.json','9ca6b04f03fdaabd65dacd90a160cf9f51dc549e607b5f5634616469532f1b33')]:
    f=audit/n;assert sha(f.read_bytes())==expected
    auditrows[n]=[r for r in read(f)['rows'] if r.get('worker')==9]
    assert len(auditrows[n])==9
    auditproof.append({'path':str(f),'sha256':expected,'selected_rows':9})
R.mkdir(exist_ok=False)
for n in ['w09-author-task-DRAFT.md','w09-eight-entry-allowlist.json','w09-preserved-historical-exception.json','current-worker-bindings.json','MANIFEST.json','HANDOFF.json']:
    cp(P/'inputs'/n,R/'inputs'/n)
for f in (P/'probes').glob('*.json'):cp(f,R/'inputs/probes'/f.name)
save(R/'inputs/w02-nine-row-audit-extract.json',{'source_files':auditproof,'extracted_complete_rows':auditrows,'scientific_review':False})
for n,spec in W['core'].items():cp(Path(spec['path']),R/'predecessor-cores'/n)
cp(Path(W['effective_decisions']['path']),R/'effective-decisions.json')
cp(OLD/'common/frozen-shard-09.json',R/'inputs/frozen-shard-09.json')
for r in W['all_selected_payloads']:
    cp(Path(r['path']),R/'predecessors'/(r['entry_id'].split('::',1)[1]+'.yaml'))
contracts=['AGENTS.md','MAPPING_SEMANTICS.md','docs/record-reviews.md','docs/record-review-profile.md','.claude/skills/curate-yaml-record/SKILL.md','.claude/skills/review-yaml-record/SKILL.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/curate/curation_event.py','src/mediaingredientmech/synonym_policy.py','src/mediaingredientmech/sssom_grading.py','scripts/record_review.py','schema/record_review.yaml']
save(R/'preflight.json',{'status':'PASS','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_head':HEAD,'branch':W['branch'],'w09_binding':W,'planning_manifest':{'path':str(PLAN/'MANIFEST.json'),'sha256':sha((PLAN/'MANIFEST.json').read_bytes()),'members':planning},'preserved_private_packets':preserved,'original_report_files':oldfiles,'contracts':[{'path':n,'sha256':sha((ROOT/n).read_bytes())} for n in contracts],'audit_sources':auditproof,'scientific_review':False,'authorization':'Current user explicitly dispatches the draft and authorizes ordinary commit/non-force push after checks and independent final review. No maintained/other-worker writes or release approval.'})
cp(Path(__file__),R/'tools/prepare.py')
print(json.dumps({'status':'PASS','planning_members':len(planning),'selected_payloads':32,'source_cases':len(read(R/'effective-decisions.json')['decisions']),'original_report_files':len(oldfiles),'preserved_private_members':sum(x['members'] for x in preserved),'output':str(R)}))
