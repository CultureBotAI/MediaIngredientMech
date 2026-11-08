"""Package authored primary review; never writes maintained ingredient records."""
from pathlib import Path
import json, hashlib, yaml, re, copy, datetime

ART=Path('reports/all_unmatched_20261107/worker-04')
CAP=ART/'captures/chemistry'
SRC=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
assignment=json.loads((ART/'fragments/chemistry-assignment.json').read_text())
spec=json.loads((ART/'fragments/chemistry-review-spec.json').read_text())
cases=dict(zip(assignment['indices'],assignment['cases']))
sha=lambda b:hashlib.sha256(b).hexdigest()
def dump(path,obj):
 path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
def capture(p,root='artifact'):
 base=ART if root=='artifact' else SRC
 return {'root':root,'path':p.relative_to(base).as_posix(),'sha256':sha(p.read_bytes())}

receipts={}; failures={}
for f in sorted(CAP.glob('*receipts.json')):
 data=json.loads(f.read_text()); rows=data.get('receipts',[]) if isinstance(data,dict) else data
 for idx,r in enumerate(rows):
  if 'accessed_at' in r: receipts[r['path']]=(r,f,idx)
  elif 'error' in r:failures[r['path']]=(r,f,idx)

evidence=[]; byfile={}
def add_evidence(key,p,kind,locator,support,url=None,accessed=None,root='artifact'):
 eid='w04-chem-'+key
 if eid not in {e['evidence_id'] for e in evidence}:
  row={'evidence_id':eid,'kind':kind,'capture':capture(p,root),'locator':locator,'supports_or_contradicts':support,'url':url}
  if url:row['accessed_at']=accessed
  evidence.append(row)
 return eid

def ext(fn):
 if fn in byfile:return byfile[fn]
 if fn in receipts:
  r,p,i=receipts[fn];path=CAP/fn
  body=path.read_bytes()
  isfail=fn.startswith('mediadive-compound-') or b'Nothing found.' in body or (fn.endswith('.pdf') and not body.startswith(b'%PDF')) or (len(body)<5000 and b'Checking your browser' in body)
  kind='unsuccessful_search' if isfail else ('ontology' if fn.startswith('ols-') else 'primary_source')
  support='Captured actual response; inspect exact reagent label, formula, counterions, hydration, metadata disclaimer and preparation context. Does not establish full owner/export approval.'
  if isfail:support='Request returned unsupported endpoint JSON or HTML rather than the requested primary content; not substantive chemical evidence.'
  eid=add_evidence(fn.replace('.','-'),path,kind,'Full response; retrieval receipt '+p.name+' row '+str(i),support,r['url'],r['accessed_at'])
 elif fn in failures:
  r,p,i=failures[fn];eid=add_evidence('failed-'+fn.replace('.','-'),p,'unsuccessful_search','Receipt for '+fn+'; row '+str(i),'Actual bounded request failed: '+r['error']+'. This is not evidence that the substance or source does not exist.',r['url'],r['attempted_at'])
 elif (CAP/fn).exists() and fn.startswith('web-'):
  eid=add_evidence(fn.replace('.','-'),CAP/fn,'unsuccessful_search','Complete stored web discovery response','Discovery leads only; bibliographic search snippets are not verified exact-substance or supplied-form evidence.')
 else:
  raise ValueError('No truthful provenance for '+fn)
 byfile[fn]=eid;return eid

owner_docs={};owner_eids={};owners={}
def owner(stem_or_path):
 p=Path(stem_or_path) if '/' in stem_or_path else Path('data/ingredients/mapped')/(stem_or_path+'.yaml')
 key=p.as_posix()
 if key not in owners:
  data=p.read_bytes(); owner_docs[key]=yaml.safe_load(data);owners[key]={'path':key,'sha256':sha(data)}
  cp=CAP/'owners'/p.name;cp.parent.mkdir(parents=True,exist_ok=True);cp.write_bytes(data)
  owner_eids[key]=add_evidence('owner-'+p.stem,cp,'source_snapshot','Complete current owner bytes, including history, aliases and mapping evidence','Current baseline owner inspected; historical approvals, source assumptions and residual alias/form conflicts are not silently overwritten.')
 return owners[key]

