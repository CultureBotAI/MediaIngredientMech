from pathlib import Path
import copy,datetime,hashlib,json,sys,yaml
sys.path.insert(0,'src')
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
R=Path('reports/all_unmatched_20261107/worker-06');V=R/'successor-v2';F=V/'final';O=V/'research-b'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
read=lambda p:json.loads(p.read_text())
expected={'decisions.json':'815ea3441a231f3d2464a57089338c7c78d07ac3f9c3f77e77f4865b39c01acd','proposals.json':'2244c896a5b1cf50681da7d7f15c4ccabae916aa31cc9e40e18b95d72e0dfd14','author-evidence.json':'271ab84a619850116f449bfc81da93d9c2be9e7e33a2f8079074537fe0e3e6a8','partonomy-correction.json':'70b1fe7f4dd1b04d3d56135ba8eb201a7528b31b99d7a9cb538b258460f95766'}
for n,h in expected.items():assert sha(F/n)==h
prior_binding=read(O/'final-binding.json')
for n,h in prior_binding['input_hashes'].items():assert sha(V/n)==h
D=read(F/'decisions.json')['decisions'];P=read(F/'proposals.json')['proposals'];E=read(F/'author-evidence.json')['evidence'];PD=read(V/'decisions.json')['decisions'];PP=read(V/'proposals.json')['proposals'];PE=read(V/'evidence.json')['evidence'];BD=read(R/'decisions.json')['decisions'];BP=read(R/'proposals.json')['proposals']
pi={x['proposal_id']:x for x in P};ppi={x['proposal_id']:x for x in PP};bpi={x['proposal_id']:x for x in BP};ei={x['evidence_id']:x for x in E};delta=read(F/'partonomy-correction.json');pre=read(O/'private.temp/merck-source-precheck.json')
pid='A-P-MERCK108339';p=pi[pid];oldp=ppi[pid];stock='V2-P-NBRC1308-1356-TRACE';ir='V2-IR-MERCK-LABEL'
assert len(D)==188 and len(P)==99 and len(ei)==len(E)==1065
assert [i for i,(a,b) in enumerate(zip(D,PD)) if a!=b]==[35,183]
assert [i for i,(a,b) in enumerate(zip(D,BD)) if a!=b]==[19,35,133,183]
assert [k for k in pi if pi[k]!=ppi[k]]==[pid]
assert len([k for k in pi if k in bpi and pi[k]==bpi[k]])==97
assert E[:len(PE)]==PE
assert pi[stock]==ppi[stock] and D[19]==PD[19] and D[133]==PD[133]
assert delta['original_proposal']==oldp and delta['new_capture']==p['after_capture']
oldpath=R/oldp['after_capture']['path'];newpath=R/p['after_capture']['path'];old=yaml.safe_load(oldpath.read_text());new=yaml.safe_load(newpath.read_text());assert sha(oldpath)==oldp['after_capture']['sha256'] and sha(newpath)==p['after_capture']['sha256']=='d6c9233bb2171f19ac51444d43581e80412a94893e0a381ab8c9acc0b72f72aa'
assert new['components'][2]['component_name']=='D-glucose' and old['components'][2]['component_name']=='D(+)Glucose'
assert new['component_assertion']['evidence'][0]['notes'].startswith(old['component_assertion']['evidence'][0]['notes'])
assert 'D(+)Glucose' in new['component_assertion']['evidence'][0]['notes'] and 'no anomer or hydrate is inferred' in new['component_assertion']['evidence'][0]['notes']
assert new['curation_history'][:-1]==old['curation_history'] and len(new['curation_history'])==len(old['curation_history'])+1
event=new['curation_history'][-1];assert event['action']=='CORRECTED' and event['llm_assisted'] and event['curator']=='all_unmatched_20261107_worker06_root'
assert datetime.datetime.fromisoformat(event['timestamp'])<=datetime.datetime.now(datetime.timezone.utc)
restored=copy.deepcopy(new);restored['components'][2]['component_name']=old['components'][2]['component_name'];restored['component_assertion']['evidence'][0]['notes']=old['component_assertion']['evidence'][0]['notes'];restored['curation_history']=old['curation_history'];assert restored==old
for i in [35,183]:
 d=D[i];prior=PD[i]
 assert set(k for k in d if d[k]!=prior.get(k))=={'evidence_ids','independent_review','prior_validation_decision_binding','successor_validation_correction'}
 assert d['evidence_ids'][:len(prior['evidence_ids'])]==prior['evidence_ids']
 assert d['independent_review']=={'status':'complete','evidence_ids':[ir]}
 assert d['prior_validation_decision_binding']['decision_sha256']==canon(prior)
 assert d['prior_validation_decision_binding']['prior_independent_review']==prior['independent_review']
 assert d['case_id'] in p['case_ids'] and d['proposal_ids']==[pid]
