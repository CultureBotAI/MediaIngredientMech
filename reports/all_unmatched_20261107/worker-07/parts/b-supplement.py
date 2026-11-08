"""Explicit source transcriptions and final primary-evidence applicability.
Executed by b-build.py; all scientific selections below are manually reviewed.
"""
def attach(indices,eid):
 for i in indices:
  if eid not in decision(i)['evidence_ids']:decision(i)['evidence_ids'].append(eid)
def extra(indices,path,url,locator,support,at=None,kind='primary_source'):
 if at is None:at=json.loads((ROOT/path).read_text())['accessed_at']
 eid='B-EXTRA-'+str(indices[0])+'-'+hashlib.sha256((path+(url or '')).encode()).hexdigest()[:12]
 ev(eid,kind,path,locator,support,url,at,[decision(i)['case_id'] for i in indices]);attach(indices,eid)
 return eid
web='captures/b-web-original-followup2.json'
extra([76],web,'https://www.sigmaaldrich.com/PM/en/product/sigma/p3850','Sigma P3850 product title, CAS9049-37-0, sodium cation content','Supplier confirms sodium polygalacturonate polymer material, without establishing a particular catalog for DSMZ1265.')
extra([126],web,'https://www.sigmaaldrich.com/US/en/product/mm/108418','Merck TitriplexIII product CAS6381-92-6, formula and mass372.24','Together with exact SAG12/SAG19 Merck TitriplexIII references, establishes EDTA disodium dihydrate in these source contexts only.')
extra([132],web,'https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1382','SL10 table: H4MoNa2O6.2H2O','Original NBRC source repeats doubled hydration; does not authorize silent dihydrate correction.')
extra([139],web,'https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1042','Composition: Casein sodium0.5g','Original source preserves sodium caseinate material, not free casein or a digest.')
extra([110],'captures/a-source-d78eaec3d48cf38b.html','https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=900','Modified Hutner basal salts subrecipe','Complete nominal source recipe, malformed molybdate formula and JCM149 Metals44 cross-reference; reused exact original capture.',at='2026-11-08T05:06:38.116814+00:00')
p=ROOT/'captures/b-jcm1209.html'
extra([122],'captures/b-jcm1209.html','https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1209','Basal medium salts table','Original exact nominal source formulation; timestamp is file completion mtime of direct curl capture, not a newly claimed retrieval.',at=datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat())
for medium,rev in [('2467','626773d3f8cc455696560ff5fae01124'),('2485','d1fb01180e754ad4baee5b7f43c2402c')]:
 url='https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/'+'/'.join(medium)+'/atcc-medium-'+medium+'.pdf?rev='+rev
 extra([89],'captures/b-web-final-originals.json',url,'Solution A calcium chloride dehydrate line','Both exact ATCC originals repeat dehydrate; no numerical water count appears. Source spelling alone cannot prove dihydrate.')
for i in [90,116,137,138]:
 extra([i],'captures/b-web-final-attempts.json',None,'Recorded explicit searches and returned results','Attempt did not establish a reagent formula/product for the exact frozen source; search snippets and other BG11 recipes do not settle the original source identity.',kind='unsuccessful_search')
for r in json.loads((ROOT/'parts/b-final-retrievals.json').read_text()):
 if not r['success']:continue
 key=r['url'].split('=')[-1]
 indices={'M2809':[135],'M2760':[137],'M2499':[136,138],'M3120':[136],'M2601':[136],'M2367':[136],'CHEBI:64758':[126]}[key]
 extra(indices,r['path'],r['url'],'Complete primary response: meta source identity and all ingredient/subrecipe tables' if key.startswith('M') else 'CHEBI64758 label and identity annotations','Exact source independently retrieved after earlier timeout; applies only to its matching frozen recipe and formula. Empty src_url supplies no further original source attribution.',at=r['accessed_at'],kind='primary_source' if key.startswith('M') else 'ontology')
