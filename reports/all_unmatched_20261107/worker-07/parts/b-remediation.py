"""Manual remediation of A's independent primary-source findings.
Executed after the preserved original supplement. Before versions are retained
in b-pre-remediation; no maintained owner or source recipe is edited.
"""
import html

# Every retrieved response is classified by its actual content, not HTTP alone.
remed=[]
for fn in ['b-remediation-retrievals.json','b-remediation2-retrievals.json','b-remediation3-retrievals.json','b-remediation4-retrievals.json','b-remediation5-retrievals.json','b-remediation6-retrievals.json']:
 for n,r in enumerate(json.loads((ROOT/'parts'/fn).read_text())):
  r=copy.deepcopy(r);r['manifest']='parts/'+fn;r['manifest_index']=n
  i=r['case_index'];fam=r['family'];path=r.get('path');body=(ROOT/path).read_text(errors='replace') if path and not path.endswith('.pdf') else ''
  kind='unsuccessful_search';support='The exact primary URL was pursued, but the response supplies no usable formulation or product identity.'
  if fam.startswith('PMID'):
   kind='source_snapshot';support='Europe PMC bibliographic metadata identifies the exact cited primary paper and DOI. Its abstract and access links do not specify the reagent sodium count or hydrate.'
  elif fam.startswith('OLS') and r['http_status']=='200':
   kind='ontology';support='Exact preserved ontology search results. Zero results or unrelated results are bounded search outcomes, not proof that no term exists anywhere; parent candidates require explicit chemical-scope comparison.'
  elif fam=='CHEBI190300':
   kind='ontology';support='Exact non-obsolete CHEBI190300 term record labels inorganic phosphate salt and defines a phosphate salt lacking C-H bonds. This is an asymmetric class anchor for the source-confirmed CAS tetrahydrate, not its exact identity.'
  elif fam=='DOI10.1186/1475-2859-10-25':
   kind='primary_source';support='Follonier2011 Methods distinguishes modified E2 flask medium (references Durner2001) from the fully listed bioreactor medium. Literal bioreactor NaNH4PO4·4H2O lacks hydrogenphosphate H and cannot establish the three frozen E2 flask occurrences. Its EDTANa·2H2O belongs to this paper, not the seven B90 sources.'
  elif fam=='SchaechterPDF':
   kind='primary_source';support='Schaechter1958 original Table1 p594 footnote(c) explicitly specifies Na(NH4)HPO4·4H2O1.74g/L in salt solution, made as50x concentrate. Rows14–22 all invoke that solution: applies to nine Schaechter occurrences only. Exact printed formula visually checked in b-schaechter-table1.png; frozen quantities are not recalculated.'
  elif fam in ['M2256','M3175','M3057','M3221','M2577','JCM825','MediaDive4784','NBRC1620','TOGOM708']:
   kind='primary_source'
   support={
    'M2256':'Exact TogoM2256 Columbia-broth subrecipe specifies Magnesium Sulfate (anhydrous)0.1g; no original src_url is supplied.',
    'M3175':'Exact TogoM3175 modifiedGS2 recipe specifies sodium citrate tribasic dihydrate3g; no original src_url is supplied.',
    'M3057':'Exact TogoM3057 main solution specifies CH3COONa200mg and links original NBRC1620. Formula supports sodium acetate with no printed water of crystallization.',
    'M3221':'Exact TogoM3221 specifies CH3COONa0.0683g/L in main medium; src_url is empty. This is not an EDTA source-form resolution.',
    'M2577':'Exact TogoM2577 modifiedNOS table specifies L-Cysteine x HCl0.1g; no monohydrate is printed. Retain the source form.',
    'JCM825':'Original JCM825 KOKO medium specifies3% L-cysteine·HCl·H2O solution10ml among separately added sterile anaerobic stocks. Percentage basis and stock solvent/pH are unspecified.',
    'MediaDive4784':'Exact MediaDive4784 Main sol.J825 row15 corroborates compound L-Cysteine HCl x H2O, attribute3%, amount10ml; recipe steps identify separately added anaerobic stocks.',
    'NBRC1620':'Original NBRC1620 Azospira medium confirms CH3COONa200mg; no hydrate is printed.',
    'TOGOM708':'Exact TogoM708 JCM688-derived record specifies5% L--Cysteine·HCl·H2O5ml and explicitly instructs use Medium687 replacing methanol solution with sodium formate solution. The cysteine stock is therefore inherited from687; current JCM688 Nothing-found response is not support.'}[fam]
  elif fam in ['DOI10.1007/s00253-004-1743-y','DOI10.1007/s00253-003-1499-9','ParkPDF','Zhu2004PDF'] and r['http_status']=='200':
   support='Publisher returned article abstract/reference/paywall HTML, including for the requested PDF URL; no full Methods reagent table was supplied. The accessible bibliographic record does not resolve the sodium EDTA form.'
  elif 'linkinghub.elsevier.com' in str(r.get('final_url')):
   support='DOI resolves to an Elsevier linking/cookie landing page, not the full article Methods. It supplies no exact reagent formula; publication access failure is retained.'
  elif fam in ['SigmaV6629','UTEXDAS']:
   support='Direct curl retrieval failed or was rate limited. The successful independent web-tool primary captures are separately referenced; this failed response supplies no identity evidence.'
  elif fam=='TOGOM685':
   support='Retrieved TogoM685 is not the exact JCM665 source context and is not used to support that stock; retained only as an unsuccessful source-location attempt.'
  eid='B-REMED-'+hashlib.sha256((fn+str(n)+r['url']).encode()).hexdigest()[:14]
  ev(eid,kind,path or 'parts/'+fn,'Complete response for '+fam if path else f'entry[{n}] retrieval failure',support,r['url'],r['accessed_at'],[decision(i)['case_id']]);attach([i],eid)
  r.update(evidence_id=eid,evidence_kind=kind,assessment=support);remed.append(r)

