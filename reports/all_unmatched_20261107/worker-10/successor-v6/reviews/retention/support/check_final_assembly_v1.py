#!/usr/bin/env python3
"""Independent final S6 metadata/retention checker; no source science approval."""
import datetime,hashlib,importlib.util,json,pathlib,shutil,subprocess,time,yaml
R=pathlib.Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v6';P=R/'.temp/all-unmatched-worker-10/successor-v6/retention';O=S/'reviews/retention';Q=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
HEAD='3e190a0f6c5a978ca8ed7e3bc7b6a2d66935548b';C9='c9a96da71a1977014680e5a92e600dfc7e3874db';RID='20261108T085159Z-w10-qualified-component-assertions-successor';REPORT=O/'final-assembly-metadata-review-v1.json'
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();h=lambda b:hashlib.sha256(b).hexdigest();start=now();tick=time.monotonic();checks=[];commands=[]
def rd(p):return json.loads(p.read_text())
def canon(x):return h(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode())
def bind(p):return {'path':str(p.relative_to(R)) if p.is_relative_to(R) else str(p),'sha256':h(p.read_bytes()),'bytes':p.stat().st_size}
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def ck(n,ok,detail=None):checks.append({'check':n,'pass':bool(ok),'detail':detail})
def resolve(c):
 p=pathlib.Path(c['path'])
 if p.is_absolute():return p
 if c.get('root')=='artifact' or str(p).startswith('successor-'):return A/p
 if c.get('root')=='source':return Q/p
 return R/p

def bindings(j,tag):
 if isinstance(j,dict):
  if isinstance(j.get('path'),str) and isinstance(j.get('sha256'),str):
   p=resolve(j);ck('Actual binding '+tag+':'+j['path'],p.is_file() and h(p.read_bytes())==j['sha256'])
  for k,v in j.items():bindings(v,tag+'/'+k)
 elif isinstance(j,list):
  for i,v in enumerate(j):bindings(v,tag+'/'+str(i))
def run(argv):
 t=now();t0=time.monotonic();r=subprocess.run(argv,capture_output=True);commands.append({'argv':argv,'started_at':t,'finished_at':now(),'runtime_seconds':time.monotonic()-t0,'exit_code':r.returncode,'stdout_sha256':h(r.stdout),'stderr':r.stderr.decode(errors='replace')});ck('Command '+str(argv),r.returncode==0);return r.stdout

def diff(a,b,p=''):
 if type(a)!=type(b):return [{'pointer':p,'before':a,'after':b}]
 if isinstance(a,dict):return sum((diff(a.get(k),b.get(k),p+'/'+k) for k in sorted(set(a)|set(b))),[])
 if isinstance(a,list):return [] if a==b else [{'pointer':p,'before':a,'after':b}]
 return [] if a==b else [{'pointer':p,'before':a,'after':b}]
if REPORT.exists():raise RuntimeError('Frozen report exists; do not overwrite')
# Caller waits for the root handoff/check readiness message before this final run.
for n in ['HANDOFF.json','HANDOFF.md','native-check-command.json','native-check.stdout']:
 if not (S/n).is_file():raise RuntimeError('Final root assembly incomplete: '+n)
