from pathlib import Path
import json,hashlib,datetime,copy,subprocess
import yaml
R=Path.cwd();C=R.parents[2];O=R/'.temp/peptone-final-dependencies-v1';D=O/'source-review'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(n,v):(D/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
plan=json.loads((O/'author-plan-v2.json').read_text()); receipts=json.loads((O/'write-receipts.json').read_text())['rows']; pins=json.loads((D/'input-pins.json').read_text());
for ev in pins['primary_evidence']:
 assert sha(R/ev['path'])==ev['sha256']
expected={'GYPS':'ad9fdcf66ef72672060106af433a32583df72252adae2fb5521b03a696a23725','PYGS':'f95aa34b0872db40d4f2d08918105b54db401e7fa8cf4409e08258b2df936312','Marine_agar_2216':'ed61879570d90b147ee7ed7767b7a900738b1cf010c73e596ba8d7f161490082'}
objects={};results=[]
def validate_delta(stem,b,a,planrow):
 assert set(b)==set(a),'top level fields altered'
 assert len(a['curation_history'])==len(b['curation_history'])+1,'history append count'
 assert a['curation_history'][:-1]==b['curation_history'],'history prefix altered'
 event=a['curation_history'][-1]; assert event['llm_assisted'] is True and event['curator']=='codex-worker03 /root dependent-origin author';assert event['action']=='COUPLED_PEPTONE_REFERENCE';assert event['previous_status']==event['new_status']=='MAPPED'
 expn=3 if stem=='PYGS' else 1;be=b['component_assertion']['evidence'];ae=a['component_assertion']['evidence'];assert ae[:len(be)]==be and len(ae)==len(be)+expn,'evidence prefix/count altered'
 aa=copy.deepcopy(a);aa['curation_history']=copy.deepcopy(b['curation_history']);aa['component_assertion']['evidence']=copy.deepcopy(be)
 i=2 if stem=='GYPS' else 0
 if stem=='GYPS':
  assert a['components'][i]['component_id']=='MICRO:0000178','GYPS generic replacement'
  assert a['components'][i]['component_name']=='Bacto Peptone (Difco)'
  assert 'exact printed constituent: bacto-peptone (Difco)' in a['components'][i]['source']
  assert planrow['predecessor_origin'] is None and planrow['native_source_core_member'] is False,'invented GYPS source origin'
  assert 'historical catalogue/lot is unknown' in ae[-1]['notes'].lower()
  assert 'modern catalogue assignment' in ae[-1]['notes']
  aa['components'][i]['component_name']=b['components'][i]['component_name'];aa['components'][i]['source']=b['components'][i]['source']
 else:
  assert a['components'][i]['component_id']=='mesh:D010461','wrong generic identity'
  aa['components'][i]['component_id']=b['components'][i]['component_id']
 assert aa==b,'unauthorized retained-field change'
 if stem=='Marine_agar_2216':
  assert len(a['components'])==17 and a['component_assertion']['completeness']=='PARTIAL'
  assert a['components'][0]['concentration_value']=='5.0' and a['components'][0]['concentration_unit']=='G_PER_SOURCE_SCRATCH_FORMULA_BATCH'
  mg=next(x for x in a['components'] if x['component_name']=='Magnesium Chloride');assert mg['reference_scope']=='UNMAPPED' and 'component_id' not in mg
  assert '55.2520g' in a['notes'] and '55.1g' in a['notes']
 if stem=='PYGS':assert a['component_assertion']['completeness']=='UNKNOWN' and 'all three material-edge holds remain' in a['component_assertion']['notes']
 return True
for row in plan['rows']:
 stem=Path(row['owner_path']).stem;p=O/'payloads'/f'{stem}.yaml';before=O/row['current_payload']['path']; maintained=O/row['maintained_before']['path']
 assert sha(p)==expected[stem];assert sha(before)==row['current_payload']['sha256'];assert sha(maintained)==row['maintained_before']['sha256'];assert sha(R/row['owner_path'])==sha(maintained)
 b=yaml.safe_load(before.read_text());a=yaml.safe_load(p.read_text());validate_delta(stem,b,a,row)
 origin=row['predecessor_origin'];gitcheck=None
 if origin:
  wr=C/'workers'/f"w{origin['worker']:02d}"/'worktree';blob=subprocess.check_output(['git','-C',str(wr),'show',origin['head']+':'+origin['git_path']]);assert hashlib.sha256(blob).hexdigest()==sha(before);gitcheck={'worker':origin['worker'],'head':origin['head'],'proposal_id':origin['proposal']['proposal_id'],'git_path':origin['git_path'],'exact_blob_matches':True}
 objects[stem]=(b,a,row)
 results.append({'owner_path':row['owner_path'],'payload_sha256':sha(p),'maintained_before_sha256':sha(maintained),'composition_parent_sha256':sha(before),'all_prior_fields_preserved_except_declared_component_change':True,'history_prefix_preserved':True,'history_append_count':1,'component_evidence_append_count':len(a['component_assertion']['evidence'])-len(b['component_assertion']['evidence']),'components':len(a['components']),'top_level_fields':len(a),'predecessor_git_verification':gitcheck,'result':'PASS_FOR_BOUNDED_DEPENDENCY_PROPOSAL','all_other_scientific_holds_preserved':True,'whole_owner_role_export_approval':False})
controls=[]
def control(name,stem,mutation):
 b,a,row=copy.deepcopy(objects[stem]);mutation(a,row)
 try:validate_delta(stem,b,a,row)
 except AssertionError as e:controls.append({'name':name,'expected':'reject','observed':'reject','reason':str(e)});return
 raise AssertionError('negative control accepted: '+name)
control('GYPS generic mesh retarget','GYPS',lambda a,r:a['components'][2].update(component_id='mesh:D010461'))
control('Marine stale per-litre unit','Marine_agar_2216',lambda a,r:a['components'][0].update(concentration_unit='G_PER_L'))
control('Marine lost magnesium withdrawal','Marine_agar_2216',lambda a,r:a['components'][4].update(reference_scope='MIM_CATALOG',component_id='CHEBI:86345'))
control('PYGS erased W06 history','PYGS',lambda a,r:a['curation_history'].pop(-2))
control('PYGS cleared material holds','PYGS',lambda a,r:a['component_assertion'].update(notes='No remaining holds.'))
control('GYPS fabricated frozen source origin','GYPS',lambda a,r:r.update(predecessor_origin={'worker':3,'proposal_id':'invented'}))
control('GYPS modern catalogue assigned','GYPS',lambda a,r:a['components'][2].update(catalog_number='211677'))
control('Marine old owner alias removed','Marine_agar_2216',lambda a,r:a['synonyms'].pop())
control('PYGS changed other starch part','PYGS',lambda a,r:a['components'][3].update(component_name='salts'))
report={'schema_version':1,'reviewer':'/root/peptone_final_sources','independence':'Source reviewer supplied an initial bounded source assessment but did not author or write any payload, writer, author plan or lineage proposal. This is a fresh exact-final-byte source/diff review of root-authored payloads. Separate skeptical review remains independently required.','completed_at':now,'status':'PASS_FOR_EXACT_BOUNDED_DEPENDENCY_PROPOSALS_WITH_RETAINED_HOLDS','author_plan':{'path':str((O/'author-plan-v2.json').relative_to(R)),'sha256':sha(O/'author-plan-v2.json')},'write_receipts_sha256':sha(O/'write-receipts.json'),'reviewed_complete_payloads':results,'source_applicability':{'GYPS':'Printed Alain p1622 explicitly bacto-peptone (Difco); capitalization/hyphen normalization is harmless because exact literal remains in component.source and added evidence. Existing MICRO reference retained conditionally to distinct Bacto owner, not new brand-specific MICRO equivalence or generic peptone. No modern catalogue, quantities, universal formulation or owner approval added.','PYGS':'All three exact original abstracts explicitly name peptone in organism-bound PYGS. New target uses the separately selected actual generic owner mesh:D010461. All other ingredients, UNKNOWN completeness, absent quantities, W06 source-evidence objects/history and three material-edge holds are exact retained objects. Underlying full papers are not claimed inspected.','Marine_agar_2216':'ATCC scratch formula explicitly names generic Peptone5g and1000mL water; generic target is supported. Actual current W04 successor already uses G_PER_SOURCE_SCRATCH_FORMULA_BATCH/PARTIAL,17dry rows, MgUNMAPPED,55.2520g-versus55.1g discrepancy. Those current fields are exact preserved. The earlier source-review suggestion to retain5.0G_PER_L concerned the maintained baseline only and is superseded for current successor composition by this review; no quantity change is recommended.'},'science_retention_boundary':'Complete final payloads read; full object equivalence to exact current W04/W06/maintained GYPS parents verified after removing only one truthful new history event, appended claim evidence and the declared peptone field delta. Retained whole-owner assertions are not newly independently approved.','negative_controls':controls,'positive_controls_passed':3,'new_findings':[],'remaining_conditions':['Root must independently bind final published head and true sidecar origin intake; this source review does not make external dependencies part of W03 frozen188cases.','Generic target c083794668a362203de6430eaa2609c34cd8ef78574a1230aa25b4a64fb55fd7 and distinct Bacto42fdcb34ce61e437b22ce702d43a775b6e0f84804cde1372194034a1789a296b remain exact separate application dependencies.','If distinct Bacto identity is not accepted, a separately reviewed literalUNMAPPED successor is required; do not redirect GYPS to mesh.','Native validation is separate from source proof; no whole owner, role, export or release authority.','FAB/Oxoid and all other source exclusions are unaffected; no global replacement.'],'failed_tool_attempts':[{'command':'python3 read payloads with PyYAML','exit_code':1,'error':'ModuleNotFoundError: No module named yaml','disposition':'Read-only attempt; rerun successfully with maintained private Python3.13 environment. No candidate output written by either attempt.'}]}
dump('final-byte-source-review.json',report)
dump('final-byte-source-review-receipt.json',{'reviewer':'/root/peptone_final_sources','completed_at':now,'status':report['status'],'report_path':str((D/'final-byte-source-review.json').relative_to(R)),'report_sha256':sha(D/'final-byte-source-review.json'),'script_sha256':sha(D/'review_final_bytes.py'),'payloads':[{k:r[k] for k in ['owner_path','payload_sha256']} for r in results],'initial_source_review_preserved':{'path':str((D/'per-consumer-source-assessment.json').relative_to(R)),'sha256':sha(D/'per-consumer-source-assessment.json')},'no_payload_or_origin_writes_performed':True})
print(json.dumps({'report_sha256':sha(D/'final-byte-source-review.json'),'receipt_sha256':sha(D/'final-byte-source-review-receipt.json'),'negative_controls':len(controls),'exact_payloads':3},indent=2))
