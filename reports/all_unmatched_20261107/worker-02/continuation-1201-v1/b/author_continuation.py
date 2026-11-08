"""Serialize individually researched continuation decisions; no maintained writes.
Specifications below are manually authored source assessments, not lexical matches.
"""
from pathlib import Path
import copy, datetime, hashlib, json, re, yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient

R=Path('reports/all_unmatched_20261107/worker-02')
B=R/'continuation-1201-v1/b'
NOW='2026-11-08T06:01:16Z'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,x): Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def cap(p): return {'root':'artifact','path':str(Path(p).resolve().relative_to(R.resolve())),'sha256':sha(p)}
assigned=json.loads((B/'assigned.json').read_text())['cases']
D={x['index']:copy.deepcopy(x['decision']) for x in assigned}
DOS={x['index']:x for x in json.loads((B/'reread-source-dossiers.json').read_text())}
OLD={x['evidence_id']:x for x in json.loads((R/'evidence.json').read_text())['evidence']}
E=[]; P=[]; ledger=[]
for d in D.values():
 d['independent_review']={'status':'pending','evidence_ids':[]}
 d['primary_author']='/root/research_b'
 d['proposal_ids']=[]
def evidence(eid,path,kind,claim,idx,url=None,at=NOW):
 e={'evidence_id':eid,'kind':kind,'capture':cap(path),'locator':url or str(path),'supports_or_contradicts':claim,'case_ids':[D[i]['case_id'] for i in idx]}
 if url:e.update(url=url,accessed_at=at)
 E.append(e)
 for i in idx:
  if eid not in D[i]['evidence_ids']:D[i]['evidence_ids'].append(eid)
 return eid
evidence('b2-dossiers',B/'reread-source-dossiers.json','source_snapshot','Complete frozen case and full-recipe reread, source paths and original hashes. This is frozen context, not an independent primary publication.',list(D))
evidence('b2-catalogue',B/'catalogue-lookup.json','local_validation','Ignored-independent actual YAML catalogue inspection and current label-index hash; candidate records include exact bytes and histories.',list(D))
retrieval_cases={'mesh-ferricsulfate':[72],'mesh-feedta':[125],'noah-fe-edta':[125],'jcm431':[103],'jcm997':[84],'jcm1137':[95,107],'chebi-50732':[74],'chebi-53471':[99],'chebi-53438':[72],'chebi-27569':[102],'chebi-39033':[84],'chebi-86156':[76],'chebi-30729':[125]}
for manifest in ['retrievals.json','supplement-retrievals.json']:
 for row in json.loads((B/manifest).read_text()):
  idx=retrieval_cases.get(row['name'])
  if not idx or not row.get('path'):continue
  path=Path(row['path'])
  kind='unsuccessful_search' if row['name'] in ['jcm997','jcm1137'] else 'primary_source'
  claim=('Endpoint returns no requested medium table; no recipe identity is inferred.' if kind=='unsuccessful_search' else 'Direct primary source/ontology capture; use only case-specific assertions explained in the decision.')
  evidence('b2-'+row['name'],path,kind,claim,idx,row['url'],row['accessed_at'])
for fn,idx,claim in [('primary-web-round4.json',[68,99,102,125],'Primary BD product name, Sigma chromium variable hydrate CAS/formula, Sigma larch arabinogalactan botanical material, and Canada ammonium ferric EDTA CAS identity. Supplier product numbers are comparison evidence, not recipe-selected catalogues.'),('primary-web-round9.json',[68,84],'Primary Sigma PIPES name/free-acid correspondence; original authors OADC recipe is comparison evidence and does not prove the exact commercial product formula.'),('primary-web-round8.json',[97],'Unsuccessful original Delft retrieval; technical timeout does not imply nonexistence.'),('search-identity-round3.json',[72,73,79,84,85,95,97,107,109,115,120,121,122],'Bounded primary-source discovery and comparison search; unverified candidate hits are not source-form assignments.'),('search-identity-round7.json',[68,72,73,79,85,95,97,107,109,115,120,121,122],'Additional bounded primary-source search; absence within this query is not global ontology absence.')]:
 evidence('b2-'+fn.removesuffix('.json'),B/'captures'/fn,'local_validation' if fn in ['primary-web-round4.json','primary-web-round9.json'] else 'unsuccessful_search',claim,idx)
for key,idx,url,claim in [
 ('bd-oadc-name',[68],'https://www.bd.com/en-ca/products-and-solutions/products/product-page.212240','BD identifies BBL Middlebrook OADC,6x100mL. This corroborates named branded preparation, not the recipe-selected pack code or complete formula.'),
 ('chromium-hydrate-supplier',[99],'https://www.sigmaaldrich.com/US/en/product/aldrich/342432','Sigma identifies chromium(III) sulfate hydrate Cr2(SO4)3·xH2O,CAS15244-38-9. Formula weight is explicitly anhydrous basis and must not become actual hydrate molecular weight.'),
 ('larch-supplier',[102],'https://www.sigmaaldrich.com/US/en/product/sigma/10830','Supplier identifies larch-wood arabinogalactan. Its catalogue number, assay and water limit are comparison evidence and are not assigned to source M2313.'),
 ('feedta-canada',[125],'https://www.canada.ca/en/environment-climate-change/services/evaluating-existing-substances/screening-assessment-edta-salts.html','Government substance assessment identifies ammonium ferric EDTA,CAS21265-50-9. Pair with exact NLM ammonium-salt concept, not parent Fe-EDTA anion.')]:
 evidence('b2-'+key,B/'captures/primary-web-round4.json','primary_source',claim,idx,url,'2026-11-08T05:55:45Z')
