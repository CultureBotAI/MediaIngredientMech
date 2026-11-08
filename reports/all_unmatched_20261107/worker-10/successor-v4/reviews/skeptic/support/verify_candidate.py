from pathlib import Path
import copy,datetime,hashlib,json,subprocess,sys
sys.dont_write_bytecode=True
R=Path.cwd();sys.path.insert(0,str(R/'src'))
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient
A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v4';V=A/'successor-v3';O=R/'.temp/all-unmatched-worker-10/successor-v4/skeptic'
PID='sv1-buffers-carbonate_co2_nominal4percent_togo_m202';HEAD='c9a96da71a1977014680e5a92e600dfc7e3874db'
sha=lambda b:hashlib.sha256(b).hexdigest()
canon=lambda x:sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
load=lambda p:json.loads(p.read_bytes())
checks=[]
def ck(n,x):checks.append({'check':n,'pass':bool(x)})
def blob(p):return subprocess.check_output(['git','show',HEAD+':'+str(p.relative_to(R))],cwd=R)
def diff(a,b,p=''):
 if type(a)!=type(b):return [{'path':p,'before':a,'after':b}]
 if isinstance(a,dict):return sum((diff(a.get(k),b.get(k),p+'.'+k) for k in sorted(set(a)|set(b))),[])
 if isinstance(a,list):
  if len(a)!=len(b):return [{'path':p,'before':a,'after':b}]
  return sum((diff(x,y,p+f'[{i}]') for i,(x,y) in enumerate(zip(a,b))),[])
 return [] if a==b else [{'path':p,'before':a,'after':b}]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
freeze=load(S/'author-freeze.json')
for bind in list(freeze['author_core'].values())+[freeze['proof'],freeze['source_assessment']]:ck('author frozen binding '+bind['path'],sha((R/bind['path']).read_bytes())==bind['sha256'])
before_path=V/'enum/proposed'/f'{PID}.yaml';after_path=A/freeze['payload']['path']
before_raw=blob(before_path);after_raw=after_path.read_bytes();before=yaml.safe_load(before_raw);after=yaml.safe_load(after_raw)
ck('exact predecessor',before_path.read_bytes()==before_raw and sha(before_raw)=='fa07901e230c7cc707ddacb6f5ff70def989c7d1ecfa40118ef2497136e0e1ce')
ck('exact frozen successor',sha(after_raw)==freeze['payload']['sha256']=='135788bfd2a511671a90ff9b912092df789c9209995f88d11b4aa6134eca0625')
restored=copy.deepcopy(after);restored['component_assertion']['completeness']='PARTIAL';event=restored['curation_history'].pop()
ck('whole payload exact allowed rollback',restored==before)
ck('raw predecessor recovered without formatting drift',yaml.safe_dump(restored,default_flow_style=False,sort_keys=False,allow_unicode=True,width=80).encode()==before_raw)
ck('single specific enum correction',before['component_assertion']['completeness']=='PARTIAL' and after['component_assertion']['completeness']=='UNKNOWN')
ck('one honest appended history',after['curation_history'][:-1]==before['curation_history'] and len(after['curation_history'])==len(before['curation_history'])+1 and event['llm_assisted'] is True and event['curator']=='Codex worker10 /root' and event['action']=='CORRECTED_COMPONENT_COMPLETENESS' and event['previous_status']==event['new_status']==before['mapping_status'])
ck('history cites original findings and exact field',all(x in event['changes'] for x in ['W10-SV2-INHERITED-COMPLETENESS-001','SCI-CARBONATE-COMPLETENESS-001','component_assertion.completeness from PARTIAL to UNKNOWN','6719089745','no water or composition is inferred','No identity, role, whole-owner or export approval change']))
ck('history after filed issue observation',event['timestamp']>'2026-11-08T08:08:22')
ck('LABEL_ENUMERATION two UNMAPPED parts exact',after['component_assertion']['method']=='LABEL_ENUMERATION' and before['components']==after['components'] and len(after['components'])==2 and all(x['reference_scope']=='UNMAPPED' for x in after['components']))
ck('mapping evidence and all other scientific fields exact',after['ontology_mapping']==before['ontology_mapping'] and after['ontology_mapping']['evidence'][0]['evidence_type']=='LLM_SUGGESTION' and all(after[k]==v for k,v in before.items() if k not in ['component_assertion','curation_history']))
schema_errors=validate_ingredient(after);ck('fresh native closed-schema validation',not schema_errors)
cores={};oldcores={}
for name in ['decisions','proposals','evidence']:
 old_raw=blob(V/f'{name}.json');ck('authentic predecessor core '+name,old_raw==(V/f'{name}.json').read_bytes());oldcores[name]=json.loads(old_raw);cores[name]=load(S/f'author-core/{name}.json')
