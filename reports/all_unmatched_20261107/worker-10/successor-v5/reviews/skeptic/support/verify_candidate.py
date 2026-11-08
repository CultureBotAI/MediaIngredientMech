from pathlib import Path
import copy,datetime,hashlib,json,subprocess,sys,yaml
sys.dont_write_bytecode=True
R=Path.cwd();sys.path.insert(0,str(R/'src'))
from mediaingredientmech.validation.write_validated import validate_ingredient
A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v5';B=A/'successor-v4/final-core';P=R/'.temp/all-unmatched-worker-10/successor-v5/skeptic'
HEAD='82fc29d837a223edb9c436445ec7ea13d2840c7b';PID='sv1-bio-calf_blood_togo_m2854'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_bytes());canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
start=datetime.datetime.now(datetime.timezone.utc).isoformat();checks=[]
def ck(n,x):checks.append({'check':n,'pass':bool(x)})
def blob(p):return subprocess.check_output(['git','show',HEAD+':'+str(p.relative_to(R))],cwd=R)
freeze=load(S/'author-freeze.json');proof=load(S/'payload-change-proof.json');source=load(S/'source-assessment.json');initial=load(P/'source-scope-review-v1.json')
for b in [freeze['payload'],freeze['proof'],freeze['source_assessment'],*freeze['author_core'].values()]:ck('author frozen input '+b['path'],sha(A/b['path'])==b['sha256'])
before_path=A/proof['before']['path'];after_path=A/proof['after']['path'];before=yaml.safe_load(before_path.read_text());after=yaml.safe_load(after_path.read_text())
ck('authentic predecessor',before_path.read_bytes()==blob(before_path) and sha(before_path)=='62f0dc3300c488be2fb9d52f2c65e8e6826715d81177cf8e4ce48af422ed7338')
ck('exact successor',sha(after_path)=='7a54c5bb03008949dec5ced0fbb8da9deee348fd4ad2473e66d41655db975b9d')
oldtext=proof['old_explanation'];newtext=proof['new_explanation']
ck('only exact mapping current note substitution',after['ontology_mapping']['evidence'][0]['notes']==before['ontology_mapping']['evidence'][0]['notes'].replace(oldtext,newtext))
ck('only exact general current note substitution',after['notes']==before['notes'].replace(oldtext,newtext))
ck('one appended truthful history; old prefix exact',after['curation_history'][:-1]==before['curation_history'] and after['curation_history'][-1]==proof['appended_history'] and len(after['curation_history'])==len(before['curation_history'])+1)
event=after['curation_history'][-1];ck('actual AI author and status unchanged',event['curator']=='Codex worker10 /root' and event['llm_assisted'] is True and event['previous_status']==event['new_status']==before['mapping_status'] and event['action']=='CORRECTED_CALF_BLOOD_EXPLANATION')
restore=copy.deepcopy(after);restore['notes']=before['notes'];restore['ontology_mapping']['evidence'][0]['notes']=before['ontology_mapping']['evidence'][0]['notes'];restore['curation_history'].pop()
ck('entire payload exact after authorized rollback',restore==before)
ck('raw YAML predecessor restored without unrelated formatting changes',yaml.safe_dump(restore,sort_keys=False,allow_unicode=True,width=80).encode()==before_path.read_bytes())
ck('exact whole object hashes independently computed',canon(before)==proof['before_object_sha256'] and canon(after)==proof['after_object_sha256'])
ck('source/identity/mapping/provenance unchanged',after['ontology_mapping']['evidence'][0]['source']==before['ontology_mapping']['evidence'][0]['source'] and after['ontology_mapping']['evidence'][0]['evidence_type']=='LLM_SUGGESTION' and after['identifier']==before['identifier'] and after['ontology_mapping']['mapping_quality']==before['ontology_mapping']['mapping_quality']=='NARROW_MATCH')
ck('new current explanation contains bounded correct distinctions',all(t in newtext for t in ['source names calf blood','blood material rather than serum','calf specifies developmental origin','does not explicitly say whole','defibrination, lysis, supplier','basis of its literal 10%','remain unknown']))
ck('misleading age/fraction phrase no longer active',all('Calf age class distinguishes it from serum' not in after[k] for k in ['notes']) and 'Calf age class distinguishes it from serum' not in after['ontology_mapping']['evidence'][0]['notes'])
schema_errors=validate_ingredient(after);ck('fresh native full record closed-schema validation',not schema_errors)
old={k:load(B/f'{k}.json')[k] for k in ['decisions','proposals','evidence']};cur={k:load(S/'author-core'/f'{k}.json')[k] for k in old}
for k in old:ck('authentic predecessor complete core '+k,(B/f'{k}.json').read_bytes()==blob(B/f'{k}.json'))
ck('all188case IDs and order preserved',len(cur['decisions'])==len(old['decisions'])==188 and [x['case_id'] for x in cur['decisions']]==[x['case_id'] for x in old['decisions']])
ck('all127proposal IDs and order preserved',len(cur['proposals'])==len(old['proposals'])==127 and [x['proposal_id'] for x in cur['proposals']]==[x['proposal_id'] for x in old['proposals']])
ck('all304 occurrence bindings exact',[x['occurrence_ids'] for x in cur['decisions']]==[x['occurrence_ids'] for x in old['decisions']] and len({i for x in cur['decisions'] for i in x['occurrence_ids']})==304)
ck('only case44 changed',[i for i,(a,b) in enumerate(zip(old['decisions'],cur['decisions'])) if a!=b]==[44])
ck('only calf proposal changed',[b['proposal_id'] for a,b in zip(old['proposals'],cur['proposals']) if a!=b]==[PID])
eids=['sv5-calf-source-assessment','sv5-calf-field-diff','sv5-calf-filed-finding']
ck('all1206 old evidence objects exact',cur['evidence'][:1206]==old['evidence'] and len(old['evidence'])==1206 and len(cur['evidence'])==1209 and [e['evidence_id'] for e in cur['evidence'][1206:]]==eids)
ck('no duplicate current evidence IDs',len({e['evidence_id'] for e in cur['evidence']})==len(cur['evidence']))
caseold=old['decisions'][44];case=cur['decisions'][44];propold=next(x for x in old['proposals'] if x['proposal_id']==PID);prop=next(x for x in cur['proposals'] if x['proposal_id']==PID)
for kind,a,b in [('case',caseold,case),('proposal',propold,prop)]:
 x=copy.deepcopy(b);marker=x.pop('wording_successor')
 ck(kind+' honest pending review with exact oldreview retained',b['independent_review']=={'status':'pending','evidence_ids':[]} and marker['prior_independent_review']==a['independent_review'] and marker['review_state']=='pending_exact_independent_review')
 ck(kind+' exact payload/author/scope bridge',marker['previous_capture']==proof['before'] and marker['selected_capture']==proof['after'] and marker['predecessor_head']==HEAD and marker['author']=='Codex worker10 /root' and marker['identity_or_alias_change'] is False and marker['whole_owner_or_export_approval'] is False)
 ck(kind+' exactly3evidence appended',b['evidence_ids']==a['evidence_ids']+eids)
 x['independent_review']=a['independent_review'];x['evidence_ids']=a['evidence_ids']
 if kind=='case':
  ck('case exact two explanation replacements',b['reasoning']==b['completion_reassessment']['bounded_scientific_conclusion']==newtext and a['reasoning']==a['completion_reassessment']['bounded_scientific_conclusion']==oldtext)
  ck('case exact issue link append',b['issue_refs']==a['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6719103915'])
  x['reasoning']=a['reasoning'];x['completion_reassessment']['bounded_scientific_conclusion']=a['completion_reassessment']['bounded_scientific_conclusion'];x['issue_refs']=a['issue_refs']
 else:
  ck('proposal exact description replacement',b['description']==newtext and a['description']==oldtext)
  ck('proposal review state explicitly limited','Pending exact bounded wording' in b['review_status_explanation'] and 'no blanket' in b['review_status_explanation'])
  for k in ['description','after_capture','review_status_explanation']:x[k]=a[k]
 ck(kind+' whole object exact authorized rollback',x==a)
