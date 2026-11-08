#!/usr/bin/env python3
"""Retention-only S6 author audit; independence and original HCl authorship disclosed."""
import copy,datetime,difflib,hashlib,json,pathlib,shutil,subprocess,time,yaml
R=pathlib.Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v6';P=R/'.temp/all-unmatched-worker-10/successor-v6/retention';O=S/'reviews/retention';Q=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
HEAD='3e190a0f6c5a978ca8ed7e3bc7b6a2d66935548b';DIFCO='sv3-hm-difco-columbia1270';ISSUE='https://github.com/CultureBotAI/MediaIngredientMech/issues/1201#issuecomment-6719268125';REPORT=O/'author-core-retention-review-v1.json'
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();h=lambda b:hashlib.sha256(b).hexdigest();start=now();tick=time.monotonic();checks=[];commands=[]
def rd(p):return json.loads(p.read_text())
def canon(x):return h(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode())
def bind(p):return {'path':str(p.relative_to(R)) if p.is_relative_to(R) else str(p),'sha256':h(p.read_bytes()),'bytes':p.stat().st_size}
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def ck(n,ok,detail=None):checks.append({'check':n,'pass':bool(ok),'detail':detail})
def diff(a,b,p=''):
 if type(a)!=type(b):return [{'pointer':p,'before':a,'after':b}]
 if isinstance(a,dict):return sum((diff(a.get(k),b.get(k),p+'/'+k) for k in sorted(set(a)|set(b))),[])
 if isinstance(a,list):return [] if a==b else [{'pointer':p,'before':a,'after':b}]
 return [] if a==b else [{'pointer':p,'before':a,'after':b}]
def run(argv):
 t=now();t0=time.monotonic();r=subprocess.run(argv,capture_output=True);commands.append({'argv':argv,'started_at':t,'finished_at':now(),'runtime_seconds':time.monotonic()-t0,'exit_code':r.returncode,'stdout':r.stdout.decode(errors='replace'),'stderr':r.stderr.decode(errors='replace')});ck('Command '+str(argv),r.returncode==0);return r.stdout
if REPORT.exists():raise RuntimeError('Existing frozen report; do not overwrite')
base=rd(P/'baseline-v1.json');pres=rd(P/'preservation-baseline-v1.json');inventory=rd(P/'target-inventory-v1.json');targetids={p['proposal_id'] for p in inventory};targetcids={c for p in inventory for c in p['case_ids']};freeze=rd(S/'author-freeze.json');assessment=rd(S/'source-assessment.json');assess={r['proposal_id']:r for r in assessment['rows']};proof=rd(S/'payload-change-proof.json');proofrows={r['proposal_id']:r for r in proof['rows']};tri=rd(P/'frozen/triage/TRIAGE-v2.json');tr={r['proposal_id']:r for r in tri['rows']}
ck('Original private baseline exact',h((P/'baseline-v1.json').read_bytes())=='44c1bc99238a5afa4d93404f790c9d7ac0a92f5c1c08612de0cdb01963dd1cdc')
old={n:rd(P/'frozen/final-core'/f'{n}.json') for n in ['decisions','evidence','proposals']};new={n:rd(S/'author-core'/f'{n}.json') for n in old};idx={}
for name,core in [('old',old),('new',new)]:idx[name]={n:{v[{'decisions':'case_id','evidence':'evidence_id','proposals':'proposal_id'}[n]]:v for v in core[n][n]} for n in core}
op=idx['old']['proposals'];np=idx['new']['proposals'];od=idx['old']['decisions'];nd=idx['new']['decisions'];oe=idx['old']['evidence'];ne=idx['new']['evidence']
for n in new:
 ck('Exact author freeze '+n,h((S/'author-core'/f'{n}.json').read_bytes())==freeze['author_core'][n+'.json']['sha256'])
 ck('Root document metadata retained '+n,{k:v for k,v in old[n].items() if k!=n}=={k:v for k,v in new[n].items() if k!=n})
