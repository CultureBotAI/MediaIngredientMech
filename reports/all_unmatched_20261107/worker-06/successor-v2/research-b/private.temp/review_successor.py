"""Independent source-science and successor-selection review; no maintained mutation."""
from pathlib import Path
import json, hashlib, datetime, subprocess, yaml
R=Path('reports/all_unmatched_20261107/worker-06'); V=R/'successor-v2'; O=V/'research-b'
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
H='d5a7613c931d45d057eaca7b5ec15280aca76c9e'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
D=json.loads((V/'decisions.json').read_text())['decisions']; P=json.loads((V/'proposals.json').read_text())['proposals']; E=json.loads((V/'author-evidence.json').read_text())['evidence']; L=json.loads((V/'lineage.json').read_text())
BD=json.loads((R/'decisions.json').read_text())['decisions']; BP=json.loads((R/'proposals.json').read_text())['proposals']; BE=json.loads((R/'evidence.json').read_text())['evidence']; S=json.loads((Q/'shards/shard-06.json').read_text())['cases']
assert sha(V/'decisions.json')=='5cabffc9e9f99ff0fa4b069c1f9c5575649aff0ba3437d1f96f557c276290f00'
assert sha(V/'proposals.json')=='11f9ded7530efcf857c7564a9f8b9685847497beb5142318f519c1a8843279d7'
di={x['case_id']:x for x in D}; bi={x['case_id']:x for x in BD}; pi={x['proposal_id']:x for x in P}; bpi={x['proposal_id']:x for x in BP}; ei={x['evidence_id']:x for x in E}
newid='V2-P-NBRC1308-1356-TRACE'; retired={'A-P-NBRC1308-TRACE','C-P-NBRC1356-TRACE'}; p=pi[newid]
assert len(D)==len(di)==len(BD)==188 and len(P)==len(pi)==99 and len(BP)==100
assert set(bpi)-set(pi)==retired and set(pi)-set(bpi)=={newid}
changed=[i for i,s in enumerate(S) if di[s['case_id']]!=bi[s['case_id']]];assert changed==[19,133]
assert all(pi[k]==bpi[k] for k in set(pi)&set(bpi)) and len(set(pi)&set(bpi))==98
assert all(ei[e['evidence_id']]==e for e in BE)
case_rows=[];payload_rows=[]
for i,s in enumerate(S):
 d=di[s['case_id']];assert d['case_input_sha256']==canon(s)
 assert d['source']=={k:s[k] for k in ['source','source_case_id','source_label','raw_source_label']}
 assert set(d['occurrence_ids'])=={z['occurrence_id'] for z in s.get('occurrences',[])}
 assert all(s['case_id'] in pi[pid]['case_ids'] for pid in d['proposal_ids'])
 assert not retired&set(d['proposal_ids'])
 assert all(e in ei for e in d['evidence_ids'])
 assert all(e in ei or e=='V2-IR-NBRC1308-1356' for e in d['independent_review']['evidence_ids'])
 case_rows.append({'case_index':i,'case_id':s['case_id'],'original_case_sha256':canon(s),'selected_decision_sha256':canon(d),'unchanged_from_original':i not in changed,'original_occurrence_ids_preserved':True,'selected_proposal_ids':d['proposal_ids']})
for row in P:
 assert all(row['proposal_id'] in di[c]['proposal_ids'] for c in row['case_ids'])
 assert all(e in ei for e in row['evidence_ids'])
 cap=row['after_capture'];assert sha(R/cap['path'])==cap['sha256']
 payload_rows.append({'proposal_id':row['proposal_id'],'after_capture':cap,'unchanged_original_object_and_bytes':row['proposal_id']!=newid})
for e in E:
 cap=e['capture'];assert sha((R if cap['root']=='artifact' else Q)/cap['path'])==cap['sha256'],e['evidence_id']
for n in ['decisions.json','evidence.json','proposals.json','source-holds.json','SHA256SUMS']:
 f=R/n;assert f.read_bytes()==subprocess.check_output(['git','show',H+':'+str(f)])