evidence('b2-pipes-supplier',B/'captures/primary-web-round9.json','primary_source','Sigma primary product/SDS calls free-acid CAS5625-37-6 PIPES, while salt products are explicitly labelled salts. The recipe catalogue number is not inferred.',[84],'https://www.sigmaaldrich.com/BR/en/product/sigma/p6757','2026-11-08T06:00:08Z')
evidence('b2-oadc-authors',B/'captures/primary-web-round9.json','primary_source','Original protocol authors expand OADC as a mixture containing oleic acid,albumin,dextrose,catalase and list BD212240 as commercial alternative. Only named constituent scope is used; exact commercial quantities are not transferred.',[68],'https://www.researchgate.net/publication/46111859_Laboratory_Maintenance_of_Mycobacterium_abscessus','2026-11-08T06:00:08Z')
evidence('b2-native-mesh',R/'continuation-1201-v1/validation/native-mesh-concepts.json','local_validation','Production native OAK resolves exact concepts M0315963 ferric sulfate hexahydrate and M0313825 Fe(III)-EDTA ammonium salt; descriptor parents are broader.',[72,125])
evidence('b2-native-atp-selenite-scope',R/'continuation-1201-v1/validation/native-atp-selenite-scope-details.json','local_validation','Read-only local ontology statements and ignored-inclusive actual owner search: CHEBI50732 has water-free disodium structure/CAS987-65-5; CHEBI48843 has sodium:selenite2:1 formula and distinct pentahydrate CHEBI131361. Bounded MeSH search did not establish hydration-unspecified disodiumATP identity. This is not a global ontology-absence proof.',[74,79])
evidence('b2-approval-refusal',B/'approval-refusal.json','unsuccessful_search','Automatic approval refused a new primary-download batch; no retry. Existing source evidence remains usable. The refusal is not a scientific absence claim.',[68,84,97])
for i in D:
 D[i]['scope_index']=i
def primary(i):return [e for e in DOS[i]['primary_evidence'] if e['kind']=='primary_source']
def sourceurl(i):return '; '.join(dict.fromkeys(e['url'] for e in primary(i)))
def evfor(indices):return list(dict.fromkeys(eid for i in indices for eid in D[i]['evidence_ids']))
def note(i,text,status='revised',missing=None,nochange=None,disposition=None):
 d=D[i];old=d['reasoning'];d['reasoning']=text
 d['applicability']=f'All {len(d["occurrence_ids"])} frozen occurrences and full recipe snapshots reviewed. '+text+' Exact occurrence scope is preserved; source transcription/receiving-medium errors remain separate publication holds. No downstream release, synchronization or rebuild is approved.'
 if disposition:d['disposition']=disposition
 d['missing_requirement']=missing;d['no_change_reason']=nochange
 ledger.append({'scope_index':i,'case_id':d['case_id'],'previous_reasoning':old,'assessment':text,'status':status,'scientific_missing_fact':missing,'occurrence_ids':d['occurrence_ids'],'publication_holds':'All original source/downstream holds remain; proposal review does not approve a receiving-medium dose or global owner release.'})
def components(items):
 out=[]
 for item in items:
  name,cid,*qty=item
  c={'component_name':'water' if cid=='CHEBI:15377' else name,'reference_scope':'MIM_CATALOG' if cid else 'UNMAPPED'}
  if cid:c['component_id']=cid
  if qty:c.update(concentration_value=qty[0],concentration_unit=qty[1])
  out.append(c)
 return out
def base(identifier,name,indices,notes,itype='SINGLE_INGREDIENT',target=None,label=None,quality='EXACT_MATCH'):
 target=target or identifier; label=label or name
 return {'identifier':identifier,'preferred_term':name,'mapping_status':'MAPPED','ingredient_type':itype,
 'ontology_mapping':{'ontology_id':target,'ontology_label':label,'ontology_source':('kgmicrobe.ingredient' if target.startswith('kgmicrobe.ingredient:') else 'MESH' if target.startswith('mesh:') else 'CHEBI'),'mapping_quality':quality,
 'evidence':[{'evidence_type':'MANUAL_CURATION','source':sourceurl(indices[0]),'notes':notes}]},
 'notes':notes,
 'curation_history':[{'timestamp':NOW,'curator':'codex_worker02_issue1201_source_review','action':'CREATED','changes':notes+' Isolated proposal, pending independent and coordinator review.','new_status':'MAPPED','llm_assisted':True}]}
def proposal(key,indices,record,description,owner=None,occurrences=None):
 owner=owner or 'data/ingredients/mapped/'+key+'.yaml'
 old=Path(owner);before=None
 if old.exists():
  before=sha(old);(B/'before'/old.name).write_bytes(old.read_bytes())
  evidence('b2-owner-'+key,B/'before'/old.name,'local_validation','Exact current owner bytes inspected before this isolated edit.',indices)
 versioned={'magnesium_sulfate_heptahydrate_6gl_togo_m2231','sodium_bicarbonate_solution3_jcm414','selenite_tungstate_atcc2686','chromium_sulfate_variable_hydrate'}
 after=B/'after'/(Path(owner).stem+'-v2.yaml' if key in versioned else Path(owner).name)
 write_validated_ingredient(record,after)
 p={'proposal_id':'b2-proposal-'+key,'case_ids':[D[i]['case_id'] for i in indices],'description':description,'evidence_ids':evfor(indices),'owner_path':owner,'kind':'edit_existing_owner' if before else 'new_owner','before_sha256':before,'after_capture':cap(after),'integration_obligations':['Independent skeptical and native review of these exact bytes before application.','Preserve original source labels and all source/receiving-medium holds. No automatic global matching from a source pointer.','Compare other workers proposals and any predecessor proposal for this owner; combine from original baseline rather than overwrite.'], 'historical_finding_ids':[]}
 if occurrences:p['applicable_occurrence_ids']=occurrences
 P.append(p)
 for i in indices:D[i]['proposal_ids'].append(p['proposal_id'])
 return p
