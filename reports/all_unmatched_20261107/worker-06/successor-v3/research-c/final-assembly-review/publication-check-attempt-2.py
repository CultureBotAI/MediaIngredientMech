from pathlib import Path
import collections,datetime,hashlib,importlib.util,json,subprocess,sys,yaml
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-06';S=A/'successor-v3';F=A/'successor-v2/final';O=S/'research-c/final-assembly-review';N=R/'reviews/structured/20261108T064951Z-w06-successor-v3-reconciliation'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def obj(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=R).decode()
errors=[]
def ck(v,m):
 if not v:errors.append(m)
sel=read(S/'selection.json');delta=read(S/'delta.json');comp=read(S/'completion-receipt.json');hold=read(S/'remaining-holds.json');H=read(S/'source-holds.json');native=read(S/'native/review-content.json');previous=read(O/'review-final.json')
D=read(S/'decisions.json')['decisions'];P=read(S/'proposals.json')['proposals'];E=read(S/'evidence.json')['evidence'];pm={p['proposal_id']:p for p in P};em={e['evidence_id']:e for e in E};dm={d['case_id']:d for d in D};hm={h['case_id']:h for h in H['cases']}
inputs={n:sha(S/n) for n in ['selection.json','decisions.json','proposals.json','evidence.json','source-holds.json','delta.json','review-coverage.json','finding-dispositions.json','sealed-review-read-coverage.json','HANDOFF.md','completion-receipt.json','remaining-holds.json']}
for n,h in previous['input_hashes'].items():ck(sha(S/n)==h,'final integration input unchanged '+n)
for n,r in comp['authoritative_intake']['core'].items():ck(sha(R/r['path'])==r['sha256']==sel['core'][n]['sha256'],'completion core '+n)
ck(sha(S/'selection.json')==comp['authoritative_intake']['selection']['sha256'],'completion selector')
ck(inputs['HANDOFF.md']=='45191859042ac10642ca9153f2f3f74db1c09cf4cfa69035e2f4bcaaf399b7e5','handoff exact announced bytes')
ck(inputs['completion-receipt.json']=='76d61dc35d4a565bb059dea921aa752e65b76f10e9830d394ce37bc0c19ba792','completion exact announced bytes')
for n,h in comp['historical_and_current_core_hashes'].items():
 for field,p in [('original_d5',A/n),('previous_v2',F/n),('current_v3',S/n)]:ck(sha(p)==h[field],f'completion historical core {field} {n}')
for r in comp['independent_review_receipts']:ck(sha(R/r['path'])==r['sha256'],'completion review '+r['path'])
for p,h in comp['native_pair'].items():ck(sha(R/p)==h,'completion native pair '+p)
ck(sha(R/comp['native_check']['path'])==comp['native_check']['sha256'],'completion native command capture')
# Use the native read API to check authoritative YAML, rendered Markdown and retained Git provenance.
spec=importlib.util.spec_from_file_location('w06_record_review_publication',R/'scripts/record_review.py');mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
saved=mod.read_review(R,str((N/'review.yaml').relative_to(R)))
ck(saved==native,'saved native pair equals reviewed content')
source_verified=[]
for r in native['source']['inputs']:
 actual=sha(R/r['path']);ck(actual==r['sha256'],'native source input '+r['path']);source_verified.append({'path':r['path'],'sha256':actual,'role':r['role']})
expected_targets={x['proposal_id'] for x in delta['proposal_deltas']}|{x['case_id'] for x in delta['case_deltas']}
targets={t['target_id']:t for t in native['targets']}
ck(len(targets)==74 and set(targets)==expected_targets,'native74 exact changed target coverage')
ck(native['scope']['population_size']==74 and set(native['scope']['reviewed_target_ids'])==expected_targets and native['scope']['coverage']=='full','native full coverage only relative74')
for tid,t in targets.items():
 if tid in pm:ck(t['path']==str((A/pm[tid]['after_capture']['path']).relative_to(R)),'native selected proposal '+tid)
 else:ck(t['path']==str((A/'native-inputs/frozen-shard-06.json').relative_to(R)) and t['selector']==f'cases[case_id={tid}]','native frozen case selector '+tid)