ck('Exact 127 proposal IDs/order',list(op)==list(np) and len(np)==127);ck('Exact188 case IDs/order',list(od)==list(nd) and len(nd)==188)
occ=[o for d in nd.values() for o in d['occurrence_ids']];ck('304 exact unique occurrences',len(occ)==len(set(occ))==304 and all(od[c]['occurrence_ids']==nd[c]['occurrence_ids'] for c in od))
ck('122 other complete proposals exact',sum(op[k]==np[k] for k in op if k not in targetids)==122);ck('182 other complete decisions exact',sum(od[k]==nd[k] for k in od if k not in targetcids)==182)
ck('No evidence removed',set(oe)<=set(ne));ck('1212 original evidence objects exact',len(oe)==1212 and all(oe[k]==ne[k] for k in oe))
newids=['sv6-source-assertion-assessment','sv6-exact-assertion-diffs','sv6-filed-qualified-findings'];ck('Only three scoped evidence additions',set(ne)-set(oe)==set(newids) and len(ne)==1215)
for eid in newids:
 e=ne[eid];ck('Native kind/six case scope '+eid,set(e['case_ids'])==targetcids and e['url'] is None and e['kind']==('source_snapshot' if eid==newids[-1] else 'local_validation'))
# Every payload actually read/hash checked; full YAML preservation and exact semantic changes.
payload_results=[];payload_deltas={};raw_diffs=[]
for pid,p in np.items():
 path=A/p['after_capture']['path'];b=path.read_bytes();ck('Selected payload actual '+pid,h(b)==p['after_capture']['sha256'])
 if pid not in targetids:
  ck('Unchanged payload '+pid,p['after_capture']==op[pid]['after_capture'] and h(b)==op[pid]['after_capture']['sha256']);continue
 oldpath=A/op[pid]['after_capture']['path'];a=oldpath.read_bytes();ya=yaml.safe_load(a);yb=yaml.safe_load(b);ds=diff(ya,yb);payload_deltas[pid]=ds
 allowed={'/component_assertion/completeness','/component_assertion/notes','/curation_history'}|({'/component_assertion/method'} if pid==DIFCO else set());ck('Only allowed payload fields '+pid,{x['pointer'] for x in ds}==allowed,[x['pointer'] for x in ds])
 expected=tr[pid]['recommendation'];ck('Qualified intended assertion '+pid,all(yb['component_assertion'][k]==v for k,v in expected.items()))
 aa=copy.deepcopy(ya);bb=copy.deepcopy(yb)
 for j in [aa,bb]:
  j['component_assertion'].pop('notes');j['component_assertion'].pop('completeness');j.pop('curation_history')
  if pid==DIFCO:j['component_assertion'].pop('method')
 ck('All other complete payload fields exact '+pid,aa==bb)
 ck('Whole original history exact prefix '+pid,len(yb['curation_history'])==len(ya['curation_history'])+1 and yb['curation_history'][:-1]==ya['curation_history'])
 hist=yb['curation_history'][-1];ck('Truthful attributed appended history '+pid,hist['curator']=='Codex worker10 /root' and hist['llm_assisted'] is True and hist['action']=='CORRECTED_SOURCE_RELATIVE_COMPONENT_ASSERTION' and hist['previous_status']==hist['new_status']=='MAPPED' and ISSUE in hist['changes'] and 'not human scientific review' in hist['changes'])
 ck('Original assertion evidence exact '+pid,yb['component_assertion']['evidence']==ya['component_assertion']['evidence'])
 text=assess[pid]['assessment'];ck('Exact active note scope '+pid,yb['component_assertion']['notes']==(text if pid==DIFCO else ya['component_assertion']['notes']+' '+text))
 ck('Source assessment matches frozen triage sources '+pid,assess[pid]['primary_bindings']==tr[pid]['primary_evidence'])
 pr=proofrows[pid];ck('Proof actual before/after '+pid,pr['before']==op[pid]['after_capture'] and pr['after']==p['after_capture'] and pr['before_assertion']==ya['component_assertion'] and pr['after_assertion']==yb['component_assertion'] and pr['appended_history']==hist)
 actual_fields=sorted(x['pointer'].strip('/').replace('/','.') for x in ds if x['pointer']!='/curation_history');ck('Proof exact changed field enumeration '+pid,sorted(pr['changed_existing_fields'])==actual_fields)
 raw=''.join(difflib.unified_diff(a.decode().splitlines(True),b.decode().splitlines(True),fromfile=op[pid]['after_capture']['path'],tofile=p['after_capture']['path']));dest=P/'actual-diffs'/f'{pid}.diff';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(raw);raw_diffs.append(bind(dest))
 payload_results.append({'proposal_id':pid,'before':op[pid]['after_capture'],'after':p['after_capture'],'allowed_existing_fields':actual_fields,'history_prefix_length':len(ya['curation_history']),'components_canonical_sha256':canon(yb['components']),'original_assertion_evidence_sha256':canon(yb['component_assertion']['evidence']),'original_other_fields_sha256':canon(aa),'selected_other_fields_sha256':canon(bb)})