def stock(key,indices,name,items,notes,solution='MINERAL_STOCK',method='LABEL_ENUMERATION',complete='UNKNOWN',occurrences=None):
 text=notes+' Component completeness is '+complete+'. Unstated solvent, hydration, assay and final volume are not invented. This is the named preparation at the cited source scope; no full-formulation equivalence with other products is asserted.'
 rec=base('kgmicrobe.ingredient:'+key,name,indices,text,'STOCK_SOLUTION',quality='FALLBACK_REGISTRY')
 rec['solution_type']=solution;rec['components']=components(items)
 rec['component_assertion']={'method':method,'completeness':complete,'evidence':[{'evidence_type':'RECIPE_SOURCE','source':sourceurl(i),'source_record':D[i]['source']['source_label'],'notes':notes} for i in indices]}
 return proposal(key,indices,rec,text,occurrences=occurrences)

# Each stock was read with its own primary recipe; concentration is source-stated.
STOCKS=[
 ('sodium_carbonate_8_percent_wv_jcm1023_363',[63],'8% w/v sodium carbonate stock (JCM1023/363)', [('Na2CO3','CHEBI:29377','8','PERCENT_W_V')], 'JCM1023 and363 explicitly name 8% w/v Na2CO3 stock and add 2.5mL. Frozen2.5G_PER_L is a receiving-medium transcription error, not a bar to recording the stock. Water elsewhere in the medium does not identify this stock solvent.'),
 ('ferrous_sulfate_heptahydrate_02_percent_wv_togo_m2649',[70],'0.2% w/v ferrous sulfate heptahydrate stock (TOGO M2649)', [('FeSO4 x 7 H2O','CHEBI:75836','0.2','PERCENT_W_V')], 'TOGO M2649 explicitly specifies sterile anoxic FeSO4x7H2O0.2%w/v stock,10mL addition. Current DSMZ503 states0.1%; retain that source-version conflict and qualify this proposal to the captured M2649 formulation.'),
 ('methanol_50_percent_vv_jcm_sources',[75],'50% v/v methanol stock (JCM1146/1147/1173/1174/1176/1415)', [('Methanol','CHEBI:17790','50','PERCENT_V_V')], 'All six frozen occurrences state50%v/v methanol preparation; original JCM or direct TOGO source corroborates the stated strength, including M1256 for JCM1173. Sterilization alternatives are source-specific procedures and are not chosen or generalized. No solvent is identified in the stock statement.'),
 ('ferrous_sulfate_002m_nbrc213',[80],'0.02 M FeSO4 stock (NBRC213)', [('FeSO4 (hydration unspecified)',None,'0.02','M')], 'NBRC213 explicitly calls for2.5mL of FeSO4(0.02M). The stock concentration is known; reagent hydration and solvent are not. The component therefore remains UNMAPPED rather than asserting anhydrous or heptahydrate identity.'),
 ('magnesium_sulfate_heptahydrate_10_percent_jcm987',[83],'10% magnesium sulfate heptahydrate stock (JCM987)', [('MgSO4 x 7 H2O','CHEBI:31795','10','PERCENT')], 'JCM987 specifies10%MgSO4·7H2O and50mL of this stock among separately sterilized solutions. The percent basis is unspecified; no w/v or v/v conversion is made.'),
 ('magnesium_sulfate_heptahydrate_6gl_togo_m2231',[86],'6 g/L magnesium sulfate heptahydrate stock (TOGO M2231)', [('MgSO4 x 7 H2O','CHEBI:31795','6','G_PER_L'),('Distilled water','CHEBI:15377')], 'M2231 explicitly labels the stock6g/L and lists6gMgSO4·7H2O plus1Ldeionized water. The6g/L assertion comes from the source label, not a final-volume inference from added water. Water quantity is preserved only as added batch water in this note. The separate PIV metal-solution make-up instruction is not applied to this stock.'),
 ('sodium_resazurin_01_percent_wv_jcm363_1023',[88,93],'0.1% w/v sodium resazurin stock (JCM363/1023)', [('Resazurin sodium salt',None,'0.1','PERCENT_W_V')], 'JCM363 and1023 explicitly specify sodium resazurin0.1%w/v stock,1mL addition. The doubled hyphen in one frozen label is typographic; neither stock is free-acid resazurin. Sodium-salt component is retained UNMAPPED because a verified active exact salt target has not been established; that does not block the whole preparation.'),
 ('sulfuric_acid_2n_dsmz29_40_206_897',[90,106],'2 N sulfuric acid preparation (DSMZ29/40/206/897)', [('H2SO4','CHEBI:26836','2','N')], 'The cited DSMZ recipes explicitly prescribe2N sulfuric acid in their titration or preparation steps. Normality is retained as stated; no molarity, density or solvent is inferred. Individual receiving-medium additions and process contexts remain source-specific.'),
 ('sodium_bicarbonate_solution3_jcm414',[92],'Sodium bicarbonate Solution3 (JCM414)', [('NaHCO3','CHEBI:32139'),('Distilled water','CHEBI:15377')], 'JCM414/TOGO M412 specify2gNaHCO3 plus40mLdistilled water for filter-sterilized Solution3. These are batch amounts; no concentration is computed from added water. JCM also annotates5% without a basis. The pointer Sol.3 is not made a global resolving alias.'),
 ('magnesium_sulfate_1m_togo_m2790',[101],'1 M MgSO4 stock (TOGO M2790 M9)', [('MgSO4 (hydration unspecified)',None,'1','M')], 'The primary M2790 M9 table explicitly adds200µL of1MMgSO4 in a recipe with100mLsource basis. Frozen200G_PER_L is incorrect and remains a source-data hold. The1M stock is independently representable; hydration and solvent are unreported and are not guessed.'),
 ('selenite_tungstate_atcc2686',[103],'Selenite-tungstate solution (ATCC2686)', [('NaOH','CHEBI:32145'),('Na2SeO3 x 5 H2O','CHEBI:131361'),('Na2WO4 x 2 H2O','CHEBI:63939'),('Distilled water','CHEBI:15377')], 'ATCC2686 gives batch amounts0.5gNaOH,3mgNa2SeO3·5H2O,4mgNa2WO4·2H2O and1Ldistilled water. Added water does not establish final volume, so all component concentration fields are omitted. Fresh JCM431 comparison instead gives0.4g,6mg,8mg and1Lwater, so the existing JCM431 owner and competing worker proposals are not this formula. No winner is selected among external proposals.'),
 ('ferrous_sulfate_heptahydrate_02_percent_atcc1340',[104],'0.2% ferrous sulfate heptahydrate stock (ATCC1340)', [('FeSO4 x 7 H2O','CHEBI:75836','0.2','PERCENT')], 'ATCC1340 explicitly specifies0.2%FeSO4·7H2O stock and0.4mL addition. Percent basis and stock solvent are unspecified. Do not equate this with M2649 explicit w/v formulation or infer full formulation from the receiver.'),
 ('sulfuric_acid_025n_nbrc1379',[110],'0.25 N sulfuric acid preparation (NBRC1379)', [('H2SO4','CHEBI:26836','0.25','N')], 'NBRC1379 uses1Lof0.25NH2SO4 to prepare SolutionII containing400gFeSO4·7H2O. This owner denotes the acid preparation supplied to that mixture, not the resulting iron solution. No final-volume or normality-to-molarity conversion is made.'),
 ('concentrated_sulfuric_acid_togo_m2241',[111],'Concentrated sulfuric acid preparation (TOGO M2241)', [('H2SO4','CHEBI:26836')], 'M2241 DH micronutrient solution explicitly uses0.5mLconcentrated H2SO4. Source names a concentrated preparation but supplies no numerical assay, water amount or density. Represent only this source-qualified material; no97%,98% or standard molarity is invented.'),
 ('concentrated_sulfuric_acid_jcm970_atcc920',[113],'Concentrated sulfuric acid preparation (JCM970/ATCC920 source scope)', [('H2SO4','CHEBI:26836')], 'TOGO M1020/JCM970 specifies2mLconcentrated sulfuric acid; ATCC920-derived M3142/M3140 micronutrient stocks specify0.5mL. This bounded named-material record captures only the shared stated concentrated-acid description; no equal assay or full-formulation equivalence is claimed between the source preparations.'),
 ('sulfuric_acid_10n_named_sources',[114,118],'10 N sulfuric acid preparation (cited DSMZ/JCM/ATCC/TOGO sources)', [('H2SO4','CHEBI:26836','10','N')], 'All seven occurrences explicitly prescribe10NH2SO4 for source-specific pH adjustment or preparation. Primary TOGO sources cover M2680,M2734,M377,M84,M2668 andM3239; the JCM382-derived occurrence retains its original recipe linkage. Normality is source-stated and does not require a guessed solvent or conversion to molarity.'),
 ('concentrated_sulfuric_acid_atcc203',[116],'Concentrated sulfuric acid preparation (ATCC203/TOGO M2236)', [('H2SO4','CHEBI:26836')], 'ATCC203/TOGO M2236 SolutionC lists0.05mLconcentrated H2SO4 alongside0.5gFeSO4·7H2O,0.14gEDTA and100mLwater. Those other constituents belong to SolutionC, not the supplied concentrated acid. Assay and solvent composition of the acid are unspecified.'),
 ('mohr_salt_02_percent_hcl0037_percent_jcm764',[119],'0.2% Mohr salt in0.037% HCl stock (JCM764)', [('Fe(NH4)2(SO4)2 x 6 H2O','CHEBI:76181','0.2','PERCENT'),('HCl','CHEBI:17883','0.037','PERCENT')], 'JCM764 explicitly specifies0.2%(NH4)2Fe(SO4)2·6H2O in0.037%HCl, with1mLstock addition. Both percent bases are unstated. Two known components are recorded without inventing water or treating the mixture as Mohr salt itself.'),
 ('resazurin_0025_percent_atcc_chopped_meat',[126],'0.025% resazurin solution (ATCC chopped-meat medium)', [('Resazurin (salt form unspecified)',None,'0.025','PERCENT')], 'ATCC chopped-meat recipe calls for4mLof0.025%resazurin solution. Percent basis, counterion and solvent are not given. The named preparation is representable with an UNMAPPED resazurin component and UNKNOWN completeness, without pretending it is a pure neutral or sodium reagent.'),
 ('concentrated_sulfuric_acid_utex_bbm',[127],'Concentrated sulfuric acid preparation (UTEX BBM trace stock)', [('H2SO4','CHEBI:26836')], 'UTEX BBM trace stock explicitly lists10mLconcentrated H2SO4 and makes the total trace-stock volume1L. That establishes the acid volume per litre of trace stock, not the acid assay. This owner captures the supplied concentrated acid with no assumed97/98% strength.'),
]
acid_notes=' '.join(s[4] for s in STOCKS if s[0].startswith('concentrated_sulfuric_acid_'))
STOCKS=[s for s in STOCKS if not s[0].startswith('concentrated_sulfuric_acid_')]
STOCKS.append(('concentrated_sulfuric_acid_assay_unspecified',[111,113,116,127],'Concentrated sulfuric acid preparation (assay unspecified)',[('H2SO4','CHEBI:26836')],acid_notes+' Source IDs do not establish distinct substances, so one bounded unspecified-assay material is proposed. This shared record asserts only the common named preparation, not equal commercial assay or interchangeability of unknown formulations.'))
for key,idx,name,parts,n in STOCKS:
 stock(key,idx,name,parts,n,method='RECIPE_TRANSCRIPTION' if len(parts)>1 else 'LABEL_ENUMERATION')
 for i in idx:note(i,n+' A source-supported isolated stock proposal now replaces the previous unperformed-curation deferral.',disposition='stock_product_mixture_context')

