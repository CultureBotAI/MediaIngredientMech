from pathlib import Path
import ast,copy,json,hashlib,datetime,subprocess
import yaml
R=Path.cwd();C=R.parents[2];O=R/'.temp/peptone-final-dependencies-v1';D=O/'source-review'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(n,v):(D/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
old_report=D/'final-byte-source-review.json';assert sha(old_report)=='6ebbf1560037f319973569d0aaf7d86a9813c866559f7caefb81bbcef1901970'
prior=json.loads(old_report.read_text());plan=json.loads((O/'author-plan-v2.json').read_text())
old_check=D/'review_final_bytes.py';assert sha(old_check)==json.loads((D/'final-byte-source-review-receipt.json').read_text())['script_sha256']
# Execute only the previously independently written pure validator function, not its file-writing entry point.
tree=ast.parse(old_check.read_text());fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='validate_delta');exec(compile(ast.Module(body=[fn],type_ignores=[]),'reviewer-v1-pure-function','exec'),globals())
expected={'GYPS':'fa98f361a39dcaf0bea1f4046829287581bc45e2813044696e5070de58708aa1','PYGS':'d28106eb42ad32b85b68177d035b9ee631a15c14941d04c5744f170cf2497cf5','Marine_agar_2216':'3e0263d2bc99643780fd1e3ba8c839661f47c5d64045beb0b71cfc8b058c38b1'}
rows=[];objects={}
for row in plan['rows']:
 stem=Path(row['owner_path']).stem;p=O/'payloads-v2'/f'{stem}.yaml';prev=O/'payloads'/p.name;parent=O/row['current_payload']['path']
 assert sha(p)==expected[stem];assert sha(prev)==next(x['payload_sha256'] for x in prior['reviewed_complete_payloads'] if x['owner_path']==row['owner_path']);assert sha(parent)==row['current_payload']['sha256'];assert sha(R/row['owner_path'])==row['maintained_before']['sha256']
 a=yaml.safe_load(p.read_text());before=yaml.safe_load(parent.read_text());old=yaml.safe_load(prev.read_text());oldstamp=old['curation_history'][-1]['timestamp'];newstamp=a['curation_history'][-1]['timestamp']
 assert oldstamp!=newstamp; assert p.read_bytes().replace(newstamp.encode(),oldstamp.encode(),1)==prev.read_bytes(),'not exact timestamp-only byte change'
 validate_delta(stem,before,a,row)
 gitverified=None
 if row['predecessor_origin']:
  org=row['predecessor_origin'];blob=subprocess.check_output(['git','-C',str(C/'workers'/f"w{org['worker']:02d}"/'worktree'),'show',org['head']+':'+org['git_path']]);assert hashlib.sha256(blob).hexdigest()==sha(parent);gitverified={'worker':org['worker'],'head':org['head'],'git_path':org['git_path'],'sha256':sha(parent)}
 rows.append({'owner_path':row['owner_path'],'payload_path':str(p.relative_to(R)),'payload_sha256':sha(p),'v1_payload_sha256':sha(prev),'old_timestamp':oldstamp,'new_timestamp':newstamp,'exact_bytes_only_timestamp_changed':True,'full_payload_read_and_delta_checked':True,'source_parent_sha256':sha(parent),'git_source_parent_reverified':gitverified,'before_sha256':row['maintained_before']['sha256'],'result':'PASS_WITH_EXISTING_SOURCE_TARGET_APPLICATION_HOLDS'})
 objects[stem]=(before,a,row)
pins=json.loads((D/'input-pins.json').read_text());sourcepins=[]
for ev in pins['primary_evidence']:
 p=R/ev['path'];assert sha(p)==ev['sha256'];sourcepins.append({'path':ev['path'],'sha256':sha(p),'unchanged':True})
controls=[]
def negative(name,stem,mut):
 b,a,r=copy.deepcopy(objects[stem]);mut(a,r)
 try:validate_delta(stem,b,a,r)
 except AssertionError as e:controls.append({'name':name,'expected':'reject','actual':'reject','reason':str(e)});return
 raise AssertionError('unexpected acceptance: '+name)
negative('GYPS generic retarget','GYPS',lambda a,r:a['components'][2].update(component_id='mesh:D010461'))
negative('Marine per-litre regression','Marine_agar_2216',lambda a,r:a['components'][0].update(concentration_unit='G_PER_L'))
negative('Marine Mg hexahydrate regression','Marine_agar_2216',lambda a,r:a['components'][4].update(reference_scope='MIM_CATALOG',component_id='CHEBI:86345'))
negative('PYGS origin history deletion','PYGS',lambda a,r:a['curation_history'].pop(-2))
negative('PYGS hold deletion','PYGS',lambda a,r:a['component_assertion'].update(notes='No holds.'))
negative('GYPS fictional source case','GYPS',lambda a,r:r.update(predecessor_origin={'worker':3,'case':'fabricated'}))
negative('GYPS modern catalogue inference','GYPS',lambda a,r:a['components'][2].update(catalog_number='211677'))
negative('Marine inherited alias loss','Marine_agar_2216',lambda a,r:a['synonyms'].pop())
negative('PYGS unrelated part mutation','PYGS',lambda a,r:a['components'][3].update(component_name='salts'))
report={'reviewer':'/root/peptone_final_sources','completed_at':now,'status':'PASS_FOR_EXACT_V2_BOUNDED_DEPENDENCY_PROPOSALS_WITH_RETAINED_HOLDS','independence':prior['independence'],'reviewed_payloads':rows,'source_hashes_rechecked':sourcepins,'negative_controls_rerun':controls,'positive_controls_passed':3,'v1_review_preserved':{'path':str(old_report.relative_to(R)),'sha256':sha(old_report)},'v2_write_receipts':{'path':str((O/'write-receipts-v2.json').relative_to(R)),'sha256':sha(O/'write-receipts-v2.json')},'source_conclusions':prior['source_applicability'],'remaining_conditions':prior['remaining_conditions'],'new_findings':[],'repair_review_scope':'Root reported private-writer freshness defect and regenerated payloads. This review independently establishes exact new source payload bytes and absence of scientific/lineage-content drift. It does not independently certify private-writer freshness implementation; separate technical skeptical review must do so.','whole_owner_role_export_approval':False,'record_or_origin_edits_by_reviewer':False}
dump('final-byte-source-review-v2.json',report)
dump('final-byte-source-review-v2-receipt.json',{'reviewer':'/root/peptone_final_sources','completed_at':now,'status':report['status'],'report_path':str((D/'final-byte-source-review-v2.json').relative_to(R)),'report_sha256':sha(D/'final-byte-source-review-v2.json'),'script_sha256':sha(D/'review_final_bytes_v2.py'),'payloads':rows,'no_payload_or_origin_writes_performed':True})
print(json.dumps({'report_sha256':sha(D/'final-byte-source-review-v2.json'),'receipt_sha256':sha(D/'final-byte-source-review-v2-receipt.json'),'script_sha256':sha(D/'review_final_bytes_v2.py'),'positive':3,'negative':len(controls)},indent=2))
