import copy,datetime,hashlib,json,pathlib,shutil,sys,yaml
sys.path.insert(0,str(pathlib.Path('src').resolve()))
from mediaingredientmech.validation.write_validated import write_validated_ingredient
R=pathlib.Path('reports/all_unmatched_20261107/worker-10');K=R/'successor-v1/kg';H=K/'history/author-v1';H.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
for n in ['decisions.json','evidence.json','proposals.json','validation.json']:
 if not (H/n).exists():shutil.copy2(K/n,H/n)
if not (H/'proposed').exists():shutil.copytree(K/'proposed',H/'proposed')
D=json.loads((K/'decisions.json').read_text());E=json.loads((K/'evidence.json').read_text());P=json.loads((K/'proposals.json').read_text());changes=[]
receipt=json.loads((K/'urls4-receipt.json').read_text())[0]
E['evidence'].append({'evidence_id':'sv1-kg-jcm403','kind':'primary_source','capture':receipt['capture'],'url':receipt['url'],'accessed_at':receipt['accessed_at'],'locator':'Vitamin solution and Thiamine solution tables, reached by explicit JCM391 crossreferences','supports_or_contradicts':'Direct primary JCM403 prints100mL sodiumphosphatebuffer10mM,pH7.1 in vitamin stock and100mL25mM,pH3.4 in thiamine stock. JCM391 itself only crossreferences these solutions.'})
newnote='JCM391 explicitly crossreferences the vitamin solution in JCM403. Direct JCM403 lists100mL sodium phosphate buffer10mM,pH7.1 in that solution; its separate thiamine solution uses25mM,pH3.4. MediaDiveJ391 expands the same crossreference, so it is derivative corroboration. This source-qualified stock preserves printed concentration/pH without inferring salt ratios, hydrate forms, titrant, solvent chemical identity or hidden water amounts.'
refmap={'Proteose peptone':('data/ingredients/mapped/Proteose_Peptone.yaml','MICRO:0000180'),'Liver digest':('data/ingredients/mapped/Liver_Digest.yaml','MICRO:0001668'),'Yeast extract':('data/ingredients/mapped/Yeast_Extract.yaml','FOODON:03315426'),'Sodium chloride':('data/ingredients/mapped/Nacl.yaml','CHEBI:26710'),'Agar':('data/ingredients/mapped/Agar.yaml','CHEBI:2509')}
refs={};targetids={'sv1-kg-difco-columbia1270','sv1-kg-sodium-buffer391','sv1-kg-indochrome-mixture','sv1-kg-oxoid-blood-base2'}
for p in P['proposals']:
 if p['proposal_id'] not in targetids:continue
 file=R/p['after_capture']['path'];v=yaml.safe_load(file.read_text());before=sha(file)
 if p['proposal_id']=='sv1-kg-difco-columbia1270':
  for k in ['notes']:v[k]=v[k].replace('horse blood','sheep blood')
  v['supplied_form'][0]['notes']=v['supplied_form'][0]['notes'].replace('horse blood','sheep blood')
  for e in v['ontology_mapping']['evidence']:e['notes']=e['notes'].replace('horse blood','sheep blood')
  p['description']=p['description'].replace('horse blood','sheep blood')
  for e in v['curation_history']:e['changes']=e['changes'].replace('horse blood','sheep blood')
  v['notes']+=' Direct JCM1270 specifies sheep blood, including70C for15minutes after addition; MediaDiveJ1270 incorrectly says horse blood. This source discrepancy is retained and does not alter the44g dry-base identity. No blood is a component of this base.'
 if p['proposal_id']=='sv1-kg-sodium-buffer391':
  v['notes']=newnote;v['supplied_form'][0]['notes']=newnote;v['ontology_mapping']['evidence']=[{'evidence_type':'MANUAL_CURATION','source':receipt['url'],'notes':newnote}];v['component_assertion']['evidence'][0]['source']=receipt['url'];v['component_assertion']['evidence'][0]['notes']='JCM403 vitamin table, explicitly referenced by JCM391: nominal10mM sodium phosphate. Exact salt species/ratio and remaining constituents not stated.';p['description']=newnote;p['evidence_ids'].append('sv1-kg-jcm403');v['curation_history'][-1]['changes']=newnote+' Proposal only; inherited publication/role/source holds remain.'
 if p['proposal_id']=='sv1-kg-indochrome-mixture':
  old=yaml.safe_load(pathlib.Path(p['owner_path']).read_text());v['ontology_mapping']['evidence']=copy.deepcopy(old['ontology_mapping']['evidence'])+v['ontology_mapping']['evidence'];v['notes']=(v.get('notes','')+' Previous primary identity kgmicrobe.compound:indochrome and its historical DATABASE_MATCH evidence are preserved in provenance. Successor proposes kgmicrobe.ingredient:indochrome for the named undefined pigment material, without four-fraction or ratio claims.').strip()
 if p['proposal_id'] in ['sv1-kg-difco-columbia1270','sv1-kg-oxoid-blood-base2']:
  for c in v['components']:
   if c['component_name'] in refmap:
    owner,ident=refmap[c['component_name']];actual=yaml.safe_load(pathlib.Path(owner).read_text());assert actual['identifier']==ident and actual['mapping_status']!='REJECTED';c['component_id']=ident;c['reference_scope']='MIM_CATALOG';refs[owner]={'sha256':sha(owner),'raw_text':pathlib.Path(owner).read_text()}
  p['evidence_ids'].append('sv1-kg-component-lookup')
 write_validated_ingredient(v,file);p['after_capture']['sha256']=sha(file);changes.append({'proposal_id':p['proposal_id'],'before_sha256':before,'after_sha256':sha(file)})
