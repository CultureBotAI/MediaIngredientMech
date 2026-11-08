#!/usr/bin/env python3
"""Read-only published S5 retention baseline; outputs exclusively private S6/retention."""
import datetime,hashlib,json,pathlib,subprocess,time,yaml
R=pathlib.Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v5';P=R/'.temp/all-unmatched-worker-10/successor-v6/retention';C=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107');Q=C/'queue/preliminary-v5';T=C/'preflight/w10-family-residual-triage-v1';HEAD='3e190a0f6c5a978ca8ed7e3bc7b6a2d66935548b'
at=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();h=lambda b:hashlib.sha256(b).hexdigest();started=at();tick=time.monotonic();checks=[];commands=[]
def canon(x):return h(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode())
def rd(p):return json.loads(p.read_text())
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def bind(p):return {'path':str(p.relative_to(R)) if p.is_relative_to(R) else str(p),'sha256':h(p.read_bytes()),'bytes':p.stat().st_size}
def ck(n,v,detail=None):checks.append({'check':n,'pass':bool(v),'detail':detail})
def run(argv):
 t=at();t0=time.monotonic();r=subprocess.run(argv,capture_output=True);commands.append({'argv':argv,'started_at':t,'finished_at':at(),'runtime_seconds':time.monotonic()-t0,'exit_code':r.returncode,'stdout_sha256':h(r.stdout),'stderr':r.stderr.decode(errors='replace')});ck('Command success '+str(argv),r.returncode==0);return r.stdout

def freeze(path,rel):
 b=path.read_bytes();out=P/'frozen'/rel;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(b);return {**bind(path),'private_copy':str(out.relative_to(R))}
if (P/'baseline-v1.json').exists():raise RuntimeError('Frozen baseline already exists')
head=run(['git','rev-parse','HEAD']).decode().strip();status=run(['git','status','--porcelain=v1','--untracked-files=no']).decode();ck('Exact published S5 head',head==HEAD);ck('Tracked clean baseline',not status,status)
fmt=run(['git','rev-parse','--show-object-format']).decode().strip();ck('Git object format SHA1',fmt=='sha1')
tracked={}
for ent in run(['git','ls-tree','-r','-z',HEAD]).split(b'\0'):
 if not ent:continue
 info,path=ent.split(b'\t',1);mode,kind,oid=info.decode().split();tracked[path.decode()]=oid

def git_equal(path):
 rel=str(path.relative_to(R));b=path.read_bytes();oid=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();ok=tracked.get(rel)==oid;ck('Published Git blob '+rel,ok);return {'path':rel,'sha256':h(b),'computed_git_blob_oid':oid,'published_git_blob_oid':tracked.get(rel),'equal':ok}
tri=rd(T/'TRIAGE-v2.json');targets={x['proposal_id']:x for x in tri['rows']};ck('Exactly five scoped targets',len(targets)==5)
selection=rd(S/'selection.json');sbind=freeze(S/'selection.json','selection.json');core={};corebind={};gitchecks=[git_equal(S/'selection.json')]
for n,x in selection['authoritative_core'].items():
 p=A/x['path'];ck('Selection authoritative hash '+n,h(p.read_bytes())==x['sha256']);core[n]=rd(p);corebind[n]=freeze(p,pathlib.Path('final-core')/n);gitchecks.append(git_equal(p))
