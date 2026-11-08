import json,pathlib,urllib.parse,hashlib,subprocess,yaml
R=pathlib.Path('reports/all_unmatched_20261107/worker-10');S=R/'successor-v1/kg';P=S/'private';P.mkdir(parents=True,exist_ok=True)
ix=json.loads((R/'successor-v1/assigned-no-proposal-cohort.json').read_text())['partitions']['kg'];ds=[d for d in json.loads((R/'kg/decisions.json').read_text())['decisions'] if d['source_index'] in ix]
terms={137:'CMC PY horse serum',139:'atrop-abyssomicin C',140:'3-methylacetate',141:'Blood agar base',142:'abyssomicin G',144:'Cerophyll',145:'sodium acetate',146:'exfoliatin',147:'HEPES',149:'potassium 5-dehydro-D-gluconate',150:'abyssomicin H',151:'abyssomicin B',152:'ammonium oxalate',154:'sodium acetate trihydrate',155:'hortesin',158:'calf serum',159:'potassium phosphate buffer',161:'pyridoxine',162:'sterile serum',166:'DL-aspartic acid',168:'indochrome',169:'blood agar base no 2',171:'alboverticillin',173:'aminostyryl acetate',177:'rice starch',178:'Columbia blood agar base',180:'ampicillin sodium',181:'swine serum',182:'cyanocobalamin',183:'sodium phosphate buffer',184:'PIPES'}
jobs={f'ols-{i}':'https://www.ebi.ac.uk/ols4/api/search?'+urllib.parse.urlencode({'q':t,'rows':30,'exact':'false'}) for i,t in terms.items()}
for n in ['156','828','833','J915','J918','J1205','461b','746','1783','1800','J391','J403','J439','J462','J721','J911','J981','J1108','J1223','J1307','J1270']:
 jobs['medium-'+n]='https://mediadive.dsmz.de/rest/medium/'+n
for n in ['646','420','1076b','301'] :jobs['pdf-'+n]='https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium'+n+'.pdf'
for n in ['1303','1270']:jobs['jcm-'+n]='https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD='+n
jobs.update({'chebi44933':'https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44933','pc-pipes':'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/79723/property/InChI,InChIKey,MolecularFormula/JSON','ccap-hsm':'https://www.ccap.ac.uk/wp-content/uploads/MR_HSM.pdf','albo-2022':'https://pubs.acs.org/doi/10.1021/acs.jnatprod.2c00065','dl-aspartic-sigma':'https://www.sigmaaldrich.com/US/en/product/sigma/a9256'})
(P/'urls1.json').write_text(json.dumps(jobs,indent=2))
# rg -uu enumerates ignored and hidden paths; the active per-record catalog and generated label index are exhaustively inspected.
paths=subprocess.check_output(['rg','--files','--no-ignore','--hidden','data/ingredients'],text=True).splitlines();records=[]
for f in paths:
 if f.endswith('.yaml'):
  p=pathlib.Path(f);v=yaml.safe_load(p.read_text());records.append((f,v,p.read_text(),hashlib.sha256(p.read_bytes()).hexdigest()))
syn={137:['cmc','horse serum'],139:['abyssomicin','abybetaomicin'],140:['methylacetate'],141:['blood agar'],142:['abyssomicin'],144:['cerophyll','cereal grass'],145:['acetate'],146:['exfoliatin','exfoliative'],147:['hepes'],149:['dehydro','ketoglucon','keto-d-glucon'],150:['abyssomicin'],151:['abyssomicin'],152:['oxalate'],154:['acetate'],155:['hortesin'],158:['calf serum','bovine serum'],159:['phosphate buffer','k-phosphate'],161:['pyridox'],162:['serum'],163:['abyssomicin','abybetaomicin'],166:['aspartic','aspartate'],167:['abyssomicin'],168:['indochrome','indigoidine'],169:['blood agar'],170:['indochrome','indigoidine'],171:['alboverticillin','triculamin'],173:['aminostyryl'],175:['acetate'],177:['starch'],178:['columbia'],180:['ampicillin'],181:['swine serum','porcine serum'],182:['cobalamin','b12'],183:['phosphate buffer','na-phosphate'],184:['pipes'],185:['dehydro','ketoglucon','keto-d-glucon'],186:['abyssomicin']}
syn[153]=syn[150]
lookup=[];selected={}
index=pathlib.Path('docs/data/label_index.csv').read_text()
for d in ds:
 qs=syn[d['source_index']];hits=[]
 for f,v,raw,h in records:
  labels=[v.get('identifier',''),v.get('preferred_term',''),v.get('ontology_mapping',{}).get('ontology_label','')]+[s.get('synonym_text','') for s in v.get('synonyms',[])]
  matched=[x for x in labels if any(q in x.lower() for q in qs)]
  if matched:hits.append({'path':f,'sha256':h,'identifier':v.get('identifier'),'mapping_status':v.get('mapping_status'),'matched_labels':matched});selected[f]={'sha256':h,'raw_text':raw}
 lookup.append({'source_index':d['source_index'],'case_id':d['case_id'],'queries':qs,'searched_ignored_files':True,'catalog_files_inspected':len(records),'matches':hits,'label_index_rows':[l for l in index.splitlines() if any(q in l.lower() for q in qs)]})
(S/'owner-lookup.json').write_text(json.dumps({'method':'rg --files --no-ignore --hidden data/ingredients; parse all YAML labels, identifiers, ontology labels and synonyms; separately scan complete generated label_index.csv','cases':lookup},indent=2)+'\n')
(S/'owner-baselines.json').write_text(json.dumps(selected,indent=2)+'\n')
print('prepared',len(jobs),'fetches;',len(records),'catalog owners;',len(lookup),'case lookups;',len(selected),'candidate owners')
