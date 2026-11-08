#!/usr/bin/env python3
"""Independent read-only S4 baseline, writing exclusively under this private directory."""
import datetime,hashlib,json,pathlib,subprocess,time
R=pathlib.Path.cwd(); A=R/'reports/all_unmatched_20261107/worker-10'; S=A/'successor-v4'
P=R/'.temp/all-unmatched-worker-10/successor-v5/retention'
C=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
Q=C/'queue/preliminary-v5'
EXPECTED='82fc29d837a223edb9c436445ec7ea13d2840c7b'
TARGET='sv1-bio-calf_blood_togo_m2854'
at=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
started=at();tick=time.monotonic();checks=[];commands=[]
def h(b):return hashlib.sha256(b).hexdigest()
def canon(j):return h(json.dumps(j,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode())
def dump(p,j):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
def command(args):
 t=time.monotonic();r=subprocess.run(args,capture_output=True);commands.append({'command':args,'exit_code':r.returncode,'runtime_seconds':time.monotonic()-t,'stdout':r.stdout.decode(errors='replace') if len(r.stdout)<15000 else None,'stdout_sha256':h(r.stdout),'stderr':r.stderr.decode(errors='replace')});return r
def check(name,v,details=None):checks.append({'check':name,'pass':bool(v),'details':details})
def binding(p):return {'path':str(p.relative_to(R)) if p.is_relative_to(R) else str(p),'sha256':h(p.read_bytes()),'bytes':p.stat().st_size}
def freeze(p,sub):
 b=p.read_bytes();out=P/'frozen'/sub;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(b);return {**binding(p),'private_copy':str(out.relative_to(R))}

P.mkdir(parents=True,exist_ok=True)
if (P/'baseline-v1.json').exists():raise RuntimeError('Baseline already exists; do not overwrite frozen receipt.')
head=command(['git','rev-parse','HEAD']).stdout.decode().strip();status=command(['git','status','--porcelain=v1','--untracked-files=no']).stdout.decode();check('Expected published HEAD',head==EXPECTED,head);check('Tracked worktree clean at baseline',not status,status)
selection=json.loads((S/'selection-v2.json').read_text());sb=freeze(S/'selection-v2.json','selection-v2.json');core={};corebindings={}
for n,desc in selection['authoritative_core'].items():
 p=A/desc['path'];j=json.loads(p.read_text());core[n]=j;corebindings[n]=freeze(p,pathlib.Path('final-core')/n);check('Authoritative core '+n,h(p.read_bytes())==desc['sha256'],{'expected':desc['sha256'],'actual':h(p.read_bytes())})
ps=core['proposals.json']['proposals'];ds=core['decisions.json']['decisions'];es=core['evidence.json']['evidence'];pm={p['proposal_id']:p for p in ps};dm={d['case_id']:d for d in ds};em={e['evidence_id']:e for e in es}
selected=selection['selected_payloads'];check('127 unique selected proposals',len(ps)==len(pm)==len(selected)==127);check('188 unique cases',len(ds)==len(dm)==188)
occ=[oid for d in ds for oid in d['occurrence_ids']];check('304 original occurrence IDs',len(occ)==len(set(occ))==304,{'memberships':len(occ),'unique':len(set(occ))})
check('Selected IDs exactly core IDs',{p['proposal_id'] for p in selected}==set(pm))
payloads=[];git_compare_paths=[S/'selection-v2.json']+[A/x['path'] for x in selection['authoritative_core'].values()]
for row in selected:
 p=pm[row['proposal_id']];c=p['after_capture'];path=A/c['path'];b=path.read_bytes();check('Selected entry mirrors proposal '+p['proposal_id'],row['after_capture']==c and row['case_ids']==p['case_ids'] and row['owner_path']==p['owner_path'] and row['before_sha256']==p.get('before_sha256'))
 check('Payload hash '+p['proposal_id'],h(b)==c['sha256'])
 check('Proposal backlinks '+p['proposal_id'],all(cid in dm and p['proposal_id'] in dm[cid]['proposal_ids'] for cid in p['case_ids']))
 payloads.append({'proposal_id':p['proposal_id'],'proposal_object_sha256':canon(p),'case_ids':p['case_ids'],'owner_path':p['owner_path'],'before_sha256':p.get('before_sha256'),'after_capture':c,'target':p['proposal_id']==TARGET,'frozen_payload':freeze(path,pathlib.Path('payloads')/c['path'])});git_compare_paths.append(path)
check('Only one baseline target',len([p for p in payloads if p['target']])==1)
target=pm[TARGET];check('Target published selected hash',target['after_capture']['sha256']=='62f0dc3300c488be2fb9d52f2c65e8e6826715d81177cf8e4ce48af422ed7338')
check('Target case44 only',target['case_ids']==[next(d['case_id'] for d in ds if d['source_index']==44)])
sentinels=[]
for p in payloads:
 if 'carbonate_co2' in p['proposal_id'].lower() or 'isp4' in json.dumps(p).lower() or 'isp_4' in json.dumps(p).lower():sentinels.append(p)
check('Carbonate135788 retained baseline',any(p['after_capture']['sha256']=='135788bfd2a511671a90ff9b912092df789c9209995f88d11b4aa6134eca0625' for p in sentinels))
check('ISP4 sentinel found',any('isp4' in json.dumps(p).lower() or 'isp_4' in json.dumps(p).lower() for p in sentinels))

# Frozen source objects and all snapshots checked at their real source paths.
shard=Q/'shards/shard-10.json';q=json.loads(shard.read_text());casebindings=[];snapshotbindings={}
for d in ds:
 original=q['cases'][d['source_index']];check('Source case digest '+str(d['source_index']),canon(original)==d['case_input_sha256']);check('Original source case ID '+str(d['source_index']),original['case_id']==d['case_id']);check('Original occurrences '+str(d['source_index']),sorted(o['occurrence_id'] for o in original.get('occurrences',[]))==sorted(d['occurrence_ids']))
 for o in original.get('occurrences',[]):
  path=Q/o['full_recipe_snapshot'];actual=h(path.read_bytes());check('Source snapshot '+o['occurrence_id'],actual==o['source_file_sha256']);snapshotbindings[o['full_recipe_snapshot']]={'path':str(path),'sha256':actual,'bytes':path.stat().st_size}
 casebindings.append({'source_index':d['source_index'],'case_id':d['case_id'],'source_case_sha256':canon(original),'decision_object_sha256':canon(d),'occurrence_ids':d['occurrence_ids'],'proposal_ids':d['proposal_ids']})

# Read Git objects for the actual authoritative core and every selected payload.
gitchecks=[]
for path in dict.fromkeys(git_compare_paths):
 rel=str(path.relative_to(R));r=command(['git','show',EXPECTED+':'+rel]);actual=h(path.read_bytes());same=r.returncode==0 and h(r.stdout)==actual;gitchecks.append({'path':rel,'working_sha256':actual,'published_blob_sha256':h(r.stdout),'git_exit':r.returncode,'equal':same});check('Published bytes '+rel,same)

# Ignored-inclusive explicit filesystem walk; successor-v5 is excluded as new work.
old_artifacts=[binding(p) for p in sorted(A.rglob('*')) if p.is_file() and not p.is_relative_to(A/'successor-v5')]
old_s4=[x for x in old_artifacts if x['path'].startswith(str(S.relative_to(R))+'/')]
owners=[binding(p) for p in sorted((R/'data/ingredients').rglob('*.yaml'))]
canonical_reviews=[binding(p) for p in sorted((R/'data/reviews').rglob('*')) if p.is_file()] if (R/'data/reviews').exists() else []
contexts=[]
for path in sorted((C/'preflight/w10-calf-wording-triage-v1').rglob('*')):
 if path.is_file():contexts.append(binding(path))
manifest={'old_artifact_files':old_artifacts,'old_s4_files':old_s4,'maintained_owner_files':owners,'existing_canonical_review_files':canonical_reviews,'source_snapshot_files':list(snapshotbindings.values()),'triage_context_files':contexts}
dump(P/'preservation-baseline-v1.json',manifest)
dump(P/'commands-v1.json',{'commands':commands,'script':binding(pathlib.Path(__file__).resolve()),'PYTHONDONTWRITEBYTECODE':'1'})
dump(P/'frozen/original-cases.json',q)
receipt={'schema_version':1,'status':'PASS_BASELINE_FROZEN' if all(x['pass'] for x in checks) else 'FAIL_BASELINE_REQUIRES_REVIEW','reviewer':'Codex /root/buffers_research; independent retention/metadata reviewer for root-authored calf wording successor','scope':'Mechanical and metadata retention, not source-science approval. Prior serum/buffer authorship and broad preservation review involvement disclosed; none of those scientific approvals is renewed. Target science is assigned to preparation_skeptic.','started_at':started,'completed_at':at(),'runtime_seconds':time.monotonic()-tick,'head':head,'selection':sb,'authoritative_core':corebindings,'proposal_count':len(ps),'case_count':len(ds),'occurrence_count':len(occ),'unaffected_payload_count':len(ps)-1,'target_proposal_id':TARGET,'target_source_index':44,'payloads':payloads,'sentinels':sentinels,'case_bindings':casebindings,'evidence_object_bindings':[{'evidence_id':e['evidence_id'],'canonical_sha256':canon(e),'capture':e['capture']} for e in es],'git_object_checks':gitchecks,'preservation_manifest':binding(P/'preservation-baseline-v1.json'),'preservation_counts':{k:len(v) for k,v in manifest.items()},'checks':checks,'historical_metadata_note':'S4 finalization-binding.json is historical; authoritative selection-v2/final-core hashes govern this comparison. Its older evidence binding is preserved unchanged, never rewritten as a new current claim.','allowed_successor_scope':'Only target calf44 active explanatory notes/mapping-evidence explanation, proposal/case reasoning, appended history and exact dependency/review/selection metadata may change. All identity/form/ontology IDs and predicates, labels/aliases, source cases/occurrences, other126 payloads, original histories and all source/role/export holds remain.','future_steps':['Compare root candidate and final-core exact per-object deltas to this baseline.','Require independent target-source exact-byte review and inspect final native/handoff metadata without inheriting broad scientific approval.']}
dump(P/'baseline-v1.json',receipt)
print(json.dumps({'status':receipt['status'],'baseline':binding(P/'baseline-v1.json'),'counts':receipt['preservation_counts'],'proposals':len(ps),'cases':len(ds),'occurrences':len(occ),'checks':len(checks),'failures':[x for x in checks if not x['pass']]}))
