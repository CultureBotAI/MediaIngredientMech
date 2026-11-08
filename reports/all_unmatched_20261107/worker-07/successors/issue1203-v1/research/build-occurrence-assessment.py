from pathlib import Path
import json,hashlib,subprocess
from datetime import datetime,timezone
R=Path('reports/all_unmatched_20261107/worker-07').resolve(); O=Path(__file__).parent
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
CID='CM_NAME:9dd78dd62f6762ad602b4126b067042b0cc68ba65bd212f9a10b07ec20b33e8e'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
case=next(c for c in json.loads((R/'parts/b-input.json').read_text())['cases'] if c['case_id']==CID)
old={x['evidence_id']:x for x in json.loads((R/'evidence.json').read_text())['evidence']}
new=json.loads((O/'new-primary-index-v2.json').read_text())
cat=[]
def reused(oldid,newid,locator,support):
 e=old[oldid]; assert sha(R/e['capture']['path'])==e['capture']['sha256']
 x={k:e[k] for k in ['kind','capture','url','accessed_at']};x.update(evidence_id=newid,locator=locator,supports_or_contradicts=support,case_ids=[CID],reused_from_evidence_id=oldid,reused_from_published_commit='be2f4c36d3d4ed79aabe29401c555ae3fd65d7b0');cat.append(x);return newid
pdfs={
 '1592':('B-PRIMARY-2710c77f8ca289','page1 firsttable, Mg(SO4)x7H2O row; Volume[ml/l]10 and Stock Solutions[g/l]7.5','DSMZ1592 supplies7.5g/L heptahydrate stock,10mL/L; finalmedium dilutionwater does not establish stocksolvent.'),
 '1593':('B-PRIMARY-98494b9ac6eef3','page1 Mineralstable, Mg(SO4)x7H2O row; Volume[ml/l]10 and Stock Solutions[g/l]7.5','DSMZ1593 supplies7.5g/L heptahydrate stock,10mL/L; frozen10G_PER_L/PERCENT_V_V are not authoritative conversions.'),
 '1593a':('c-e-dsmz-mg-1593a','page1 firsttable, Mg(SO4)x7H2O(7.5g/l stock solution)10ml; Final volume1000ml','DSMZ1593a independently defines same nominal7.5g/L stock and10mL aliquot in1000mL formulation. Solvent/preparation remain unstated for this stock.'),
 '1673':('B-PRIMARY-e262ab0ef62350','page1 firsttable, Mg(SO4)x7H2O(350g/l stock solution)10.00ml/l','DSMZ1673 defines350g/L heptahydrate stock addition10mL/L. Frozen3.5G_PER_L is solute equivalent, not a pure-solid supplied form.'),
 '1677':('B-PRIMARY-1aa7db880c7436','page1 firsttable, Mg(SO4)x7H2O(350g/l stock solution)3.30g','DSMZ1677 explicitly identifies350g/L stock but gives3.30g; freshAPI5781 instead gives3.3ml and g_l3.3. Keep dose conflict open without changing settled nominalstock identity.'),
 '1678':('B-PRIMARY-00ba5fa7f7d433','page1 firsttable, Mg(SO4)x7H2O row: Volume[ml/l]3.3, Stock Solutions[g/l]350','DSMZ1678 defines350g/L stock at3.3mL/L; freshAPI5782 says3.3g/l. Both supportstock strength, but conflicting dose units remainheld.'),
 '1845':('c-e-dsmz-mg-1845','page1 Basal salt stock solution(20x): Mg(SO4)x7H2O7.00g; primarymainmedium lists50mL of mixed20xstock','The7g entry is pureheptahydrate constituent of mixedbasal stock, not a single-solutestock. Substock volume is not stated inPDF; API6448 volume=null. Do notinfer7g/L or finalmedium7g/L.')}
for med,(eid,loc,support) in pdfs.items():
 reused(eid,'MG1203-DSMZ-'+med.upper(),loc,support)
 p=R/old[eid]['capture']['path'];(O/('dsmz-'+med+'-derived.txt')).write_text(subprocess.check_output(['pdftotext','-layout',str(p),'-'],text=True))