for url,loc,support in [
 ('https://utex.org/products/das-vitamin-cocktail','Original UTEX DAS table row4 and preparation instructions','Exact source specifies VitaminB12 SigmaV6629; binds the product catalog to this one frozen occurrence.'),
 ('https://www.sigmaaldrich.com/US/en/product/sigma/v6629','Supplier V6629 product title, CAS and structure','Supplier identifies source-specified V6629 as cyanocobalamin CAS68-19-9. This supports the UTEX occurrence, not a global synonym for all cobalamin vitamers.')]:
 extra([91],'captures/b-remediation-web1.json',url,loc,support)
for url in ['https://www.sigmaaldrich.com/US/en/product/sigald/04266','https://www.thermofisher.com/order/catalog/product/040320.22']:
 extra([116],'captures/b-remediation-web3.json',url,'Official product identity: CAS7783-13-3; NaNH4HPO4·4H2O; molecular formulaH13NNaO8P','Confirms registry identity of the exact formula printed by Schaechter. Does not claim either modern supplier product was used in1958 or establish any of the eight other paper-family occurrences.')
extra([90],'captures/b-remediation-web3.json',None,'Exact-title fulltext searches and PMID searches','Searches did not yield a verified original fulltext reagent table for the five B90 families; snippets and unrelated records are not form evidence.',kind='unsuccessful_search')