decisions=[];D={}
for n,c in cases.items():
 disposition,reason,ids,stems,missing,files=spec[str(n)]
 cid=c['case_id'];eids=[];contexts=[]
 eids.append(add_evidence('case-'+str(n),ART/'fragments/chemistry-assignment.json','source_snapshot','$.cases['+str(assignment['indices'].index(n))+']','Complete frozen source case, all raw labels/source IDs, qualifiers, occurrence definitions, consumed rows and inherited holds. Case digest binds every field.'))
 for o in c.get('occurrences',[]):
  p=SRC/o['full_recipe_snapshot'];raw=p.read_bytes();parsed=yaml.safe_load(raw)
  assert sha(raw)==o['source_file_sha256'],(n,p)
  eid=add_evidence('recipe-'+sha(raw)[:20],p,'source_snapshot','Full recipe; component '+o['component_path'],'Complete frozen recipe inspected, including sibling ingredients, nested stocks, source URLs, references, preparation, amount units and existing caveats.',root='source')
  eids.append(eid);contexts.append({'occurrence_id':o['occurrence_id'],'recipe_id':o['recipe_id'],'component_path':o['component_path'],'snapshot':capture(p,'source'),'scope':'entire recipe bytes and parsed nested recipe; original units and qualifiers retained'})
  text=raw.decode()
  for fn,(r,_,_) in receipts.items():
   if r['url'] in text and not fn.startswith('mediadive-compound-'):eids.append(ext(fn))
  # Original NBRC/JCM providers represented by legacy variants of their URLs.
  for prefix,pat in [('nbrc',r'NBRCMediumDetailServlet\?NO=(\d+)'),('jcm',r'GRMD=(\d+)')]:
   for ident in re.findall(pat,text):
    fn=f'{prefix}-{ident}.html'
    if fn in receipts:eids.append(ext(fn))
  for ident in re.findall(r'https://togomedium.org/medium/M(\d+)',text):
   fn=f'togo-{ident}.json'
   if fn in receipts or fn in failures:eids.append(ext(fn))
 for ident in filter(None,ids.split(',')):eids.append(ext('ols-CHEBI-'+ident+'.json'))
 for fn in filter(None,files.split(',')):eids.append(ext(fn))
 opaths=[o['path'] for o in c.get('original_kg_entry',{}).get('owners',[])]+[str(Path('data/ingredients/mapped')/(s+'.yaml')) for s in stems.split(',') if s]
 if n in [4,112]:opaths.append('data/ingredients/unmapped/Titanium_Iii_Citrate.yaml')
 ownerrows=[owner(p) for p in dict.fromkeys(opaths)]
 eids.extend(owner_eids[o['path']] for o in ownerrows)
 issue_nums=[]
 if n>=132:issue_nums.append(1157)
 if n in [138]:issue_nums.append(704)
 if n in [47,58,149,166,171]:issue_nums.append(655)
 if n==159:issue_nums.extend([896,344,878])
 if n in [31,32,54,59,60,102,107,119,139,148,150]:issue_nums.append(344)
 if n==140:issue_nums.append(312)
 if n==157:issue_nums.append(320)
 if n==5:issue_nums.append(761)
 for num in issue_nums:
  for suffix in ['', '-comments']:
   p=ART/f'captures/issues/issue-{num}{suffix}.json'
   if p.exists():
    # Parent owns live-fetch receipts; this local evidence binds exact retrieved bytes.
    json.loads(p.read_text())
    eids.append(add_evidence(f'issue-{num}{suffix}',p,'source_snapshot','Complete captured issue '+str(num)+suffix,'Prior scientific ruling and current issue context inspected; evidence is read-only and does not authorize a changed source scope.'))
 prior=c.get('original_kg_entry',{})
 d={'case_id':cid,'case_input_sha256':sha(json.dumps(c,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()),'source':{k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']},'occurrence_ids':[o['occurrence_id'] for o in c.get('occurrences',[])],'disposition':disposition,'reasoning':reason,'applicability':f'Applies only to frozen case {cid}, source {c["source"]}, identifier {c["source_case_id"]}; every listed recipe context and exact raw/processed label remains bound by case_input_sha256. '+('KG helper/graph occurrence definition is retained verbatim and is not asserted to be recipe frequency. ' if prior else '')+'Matching lexical labels do not extend source identity to unrelated cases. All inherited downstream and complete-payload publication holds remain in force.','evidence_ids':list(dict.fromkeys(eids)),'proposal_ids':[],'no_change_reason':missing or 'The reviewed source identity is already represented in current owner bytes; no new alias or identity mutation is needed. Complete-payload/native publication review is separate and inherited holds are retained.','missing_requirement':missing or None,'owner_records':ownerrows,'issue_refs':['https://github.com/CultureBotAI/MediaIngredientMech/issues/'+str(x) for x in issue_nums],'independent_review':{'status':'pending','evidence_ids':[]},'source_contexts_inspected':contexts,'inherited_source_record':prior.get('source_record'),'inherited_occurrence_definition':prior.get('occurrences_definition'),'inherited_downstream_holds':prior.get('downstream_holds',[]),'publication_disposition':'PRESERVE_ALL_INHERITED_HOLDS; PROPOSALS_REQUIRE_NEW_COMPLETE_PAYLOAD_REVIEW'}
 decisions.append(d);D[n]=d

# Primary documents independently retrieved by the skeptical reviewer, reused with
# original retrieval times and hashes rather than refetched or re-dated.
rr=ART/'independent-review/chemistry-biological-captures/reviewer-retrievals.json'
if rr.exists():
 for i,row in enumerate(json.loads(rr.read_text())):
  rp=Path(row['path']) if row.get('path') else rr
  kind='primary_source' if row.get('status')==200 else 'unsuccessful_search'
  eid=add_evidence('reviewer-primary-'+str(i),rp,kind,'Independent reviewer receipt row '+str(i)+'; full primary document where returned','Raka-Ray manufacturer formula still leaves potassium-glutamate stereo/form unspecified; JCM401 separately retains ambiguous13ml total and1ml water; ATCC retrieval failure does not establish source absence.',row['url'],row['accessed_at'])
  for n in row['indices']:D[n]['evidence_ids'].append(eid)
fp=SRC/'inputs/culturemech/data/normalized_yaml/algae/F_2_Medium.yaml'
eid=add_evidence('biotin-stock-comparator',fp,'source_snapshot','Full frozen F/2 recipe; nested Biotin Vitamin Solution','Comparator only: UTEX biotin stock is HEPES-buffered200ml preparation with5mg biotin, distinct from NBRC989 ethanol100ml/5mg stock. This does not claim the F/2 case as assigned or approve its recipe.',root='source')
D[61]['evidence_ids'].append(eid)

# Only exact isolated owner payloads are written. Case-spec reasoning is human-authored above.
proposals=[]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def proposal(key,nums,stem,adds=(),rejects=(),newid=None,newlabel=None,new=False,repair_structure=False):
 path=Path('data/ingredients/mapped')/(stem+'.yaml');pkey=path.as_posix()
 if new:
  assert not path.exists()
  term=json.loads((CAP/f'ols-CHEBI-{newid}.json').read_text())['_embedded']['terms'][0]
  d={'identifier':'CHEBI:'+str(newid),'preferred_term':newlabel,'ontology_mapping':{'ontology_id':'CHEBI:'+str(newid),'ontology_label':term['label'],'ontology_source':'CHEBI','mapping_quality':'EXACT_MATCH','evidence':[]},'synonyms':[],'mapping_status':'MAPPED','ingredient_type':'SINGLE_INGREDIENT','curation_history':[]}
  a=term.get('annotation',{});props={}
  for src,dst in [('generalized_empirical_formula','molecular_formula'),('inchi_string','inchi'),('smiles_string','smiles')]:
   if a.get(src):props[dst]=a[src][0]
  if a.get('mass'):props['molecular_weight']=float(a['mass'][0])
  # Retinol and ionic oxoglutarate deliberately do not acquire a stereo-specific or acid CAS.
  if newid in [40947,190439]:
   cas=[x[4:] for x in a.get('database_cross_reference',[]) if x.startswith('cas:')]
   if len(cas)==1:props['cas_rn']=cas[0]
  props.update(data_source='ChEBI via OLS4; exact captured primary ontology',retrieval_date=receipts[f'ols-CHEBI-{newid}.json'][0]['accessed_at'])
  d['chemical_properties']=props;before=None
 else:
  owner(pkey);d=copy.deepcopy(owner_docs[pkey]);before=owners[pkey]['sha256']
 for s in adds:
  if s not in [x['synonym_text'] for x in d.get('synonyms',[])]:d.setdefault('synonyms',[]).append({'synonym_text':s,'synonym_type':'EXACT_SYNONYM','source':'all_unmatched_20261107_worker04_source_review'})
 for s in rejects:
  matches=[x for x in d.get('synonyms',[]) if x['synonym_text']==s]
  assert matches,('missing reject',stem,s)
  for x in matches:x['synonym_type']='REJECTED_LABEL'
 if newid and not new:
  d['identifier']='CHEBI:'+str(newid);d['ontology_mapping'].update(ontology_id='CHEBI:'+str(newid),ontology_label=newlabel,mapping_quality='SYNONYM_MATCH')
 if repair_structure:
  a=json.loads((CAP/'ols-CHEBI-232425.json').read_text())['_embedded']['terms'][0]['annotation']
  for src,dst in [('generalized_empirical_formula','molecular_formula'),('inchi_string','inchi'),('smiles_string','smiles')]:d['chemical_properties'][dst]=a[src][0]
  d['chemical_properties']['data_source']='ChEBI:232425 via captured OLS4; original CAS provenance retained in history'
  d['chemical_properties']['retrieval_date']=receipts['ols-CHEBI-232425.json'][0]['accessed_at']
 desc=' '.join(D[n]['reasoning'] for n in nums)
 d.setdefault('ontology_mapping',{}).setdefault('evidence',[]).append({'evidence_type':'MANUAL_CURATION','source':'all_unmatched_20261107 worker04 primary proposal '+key,'notes':desc+' Evidence and exact frozen scope are recorded in reports/all_unmatched_20261107/worker-04/fragments/chemistry-decisions.json. This proposed delta does not approve complete owner/export payload or remove inherited holds.'})
 d.setdefault('curation_history',[]).append({'timestamp':now,'curator':'codex_worker04_chemistry','action':'CREATED' if new else 'CORRECTED','changes':'Isolated source-review proposal '+key+': '+('new exact ingredient identity; ' if new else '')+'added aliases '+repr(list(adds))+'; rejected provenance labels '+repr(list(rejects))+('. Exact ontology promotion.' if newid and not new else '')+('. Corrected hydrate InChI/SMILES to include one water.' if repair_structure else '')+' Subject to independent skeptical review and guarded coordinator integration; inherited full-payload support must not transfer.','new_status':'MAPPED','llm_assisted':True})
 after=ART/'proposals/chemistry'/(stem+'.after.yaml');after.parent.mkdir(parents=True,exist_ok=True);after.write_text(yaml.safe_dump(d,sort_keys=False,allow_unicode=True,width=1000))
 peids=list(dict.fromkeys(e for n in nums for e in D[n]['evidence_ids']))
 pid='w04-chem-proposal-'+key
 proposals.append({'proposal_id':pid,'case_ids':[cases[n]['case_id'] for n in nums],'description':desc,'evidence_ids':peids,'owner_path':pkey,'kind':'new_owner' if new else 'edit_existing_owner','after_capture':capture(after),'before_sha256':before,'publication_obligations':['Withdraw inherited complete-payload support for changed owner.','Regenerate synchronized YAML/SSSOM only during guarded coordinator integration.','Review all published aliases, registry rows and asymmetric relationships against final owner bytes.','Retain all source-bound holds pending independent/native complete-payload approval.'],'cross_shard_owner_conflict':'Coordinator must compare this original before hash against all worker proposals; never apply last-writer-wins.'})
 for n in nums:
  D[n]['proposal_ids'].append(pid);D[n]['no_change_reason']=None
  if not new and owners[pkey] not in D[n]['owner_records']:D[n]['owner_records'].append(owners[pkey])

proposal('trisodium-edta',[1],'Na3-edta',adds=['3Na-EDTA'],rejects=['EDTA di sodium salt'])
proposal('polysorbate80-alias',[5],'Tween_80',adds=[cases[5]['raw_source_label']])
proposal('water-spelling',[14],'Distilled_Water',adds=[cases[14]['raw_source_label']])
proposal('glycerol-anhydrous',[15,167],'Glycerol',adds=['Glycerol (anhydrous)'])
proposal('d-biotin-spellings',[24,78],'Biotin',adds=[cases[n]['raw_source_label'] for n in [24,78]])
proposal('nacetyl-d-monomer',[35,37],'N-acetyl-d-glucosamine',adds=[cases[n]['raw_source_label'] for n in [35,37]])
proposal('glutamate-monohydrate',[58,166],'Sodium_Glutamate_Monohydrate',adds=[cases[58]['raw_source_label']],repair_structure=True)
proposal('folate-b9',[76],'Folic_Acid',adds=[cases[76]['raw_source_label']])
proposal('ferric-ammonium-citrate',[77],'Ferric_Ammonium_Citrate',adds=[cases[77]['raw_source_label']])
proposal('ferric-edta',[94],'Fe_Iii-edta',adds=[cases[94]['raw_source_label']])
proposal('retinol',[28],'Retinol',adds=['Retinol'],newid=50211,newlabel='retinol',new=True)
proposal('barium-carbonate',[40],'Barium_Carbonate',adds=['BaCO3'],newid=190439,newlabel='barium carbonate',new=True)
proposal('bis-tris-propane',[103],'Bis_Tris_Propane',adds=['Bis Tris Propane'],newid=40947,newlabel='bis-tris propane',new=True)
proposal('2-oxoglutarate',[128],'2-Oxoglutarate',adds=['2-Oxoglutarate'],newid=16810,newlabel='2-oxoglutarate(2-)',new=True)
proposal('putrescine-dihydrochloride',[137],'Putrescine_Dihydrochloride',newid=201718,newlabel='1,4-Diaminobutane dihydrochloride')
proposal('orthomolybdate-alias',[140],'Diammonium_molybdate',rejects=['(NH4)6Mo7O24'])
proposal('heptamolybdate-tetrahydrate',[140],'Ammonium_Molybdate_Tetrahydrate',adds=['(NH4)6Mo7O24 x 4 H2O'])
proposal('taps-salt-alias',[152],'TAPS_Sodium_Salt',rejects=['TAPS'])
proposal('tungstate-malformed-alias',[168],'Na2wo4_X_2_H2o',rejects=['Na2WO2 x 2 H2O','Na2WO2.2H2O'])
proposal('monosodium-glutamate-alias',[149,171],'Na_Glutamate',rejects=['Na2-glutamate'])
proposal('thiosulfate-malformed-alias',[182],'Na2s2o3',rejects=['Na2S2SO3'])

def stock(key,n,stem,label,components,completeness,source,notes,solution='OTHER'):
 path=Path('data/ingredients/mapped')/(stem+'.yaml');assert not path.exists()
 ident='kgmicrobe.ingredient:'+stem.lower()
 # Slug and source-qualified labels were searched including ignored files.
 for p in Path('data/ingredients').rglob('*.yaml'):
  assert not re.search(r'^identifier: '+re.escape(ident)+r'\s*$',p.read_text(),re.M),('duplicate',p,ident)
 de=add_evidence('stock-duplicate-search',CAP/'stock-duplicate-search.txt','local_validation','rg -uu data/ingredients and docs/data/label_index.csv; source-qualified labels and slugs','Ignored files included. Existing generic biotin stock, carbonate stocks and generic titanium-citrate placeholder do not establish exact formulation identity.')
 D[n]['evidence_ids'].append(de)
 d={'identifier':ident,'preferred_term':label,'mapping_status':'MAPPED','ingredient_type':'STOCK_SOLUTION','solution_type':solution,'ontology_mapping':{'ontology_id':ident,'ontology_label':label,'ontology_source':'kgmicrobe.ingredient','mapping_quality':'FALLBACK_REGISTRY','evidence':[{'evidence_type':'MANUAL_CURATION','source':source,'notes':'Source-qualified formulation identity. No molecular exactMatch or generic-stock equivalence is asserted. '+notes}]},'synonyms':[{'synonym_text':cases[n]['raw_source_label'],'synonym_type':'REJECTED_LABEL','source':source}],'components':components,'component_assertion':{'method':'RECIPE_TRANSCRIPTION','completeness':completeness,'evidence':[{'evidence_type':'RECIPE_SOURCE','source':source,'source_record':label,'notes':notes}],'notes':'Amounts retain their explicit stock or source-batch basis; no measured final volume or receiving-medium concentration is inferred.'},'notes':'Isolated source-review proposal. Generic raw source spelling retained as nonresolving provenance so this specific formulation cannot capture other preparations. '+notes,'curation_history':[{'timestamp':now,'curator':'codex_worker04_chemistry','action':'CREATED','changes':'Proposed source-qualified stock '+key+' with source-stated component scope. No maintained owner or publication selector was changed.','new_status':'MAPPED','llm_assisted':True}]}
 after=ART/'proposals/chemistry'/(stem+'.after.yaml');after.write_text(yaml.safe_dump(d,sort_keys=False,allow_unicode=True,width=1000))
 pid='w04-chem-proposal-'+key
 proposals.append({'proposal_id':pid,'case_ids':[cases[n]['case_id']],'description':D[n]['reasoning'],'evidence_ids':list(dict.fromkeys(D[n]['evidence_ids'])),'owner_path':path.as_posix(),'kind':'new_owner','after_capture':capture(after),'before_sha256':None,'publication_obligations':['Coordinator validates schema and partonomy with proposal overlay.','Generic source spellings are nonresolving provenance; no global source matching release.','No source concentration/unit repair or maintained data edit is performed here.'],'cross_shard_owner_conflict':'Compare source formulation and intended slug against other worker proposals before integration.'})
 D[n]['proposal_ids'].append(pid);D[n]['no_change_reason']=None

stock('nbrc989-biotin-ethanol',61,'NBRC_989_Biotin_Ethanol_Stock','NBRC 989 biotin ethanol stock',[
 {'component_name':'Biotin','reference_scope':'UNMAPPED','concentration_value':'5','concentration_unit':'mg per source batch'},
 {'component_name':'Ethanol','reference_scope':'UNMAPPED','concentration_value':'100','concentration_unit':'ml per source batch'}],
 'COMPLETE','https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=989','NBRC989 *Biotin solution table explicitly gives5mg biotin and100ml ethanol; this differs from the HEPES-buffered UTEX biotin vitamin stock in the frozen F/2 comparator. The2ml receiving-medium addition is not stock composition.','VITAMIN_MIX')
stock('togo2809-carbonate8percent',55,'TOGO_2809_Sodium_Carbonate_8_Percent','TOGO 2809 sodium carbonate 8% w/v stock',[
 {'component_name':'Na2CO3','reference_scope':'UNMAPPED','concentration_value':'80','concentration_unit':'G_PER_L'}],
 'PARTIAL','https://togomedium.org/medium/M2809','The stock label8%(wt/vol) explicitly supplies80g/L Na2CO3. Solvent identity and amount are not separately specified, so neither is invented. The100ml quantity is the amount added in titanium-citrate preparation.','MINERAL_STOCK')
stock('togo2809-titanium-citrate',112,'TOGO_2809_Titanium_Citrate_Stock','TOGO 2809 LS4D titanium citrate stock',[
 {'component_name':'0.2 M Sodium citrate solution','reference_scope':'UNMAPPED','concentration_value':'500','concentration_unit':'ml per source batch'},
 {'component_name':'20% (wt/vol) TiCl3 solution','reference_scope':'UNMAPPED','concentration_value':'37.5','concentration_unit':'ml per source batch'},
 {'component_name':'8% (wt/vol) Na2CO3 solution','reference_scope':'UNMAPPED','concentration_value':'100','concentration_unit':'ml per source batch'}],
 'PARTIAL','https://togomedium.org/medium/M2809','TOGO2809 comments paragraph16 gives these three stock additions. Nitrogen is the preparation atmosphere and is not asserted as a quantified dissolved constituent. These are formulation inputs; Ti/citrate speciation and the final reacted composition/volume are not claimed. The source5ml addition to LS4D must not become5g/L.','OTHER')
stock('togo2262-hepes-naoh',68,'TOGO_2262_HEPES_NaOH_Stock','TOGO 2262 HEPES-NaOH 1 M pH 7.5 stock',[
 {'component_name':'HEPES','reference_scope':'UNMAPPED','concentration_value':'238.3','concentration_unit':'G_PER_L'},
 {'component_name':'NaOH','reference_scope':'UNMAPPED'},
 {'component_name':'Water','reference_scope':'UNMAPPED'}],
 'PARTIAL','https://togomedium.org/medium/M2262','TOGO2262 comments paragraph6 gives119.15g HEPES and final500ml stock volume, yielding238.3g/L; pH7.5 and nominal1M are source-stated. NaOH is explicit in the stock title but its titration amount is unspecified. Initial250ml water followed by making up to500ml is not a measured final pure-water amount. The medium1mM occurrence is distinct from the1M stock.','BUFFER_SOLUTION')
stock('togo1146-crotonate-stock',3,'TOGO_1146_1147_Crotonic_Acid_Stock','TOGO 1146/1147 crotonic acid 0.5 M pH 7 stock',[
 {'component_name':'Crotonic acid','reference_scope':'UNMAPPED','concentration_value':'0.5','concentration_unit':'MOLAR'}],
 'PARTIAL','https://togomedium.org/medium/M1146','TOGO1146 and1147 list0.5M Crotonic acid(pH7.0) as a20ml sterile anaerobic stock addition. The stated concentration and pH define the source-qualified stock context; neutralizing reagent and solvent are not explicitly specified and are not invented. No stock-to-receiving-medium mass or pure-acid identity is asserted.','OTHER')

for d in decisions:
 if d['disposition']=='new_distinct_ingredient_proposal':assert d['proposal_ids']
 assert d['evidence_ids']
dump(ART/'fragments/chemistry-decisions.json',{'schema_version':1,'worker_slot':4,'shard_sha256':'446d8ca4f93e4275a48f42fe29944b09253d2ddd9b7c2575a2ee74b72fcd833a','phase':'shard','decisions':decisions})
dump(ART/'fragments/chemistry-evidence.json',{'schema_version':1,'evidence':evidence})
dump(ART/'fragments/chemistry-proposals.json',{'schema_version':1,'proposals':proposals})
print(json.dumps({'decisions':len(decisions),'proposals':len(proposals),'evidence':len(evidence),'independent_review':'pending','owners':len(owners)},indent=2))