reused('B-PRIMARY-7a4fe57da02e52','MG1203-MEDIADIVE-6270','data.id=6270; data.recipe[compound_id=2154], recipe_order3; attribute/amount/unit; data.volume','Explicit7.5g/l stocksolution,10ml,volume1000: supports exact1593a stockinput in both frozen representations; no solvent inferred.')
reused('B-PRIMARY-f918a5c4f70e27','MG1203-MEDIADIVE-6328','data.id=6328; data.recipe[compound_id=2154], recipe_order4; amount/unit/attribute; data.volume','Unqualified heptahydrate mass0.1g in500mL recipe; supports soluteidentity and0.2g/L normalization inSolutionRecipe, contradicts0.1G_PER_L flattenedMediaRecipe as dose.')
reused('B-PRIMARY-ebb460e3dfe0df','MG1203-MEDIADIVE-1897','data.medium.id=1897; data.solutions[id=6641], volume1000; recipe[compound_id=2154], recipe_order8','Unqualified heptahydrate mass0.05g in1000mL recipe; frozen0.05G_PER_L is compatible with mass-of-solute context, no stock claim.')
reused('B-ONTOLOGY-CHEBI:31795','MG1203-CHEBI-31795','_embedded.terms[obo_id=CHEBI:31795]:label,description,formula,CAS10034-99-8,is_obsolete=false','CHEBI31795 denotes magnesium sulfate heptahydrate; supports component identity only, not stockwhole equivalence or dose.')
for e in new:
 ident=e['url'].rsplit('/',1)[1]
 support={
 '5518':'7.5g/l stockattribute,10ml,volume1000 confirms suppliedstock inDSM1592; frozenpercent-volume is not accepted.',
 '5736':'7.5g/l stockattribute,10ml,volume1000 confirms suppliedstock inDSM1593; frozenpercent-volume is not accepted.',
 '5775':'350g/l stockattribute,10ml,volume1000,g_l3.5; primarydose isstockaliquot and3.5G_PER_L expresses soluteamount, not suppliedidentity.',
 '5781':'350g/l stockattribute,3.3ml,volume1000,g_l3.3; dose conflicts withDSM1677PDF3.3g and concentrationnormalization. Strengthidentitysettled, doseheld.',
 '5782':'350g/l stockattribute,3.3g/l,volume1000,g_l3.3; dose conflicts withDSM1678PDF3.3ml/l. Strengthidentitysettled, doseheld.',
 '6448':'Unqualified Mg(SO4)x7H2O7g,attribute=null,volume=null, g_l7; purecompound constituent of mixedbasalstock. g_l7 does notsettle absent denominator.'}[ident]
 cat.append({k:e[k] for k in ['evidence_id','capture','url','accessed_at']}|{'kind':'primary_source','locator':f'data.id={ident}; data.recipe[compound_id=2154], amount/unit/attribute/g_l; data.volume','supports_or_contradicts':support,'case_ids':[CID]})