for i,(a,b) in enumerate(zip(old['decisions'],cur['decisions'])):
 ck('allcase source/backlinks/holds exact '+str(i),all(a.get(k)==b.get(k) for k in ['case_id','case_input_sha256','source','occurrence_ids','disposition','applicability','proposal_ids','owner_records','publication_approval','existing_holds_preserved']))
 if i!=44:ck('unchanged complete decision '+str(i),a==b)
payloads=[]
for a,b in zip(old['proposals'],cur['proposals']):
 p=A/b['after_capture']['path'];ck('selected payload exact '+b['proposal_id'],sha(p)==b['after_capture']['sha256'])
 if b['proposal_id']!=PID:ck('unchanged complete proposal and payload '+b['proposal_id'],a==b and p.read_bytes()==blob(p))
 payloads.append({'proposal_id':b['proposal_id'],'after_capture':b['after_capture'],'changed':b['proposal_id']==PID})
for e in cur['evidence'][1206:]:ck('new evidence captured bytes '+e['evidence_id'],sha(A/e['capture']['path'])==e['capture']['sha256'])
ck('author exact source object and positive rows',source['source']==initial['source_evidence'] and source['source_row']==initial['full_source']['components'][0]['items'][1] and source['source_comments']==initial['full_source']['comments'] and source['no_new_primary_http_retrieval'] is True)
issue=load(S/'inputs/issue1237-filed-finding.json');ck('filed finding precedes correction',issue['id']==6719103915 and issue['html_url']==source['issue'] and issue['created_at']<event['timestamp'] and 'W10-SV3-SKEPTIC-CALF-BLOOD-WORDING' in issue['body'])
ck('source head still authorized predecessor',subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()==HEAD)
out={'started_at':start,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS' if all(c['pass'] for c in checks) else 'FAIL','checks':checks,'check_count':len(checks),'failures':[c for c in checks if not c['pass']],'author_freeze':freeze,'full_payload_before':before,'full_payload_after':after,'full_case_before':caseold,'full_case_after':case,'full_proposal_before':propold,'full_proposal_after':prop,'all127_payload_bindings':payloads,'new_evidence_objects':cur['evidence'][1206:],'native_schema_errors':[str(e) for e in schema_errors],'counts':{'cases':188,'unchanged_complete_decisions':187,'selected_payloads':127,'unchanged_other_payloads_and_proposals':126,'occurrences':304,'old_evidence_exact':1206,'new_evidence':3,'author_evidence_total':1209},'source_interpretation':'The exact corrected current explanation distinguishes material fraction from developmental origin, withdraws the unsupported literal whole qualifier, and retains unspecified processing and percentage basis without changing identity, mapping or aliases. Historical erroneous text is preserved as historical, with an explicit corrective event.'}
with (P/'candidate-verification-v1.json').open('x') as f:json.dump(out,f,indent=2,ensure_ascii=False);f.write('\n')
print(json.dumps({'status':out['status'],'check_count':len(checks),'failures':out['failures'],'sha256':sha(P/'candidate-verification-v1.json')}))