ck(native['source']['git_revision']==comp['parent_published_head'] and native['source']['state']=='working_tree','native truthful working-tree base')
ck(native['reviewer']['independence']=='self_review' and 'C seven payloads and fourteen outcomes by root' in native['reviewer']['independence_basis'],'native authorship disclosure')
ck(native['verdict']=='pass_with_limitations' and not native['findings'],'native bounded verdict')
# Native external captures reuse the canonical ledger retrieval times, not assembly time.
nev={e['evidence_id']:e for e in native['evidence']}; reused=[];local=[]
for e in native['evidence']:
 if e['evidence_id'] in em:
  ce=em[e['evidence_id']];ck(e['snapshot_sha256']==ce['capture']['sha256'],'native captured bytes '+e['evidence_id']);
  if ce.get('accessed_at'):ck(e['accessed_at']==ce['accessed_at'],'native original retrieval time '+e['evidence_id']);reused.append(e['evidence_id'])
 if not e['reference'].startswith(('https://','http://')):
  ck(sha(R/e['reference'])==e['snapshot_sha256'],'native local evidence '+e['evidence_id']);local.append(e['evidence_id'])
 else:ck(e['evidence_id'] in em,'native external evidence canonical binding '+e['evidence_id'])
fd=read(S/'finding-dispositions.json');fm={f['finding_id']:f for f in fd['findings']};assessed=set()
ck(len(native['assessments'])==12 and {x['assessment_id'] for x in native['assessments']}==set(fm),'all12 finding assessments')
for x in native['assessments']:
 f=fm[x['assessment_id']];expected=set(f['case_ids'])|{p['proposal_id'] for p in f['final_proposal_bindings']};ck(set(x['target_ids'])==expected,'native assessment target scope '+x['assessment_id']);ck(set(x['evidence_ids'])<=set(nev),'native assessment evidence '+x['assessment_id']);assessed.update(x['target_ids'])
ck(assessed==expected_targets,'native all74 targets assessed')
# Final C independent science receipt is a distinct root review; this script performs binding checks only.
cb=read(S/'research-root/review-c/central-binding-addendum.json')
for n,h in cb['final_input_hashes'].items():ck(sha(S/n)==h,'C root final core '+n)
for r in cb['case_bindings']:ck(obj(D[r['case_index']])==r['final_object_sha256'] and D[r['case_index']]['case_id']==r['case_id'],'C root final case '+str(r['case_index']))
for pid,h in cb['final_payload_hashes'].items():ck(pm[pid]['after_capture']['sha256']==h and sha(A/pm[pid]['after_capture']['path'])==h,'C root final payload '+pid)
ck(len(cb['case_bindings'])==14 and len(cb['final_payload_hashes'])==7 and not cb['open_findings'],'C root14/7 scope and no open findings')
ck(sha(R/cb['scientific_basis']['path'])==cb['scientific_basis']['sha256'],'C root independent basis')
commands=[]
for n in ['inspect','validate','save','check']:
 p=S/'native'/f'{n}-command.json';x=read(p);ck(x['exit_code']==0,'native recorded command '+n);commands.append({'path':str(p.relative_to(R)),'sha256':sha(p),'exit_code':x['exit_code']})
checkcmd=read(S/'native/check-command.json');ck(checkcmd['command'][1:]==['scripts/record_review.py','check','--base',comp['parent_published_head'],'--require-reviews'],'native full check exact base/scope command')
checklog=(S/'native/check.log').read_text();j=json.JSONDecoder().raw_decode(checklog[checklog.index('{'):])[0];ck(j['valid_reviews']==1023 and j['coverage']=='declared_scopes_only','native full check1023 declared scopes')
# Compare every remaining-limit entry against its exact source outcome and immutable held state.
limits=hold['case_limits'];limit_indices=set()
for r in limits:
 i=r['case_index'];d=D[i];limit_indices.add(i)
 for k in ['case_id','disposition','missing_requirement','occurrence_ids','proposal_ids']:ck(r[k]==d[k],f'remaining limit {i} {k}')
 ck(r['raw_source_label']==d['source']['raw_source_label'],'remaining raw label '+str(i));ck(r['frozen_source_state']==hm[d['case_id']]['frozen_source_state'],'remaining frozen state '+str(i))
