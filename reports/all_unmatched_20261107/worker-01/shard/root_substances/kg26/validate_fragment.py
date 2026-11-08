import json,pathlib,hashlib,datetime,yaml
R=pathlib.Path('reports/all_unmatched_20261107/worker-01');B=R/'shard/root_substances/kg26';src=pathlib.Path('.temp/all-unmatched-worker-01/shard/root_substances.json');alloc=json.loads(src.read_text());cases={x['case']['case_id']:x['case'] for x in alloc['cases'] if x['index'] in list(range(161,185))+[186,187]}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest(); digest=lambda o:hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
D=json.loads((B/'decisions.fragment.json').read_text())['decisions'];E=json.loads((B/'evidence.fragment.json').read_text())['evidence'];P=json.loads((B/'proposals.fragment.json').read_text())['proposals'];assert len(D)==26 and {d['case_id'] for d in D}==set(cases);assert len({e['evidence_id'] for e in E})==len(E);ei={e['evidence_id']:e for e in E};pi={p['proposal_id']:p for p in P};checked=[]
for e in E:
 c=e['capture'];assert c['root']=='artifact';p=R/c['path'];assert not p.is_symlink() and '..' not in pathlib.PurePosixPath(c['path']).parts and sha(p)==c['sha256'],e['evidence_id'];assert set(e['case_ids'])<=set(cases);checked.append(c)
for d in D:
 c=cases[d['case_id']];assert digest(c)==d['case_input_sha256'];assert d['source']=={k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']};assert d['occurrence_ids']==[];assert d['evidence_ids'] and set(d['evidence_ids'])<=set(ei);assert set(d['proposal_ids'])<=set(pi)
 for o in d['owner_records']:assert sha(pathlib.Path(o['path']))==o['sha256']
for p in P:
 assert set(p['case_ids'])<=set(cases);assert set(p['evidence_ids'])<=set(ei);assert sha(pathlib.Path(p['owner_path']))==p['before_sha256'];assert sha(R/p['after_capture']['path'])==p['after_capture']['sha256']
 b=yaml.safe_load(pathlib.Path(p['owner_path']).read_text());a=yaml.safe_load((R/p['after_capture']['path']).read_text());a['curation_history'].pop()
 for s in a['synonyms']:
  if s['synonym_text'] in ['(5% w/v solution)','(after autoclaving)']:s['synonym_type']='RAW_TEXT'
 assert a==b
receipt={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','scope':'Fragment integrity only. Full188 structural auditor and independent scientific/native owner review remain coordinator/reviewer obligations.','case_count':len(D),'evidence_count':len(E),'proposal_count':len(P),'review_status_counts':{s:sum(d['independent_review']['status']==s for d in D) for s in ['pending','complete','findings_open']},'scientific_adequacy_or_approval_established':False,'input_hashes':{n:sha(B/n) for n in ['decisions.fragment.json','evidence.fragment.json','proposals.fragment.json']},'allocation_sha256':sha(src),'checks':['All26 exact original case digests/source4fields/count definitions preserved','Every evidence hash resolves under worker artifact root','All evidence/proposal references close','All current owner hashes match actual maintained files','Proposal exact structural diff is two synonym types plus one appended history; no other owner semantic changes']}
(B/'fragment-integrity-validation.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
