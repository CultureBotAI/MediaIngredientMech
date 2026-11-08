from pathlib import Path
import datetime,hashlib,json,subprocess
R=Path('reports/all_unmatched_20261107/worker-06');V=R/'successor-v2';F=V/'final';O=V/'research-b'
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5');H='d5a7613c931d45d057eaca7b5ec15280aca76c9e'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
read=lambda p:json.loads(p.read_text())
expected={'decisions.json':'815ea3441a231f3d2464a57089338c7c78d07ac3f9c3f77e77f4865b39c01acd','proposals.json':'2244c896a5b1cf50681da7d7f15c4ccabae916aa31cc9e40e18b95d72e0dfd14','evidence.json':'3abee21eb759145e210d5fa5ee3f77fcc3aba0bc0c71eccde35d9b890022fec3','author-evidence.json':'271ab84a619850116f449bfc81da93d9c2be9e7e33a2f8079074537fe0e3e6a8','selection.json':'4d716bee7fafb8fe081e1604da305d8ecfd0c05fc3e40bcdf3aa6ba0cd0d157a','source-holds.json':'eaddfd7ffe5ba2ba1be011696ad741e1b010db2cc9ca4678954a640484f70b77','partonomy-correction.json':'70b1fe7f4dd1b04d3d56135ba8eb201a7528b31b99d7a9cb538b258460f95766'}
for n,h in expected.items():assert sha(F/n)==h
first=read(O/'final-binding.json');assert sha(O/'final-binding.json')=='a9493ba6e9607894cdcf2a976209b3203b3147af8c5100366a7203098839452e'
for n,h in first['input_hashes'].items():assert sha(V/n)==h
stock_review=read(O/'scientific-review.json');merck_review=read(O/'merck-label-delta-review.json')
assert sha(O/'scientific-review.json')=='f82cdd0841cf518c0e11e56c7a281f57e1e80e15f107c5f88ed6a8508710b5c2'
assert sha(O/'merck-label-delta-review.json')=='1cc8b3643bcd93f6d29b14e7eb8207593f24979486a36644c541e7daf63e13a1'
for review,base in [(stock_review,V),(merck_review,F)]:
 assert review['status']=='complete' and review['open_findings']==0
 for n,h in review['input_hashes'].items():assert sha(base/n)==h
D=read(F/'decisions.json')['decisions'];P=read(F/'proposals.json')['proposals'];E=read(F/'evidence.json')['evidence'];AE=read(F/'author-evidence.json')['evidence'];sel=read(F/'selection.json');PD=read(V/'decisions.json')['decisions'];PP=read(V/'proposals.json')['proposals'];BD=read(R/'decisions.json')['decisions'];BP=read(R/'proposals.json')['proposals'];BE=read(R/'evidence.json')['evidence'];S=read(Q/'shards/shard-06.json')['cases']
di={x['case_id']:x for x in D};pi={x['proposal_id']:x for x in P};ppi={x['proposal_id']:x for x in PP};bpi={x['proposal_id']:x for x in BP};ei={x['evidence_id']:x for x in E}
assert len(D)==len(di)==188 and len(P)==len(pi)==99 and len(E)==len(ei)==1066
assert E[:-1]==AE and E[-1]['evidence_id']=='V2-IR-MERCK-LABEL'
assert len(BE)==1056 and all(ei[e['evidence_id']]==e for e in BE)
assert [i for i,(a,b) in enumerate(zip(D,BD)) if a!=b]==[19,35,133,183]
assert [i for i,(a,b) in enumerate(zip(D,PD)) if a!=b]==[35,183]
assert len([k for k in pi if k in bpi and pi[k]==bpi[k]])==97
assert [k for k in pi if pi[k]!=ppi[k]]==['A-P-MERCK108339']
assert set(bpi)-set(pi)=={'A-P-NBRC1308-TRACE','C-P-NBRC1356-TRACE'} and set(pi)-set(bpi)=={'V2-P-NBRC1308-1356-TRACE'}
for key,ir in [('trace_reconciliation','V2-IR-NBRC1308-1356'),('necessary_validation_correction','V2-IR-MERCK-LABEL')]:
 c=sel[key];assert c['after_capture']==pi[c['proposal_id']]['after_capture'];assert c['case_ids']==pi[c['proposal_id']]['case_ids'];assert c['independent_receipt']==ei[ir]['capture'];assert sha(R/c['independent_receipt']['path'])==c['independent_receipt']['sha256']
for n,c in sel['current_intake'].items():assert c['path']==str(F/n) and sha(Path(c['path']))==c['sha256']==expected[n]
assert not sel['source_owner_export_approval'] and not sel['maintained_owner_merge']
assert sel['retained_unchanged_proposal_count']==97 and sel['retained_unchanged_case_count']==184
assert sel['trace_reconciliation']['occurrence_scopes_by_case']==pi['V2-P-NBRC1308-1356-TRACE']['occurrence_scopes_by_case']
case_rows=[];payload_rows=[]
for i,s in enumerate(S):
 d=di[s['case_id']];assert d['case_input_sha256']==canon(s);assert d['source']=={k:s[k] for k in ['source','source_case_id','source_label','raw_source_label']};assert set(d['occurrence_ids'])=={o['occurrence_id'] for o in s.get('occurrences',[])}
 assert d['independent_review']['status']=='complete' and all(e in ei for e in d['evidence_ids']+d['independent_review']['evidence_ids'])
 assert all(d['case_id'] in pi[p]['case_ids'] for p in d['proposal_ids'])
 case_rows.append({'case_index':i,'case_id':d['case_id'],'decision_sha256':canon(d),'unchanged_from_published_original':i not in [19,35,133,183],'independent_review_ids':d['independent_review']['evidence_ids']})