old_diff=subprocess.check_output(['git','diff','--name-only',H,'--',str(R),':!'+str(V)]).decode().splitlines();assert not old_diff
path=R/p['after_capture']['path'];assert sha(path)=='194d39c6301961eba8719f01d02762effb19c1b4a7fdfac247210f41c038127c';y=yaml.safe_load(path.read_text())
expected=[('Nitrilotriacetic acid (NTA)','12.8'),('FeCl3·6H2O','1.35'),('MnCl2·4H2O','0.1'),('CoCl2·6H2O','0.024'),('CaCl2·2H2O','0.1'),('ZnCl2','0.1'),('CuCl2·2H2O','0.025'),('H3BO3','0.01'),('Na2MoO4·2H2O','0.024'),('NaCl','1'),('NiCl2·6H2O','0.12'),('Na2SeO4','0.004'),('Na2WO4','0.004')]
assert [(z['component_name'],z['concentration_value']) for z in y['components'][:13]]==expected
assert all(z['concentration_unit']=='G' and z['reference_scope']=='UNMAPPED' for z in y['components'][:13])
assert y['components'][13]=={'component_name':'Distilled water','reference_scope':'UNMAPPED','concentration_value':'1','concentration_unit':'L'}
assert y['components'][14]=={'component_name':'NaOH','reference_scope':'UNMAPPED'} and len(y['components'])==15
assert y['component_assertion']['completeness']=='UNKNOWN' and not y.get('synonyms')
assert y['ontology_mapping']['ontology_id']==y['identifier'] and y['ontology_mapping']['mapping_quality']=='FALLBACK_REGISTRY'
assert all(z['evidence_type']=='CURATOR_JUDGMENT' for z in y['ontology_mapping']['evidence'])
assert len(y['curation_history'])==1 and y['curation_history'][0]['action']=='CREATED' and y['curation_history'][0]['llm_assisted']
catalog=[]
for f in Path('data/ingredients').rglob('*.yaml'):
 z=yaml.safe_load(f.read_text());catalog.append((str(f),z.get('identifier')))
assert not [f for f,i in catalog if i==y['identifier']]
assert not Path(p['owner_path']).exists()
included={S[19]['occurrences'][1]['occurrence_id'],S[133]['occurrences'][0]['occurrence_id']};excluded={S[19]['occurrences'][0]['occurrence_id'],S[19]['occurrences'][2]['occurrence_id']}
assert set(p['applicable_occurrence_ids'])==included and set(p['excluded_occurrence_ids'])==excluded
assert set(p['case_ids'])=={S[19]['case_id'],S[133]['case_id']}
for i in [19,133]:
 cid=S[i]['case_id'];sc=p['occurrence_scopes_by_case'][cid];assert not set(sc['included_occurrence_ids'])&set(sc['excluded_occurrence_ids']);assert set(sc['included_occurrence_ids'])|set(sc['excluded_occurrence_ids'])==set(di[cid]['occurrence_ids'])
 assert di[cid]['prior_decision_binding']['decision_sha256']==canon(bi[cid])
 assert di[cid]['prior_decision_binding']['prior_independent_review']==bi[cid]['independent_review']
assert set(pi['A-P-NBRC1020-824-TRACE']['applicable_occurrence_ids'])==excluded
assert L['published_parent_commit']==H and L['successor_author']=='/root' and not L['maintained_merge']
for z in L['original_proposals']:
 old=z['proposal_object'];assert old==bpi[old['proposal_id']] and canon(old)==z['proposal_object_sha256']
 oldpath=R/old['after_capture']['path'];oy=yaml.safe_load(oldpath.read_text());assert sha(oldpath)==old['after_capture']['sha256'];assert oldpath.read_bytes()==subprocess.check_output(['git','show',H+':'+str(oldpath)])
 assert oy['curation_history']==z['original_curation_history'] and oy['identifier']==z['original_identifier'];cap=z['prior_independent_review'];assert sha(R/cap['path'])==cap['sha256']