paper='captures/b-web-final-paper.json'
extra([117],paper,'https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=981','Original NBRC981 composition row 0.1M TrisHCl(pH7.5)50ml','Confirms original stock concentration and pH; detailed buffer preparation remains unreported.')
extra([136],paper,'https://assets.thermofisher.com/chem-specs-pdf/retrievePdf?rootSku=L11857&sku=L11857.22','Manufacturer disodium magnesiumEDTA hydrate formula and2.2–5waters loss-on-drying range','Demonstrates magnesium-containing salt and variable hydration exist. Does not establish this catalog was used in any of the four BG11 source recipes.')
extra([116],paper,'https://doi.org/10.1099/00221287-19-3-592','Schaechter1958 publisher abstract; full-text loading shell','Exact cited primary publication was accessed but exposed no reagent formula in the returned abstract/shell. Does not justify hydrate or sodium stoichiometry assignment.')
extra([116],paper,'https://pmc.ncbi.nlm.nih.gov/articles/PMC235284/','Browser challenge returned for Hassan1977 source','Original full-text attempt unsuccessful; cannot treat browser-challenge bytes as methods evidence.',kind='unsuccessful_search')
extra([116],paper,'https://pmc.ncbi.nlm.nih.gov/articles/PMC197015/','Browser challenge returned for Tseng1994 source','Original full-text attempt unsuccessful; no supplied-form inference from this response.',kind='unsuccessful_search')
decision(77)['reasoning']='All nine frozen occurrences preserve Fe2(SO4)3 x H2O. Original DSMZ188 independently repeats the ferric hydrate. The retrieved current DSMZ1053 recipe differs and uses ferrous sulfate heptahydrate in Wolin mineral solution; it cannot certify the historical frozen ferric-hydrate occurrence. CHEBI53438 is the non-hydrated iron(III) sulfate parent; xH2O is not sufficient evidence for a fixed water count.'
decision(137)['reasoning']+=' Directly retrieved TOGO M2760 repeats Na2MoO3 in Trace mineral and leaves src_url empty; no independent correcting source is supplied.'
decision(138)['reasoning']+=' Directly retrieved TOGO M2499 repeats CuSO2.5H2O; other separately captured BG11 recipes3120/2601/2367 use CuSO4.5H2O, but they are distinct records and cannot supply an authoritative correction for M2499.'
decision(138)['missing_requirement']='Authoritative correction or reagent identity for exact TOGO M2499, which itself repeats CuSO2.5H2O and has no original src_url. Other BG11 recipes with CuSO4.5H2O provide a candidate correction, not proof of source equivalence.'
# Include truthful failed retrieval provenance for each source case, never as support.
for fn in ['b-retrievals.json','b-extra-retrievals.json','b-curl-retrievals.json']:
 rs=json.loads((ROOT/'parts'/fn).read_text())
 for n,r in enumerate(rs):
  if r['success']:continue
  ids=[c for c in r.get('case_ids',[]) if c in primary_by_case]
  if not ids:continue
  eid='B-FAILED-'+fn.replace('.json','')+'-'+str(n)
  ev(eid,'unsuccessful_search','parts/'+fn,f'entry[{n}] '+r['url'],'Primary-source retrieval attempted but unavailable; failure is not evidence for or against identity.',r['url'],r['accessed_at'],ids)
  for cid in ids:
   next(d for d in D if d['case_id']==cid)['evidence_ids'].append(eid)
decision(89)['reasoning']+=' Directly opened ATCC2467 and2485 originals repeat dehydrate in SolutionA; the missing water count persists in the primary sources.'
decision(89)['missing_requirement']='ATCC clarification or product/formula evidence establishing the water count in SolutionA; the currently available original2467/2485 recipes repeat dehydrate without a formula.'
decision(125)['reasoning']=decision(125)['reasoning'].replace('ferric sulfate','ferrous sulfate')
decision(126)['no_change_reason']='Resolve only these two SAG occurrences to EDTA disodium dihydrate through their explicit Merck TitriplexIII specification. Do not add generic Disodium EDTA as a global hydrate-specific synonym.'
# New local identities preserve source recipes and never acquire generic resolving aliases.
def comp(name,value=None,unit=None,note=None):
 x={'component_name':name,'reference_scope':'UNMAPPED'}
 if value is not None:x.update(concentration_value=str(value),concentration_unit=unit)
 if note:x['source']=note
 return x
