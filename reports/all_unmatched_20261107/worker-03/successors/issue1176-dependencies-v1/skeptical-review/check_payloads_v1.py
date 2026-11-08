from pathlib import Path
import json,yaml,hashlib,copy,sys,datetime
R=Path.cwd();O=R/'.temp/peptone-final-dependencies-v1';S=O/'skeptical-review';sys.path.insert(0,str(R/'src'))
from mediaingredientmech.validation.write_validated import validate_ingredient
sha=lambda b:hashlib.sha256(b).hexdigest()
can=lambda x:json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
plan=json.loads((O/'author-plan-v2.json').read_text());results=[]
expected={'GYPS':'ad9fdcf66ef72672060106af433a32583df72252adae2fb5521b03a696a23725','PYGS':'f95aa34b0872db40d4f2d08918105b54db401e7fa8cf4409e08258b2df936312','Marine_agar_2216':'ed61879570d90b147ee7ed7767b7a900738b1cf010c73e596ba8d7f161490082'}
def leaves(x):
 if isinstance(x,dict):return sum(leaves(v) for v in x.values())
 if isinstance(x,list):return sum(leaves(v) for v in x)
 return 1
for r in plan['rows']:
 name=Path(r['owner_path']).stem;p=O/'payloads'/f'{name}.yaml';raw=p.read_bytes();assert sha(raw)==expected[name]
 src=O/r['current_payload']['path'];oldraw=src.read_bytes();assert sha(oldraw)==r['current_payload']['sha256'];old=yaml.safe_load(oldraw);new=yaml.safe_load(raw)
 before=O/r['maintained_before']['path'];assert before.read_bytes()==(R/r['owner_path']).read_bytes()
 i=r['component_index'];n=len(r['append_evidence']);assert new['components'][i]==r['new_component'];assert new['component_assertion']['evidence'][-n:]==r['append_evidence'];assert new['curation_history'][:-1]==old['curation_history'];event=new['curation_history'][-1]
 assert event['curator']=='codex-worker03 /root dependent-origin author' and event['llm_assisted'] is True and event['changes']==r['event_text']
 assert event['previous_status']==event['new_status']==old['mapping_status']
 restored=copy.deepcopy(new);restored['components'][i]=old['components'][i];restored['component_assertion']['evidence']=restored['component_assertion']['evidence'][:-n];restored['curation_history'].pop();assert restored==old
 for j,(a,b) in enumerate(zip(old['components'],new['components'])):
  assert {k:v for k,v in a.items() if k.startswith('concentration') or k=='proportion'}=={k:v for k,v in b.items() if k.startswith('concentration') or k=='proportion'}
 errors=validate_ingredient(new);assert not errors,errors
 results.append({'dependency_id':r['dependency_id'],'owner_path':r['owner_path'],'payload_path':str(p.relative_to(R)),'payload_sha256':sha(raw),'predecessor_sha256':sha(oldraw),'maintained_before_sha256':sha(before.read_bytes()),'component_index':i,'before_component':old['components'][i],'after_component':new['components'][i],'added_evidence_objects':n,'history_events_appended':1,'history_prefix_unchanged':True,'unchanged_projection_sha256':sha(can(restored)),'top_level_fields_read':len(new),'leaf_fields_read':leaves(new),'all_other_fields_equal_predecessor':True,'all_quantity_fields_unchanged':True,'native_closed_schema_errors':0,'new_event':event})
obj={'reviewer':'/root/peptone_final_skeptic','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'All complete actual3payloads read; positive assessment limited to bounded peptone correction plus exact preservation of unrelated prior fields, not independent whole-owner chemistry/role/export approval.','status':'THREE_PAYLOAD_SCIENTIFIC_DELTAS_SUPPORTED_WITH_CONDITIONS_PRODUCER_GUARD_FINDING_PENDING','source_inspection':'primary-skeptical-assessment-v1.json and raw-source-readback-v1.json','rows':results,'counts':{'payloads':3,'components_retained':sum(len(yaml.safe_load((O/'payloads'/f'{n}.yaml').read_text())['components']) for n in expected),'appended_component_evidence':5,'appended_history':3,'top_level_fields':sum(x['top_level_fields_read'] for x in results),'leaf_fields':sum(x['leaf_fields_read'] for x in results)},'known_conditions':['PYGS and Marine require separately accepted exact generic parent c083794668a362203de6430eaa2609c34cd8ef78574a1230aa25b4a64fb55fd7.','GYPS preserves existing Bacto reference conditionally; Bacto whole identity/mapping must be separately retained/accepted. No source proof supports generic mesh substitution.','W04/W06 source origins remain foreign predecessor authors, W03 only dependent edit author; GYPS is genuine incoming dependency, no frozen child case invented.','Native core ingestion route and finalrootapplication need distinct review; final37notapproved here.','FAB remains Oxoid and all other peptone withdrawals untouched.'],'new_findings':['W03-PEPTONE-GUARD-001 affects producer input-freshness controls, not the source support of these actual pinned bytes.']}
p=S/'payload-source-readback-v1.json';assert not p.exists();p.write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj['counts']));print(sha(p.read_bytes()))