base=rd(P/'baseline-v1.json');pres=rd(P/'preservation-baseline-v1.json');inv=rd(P/'target-inventory-v1.json');tids={p['proposal_id'] for p in inv};tcids={c for p in inv for c in p['case_ids']};tindices=sorted({i for p in inv for i in p['case_indices']});freeze=rd(S/'author-freeze.json');authorreview=rd(O/'author-core-retention-review-v1.json')
ck('Frozen author review unchanged',h((O/'author-core-retention-review-v1.json').read_bytes())=='ab6aa8a6aedc1041fee54575c9e7ee29b55ae0f5442e28723b2547ff283c9d6e')
cores={label:{n:rd(folder/f'{n}.json') for n in ['decisions','proposals','evidence']} for label,folder in [('s5',P/'frozen/final-core'),('author',S/'author-core'),('final',S/'final-core')]}
for n in cores['author']:ck('Original author freeze core '+n,h((S/'author-core'/f'{n}.json').read_bytes())==freeze['author_core'][n+'.json']['sha256'])
c9selbytes=run(['git','show',C9+':'+str(A.relative_to(R))+'/successor-v3/selection.json']);c9sel=json.loads(c9selbytes);p=P/'final-c9-baseline/selection.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(c9selbytes);gitcopies=[bind(p)];cores['c9']={}
for n in cores['author']:
 b=run(['git','show',C9+':'+str(A.relative_to(R))+'/successor-v3/'+n+'.json']);ck('c9 authoritative '+n,h(b)==c9sel['authoritative_core'][n+'.json']);p=P/'final-c9-baseline'/f'{n}.json';p.write_bytes(b);gitcopies.append(bind(p));cores['c9'][n]=json.loads(b)
idx={label:{n:{x[{'decisions':'case_id','proposals':'proposal_id','evidence':'evidence_id'}[n]]:x for x in core[n][n]} for n in core} for label,core in cores.items()};op=idx['s5']['proposals'];np=idx['final']['proposals'];od=idx['s5']['decisions'];nd=idx['final']['decisions'];ne=idx['final']['evidence']
ck('127 proposal IDs/order exact',list(op)==list(np) and len(np)==127);ck('188 case IDs/order exact',list(od)==list(nd) and len(nd)==188);occ=[o for d in nd.values() for o in d['occurrence_ids']];ck('304 unique occurrences retained',len(occ)==len(set(occ))==304 and all(od[c]['occurrence_ids']==nd[c]['occurrence_ids'] for c in nd))
ck('122 unaffected whole proposals exact',sum(op[p]==np[p] for p in op if p not in tids)==122);ck('182 unaffected whole decisions exact',sum(od[c]==nd[c] for c in od if c not in tcids)==182)
newids=['sv6-independent-assertions','sv6-independent-retention','sv6-native-narrow-validation'];ck('1218 evidence with only three final additions',len(ne)==1218 and set(ne)-set(idx['author']['evidence'])==set(newids))
for eid,e in idx['author']['evidence'].items():ck('Author evidence exact '+eid,e==ne[eid])
for eid,e in idx['s5']['evidence'].items():ck('Original evidence exact '+eid,e==ne[eid])
for eid in newids:ck('Final evidence case scope/kind '+eid,set(ne[eid]['case_ids'])==tcids and ne[eid]['url'] is None and ne[eid]['kind']==('local_validation' if eid==newids[-1] else 'independent_review'))
allowed={'/component_assertion_successor/independent_review_bindings','/component_assertion_successor/review_state','/evidence_ids','/independent_review/evidence_ids','/independent_review/status'};deltas={}
for n,targets in [('proposals',tids),('decisions',tcids)]:
 deltas[n]={};ck('Root metadata exact '+n,{k:v for k,v in cores['author'][n].items() if k!=n}=={k:v for k,v in cores['final'][n].items() if k!=n})
 for key,b in idx['final'][n].items():
  a=idx['author'][n][key]
  if key not in targets:ck('Final unaffected '+n+':'+key,a==b);continue
  ds=diff(a,b);deltas[n][key]=ds;ck('Only reviewed pointer/status finalization '+n+':'+key,{x['pointer'] for x in ds}<=allowed|({'/review_status_explanation'} if n=='proposals' else set()))
  ck('Exact final evidence append '+n+':'+key,b['evidence_ids']==a['evidence_ids']+newids)
  ck('Exact scoped complete review '+n+':'+key,b['independent_review']=={'status':'complete','evidence_ids':newids[:2]} and b['component_assertion_successor']['review_state']=='complete_for_exact_qualified_source_assertion_correction')
  ck('No whole-owner/scope change '+n+':'+key,b['component_assertion_successor']['whole_owner_or_export_approval'] is False and b['component_assertion_successor']['source_case_association_changed'] is False)
  bindings(b['component_assertion_successor']['independent_review_bindings'],n+key)
