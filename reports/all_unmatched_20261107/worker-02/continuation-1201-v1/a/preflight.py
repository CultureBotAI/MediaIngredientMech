from pathlib import Path
import datetime, hashlib, json, re, shutil
import yaml

OLD=Path('reports/all_unmatched_20261107/worker-02')
R=OLD/'continuation-1201-v1/a'
SRC=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
sha=lambda b:hashlib.sha256(b).hexdigest()
assigned=json.loads((R/'assigned.json').read_text())['cases']
cases=json.loads(Path('.temp/all-unmatched-worker-02/cases-a.json').read_text())
evidence={x['evidence_id']:x for x in json.loads((OLD/'evidence.json').read_text())['evidence']}
queries={
0:r'fe2.*so4|ferric.*sulfate|iron\(3\+\).*sulfate',3:r'vso4|vos[o0]4|vanad.*sulfate',4:r'feso4|ferrous.*sulfate|hcl',6:r'nh4c[lI]|ammonium chloride',7:r'sol\.? ?2|jcm|chalcopyrite',8:r'fe2.*so4|ferric.*sulfate',9:r'ultrapure|water|h2o',10:r'malat|malic',11:r'h2so4|sulfuric|sulphuric',12:r'meat|beef|horse|filtrate',15:r'methanol',16:r'GDP|guanosine.*diphosphate|glucose',17:r'h2so4|sulfuric|sulphuric',19:r'h2so4|sulfuric|sulphuric',21:r'mnso4|manganese.*sulfate',22:r'alk.*so4|kal.*so4|aluminium potassium|potassium aluminium',23:r'ebios|brewer|yeast',24:r'ni.*nh4|ammonium nickel|nickel ammonium',26:r'carrot',27:r'fe.*nh4|ferrous ammonium|hcl',28:r'niso4|nickel.*sulfate',29:r'cyste[i]?n.*hcl|cysteine hydrochloride',31:r'coso4|cobalt.*sulfate',32:r'alk.*so4|kal.*so4|aluminium potassium|potassium aluminium',33:r'arginine',34:r'fe.*nh4|ferrous ammonium',35:r'selenic|selenous|se-acid',36:r'mnso4|manganese.*sulfate',38:r'mnso4|manganese.*sulfate',41:r'mnso4|manganese.*sulfate',42:r'zinc|znso4|zncl',43:r'hcl|hydrochlor',44:r'sol\.? ?1|croton|alkaliph',46:r'h2so4|sulfuric|sulphuric',47:r'fe2.*so4|ferric.*sulfate',48:r'methanol',49:r'h2so4|sulfuric|sulphuric',50:r'whatman|filter paper|cellulose',51:r'coso4|cobalt.*sulfate',52:r'alk.*so4|kal.*so4|aluminium potassium|potassium aluminium',53:r'fe.*nh4|ferrous ammonium',54:r'^agar$|ager',56:r'standard.*mineral|hutner|metals.*44|phosphate.*buffer',57:r'alk.*so4|kal.*so4|aluminium potassium|potassium aluminium',58:r'sol\.? ?1|jcm|mrssi|alkaliph|mineral base',59:r'feso4|ferrous.*sulfate|h2so4',60:r'feso4|ferrous.*sulfate',61:r'cuso4|copper.*sulfate'}
catalog=[]
for p in sorted(Path('data/ingredients').rglob('*.yaml')):
 b=p.read_bytes(); obj=yaml.safe_load(b)
 if isinstance(obj,dict) and obj.get('identifier'):
  labels=[obj.get('identifier',''),obj.get('preferred_term',''),(obj.get('ontology_mapping') or {}).get('ontology_label','')]+[x.get('synonym_text','') for x in obj.get('synonyms') or []]
  catalog.append({'path':str(p),'sha256':sha(b),'identifier':obj['identifier'],'preferred_term':obj['preferred_term'],'mapping_status':obj.get('mapping_status'),'labels':labels,'record':obj})
label_index=Path('docs/data/label_index.csv').read_text()
results=[]; refchecks=[]; owners={}
(R/'before').mkdir(exist_ok=True)
for row in assigned:
 i=row['index']; d=row['decision']; c=cases[i]; assert c['case_id']==d['case_id']
 matches=[x for x in catalog if any(re.search(queries[i],str(t),re.I) for t in x['labels'])]
 for m in matches:
  dest=R/'before'/Path(m['path']).parent.name/Path(m['path']).name;dest.parent.mkdir(exist_ok=True);shutil.copyfile(m['path'],dest)
  m['capture']={'root':'artifact','path':str(dest.relative_to(OLD)),'sha256':m['sha256']};owners[m['path']]=m
 source_checks=[]
 for eid in d['evidence_ids']:
  e=evidence.get(eid)
  if not e:continue
  cap=e.get('capture')
  if not cap:continue
  base={'source':SRC,'artifact':OLD,'mim':Path('.')}.get(cap['root'])
  if base is None:continue
  data=(base/cap['path']).read_bytes();assert sha(data)==cap['sha256'],(i,eid)
  source_checks.append({'evidence_id':eid,'kind':e['kind'],'capture':cap,'url':e.get('url'),'locator':e.get('locator')})
 frozen=[]
 for occ in c.get('occurrences',[]):
  data=(SRC/occ['full_recipe_snapshot']).read_bytes();assert sha(data)==occ['source_file_sha256'];obj=yaml.safe_load(data)
  frozen.append({'occurrence':occ,'whole_recipe':obj,'sha256':sha(data)})
 results.append({'index':i,'case_id':d['case_id'],'case_input_sha256':d['case_input_sha256'],'raw_label':d['source']['raw_source_label'],'owner_search':{'pattern':queries[i],'scope':'All YAML under data/ingredients via Path.rglob (includes ignored files); all preferred names, identifiers, ontology labels and all synonym types, including rejected candidates. Generated label_index separately searched. This is candidate retrieval, not identity approval.','catalog_records_examined':len(catalog),'matches':[{'path':x['path'],'sha256':x['sha256'],'identifier':x['identifier'],'preferred_term':x['preferred_term'],'mapping_status':x['mapping_status'],'capture':x['capture']} for x in matches],'label_index_lines':[line for line in label_index.splitlines() if re.search(queries[i],line,re.I)]},'verified_prior_evidence':source_checks,'frozen_occurrences':frozen})
(R/'owner-lookups-and-context.json').write_text(json.dumps({'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'catalog_manifest':[{'path':x['path'],'sha256':x['sha256']} for x in catalog],'label_index_sha256':sha(Path('docs/data/label_index.csv').read_bytes()),'cases':results},indent=2,ensure_ascii=False)+'\n')
(R/'owner-candidates.json').write_text(json.dumps(list(owners.values()),indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'cases':len(results),'occurrences':sum(len(x['frozen_occurrences']) for x in results),'catalog_records':len(catalog),'candidate_owner_files':len(owners),'per_case':[(x['index'],x['raw_label'],len(x['owner_search']['matches'])) for x in results]},indent=2))
