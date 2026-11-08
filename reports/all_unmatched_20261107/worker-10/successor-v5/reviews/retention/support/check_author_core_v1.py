#!/usr/bin/env python3
"""Independent exhaustive retention check of the root's bounded calf wording successor."""
import copy,datetime,hashlib,json,pathlib,shutil,subprocess,time,yaml
R=pathlib.Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v5';P=R/'.temp/all-unmatched-worker-10/successor-v5/retention';O=S/'reviews/retention'
Q=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
TARGET='sv1-bio-calf_blood_togo_m2854';EXPECTED='82fc29d837a223edb9c436445ec7ea13d2840c7b'
at=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();h=lambda b:hashlib.sha256(b).hexdigest();started=at();tick=time.monotonic();checks=[]
def rd(p):return json.loads(p.read_text())
def canon(j):return h(json.dumps(j,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode())
def dump(p,j):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
def bind(p):return {'path':str(p.relative_to(R)) if p.is_relative_to(R) else str(p),'sha256':h(p.read_bytes()),'bytes':p.stat().st_size}
def check(name,ok,detail=None):checks.append({'check':name,'pass':bool(ok),'detail':detail})
def diff(a,b,p=''):
 if type(a)!=type(b):return [{'pointer':p,'before':a,'after':b}]
 if isinstance(a,dict):return sum((diff(a.get(k),b.get(k),p+'/'+k) for k in sorted(set(a)|set(b))),[])
 if isinstance(a,list):return [] if a==b else [{'pointer':p,'before':a,'after':b}]
 return [] if a==b else [{'pointer':p,'before':a,'after':b}]
if (O/'author-core-retention-review-v1.json').exists():raise RuntimeError('Do not overwrite frozen independent review')
base=rd(P/'baseline-v1.json');nativebase=rd(P/'native-baseline-supplement-v1.json');pres=rd(P/'preservation-baseline-v1.json');frozen=rd(S/'author-freeze.json')
old={n:rd(P/'frozen/final-core'/f'{n}.json') for n in ['decisions','proposals','evidence']};new={n:rd(S/'author-core'/f'{n}.json') for n in old}
for n in old:check('Frozen candidate core '+n,h((S/'author-core'/f'{n}.json').read_bytes())==frozen['author_core'][n+'.json']['sha256'])
op={p['proposal_id']:p for p in old['proposals']['proposals']};np={p['proposal_id']:p for p in new['proposals']['proposals']};od={d['case_id']:d for d in old['decisions']['decisions']};nd={d['case_id']:d for d in new['decisions']['decisions']};oe={e['evidence_id']:e for e in old['evidence']['evidence']};ne={e['evidence_id']:e for e in new['evidence']['evidence']}
targetcid=op[TARGET]['case_ids'][0]
check('127 proposal IDs and order retained',[x['proposal_id'] for x in old['proposals']['proposals']]==[x['proposal_id'] for x in new['proposals']['proposals']] and len(np)==127)
check('188 case IDs and order retained',[x['case_id'] for x in old['decisions']['decisions']]==[x['case_id'] for x in new['decisions']['decisions']] and len(nd)==188)
check('304 original occurrence IDs retained',sum(len(d['occurrence_ids']) for d in nd.values())==304 and all(od[c]['occurrence_ids']==nd[c]['occurrence_ids'] for c in od))
check('All frozen source objects and proposal routing unchanged',all(all(od[c].get(k)==nd[c].get(k) for k in ['source','case_id','source_index','case_input_sha256','occurrence_ids','proposal_ids','owner_records','disposition','applicability','missing_requirement','no_change_reason']) for c in od))
check('126 nontarget proposal objects exact',sum(op[p]==np[p] for p in op if p!=TARGET)==126)
check('187 nontarget decisions exact',sum(od[c]==nd[c] for c in od if c!=targetcid)==187)
check('All1206 prior evidence objects exact',len(oe)==1206 and all(e in ne and oe[e]==ne[e] for e in oe))
added=sorted(set(ne)-set(oe));check('Exactly three scoped author evidence entries',added==sorted(['sv5-calf-source-assessment','sv5-calf-field-diff','sv5-calf-filed-finding']) and len(ne)==1209)
for e in added:check('New evidence scoped and native-kind '+e,ne[e]['case_ids']==[targetcid] and ne[e]['kind'] in ['source_snapshot','local_validation'] and ne[e]['url'] is None)
pd=diff(op[TARGET],np[TARGET]);dd=diff(od[targetcid],nd[targetcid]);allowedP={'/after_capture/path','/after_capture/sha256','/description','/evidence_ids','/independent_review/evidence_ids','/independent_review/status','/review_status_explanation','/wording_successor'};allowedD={'/completion_reassessment/bounded_scientific_conclusion','/evidence_ids','/independent_review/evidence_ids','/independent_review/status','/issue_refs','/reasoning','/wording_successor'}
check('Target proposal only allowlisted dependency/explanation deltas',set(x['pointer'] for x in pd)<=allowedP,[x['pointer'] for x in pd]);check('Target decision only allowlisted dependency/explanation deltas',set(x['pointer'] for x in dd)<=allowedD,[x['pointer'] for x in dd])
for name,before,after in [('proposal',op[TARGET],np[TARGET]),('decision',od[targetcid],nd[targetcid])]:
 check(name+' evidence additions only',after['evidence_ids'][:len(before['evidence_ids'])]==before['evidence_ids'] and sorted(after['evidence_ids'][len(before['evidence_ids']):])==added)
 check(name+' exact prior review preserved as history',after['wording_successor']['prior_independent_review']==before['independent_review'])
 check(name+' independent review reset pending',after['independent_review']=={'status':'pending','evidence_ids':[]})
 check(name+' no new identity/release authority',after['wording_successor']['identity_or_alias_change'] is False and after['wording_successor']['whole_owner_or_export_approval'] is False)
oldpath=A/op[TARGET]['after_capture']['path'];newpath=A/np[TARGET]['after_capture']['path'];yb=yaml.safe_load(oldpath.read_bytes());ya=yaml.safe_load(newpath.read_bytes());yd=diff(yb,ya)
check('Target old/new expected SHA',h(oldpath.read_bytes())=='62f0dc3300c488be2fb9d52f2c65e8e6826715d81177cf8e4ce48af422ed7338' and h(newpath.read_bytes())=='7a54c5bb03008949dec5ced0fbb8da9deee348fd4ad2473e66d41655db975b9d')
check('Payload only two notes plus appended history',set(x['pointer'] for x in yd)=={'/notes','/ontology_mapping/evidence','/curation_history'})
yb2=copy.deepcopy(yb);ya2=copy.deepcopy(ya)
for j in [yb2,ya2]:j.pop('notes');j.pop('curation_history');j['ontology_mapping']['evidence'][0].pop('notes')
check('All remaining payload fields exact',yb2==ya2)
check('Two original history events exact prefix',len(yb['curation_history'])==2 and len(ya['curation_history'])==3 and ya['curation_history'][:2]==yb['curation_history'])
check('New history truthful declared LLM correction',ya['curation_history'][2]['llm_assisted'] is True and ya['curation_history'][2]['curator']=='Codex worker10 /root' and ya['curation_history'][2]['previous_status']==ya['curation_history'][2]['new_status']=='MAPPED')
assessment=rd(S/'source-assessment.json');check('Same assessed wording in current fields',assessment['assessment']==np[TARGET]['description']==nd[targetcid]['reasoning']==nd[targetcid]['completion_reassessment']['bounded_scientific_conclusion'] and ya['notes'].startswith(assessment['assessment']) and ya['ontology_mapping']['evidence'][0]['notes'].startswith(assessment['assessment']))
check('Source evidence object and original retrieval exact',assessment['source']==oe['bio-primary-aff5f4b09e39e12c'])
check('Source copy exactly original capture',h((S/'inputs/source.json').read_bytes())==oe['bio-primary-aff5f4b09e39e12c']['capture']['sha256'])
payloadchecks=[]
for pid,p in np.items():
 path=A/p['after_capture']['path'];actual=h(path.read_bytes());same=actual==p['after_capture']['sha256'];check('Selected payload '+pid,same)
 if pid!=TARGET:check('Unaffected selected payload '+pid,actual==op[pid]['after_capture']['sha256'])
 payloadchecks.append({'proposal_id':pid,'capture':p['after_capture'],'actual_sha256':actual,'unchanged':pid!=TARGET and actual==op[pid]['after_capture']['sha256']})
capturechecks=[];cache={}
for eid,e in ne.items():
 c=e['capture'];path=(A if c['root']=='artifact' else Q)/c['path'];cache.setdefault(str(path),h(path.read_bytes()));actual=cache[str(path)];check('Evidence capture '+eid,actual==c['sha256']);capturechecks.append({'evidence_id':eid,'capture':c,'actual_sha256':actual})
preservation=[]
for category,items in pres.items():
 for item in items:
  path=pathlib.Path(item['path']);path=path if path.is_absolute() else R/path;exists=path.is_file();actual=h(path.read_bytes()) if exists else None;ok=actual==item['sha256'];check('Preservation '+category+':'+item['path'],ok);preservation.append({'category':category,'path':item['path'],'expected_sha256':item['sha256'],'actual_sha256':actual,'pass':ok})
for item in nativebase['tracked_canonical_review_files']:
 path=R/item['path'];actual=h(path.read_bytes());check('Canonical native preservation '+item['path'],actual==item['sha256'])
head=subprocess.check_output(['git','rev-parse','HEAD']).decode().strip();status=subprocess.check_output(['git','status','--porcelain=v1','--untracked-files=no']).decode();check('Published predecessor HEAD retained',head==EXPECTED);check('No tracked changes at author stage',not status,status)
frozenchecks=[]
for key in ['payload','proof','source_assessment']:
 c=frozen[key];path=A/c['path'];ok=h(path.read_bytes())==c['sha256'];check('Author freeze binding '+key,ok);frozenchecks.append({'key':key,'binding':c,'pass':ok})
failures=[c for c in checks if not c['pass']]
O.mkdir(parents=True,exist_ok=True)
dump(P/'author-core-checks-v1.json',{'started_at':started,'completed_at':at(),'runtime_seconds':time.monotonic()-tick,'checks':checks,'proposal_delta':pd,'decision_delta':dd,'payload_delta':yd,'payload_checks':payloadchecks,'evidence_capture_checks':capturechecks,'preservation_checks':preservation,'author_freeze_checks':frozenchecks})
support=[]
for path in [P/'baseline-v1.json',P/'preservation-baseline-v1.json',P/'native-baseline-supplement-v1.json',P/'commands-v1.json',P/'freeze_baseline_v1.py',P/'freeze_native_context_v1.py',P/'check_author_core_v1.py',P/'author-core-checks-v1.json']:
 dest=O/'support'/path.name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(path,dest);support.append({'original':bind(path),'copy':bind(dest),'byte_equal':path.read_bytes()==dest.read_bytes()})
report={'schema_version':1,'verdict':'pass_with_limitations' if not failures else 'findings_open','findings':failures,'reviewer':'Codex /root/buffers_research','independence':'Independent of root-authored successor-v5 calf wording payload and original bio calf-blood payload. Previously authored serum corrections, buffer proposals and chemical work and reviewed broad integration metadata; this retention review does not renew scientific approval of those unchanged bytes. Target source science/exact target review belongs to preparation_skeptic.','scope':'Exhaustive selection, case/proposal/evidence object retention and exact allowed deltas against an independently frozen publishedS4 baseline. No corpus changes or external writes.','started_at':started,'completed_at':at(),'runtime_seconds':time.monotonic()-tick,'predecessor_head':head,'input_bindings':{'author_freeze':bind(S/'author-freeze.json'),'core':{n:bind(S/'author-core'/f'{n}.json') for n in old},'payload':bind(newpath),'source_assessment':bind(S/'source-assessment.json'),'proof':bind(S/'payload-change-proof.json')},'counts':{'selected_proposals':127,'cases':188,'occurrences':304,'unchanged_other_proposal_objects':126,'unchanged_other_payloads':126,'unchanged_other_decisions':187,'unchanged_original_evidence_objects':1206,'new_scoped_author_evidence_objects':3,'current_evidence_capture_checks':len(capturechecks),'old_A_files':len(pres['old_artifact_files']),'old_S4_files':len(pres['old_s4_files']),'maintained_owners':len(pres['maintained_owner_files']),'existing_canonical_review_files':len(nativebase['tracked_canonical_review_files']),'checks':len(checks)},'allowed_delta_assessment':'Only current payload notes and mapping-evidence notes change, with one appended correction event. Exact source label, identifier, mapping/predicate/provenance, all original history, nonresolving raw-label provenance, unknown processing/basis and holds remain. Proposal/case wording and dependent evidence/issue/review markers change only for calf44.','target_proposal_id':TARGET,'target_case_id':targetcid,'target_old_sha256':h(oldpath.read_bytes()),'target_new_sha256':h(newpath.read_bytes()),'sentinels':base['sentinels'],'delta_pointers':{'proposal':[x['pointer'] for x in pd],'decision':[x['pointer'] for x in dd],'payload':[x['pointer'] for x in yd]},'S4_context':'Historical finalization-binding older evidence hash is explained by immutable report-metadata-correction-v1/HANDOFF-v2; authoritative selection-v2/final-core govern. It is not a new successor-v5 defect.','support_copies':support,'limitations':['This is retention/dependency review, not independent primary science acceptance or a fresh whole-owner/ontology/role review.','Author core correctly keeps the changed target review pending; exact independent target science, final review evidence, native wrapper and authoritative final selection/handoff must be checked later.','No maintained application, export approval, downstream rebuild or GitHub mutation is performed.'],'approval':{'scientific_renewal_of_unchanged_payloads':False,'whole_owner':False,'role':False,'export':False,'application':False}}
dump(O/'author-core-retention-review-v1.json',report)
(O/'author-core-retention-review-v1.md').write_text('Independent retention review: **'+report['verdict']+'**.\n\nAll127proposal IDs,188cases and304occurrences are retained. The126other proposal objects/payloads,187other decisions and1206original evidence objects are exact. Only calf44 current explanatory notes/reasoning and required history/dependency metadata change. Three scoped evidence records are added.\n\nThe old2623artifact files,147S4files,2956maintained owners and2052canonical review files remain exact. Carbonate135788... and ISP4 are unchanged.\n\nReviewer: Codex /root/buffers_research, independent of the root-authored calf correction; earlier serum/buffer authorship is disclosed. This check renews no earlier scientific/role/export approval. Independent target science and final native/handoff checks remain required.\n')
print(json.dumps({'verdict':report['verdict'],'report':bind(O/'author-core-retention-review-v1.json'),'checks':len(checks),'failures':failures}))