for p in P:
 c=p['after_capture'];assert sha(R/c['path'])==c['sha256'];assert all(p['proposal_id'] in di[i]['proposal_ids'] for i in p['case_ids']);assert all(e in ei for e in p['evidence_ids']+p.get('independent_review',{}).get('evidence_ids',[]))
 payload_rows.append({'proposal_id':p['proposal_id'],'after_capture':c,'unchanged_from_published_original':p['proposal_id'] in bpi and p==bpi[p['proposal_id']]})
for e in E:
 c=e['capture'];assert c['root'] in ['artifact','source'];assert sha((R if c['root']=='artifact' else Q)/c['path'])==c['sha256'],e['evidence_id']
sp=pi['V2-P-NBRC1308-1356-TRACE'];assert sp==ppi[sp['proposal_id']]
assert sp['after_capture']==stock_review['new_payload']
assert set(sp['applicable_occurrence_ids'])=={S[19]['occurrences'][1]['occurrence_id'],S[133]['occurrences'][0]['occurrence_id']}
assert set(sp['excluded_occurrence_ids'])==set(pi['A-P-NBRC1020-824-TRACE']['applicable_occurrence_ids'])
assert pi['A-P-MERCK108339']['after_capture']==merck_review['new_payload']
manifest=R/'SHA256SUMS';assert manifest.read_bytes()==subprocess.check_output(['git','show',H+':'+str(manifest)]);manifest_count=0
for line in manifest.read_text().splitlines():
 h,n=line.split('  ',1);assert sha(Path(n))==h,n;manifest_count+=1
for n in ['decisions.json','evidence.json','proposals.json','source-holds.json']:
 p=R/n;assert p.read_bytes()==subprocess.check_output(['git','show',H+':'+str(p)])
for p in BP:
 c=p['after_capture'];path=R/c['path'];assert sha(path)==c['sha256'];assert path.read_bytes()==subprocess.check_output(['git','show',H+':'+str(path)])
assert (F/'source-holds.json').read_bytes()==(V/'source-holds.json').read_bytes()==(R/'source-holds.json').read_bytes();assert read(F/'source-holds.json')['downstream_hold_row_count']==88
assert not subprocess.check_output(['git','diff','--name-only',H,'--',str(R),':!'+str(V)]).strip()
out={'schema_version':1,'reviewer':'Codex /root/research_b','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'complete','open_binding_findings':0,'scope':'Final authoritative successor intake under successor-v2/final, after stock reconciliation and source-backed Merck component-label correction. Exact scientific receipts and full188-case structural/provenance bindings; full validator outcomes remain separate.','authoritative_selection':{'path':str(F/'selection.json'),'sha256':expected['selection.json']},'input_root':'successor-v2/final','input_hashes':expected,'scientific_reviews':[sel['trace_reconciliation']['independent_receipt'],sel['necessary_validation_correction']['independent_receipt']],'historical_binding_preserved':{'path':'successor-v2/research-b/final-binding.json','sha256':sha(O/'final-binding.json'),'all_bound_first99_inputs_unchanged':True},'published_original_commit':H,'counts':{'selected_cases':188,'selected_proposals':99,'evidence':1066,'original_evidence_entries_preserved':1056,'unchanged_cases_from_published':184,'unchanged_selected_proposals_from_published':97,'original_payload_bytes_preserved':100,'original_manifest_files_preserved':manifest_count,'downstream_hold_rows_preserved':88},'checks':{'both_actual_independent_receipts_in_final_evidence':'PASS','final_evidence_equals_author_evidence_plus_actual_merck_review':'PASS','all188_frozen_case_digests_raw_labels_occurrences_backlinks':'PASS','all99_selected_payload_hashes_and_case_backlinks':'PASS','all1066_evidence_capture_hashes':'PASS','stock_exact_payload_outcomes_and_occurrence_partition_unchanged':'PASS','merck_exact_reviewed_delta_and_two_outcomes':'PASS','original100_and_first99_inputs_and_receipts_preserved':'PASS','all88_source_holds_unchanged':'PASS','only_final_selection_names_authoritative_intake':'PASS'},'all_case_bindings':case_rows,'all_payload_bindings':payload_rows,'limitations':['This exact-binding check does not claim full-catalog or schema checks passed; those actual commands and statuses are separately retained by the coordinator. Earlier original100 and initial99 partonomy failures remain historical evidence.','Scientific review is new only for the two reconciled-stock cases and two bounded Merck-label cases. The remaining184 decisions and97 payloads retain original review evidence; B-authored campaign science is not self-approved.','Nominal stock formulation equality does not establish equal post-sterilization speciation; source-specific doses, processing and unknown final adjustment/volume remain.','Current Merck typical formulation is not a historical-lot or generic family identity claim. Source-case, whole-owner, export release and maintained installation remain unapproved.'],'scientific_release_approval':False,'maintained_owner_merge_approved':False}
for n,h in expected.items():assert sha(F/n)==h
p=O/'final-binding-v2.json';p.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'path':str(p),'sha256':sha(p),'status':out['status'],'counts':out['counts']}))