expected_limits={i for i,d in enumerate(D) if d['missing_requirement'] or hm[d['case_id']]['frozen_source_state'].get('downstream_holds')}
ck(len(limits)==131 and limit_indices==expected_limits,'complete131 remaining limits')
unresolved=[i for i,d in enumerate(D) if d['disposition']=='unresolved'];ck(len(unresolved)==29 and hold['unresolved_case_indices']==unresolved,'29 precise unresolved cases')
allholds=sum(len(h['frozen_source_state'].get('downstream_holds',[])) for h in H['cases']);listedholds=sum(len(r['frozen_source_state'].get('downstream_holds',[])) for r in limits)
ck(allholds==listedholds==88==hold['original_downstream_hold_count'],'88 exact downstream holds retained')
ck(hold['source_holds_sha256']==sha(S/'source-holds.json') and (S/'source-holds.json').read_bytes()==(F/'source-holds.json').read_bytes(),'unchanged held states bytes')
actual_counts={'cases':len(D),'CM_occurrence_ids':len({o for d in D for o in d['occurrence_ids']}),'original_downstream_holds':allholds,'proposals':len(P),'proposal_kinds':dict(collections.Counter(p['kind'] for p in P)),'evidence':len(E),'changed_payloads':len(sel['changed_payloads']),'changed_proposal_metadata':len(delta['proposal_deltas']),'changed_case_outcomes_or_review_metadata':len(delta['case_deltas'])}
ck(actual_counts==comp['counts'],'completion all current counts')
ck(comp['whole_owner_role_export_approval'] is False and comp['maintained_application'] is False and hold['whole_owner_role_export_approval'] is False,'completion and holds no inferred approval')
# Recheck both immutable published manifests and every member, including ignored files explicitly listed.
historical=[]
for head,rel in [('d5a7613c931d45d057eaca7b5ec15280aca76c9e',A/'SHA256SUMS'),('1b3641853c7105b9091f81b5a9b19c99e8ed351e',A/'successor-v2/SHA256SUMS')]:
 raw=subprocess.check_output(['git','show',head+':'+str(rel.relative_to(R))],cwd=R);ck(raw==rel.read_bytes(),'published manifest bytes '+head);count=0
 for line in raw.decode().splitlines():
  h,p=line.split('  ',1);ck(sha(R/p)==h,'published member '+p);count+=1
 historical.append({'head':head,'manifest':str(rel.relative_to(R)),'sha256':sha(rel),'members_verified':count,'ignored_files_included':True})