ps=core['proposals.json']['proposals'];ds=core['decisions.json']['decisions'];es=core['evidence.json']['evidence'];pm={p['proposal_id']:p for p in ps};dm={d['case_id']:d for d in ds};em={e['evidence_id']:e for e in es}
ck('127 unique proposals',len(ps)==len(pm)==127);ck('188 unique cases',len(ds)==len(dm)==188);ck('1212 original evidence',len(es)==len(em)==1212)
occ=[o for d in ds for o in d['occurrence_ids']];ck('304 unique occurrences',len(occ)==len(set(occ))==304);ck('Selection and proposal IDs equal',{p['proposal_id'] for p in selection['selected_payloads']}==set(pm));ck('Five targets selected',set(targets)<=set(pm))
payloads=[];target_inventory=[]
for row in selection['selected_payloads']:
 p=pm[row['proposal_id']];c=p['after_capture'];path=A/c['path'];b=path.read_bytes();ck('Payload actual '+p['proposal_id'],h(b)==c['sha256']);ck('Selected row exact '+p['proposal_id'],all(row[k]==p.get(k,p['owner_path'] if k=='destination_path' else None) for k in row));ck('Case backlinks '+p['proposal_id'],all(p['proposal_id'] in dm[c]['proposal_ids'] for c in p['case_ids']));pb=freeze(path,pathlib.Path('payloads')/c['path']);gitchecks.append(git_equal(path));payloads.append({'proposal_id':p['proposal_id'],'proposal_object_sha256':canon(p),'case_ids':p['case_ids'],'owner_path':p['owner_path'],'before_sha256':p.get('before_sha256'),'after_capture':c,'target':p['proposal_id'] in targets,'frozen_payload':pb})
 if p['proposal_id'] in targets:
  t=targets[p['proposal_id']];y=yaml.safe_load(b);ck('Triage/current exact payload '+p['proposal_id'],t['payload_sha256']==h(b));ck('Triage/current exact assertion '+p['proposal_id'],t['current_assertion']==y['component_assertion']);ck('Triage/current exact components '+p['proposal_id'],t['components']==y['components']);target_inventory.append({'proposal_id':p['proposal_id'],'payload':c,'complete_proposal':p,'complete_current_payload':y,'case_indices':[dm[c]['source_index'] for c in p['case_ids']],'case_ids':p['case_ids'],'occurrence_ids':[o for c in p['case_ids'] for o in dm[c]['occurrence_ids']],'current_assertion':y['component_assertion'],'permitted_assertion':t['recommendation'],'permitted_scope':t['scope'],'preserve':t['preserve']})
case_union=sorted({i for x in target_inventory for i in x['case_indices']});ck('Six exact target cases',case_union==[65,87,94,102,125,178]);ck('122 unaffected selected payloads',sum(not p['target'] for p in payloads)==122)
sentinels=[p for p in payloads if 'carbonate_co2' in p['proposal_id'] or p['proposal_id']=='sv1-bio-calf_blood_togo_m2854' or 'isp4' in p['proposal_id']]
ck('Carbonate exact retained sentinel',any(p['after_capture']['sha256']=='135788bfd2a511671a90ff9b912092df789c9209995f88d11b4aa6134eca0625' for p in sentinels));ck('Calf exact retained sentinel',any(p['after_capture']['sha256']=='7a54c5bb03008949dec5ced0fbb8da9deee348fd4ad2473e66d41655db975b9d' for p in sentinels));ck('ISP4 retained sentinel',any(p['proposal_id']=='sv2-isp4-jcm58-complete-formulation' for p in sentinels))
shard=rd(Q/'shards/shard-10.json');casebindings=[];snapshots={}
for d in ds:
 original=shard['cases'][d['source_index']];ck('Original case hash '+str(d['source_index']),canon(original)==d['case_input_sha256']);ck('Original ID '+str(d['source_index']),original['case_id']==d['case_id']);ck('Original occurrence IDs '+str(d['source_index']),sorted(o['occurrence_id'] for o in original.get('occurrences',[]))==sorted(d['occurrence_ids']))
 for o in original.get('occurrences',[]):
  path=Q/o['full_recipe_snapshot'];ck('Frozen recipe '+o['occurrence_id'],h(path.read_bytes())==o['source_file_sha256']);snapshots[str(path)]=bind(path)
 casebindings.append({'source_index':d['source_index'],'case_id':d['case_id'],'source_case_sha256':canon(original),'decision_sha256':canon(d),'occurrence_ids':d['occurrence_ids'],'proposal_ids':d['proposal_ids']})
evidence=[]
for e in es:
 c=e['capture'];path=(A if c['root']=='artifact' else Q)/c['path'];actual=h(path.read_bytes());ck('Evidence actual '+e['evidence_id'],actual==c['sha256']);evidence.append({'evidence_id':e['evidence_id'],'canonical_sha256':canon(e),'capture':c,'actual_capture_sha256':actual})