# Named branded material, without assuming the missing catalogue code is fatal.
n='JCM386 and714 explicitly supply BD-BBL Middlebrook OADC enrichment. BD confirms the named BBL product. OADC constituent scope is corroborated by the primary protocol authors; no precise commercial formula, lot or recipe-selected pack code is asserted. The existing generic/Difco OADC owner is not silently made identical to this branded material.'
stock('middlebrook_oadc_bd_bbl',[68],'Middlebrook OADC enrichment (BD-BBL)', [('Oleic acid','CHEBI:16196'),('Albumin',None),('Dextrose',None),('Catalase','cas:9001-05-2')],n,solution='OTHER',method='ABBREVIATION_EXPANSION')
note(68,n+' Missing lot-level formulation does not block this bounded preparation proposal.',disposition='stock_product_mixture_context')

n='NBRC1025 explicitly supplies Fe2(SO4)3·6H2O0.01g. Primary NLM C024823 distinguishes exact narrower concept M0315963 ferric sulfate hexahydrate,CAS13761-89-2 from generic and other hydrate concepts. Native exact-label validation passes. The earlier CHEBI-only search gap is closed.'
rec=base('mesh:M0315963','Ferric sulfate hexahydrate',[72],n,label='ferric sulfate hexahydrate')
rec['chemical_properties']={'cas_rn':'13761-89-2','molecular_formula':'Fe2(SO4)3.6H2O','data_source':'Primary NLM C024823 narrower concept M0315963 and NBRC1025'}
rec['synonyms']=[{'synonym_text':D[72]['source']['raw_source_label'],'synonym_type':'EXACT_SYNONYM','source':sourceurl(72)}]
proposal('Ferric_sulfate_hexahydrate',[72],rec,n)
note(72,n,disposition='new_distinct_ingredient_proposal')