# Actual selected bytes and all evidence captures.
payloadchecks=[]
for pid,p in np.items():
 actual=h(resolve(p['after_capture']).read_bytes());ck('Selected actual '+pid,actual==p['after_capture']['sha256']);ck('Same reviewed payload '+pid,p['after_capture']==idx['author']['proposals'][pid]['after_capture']);payloadchecks.append({'proposal_id':pid,'capture':p['after_capture'],'actual_sha256':actual,'same_as_s5':actual==op[pid]['after_capture']['sha256']})
ck('Exactly five payload changes from S5',{r['proposal_id'] for r in payloadchecks if not r['same_as_s5']}==tids)
for sent in base['sentinels']:ck('Retained sentinel '+sent['proposal_id'],np[sent['proposal_id']]==op[sent['proposal_id']] and np[sent['proposal_id']]['after_capture']==sent['after_capture'])
captures=[]
for eid,e in ne.items():
 actual=h(resolve(e['capture']).read_bytes());ck('Evidence actual '+eid,actual==e['capture']['sha256']);captures.append({'evidence_id':eid,'capture':e['capture'],'actual_sha256':actual})
# Every 315-member bridge derived independently from complete selected source objects.
bridgechecks=[];bridges=[];priorchanges={'sv1-buffers-carbonate_co2_nominal4percent_togo_m202','sv1-bio-calf_blood_togo_m2854'}
sourcekeys=['source','source_index','case_id','case_input_sha256','occurrence_ids','owner_records','proposal_ids','disposition','applicability','publication_approval','existing_holds_preserved']
for name,label in [('complete-bridge.json','s5'),('combined-c9-bridge.json','c9')]:
 bridge=rd(S/name);bp=idx[label]['proposals'];bd=idx[label]['decisions'];ck(name+' exhaustive unique 315 membership',len(bridge['all_cases'])==len({r['case_id'] for r in bridge['all_cases']})==188 and len(bridge['all_proposals'])==len({r['proposal_id'] for r in bridge['all_proposals']})==127 and {r['case_id'] for r in bridge['all_cases']}==set(nd) and {r['proposal_id'] for r in bridge['all_proposals']}==set(np));changedcases=[];changedprops=[];changedbytes=[]
 for row in bridge['all_cases']:
  key=row['case_id'];a=bd[key];b=nd[key];expected={'source_index':b['source_index'],'case_id':key,'before_object_sha256':canon(a),'after_object_sha256':canon(b),'complete_object_exact':a==b,'source_identity_occurrence_owner_hashes_exact':all(a.get(k)==b.get(k) for k in sourcekeys),'reasoning_exact':a['reasoning']==b['reasoning'],'occurrence_ids':b['occurrence_ids'],'proposal_ids':b['proposal_ids']};ck(name+' case exact '+key,row==expected);ck(name+' source/scope unchanged '+key,expected['source_identity_occurrence_owner_hashes_exact']);bridgechecks.append({'bridge':name,'kind':'case','key':key,'independently_derived':expected,'actual_matches':row==expected})
  if a!=b:changedcases.append(b['source_index'])
 for row in bridge['all_proposals']:
  key=row['proposal_id'];a=bp[key];b=np[key];ab=resolve(a['after_capture']).read_bytes();bb=resolve(b['after_capture']).read_bytes();ck(name+' actual historical payload '+key,h(ab)==a['after_capture']['sha256']);expected={'proposal_id':key,'before_proposal_sha256':canon(a),'after_proposal_sha256':canon(b),'proposal_object_exact':a==b,'old_capture':a['after_capture'],'selected_capture':b['after_capture'],'payload_byte_exact':ab==bb,'owner_path':b['owner_path'],'before_owner_sha256':b['before_sha256'],'case_ids':b['case_ids'],'whole_owner_approval':False};ck(name+' proposal exact '+key,row==expected);ck(name+' owner preimage/cases retained '+key,all(a.get(k)==b.get(k) for k in ['owner_path','destination_path','before_sha256','case_ids','kind']));bridgechecks.append({'bridge':name,'kind':'proposal','key':key,'independently_derived':expected,'actual_matches':row==expected})
  if a!=b:changedprops.append(key)
  if ab!=bb:changedbytes.append(key)
 expectedcases=tindices if label=='s5' else sorted(tindices+[21,44,187]);expectedprops=tids if label=='s5' else tids|priorchanges;ck(name+' changed case set',sorted(changedcases)==expectedcases);ck(name+' changed proposal set',set(changedprops)==expectedprops);ck(name+' changed payload set',set(changedbytes)==expectedprops);bridges.append({'binding':bind(S/name),'member_count':315,'changed_case_indices':sorted(changedcases),'changed_proposal_ids':changedprops,'changed_payload_ids':changedbytes})