# Each literature family is pursued and accounted separately for every occurrence.
family_specs={
 90:[('Park2005',[0],['15459799'],['PMID15459799','DOI10.1007/s00253-004-1743-y','ParkPDF'],'Publisher abstract/paywall HTML obtained; PDF URL also returned HTML. No methods/reagent specification recovered.','Exact Park source reagent formula or catalog is still needed for sodium count and hydrate.'),
     ('Zhu2004_2005',[1],['14673546','15781419'],['PMID14673546','PMID15781419','DOI10.1007/s00253-003-1499-9','DOI10.1016/j.ymben.2004.10.004','Zhu2004PDF','Zhu2005PDF'],'2004 publisher abstract/paywall HTML and2005 Elsevier landing page recovered; explicit PDF attempts unavailable.','Original Zhu reagent specification of sodium EDTA is still needed; neither accessible abstract distinguishes sodium count or hydrate.'),
     ('Fischer2003',[2],['12603321'],['PMID12603321','DOI10.1046/j.1432-1033.2003.03448.x','FischerPDF'],'Exact PMID/DOI confirmed; Wiley article andPDF requests return403/challenge.','Fischer M9 trace reagent formula or catalog remains unavailable; no transfer of form from other M9 protocols.'),
     ('Mogensen2006',[3,4],['16698295'],['PMID16698295','Mogensen2006'],'Exact citation metadata recovered; DOI returns Elsevier linking/cookie page without methods.','The original minimal-medium trace solution or product catalog must establish EDTA sodium count and hydration; ethanol/glucose variants remain paired only by this cited source.'),
     ('Shcolnick2006',[5,6],['17234153'],['PMID17234153','Shcolnick2006'],'Exact citation metadata recovered; DOI returns Elsevier linking/cookie page without methods.','The exact YBG11/YBG11-0FeCl3 reagent definition remains unavailable; conventional BG11 EDTA form is not evidence for these source variants.')],
 116:[('Schaechter1958',[0,1,7,9,10,11,12,13,15],['13611202'],['PMID13611202','DOI10.1099/00221287-19-3-592','SchaechterPDF'],'Full original PDF and visual Table1 confirm Na(NH4)HPO4·4H2O1.74g/L in shared salt solution(c); rows14–22 explicitly use it.','Source identity resolved to sodium ammonium hydrogen phosphate tetrahydrate for these nine only. Frozen millimolar values and50x preparation note are preserved.'),
      ('Follonier2011_Durner2001',[2,3,4],['21513516','11135197'],['PMID21513516','PMID11135197','DOI10.1186/1475-2859-10-25','Durner2001','PMC3107774'],'Follonier full Methods recovered. Flask medium is modified E2 referring toDurner; separate bioreactor recipe prints NaNH4PO4·4H2O. Durner original DOI request returned403.','Exact Durner/E2 flask supplied salt is still unconfirmed; separate bioreactor formula has omitted acidH and cannot resolve these three frozen flasks.'),
      ('Hassan1977',[5,6,8,14],['233720'],['PMID233720','DOI10.1128/jb.130.2.805-811.1977','PMC235284','HassanEPMCpdf','HassanPMCpdf','HassanASMPDF'],'Exact citation recovered; ASM article/PDF andEuropePMC returned403/500; PMC PDF request returned browser challengeHTML, notPDF.','Hassan original medium reagent formula/catalog is still unavailable. No assumption that its16.7394mM salt matches Schaechter tetrahydrate.'),
      ('Tseng1994',[16],['7961411'],['PMID7961411','DOI10.1128/jb.176.21.6599-6605.1994','PMC197015','TsengEPMCpdf','TsengPMCpdf','TsengASMPDF'],'Exact citation recovered; ASM article/PDF andEuropePMC returned403/500; PMC PDF request returned challengeHTML.','Exact Vogel-Bonner implementation cited by Tseng remains unverified for hydrogenphosphate stoichiometry and hydrate; recipe-name familiarity is insufficient.')]
}
ledger=[]
for i,specs in family_specs.items():
 covered=[]
 for name,positions,pmids,fams,finding,remaining in specs:
  attempts=[r for r in remed if r['family'] in fams];assert all(any(r['family']==f for r in attempts)for f in fams)
  oids=[CASES[i-70]['occurrences'][p]['occurrence_id']for p in positions];covered+=oids
  ledger.append({'case_index':i,'case_id':decision(i)['case_id'],'family':name,'occurrence_ids':oids,'source_files':[CASES[i-70]['occurrences'][p]['full_recipe_snapshot']for p in positions],'cited_pmids':pmids,'attempts':attempts,'finding':finding,'remaining_requirement':remaining})
 assert sorted(covered)==sorted(decision(i)['occurrence_ids'])
