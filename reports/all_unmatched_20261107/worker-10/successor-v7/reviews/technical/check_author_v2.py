"""Independent technical/full-payload and lineage checks of frozen S7 author-v2.
Writes only private technical fixtures. No primary-science or release approval.
"""
import copy,csv,datetime,hashlib,importlib.util,json,os,subprocess,sys,time,traceback
from pathlib import Path
from collections import defaultdict
from dataclasses import asdict
sys.dont_write_bytecode=True
R=Path.cwd();P=Path(__file__).resolve().parent;A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v7';RUN=P/'author-v2-checks';RUN.mkdir(exist_ok=False)
sys.path.insert(0,str(R/'src'))
import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import validate_ingredient,write_validated_ingredient,ValidationFailedError
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym
START=datetime.datetime.now(datetime.timezone.utc).isoformat();TIMER=time.monotonic();CHECKS=[];READS={}
NEW='sv7-dependent-columbia-unmapped0118-partition';DIF='sv3-hm-difco-columbia1270';OX='sv1-bio-columbia_blood_agar_oxoid_m2224';BUFS=['sv1-buffers-tris_hcl_0_2m_ph7_5_dsmz273','sv1-buffers-hepes_2m_ph7_jcm556_1200'];CHANGED=[NEW,DIF,*BUFS]
def sha(b):return hashlib.sha256(b).hexdigest()
def raw(p):
 p=Path(p);b=p.read_bytes();READS[str(p)]={'sha256':sha(b),'bytes':len(b)};return b
def js(p):return json.loads(raw(p))
def obj(p):return yaml.safe_load(raw(p))
def ck(n,v,detail=None):
 CHECKS.append({'name':n,'pass':bool(v),'detail':detail})
 if not v:raise AssertionError((n,detail))
def save(n,x):
 p=RUN/n;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False,default=str);f.write('\n')
def cap(x):
 ck('capture root',x['root']=='artifact');p=A/x['path'];ck('capture hash:'+x['path'],sha(raw(p))==x['sha256']);return p
def module(n,p):
 b=raw(p);spec=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(spec);sys.modules[n]=m;exec(compile(b,str(p),'exec'),m.__dict__);return m
def delta(a,b,path=''):
 if type(a)!=type(b):return [path]
 if isinstance(a,dict):return [p for k in sorted(a.keys()|b.keys()) for p in ([path+'/'+k] if k not in a or k not in b else delta(a[k],b[k],path+'/'+k))]
 if isinstance(a,list):return [path] if len(a)!=len(b) else [p for i,(x,y) in enumerate(zip(a,b)) for p in delta(x,y,path+'/'+str(i))]
 return [] if a==b else [path]