assert set(p['case_ids'])=={D[i]['case_id'] for i in [35,183]}
for e in E:
 c=e['capture'];base=R if c['root']=='artifact' else Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5');assert sha(base/c['path'])==c['sha256']
for x in P:assert sha(R/x['after_capture']['path'])==x['after_capture']['sha256']
targetpath=Path('data/ingredients/mapped/D-glucose.yaml');target=yaml.safe_load(targetpath.read_text());assert sha(targetpath)==pre['active_target']['sha256']
before=[vars(v) for v in validate_component_partonomy([target,old])];after=[vars(v) for v in validate_component_partonomy([target,new])]
assert len(before)==1 and before[0]['code']=='REFERENCE_LABEL_MISMATCH' and not after
report={'schema_version':1,'reviewer':'Codex /root/research_b','author_reviewed':'Codex /root','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'complete','open_findings':0,'input_hashes':expected,'input_root':'successor-v2/final','new_payload':p['after_capture'],'original_payload':oldp['after_capture'],'source_precheck':{'root':'artifact','path':'successor-v2/research-b/private.temp/merck-source-precheck.json','sha256':sha(O/'private.temp/merck-source-precheck.json')},'prior_snapshot_preservation':{'receipt_path':'successor-v2/research-b/final-binding.json','receipt_sha256':sha(O/'final-binding.json'),'all_bound_first99_inputs_unchanged':True,'stock_review_sha256':sha(O/'scientific-review.json'),'stock_payload_and_two_outcomes_unchanged':True},'scientific_assessment':'The full captured supplier composition explicitly states D(+)Glucose 20.0g/litre. The defining captured CHEBI17634 record labels the D-configuration substance D-glucose and lists D(+)-glucose. Using the canonical label for the already chosen CHEBI17634 reference is chemically consistent; the exact supplier spelling remains in component evidence. No hydrate, anomer, generic-glucose identity, changed amount or new global synonym is inferred. The prepared-broth quantity basis, peptone fractions, separate receiving-medium agar, UNKNOWN composition closure and historical-lot/current-typical limitations remain unchanged.','actual_delta':['/components/2/component_name: D(+)Glucose to D-glucose','/component_assertion/evidence/0/notes: original note retained and raw spelling/canonical-reference explanation appended','/curation_history: original history preserved and one actual root CORRECTED event appended'],'affected_case_reviews':[{'case_index':i,'case_id':D[i]['case_id'],'decision_sha256':canon(D[i]),'raw_source':D[i]['source'],'occurrence_ids':D[i]['occurrence_ids'],'assessment':('Both complete CM frozen recipes retain catalog108339 at30g/L and separate15g/L agar; the exact component change does not broaden either occurrence.' if i==35 else 'The complete frozen KG context and primary medium1429 explicitly qualify ingredient1279 as Merck108339,2%; raw generic label alone is not treated as an alias for the catalog product. No measured occurrence frequency or downstream approval is invented.')} for i in [35,183]],'findings':[{'finding_id':'V2-B-MERCK-01','status':'resolved','finding':'Full-catalog overlay exposed an inherited exact-reference-label mismatch for supplier D(+)Glucose. Baseline passed; both original100 and initial99 overlays reproduced the same single failure.','resolution':'The final isolated proposal uses the canonical label of the existing D-specific component identifier, retains the raw supplier wording and all substantive product fields, and preserves failed receipts. The focused actual-payload native check now reports zero violations.'}],'focused_check':{'module':'src/mediaingredientmech/validation/component_partonomy.py','module_sha256':sha(Path('src/mediaingredientmech/validation/component_partonomy.py')),'scope':'Read-only in-memory original/corrected Merck parent with actual maintained D-glucose target; not full-catalog validation','target_sha256':sha(targetpath),'before_violations':before,'after_violations':after},'selection_check':{'case_count':188,'proposal_count':99,'unchanged_decisions_vs_published':184,'unchanged_proposals_vs_published':97,'unchanged_decisions_vs_initial99':186,'unchanged_proposals_vs_initial99':98,'all_author_evidence_capture_hashes':'PASS','all_selected_payload_hashes':'PASS'},'independence':'Reviewer did not author either original Merck proposal or root successor correction. A source assessment was read as original-author contribution, not independent approval. B independently reread full supplier and ontology captures, both complete CM frozen recipes and complete KG context; prior B-authored science is not self-approved.','final_evidence_binding':'Pending final-binding-v2.json after this actual receipt is appended as V2-IR-MERCK-LABEL. No self-containing final evidence hash is claimed.','source_owner_export_approval':False,'maintained_change_approval':False}
for n,h in expected.items():assert sha(F/n)==h
out=O/'merck-label-delta-review.json';out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'path':str(out),'sha256':sha(out),'status':report['status'],'open_findings':report['open_findings']}))