(ROOT/'parts/b-family-review.json').write_text(json.dumps({'reviewed_at':NOW,'families':ledger},ensure_ascii=False,indent=2)+'\n')
for i in [90,116]:
 extra([i],'parts/b-family-review.json',None,'All source-family occurrence IDs and individual original-publication retrievals','Records exact family-specific pursuit, obtained content, limitations and remaining identity requirement for every occurrence.',at=NOW,kind='source_snapshot')
 decision(i)['source_family_assessments']=[{k:v for k,v in f.items()if k!='attempts'}for f in ledger if f['case_index']==i]
decision(90)['reasoning']='The seven SodiumEDTA occurrences form five independently checked paper families: Park2005(1), Zhu2004/2005(1), Fischer2003(1), Mogensen2006(2), and Shcolnick2006(2). Every exact cited PMID and DOI was pursued and is bound in b-family-review.json. Publisher abstracts/paywalls, Elsevier landing pages and Wiley challenges did not expose the original reagent formulas or catalogs. Thus sodium stoichiometry and hydrate remain unknown separately for each family; Follonier2011 EDTANa·2H2O is from another case and is not transferable.'
decision(90)['missing_requirement']='Obtain each of the five exact papers\' sodiumEDTA reagent formula/catalog or detailed medium trace-stock specification. Family-specific retrieval paths and unavailable content are recorded; no general EDTA synonym or cross-paper hydrate assumption resolves these seven occurrences.'
decision(90)['no_change_reason']=decision(90)['missing_requirement']

# Exact source-scoped nominal preparations are representable despite unknown solvent.
def scoped_stock(i,positions,stem,label,url,solute,value,unit,preparation):
 oids=[CASES[i-70]['occurrences'][p]['occurrence_id']for p in positions]
 pid=stock([i],stem,label,url,[comp(solute,value,unit)],preparation+' The component list is UNKNOWN: the source does not specify stock solvent, manufacturing details or additional stock constituents. Preserve concentration on the stock solute; do not reinterpret the dose as final-medium concentration. Applies only to occurrence IDs '+', '.join(oids)+'. No cross-source equality or global raw-label alias is asserted.','UNKNOWN','OTHER')
 p=next(p for p in P if p['proposal_id']==pid);p['occurrence_ids']=oids
 return pid
for n,positions in [('110',[0,1,2,3,6,7,8]),('78',[4,9,10,11,12]),('110a',[5])]:
 scoped_stock(95,positions,'dsmz_'+n+'_sodium_hydroxide_1n','DSMZ'+n+' sodium hydroxide1N stock','https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium'+n+'.pdf','NaOH','1','N','Original DSMZ'+n+' specifies25ml of1N NaOH in meat extraction. Water in the meat extraction is a separate recipe input, not proof of stock solvent composition.')
for n,positions,dose,prep in [
 (1362,[0],'10ml','Autoclaved and stored under N2; added aseptically/anaerobically after standing the medium overnight.'),
 (1415,[1],'5ml','Autoclaved and stored under N2; final separate stock addition.'),
 (1422,[2],'4ml','Autoclaved and stored under N2; added prior to inoculation. Current primary dose4ml/L differs from frozenJCM1422 dose10.0ml/L; preserve both source versions without changing frozen quantities.'),
 (1462,[3,4],'10ml','JCM1463 explicitly uses1462 with only NaCl changed9to21g/L, so the same referenced stock is inherited; other stock composition is not inferred.'),
 (1351,[5],'5ml','Separately added stock; final medium pH readjustment does not establish stock pH.'),
 (1388,[6],'5ml','Autoclaved and stored under N2; final separate stock addition.'),
 (1389,[7],'5ml','Autoclaved and stored under N2; culture-supernatant context remains separate from the stock.'),
 (1412,[8],'10ml','Autoclaved and stored under N2; separately added with glucose and sulfide stocks.'),
 (1430,[9],'8ml','Stock addition to semi-solid heterotrophic medium; final-medium pH7 adjustment is not stock pH.'),
 (1431,[10],'8ml','Stock addition to semi-solid autotrophic medium; final-medium pH7 adjustment is not stock pH.'),
 (1435,[11],'5ml','Autoclaved and stored under N2; added prior to use.'),
 (1474,[12],'10ml','Listed as separate5% solution in BL broth with2%NaCl; liver extract and final-medium pH7.2 are separate context.'),
 (1188,[13],'6ml','Separately added sterile anaerobic stock; unstarred cysteine entry is not the filter-sterilized pyruvate/bicarbonate entries.')]:
 scoped_stock(121,positions,'jcm_'+str(n)+'_l_cysteine_hcl_monohydrate_5_percent','JCM'+str(n)+' L-cysteine hydrochloride monohydrate5% stock',jcm(n),'L-Cysteine·HCl·H2O','5','PERCENT_BASIS_UNSPECIFIED','Original JCM'+str(n)+' specifies'+dose+' of5% monohydrate stock. '+prep+' Percentage basis remains unspecified.')