byid={e['evidence_id']:e for e in cat}
meds=['1845','1593','1673','1677','1678','1592','1593a','1818','1592','1593','1673','1677','1678','1593a','1818','1845','1897']
sol={'1592':'5518','1593':'5736','1593a':'6270','1673':'5775','1677':'5781','1678':'5782','1818':'6328','1845':'6448','1897':'6641'}
rows=[]
for i,(occ,med) in enumerate(zip(case['occurrences'],meds)):
 assert sha(Q/occ['full_recipe_snapshot'])==occ['source_file_sha256']
 stock=med in ['1592','1593','1593a','1673','1677','1678'];strength='7.5' if med in ['1592','1593','1593a'] else '350' if stock else None
 eids=[]
 if med in pdfs:eids.append('MG1203-DSMZ-'+med.upper())
 if med in ['1593a','1818']:eids.append('MG1203-MEDIADIVE-'+sol[med])
 elif med=='1897':eids.append('MG1203-MEDIADIVE-1897')
 else:eids.append('MG1203-PRIMARY-MEDIADIVE-SOLUTION-'+sol[med]+'-V2')
 eids.append('MG1203-CHEBI-31795')
 row={'occurrence_index':i,**occ,'source_recipe_capture':{'root':'source','path':occ['full_recipe_snapshot'],'sha256':occ['source_file_sha256']},'primary_medium':med,'primary_solution':sol[med], 'disposition':'stock_product_mixture_context' if stock else 'existing_identity_or_alias','material_scope':'source-qualified nominal heptahydrate stock' if stock else 'heptahydrate solute component','solute_identity':{'identifier':'CHEBI:31795','label':'magnesium sulfate heptahydrate','assessment':'supported; unchanged'},'source_identity_status':'settled_at_declared_scope','stock_concentration':{'value':strength,'unit':'G_PER_L'} if stock else None,'preferred_proposal_reuse':'C-P08' if strength=='7.5' else 'new distinct source-qualified350g/L stock after campaign-wide duplicate check' if stock else None,'evidence_ids':eids,'primary_evidence':[{'evidence_id':eid,'capture':byid[eid]['capture'],'url':byid[eid]['url'],'accessed_at':byid[eid]['accessed_at'],'locator':byid[eid]['locator']} for eid in eids], 'missing_evidence_holds':[], 'integration_requirements':[]}
 if stock:
  row['missing_evidence_holds'].append({'scope':'stock solvent and preparation','requirement':f'For the nominal{strength}g/L MgSO4·7H2O stock, obtain an explicit source statement of solvent identity/amount and preparation convention before asserting complete composition or identical fully specified preparation. The cited instructions to make up the final medium with water do not specify stock solvent.','blocks':'Complete component-list or full preparation equivalence; does not block isolated source-qualified nominalstock payload with completeness UNKNOWN.'})
  row['integration_requirements'].append('Use exact occurrence/source-qualified stock mapping; do not apply global rawlabel-to-pure-solute alias, genericingredient2154 identity, orstockcomponent identity as stockwhole identity.')
  if strength=='7.5':
   row['primary_dose']={'amount':'10','unit':'mL','recipe_final_volume':'1000mL','stock_concentration':'7.5g/L','status':'settled by direct primarysource; not calculated from frozen concentration'}
   row['reasoning']='The exact recipe primary record names a7.5g/L stock and10mL aliquot for1000mL final medium. The frozen label suppresses the stockattribute; the imported numeric concentration does not change supplied form. Both MediaRecipe and SolutionRecipe copies refer to this same stockinput. Reuse C-P08 nominalstock identity; CHEBI31795 remains its component.'
   row['frozen_annotation_assessment']='Frozen '+json.dumps(occ['raw_component']['concentration'],sort_keys=True)+' is preserved verbatim as provenance. Direct primary10mL stockaddition determines scope; no PERCENT_V_V conversion is asserted.'
  elif med=='1673':
   row['primary_dose']={'amount':'10','unit':'mL/L','stock_concentration':'350g/L','status':'settled by matching DSMZPDF/API; frozen3.5G_PER_L is a solute-equivalent representation'}
   row['reasoning']='DSMZ1673 and MediaDive5775 explicitly name350g/L stock and10mL/L addition. API g_l3.5 and frozen3.5G_PER_L express solutequantity but cannot turn the suppliedstock into pureheptahydrate. Distinct nominal350g/L stock is required; C-P08 at7.5g/L is inapplicable.'
   row['frozen_annotation_assessment']='The3.5G_PER_L value is consistent with the stock-derived solute equivalent but not evidence of direct solidinput orstock concentration.'
  else:
   row['primary_dose']={'status':'held due contradictory primarysource dose units','DSMZ_PDF':'3.30g of350g/L stock' if med=='1677' else '3.3mL/L of350g/L stock','MediaDive_API':'3.3ml, g_l3.3' if med=='1677' else '3.3g/l, g_l3.3','recipe_final_volume':'1000mL'}
   row['missing_evidence_holds'].append({'scope':'dose and final-medium concentration','requirement':f'Obtain authoritative clarification for DSMZ{med}/MediaDive{sol[med]} on the3.3 addition unit and corresponding final-medium amount; current PDF/API disagree. Do not select a unit by analogy to a related medium or treat frozen3.3G_PER_L as correction.','blocks':'Dose/final-medium conversion and sourcequantity release; does not block explicitly declared350g/L nominalstock identity.'})
   row['reasoning']=f'Both DSMZ{med} and MediaDive{sol[med]} explicitly identify350g/L heptahydratestock, while the dose fields disagree. Material/strength can be represented now as a source-qualified nominalstock with CHEBI31795 component; dose must stayheld. This is not C-P08 at7.5g/L.'
   row['frozen_annotation_assessment']='Frozen3.3G_PER_L agrees with one derivative/API number but cannot resolve contradictory primary addition units.'
 else:
  row['preferred_proposal_reuse']='Existing CHEBI31795 solute owner; no new chemical orstock owner for this occurrence'
  row['integration_requirements'].append('Resolve only this source-bound solute occurrence; do not make sharedrawlabel globally resolve all17 to pureheptahydrate.')
  if med=='1845':
   row['primary_dose']={'amount':'7','unit':'g','scope':'ingredient in Basal salt stocksolution(20x), a mixedpreparation','stock_recipe_volume':None,'status':'mass7g settled; denominator/finalmedium conversion held'}
   row['reasoning']='DSMZ1845 lists7g MgSO4·7H2O inside a mixed Basal salt stocksolution(20x), alongsideKH2PO4,KCl,NaCl. MediaDive6448 confirms an unqualified7g compoundinput and volume=null. The ingredient is theheptahydrate component, not the wholemixedstock or a7g/L single-solutestock.'
   row['missing_evidence_holds'].append({'scope':'mixedbasalstock denominator','requirement':'Obtain explicit finalvolume of the20x basal saltstock; DSMZ1845 does notstate it and MediaDive6448 volume=null. Do not infer1L from g_l7,20x,50mL use, or the frozen7G_PER_L.','blocks':'7g/L stock orfinal-medium dose assertion, not CHEBI31795 component identity.'})
   row['frozen_annotation_assessment']='Frozen7G_PER_L is not validated: source provides7g with no basalstockvolume. The finalmedium uses50mL of a multicomponent20x stock.'
   if i==0:
    row['integration_requirements'].append('CultureMech001268 flattened the basalstock constituent into root ingredients/2. Restore source hierarchy/retain nested component qualification before asserting it is a direct main-medium ingredient; no new evidence is needed to establish that hierarchy.')
  elif med=='1818':
   row['primary_dose']={'amount':'0.1','unit':'g','recipe_final_volume':'500mL','status':'mass/volume explicitly primary;0.2g/L normalization is derived and arithmetic-only'}
   row['reasoning']='MediaDive6328 explicitly lists0.1g unqualified MgSO4·7H2O in a500mL recipe, with no stockattribute. This is a soluteingredient, so CHEBI31795 applies. An explicitbatch amount supports identity independently of the imported concentration difference.'
   row['frozen_annotation_assessment']='Frozen0.1G_PER_L inMediaRecipe conflicts with primary0.1g per500mL; sourcequantity correction is settled, not a missing-evidence hold.' if i==7 else 'Frozen0.2G_PER_L agrees arithmetically with primary0.1g per500mL; no stock identity is present.'
   if i==7:row['integration_requirements'].append('Correct the flattened MediaRecipe quantity in its owning source workflow using0.1g/500mL; preserve frozenbytes and do notedit CultureMech here.')
  else:
   row['primary_dose']={'amount':'0.05','unit':'g','recipe_final_volume':'1000mL','status':'settled by direct primarymass/volume'}
   row['reasoning']='MediaDive1897/solution6641 lists0.05g unqualified MgSO4·7H2O in1000mL. No stockattribute orvolumeofstock is asserted. Frozen0.05G_PER_L agrees and CHEBI31795 applies as pureheptahydrate ingredient.'
   row['frozen_annotation_assessment']='Frozen0.05G_PER_L matches primary0.05g/1000mL; no dose conflict identified.'
 rows.append(row)