n='TOGO M1052 explicitly names PIPES(Sigma),6g. Current Sigma primary documentation calls CAS5625-37-6 PIPES; sodium salts are separately labelled. Existing Pipes.yaml already denotes this precise PIPES free-acid name. No source catalogue code is inferred. The earlier catalogue-number-only deferral is not a scientific blocker.'
path=Path('data/ingredients/mapped/Pipes.yaml');rec=yaml.safe_load(path.read_text())
rec.setdefault('synonyms',[]).append({'synonym_text':'PIPES (Sigma)','synonym_type':'EXACT_SYNONYM','source':sourceurl(84)})
rec.setdefault('curation_history',[]).append({'timestamp':NOW,'curator':'codex_worker02_issue1201_source_review','action':'ADDED_SYNONYMS','changes':n,'llm_assisted':True})
proposal('pipes_sigma',[84],rec,n,str(path));note(84,n,disposition='existing_identity_or_alias')

n='The directly inspected frozen CultureMech recipes explicitly name Silicone antifoam(BDH), with source-specific citations and preserved excerpts attributed to Verduyn1992 andFlikweert1996. The original PDFs were not independently retrieved: timeouts and an explicit approval refusal are recorded. The bounded material is the BDH silicone-antifoam preparation reported by those recipe records, not a verified catalogue number, silicone molecular species or fixed-strength emulsion. Original quotation verification remains an operational publication-evidence limitation.'
rec=base('kgmicrobe.ingredient:silicone_antifoam_bdh_reported','Silicone antifoam (BDH; reported recipe material)',[97],n,'UNDEFINED_MIXTURE',quality='FALLBACK_REGISTRY')
rec['ontology_mapping']['evidence'][0]['source']='CultureMech:010555; CultureMech:010556; CultureMech:010557; CultureMech:010558; frozen source snapshots in b/captures/case-97.json'
rec['components']=components([('Silicone material (composition unspecified)',None)])
rec['component_assertion']={'method':'LABEL_ENUMERATION','completeness':'UNKNOWN','evidence':[{'evidence_type':'RECIPE_SOURCE','source':'CultureMech frozen case '+D[97]['case_id'],'source_record':'All four exact recipe snapshots bound by b-case-97 and b-recipe-97-*','notes':n}]}
proposal('silicone_antifoam_bdh_reported',[97],rec,n)
note(97,n,disposition='stock_product_mixture_context',missing='Independently retrieve original Verduyn/Flikweert pages before asserting their quotations were directly verified. No exact catalogue/strength is required for the bounded reported-material proposal.')

