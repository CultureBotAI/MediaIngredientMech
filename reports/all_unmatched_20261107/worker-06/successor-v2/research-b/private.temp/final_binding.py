"""Bind final successor intake without modifying its scientific review."""
from pathlib import Path
import datetime, hashlib, json, subprocess
R=Path('reports/all_unmatched_20261107/worker-06'); V=R/'successor-v2'; O=V/'research-b'
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
H='d5a7613c931d45d057eaca7b5ec15280aca76c9e'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
read=lambda p:json.loads(p.read_text())
expected={'decisions.json':'5cabffc9e9f99ff0fa4b069c1f9c5575649aff0ba3437d1f96f557c276290f00','proposals.json':'11f9ded7530efcf857c7564a9f8b9685847497beb5142318f519c1a8843279d7','evidence.json':'81fa2bec01e1bdbd84c04fa6e5d44c94ebd73c4d9829eadc26165eb10d165115','author-evidence.json':'57f6d80b57eb39f98d36a6286412336430605ef79670e78d30e7ce558571b8e5','lineage.json':'35ebf1795329c3c64233982cf463433e57b1d9cc8af871bf3c34725f330989d8','selection.json':'b4f413cc9ccaf144cd3c6f92d857a0afeae227836b2ee17466dd705665f06c41','source-holds.json':'eaddfd7ffe5ba2ba1be011696ad741e1b010db2cc9ca4678954a640484f70b77','research-b/scientific-review.json':'f82cdd0841cf518c0e11e56c7a281f57e1e80e15f107c5f88ed6a8508710b5c2'}
for name,digest in expected.items(): assert sha(V/name)==digest,name
D=read(V/'decisions.json')['decisions']; P=read(V/'proposals.json')['proposals']; E=read(V/'evidence.json')['evidence']; AE=read(V/'author-evidence.json')['evidence']; selection=read(V/'selection.json'); review=read(O/'scientific-review.json')
BD=read(R/'decisions.json')['decisions']; BP=read(R/'proposals.json')['proposals']; BE=read(R/'evidence.json')['evidence']; S=read(Q/'shards/shard-06.json')['cases']
di={x['case_id']:x for x in D}; bi={x['case_id']:x for x in BD}; pi={x['proposal_id']:x for x in P}; bpi={x['proposal_id']:x for x in BP}; ei={x['evidence_id']:x for x in E}
assert len(D)==len(di)==188 and len(P)==len(pi)==99 and len(E)==len(ei)==1062
ir='V2-IR-NBRC1308-1356'; new='V2-P-NBRC1308-1356-TRACE'; retired={'A-P-NBRC1308-TRACE','C-P-NBRC1356-TRACE'}
assert E[:-1]==AE and E[-1]['evidence_id']==ir
assert all(ei[x['evidence_id']]==x for x in BE) and len(BE)==1056
assert ei[ir]['capture']==selection['independent_receipt']=={'root':'artifact','path':'successor-v2/research-b/scientific-review.json','sha256':expected['research-b/scientific-review.json']}
assert review['status']=='complete' and review['open_findings']==0 and not review['scientific_release_approval']
for name,digest in review['input_hashes'].items():assert sha(V/name)==digest
for name,cap in selection['current_intake'].items():assert cap['path']==str(V/name) and sha(Path(cap['path']))==cap['sha256']==expected[name]
assert selection['reconciled_proposal']==pi[new] and selection['proposal_count']==99 and selection['case_count']==188
assert not selection['source_owner_export_approval'] and not selection['maintained_owner_merge']
assert set(bpi)-set(pi)==retired and set(pi)-set(bpi)=={new}
assert [i for i,s in enumerate(S) if di[s['case_id']]!=bi[s['case_id']]]==[19,133]
case_rows=[]
for i,s in enumerate(S):
 d=di[s['case_id']]
 assert d['case_input_sha256']==canon(s)
 assert d['source']=={k:s[k] for k in ['source','source_case_id','source_label','raw_source_label']}
 assert set(d['occurrence_ids'])=={o['occurrence_id'] for o in s.get('occurrences',[])}
 assert d['independent_review']['status']=='complete'
 assert all(e in ei for e in d['evidence_ids']+d['independent_review']['evidence_ids'])
 assert all(d['case_id'] in pi[p]['case_ids'] for p in d['proposal_ids'])
 assert not retired&set(d['proposal_ids'])
 if i in [19,133]:assert ir in d['independent_review']['evidence_ids']
 case_rows.append({'case_index':i,'case_id':d['case_id'],'decision_sha256':canon(d),'unchanged_from_published_original':i not in [19,133]})