ck([r['members_verified'] for r in historical]==[1758,115],'historical member counts')
tracked=git('diff','--name-status','1b3641853c7105b9091f81b5a9b19c99e8ed351e','--').splitlines()
allowed_new=(str(S.relative_to(R))+'/',str(N.relative_to(R))+'/')
ck(all(line.startswith('A\t') and line.split('\t',1)[1].startswith(allowed_new) for line in tracked),'only permitted new successor/native files staged')
branch=git('branch','--show-current').strip();ck(branch==comp['branch'],'assigned branch')
for n,h in inputs.items():ck(sha(S/n)==h,'stable publication input '+n)
result={'review_id':'V3-C-PUBLICATION-METADATA-1','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'Codex /root/research_c','review_type':'Independent final metadata, native target/diff and publication claim-scope scrutiny','scientific_review':False,'author_overlap':'Reviewer authored seven Water-removal payloads and fourteen source corrections. This receipt does not independently approve that science; exact root independent review and central-binding addendum provide its separate scientific review.','scope':'Exact final native YAML/Markdown pair and content, all74 targets/237 source input hashes/205 evidence entries/12 assessments; final HANDOFF, completion and every131 remaining-limit row; stable final core and independent receipts; current native gate receipt; all1873 historical manifest members. Metadata and claim-scope review only.','status':'FAIL' if errors else 'PASS','open_findings':errors,'input_hashes':inputs,'native_pair':comp['native_pair'],'native_read_api':'scripts.record_review.read_review validated YAML, rendered Markdown and retained working-tree Git-base provenance; all current source input hashes additionally verified here.','native_scope':{'targets':len(targets),'proposal_entries':len(delta['proposal_deltas']),'affected_cases':len(delta['case_deltas']),'source_inputs':len(source_verified),'evidence_entries':len(nev),'canonical_reused_evidence_with_original_times':len(reused),'local_evidence_hashes':len(local),'assessment_groups':len(native['assessments']),'self_review_disclosure':native['reviewer'],'verdict':native['verdict']},'native_source_input_bindings':source_verified,'native_evidence_ids_with_preserved_retrieval_times':reused,'native_commands':commands,'native_check_result':j,'native_check_log_sha256':sha(S/'native/check.log'),'C_independent_science_binding':{'path':str((S/'research-root/review-c/central-binding-addendum.json').relative_to(R)),'sha256':sha(S/'research-root/review-c/central-binding-addendum.json'),'case_count':14,'payload_count':7,'scientific_basis':cb['scientific_basis']},'counts':actual_counts,'remaining_limits':{'case_limits':len(limits),'unresolved_case_indices':unresolved,'downstream_hold_rows':allholds,'all_fields_match_canonical_outcomes_and_frozen_states':True},'handoff_claim_assessments':['Counts and all current/historical ledger hashes agree with exact files.','Native full74 scope means26 changed proposal entries plus48 changed outcomes, not188 fresh source reviews or whole-owner approval.','The twelve native supported assessments concern bounded proposed finding dispositions, with J887/1886 and product/form uncertainties explicitly retained.','Authorship and distinct science review rotation are disclosed; publication scrutiny does not self-approve this reviewer science.','The29 unresolved cases and all88 historical downstream holds remain; coordinator acceptance is pending.','Recorded native check is exit0 with1023 valid retained reviews and declared_scopes_only; this reviewer did not rerun the full corpus check.','Previously failed candidates/checker assumptions and historical manifests remain unchanged.','No maintained application, source selector, SSSOM, export or downstream rebuild is claimed; existing tracked files are unchanged.'],'historical_preservation':historical,'initial_checker_attempt':{'path':str((O/'publication-check-attempt-1.json').relative_to(R)),'sha256':sha(O/'publication-check-attempt-1.json'),'disposition':'Checker metadata assumption corrected; original script and exception preserved.'},'prepublication_git':{'branch':branch,'base':comp['parent_published_head'],'tracked_diff':tracked,'status':git('status','--short').splitlines()},'prior_complete_integration_review':{'path':str((O/'review-final.json').relative_to(R)),'sha256':sha(O/'review-final.json')},'pending_publication_steps':['Root creates final successor manifest, stages exact new successor/native files, performs ordinary commit and push.','This receipt does not claim verification of a future commit, push or not-yet-created successor manifest.'],'whole_owner_role_export_approval':False,'coordinator_source_case_acceptance':'pending independent re-review','maintained_mutation':False}
if errors:
 print(json.dumps({'status':'FAIL','errors':errors},indent=2));sys.exit(1)
out=O/'publication-review.json'
if out.exists():raise RuntimeError('Refusing to overwrite sealed publication review')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'status':'PASS','path':str(out.relative_to(R)),'sha256':sha(out),'native_source_inputs':len(source_verified),'native_evidence':len(nev),'remaining_limits':len(limits),'historical_members':sum(x['members_verified'] for x in historical)}))
