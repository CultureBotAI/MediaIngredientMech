import json,copy,dataclasses
from guarded_writer_v1 import *
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
root=O/'validation/controls';root.mkdir(parents=True,exist_ok=True)
results=[]
def reject(name,pid,mutator,dest=None):
 w=Writer();p=w.prepare(pid);mutator(p);out=dest or root/(name+'.yaml');before=out.read_bytes() if out.is_file() else None
 try:w.write(p,out)
 except (ValueError,Exception) as e:
  unchanged=(out.read_bytes() if out.is_file() else None)==before
  require(unchanged,'negative control created/changed output');results.append({'control':name,'result':'PASS_REFUSED_NO_OUTPUT_CHANGE','exception':type(e).__name__,'message':str(e),'destination':str(out),'no_output_change':True});return
 raise AssertionError('control improperly accepted: '+name)
g='W03-DEP-1176-GYPS';p='W03-DEP-1176-PYGS';m='W03-DEP-1176-MARINE_AGAR_2216'
reject('false_prepared_old_bytes',p,lambda x:x.update(old_bytes=b'false bridge fixture'))
reject('mutated_before_object',p,lambda x:x['before_record'].update(preferred_term='false before'))
reject('foreign_origin_impersonation',p,lambda x:x['row']['predecessor_origin'].update(worker=3))
reject('invented_core_membership',g,lambda x:x['row'].update(native_source_core_member=True))
reject('invented_GYPS_case',g,lambda x:x['row'].update(predecessor_origin={'worker':3,'case_id':'invented'}))
reject('fabricated_before_hash',m,lambda x:x['row']['maintained_before'].update(sha256='0'*64))
reject('different_owner',p,lambda x:x['row'].update(owner_path='data/ingredients/mapped/Peptone.yaml'))
reject('wrong_generic_to_Bacto',p,lambda x:x['after_record']['components'][0].update(component_id='MICRO:0000178'))
reject('wrong_Bacto_to_generic',g,lambda x:x['after_record']['components'][2].update(component_id='mesh:D010461'))
reject('Marine_stale_quantity_basis',m,lambda x:x['after_record']['components'][0].update(concentration_unit='G_PER_L'))
reject('Marine_Mg_reintroduced_hydrate',m,lambda x:x['after_record']['components'][4].update(component_id='CHEBI:86345',reference_scope='MIM_CATALOG'))
reject('invented_PYGS_quantity',p,lambda x:x['after_record']['components'][0].update(concentration_value='1',concentration_unit='G_PER_L'))
reject('GYPS_quantity_projection',g,lambda x:x['after_record']['components'][2].update(concentration_value='1',concentration_unit='G_PER_L'))
reject('other_component_mutation',p,lambda x:x['after_record']['components'][3].update(component_name='mineral salts'))
reject('history_deleted',p,lambda x:x['after_record']['curation_history'].pop(0))
reject('false_human_attribution',p,lambda x:x['after_record']['curation_history'][-1].update(llm_assisted=False,curator='human'))
reject('prior_source_evidence_deleted',p,lambda x:x['after_record']['component_assertion']['evidence'].pop(0))
reject('whole_status_promotion',g,lambda x:x['after_record'].update(mapping_status='REVIEWED'))
reject('application_flag_injected',p,lambda x:x['row'].update(application_authorized=True))
reject('outside_destination',p,lambda x:None,O/'not-authorized.yaml')
existing=root/'existing.yaml';existing.write_text('sentinel\n');reject('existing_destination',p,lambda x:None,existing)
alias=root/'Alias.yaml';alias.write_text('sentinel\n');reject('case_alias_destination',p,lambda x:None,root/'alias.yaml')
symlink=root/'linked';symlink.symlink_to(root,target_is_directory=True);reject('symlink_destination',p,lambda x:None,symlink/'bad.yaml')
# Positive all-three paths exercise the same writer; test outputs never become selected proposals.
for pid in [g,p,m]:
 w=Writer();prepared=w.prepare(pid);r=w.write(prepared,root/('positive-'+pid+'.yaml'));results.append({'control':'positive-'+pid,'result':'PASS_NATIVE_WRITE','payload_sha256':r['payload']['sha256']})