# Case/proposal mutations must be narrow and keep historical judgments explicitly historical.
proposal_deltas={};decision_deltas={}
allowedP={'/after_capture/path','/after_capture/sha256','/component_assertion_successor','/description','/evidence_ids','/independent_review/evidence_ids','/independent_review/status','/publication_holds','/review_status_explanation'}
allowedD={'/component_assertion_successor','/evidence_ids','/independent_review/evidence_ids','/independent_review/status','/issue_refs'}
for pid in targetids:
 a=op[pid];b=np[pid];ds=diff(a,b);proposal_deltas[pid]=ds;ck('Allowed proposal metadata '+pid,{x['pointer'] for x in ds}<=allowedP,[x['pointer'] for x in ds])
 if pid==DIFCO:ck('Difco description/holds retained '+pid,a['description']==b['description'] and a['publication_holds']==b['publication_holds'])
 else:
  ck('Only active HCl description phrase replaced '+pid,b['description']==a['description'].replace('partial source-supported components','source-named components with unknown list completeness'))
  ck('Only closure enum in HCl publication hold replaced '+pid,b['publication_holds']==[x.replace('PARTIAL components','components with UNKNOWN completeness') for x in a['publication_holds']])
 marker=b['component_assertion_successor'];ck('Proposal exact prior review/payload lineage '+pid,marker['prior_independent_review']==a['independent_review'] and marker['previous_capture']==a['after_capture'] and marker['selected_capture']==b['after_capture'])
 ck('Proposal exact pending state '+pid,b['independent_review']=={'status':'pending','evidence_ids':[]} and marker['review_state']=='pending_exact_independent_review')
 ck('Proposal limited marker '+pid,marker['active_assertion_scope']==assess[pid]['assessment'] and marker['source_case_association_changed'] is False and marker['whole_owner_or_export_approval'] is False and marker['predecessor_head']==HEAD and marker['issue']==ISSUE)
 ck('Proposal evidence exact prefix '+pid,b['evidence_ids']==a['evidence_ids']+newids)