assert {z['proposal_object']['proposal_id'] for z in L['original_proposals']}==retired
pre=json.loads((O/'private.temp/source-precheck.json').read_text())
findings=[
{'id':'V2-B-01','status':'resolved','severity':'major','finding':'Two earlier proposals represented the same nominal formulation under different local identifiers. The earlier per-payload reviews did not detect this cross-author duplication.','resolution':'The successor selects one root-authored formulation identity after full source comparison, retaining both immutable original proposal/history/reviewer lineages. No maintained owner is merged.'},
{'id':'V2-B-02','status':'resolved','severity':'major','finding':'Case19 includes two unrelated NBRC1020/824 occurrences under the same generic double-star label.','resolution':'The new proposal includes only1308 from case19 and1356 from case133; the two excluded occurrences retain their unchanged separate NTA/KOH proposal. All four frozen occurrence IDs and raw labels survive.'},
{'id':'V2-B-03','status':'resolved','severity':'major','finding':'Equal nominal formulation does not establish identical source processing or final chemical endpoints.','resolution':'New payload and outcomes explicitly preserve1308 one-ml autoclaved receiving mixture under80/20N2/CO2 versus1356 ten-ml filter-sterile stock inN2 handling; no endpoint equivalence is asserted.'},
{'id':'V2-B-04','status':'resolved','severity':'major','finding':'Neither printed1L water nor namedNaOH establishes a precise final volume or quantitative titrant input; finalpH7 is a condition without an explicit readjustment reagent.','resolution':'Payload retains13solutes as grams,1L water as input, unquantifiedNaOH, unspecified forms, and UNKNOWN completeness for uncertain final adjustment. It adds no global raw-label alias or child chemical mapping.'}]
report={'schema_version':1,'reviewer':'Codex /root/research_b','author_reviewed':'Codex /root','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'complete','open_findings':0,'scope':{'scientific_case_indices':[19,133],'affected_case_occurrences':4,'reconciled_stock_occurrences':2,'excluded_case19_occurrences':2,'selected_cases':188,'selected_proposals':99,'unchanged_decisions':186,'unchanged_selected_proposal_objects_and_payloads':98},'input_hashes':{n:sha(V/n) for n in ['decisions.json','proposals.json','author-evidence.json','lineage.json']},'new_payload':p['after_capture'],'original_published_commit':H,'source_precheck':{'path':'successor-v2/research-b/private.temp/source-precheck.json','sha256':sha(O/'private.temp/source-precheck.json')},'primary_sources':[{k:v for k,v in z.items() if k!='full_text_read'} for z in pre['primary_tables_read_in_full']],'scientific_assessment':'Independent complete-source inspection establishes equality of all13 listed solute masses, water input and NTA-first NaOH/pH preparation. Differing accession, star count, quantity metadata or closure label is not a substance distinction. The joint local registry identity is justified for the shared nominal stock only. Source processing/dose, unspecified final pH adjustment, water basis and unqualified hydrates remain explicit. The new record does not identify final post-processing speciation, promote child identities or release source claims.','identity_search':{'maintained_exact_identifier_collision_check':'No collision in pathlib-recursed individual maintained YAML, including ignored files','individual_records_checked':len(catalog),'semantic_owner_search_receipt':L['existing_owner_search'],'assessment':'The independently supplied maintained-owner search distinguishes defined NTA stocks by ligand amount, metals/counterions, Se/W/alum and preparation. Undecomposed generic trace owners lack positive evidence of this exact stock; they are not selected as winners.'},'findings':findings,'affected_case_reviews':[{'case_index':i,'case_id':S[i]['case_id'],'decision_sha256':canon(di[S[i]['case_id']]),'assessment':('Allthree original casescope occurrences are retained; only1308 selects the reconciled stock and1020/824 remain separate.' if i==19 else 'The sole1356 occurrence selects the same nominal formulation with its10ml filter-sterile/N2 source use retained.'),'occurrence_ids':di[S[i]['case_id']]['occurrence_ids']} for i in [19,133]],'all_case_selection_checks':case_rows,'all_selected_payload_checks':payload_rows,'checks':{'full_primary_tables_and_four_frozen_contexts':'PASS','source_quantities_forms_preparation_and_raw_scope':'PASS','new_payload_identity_alias_and_completeness':'PASS','both_original_author_histories_and_reviews':'PASS','all188_original_input_digests_occurrences_and_links':'PASS','unchanged186_decisions_and98_selected_payloads':'PASS','original100_ledger_and_payload_preservation':'PASS','author_evidence_capture_hashes':'PASS'},'independence':'Reviewer did not author the new root payload or either original A/C payload. Previous B review of C1356 is preserved as historical lineage, not used to self-approve a new authored record. Source judgments here are independently reread from full primary and frozen bytes. Unchanged B-authored campaign payload science remains bound to its separate A review; this successor check does not self-approve it.','final_evidence_binding':'Pending separately written final-binding.json after coordinator adds this actual receipt as V2-IR-NBRC1308-1356; no circular self-containing evidence hash claimed.','scientific_release_approval':False,'maintained_owner_merge_approved':False}
for n,oldhash in report['input_hashes'].items():assert sha(V/n)==oldhash
out=O/'scientific-review.json';out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'path':str(out),'sha256':sha(out),'input_hashes':report['input_hashes'],'scope':report['scope']}))