for n,positions,dose,prep in [
 (794,[0],'10ml per liter','Autoclaved anaerobic stock under N2.'),
 (687,[1,2],'5ml per liter','TogoM708 explicitly inherits medium687 replacing only methanol with formate, supporting its cysteine stock inheritance; current JCM688 returns Nothingfound and is not evidentiary support.'),
 (705,[3],'5ml per liter','Autoclaved sterile stock added prior to use.'),
 (706,[4],'0.05ml per4.7ml medium','Concentration5% belongs to added stock; the original denominator is4.7ml before stock additions, not10ml or finalvolume.'),
 (822,[5],'10ml per liter','Separately added stock; adjacent sodium sulfide and phosphate buffer are distinct preparations.'),
 (723,[6],'5ml per liter','Autoclaved and stored under N2; aseptically and anaerobically added prior to inoculation.')]:
 scoped_stock(134,positions,'jcm_'+str(n)+'_l_cysteine_hcl_monohydrate_5_percent','JCM'+str(n)+' L-cysteine hydrochloride monohydrate5% stock',jcm(n),'L-Cysteine·HCl·H2O','5','PERCENT_BASIS_UNSPECIFIED','Original JCM'+str(n)+' specifies'+dose+' of5% monohydrate stock. '+prep+' Frozen double-hyphen typography is preserved in source evidence; percentage basis is unspecified.')
for i in [95,121,134]:
 decision(i)['reasoning']+=' Concrete source-qualified nominal stock proposals preserve each distinct primary recipe family. '+({95:'DSMZ110,78 and110a stocks remain separately scoped.',121:'JCM1463 explicitly inherits1462; currentJCM1422 dose4ml/L differs from frozen10.0ml/L, with both retained.',134:'M708 explicitly inherits687 replacing methanol only; JCM706 dose0.05ml refers to4.7ml medium before stock additions.'}[i])+' UNKNOWN component-list completeness retains unreported solvent and preparation basis without deferring the whole stock.'
 decision(i)['missing_requirement']='Stock solvent, additional constituents, and percentage basis where applicable remain unspecified. Exact source-bound proposals are concrete; combining independent source-family stocks would require additional proof of preparation equivalence.'

