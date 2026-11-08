from pathlib import Path
import copy,datetime,hashlib,importlib.util,json,subprocess,sys
sys.dont_write_bytecode=True
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v5';P=R/'.temp/all-unmatched-worker-10/successor-v5/skeptic'
HEAD='82fc29d837a223edb9c436445ec7ea13d2840c7b';C9='c9a96da71a1977014680e5a92e600dfc7e3874db';PID='sv1-bio-calf_blood_togo_m2854'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_bytes());canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest();bind=lambda p:{'path':str(p.relative_to(R)),'sha256':sha(p)}
checks=[];started=datetime.datetime.now(datetime.timezone.utc).isoformat()
def ck(n,x):checks.append({'check':n,'pass':bool(x)})
def blob(p,h):return subprocess.check_output(['git','show',h+':'+str(p.relative_to(R))],cwd=R)
F={k:load(S/'final-core'/f'{k}.json')[k] for k in ['decisions','proposals','evidence']};author={k:load(S/'author-core'/f'{k}.json')[k] for k in F}
bases={}
for label,h,folder in [('current',HEAD,A/'successor-v4/final-core'),('c9',C9,A/'successor-v3')]:
 bases[label]={}
 for k in F:
  p=folder/f'{k}.json';raw=blob(p,h);ck('authentic '+label+' '+k,raw==p.read_bytes());bases[label][k]=json.loads(raw)[k]
selection=load(S/'selection.json');complete=load(S/'complete-bridge.json');combined=load(S/'combined-c9-bridge.json');finalization=load(S/'finalization-binding.json')
for b in selection['authoritative_core'].values():ck('selected core hash '+b['path'],sha(A/b['path'])==b['sha256'])
ck('exact final core binding',selection['authoritative_core']==finalization['final_core'])
ck('full final population',len(F['decisions'])==188 and len(F['proposals'])==127 and len(F['evidence'])==1212)
append_ids=['sv5-independent-wording','sv5-independent-retention','sv5-native-narrow-validation']
expected_bindings=[{'path':'successor-v5/reviews/skeptic/scientific-review-v1.json','sha256':'088acd5c1669d9462da11dbb61641916b4f6b09ad8b67e02004c724c2ffebca0'},{'path':'successor-v5/reviews/retention/author-core-retention-review-v1.json','sha256':'b59f5174f01b907207c377c77b1f70caeb42a96cc3c847ceef2a37a5f266e4d6'}]
for kind in ['decisions','proposals']:
 for i,(a,b) in enumerate(zip(author[kind],F[kind])):
  changed=(i==44 if kind=='decisions' else b['proposal_id']==PID)
  if not changed:ck('retained full author object '+kind+str(i),a==b);continue
  x=copy.deepcopy(b);m=x['wording_successor']
  ck('exact bounded final review '+kind,m['review_state']=='complete_for_exact_bounded_wording_correction' and m['independent_review_bindings']==expected_bindings and b['independent_review']=={'status':'complete','evidence_ids':append_ids[:2]})
  ck('only exact evidence append '+kind,b['evidence_ids']==a['evidence_ids']+append_ids)
  m['review_state']=a['wording_successor']['review_state'];m.pop('independent_review_bindings');x['independent_review']=a['independent_review'];x['evidence_ids']=a['evidence_ids']
  if kind=='proposals':
   ck('scoped final proposal review explanation','not blanket-transferred' in x['review_status_explanation'] and 'carbonate correction has its own exact S4 reviews' in x['review_status_explanation']);x['review_status_explanation']=a['review_status_explanation']
  ck('whole finalization rollback '+kind,x==a)
ck('all author evidence exact plus3 review objects',F['evidence'][:len(author['evidence'])]==author['evidence'] and [e['evidence_id'] for e in F['evidence'][len(author['evidence']):]]==append_ids)
for e in F['evidence'][1206:]:ck('new exact evidence '+e['evidence_id'],sha(A/e['capture']['path'])==e['capture']['sha256'])
for label,bridge in [('current',complete),('c9',combined)]:
 B=bases[label];ck('full bridge population '+label,len(bridge['all_cases'])==188 and len(bridge['all_proposals'])==127)
 for i,(a,b,row) in enumerate(zip(B['decisions'],F['decisions'],bridge['all_cases'])):
  ck(label+' exact case bridge '+str(i),row['source_index']==i and row['case_id']==b['case_id'] and row['before_object_sha256']==canon(a) and row['after_object_sha256']==canon(b) and row['complete_object_exact']==(a==b) and row['reasoning_exact']==(a['reasoning']==b['reasoning']) and row['occurrence_ids']==b['occurrence_ids'] and row['proposal_ids']==b['proposal_ids'])
  ck(label+' original source/routing scope '+str(i),all(a.get(k)==b.get(k) for k in ['case_id','case_input_sha256','source','occurrence_ids','disposition','applicability','proposal_ids','owner_records','publication_approval','existing_holds_preserved']))
 for a,b,row in zip(B['proposals'],F['proposals'],bridge['all_proposals']):
  ck(label+' exact proposal bridge '+b['proposal_id'],row['proposal_id']==b['proposal_id'] and row['before_proposal_sha256']==canon(a) and row['after_proposal_sha256']==canon(b) and row['proposal_object_exact']==(a==b) and row['old_capture']==a['after_capture'] and row['selected_capture']==b['after_capture'] and row['payload_byte_exact']==(a['after_capture']['sha256']==b['after_capture']['sha256']) and row['owner_path']==b['owner_path'] and row['before_owner_sha256']==b['before_sha256'] and row['case_ids']==b['case_ids'] and row['whole_owner_approval'] is False)
 ck(label+' all304 occurrence bindings retained',[d['occurrence_ids'] for d in B['decisions']]==[d['occurrence_ids'] for d in F['decisions']] and len({o for d in F['decisions'] for o in d['occurrence_ids']})==304)
 expected_cases=[44] if label=='current' else [21,44,187];ck(label+' exact changed case partition',[i for i,(a,b) in enumerate(zip(B['decisions'],F['decisions'])) if a!=b]==expected_cases)
 expected_pids={PID} if label=='current' else {PID,'sv1-buffers-carbonate_co2_nominal4percent_togo_m202'};ck(label+' exact changed proposal partition',{b['proposal_id'] for a,b in zip(B['proposals'],F['proposals']) if a!=b}==expected_pids)