def stock(indices,stem,label,url,components,notes,completeness='COMPLETE',stype='MINERAL_STOCK'):
 ident='kgmicrobe.ingredient:'+stem
 assert not (REPO/'data/ingredients/mapped'/f'{stem}.yaml').exists()
 after={'identifier':ident,'preferred_term':label,'mapping_status':'MAPPED','ingredient_type':'STOCK_SOLUTION','solution_type':stype,'ontology_mapping':{'ontology_id':ident,'ontology_label':label,'ontology_source':'kgmicrobe.ingredient','mapping_quality':'FALLBACK_REGISTRY','evidence':[{'evidence_type':'MANUAL_CURATION','source':url,'notes':'Source-qualified nominal preparation identity; no exact chemical or generic-stock equivalence asserted.'}]},'components':components,'component_assertion':{'method':'RECIPE_TRANSCRIPTION','completeness':completeness,'evidence':[{'evidence_type':'RECIPE_SOURCE','source':url,'source_record':label,'notes':notes}],'notes':'Completeness concerns the source constituent list, not ontology resolution. UNMAPPED parts preserve literal source wording and do not assert an unsupported exact ID.'},'notes':notes+' Raw source labels retained in linked frozen cases: '+repr([CASES[i-70]['raw_source_label'] for i in indices])+'. Generic labels are not global resolving synonyms. No pre-existing WITHHOLD or REJECTED gate is lifted.'}
 history(after,'SOURCE_QUALIFIED_STOCK_PROPOSAL','Propose exact nominal source preparation with preserved quantities and explicit unresolved details; no maintained record changed.')
 after['curation_history'][-1].pop('previous_status',None)
 proposal(indices,stem,after,'Propose source-qualified nominal preparation: '+label,kind='new_owner',notes=notes)
 return 'B-PROPOSAL-'+stem