# New chemical identity has a real form-specific CAS; raw generic source label is not an alias.
schaechter_positions=[0,1,7,9,10,11,12,13,15]
schaechter_oids=[CASES[116-70]['occurrences'][p]['occurrence_id']for p in schaechter_positions]
stem='Sodium_Ammonium_Hydrogen_Phosphate_Tetrahydrate'
assert not (REPO/'data/ingredients/mapped'/f'{stem}.yaml').exists()
after={'identifier':'cas:7783-13-3','preferred_term':'Sodium ammonium hydrogen phosphate tetrahydrate','mapping_status':'MAPPED','ingredient_type':'SINGLE_INGREDIENT','ontology_mapping':{'ontology_id':'CHEBI:190300','ontology_label':'inorganic phosphate salt','ontology_source':'CHEBI','mapping_quality':'NARROW_MATCH','evidence':[{'evidence_type':'MANUAL_CURATION','source':'https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:190300','notes':'Closest verified returned phosphate-salt class lacking C-H bonds. Form-specific CAS remains primary; no exact identity to the generic parent is claimed. Exact-name searches found no suitable exact term; CAS text search failed500 and is not absence proof.'}]},'chemical_properties':{'cas_rn':'7783-13-3','molecular_formula':'H13NNaO8P','data_source':'https://www.sigmaaldrich.com/US/en/product/sigald/04266','retrieval_date':json.loads((ROOT/'captures/b-remediation-web3.json').read_text())['accessed_at']},'synonyms':[{'synonym_text':'NaNH4HPO4·4H2O','synonym_type':'EXACT','source':'https://www.sigmaaldrich.com/US/en/product/sigald/04266'},{'synonym_text':'Na(NH4)HPO4·4H2O','synonym_type':'RAW_TEXT','source':'https://doi.org/10.1099/00221287-19-3-592'}],'notes':'Schaechter1958 Table1 p594 footnote(c) establishes this tetrahydrate in the nine source occurrences bound by proposal occurrence_ids.1.74g/L and50x concentrate are source preparation context; frozen millimolar values are not edited. Generic Sodium ammonium phosphate is deliberately not a resolving synonym: E2,Hassan andTseng source forms remain unresolved. No modern supplier procurement is attributed to the historical paper.'}
history(after,'CREATED_FROM_SOURCE_FORM_EVIDENCE','Propose CAS7783-13-3 for exact Na(NH4)HPO4·4H2O source formula; broadMatch to verified inorganic phosphate salt parent; nine source occurrences only. No maintained record changed.')
after['curation_history'][-1].pop('previous_status',None)
proposal([116],stem,after,'New distinct sodium ammonium hydrogen phosphate tetrahydrate identity for nine Schaechter1958 occurrences only.',kind='new_owner',notes='Other eight occurrences retain separate form uncertainty. No global generic-label alias; source raw labels retained in frozen cases and decision. Native exact-parent availability and full owner release review remain coordinator gates.')
P[-1]['occurrence_ids']=schaechter_oids
P[-1]['identity_predicate_consequences']='Own primary cas:7783-13-3 exact identity; skos:broadMatch to CHEBI:190300 inorganic phosphate salt; mandatory same-subject kgmicrobe registry identity row upon native integration. Never exactMatch the generic salt class.'
decision(116)['disposition']='new_distinct_ingredient_proposal'
decision(116)['reasoning']='The17 occurrences were split by their actual cited papers and each original was pursued. Schaechter1958 Table1 p594 explicitly gives Na(NH4)HPO4·4H2O1.74g/L in salt solution(c), used by all nine frozen Schaechter rows; these resolve to CAS7783-13-3, independently confirmed by official supplier formula evidence. Follonier2011 distinguishes E2 flask medium from its separate bioreactor recipe; the latter\'s literal NaNH4PO4·4H2O omits the acidH and cannot settle the three E2 flask records. Durner fulltext returned403. Four Hassan and oneTseng occurrence remain unconfirmed after exact publisher/PMC fulltext attempts. The family ledger binds all17 individually; no class-wide microcosmic-salt assumption is made.'
decision(116)['missing_requirement']='Nine Schaechter occurrence identities resolved; native exact-parent/collision checks apply to the proposed new CAS owner. Eight remaining occurrences need exact source reagent evidence: three E2flasks require Durner/E2 specification; four Hassan and oneTseng require original medium formula/catalog. Failed content retrieval is recorded per family.'

# No stale applicability prose may contradict the corrected reasoning.
for d in D:
 d['applicability']='Applies only to the exact frozen raw label, occurrence IDs and full captured source contexts enumerated in this decision. Source-scoped subset refinements and proposal occurrence_ids take precedence over generic labels. '+d['reasoning']