for b,s in zip(F['proposals'],selection['selected_payloads']):
 ck('exact selected projection '+b['proposal_id'],all(s[k]==b.get('destination_path',b['owner_path']) if k=='destination_path' else s[k]==b[k] for k in s))
 ck('selected full payload hash '+b['proposal_id'],sha(A/b['after_capture']['path'])==b['after_capture']['sha256'])
ck('no new retirement and exact prior bridge chain',complete['current_proposals_retired']==[] and all(sha(A/complete[k]['path'])==complete[k]['sha256'] for k in ['earlier_retirement_bridge','previous_complete_bridge']))
pair=load(S/'native/saved-pair.json');np=R/pair['files'][0]['path'];mp=R/pair['files'][1]['path'];spec=importlib.util.spec_from_file_location('native_review_readonly',R/'scripts/record_review.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);n=mod.load_document(np.read_text())
for b in pair['files']:ck('native exact frozen pair '+b['path'],sha(R/b['path'])==b['sha256'])
try:mod.validate_review(n);mod.assert_current_source(R,n);err=None
except Exception as ex:err=repr(ex)
ck('independent native validation and current source',err is None);ck('native Markdown exact render parity',mod.render_markdown(n)==mp.read_text())
for b in n['source']['inputs']:ck('native source binding '+b['path'],sha(R/b['path'])==b['sha256'])
for e in n['evidence']:ck('native evidence binding '+e['evidence_id'],sha(R/e['reference'])==e['snapshot_sha256'])
ck('native exact two target scope',len(n['targets'])==len(n['assessments'])==n['scope']['population_size']==2 and n['targets'][1]['selector']=='$.decisions[44]' and n['targets'][1]['target_id']==F['decisions'][44]['case_id'])
ck('native actual previous head working tree',n['source']['git_revision']==HEAD and n['source']['state']=='working_tree')
ck('native truthful root and reviewer involvement',n['reviewer']['independence']=='self_review' and 'authored the original disclosed finding' in n['reviewer']['independence_basis'] and 'did not author this candidate' in n['reviewer']['independence_basis'])
ck('native science scope narrow and holds explicit',n['scientific_review'] is True and 'corrected explanation only' in ' '.join(n['limitations']) and 'without new science approval' in ' '.join(n['limitations']))
ck('native no historical finding closure',n['findings']==n['actions']==[] and 'does not close the GitHub issue or rewrite' in ' '.join(n['limitations']))
dt=lambda x:datetime.datetime.fromisoformat(x.replace('Z','+00:00'))
ck('native start is exact labelled preflight milestone',dt(n['started_at'])==dt(load(S/'preflight.json')['at']) and 'exact start is unknown' in ' '.join(n['limitations']))
ck('native actual assembly finish precedes validation',dt(n['started_at'])<dt(n['finished_at'])<=dt(load(S/'native/validate-command.json')['started_at']))
ck('actual narrow validation and structural audit passed',load(S/'validation/narrow-native.json')['status']=='PASS' and load(S/'structural-command.json')['exit_code']==0)
ck('original independent science frozen',sha(S/'reviews/skeptic/scientific-review-v1.json')=='088acd5c1669d9462da11dbb61641916b4f6b09ad8b67e02004c724c2ffebca0')
ck('source HEAD unchanged',subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()==HEAD)
out={'started_at':started,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS' if all(c['pass'] for c in checks) else 'FAIL','check_count':len(checks),'checks':checks,'failures':[c for c in checks if not c['pass']],'input_bindings':[bind(S/n) for n in ['selection.json','complete-bridge.json','combined-c9-bridge.json','finalization-binding.json','final-core/decisions.json','final-core/proposals.json','final-core/evidence.json','native/saved-pair.json','validation/narrow-native.json','structural-command.json']]+[bind(np),bind(mp)],'native_source_inputs':len(n['source']['inputs']),'native_evidence':len(n['evidence']),'native_targets':len(n['targets']),'native_error':err,'scope':'Finalization, both complete315-row bridges and native metadata. No renewed scientific approval of carbonate or any retained owner; handoff/full native check receipt remain for the final assembly observation.'}
with (P/'final-assembly-verification-v1.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'status':out['status'],'checks':out['check_count'],'failures':out['failures'],'receipt':bind(P/'final-assembly-verification-v1.json')}))
