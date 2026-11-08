import pathlib,json,hashlib,datetime,yaml
R=pathlib.Path('reports/all_unmatched_20261107/worker-01');S=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();digest=lambda a:hashlib.sha256(json.dumps(a,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
allowed={'primary_source','source_snapshot','ontology','native_record_review','independent_review','unsuccessful_search','local_validation'}
for rel,alloc,count in [('shard/root_substances/kg26','root_substances',26),('shard/concentration_stocks','concentration_stocks',78)]:
 O=R/rel;A=pathlib.Path('.temp/all-unmatched-worker-01/shard')/(alloc+'.json');cases={x['case']['case_id']:x['case'] for x in json.loads(A.read_text())['cases'] if alloc=='concentration_stocks' or x['index'] in list(range(161,185))+[186,187]};B=O if alloc=='concentration_stocks' else R
 D=json.loads((O/'decisions.fragment.json').read_text())['decisions'];E=json.loads((O/'evidence.fragment.json').read_text())['evidence'];Q=json.loads((O/'proposals.fragment.json').read_text())['proposals'];ei={e['evidence_id']:e for e in E};qi={q['proposal_id']:q for q in Q};di={d['case_id']:d for d in D};assert len(D)==count and set(di)==set(cases);assert len(ei)==len(E) and len(qi)==len(Q)
 def capture(c):
  p=pathlib.PurePosixPath(c['path']);assert not p.is_absolute() and '..' not in p.parts and str(p)==c['path'];root=B if c['root']=='artifact' else S;f=root/p;assert c['root'] in ['artifact','source'] and f.is_file() and not f.is_symlink() and sha(f)==c['sha256'],str(f);return f
 for e in E:
  capture(e['capture']);assert e['kind'] in allowed,e;assert e['locator'] and e['supports_or_contradicts'];assert set(e.get('case_ids',[]))<=set(cases)
  if e.get('url'):assert e['url'].startswith(('https://','http://')) and e.get('accessed_at')
  if e['kind'] in ['primary_source','ontology']:assert e.get('url'),e
 for d in D:
  c=cases[d['case_id']];assert digest(c)==d['case_input_sha256'];assert d['source']=={k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']};assert d['occurrence_ids']==[x['occurrence_id'] for x in c.get('occurrences',[])];assert d['evidence_ids'] and set(d['evidence_ids'])<=set(ei);assert set(d['proposal_ids'])<=set(qi);assert d['reasoning'] and d['applicability'];assert (d['no_change_reason'] is None) if d['proposal_ids'] else bool(d['no_change_reason'])
  if d['disposition']=='unresolved':assert d['missing_requirement']
  for o in d['owner_records']:assert sha(pathlib.Path(o['path']))==o['sha256']
  for pid in d['proposal_ids']:assert d['case_id'] in qi[pid]['case_ids']
  if d['independent_review']['status']!='pending':assert d['independent_review']['evidence_ids'] and all(ei[x]['kind']=='independent_review' for x in d['independent_review']['evidence_ids'])
 for q in Q:
  a=yaml.safe_load(capture(q['after_capture']).read_text());assert q['case_ids'] and set(q['case_ids'])<=set(cases);assert q['evidence_ids'] and set(q['evidence_ids'])<=set(ei);p=pathlib.Path(q['owner_path']);assert str(p.parent) in ['data/ingredients/mapped','data/ingredients/unmapped'];assert p.suffix=='.yaml'
  if q['kind']=='new_owner':assert q['before_sha256'] is None and not p.exists()
  else:
   assert q['kind']=='edit_existing_owner' and sha(p)==q['before_sha256'];b=yaml.safe_load(p.read_text());assert a['curation_history'][:len(b['curation_history'])]==b['curation_history'];assert a['occurrence_statistics']==b['occurrence_statistics']
   assert all(any(o['path']==str(p) and o['sha256']==q['before_sha256'] for o in di[c]['owner_records']) for c in q['case_ids'])
  for c in q['case_ids']:assert q['proposal_id'] in di[c]['proposal_ids']
  if 'superseded_after_capture' in q:capture(q['superseded_after_capture'])
 receipt=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PASS',scope='Exact fragment case/source/occurrence preservation, evidence and proposal hash/reference closure, actual current before-owner guards, original history/counts preservation. New proposal strict validation and scientific author review saved separately; no independent approval is asserted here.',case_count=len(D),evidence_count=len(E),proposal_count=len(Q),scientific_adequacy_or_approval_established=False,allocation_sha256=sha(A),input_hashes={n:sha(O/n) for n in ['decisions.fragment.json','evidence.fragment.json','proposals.fragment.json']},crosslane_backlinks='Auxiliary metadata only in fragments; root must union external case links in final complete188 ledger',review_status_counts={s:sum(d['independent_review']['status']==s for d in D) for s in ['pending','complete','findings_open']})
 out=O/'fragment-integrity-completeness-v4.json';assert not out.exists();out.write_text(json.dumps(receipt,indent=2)+'\n');print(rel,json.dumps(receipt))