for cid in targetcids:
 a=od[cid];b=nd[cid];ds=diff(a,b);decision_deltas[cid]=ds;pid=next(p for p in b['proposal_ids'] if p in targetids);marker=b['component_assertion_successor'];ck('Allowed decision metadata '+str(b['source_index']),{x['pointer'] for x in ds}<=allowedD|({'/reasoning'} if b['source_index']==178 else set()),[x['pointer'] for x in ds])
 ck('Decision review/source marker '+str(b['source_index']),marker['prior_independent_review']==a['independent_review'] and marker['selected_capture']==np[pid]['after_capture'] and marker['previous_capture']==op[pid]['after_capture'] and marker['active_assertion_scope']==assess[pid]['assessment'] and marker['whole_owner_or_export_approval'] is False and marker['source_case_association_changed'] is False)
 ck('Decision pending exact '+str(b['source_index']),b['independent_review']=={'status':'pending','evidence_ids':[]} and marker['review_state']=='pending_exact_independent_review')
 ck('Decision evidence prefix/issue append '+str(b['source_index']),b['evidence_ids']==a['evidence_ids']+newids and b['issue_refs']==a['issue_refs']+[ISSUE])
 ck('Historical reassessment retained '+str(b['source_index']),b.get('completion_reassessment')==a.get('completion_reassessment'))
 if b['source_index']!=178:ck('Old HCl historical status preserved and clarified '+str(b['source_index']),a['successor_v3_reassessment']['old_completion_reassessment_is_historical'] is True and b['successor_v3_reassessment']==a['successor_v3_reassessment'] and 'Current completeness is UNKNOWN' in marker['historical_completion_reassessment_preserved'] and b['reasoning']==a['reasoning'])
 else:ck('Only specific Difco active reasoning sentence replaced',b['reasoning']==a['reasoning'].replace('Retain PARTIAL names-only components and no dry mass-ratio inference.','Use CURATED_INTERPRETATION with COMPLETE limited to the seven immediate names in the nominal 2009 manufacturer list; historical JCM lot, performance adjustments and quantitative ratios remain unverified. No dry mass-ratio inference.'))
# Original source case/routing fields and all other metadata have already been compared in whole-object allowlists.
for cid,b in nd.items():
 a=od[cid];ck('Source/owner/outcome identity exact '+cid,all(a.get(k)==b.get(k) for k in ['case_id','case_input_sha256','source','source_index','occurrence_ids','proposal_ids','owner_records','disposition','applicability','publication_approval','existing_holds_preserved','no_change_reason','missing_requirement']))
for s in base['sentinels']:ck('Explicit retained sentinel '+s['proposal_id'],op[s['proposal_id']]==np[s['proposal_id']] and h((A/s['after_capture']['path']).read_bytes())==s['after_capture']['sha256'])
# All evidence actual captures and original timestamp/scope objects; primary science itself is not reassessed.
captures=[]
for eid,e in ne.items():
 c=e['capture'];path=(A if c['root']=='artifact' else Q)/c['path'];actual=h(path.read_bytes());ck('Evidence bytes '+eid,actual==c['sha256']);captures.append({'evidence_id':eid,'capture':c,'actual_sha256':actual})
primary_metadata=[]
for body in assessment['primary_bodies']:
 sm=body['source_metadata'];eid=sm['evidence_id'];e=oe[eid];c=sm['original_capture'];actual=h((A/c['path']).read_bytes());ck('Source assessment original metadata '+eid,e['capture']==c and e['url']==sm['url'] and e['accessed_at']==sm['original_accessed_at'] and actual==body['sha256']==c['sha256']);primary_metadata.append({'evidence_id':eid,'original_accessed_at':e['accessed_at'],'url':e['url'],'capture':c,'actual_sha256':actual})