# Native structure proves existence/shape, not source scope. No maintained write.
records={str(q.relative_to(R)):yaml.safe_load(q.read_bytes()) for q in (R/'data/ingredients').rglob('*.yaml')}
for n in ['Peptone','Bacto_Peptone']:records['data/ingredients/mapped/'+n+'.yaml']=yaml.safe_load((O/'inputs/targets'/f'{n}.yaml').read_bytes())
for n in ['GYPS','PYGS','Marine_agar_2216']:records['data/ingredients/mapped/'+n+'.yaml']=yaml.safe_load((O/'payloads'/f'{n}.yaml').read_bytes())
ids={records['data/ingredients/mapped/'+n+'.yaml']['identifier'] for n in ['GYPS','PYGS','Marine_agar_2216']}
errors=validate_component_partonomy(records.values());target_errors=[dataclasses.asdict(e) for e in errors if e.record_id in ids];require(not target_errors,'actual target partonomy failed')
actual={'records_context':len(records),'target_count':3,'target_errors':target_errors,'unrelated_context_errors':[dataclasses.asdict(e) for e in errors if e.record_id not in ids]}
# A syntactically/catalog-valid semantic misroute passes native checks: use actual generic labels.
bad=copy.deepcopy(records);bad['data/ingredients/mapped/PYGS.yaml']['components'][0]['component_id']='MICRO:0000178';bad['data/ingredients/mapped/GYPS.yaml']['components'][2].update(component_name='peptone',component_id='mesh:D010461')
baderrors=[dataclasses.asdict(e) for e in validate_component_partonomy(bad.values()) if e.record_id in ids];require(not baderrors,'counterfactual no longer tests structural blindspot')
results.append({'control':'source_wrong_PYGS_Bacto_and_GYPS_generic','result':'NATIVE_PASS_SEMANTICALLY_REJECTED','target_errors':baderrors,'meaning':'Native schema/catalog checks cannot certify generic/product scope; writer negative controls and primary reviews reject these exact misroutes.'})
missing=copy.deepcopy(records);missing.pop('data/ingredients/mapped/Peptone.yaml'); errs=[dataclasses.asdict(e) for e in validate_component_partonomy(missing.values()) if e.record_id in ids];require(any(e['code']=='UNRESOLVED_MIM_REFERENCE' for e in errs),'missing-parent control not detected')
results.append({'control':'missing_generic_parent','result':'NATIVE_REFUSED','errors':errs})
# Complete projections prove no science outside the exact intended part/provenance/history changed.
proof=[]
for row in Writer().plan['rows']:
 old=yaml.safe_load(pinned(row['current_payload']));new=yaml.safe_load((O/'payloads'/pathlib.Path(row['owner_path']).name).read_bytes());norm=copy.deepcopy(new);idx=row['component_index'];norm['components'][idx]=copy.deepcopy(old['components'][idx]);norm['component_assertion']['evidence']=norm['component_assertion']['evidence'][:-len(row['append_evidence'])];norm['curation_history']=norm['curation_history'][:-1];require(norm==old,'unexpected scientific field change')
 proof.append({'dependency_id':row['dependency_id'],'full_retained_projection_sha256':sha(canon(norm)),'all_other_scientific_fields_exact':True,'prior_history_exact_prefix':True,'prior_component_evidence_exact_prefix':True,'quantities_and_absence_preserved':all([(a.get('concentration_value'),a.get('concentration_unit'))==(b.get('concentration_value'),b.get('concentration_unit')) for a,b in zip(old['components'],new['components'])])})
report={'status':'PASS','native_partonomy':actual,'controls':results,'control_count':len(results),'retention_proofs':proof,'limitations':'Single-author task guards. No hostile-concurrency claim or full repository QC. Context catalog used only for focused three-owner relation checks; source/role/export approval withheld.'}
(O/'validation/focused-controls.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS controls',len(results),'target_errors',len(target_errors),'unrelated',len(actual['unrelated_context_errors']))
