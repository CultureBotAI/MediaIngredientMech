from pathlib import Path
import json,hashlib,yaml,datetime
O=Path('reports/all_unmatched_20261107/worker-02');R=O/'continuation-1201-v1/c';A=O/'continuation-1201-v1/a/review-c'
SRC=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
sha=lambda b:hashlib.sha256(b).hexdigest()
E={e['evidence_id']:e for e in json.loads((O/'evidence.json').read_text())['evidence']};E.update({e['evidence_id']:e for e in json.loads((R/'evidence.json').read_text())['evidence']})
E.update({e['evidence_id']:e for e in json.loads((O/'continuation-1201-v1/a/evidence.json').read_text())['evidence']})
D=json.loads((R/'decisions.json').read_text())['decisions'];P=json.loads((R/'proposals.json').read_text())['proposals'];C={c['case_id']:c for c in json.loads(Path('.temp/all-unmatched-worker-02/cases-c.json').read_text())}
manifest={};errors=[];rows=[]
def bind(root,path,expect=None):
 base={'artifact':O,'source':SRC,'mim':Path('.')}[root];p=base/path;b=p.read_bytes();h=sha(b)
 if expect and expect!=h:errors.append((root,path,'hash_mismatch',expect,h))
 manifest[(root,path)]={'root':root,'path':path,'sha256':h}
 return b
for name in ['decisions.json','evidence.json','proposals.json','reassessments.json','owner-lookup.json']:
 bind('artifact',str((R/name).relative_to(O)))
for d in D:
 c=C[d['case_id']];assert sha(json.dumps(c,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode())==d['case_input_sha256']
 if c.get('occurrences'):assert set(d['occurrence_ids'])=={x['occurrence_id'] for x in c['occurrences']}
 read=[]
 for eid in d['evidence_ids']:
  if eid not in E:errors.append((d['case_id'],'missing_evidence',eid));continue
  e=E[eid];cp=e['capture'];b=bind(cp['root'],cp['path'],cp['sha256']);read.append(eid)
 for owner in d['owner_records']:bind('mim',owner['path'],owner['sha256'])
 kg=c.get('original_kg_entry',{})
 rows.append({'case_id':d['case_id'],'label':d['source']['source_label'],'case_digest_verified':True,'complete_frozen_case_keys':list(c),'source_ids':kg.get('source_ids'),'all_original_hold_data':{k:v for k,v in kg.items() if 'hold' in k or k in ['source','source_label','raw_source_label','source_case_id','source_node_id','source_node']},'read_evidence_ids':read,'owner_count':len(d['owner_records'])})
for p in P:
 cp=p['after_capture'];after=yaml.safe_load(bind(cp['root'],cp['path'],cp['sha256']))
 if p['kind']=='edit_existing_owner':before=yaml.safe_load(bind('mim',p['owner_path'],p['before_sha256']));assert after['curation_history'][:len(before.get('curation_history',[]))]==before.get('curation_history',[])
for row in json.loads((R/'owner-lookup.json').read_text()).get('cases',[]):
 pass
out={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input_hash_manifest':list(manifest.values()),'cases':rows,'errors':errors,'scope':'Integrity/read receipt only, not scientific approval. All complete frozen case objects and referenced bytes loaded; scientific findings authored separately.'}
(A/'read-and-integrity-receipt.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('cases',len(rows),'captures',len(manifest),'errors',errors)
