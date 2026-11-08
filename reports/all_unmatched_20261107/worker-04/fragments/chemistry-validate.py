"""Read-only integrity check of the 74-case chemistry fragment (not the whole shard)."""
from pathlib import Path
import json, hashlib, yaml

root=Path('reports/all_unmatched_20261107/worker-04')
source=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
sha=lambda b:hashlib.sha256(b).hexdigest()
load=lambda name:json.loads((root/'fragments'/name).read_text())
assignment=load('chemistry-assignment.json')
decisions=load('chemistry-decisions.json')['decisions']
evidence=load('chemistry-evidence.json')['evidence']
proposals=load('chemistry-proposals.json')['proposals']
di={d['case_id']:d for d in decisions}
ei={e['evidence_id']:e for e in evidence}
pi={p['proposal_id']:p for p in proposals}
assert len(di)==len(decisions)==len(assignment['cases'])==74
assert len(ei)==len(evidence) and len(pi)==len(proposals)
for item in evidence+[{'capture':p['after_capture']} for p in proposals]:
 c=item['capture'];p=(root if c['root']=='artifact' else source)/c['path']
 assert p.is_file() and not p.is_symlink()
 assert sha(p.read_bytes())==c['sha256'],p
for c in assignment['cases']:
 d=di[c['case_id']]
 assert d['case_input_sha256']==sha(json.dumps(c,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode())
 assert d['source']=={k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']}
 assert d['occurrence_ids']==[o['occurrence_id'] for o in c.get('occurrences',[])]
 assert set(d['evidence_ids'])<=ei.keys()
 for p in d['proposal_ids']:assert d['case_id'] in pi[p]['case_ids']
 for o in d['owner_records']:assert sha(Path(o['path']).read_bytes())==o['sha256']
 if d['disposition']=='unresolved':assert d['missing_requirement']
 if not d['proposal_ids']:assert d['no_change_reason']
for p in proposals:
 assert set(p['evidence_ids'])<=ei.keys()
 for cid in p['case_ids']:assert p['proposal_id'] in di[cid]['proposal_ids']
 if p['before_sha256']:assert sha(Path(p['owner_path']).read_bytes())==p['before_sha256']
 else:assert not Path(p['owner_path']).exists()
 obj=yaml.safe_load((root/p['after_capture']['path']).read_text())
 assert obj['identifier'] and obj['curation_history'][-1]['llm_assisted'] is True
 if obj.get('ingredient_type')=='STOCK_SOLUTION':
  assert obj.get('components') and obj.get('component_assertion')
  assert all(s['synonym_type']=='REJECTED_LABEL' for s in obj.get('synonyms',[])),p['proposal_id']
print('PASS chemistry fragment integrity: 74 complete frozen cases; '+str(len(evidence))+' evidence records; '+str(len(proposals))+' isolated proposals.')
print('All capture hashes, current owner hashes, complete source/occurrence preservation, proposal backlinks and YAML parse checks passed.')
print('This is not the whole-shard outcome auditor, strict LinkML validation, native mapping review, independent scientific approval or publication approval.')
for n in ['chemistry-decisions.json','chemistry-evidence.json','chemistry-proposals.json']:
 print(n,sha((root/'fragments'/n).read_bytes()))