ck('13 primary bodies scope',len(primary_metadata)==len({x['evidence_id'] for x in primary_metadata})==13)
for c in [freeze['proof'],freeze['source_assessment']]+[p['capture'] for p in freeze['payloads']]:ck('Author freeze binding '+c['path'],h((A/c['path']).read_bytes())==c['sha256'])
# Inspect actual root validation receipts without rerunning broad science/native suites.
validation=rd(S/'validation/narrow-native.json');vc=rd(S/'validation/command.json');ck('Root native completed success receipt',vc['exit_code']==0 and validation['status']=='PASS' and validation['all_selected_payloads']==127 and validation['maintained_catalog_records']==2956 and validation['whole_owner_source_role_export_approval'] is False and all(x['records']==3037 and x['violations']==[] for x in validation['partonomy'].values()))
ck('Root native exact target set',{r['proposal_id'] for r in validation['changed_payloads']}==targetids)
for row in validation['changed_payloads']:ck('Native validation target exact '+row['proposal_id'],row['before']==op[row['proposal_id']]['after_capture'] and row['after']==np[row['proposal_id']]['after_capture'] and row['closed_schema_errors']==[] and row['guarded_roundtrip_byte_exact'] and row['history_prefix_components_mapping_projection_exact'])
# Fresh exhaustive preservation checks against independently frozen baseline; includes ignored files.
preserved=[]
for category,items in pres.items():
 for item in items:
  path=pathlib.Path(item['path']);path=path if path.is_absolute() else R/path;actual=h(path.read_bytes()) if path.is_file() else None;ck('Preservation '+category+':'+item['path'],actual==item['sha256']);preserved.append({'category':category,'path':item['path'],'expected_sha256':item['sha256'],'actual_sha256':actual})
head=run(['git','rev-parse','HEAD']).decode().strip();status=run(['git','status','--porcelain=v1','--untracked-files=no']).decode();ck('Published S5 head retained',head==HEAD);ck('Tracked tree unchanged at author stage',not status,status)
manual=[{'topic':'Four HCl current assertion scope','assessment':'The complete payload diff retains all component objects, assertion evidence and original fields except completeness/notes and appended history. Active proposal phrasing now states unknown list completeness; one closure-dependent publication-hold sentence is updated with identical substantive limits. Original percentages, basis/carrier/grade uncertainty, unresolved relations and receiving-dose conflicts remain unchanged.'},{'topic':'Difco qualified scope','assessment':'The exact new assertion says CURATED_INTERPRETATION and COMPLETE only for the already declared nominal2009 seven-immediate-name list. It expressly excludes molecular composition, historical JCM lot closure, quantitative recipe or dry-mass ratio inference; adjustment/supplementation and mixed-owner partition limits remain. No component or quantity was added. This is a metadata/allowed-delta conclusion, not this reviewer’s fresh scientific endorsement.'},{'topic':'Historical HCl reassessment','assessment':'All five HCl source cases already contain successor_v3_reassessment.old_completion_reassessment_is_historical=true at frozen S5. S6 preserves those entire reassessments and adds an explicit current UNKNOWN marker. Earlier PARTIAL text is historical; it is not the selected current ComponentAssertion completeness.'},{'topic':'Attribution and review reset','assessment':'Five proposals and six cases reset only the changed scope to pending exact review while preserving prior independent_review objects inside the new lineage marker. No earlier source/owner/role/export review is treated as acceptance of this correction.'}]
failures=[c for c in checks if not c['pass']]
private=P/'author-core-checks-v1.json';dump(private,{'script_started_at':start,'script_completed_at':now(),'script_runtime_seconds':time.monotonic()-tick,'commands':commands,'checks':checks,'proposal_deltas':proposal_deltas,'decision_deltas':decision_deltas,'payload_deltas':payload_deltas,'payload_results':payload_results,'actual_raw_diffs':raw_diffs,'evidence_capture_checks':captures,'primary_metadata_checks':primary_metadata,'preservation_checks':preserved})
if failures:
 print(json.dumps({'status':'FAIL_REQUIRES_REVIEW','failures':failures,'private_receipt':bind(private)},indent=2));raise SystemExit(1)
support=[]
for path in [P/'baseline-v1.json',P/'preservation-baseline-v1.json',P/'target-inventory-v1.json',P/'commands-v1.json',P/'freeze_baseline_v1.py',pathlib.Path(__file__).resolve(),private]:
 dest=O/'support'/path.name;dest.parent.mkdir(parents=True,exist_ok=True)
 if dest.exists():raise RuntimeError('Support destination already exists '+str(dest))
 shutil.copyfile(path,dest);support.append({'original':bind(path),'copy':bind(dest),'byte_exact':path.read_bytes()==dest.read_bytes()})