oldD=oldcores['decisions']['decisions'];D=cores['decisions']['decisions'];oldP=oldcores['proposals']['proposals'];P=cores['proposals']['proposals'];oldE=oldcores['evidence']['evidence'];E=cores['evidence']['evidence']
ck('exact188 unique case population',len(D)==len(oldD)==len({d['case_id'] for d in D})==188 and [d['case_id'] for d in D]==[d['case_id'] for d in oldD])
ck('exact127 proposal population',len(P)==len(oldP)==len({p['proposal_id'] for p in P})==127 and [p['proposal_id'] for p in P]==[p['proposal_id'] for p in oldP])
ck('only cases21/187 modified',[i for i,(a,b) in enumerate(zip(oldD,D)) if a!=b]==[21,187])
ck('only target proposal modified',[p['proposal_id'] for p,q in zip(P,oldP) if p!=q]==[PID])
occ=[x for d in D for x in d['occurrence_ids']];oldocc=[x for d in oldD for x in d['occurrence_ids']]
ck('all304 occurrence bindings exact',occ==oldocc and len(set(occ))==304)
new_ids=['sv4-carbonate-completeness-source','sv4-carbonate-completeness-diff','sv4-carbonate-filed-finding']
ck('all1200 old complete evidence objects exact',len(oldE)==1200 and E[:len(oldE)]==oldE and len(E)==1203 and [e['evidence_id'] for e in E[len(oldE):]]==new_ids)
ck('no duplicate evidence IDs',len(E)==len({e['evidence_id'] for e in E}))
case_deltas=[]
for i,(a,b) in enumerate(zip(oldD,D)):
 ck('case identity/source/routing exact '+str(i),all(a[k]==b[k] for k in ['case_id','case_input_sha256','source','occurrence_ids','disposition','proposal_ids','reasoning','applicability']))
 if i not in [21,187]:ck('whole untouched decision exact '+str(i),a==b);continue
 restore=copy.deepcopy(b);marker=restore.pop('completeness_successor')
 ck('case historical review preserved '+str(i),marker['prior_independent_review']==a['independent_review'] and marker['review_state']=='pending_exact_independent_review')
 ck('case pending until fresh review '+str(i),b['independent_review']=={'status':'pending','evidence_ids':[]})
 ck('case exact evidence append '+str(i),b['evidence_ids']==a['evidence_ids']+new_ids)
 ck('case issue lineage append '+str(i),b['issue_refs']==a['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1201#issuecomment-6719089745'])
 for k in ['evidence_ids','issue_refs','independent_review']:restore[k]=a[k]
 if i==21:
  ck('case21 exact dependent hold wording',b['completion_reassessment']['quantitative_or_publication_holds'][1]==a['completion_reassessment']['quantitative_or_publication_holds'][1].replace('PARTIAL components','components with UNKNOWN completeness'))
  restore['completion_reassessment']['quantitative_or_publication_holds'][1]=a['completion_reassessment']['quantitative_or_publication_holds'][1]
 ck('case rollback only authorized dependent metadata '+str(i),restore==a)
 ck('case source association/owner approval flags '+str(i),marker['source_association_changed'] is False and marker['whole_owner_or_export_approval'] is False and marker['selected_capture']==freeze['payload'])
 case_deltas.append({'index':i,'before_sha256':canon(a),'after_sha256':canon(b),'before_complete_case':a,'after_complete_case':b,'changes':diff(a,b)})