n='JCM1182 explicitly supplies Cr2(SO4)3·xH2O. The actual Cr2_So43_X_N_H2o.yaml already represents the same variable hydrate, so no duplicate is created. Sigma primary specification identifies CAS15244-38-9 for Cr2(SO4)3·xH2O. Fresh OLS search did not establish an exact hydrate ontology term; retain CHEBI53471 chromium(III)sulfate only as asymmetric parent. Sigma anhydrous-basis molecular weight and fixed-hydrate widgets are not copied. Existing role/release obligations remain open.'
path=Path('data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml');rec=yaml.safe_load(path.read_text());rec['identifier']='cas:15244-38-9'
rec['chemical_properties']={'cas_rn':'15244-38-9','molecular_formula':'Cr2(SO4)3.xH2O','data_source':'Sigma342432 primary variable-hydrate specification; no fixed hydrate or anhydrous-basis molecular weight imported'}
rec.setdefault('synonyms',[]).append({'synonym_text':D[99]['source']['raw_source_label'],'synonym_type':'EXACT_SYNONYM','source':sourceurl(99)})
rec.setdefault('curation_history',[]).append({'timestamp':NOW,'curator':'codex_worker02_issue1201_source_review','action':'CORRECTED','changes':n,'llm_assisted':True})
for ev in rec['ontology_mapping'].get('evidence',[]):
 if 'no exact ChEBI term or own CAS' in ev.get('notes',''):
  ev['notes']='HISTORICAL ASSERTION, SUPERSEDED for CAS/primary-ID scope by the 2026-11-08 continuation: '+ev['notes']+' Current source-verified CAS15244-38-9 replaces the previous no-own-CAS/local-primary conclusion; the asymmetric anhydrous-parent relation remains.'
rec['ontology_mapping'].setdefault('evidence',[]).append({'evidence_type':'MANUAL_CURATION','source':'https://www.sigmaaldrich.com/US/en/product/aldrich/342432','notes':n})
proposal('chromium_sulfate_variable_hydrate',[99],rec,n,str(path));note(99,n,disposition='existing_identity_or_alias')

n='TOGO M2313 explicitly names larch arabinogalactan as an alternative carbon substrate at0.2%, with percent basis unspecified. Larch provenance differentiates the material from unrestricted arabinogalactan. Sigma primary botanical material confirms that larch-wood arabinogalactan is a meaningful purchasable material; its catalogue, assay, species and extraction process are not assigned to this recipe. The closest verified ontology parent is CHEBI27569 arabinogalactan; natural-polymer identity is not decomposed into free monosaccharides.'
rec=base('kgmicrobe.ingredient:larch_arabinogalactan','Larch arabinogalactan',[102],n,target='CHEBI:27569',label='arabinogalactan',quality='NARROW_MATCH')
rec['synonyms']=[{'synonym_text':D[102]['source']['raw_source_label'],'synonym_type':'EXACT_SYNONYM','source':sourceurl(102)}]
proposal('Larch_arabinogalactan',[102],rec,n);note(102,n,disposition='new_distinct_ingredient_proposal')

n='DSMZ632/1181 and their source-derived frozen recipes weigh ammonium ferric EDTA; public P10 explicitly reports that named reagent within a trace stock but remains an uncurated user dataset. Primary NLM M0313825 specifically denotes Fe(III)-EDTA,ammonium salt; C019179 parent descriptor includes other salts and is not exact. Canada substance assessment corroborates CAS21265-50-9. DSMZ1132 instead explicitly specifies Fe-NH4EDTA(4mg/ml),1.0ml; its four frozen derivatives refer to a stock, not weighed pure salt. Propose separate exact salt and source-qualified4mg/mLstock, preserving raw label ambiguity and receiving-medium errors.'
salt_occ=[o['occurrence_id'] for o in DOS[125]['case']['occurrences'] if o['recipe_id'] not in ['CultureMech:003842','CultureMech:003841','CultureMech:000568','CultureMech:011657']]
stock_occ=[o['occurrence_id'] for o in DOS[125]['case']['occurrences'] if o['occurrence_id'] not in salt_occ]
rec=base('mesh:M0313825','Fe(III)-EDTA, ammonium salt',[125],n,label='Fe(III)-EDTA, ammonium salt')
rec['chemical_properties']={'cas_rn':'21265-50-9','data_source':'Primary Canada EDTA-salts assessment; exact NLM M0313825 ammonium-salt concept'}
p_salt=proposal('Ferric_ammonium_EDTA',[125],rec,n,occurrences=salt_occ)
p_stock=stock('ferric_ammonium_edta_4mgml_dsmz1132',[125],'Ferric ammonium EDTA4mg/mL stock (DSMZ1132)',[('Fe(III)-EDTA, ammonium salt','mesh:M0313825','4','MG_PER_ML')],n,occurrences=stock_occ)
p_stock['integration_obligations'].append('Atomic dependency on '+p_salt['proposal_id']+': component MIM_CATALOG resolves in the joint proposed overlay only, not the current maintained catalogue. Do not apply the stock alone.')
note(125,n,disposition='stock_product_mixture_context')
D[125]['occurrence_dispositions']=[{'occurrence_ids':salt_occ,'proposal_ids':[p_salt['proposal_id']],'scope':'Named weighed ammonium ferric EDTA reagent; no exact commercial grade inferred.'},{'occurrence_ids':stock_occ,'proposal_ids':[p_stock['proposal_id']],'scope':'DSMZ1132 explicit4mg/mL stock; source-derived quantities remain separate.'}]