payload_rows=[]
for p in P:
 assert all(p['proposal_id'] in di[c]['proposal_ids'] for c in p['case_ids'])
 assert all(e in ei for e in p['evidence_ids'])
 assert all(e in ei for e in p.get('independent_review',{}).get('evidence_ids',[]))
 cap=p['after_capture']; assert sha(R/cap['path'])==cap['sha256']
 if p['proposal_id']!=new:assert p==bpi[p['proposal_id']]
 payload_rows.append({'proposal_id':p['proposal_id'],'after_capture':cap,'unchanged_from_published_original':p['proposal_id']!=new})
assert review['new_payload']==pi[new]['after_capture']
assert set(pi[new]['applicable_occurrence_ids'])=={S[19]['occurrences'][1]['occurrence_id'],S[133]['occurrences'][0]['occurrence_id']}
assert set(pi[new]['excluded_occurrence_ids'])==set(pi['A-P-NBRC1020-824-TRACE']['applicable_occurrence_ids'])
for e in E:
 c=e['capture']; assert c['root'] in ['artifact','source'];assert sha((R if c['root']=='artifact' else Q)/c['path'])==c['sha256'],e['evidence_id']
manifest=R/'SHA256SUMS';assert manifest.read_bytes()==subprocess.check_output(['git','show',H+':'+str(manifest)])
manifest_rows=[]
for line in manifest.read_text().splitlines():
 digest,name=line.split('  ',1);p=Path(name);assert sha(p)==digest,name;manifest_rows.append({'path':name,'sha256':digest})
for name in ['decisions.json','evidence.json','proposals.json','source-holds.json']:
 p=R/name;assert p.read_bytes()==subprocess.check_output(['git','show',H+':'+str(p)])
for p in BP:
 cap=p['after_capture']; path=R/cap['path'];assert sha(path)==cap['sha256'];assert path.read_bytes()==subprocess.check_output(['git','show',H+':'+str(path)])
assert (V/'source-holds.json').read_bytes()==(R/'source-holds.json').read_bytes()
holds=read(V/'source-holds.json');assert holds['downstream_hold_row_count']==88 and holds['case_count']==188
assert not subprocess.check_output(['git','diff','--name-only',H,'--',str(R),':!'+str(V)]).strip()
report={'schema_version':1,'reviewer':'Codex /root/research_b','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'complete','open_binding_findings':0,'scope':'Final successor intake selection and evidence bindings; scientific assessment is immutable in the separately linked receipt. This check does not certify all downstream validators or release approval.','input_hashes':expected,'scientific_review':selection['independent_receipt'],'published_original_commit':H,'counts':{'selected_decisions':len(D),'selected_proposals':len(P),'final_evidence':len(E),'unchanged_original_evidence':len(BE),'unchanged_decisions':186,'unchanged_selected_proposal_objects_and_bytes':98,'original_payload_bytes_preserved':len(BP),'original_manifest_files_preserved':len(manifest_rows),'downstream_hold_rows_preserved':88},'checks':{'actual_independent_review_receipt_in_final_evidence':'PASS','final_evidence_equals_author_evidence_plus_actual_review':'PASS','author_evidence_and_scientific_review_inputs_unchanged':'PASS','all188_frozen_case_digests_raw_labels_occurrences_and_links':'PASS','all99_selected_payloads_and_reciprocal_case_links':'PASS','exact_two_case_reconciliation_with_excluded_siblings_retained':'PASS','all1062_evidence_capture_hashes':'PASS','all_original_manifest_files_and100_payload_bytes':'PASS','original_and_successor_hold_ledgers_identical':'PASS','successor_selection_points_only_to_current_intake':'PASS'},'all_case_bindings':case_rows,'all_payload_bindings':payload_rows,'limitations':['All unchanged campaign science retains its original separate independent reviews; this binding check does not self-approve B-authored payloads.','Source, whole-owner, export, maintained installation and post-sterilization chemical equivalence are not approved.','Full-overlay validator outcomes are separate coordinator receipts. This integrity PASS does not turn a failing partonomy result into a pass.'],'scientific_release_approval':False,'maintained_owner_merge_approved':False}
for name,digest in expected.items():assert sha(V/name)==digest,name
out=O/'final-binding.json';out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'path':str(out),'sha256':sha(out),'counts':report['counts'],'status':report['status']}))