comp=K/'component-owner-lookup.json';comp.write_text(json.dumps({'ignored_files_included':True,'method':'Complete data/ingredients recursive YAML label/synonym inspection; explicit owner identity and active status checked.','resolved_component_preimages':refs,'unresolved':['Proteose Peptone No.3 has no exact maintained product owner.','Pancreatic digest of casein not equated by this review to every Tryptone product.','Cornstarch literal on genericStarch is not an exact botanical identity; bio successor owns a distinct proposed cornstarch owner, not yet maintained.','Beefheart infusion manufacturer constituent is not assigned a historical preparation yield or current local extract formulation.']},indent=2)+'\n')
E['evidence'].append({'evidence_id':'sv1-kg-component-lookup','kind':'source_snapshot','capture':{'root':'artifact','path':str(comp.relative_to(R)),'sha256':sha(comp)},'url':None,'accessed_at':None,'locator':'Five exact active component owner preimages plus unresolved branded/material alternatives','supports_or_contradicts':'Resolve establishedAgar,NaCl,YeastExtract,ProteosePeptone,LiverDigest references while keeping unsupported exact branded/dry-product identities unmapped.'})
for d in D['decisions']:
 if d['source_index']==178:
  for f in ['reasoning','applicability']:d[f]=d[f].replace('horse blood','sheep blood').replace('horseblood','sheepblood')
  d['reasoning']+=' Direct JCM1270 says sheep blood, whereas derivative MediaDiveJ1270 says horse blood. Preserve that upstream discrepancy; both separate44g base from subsequent blood addition.'
 if d['source_index']==183:
  d['reasoning']='All ten source1753 recipe contexts were inspected. The direct JCM391 source crossreferences JCM403; the newly retrieved original JCM403 vitamin table explicitly prints100mL of10mM,pH7.1 sodium phosphate buffer, while its thiamine table prints25mM,pH3.4. MediaDiveJ391 is an expanded derivative. The proposal represents only that JCM391-via403 vitamin stock preparation, without inventing salt ratios, titrant or solvent composition.';d['applicability']=newnote;d['evidence_ids'].append('sv1-kg-jcm403')
 if d['source_index'] in [169,178]:
  d['evidence_ids'].append('sv1-kg-component-lookup')
  for owner,x in refs.items():
   if not any(o['path']==owner for o in d['owner_records']):d['owner_records'].append({'path':owner,'sha256':x['sha256']})
 d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']))
for name,obj in [('decisions',D),('evidence',E),('proposals',P)]: (K/(name+'.json')).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
(K/'revision-v2.json').write_text(json.dumps({'revised_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archived_author_v1':str(H.relative_to(R)),'resolved_review_findings':['JCM1270sheepnot horse','JCM391crossreference tracedto403','Indochromehistoricalevidencerestored'],'additional_change':'Resolved five clear component owner references after complete lookup; retained specific unresolved component identity limits.','payload_changes':changes},indent=2)+'\n')
print(json.dumps(changes,indent=2))