# Completed source-scoped corrections require no false global chemical alias.
corrections={
64:('TOGO M2277 explicitly names cobalt dichloride hexahydrate alongside CoCI2.6H2O. Correct the capital-I typography only within this occurrence; CHEBI53503 is the named hexahydrate. The malformed formula is not a global synonym.','data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml'),
66:('Primary NBRC1126 says KAl(SO4)2·12H2O, not the frozen2H2O. This is a completed source correction to the existing12-hydrate identity, not evidence for a dihydrate.','data/ingredients/mapped/Alkso42_X_12_H2o.yaml'),
67:('Original DSMZ141/141c/282/718 and935b via141 establish potassium aluminium sulfate dodecahydrate. AIK uses capitalI in place of lowercase l. Preserve literal provenance and correct only these source contexts.','data/ingredients/mapped/Alkso42_X_12_H2o.yaml'),
76:('M2262 names cadmium nitrate tetrahydrate while its display formula omits the nitrate coefficient2. Existing Cd_No32_X_4_H2o.yaml and fresh official CHEBI86156 already cover the named tetrahydrate. Missing second nitrate is a source typo, not a new chemical or admissible exact alias.','data/ingredients/mapped/Cd_No32_X_4_H2o.yaml'),
91:('Original DSMZ1250 explicitly prints calcium nitrate tetrahydrate, correcting the frozen five-water token. The existing tetrahydrate owner supplies the exact corrected identity; do not mint calcium nitrate pentahydrate from the corrupted token.','data/ingredients/mapped/Ca_No32_X_4_H2o.yaml'),
98:('Original NIES source marks manganese sulfate pentahydrate with footnote1). Its substitution note distinguishes250mgheptahydrate from217mgpentahydrate. Existing CHEBI131524 is the five-water substance; the marker is not part of a resolving chemical name.','data/ingredients/mapped/Mnso4_X_5_H2o.yaml'),
105:('UTEX identifies supplier Sigma574988, independently confirming (NH4)2Ni(SO4)2·6H2O. The raw NiSO4(NH4)SO4 formula is missing an ammonium coefficient and is not an exact synonym. Correct the source to the existing ammonium nickel sulfate hexahydrate identity.','data/ingredients/mapped/Niso4_Nh42so4_X_6_H2o.yaml'),
115:('DSMZ996/TOGO M2284 preserve malformed Ni2SO4x6H2O; M2284 separately and explicitly names Nickel(II)sulfate hexahydrate. That named constituent supports a source-scoped repair to NiSO4·6H2O. It does not establish a novel Ni2 salt or license adding the literal erroneous formula to global aliases. The original formula disagreement remains a publication correction obligation.',None),
120:('NBRC840 literal Fe(NH4)2SO4·6H2O omits a sulfate coefficient. TOGO M1637 separately names ammonium iron(II)sulfate hexahydrate, matching Mohr salt; this corroborates the bounded corrected constituent. Preserve the malformed source token and source correction obligation, without making it a chemical alias or changing existing Mohr owner identity.','data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml'),
121:('M2196 separately names Magnesium sulfate heptahydrate for its malformed Mg2SO4.7H2O row0.1g. The named constituent and charge-balanced formula support source-scoped correction to MgSO4·7H2O; no second-magnesium compound or invalid global alias is created. Source correction remains separate from interpreting stock/medium quantities.','data/ingredients/mapped/Mgso4_X_7_H2o.yaml'),
122:('M2405 BSM explicitly labels the malformed(NH4)SO4 row ammonium sulfate,2.38g. Its named constituent is(NH4)2SO4, not a new monoammonium sulfate. Record the source-scoped coefficient correction to the existing ammonium sulfate owner; preserve the literal error and do not add it globally.','data/ingredients/mapped/Nh42so4.yaml'),
129:('Original JCM448 explicitly states Mg(NO3)2·6H2O2.54g, settling the missing nitrate coefficient in the frozen label. This source correction points to the existing magnesium nitrate hexahydrate substance; no malformed resolving synonym or duplicate owner is needed.','data/ingredients/mapped/Magnesium_Nitrate_Hexahydrate.yaml')}
corrections[66]=(corrections[66][0],'data/ingredients/mapped/Alk_So42_X_12_H2o.yaml')
corrections[67]=(corrections[67][0],'data/ingredients/mapped/Alk_So42_X_12_H2o.yaml')
corrections[105]=(corrections[105][0],'data/ingredients/mapped/Nh42ni_So42_X_6_H2o.yaml')
corrections[115]=(corrections[115][0],'data/ingredients/mapped/Niso4_X_6_H2o.yaml')
for i,(text,path) in corrections.items():
 if path and Path(path).exists():
  owner={'path':path,'sha256':sha(path)}
  if owner not in D[i]['owner_records']:D[i]['owner_records'].append(owner)
  (B/'before'/Path(path).name).write_bytes(Path(path).read_bytes())
  evidence('b2-corrected-owner-'+str(i),B/'before'/Path(path).name,'local_validation','Actual corrected-identity candidate owner; source spelling correction alone does not approve whole owner release.',[i])
 note(i,text,status='completed_source_correction',nochange='The corrected named substance already has an owner; the remaining change belongs to the exact source occurrence. No scientifically valid new global synonym or distinct ingredient is warranted.',disposition='supplied_form_correction')