jcm=lambda n:'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD='+str(n)
togo=lambda n:'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M'+str(n)
g=lambda n,v:comp(n,v,'G_PER_SOURCE_BATCH')
mg=lambda n,v:comp(n,v,'MG_PER_SOURCE_BATCH')
ml=lambda n,v:comp(n,v,'ML_PER_SOURCE_BATCH')
stock([94],'jcm_1013_basal_medium','JCM1013 basal medium',jcm(1013),[g('KH2PO4','1.4'),g('NH4Cl','0.5'),g('MgCl2·6H2O','0.2'),g('CaCl2·2H2O','0.15'),mg('Resazurin','1.0'),ml('Distilled water','950.0')],'Exact JCM1013 basal subrecipe, excluding separately dosed vitamins, trace salts, reductant and carbon source. Amounts per printed batch;950ml is added water, not an asserted measured final volume. Resazurin salt form unreported.')
stock([94],'jcm_431_basal_medium','JCM431 basal medium',jcm(431),[g('NaCl','1.0'),g('MgCl2·6H2O','0.4'),g('CaCl2·2H2O','0.075'),g('NH4Cl','0.25'),g('KH2PO4','0.2'),g('KCl','0.5'),comp('Distilled water','1.0','L_PER_SOURCE_BATCH')],'Exact JCM431 basal subrecipe only. This differs from JCM1013 despite the shared raw label. Retain1L addedwater without normalizing source salt quantities.')
stock([102],'jcm_946_korthof_10x_basal_medium','JCM946 Korthof 10x basal medium',jcm(946),[g('NaCl','7.0'),g('Na2HPO4','4.4'),g('Polypeptone peptone (BD-BBL)','4.0'),g('KH2PO4','1.2'),g('NaHCO3','0.1'),g('KCl','0.2'),g('CaCl2·2H2O','0.2'),comp('Distilled water','500.0','ML_PER_SOURCE_BATCH','450ml main batch plus50ml separately prepared calcium chloride solution per original JCM946 instructions.')],'Complete nominal source inputs. Mix ingredients except calcium chloride and autoclave; dissolve calcium chloride in50ml water and filter sterilize, then combine after cooling. The500ml water is the explicit450+50ml sum, not a measured finalvolume. Excludes rabbit serum/final medium dilution.',stype='COMPLEX_UNDEFINED')
stock([106],'togomedium_m2405_basal_salts_medium','TogoMedium M2405 basal salts medium',togo(2405),[comp('Distilled water','1','L_PER_SOURCE_BATCH'),g('MgSO4 . 7H2O','0.25'),g('NaCl','0.5'),g('KH2PO4','1.36'),mg('FeSO4 . 7H2O','0.28'),g('(NH4)SO4','2.38'),g('Na2HPO4','1.42'),mg('CaCl2 . 7H2O','10.69'),comp('Agar','1.5','PERCENT_BASIS_UNSPECIFIED')],'Literal M2405 BSM subrecipe, used90%v/v with10%LB. Formula (NH4)SO4 and unusual CaCl2.7H2O remain unresolved, not silently repaired. Agar percentage basis unreported. No chemical equivalence to a conventional BSM is asserted.')
stock([107],'jcm_1305_reconstituted_vitox','JCM1305 reconstituted Oxoid Vitox',jcm(1305),[comp('Oxoid Vitox supplement','1','VIAL_PER_SOURCE_BATCH'),ml('Rehydration fluid','10')],'JCM1305 specifies one Oxoid Vitox vial reconstituted in10ml rehydrationfluid, then2ml added per100ml medium. Product catalog and proprietary constituent identities remain unreported; complete preparation-input list does not establish a complete molecular composition.',stype='COMPLEX_UNDEFINED')
stock([110],'jcm_900_modified_hutner_basal_salts','JCM900 modified Hutner basal salts',jcm(900),[g('Nitrilotriacetic acid (NTA)','10.0'),g('MgSO4·7H2O','29.7'),g('CaCl2·2H2O','3.335'),mg('(NH4)6MoO24·4H2O','9.25'),mg('FeSO4·7H2O','99.0'),ml("Metals 44 (JCM149)",'50.0'),ml('Distilled water','950.0'),g('KOH','about7.3'),comp('NaOH or H2SO4',note='Alternative pH readjustment reagents; source does not require both.')],'DissolveNTA;adjustpH7.0withKOHabout7.3g;addsalts;readjustpH6.8withNaOHorH2SO4. Literal malformed(NH4)6MoO24.4H2O retained (missingMo7 cannot be inferred). JCM149 Metals44 nested mixture remains unexpanded. COMPLETE means source inputs retained, not complete resolved chemistry.')
stock([112],'togomedium_m2653_cysteine_sulfide_reducing_agent','TogoMedium M2653 cysteine-sulfide reducing agent',togo(2653),[ml('12.5% Na2S stock solution','40'),ml('Distilled water','330'),ml('N NaOH','30'),g('L-Cysteine . HCl','5')],'Exact M2653 mixture underN2 atmosphere. Sodium-sulfide percentbasis and hydrate are unreported; literal NNaOH retained as printed. Does not claim identity with the separateM2707 occurrence, whose original retrieval failed. Gas atmosphere is preparation context, not a quantified dissolved constituent.')
stock([122],'jcm_1209_basal_salts_solution','JCM1209 basal salts solution',jcm(1209),[mg('NH4NO3','50.0'),mg('MgCl2·6H2O','8.5'),mg('SiO2','7.5'),mg('MnSO4·xH2O','4.5'),mg('CaCl2·2H2O','4.2'),mg('Methylene blue','4.0'),mg('FeSO4·7H2O','1.8'),comp('Distilled water','1.0','L_PER_SOURCE_BATCH')],'Exact original JCM1209 stock,10ml added in finalrecipe. MnSO4.xH2O hydration and methyleneblue salt/hydrate remain unresolved. Allseven namedsolute inputs and1Lwater are retained without inferred productidentity.')
stock([125],'dsmz_1144_hutner_basal_salts','DSMZ1144 Hutner basal salts','https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1144.pdf',[g('Nitrilotriacetic acid (NTA)','10.00'),g('MgSO4 x 7 H2O','29.70'),g('CaCl2 x 2 H2O','3.34'),mg('(NH4)MoO7O24 x 4 H2O','9.25'),mg('FeSO4 x 7 H2O','99.00'),ml('Metals 44 (DSMZ1144)','50.00'),ml('Distilled water','950.00'),g('KOH','about7.3'),comp('NaOH or H2SO4',note='Alternative pH adjustment reagents; unspecified amounts.')],'Exact DSMZ1144 Hutner preparation:pHNTA7.0withKOH,combinedpH6.8withNaOHorH2SO4. Malformedmolybdate retained. NestedMetals44 per1Lwater:Na-EDTA250mg,ZnSO4.7H2O1095mg,FeSO4.7H2O500mg,MnSO4.H2O154mg,CuSO4.5H2O39.2mg,Co(NO3)2.6H2O24.8mg,Na2B4O7.10H2O17.7mg,andfewdropsconcentratedH2SO4. Na-EDTAidentity unresolved. Doesnot merge JCM900 sourcevariant.')
# Nominal stock concentration remains on its solute component, never final medium.
nominals=[
 (74,'togomedium_m2653_sodium_formate_20_percent','TogoMedium M2653 sodium formate20% stock',togo(2653),'Sodium formate','20','PERCENT_BASIS_UNSPECIFIED','Solvent, percentagebasis and manufacturingrecipe unreported.'),
 (82,'togomedium_m2568_l_cysteine_hcl_4_percent','TogoMedium M2568 L-cysteineHCl4% stock',togo(2568),'L-Cysteine . HCl','4','PERCENT_BASIS_UNSPECIFIED','Added10ml aftersterilization; percentbasis,solvent,pHunreported.'),
 (84,'togomedium_m3118_hcl_3m','TogoMedium M3118 HCl3M reagent',togo(3118),'HCl','3','M','pHadjustmentreagent; variableaddedamount; solvent/additivesunreported.'),
 (93,'jcm_1415_sodium_bicarbonate_8_percent','JCM1415 sodiumbicarbonate8% stock',jcm(1415),'NaHCO3','8','PERCENT_BASIS_UNSPECIFIED','Asteriskmeansfiltersterilized;25mladdition; solvent/percentbasisunreported.'),
 (103,'jcm_665_sodium_acetate_2m_ph7','JCM665 sodiumacetate2M pH7 stock',jcm(665),'Sodium acetate','2','M','pH7.0; solvent,titrant and suppliedhydrate unreported.'),
 (114,'jcm_923_sodium_acetate_20mm','JCM923 sodiumacetate20mM stock',jcm(923),'Sodium acetate','20','MM','Sterileanaerobicstock;0.05ml per5mlculture; solvent,suppliedhydrate,pHunreported.'),
 (117,'nbrc_981_tris_hcl_01m_ph75','NBRC981 TrisHCl0.1M pH7.5 buffer',togo(1768),'Tris-HCl buffer','0.1','M','pH7.5; source doesnot provide detailed acidbasecomposition or solvent; notpureTrisHClsalt.'),
 (118,'jcm_825_l_cysteine_hcl_monohydrate_3_percent','JCM825 L-cysteineHClmonohydrate3% stock',jcm(825),'L-Cysteine HCl x H2O','3','PERCENT_BASIS_UNSPECIFIED','Original JCM825 and matching MediaDive4784 both specify3% monohydrate stock,10ml added; solvent,percentagebasis and stockpH unreported.'),
 (119,'togomedium_m2568_sodium_fumarate_1_percent','TogoMedium M2568 sodiumfumarate1% stock',togo(2568),'Sodium fumarate','1','PERCENT_BASIS_UNSPECIFIED','Added2ml aftersterilization; sodiumstoichiometry,percentbasis,solventunreported.'),
 (120,'togomedium_m2568_sodium_lactate_60_percent_syrup','TogoMedium M2568 sodiumlactate60% syrup',togo(2568),'Sodium lactate','60','PERCENT_BASIS_UNSPECIFIED','Commercialsyrup; stereochemistry,supplier,percentbasisunreported. Noexactlactatesoluteidentifier.'),
 (123,'jcm_923_tris_base_1m_ph8','JCM923 Trisbase1M pH8 stock',jcm(923),'Tris base','1','M','JCM923TiNTA recipe7.2ml; JCM924explicitlyreferencesit. pH8 specified; titrant/solvent unreported.'),
 (133,'jcm_1479_l_cysteine_hcl_monohydrate_5_percent_ph7','JCM1479 L-cysteineHClmonohydrate5% pH7 stock',jcm(1479),'L-Cysteine·HCl·H2O','5','PERCENT_BASIS_UNSPECIFIED','pH7.0 and1mladdition explicit; percentagebasis,solvent,pHadjustment reagent unreported.'),
 (135,'togomedium_m2809_sodium_citrate_02m','TogoMedium M2809 sodiumcitrate0.2M stock',togo(2809),'Sodium citrate','0.2','M','LS4D source nominalstock; sodiumstoichiometry,hydrate,solvent,pHunreported.')]
for i,stem,label,url,solute,value,unit,note in nominals:
 stock([i],stem,label,url,[comp(solute,value,unit)],'Nominal source-qualified stock only. '+note+' The source does not establish a complete constituent list; no omitted solvent or titrant is invented.','UNKNOWN','BUFFER_SOLUTION' if i in [103,117,123,135] else 'OTHER')
exec(compile((ROOT/'parts/b-remediation.py').read_text(),str(ROOT/'parts/b-remediation.py'),'exec'))
# Evidence added above must also bind existing-owner proposal payloads.
for p in P:
 p['evidence_ids']=list(dict.fromkeys(e for d in D if d['case_id'] in p['case_ids'] for e in d['evidence_ids']))