# Explicit filesystem traversal includes ignored files; only new S6 is excluded.
old=[bind(p) for p in sorted(A.rglob('*')) if p.is_file() and not p.is_relative_to(A/'successor-v6')];owners=[bind(p) for p in sorted((R/'data/ingredients').rglob('*.yaml'))];natives=[bind(p) for p in sorted((R/'reviews/structured').rglob('*')) if p.is_file()];triage=[bind(p) for p in sorted(T.rglob('*')) if p.is_file()]
for entry in old+owners+natives:gitchecks.append(git_equal(R/entry['path']))
ck('2956 maintained owners',len(owners)==2956)
manifest={'old_artifact_files':old,'old_s4_files':[p for p in old if p['path'].startswith(str((A/'successor-v4').relative_to(R))+'/')],'old_s5_files':[p for p in old if p['path'].startswith(str(S.relative_to(R))+'/')],'maintained_owner_files':owners,'existing_canonical_review_files':natives,'source_snapshot_files':list(snapshots.values()),'triage_context_files':triage}
dump(P/'preservation-baseline-v1.json',manifest);dump(P/'frozen/original-cases.json',shard);dump(P/'target-inventory-v1.json',target_inventory)
for name in ['TRIAGE-v2.json','AUTHOR-TASK-v2.md']:freeze(T/name,pathlib.Path('triage')/name)
# Bind authoritative S5 selection/handoff/native and historical S4 metadata corrections explicitly.
contexts=[]
for rel in ['successor-v5/HANDOFF.json','successor-v5/HANDOFF.md','successor-v5/SHA256SUMS','successor-v5/native/saved-pair.json','successor-v5/reviews/retention/final-assembly-metadata-review-v1.json','successor-v4/selection-v2.json','successor-v4/HANDOFF-v2.json','successor-v4/report-metadata-correction-v1.json']:
 path=A/rel;contexts.append(freeze(path,pathlib.Path('context')/rel))
dump(P/'commands-v1.json',{'commands':commands,'script':bind(pathlib.Path(__file__).resolve()),'PYTHONDONTWRITEBYTECODE':'1'})
receipt={'schema_version':1,'status':'PASS_BASELINE_FROZEN' if all(c['pass'] for c in checks) else 'FAIL_BASELINE_REQUIRES_REVIEW','reviewer':'Codex /root/buffers_research','scope':'Read-only published-S5 object/payload/source/preservation baseline for root-authored S6 correction. Retention and metadata only, no independent primary-science acceptance.','prior_involvement':'I authored the original four successor-v1 buffer/HCl proposals and later serum corrections, and performed broad retention/integration reviews. I did not author bio_research successor-v3 HCl/Difco corrections or this root successor-v6 candidate. This review does not claim historically uninvolved independence or renew any source/identity/owner science.','started_at':started,'completed_at':at(),'runtime_seconds':time.monotonic()-tick,'head':head,'selection':sbind,'authoritative_core':corebind,'proposal_count':len(ps),'case_count':len(ds),'occurrence_count':len(occ),'evidence_count':len(es),'target_proposal_ids':list(targets),'target_case_indices':case_union,'target_occurrence_count':len({o for x in target_inventory for o in x['occurrence_ids']}),'unaffected_payload_count':122,'unaffected_case_count':182,'payloads':payloads,'sentinels':sentinels,'case_bindings':casebindings,'evidence_object_bindings':evidence,'git_object_checks':gitchecks,'preservation_manifest':bind(P/'preservation-baseline-v1.json'),'preservation_counts':{k:len(v) for k,v in manifest.items()},'target_inventory':bind(P/'target-inventory-v1.json'),'context_bindings':contexts,'checks':checks,'allowed_successor_scope':'Four HCl assertions PARTIAL to UNKNOWN, retaining LABEL_ENUMERATION, known components and unknown basis/carrier/overlap. Difco LABEL_ENUMERATION to CURATED_INTERPRETATION and PARTIAL to COMPLETE only for the already expressly nominal2009 seven-immediate-input list; not historical lot or molecular composition. Necessary current assertion/report explanations and truthful appended history/dependencies only. No component, identity, quantity, alias, routing, raw source, old history, old review or hold rewrite.','approval':{'fresh_source_science':False,'whole_owner':False,'application':False,'role':False,'export':False,'future_published_head':False}}
dump(P/'baseline-v1.json',receipt)
print(json.dumps({'status':receipt['status'],'baseline':bind(P/'baseline-v1.json'),'counts':receipt['preservation_counts'],'checks':len(checks),'failures':[c for c in checks if not c['pass']]},indent=2))