payloads=[];proposal_delta=None
for a,b in zip(oldP,P):
 cap=b['after_capture'];p=A/cap['path'];raw=p.read_bytes();ck('selected full payload hash '+b['proposal_id'],sha(raw)==cap['sha256'])
 if b['proposal_id']!=PID:
  ck('unchanged complete proposal and payload '+b['proposal_id'],a==b and raw==blob(p))
 else:
  restore=copy.deepcopy(b);marker=restore.pop('completeness_successor')
  ck('same two case links and one applicable CM occurrence',a['case_ids']==b['case_ids']==[D[21]['case_id'],D[187]['case_id']] and a['applicable_occurrence_ids']==b['applicable_occurrence_ids']==D[21]['occurrence_ids'] and a['source_case_applicability']==b['source_case_applicability'])
  ck('target proposal exact dependent text',b['description']==a['description'].replace('partial source-supported components','source-named components with unknown list completeness') and b['publication_holds'][1]==a['publication_holds'][1].replace('PARTIAL components','components with UNKNOWN completeness'))
  ck('target proposal exact evidence append',b['evidence_ids']==a['evidence_ids']+new_ids)
  ck('target historical review preserved',marker['prior_independent_review']==a['independent_review'] and marker['source_association_changed'] is False and marker['whole_owner_or_export_approval'] is False and marker['selected_capture']==freeze['payload'])
  for k in ['after_capture','description','publication_holds','evidence_ids','independent_review','review_status_explanation']:restore[k]=a[k]
  ck('complete proposal rollback exact',restore==a)
  ck('target pending exact successor review',b['independent_review']=={'status':'pending','evidence_ids':[]} and 'Pending separate exact completeness/source assessment' in b['review_status_explanation'])
  proposal_delta={'before_sha256':canon(a),'after_sha256':canon(b),'before_full_proposal':a,'after_full_proposal':b,'changes':diff(a,b)}
 payloads.append({'proposal_id':b['proposal_id'],'capture':cap,'changed':b['proposal_id']==PID,'before_capture':a['after_capture']})
for e in E[-3:]:ck('new evidence exact capture '+e['evidence_id'],sha((A/e['capture']['path']).read_bytes())==e['capture']['sha256'])
source=load(S/'source-assessment.json');t=load(A/'buffers/captures/2b7e3ee4d3ec3dfb08be.json');md=load(A/'kg/captures/mdJ209.json')
ck('author full source sections/comment/meta literal',source['full_source_sections']==t['components'] and source['full_source_comments']==t['comments'] and source['source_meta']==t['meta'] and source['md_buffer_row']==md['data']['solutions'][0]['recipe'][11])
ck('author original capture times retained',source['fresh_http_primary_retrieval'] is False and all(e==next(x for x in oldE if x['evidence_id']==e['evidence_id']) for e in source['primary_captures_with_original_timestamps']))
ck('source head still unchanged',subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()==HEAD)
fails=[c for c in checks if not c['pass']]
out={'started_at':start,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS' if not fails else 'FAIL','checks':checks,'check_count':len(checks),'failures':fails,'frozen_author_stage':freeze,'payload_before':before,'payload_after':after,'raw_payload_before_sha256':sha(before_raw),'raw_payload_after_sha256':sha(after_raw),'native_schema_errors':[str(x) for x in schema_errors],'case_deltas':case_deltas,'proposal_delta':proposal_delta,'all127_payload_bindings':payloads,'new_evidence_objects':E[-3:],'counts':{'cases':188,'retained_whole_decisions':186,'case_metadata_successors':2,'selected_payloads':127,'unchanged_payloads':126,'changed_payloads':1,'original_occurrences':304,'evidence_old_preserved':1200,'author_evidence_total':1203}}
with (O/'candidate-verification-v1.json').open('x') as f:json.dump(out,f,indent=2,ensure_ascii=False);f.write('\n')
print(json.dumps({'status':out['status'],'checks':len(checks),'failures':fails,'sha256':sha((O/'candidate-verification-v1.json').read_bytes())},indent=2))