report={'schema_version':1,'verdict':'pass_with_limitations','findings':[],'reviewer':'Codex /root/buffers_research','scientific_review':False,'scope':'Exhaustive author-core/full-cohort retention, exact permitted field deltas, source-capture metadata preservation and narrow validation receipt inspection. No independent primary-science approval.','prior_involvement':base['prior_involvement'],'actual_reading_start_exact':None,'timing_note':'Payload/metadata reading preceded this mechanical checker; exact reading start was not recorded. Script timing measures only this audit execution.','script_started_at':start,'script_completed_at':now(),'script_runtime_seconds':time.monotonic()-tick,'review_completed_at':now(),'head_observed':head,'input_bindings':{'author_freeze':bind(S/'author-freeze.json'),'core':{n:bind(S/'author-core'/f'{n}.json') for n in new},'proof':bind(S/'payload-change-proof.json'),'source_assessment':bind(S/'source-assessment.json'),'validation':bind(S/'validation/narrow-native.json'),'validation_command':bind(S/'validation/command.json')},'counts':{'selected_proposals':127,'cases':188,'unique_occurrences':304,'target_payloads':5,'target_cases':6,'target_cm_occurrences':12,'unchanged_other_proposals_and_payloads':122,'unchanged_other_complete_decisions':182,'original_evidence_exact':1212,'new_scoped_evidence':3,'current_evidence_capture_checks':1215,'primary_capture_metadata_checks':13,**{k:len(v) for k,v in pres.items()},'checks':len(checks)},'exact_target_payloads':payload_results,'metadata_delta_pointers':{'proposals':{k:[x['pointer'] for x in v] for k,v in proposal_deltas.items()},'decisions':{k:[x['pointer'] for x in v] for k,v in decision_deltas.items()}},'manual_metadata_assessments':manual,'retained_sentinels':base['sentinels'],'validation_disposition':'Inspected completed native receipt for the five exact hashes: closed schema zero errors, guarded byte roundtrip exact; predecessor/successor3037-record overlays have no violations. Did not rerun broad tests or conduct new source science.','support_copies':support,'limitations':['The changed assertion science requires separate exact author-independent assessment; this reviewer authored the original four successor-v1 HCl proposals.','Author-core correctly leaves five proposal/six-case changed scopes pending. Final-core, native wrapper, handoff and publication metadata require a later exact binding review.','No maintained application, source/owner/role/export approval, future-head acceptance, Git or GitHub mutation.'],'approval':{'fresh_science':False,'whole_owner':False,'role':False,'export':False,'application':False,'future_published_head':False}}
dump(REPORT,report)
REPORT.with_suffix('.md').write_text('Independent author-core retention review: **pass_with_limitations**; no findings.\n\nAll 127 proposal IDs,188 cases and304 unique occurrences are retained. Five payloads and six source-case dependency sets change;122 other proposals/payloads,182 other complete decisions and1212 original evidence objects remain exact. Three scoped evidence objects are added.\n\nThe four HCl changes are limited to UNKNOWN completeness, necessary assertion explanation and history. Difco changes to CURATED_INTERPRETATION and COMPLETE only for the existing nominal2009 seven-input name list, retaining historical-lot, adjustment, quantity and partition limits. All component, identity, amount, alias and source objects remain exact. Historical HCl reassessments were already marked historical and remain unchanged.\n\nAll2705 prior artifact files,147 S4 files,82 S5 files,2956 owners,2054 canonical review files and244 recipe snapshots remain exact. Carbonate, calf and ISP4 sentinels are retained. Root native receipts bind the exact candidates; no broad suite was rerun.\n\nPrior original HCl/buffer/serum authorship is disclosed. This is retention and metadata review only; separate primary science and final native/handoff binding reviews remain required. No owner, role, export or future-head approval is conferred.\n')
print(json.dumps({'verdict':report['verdict'],'report':bind(REPORT),'checks':len(checks),'findings':[]},indent=2))