sel=rd(S/'selection.json');hand=rd(S/'HANDOFF.json');fin=rd(S/'finalization-binding.json');pair=rd(S/'native/saved-pair.json');metadata=['selection.json','complete-bridge.json','combined-c9-bridge.json','finalization-binding.json','HANDOFF.json','native/saved-pair.json','subagent-scopes.json','issue-linked-correction.json']
for n in cores['final']:ck('Selection/finalization authoritative core '+n,resolve(sel['authoritative_core'][n+'.json'])==S/'final-core'/f'{n}.json' and fin['final_core'][n+'.json']==sel['authoritative_core'][n+'.json'])
ck('127 exact selected rows',len(sel['selected_payloads'])==127 and {r['proposal_id'] for r in sel['selected_payloads']}==set(np) and all(row=={k:p.get(k,p['owner_path'] if k=='destination_path' else None) for k in row} for row in sel['selected_payloads'] for p in [np[row['proposal_id']]]))
for name in metadata:bindings(rd(S/name),name)
ck('Exact root-frozen handoff bytes',h((S/'HANDOFF.json').read_bytes())=='c8e087b45b6123b364fb6c63a90d7770a19d62e9e166ad12142ada16c2a2208e' and h((S/'HANDOFF.md').read_bytes())=='b2ef1362ee6a0c04c4b36df4be21c8f89ead5fb4c91096dbc6c083286253ebac')
ck('Five qualified selection scopes',len(sel['qualified_component_assertion_successor'])==5 and all(x['after_capture']==np[x['proposal_id']]['after_capture'] and x['scope']==np[x['proposal_id']]['component_assertion_successor']['active_assertion_scope'] for x in sel['qualified_component_assertion_successor']))
expectedcounts={'cases':188,'unique_occurrences':304,'proposal_ids':127,'changed_payloads_since_s5':5,'byte_identical_other_payloads_since_s5':122,'affected_case_indices':tindices,'unchanged_complete_case_objects_since_s5':182,'affected_cm_occurrences':12,'source_outcomes_changed':0,'changed_payloads_since_c9':7,'unchanged_complete_case_objects_since_c9':179,'prior_evidence_objects_exact':1212,'evidence_objects':1218,'current_retirements':0};ck('Exact handoff accounting',hand['accounting']==rd(S/'accounting.json')==expectedcounts);ck('Final no blanket application approval',sel['approval'] is False and hand['maintained_application_or_export_approval'] is False and pair['owner_role_export_approval'] is False)
# Canonical native actual eleven-target pair and exact renderer parity.
yp=R/'reviews/structured'/RID/'review.yaml';mp=yp.with_suffix('.md');native=yaml.safe_load(yp.read_text());markdown=mp.read_text();bindings(native['source']['inputs'],'native input');ck('Native input/final object parity',native==yaml.safe_load((S/'native/review-input.yaml').read_text()));ck('Handoff saved pair equality',hand['native_review']==pair)
spec=importlib.util.spec_from_file_location('record_review',R/'scripts/record_review.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);ck('Exact canonical renderer parity',mod.render_markdown(native)==markdown);ck('Embedded full YAML parity',yaml.safe_load(markdown.split('```yaml\n',1)[1].rsplit('```',1)[0])==native)
for e in native['evidence']:ck('Native evidence '+e['evidence_id'],h((R/e['reference']).read_bytes())==e['snapshot_sha256'])
expectedtargets={'PROPOSAL:'+p for p in tids}|tcids;ck('Exactly11 declared native targets',native['scope']['population_size']==11 and set(native['scope']['reviewed_target_ids'])==expectedtargets and {x['target_id'] for x in native['targets']}==expectedtargets and len(native['targets'])==11)
for target in native['targets']:
 tid=target['target_id']
 if tid.startswith('PROPOSAL:'):ck('Native exact proposal target '+tid,target['path']==str(resolve(np[tid.removeprefix('PROPOSAL:')]['after_capture']).relative_to(R)) and target['kind']=='source')
 else:ck('Native exact case target '+tid,target['path']==str((S/'final-core/decisions.json').relative_to(R)) and target['selector']=='$.decisions['+str(nd[tid]['source_index'])+']' and cores['final']['decisions']['decisions'][nd[tid]['source_index']]['case_id']==tid)
ck('Native limited review and attribution',native['reviewer']['independence']=='self_review' and 'original four S1 HCl proposals' in native['reviewer']['independence_basis'] and 'not independent HCl science' in native['reviewer']['independence_basis'] and native['verdict']=='pass_with_limitations' and native['completion']=='completed' and native['findings']==[] and native['actions']==[])
ck('Native recorded milestone timing/base',native['source']['git_revision']==HEAD and native['source']['state']=='working_tree' and native['started_at']==rd(S/'preflight.json')['at'].replace('+00:00','Z') and 'Exact earlier reading start is unknown' in ' '.join(native['limitations']))
ck('Native bounded scope safeguards',native['scientific_review'] is True and 'nominal2009 seven immediate ingredient-name list' in ' '.join(native['limitations']) and 'Historical HCl completion reassessments' in ' '.join(native['limitations']) and 'not blanket-transferred' in ' '.join(native['limitations']))
# Validation receipt inspection only; no broad native/schema reruns here.
val=rd(S/'validation/narrow-native.json');struct=rd(S/'structural-audit.json');nc=rd(S/'native-check-command.json');nout=rd(S/'native-check.stdout');ck('Native narrow completed exact input scope',val['status']=='PASS' and all(r['after']==np[r['proposal_id']]['after_capture'] and r['closed_schema_errors']==[] and r['guarded_roundtrip_byte_exact'] for r in val['changed_payloads']) and {r['proposal_id'] for r in val['changed_payloads']}==tids and all(x['records']==3037 and x['violations']==[] for x in val['partonomy'].values()))
ck('Structural exact complete cohort',struct['structural_accounting']=='PASS' and struct['accounted_case_count']==188 and struct['proposal_count']==127 and struct['evidence_count']==1218 and struct['scientific_adequacy_or_approval_established'] is False)
ck('Full native successful declared-scope receipt',nc['exit_code']==0 and nout==hand['native_complete_review_check']=={'repository':'CultureBotAI/MediaIngredientMech','valid_reviews':1028,'coverage':'declared_scopes_only'});ck('Native stderr deprecation only',(S/'native-check.stderr').read_text().strip()=='topClass is deprecated - use top_class')
# Complete preservation and the two prior seal manifests.
preservation=[]
for category,items in pres.items():
 for item in items:
  path=pathlib.Path(item['path']);path=path if path.is_absolute() else R/path;actual=h(path.read_bytes()) if path.is_file() else None;ck('Preserved '+category+':'+item['path'],actual==item['sha256']);preservation.append({'category':category,'path':item['path'],'expected_sha256':item['sha256'],'actual_sha256':actual})
seals=[]
for version in ['successor-v4','successor-v5']:
 manifest=A/version/'SHA256SUMS';members=[]
 for line in manifest.read_text().splitlines():
  sha,path=line.split('  ',1);actual=h((R/path).read_bytes());ck('Prior seal '+version+':'+path,actual==sha);members.append({'path':path,'expected_sha256':sha,'actual_sha256':actual})
 seals.append({'version':version,'manifest':bind(manifest),'member_count':len(members),'members':members})
head=run(['git','rev-parse','HEAD']).decode().strip();rawstatus=run(['git','status','--porcelain=v1','--untracked-files=all']).decode();rows=[{'status':s[:2],'path':s[3:]} for s in rawstatus.splitlines()];ck('Published predecessor head exact',head==HEAD);ck('Only new permitted report/native changes',all(r['status'] in ['??','A '] and (r['path'].startswith(str(S.relative_to(R))+'/') or r['path'].startswith('reviews/structured/'+RID+'/')) for r in rows),rows)
manual=[{'topic':'Finalization scope','assessment':'All five payloads equal the author-reviewed bytes. Only exact scoped reviewer/validation pointers and status finalize in five proposal/six case objects; original interpretations and prior historical markers are unchanged. Both bridges are checked row by row from complete objects, including seven cumulative changed payloads and nine changed case objects from c9.'},{'topic':'HCl authorship and science separation','assessment':'Native wrapper explicitly declares root self-review author/assembler and this reviewer’s original four S1 HCl authorship. My scope remains retention/metadata, not independent HCl science. The separate skeptic discloses its prior review involvement and owns only the new claim-specific source assessment.'},{'topic':'Qualified Difco interpretation and preserved holds','assessment':'Complete native/handoff texts retain COMPLETE only for the nominal2009 seven immediate ingredient-name list, under CURATED_INTERPRETATION. Actual historical JCM lot, performance adjustment, component amounts, molecular composition, owner partition and role/export remain unapproved. Four HCl UNKNOWN assertions retain percentage/carrier/overlap limits. Original historical PARTIAL reassessments remain explicitly historical.'},{'topic':'Prior correction and publication attribution','assessment':'Carbonate and calf corrections, ISP4, original findings and prior S4/S5 seals retain exact bytes/scopes. Earlier W09/c9 review is not inherited as blanket approval. Native timing separates recorded preflight milestone from unknown earlier reading start; local read timestamps preserve original retrieval times. Final handoff requires later publication receipt; no future head is claimed reviewed.'}]
failures=[x for x in checks if not x['pass']];private=P/'final-assembly-checks-v1.json';dump(private,{'script_started_at':start,'script_completed_at':now(),'runtime_seconds':time.monotonic()-tick,'checks':checks,'commands':commands,'author_to_final_deltas':deltas,'bridge_member_checks':bridgechecks,'bridge_summary':bridges,'payload_checks':payloadchecks,'evidence_capture_checks':captures,'preservation_checks':preservation,'prior_seal_checks':seals,'c9_git_baseline_copies':gitcopies,'observed_git_status':rows})
if failures:
 print(json.dumps({'status':'FAIL_REQUIRES_REVIEW','findings':failures,'receipt':bind(private)},indent=2));raise SystemExit(1)
support=[]
for src in [pathlib.Path(__file__).resolve(),private]:
 dest=O/'support'/src.name
 if dest.exists():raise RuntimeError('Do not overwrite existing support '+str(dest))
 shutil.copyfile(src,dest);support.append({'original':bind(src),'copy':bind(dest),'byte_exact':src.read_bytes()==dest.read_bytes()})
report={'schema_version':1,'verdict':'pass_with_limitations','findings':[],'reviewer':'Codex /root/buffers_research','scientific_review':False,'scope':'Independent final-core retention, all630 bridge memberships, selected/capture hashes, canonical11-target native pair, final handoff and prior sealed-artifact preservation. No new source science.','prior_involvement':base['prior_involvement'],'actual_reading_start_exact':None,'timing_note':'Final metadata reading preceded the checker; exact first reading time was not recorded. Script execution interval measures the mechanical audit only.','script_started_at':start,'script_completed_at':now(),'script_runtime_seconds':time.monotonic()-tick,'review_completed_at':now(),'head_observed':head,'counts':{**expectedcounts,'bridges':2,'members_per_bridge':315,'native_targets':11,'native_source_inputs':len(native['source']['inputs']),'native_evidence_entries':len(native['evidence']),**{k:len(v) for k,v in pres.items()},'checks':len(checks)},'input_bindings':[bind(S/x) for x in metadata+['HANDOFF.md','author-freeze.json','reviews/retention/author-core-retention-review-v1.json','reviews/skeptic/scientific-review-v1.json','validation/narrow-native.json','native-check-command.json','native-check.stdout','native-check.stderr','structural-audit.json']]+[bind(S/'final-core'/f'{n}.json') for n in cores['final']]+[bind(yp),bind(mp)],'bridge_summary':bridges,'author_to_final_delta_pointers':{n:{k:[d['pointer'] for d in v] for k,v in ds.items()} for n,ds in deltas.items()},'manual_metadata_assessment':manual,'prior_seals':[{'version':x['version'],'manifest':x['manifest'],'member_count':x['member_count']} for x in seals],'retained_sentinels':base['sentinels'],'support_copies':support,'validation_receipt_scope':'Read exact successful native narrow and full-review receipts; five guarded schema roundtrips and two3037-record partonomy overlays have no errors, full native check1028 declared scopes only. This review did not rerun broad tests.','limitations':['This is metadata/retention review. Original HCl authorship prevents claiming new independent HCl science; the separate skeptic provides claim-specific science.','Only present final artifacts at these exact hashes are bound. Final manifest, new commit, remote and future published-head acceptance remain root responsibilities.','No maintained application, owner/alias/role/export approval, source mutation, Git/GitHub mutation, paid or external session.'],'approval':{'fresh_science':False,'whole_owner':False,'role':False,'export':False,'application':False,'future_published_head':False}}
dump(REPORT,report)
REPORT.with_suffix('.md').write_text('Final assembly retention/metadata review: **pass_with_limitations**, no findings.\n\nAll127 proposals,188 cases and304 unique occurrences remain accounted for. Both315-member bridges match independently read full baseline objects. Since S5, five payloads/six case dependency objects change;122 other payloads/proposals and182 other complete decisions remain exact. Since c9, the bridge records seven bounded payload corrections and nine changed case objects.\n\nAll1218 evidence captures and127 selected payload hashes are exact. All2705 prior artifact files,2956 owners,2054 canonical reviews and244 recipe snapshots remain unchanged. Both prior S4/S5 seal manifests verify. The canonical11-target YAML and Markdown have exact renderer parity, actual source/evidence hashes and correct case selectors. The full native receipt passes with1028 declared-scope reviews.\n\nFinalization preserves the four HCl UNKNOWN and qualified nominal2009 Difco COMPLETE scopes, historical reassessments and all unresolved source/owner/role/export holds. Original HCl authorship is disclosed; this is metadata-only review, without scientific renewal or future-head acceptance. Root retains final sealing/publication/integration responsibility.\n')
print(json.dumps({'verdict':report['verdict'],'report':bind(REPORT),'checks':len(checks),'findings':[]},indent=2))