holds={
73:('NBRC109 andM2239 both specify adenine sulfate but do not give adenine:sulfate stoichiometry or hydration. Sigma A2545 hemisulfate is a verified candidate, not proof that either recipe selected it. A free-adenine owner is chemically incorrect; this is a genuine salt-form ambiguity rather than a missing-ontology-term excuse.','Source-specific salt stoichiometry/hydration or a supplier catalogue/author statement distinguishing the adenine sulfate form used.'),
74:('Original Merlen1999 Table1 explicitly gives ATP(Na2) for CultureMech007240, so the neutral ATP interpretation is false there. Exact CHEBI50732 denotes the disodium molecular salt, but the source does not settle hydrate/form; the other25 Zahorchak1982 source recipes specify ordinary ATP with no counterion. All scanned Zahorchak pages were previously inspected and are retained evidence; this is not an unavailable-paper claim. A single generic ATP owner or Na2 assignment across26occurrences would lose supplied-form distinctions.','For25Zahorchak occurrences, the ordinary ATP counterion/supplied form; forMerlen, confirmation of hydrate/supplied form before claiming an exact purchasable-form owner. The source-explicit disodium scope is retained and not discarded.'),
79:('ATCC source explicitly says Se-Salt(Na selenite), andM2555 labels sodium selenite. This establishes the sodium-selenite family but does not distinguish the separately represented anhydrous and pentahydrate supplied forms. No evidence supports sodium selenate, selenium acid or a stock concentration.','A source-specific supplied-form/hydration statement for the Na selenite reagent; do not transfer a generic supplier candidate into the recipe.'),
85:('NBRC830/831 and their TOGO counterparts explicitly repeat(NH4)2SO4·7H2O, including a heptahydrate name. No captured primary supplier/characterization source establishes that unusual solid as the supplied material. The seven waters cannot be deleted just because ordinary ammonium sulfate is familiar, and a proposed new chemical cannot be validated solely by repeated copying of the same suspicious recipe formula.','Primary preparation/characterization or source-author correction establishing the claimed ammonium sulfate heptahydrate or replacing the explicit seven-water formula.'),
95:('M1217/JCM1137-derived source explicitly names calcium nitrate hexahydrate,49.4mg. Fresh JCM1137 endpoint contains no medium table; shared MediaDive occurrence repeats the same source string and is not independent form verification. Calcium nitrate tetrahydrate is a distinct existing candidate, not a justified replacement.','Primary supplier/characterization or source-author correction establishing the six-water calcium nitrate form used by JCM1137.'),
107:('The MediaDive5240-derived frozen occurrence repeats calcium nitrate hexahydrate from the same JCM1137 lineage asB95. No independently inspected primary material specification establishes that six-water form; ordinary tetrahydrate cannot be substituted from familiarity.','Same source-specific calcium nitrate six-water characterization/supplier or author correction asB95; retain distinct occurrence identity.'),
109:('NBRC869 andM1666 say Dithionite(ca.),about20mg, and separately describe adding dithionite solution. The ca. qualifier means approximately, not calcium. Neither counterion nor a stock concentration is given, so the source does not specify which purchasable salt or preparation is intended.','Identify the dithionite counterion and the solution actually supplied, including strength if an exact stock identity is asserted; no calcium inference from ca..')}
holds[74]=(holds[74][0]+' Fresh local ontology statements show CHEBI50732 carries a water-free structure andCAS987-65-5; the bounded MeSH search found no established hydration-unspecified disodiumATP concept. This differs from chromium variable hydrate, whose source explicitly supplies xH2O. An invented variable-hydrate claim or disguised source-specific pure compound would not resolve the missing physical form.',holds[74][1])
holds[79]=(holds[79][0]+' Local ontology statements distinguish CHEBI48843,CAS10102-18-8,formula2Na.O3Se from CHEBI131361,pentahydrate,CAS26970-82-1. MeSHD018038 spans separate sodiumselenite, pentahydrate and monosodium concepts; the descriptor cannot be substituted as an exact generic purchased form. Existing common-name aliases are not independent evidence of what ATCC supplied.',holds[79][1])
for i,(text,missing) in holds.items():note(i,text,status='retained_scientific_hold',missing=missing,nochange='No exact supplied-form identity is established by the inspected evidence. The missing scientific fact is stated explicitly; broader ontology, catalogue or native release work is not the blocker.',disposition='unresolved')
D[74]['occurrence_dispositions']=[{'occurrence_ids':[DOS[74]['case']['occurrences'][0]['occurrence_id']],'scope':'Merlen Table1 explicitly establishes disodium ATP salt; hydration is unspecified. No claim of neutral ATP or verified water-free supplied form.'},{'occurrence_ids':[x['occurrence_id'] for x in DOS[74]['case']['occurrences'][1:]],'scope':'Zahorchak ordinary ATP counterion and hydration unspecified; original scans inspected, not unavailable.'}]

# Shared C-authored proposals; no duplicate payload or premature reviewer approval.
for i,pid,text in [(112,'c2-proposal-desiccated-ox-bile','NBRC1004/1390 explicitly name desiccated ox bile. Drying and animal-source scope support the existing dried-material owner without an inferred commercial grade; use the independently reviewed C-authored promotion of the actual owner.'),(117,'c2-proposal-emjh-enrichment','Original DSMZ1113 separately specifies EMJH enrichment100mL and EMJH base2.3g. The three frozen derivatives instead carry100G_PER_L twice and100PERCENT_V_V once; those receiving-quantity conflicts remain explicit holds and are not approved as100mL. The C-authored source-qualified enrichment proposal preserves the material/base separation, with known albumin/Tween80 constituents and PARTIAL completeness from manufacturer unspecified growth factors; no exact manufacturer-version equality is asserted.')]:
 D[i]['proposal_ids']=[pid]
 note(i,text,status='shared_proposal',disposition='stock_product_mixture_context')

assert sorted(x['scope_index'] for x in ledger)==sorted(D)
doc={'schema_version':1,'worker_slot':2,'shard_sha256':'993e393b8a50e6061e4a9863bd60b3ab2a48ee584907a97e3066c1cbc03d6db0','phase':'shard','subset_status':'primary_complete_pending_independent_review','decisions':[D[i] for i in sorted(D)]}
dump(B/'decisions.json',doc);dump(B/'evidence.json',{'schema_version':1,'evidence':E});dump(B/'proposals.json',{'schema_version':1,'proposals':P});dump(B/'reassessments.json',{'schema_version':1,'assessments':ledger})
dump(B/'progress.json',{'assigned_count':51,'structural_dossiers_reread':51,'scientific_reassessments_serialized':len(ledger),'guarded_proposals_written':len(P),'shared_C_proposals':2,'phase':'primary_complete_pending_independent_review','independent_review':'pending','timestamp':NOW})
print('serialized',len(ledger),'cases',len(P),'proposals')