def main():
 baseline=js(P/'baseline-v1.json');freeze=js(S/'author-freeze-v2.json');raw(P.parent/'inputs/user-task.md')
 core={n:js(cap(x)) for n,x in freeze['core'].items()};ps=core['proposals.json']['proposals'];ds=core['decisions.json']['decisions'];es=core['evidence.json']['evidence']
 old=baseline['selected_core'];ops=old['proposals.json']['object']['proposals'];ods=old['decisions.json']['object']['decisions'];oes=old['evidence.json']['object']['evidence']
 pb={p['proposal_id']:p for p in ops};pn={p['proposal_id']:p for p in ps};db={d['case_id']:d for d in ods};dn={d['case_id']:d for d in ds}
 ck('original IDs plus one dependent',set(pn)==set(pb)|{NEW} and len(ps)==128)
 ck('original 188 ordered case IDs',[d['case_id'] for d in ds]==[d['case_id'] for d in ods] and len(ds)==188)
 ck('original 304 occurrences exact',[d['occurrence_ids'] for d in ds]==[d['occurrence_ids'] for d in ods] and sum(len(d['occurrence_ids']) for d in ds)==304)
 ck('1218 evidence prefix exact',es[:1218]==oes and len(es)==1224)
 changedp=[pid for pid in pb if pb[pid]!=pn[pid]];ck('four old proposal metadata changes',set(changedp)=={DIF,OX,*BUFS})
 changedc=[cid for cid in db if db[cid]!=dn[cid]];allowedcases={cid for pid in [DIF,OX,*BUFS] for cid in pb[pid]['case_ids']};ck('four affected source cases',set(changedc)==allowedcases)
 records={};before={};payload_diffs={};history_calls=[]
 for p in ps:
  path=cap(p['after_capture']);records[p['proposal_id']]=obj(path)
  ck('closed schema full selected payload:'+p['proposal_id'],not validate_ingredient(records[p['proposal_id']]))
  if p['proposal_id'] in pb:
   oldp=pb[p['proposal_id']];ck('actual kind/before preserved:'+p['proposal_id'],p['kind']==oldp['kind'] and p.get('before_sha256')==oldp.get('before_sha256') and p['owner_path']==oldp['owner_path'])
   if p['proposal_id'] not in [DIF,*BUFS]:ck('124 old payload bytes exact:'+p['proposal_id'],p['after_capture']==oldp['after_capture'])
   before[p['proposal_id']]=obj(cap(oldp['after_capture']))
 ck('new dependency authentic owner',pn[NEW]['kind']=='edit_existing_owner' and pn[NEW]['before_sha256']=='29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324' and pn[NEW]['owner_path']=='data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml')
 before[NEW]=obj(R/pn[NEW]['owner_path']);ck('new before bytes authentic',sha(raw(R/pn[NEW]['owner_path']))==pn[NEW]['before_sha256'])
 for pid in CHANGED:
  oldr=before[pid];r=records[pid];changes=delta(oldr,r);payload_diffs[pid]=changes
  allowed={'/curation_history','/notes','/synonyms/1/synonym_type','/synonyms/2/synonym_type'} if pid==NEW else ({'/curation_history','/notes','/synonyms'} if pid==DIF else {'/curation_history','/component_assertion/completeness'})
  ck('exact allowed changed fields:'+pid,set(changes)==allowed,changes)
  ck('history prefix and single event:'+pid,r['curation_history'][:-1]==oldr['curation_history'] and len(r['curation_history'])==len(oldr['curation_history'])+1)
  event=r['curation_history'][-1];ck('new event real attribution:'+pid,event['llm_assisted'] is True and event['curator']=='Codex worker10 /root' and event['previous_status']==oldr['mapping_status'] and event['new_status']==r['mapping_status'])
  replay=copy.deepcopy(r);replay['curation_history']=copy.deepcopy(oldr['curation_history'])
  calls=[];hcode=record_curation_event.__code__;wcode=write_validated_ingredient.__code__
  def trace(frame,what,arg):
   if what=='call' and frame.f_code in [hcode,wcode]:calls.append({'function':frame.f_code.co_name,'file':frame.f_code.co_filename,'history_length':len(frame.f_locals['record']['curation_history'])})
  dest=RUN/'guarded'/Path(pn[pid].get('destination_path',pn[pid]['owner_path'])).name;ck('new fixture absent:'+pid,not dest.exists());previous=sys.getprofile();sys.setprofile(trace)
  try:record_curation_event(replay,**event);write_validated_ingredient(replay,dest)
  finally:sys.setprofile(previous)
  ck('native history and guarded exact roundtrip:'+pid,replay==r and sha(raw(dest))==pn[pid]['after_capture']['sha256'])
  ck('real native calls:'+pid,[x['function'] for x in calls]==['record_curation_event','write_validated_ingredient'])
  history_calls.append({'proposal_id':pid,'calls':calls,'event':event,'payload_sha256':sha(raw(dest))})
  if pid in BUFS:ck('buffer native enum only:'+pid,oldr['component_assertion']['completeness']=='PARTIAL' and r['component_assertion']['completeness']=='UNKNOWN')
 ck('Difco seven-component assertion retained',records[DIF]['components']==before[DIF]['components'] and records[DIF]['component_assertion']==before[DIF]['component_assertion'] and records[DIF]['component_assertion']['completeness']=='COMPLETE')
 ck('generic identifier/status untouched',records[NEW]['identifier']=='UNMAPPED_0118' and records[NEW]['mapping_status']=='UNMAPPED')
 ck('both vendor raw texts/sources retained',[(x['synonym_text'],x['source']) for x in records[NEW]['synonyms']]==[(x['synonym_text'],x['source']) for x in before[NEW]['synonyms']])
 ck('generic unresolved aliases',all(not is_resolving_synonym(x) for x in records[NEW]['synonyms'][1:]) and is_resolving_synonym(records[NEW]['synonyms'][0]))
 ck('Difco transferred exact sourced vendor label',records[DIF]['synonyms']==[before[NEW]['synonyms'][2]] and is_resolving_synonym(records[DIF]['synonyms'][0]))
 for cid in changedc:
  d=dn[cid];o=db[cid]
  for k in ['case_input_sha256','source','occurrence_ids','owner_records']:ck('case immutable source:'+cid+':'+k,d.get(k)==o.get(k))
  ck('old case evidence preserved:'+cid,d['evidence_ids'][:len(o['evidence_ids'])]==o['evidence_ids'])
  ck('original case proposals retained:'+cid,d['proposal_ids'][:len(o['proposal_ids'])]==o['proposal_ids'])
  newrefs=set(d['evidence_ids'])-set(o['evidence_ids'])
  for e in es[1218:]:
   if e['evidence_id'] in newrefs:ck('new evidence exact applicability:'+cid+':'+e['evidence_id'],cid in e['case_ids'])
 # Full source-routing objects remain separate from campaign membership.
 routing=js(S/'source-routing.json');deps=js(S/'cross-worker-dependencies.json');rows=routing['seven_context_rows']
 ck('three dry context routes four prepared holds',len(rows)==7 and sum(x['route_supported'] for x in rows)==3 and all(not x['assigned_W10_case_added'] and not x['assigned_W10_occurrence_added'] for x in rows))
 for x in rows:
  cap(x['source_recipe_capture']);ck('route exact dependency:'+x['context_id'],x['same_owner_dependency']['after_capture']==pn[NEW]['after_capture'])
  if not x['route_supported']:ck('prepared1L held:'+x['context_id'],x['target_proposal_id'] is None and x['exact_source_quantity']=={'value':'1000','unit':'ML_PER_L'})
 ck('external W04 origin remains new null-before',deps['W04_origin']['original_proposal']['kind']=='new_owner' and deps['W04_origin']['original_proposal']['before_sha256'] is None)
 ck('external origins not selected',deps['W04_origin']['proposal_id'] not in pn and deps['W04_origin']['original_case']['case_id'] not in dn)
 ck('external W04/pattern payload hashes',sha(raw(cap(deps['W04_origin']['payload_capture'])))=='4a3d54349a5c37167c2e13823d67808114c84212cea7dadc876334d4b10904d7' and sha(raw(cap(deps['existing_coordinator_prototype'])))=='5846b9ce27870e67702189ec59d16d255151ebe4016d30783142857a47b68ca2')
 ck('Oxoid payload unchanged and composition held',pn[OX]['after_capture']==pb[OX]['after_capture'] and not deps['combined_payload_authored_here'] and not deps['W04_payload_changed'] and not deps['W10_payload_changed'])
 # Immutable maintained catalog and two in-memory overlays.
 catalog={str(p.relative_to(R)):obj(p) for p in sorted((R/'data/ingredients').rglob('*.yaml'))}
 ck('all2956 baseline owner bytes exact',{p:sha(raw(R/p)) for p in catalog}==baseline['maintained_owner_hashes'])
 def overlay(proposals,rs):
  out=copy.deepcopy(catalog)
  for p in proposals:
   if p['kind']=='edit_existing_owner':ck('actual maintained before:'+p['proposal_id'],sha(raw(R/p['owner_path']))==p['before_sha256']);out.pop(p['owner_path'])
   else:ck('new owner origin null/absent:'+p['proposal_id'],p.get('before_sha256') is None and not (R/p['owner_path']).exists())
   dest=p.get('destination_path',p['owner_path']);ck('no duplicate overlay destination:'+p['proposal_id'],dest not in out);out[dest]=rs[p['proposal_id']]
  return out
 previous=overlay(ops,before);current=overlay(ps,records)
 errors={name:[str(e) for e in validate_component_partonomy(o.values())] for name,o in [('previous',previous),('current',current)]};ck('both full overlays native partonomy',not any(errors.values()),errors)
 def active(o):
  ids=defaultdict(list)
  for p,r in o.items():
   if r.get('mapping_status')!='REJECTED':ids[r['identifier']].append(p)
  return dict(ids)
 ck('active identifier membership unchanged',active(previous)==active(current))
 # Actual label-index emitter, private only.
 exp=module('s7_independent_export_lists',R/'scripts/export_lists.py');lf=RUN/'label-index.csv';exp.export_label_index(list(current.values()),lf)
 with lf.open() as f:labelrows=list(csv.DictReader(f))
 vendor=records[DIF]['synonyms'][0]['synonym_text'];oxlabel=records[NEW]['synonyms'][1]['synonym_text']
 relevant=[x for x in labelrows if x.get('label','').casefold() in [vendor.casefold(),oxlabel.casefold(),'columbia blood agar base']]
 ck('rejected vendor labels absent generic emitter',vendor not in exp._synonyms(records[NEW]) and oxlabel not in exp._synonyms(records[NEW]))
 ck('actual Difco alias emitter',vendor in exp._synonyms(records[DIF]))
 # Native-shape and semantic invariant negative controls are distinguished.
 controls=[]
 for label,mutate in [('unknown_field',lambda r:r.update(synthetic_unknown_field=True)),('bad_enum',lambda r:r['component_assertion'].update(completeness='BAD_ENUM'))]:
  bad=copy.deepcopy(records[BUFS[0]]);mutate(bad);target=RUN/(label+'-must-not-exist.yaml');rejected=False;message=None
  try:write_validated_ingredient(bad,target)
  except ValidationFailedError as e:rejected=True;message=e.summary()
  ck('native writer rejects:'+label,rejected and not target.exists());controls.append({'name':label,'native_rejected':rejected,'diagnostic':message})
 bad=copy.deepcopy(records[NEW]);bad['synonyms'][1]['synonym_type']='CATALOG_VARIANT';ck('resolving-alias regression detected',is_resolving_synonym(bad['synonyms'][1]) and oxlabel in exp._synonyms(bad));controls.append({'name':'reverted_resolving_alias','schema_valid':not validate_ingredient(bad),'native_resolution_guard_detects':True})
 for label,key in [('invented_buffer_part','components'),('changed_buffer_identity','identifier'),('lost_raw_source','synonyms')]:
  pid=NEW if key=='synonyms' else BUFS[0];bad=copy.deepcopy(records[pid])
  if key=='components':bad[key].append({'component_name':'water','reference_scope':'UNMAPPED'})
  elif key=='identifier':bad[key]='kgmicrobe.ingredient:synthetic_wrong_identity'
  else:bad[key][1]['source']='synthetic wrong provenance'
  changes=delta(records[pid],bad);ck('exact full-field control:'+label,bool(changes));controls.append({'name':label,'changed_fields':changes,'exact_authorized_payload_guard_detects':True})
 bad=copy.deepcopy(records[BUFS[0]]);bad['components'][0]['concentration_value']='1';errs=[str(e) for e in validate_component_partonomy([*catalog.values(),bad])];ck('native concentration pairing control',any('INCOMPLETE_CONCENTRATION' in x for x in errs));controls.append({'name':'unpaired_quantity','native_partonomy_errors':errs})
 bad=copy.deepcopy(records[DIF]);bad['components'][2]['component_id']='kgmicrobe.ingredient:missing_s7_control';errs=[str(e) for e in validate_component_partonomy([*catalog.values(),bad])];ck('native unresolved reference control',any('UNRESOLVED_MIM_REFERENCE' in x for x in errs));controls.append({'name':'missing_active_reference','native_partonomy_errors':errs})
 # True producer, complete owner index, in-memory row generation only.
 claw=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw');producer=module('s7_independent_projection',claw/'scripts/build_mim_ingredient_sssom.py');producer._check_producer_bindings();projections={}
 for label,ov,rs in [('before',previous,before),('after',current,records)]:
  owners=producer.build_owner_index({producer._mim_curie(Path(path).name):rec for path,rec in ov.items()});out={}
  for pid in CHANGED:
   path=R/pn[pid].get('destination_path',pn[pid]['owner_path']);suppressed=[];rr=producer._row_from_yaml(path,{},{},{},{},record=rs[pid],owners=owners,suppressions=suppressed);out[pid]={'rows':rr,'suppressions':[asdict(x) for x in suppressed]}
  projections[label]=out
 producer._check_producer_bindings();ck('generic owner has no mapped projection',not projections['before'][NEW]['rows'] and not projections['after'][NEW]['rows'])
 projdiff={}
 for pid in [DIF,*BUFS]:
  a=projections['before'][pid]['rows'];b=projections['after'][pid]['rows'];ck('one own identity projection:'+pid,len(a)==len(b)==1 and b[0]['predicate_id']=='skos:exactMatch' and b[0]['object_id']==records[pid]['identifier'])
  change={k:{'before':a[0].get(k),'after':b[0].get(k)} for k in a[0].keys()|b[0].keys() if a[0].get(k)!=b[0].get(k)};projdiff[pid]=change;ck('bounded projection delta:'+pid,set(change)<={'source','mapping_date','other'} and ('other' not in change or pid==DIF))
 rules=module('s7_independent_rule_d',R/'scripts/validate_sssom_invariants.py');rules.INGREDIENTS_DIR=RUN/'guarded';rules._subject_to_path.cache_clear()
 actualrows=[x for pid in [DIF,*BUFS] for x in projections['after'][pid]['rows']];badrows=[dict(x,predicate_id='skos:closeMatch') for x in actualrows];reject=list(rules.evaluate_rule_d(badrows));ck('native real RuleD positive/negative',not list(rules.evaluate_rule_d(actualrows)) and len(reject)==len(badrows)==3)
 # Preserve all inputs observed before writing the receipt.
 ck('frozen S6 core files remain exact',all(sha(raw(R/x['path']))==x['sha256'] for x in baseline['selected_core'].values()))
 for x in freeze['core'].values():cap(x)
 save('checks.json',{'status':'PASS','started_at':START,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runtime_seconds':time.monotonic()-TIMER,'checks':CHECKS,'input_hashes':READS,'script_sha256':sha(Path(__file__).read_bytes()),'counts':{'proposals':len(ps),'cases':len(ds),'occurrences':304,'evidence':len(es),'unchanged_payloads':124,'changed_old_payloads':3,'new_existing_owner_dependency':1,'unchanged_proposal_objects':123,'changed_old_proposal_metadata':4,'unchanged_cases':184,'changed_cases':4,'maintained_owners':len(catalog),'prior_overlay':len(previous),'current_overlay':len(current)},'changed_case_ids':changedc,'changed_proposal_ids':changedp,'payload_diffs':payload_diffs,'history_calls':history_calls,'partonomy':errors,'label_index_relevant_rows':relevant,'negative_controls':controls,'actual_projections':projections,'projection_differences':projdiff,'RuleD_negative_rejections':reject,'producer_inputs':{str(p):sha(b) for p,b in producer._IMPORTED_PRODUCER_BYTES.items()},'review_pending_not_a_failure':True,'science_approval':False,'whole_owner_role_export_approval':False})
 print(json.dumps({'status':'PASS','checks':len(CHECKS),'counts':{'payloads':128,'guarded_changed':4,'overlay':len(current)},'projection_differences':projdiff},indent=2))

if __name__=='__main__':
 try:main()
 except BaseException as e:
  save('failure.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'error':repr(e),'traceback':traceback.format_exc(),'checks':CHECKS,'input_hashes':READS});raise