assert len(rows)==17 and len({r['occurrence_id'] for r in rows})==17
for e in cat:assert sha(R/e['capture']['path'])==e['capture']['sha256']
assessment={'schema_version':1,'author_agent':'/root/mg_occurrence_author','authored_at':datetime.now(timezone.utc).isoformat(),'independent_review_status':'pending different-author review','case_id':CID,'case_input_sha256':hashlib.sha256(json.dumps(case,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest(),'source_container':{'path':'parts/b-input.json','sha256':sha(R/'parts/b-input.json')},'immutable_predecessor_commit':'be2f4c36d3d4ed79aabe29401c555ae3fd65d7b0','issue_url':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1203','coverage':{'frozen_occurrences':17,'nominal_7_5_g_l_stock_occurrences':6,'nominal_350_g_l_stock_occurrences':6,'solute_component_occurrences':5},'scope_boundary':'Research/authoring of exact17 occurrenceoutcomes only. This is not independentreview, wholeownerapproval, othercaseapproval, maintainedsource edit, orrelease support.','existing_proposal_comparison':{'C-P08':{'capture':{'root':'artifact','path':'proposed_owners/c-C-P08.yaml','sha256':sha(R/'proposed_owners/c-C-P08.yaml')},'assessment':'Same nominal7.5g/L solute/stockcontext inDSMZ1592,1593,1593a; reuse source-qualified identity withUNKNOWNsolvent/preparation, no duplicate. Does not apply350g/L, unqualifiedsolute, ormixed20x basalstock contexts.'},'350g_l_search_scope':'gitignore-inclusive rg search of currentworktree data/ingredients and publishedworker07 proposed_owners found onlyC-P08 matching Mg sulfate stock; campaignwide check is root integration responsibility before minting.'},'retrieval_caveat':'Initial fetch-primary.py wrote sixAPI bodies before a localpath receiptformatter failed. Those firstbodies are not used in evidencecatalog. Separately namedv2 captures have full HTTP200 metadata and owntruthful timestamps. DSMZ1818/1897PDF URLs returned404; existing exact MediaDiveAPI payloads provide applicable primaryevidence.','occurrences':rows}
for fn,obj in [('occurrence-assessment.json',assessment),('occurrence-evidence.json',{'schema_version':1,'evidence':cat})]:
 p=O/fn; assert not p.exists(),str(p);p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(assessment['coverage']));print('assessment_sha256',sha(O/'occurrence-assessment.json'));print('evidence_sha256',sha(O/'occurrence-evidence.json'))
