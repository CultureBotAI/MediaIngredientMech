"""Isolated issue-1227 author payloads; never writes maintained data."""
from pathlib import Path
import copy, datetime, hashlib, json, re, subprocess, sys
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event

R = Path('reports/all_unmatched_20261107/worker-08')
M = R / 'successors/issue-1227-v1/research/vitamins_mixtures'
A = json.loads((M / 'assignment.json').read_text())
E = {e['evidence_id']: e for e in json.loads((R / 'successors/issue-1201-v1/evidence.json').read_text())['evidence']}
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
BASE = 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(name, obj):
    (M / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
def capture(p): return {'root':'artifact', 'path':str(p.relative_to(R)), 'sha256':sha(p)}

# Explicit, individually adjudicated source labels. No fuzzy result is applied.
GROUPS = [
('CHEBI:30753',['p-Aminobenzoic acid']),
('CHEBI:15377',['Distilled water','Water']),
('CHEBI:15956',['Biotin']),('CHEBI:15940',['Nicotinic acid']),
('CHEBI:17154',['Nicotinamide']),('CHEBI:27470',['Folic acid']),
('CHEBI:17015',['Riboflavin']),('CHEBI:17268',['myo-Inositol','i-Inositol']),
('CHEBI:49105',['Thiamine HCl','Thiamine hydrochloride','Thiamine-HCl','Thiamine·HCl']),
('CHEBI:132751',['Thiamine·HCl·2H2O']),
('CHEBI:30961',['Pyridoxine hydrochloride','Pyridoxine-HCl','Pyridoxine·HCl']),
('CHEBI:131529',['Pyridoxal hydrochloride']),('CHEBI:131532',['Pyridoxamine·2HCl']),
('CHEBI:29073',['L-Ascorbic acid']),('CHEBI:15846',['β-NAD']),
('CHEBI:9532',['Thiamine pyrophosphate']),('CHEBI:17905',['Coenzyme M']),
('CHEBI:16494',['Lipoic acid','(DL)-alpha-Lipoic acid']),
('CHEBI:133341',['Choline chloride']),
('CHEBI:31345',['D-Calcium pantothenate','Calcium D-(+)-pantothenate']),
('CHEBI:17439',['Cyanocobalamin']),
('CHEBI:32588',['KCl']),('CHEBI:31206',['NH4Cl']),('CHEBI:63036',['KH2PO4']),
('CHEBI:131527',['K2HPO4']),('CHEBI:26710',['NaCl','Sodium chloride']),
('CHEBI:32030',['KBr']),('CHEBI:28741',['NaF']),('CHEBI:32149',['Na2SO4']),
('CHEBI:33118',['H3BO3']),('CHEBI:32139',['NaHCO3']),
('CHEBI:32035',['KOH','KOH (neutralizing nitrilotriacetic acid)']),
('CHEBI:44557',['Nitrilotriacetic acid']),
('CHEBI:31795',['MgSO4·7H2O','MgSO4.7H2O']),
('CHEBI:86345',['MgCl2 . 6H2O']),
('CHEBI:86158',['CaCl2·2H2O','CaCl2.2H2O','CaCl2 . 2H2O']),
('CHEBI:86244',['(NH4)6Mo7O24·4H2O']),
('CHEBI:75836',['FeSO4·7H2O','FeSO4.7H2O']),
('CHEBI:86249',['FeCl2·4H2O']),('CHEBI:53503',['CoCl2·6H2O']),
('CHEBI:53542',['NiCl2·6H2O']),('CHEBI:86368',['MnCl2·4H2O']),
('CHEBI:86356',['MnSO4.2H2O']),('CHEBI:86318',['CuCl2·2H2O']),
('CHEBI:31440',['CuSO4.5H2O','CuSO4·5H2O']),('CHEBI:36385',['SrCl2 . 6H2O']),
('CHEBI:75213',['Na2MoO4·2H2O','Na2MoO4.2H2O']),('CHEBI:49976',['ZnCl2']),
('CHEBI:15366',['Acetic acid']),('CHEBI:30768',['Propionic acid']),
('CHEBI:30772',['Butyric acid']),('CHEBI:17418',['n-Valeric acid']),
('CHEBI:16135',['iso-Butyric acid']),('CHEBI:28484',['iso-Valeric acid']),
('CHEBI:37070',['DL-2-Methylbutyric acid']),('CHEBI:75228',['Sodium Lactate']),
('FOODON:03315426',['Yeast Extract']),('CHEBI:39010',['MES']),('CHEBI:2511',['Agarose']),
('CHEBI:16183',['Methane']),('ENVO:00002005',['Air']),
# Additional manufacturer-explicit L0230 inputs; no inferred water.
('CHEBI:78292',['FeNaEDTA']),('CHEBI:8346',['KI']),('CHEBI:86364',['MnSO4·H2O']),
('CHEBI:32312',['ZnSO4·7H2O']),('CHEBI:3312',['CaCl2']),('CHEBI:63043',['KNO3']),
('CHEBI:32599',['MgSO4']),('CHEBI:63038',['NH4NO3'])]
MAP = {label: curie for curie, labels in GROUPS for label in labels}
MAP['JCM 197 trace vitamins']='kgmicrobe.ingredient:nbrc903_vitamin_solution'
MAP['DI Water']='kgmicrobe.ingredient:deionized_water'
NORMALIZED_COMPONENT_NAMES={'CoCl2·6H2O':'cobalt chloride hexahydrate','NiCl2·6H2O':'nickel chloride hexahydrate','FeNaEDTA':'Sodium ferric EDTA','(NH4)6Mo7O24·4H2O':'hexaammonium heptamolybdate tetrahydrate','KOH (neutralizing nitrilotriacetic acid)':'KOH','DI Water':'Deionized water'}
HOLDS = {
'Vitamin B12':'Generic B12 does not select a vitamer. CHEBI:176843 is a class; CHEBI:17439 selects cyanocobalamin. Preserve source and owner holds.',
'VitaminB12':'Generic B12 does not select a vitamer. CHEBI:176843 is a class; CHEBI:17439 selects cyanocobalamin. Preserve source and owner holds.',
'Calcium pantothenate':'Source does not select D versus DL stereochemistry. The active CHEBI:31345 structure is D-specific.',
'Ca-pantothenate':'Source does not select D versus DL stereochemistry. The active CHEBI:31345 structure is D-specific.',
'DL-Calcium pantothenate':'Source explicitly says DL; the active CHEBI:31345 structure is D-specific. No D-only substitution.',
'CoSO4':'TOGO gives CoSO4 without a hydrate specification. No heptahydrate or specific supplied anhydrous form is inferred from this compressed source row.',
'DI Water':'Source explicitly requires deionized water. No active exact deionized preparation owner was found in the ignored-inclusive individual catalog search; do not substitute a distilled-grade preparation.',
'Vitamin K1':'Source says K1 without stereoisomer/product specification. The active CHEBI:18067 structure selects natural phylloquinone stereochemistry. Retain this source-form limit without blocking the stock identity.',
'Ethanol (95 %)':'Immediate input is 95% ethanol, not neat ethanol; percentage basis and complete prepared-carrier identity are not supplied.',
"Metals ''44'' (see below)":'JCM149 enumerates a nested Metals44 preparation; the MICRO:0000456 owner has no formula bridge, and nested MnSO4·xH2O remains unresolved. Preserve the nested component.',
'Sodium phosphate buffer (10 mM, pH 7.1)':'The active generic sodium-phosphate-buffer owner combines several strengths/pH values. No exact complete 10 mM pH 7.1 stock formulation bridge is established.',
'Sodium phosphate buffer (10 mM; pH 7.1)':'The active generic sodium-phosphate-buffer owner combines several strengths/pH values. No exact complete 10 mM pH 7.1 stock formulation bridge is established.',
'10 mM Potassium phosphate buffer (pH 7.2)':'The active generic potassium-phosphate-buffer owner does not establish this exact 10 mM pH 7.2 preparation; salt ratio/carrier protocol remain unspecified.',
'NH4Cl (14% w/v solution)':'The immediate input is a 14% w/v stock, not neat ammonium chloride. No exact active stock owner/formulation bridge was established.',
'KH2PO4 (7% w/v solution)':'The immediate input is a 7% w/v stock, not neat potassium dihydrogen phosphate. No exact active stock owner/formulation bridge was established.',
'Na2WO4 (10 mM solution)':'Immediate input is a 10 mM solution with unspecified hydrate/carrier, not neat sodium tungstate.',
'FeCl3 (25 mM solution)':'Immediate input is a 25 mM solution with unspecified hydrate/carrier, not neat ferric chloride.',
'JCM 628 modified Wolfe mineral solution':'Source recipe is known, but no exact active catalog owner for this nested four-salt carrier was established. Do not flatten it or borrow a different Wolfe formulation.',
'JCM 629 artificial saltwater':'Source recipe is known, but no exact active catalog owner for this nested eight-salt carrier was established. Do not use generic seawater as exact identity.',
'JCM 197 trace minerals':'Source recipe is known; an exact active catalog preparation with its NTA/metal recipe and KOH adjustment was not established.',
'JCM 197 trace vitamins':'The source formula matches the selected NBRC903 candidate, but that proposal is not an admitted maintained catalog owner. Preserve the explicit coordinator dependency and no automatic integration.'}

CAT = {}
for f in Path('data/ingredients').rglob('*.yaml'):
    d = yaml.safe_load(f.read_text())
    if isinstance(d,dict) and d.get('mapping_status') == 'MAPPED': CAT.setdefault(d['identifier'],[]).append((f,d))
dependency_proposal=next(p for p in A['proposals'] if p['proposal_id']=='vm1201-prop-nbrc903-vitamin')
dependency_path=R/dependency_proposal['after_capture']['path']
CAT['kgmicrobe.ingredient:nbrc903_vitamin_solution']=[(dependency_path,yaml.safe_load(dependency_path.read_text()))]
all_old_proposals=json.loads((R/'successors/issue-1201-v1/proposals.json').read_text())['proposals']
di_proposal=next(p for p in all_old_proposals if p['proposal_id']=='if1201-new-deionized_water')
di_path=R/'successors/issue-1227-v1/research/inorganic_forms/proposed_owners/deionized_water.yaml'
assert sha(di_path)=='b67b85580ee3b894b6641393520755ffc4aa1a8c90eea7052d4336b7237bfccc'
CAT['kgmicrobe.ingredient:deionized_water']=[(di_path,yaml.safe_load(di_path.read_text()))]

def reason(name, curie):
    special = {
    'DI Water':'ATCC1249 explicitly names DI Water in Component III. Conditional dependency on selected if1201-new-deionized_water, whose preparation identity denotes deionization alone, without resistivity, purity, sterility or distillation assertions. This is a proposed overlay entity, not yet a maintained owner; joint integration and independent review are required. The source grade and 400 ml input are preserved.',
    'JCM 197 trace vitamins':'Conditional same-bundle dependency on vm1201-prop-nbrc903-vitamin, not an already admitted maintained owner. Direct JCM197 and NBRC903 tables both enumerate biotin 2 mg, folic acid 2 mg, pyridoxine-HCl 10 mg, thiamine-HCl/riboflavin/nicotinic acid/calcium pantothenate/pABA/lipoic acid 5 mg each, generic B12 0.1 mg and distilled water 1 L. Both filter the vitamin stock; no D-specific pantothenate or cyanocobalamin is introduced. The referenced candidate already cites both sources. Requires joint integration and independent review; frozen Wolfe stock differs. Exact final dependency payload is bound in the author dependency ledger.',
    'Thiamine pyrophosphate':'JCM1100 names thiamine pyrophosphate; ChEBI:9532 names thiamine(1+) diphosphate. This entity reference does not copy chloride-bearing inherited chemical properties. Existing #319/#320/#268 and WITHHOLD position2792 remain in force.',
    'Coenzyme M':'JCM1097 names coenzyme M; ChEBI:17905 is the named free-acid entity. No sodium counterion, separate sodium-salt reagent or solution speciation is inferred.',
    'β-NAD':'JCM1100 explicitly names beta-NAD, a recorded synonym of NAD(+)/CHEBI:15846. No sodium salt, reduced NADH or additional counterion is asserted.',
    'KOH':'TOGO M2567 comments explicitly use KOH at pH 6.5 then 7.0. Reference identifies the named chemical constituent, with no quantity, carrier or stock concentration inferred.',
    'Water':'Water retained in an aqueous supernatant is a curated interpretation of the NBRC1356 process. The amount and retained solutes are unknown.',
    'Sodium Lactate':'ATCC1249 names sodium lactate without stereochemistry; CHEBI:75228 has stereo-unspecified structure, not a sodium L-lactate substitution.',
    'MES':'JCM628 uses MES by mass; select the MES compound entity, not the separate MES-buffer stock.',
    'FeNaEDTA':'Duchefa L0230 specifies ferric sodium EDTA/FeNaEDTA, 36.70 mg/L and 100 micromolar, consistent with the named sodium feredetate entity. No hydrate is introduced.',
    'CaCl2':'Duchefa L0230 explicitly gives CaCl2 332.02 mg/L and 2.99 mM, consistent with the anhydrous formula; do not substitute the dihydrate.',
    'MgSO4':'Duchefa L0230 explicitly gives MgSO4 180.54 mg/L and 1.50 mM, consistent with the anhydrous formula; do not substitute the heptahydrate.',
    'Air':'JCM510 explicitly names air as a constituent of the methane-air blend. The air entity is referenced without invented internal gas fractions.',
    'Calcium D-(+)-pantothenate':'MediaDive5980 explicitly selects D-(+)-calcium pantothenate; the active CHEBI:31345 structure matches that stereochemistry.',
    'D-Calcium pantothenate':'Gibco11120 manufacturer table explicitly selects D-calcium pantothenate; the active CHEBI:31345 structure matches that stereochemistry.'}
    if name in special:return special[name]
    return f'The cited recipe names {name}; the inspected active catalog and primary ontology identity {curie} match this stated chemical form. Source spelling, amount, unit and preparation boundary are preserved; no role, owner-wide or export approval is transferred.'

proposals=[]; assessments=[]; evidence_ledger=[]; components=[]; completeness=[]; promotions=[]
for ix,p0 in enumerate(A['proposals']):
    p=copy.deepcopy(p0); before=R/p['after_capture']['path'];assert sha(before)==p['after_capture']['sha256']
    d=yaml.safe_load(before.read_text());original=copy.deepcopy(d);changes=[]
    for j,e in enumerate(d.get('ontology_mapping',{}).get('evidence',[])):
        if e.get('evidence_type')=='MANUAL_CURATION':
            # None of these newly authored registry-decision entries is human-source evidence.
            assert p['before_sha256'] is None, (p['proposal_id'],j)
            e['evidence_type']='CURATOR_JUDGMENT'
            evidence_ledger.append({'proposal_id':p['proposal_id'],'json_pointer':f'/ontology_mapping/evidence/{j}','before':original['ontology_mapping']['evidence'][j],'after':copy.deepcopy(e),'reason':'This assertion records the author decision to identify a source-qualified preparation in the ingredient registry. The cited primary recipe/product supplies facts; no human reviewer supplied this mapping evidence. CURATOR_JUDGMENT records the decision and the appended event records LLM assistance.'})
    if d!=original:changes.append('IR001: reclassify newly authored registry decisions as CURATOR_JUDGMENT, preserving source URLs and notes')
    if ix in (1,2):
        d['preferred_term']='JCM 403 vitamin solution' if ix==1 else 'JCM 403 vitamin B12 solution'
        for s in d.get('synonyms',[]):
            assert '403' in s['synonym_text'];s['synonym_type']='REJECTED_LABEL'
        changes.append('IR002: qualify the preferred name by JCM and retain the three providerless recipe pointers as REJECTED_LABEL provenance only')
        d['notes']=d.get('notes','').replace('Raw pointer aliases apply only to this JCM formulation.','Providerless Medium No. 403 pointers are retained as REJECTED_LABEL provenance and must not resolve or export as names. Source occurrence links establish this JCM preparation separately.')
    if ix in (2,3):
        old=d['identifier']; ident='kgmicrobe.ingredient:'+Path(p['owner_path']).stem.lower()
        if ix==3:
            ident='kgmicrobe.ingredient:linsmaier_skoog_medium_including_vitamins'
            d['preferred_term']='Duchefa L0230 Linsmaier and Skoog medium including vitamins'
        d['identifier']=ident;d['mapping_status']='MAPPED'
        d['ontology_mapping']={'ontology_id':ident,'ontology_label':d['preferred_term'],'ontology_source':'kgmicrobe.ingredient','mapping_quality':'FALLBACK_REGISTRY','evidence':[{'evidence_type':'CURATOR_JUDGMENT','source':('https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403' if ix==2 else 'https://www.duchefa-biochemie.com/product/details/number/L0230/name/linsmaier-skoog-medium-including-vitamins'),'notes':'Existing placeholder promotion for the source-defined whole preparation. Bounded catalog and ontology searches found the same imported owner and no exact whole-preparation ontology identity. This registry mapping is not an identity mapping to any constituent.'}]}
        if ix==2:
            d['notes']=d['notes'].replace('Preserve UNMAPPED_0567 and all historical source holds.','Promote the existing UNMAPPED_0567 preparation to its ingredient registry identity while preserving its complete history and all historical source holds. Providerless pointers remain nonresolving REJECTED_LABEL provenance. Generic B12 remains ungrounded at component level; no vitamer is selected.')
        else:
            d['notes']=d['notes'].replace('Retain UNMAPPED_0427 pending a separately scoped registry promotion; this proposal is exact source/product provenance and alias enrichment.','Promote the same UNMAPPED_0427 owner to a product-qualified ingredient registry identity; no second owner is created. The 15 listed components describe the dry basal-medium product at the manufacturer\'s nominal reconstitution basis (mg per litre), not a complete supplemented culture or a prepared stock. No water, sugar, growth regulator, final volume or historical batch equivalence is inferred. The certificate corroborates the product formulation; its batch is not assigned to the frozen occurrence.')
            vals=[('CoCl2·6H2O','0.025'),('CuSO4·5H2O','0.025'),('FeNaEDTA','36.70'),('H3BO3','6.20'),('KI','0.83'),('MnSO4·H2O','16.90'),('Na2MoO4·2H2O','0.25'),('ZnSO4·7H2O','8.60'),('CaCl2','332.02'),('KH2PO4','170.00'),('KNO3','1900.00'),('MgSO4','180.54'),('NH4NO3','1650.00'),('myo-Inositol','100.00'),('Thiamine HCl','0.40')]
            d['components']=[{'component_name':n,'reference_scope':'UNMAPPED','concentration_value':v,'concentration_unit':'MG_PER_L'} for n,v in vals]
            d['component_assertion']={'method':'RECIPE_TRANSCRIPTION','completeness':'COMPLETE','evidence':[{'evidence_type':'RECIPE_SOURCE','source':'https://www.duchefa-biochemie.com/product/details/number/L0230/name/linsmaier-skoog-medium-including-vitamins','source_record':'L0230 composition table: Micro Elements, Macro Elements, Vitamins','notes':'Fifteen dry-product inputs; total 4402.49 mg per litre at nominal reconstitution. This is the complete manufacturer enumeration, not an assertion about every supplement in a finished plant culture. No water is a dry-product component.'},{'evidence_type':'RECIPE_SOURCE','source':'https://duchefa-biochemie.com/ac/download/number/L0230/id/7087','source_record':'Certificate of Content, L0230, batch P24889, 12 August 2025','notes':'Corroborates all fifteen formulation inputs and total; does not establish the historical lot used in the frozen source.'}]}
        changes.append('IR004: promote the existing placeholder to the whole-preparation registry identity and complete supported formulation curation')
        target=p['owner_path'].replace('/unmapped/','/mapped/')
        promotions.append({'proposal_id':p['proposal_id'],'old_identifier':old,'new_identifier':ident,'frozen_preimage_path':p['owner_path'],'intended_mapped_path':target,'filename_preserved':Path(target).name==Path(p['owner_path']).name,'source_occurrence_integration_authorized':False})
        p['integration_obligations']=p.get('integration_obligations',[])+[f'Promotion: after independently approved application, move the existing file to {target}, preserving its filename/history; retire placeholder {old} without a duplicate owner; synchronize native maintained surfaces and registry SSSOM through supported tools. This proposal does not apply that change or release source/export holds.']
    if ix==36:
        d.setdefault('synonyms',[]).append({'synonym_text':'JCM 197 trace vitamins','synonym_type':'EXACT_SYNONYM','source':'Source-qualified preparation name: JCM 197 trace-vitamin table https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; exact enumerated input formula and filtration comparison with NBRC 903 https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=903. Conditional same-bundle component dependency; no unqualified Trace vitamins alias or occurrence transfer.'})
        changes.append('IR003: record the source-qualified JCM 197 trace vitamins name after complete primary formula comparison, enabling conditional top-layer references')
    if ix==21:
        d['notes']=d['notes'].replace('It is distinct from a pure cyanocobalamin ingredient and from vitamer-unspecified JCM 403 B12 stock.','The preparation differs from pure cyanocobalamin. Equivalence to the vitamer-unspecified JCM 403 B12 stock is not established: both print 5 mg in 100 ml distilled water, but JCM 403 does not select cyanocobalamin. No chemical distinction or cross-source merge is inferred from that missing vitamer information.')
        changes.append('IR004 duplicate adjudication: qualify the JCM 403 comparison as unresolved equivalence, not a proved chemical distinction')
    newrefs=0
    for j,c in enumerate(d.get('components',[])):
        name=c['component_name'];prev=copy.deepcopy(c)
        if c['reference_scope']!='UNMAPPED':
            components.append({'proposal_id':p['proposal_id'],'component_index':j,'before':prev,'after':copy.deepcopy(c),'outcome':'preserved_existing_assertion','reason':'Existing component assertion belongs to the CultureBotHT source and is outside the new-reference correction. Its source/form comparison and all holds remain unchanged.'});continue
        curie=MAP.get(name)
        if curie:
            assert CAT.get(curie),curie
            owners=[{'path':str(f),'sha256':sha(f),'preferred_term':x['preferred_term'],'mapping_status':x['mapping_status']} for f,x in CAT[curie]]
            c['component_id']=curie;c['reference_scope']='MIM_CATALOG'
            c['source']='Literal source component: '+name+'. Issue 1227 IR003 component-specific adjudication: '+reason(name,curie)
            if name in NORMALIZED_COMPONENT_NAMES:
                c['component_name']=NORMALIZED_COMPONENT_NAMES[name]
                c['source']+=' The component display name uses the equivalent recognized catalog label for native reference validation; the literal source name is preserved here.'
            newrefs+=1;why=reason(name,curie);outcome=('conditional_selected_overlay_reference' if name in ('DI Water','JCM 197 trace vitamins') else 'grounded_compatible_active_entity')
        else:
            assert name in HOLDS, name
            owners=[];why=HOLDS[name];outcome='precise_identity_or_preparation_hold'
            c['source']='Issue 1227 IR003 retained limit: '+why
        components.append({'proposal_id':p['proposal_id'],'component_index':j,'before':prev,'after':copy.deepcopy(c),'outcome':outcome,'reason':why,'catalog_owners':owners,'source_evidence_ids':[i for i in p.get('evidence_ids',[]) if i in E and E[i]['kind']=='primary_source']})
    if newrefs:changes.append(f'IR003: bind {newrefs} compatible source components to active catalog entities or explicitly conditional selected-proposal entities without copying role or export approval')
    if ix==29:
        d['component_assertion']['method']='CURATED_INTERPRETATION';changes.append('IR005: identify retained supernatant water as a curated interpretation, not a literal retained-phase recipe transcription')
        for e in d['component_assertion']['evidence']:
            e['notes']='The recipe lists charged inputs and instructs recovery of supernatant after precipitation. Water in that aqueous recovered phase is an interpretation; retained salts and their amounts/completeness are unknown. Charged masses are provenance only, not retained-solute concentrations.'
    if ix==29 or 40<=ix<=45:
        was=d['component_assertion']['completeness'];d['component_assertion']['completeness']='UNKNOWN'
        d['notes']=d.get('notes','').replace('PARTIAL preparation record','preparation record with UNKNOWN component completeness')
        d['notes']=d['notes'].replace('PARTIAL assertion includes only the known aqueous carrier','Assertion of UNKNOWN completeness includes only the interpreted aqueous carrier')
        for e in d['component_assertion'].get('evidence',[]):e['notes']=e.get('notes','').replace('PARTIAL preparation record','preparation record with UNKNOWN component completeness')
        changes.append('IR006: set UNKNOWN because the source does not establish retained or full stock membership; no explicitly omitted constituent list is claimed')
        completeness.append({'proposal_id':p['proposal_id'],'before':was,'after':'UNKNOWN','reason':'Retained-phase membership unknown after precipitation' if ix==29 else 'Named stock does not specify its carrier or complete constituent set; missing information is not explicit omission.'})
    elif ix in (30,31,32,33):
        completeness.append({'proposal_id':p['proposal_id'],'before':'PARTIAL','after':'PARTIAL','reason':('Malformed source input is explicitly omitted from components and preserved in notes.' if ix<32 else 'CO2 pH treatment and unspecified initial pH adjustment are explicitly outside the six represented inputs.')})
    if newrefs:
        for e in d.get('component_assertion',{}).get('evidence',[]):
            e['notes']=e.get('notes','').replace('Component references remain UNMAPPED pending form-specific grounding.','Compatible components now reference their inspected catalog entities; remaining UNMAPPED references preserve the specific unresolved vitamer, stereochemistry or nested-preparation boundary.')
        d['notes']=d.get('notes','').replace('UNMAPPED component references preserve source wording without inventing hydrate, stereoisomer or vitamer groundings.','Component references identify compatible active entities only after source-form review. Remaining UNMAPPED components retain their precise form or nested-preparation limits. Component names and quantities remain source-specific; no role or export approval is inherited.')
    if changes:
        for old_text,new_text in [('state2 mg','state 2 mg'),('uses0.4 ml of a0.01%','uses 0.4 ml of a 0.01%'),('filter-sterilized0.1','filter-sterilized 0.1'),('added3 ml','added 3 ml'),('its0.01%','its 0.01%'),('gives0.2 ml of 0.1%Vitamin','gives 0.2 ml of 0.1% Vitamin'),('including0.1 ml','including 0.1 ml'),('Vitamin K1(1%solution)','Vitamin K1 (1% solution)'),('main2474','main 2474'),('Solution(100X)','Solution (100X)'),('family11120','family 11120'),('official100X','official 100X')]:
            d['notes']=d.get('notes','').replace(old_text,new_text)
    # No retroactive edits to prior events, roles, counts or unrelated chemistry.
    assert d.get('curation_history')==original.get('curation_history')
    for k in ('occurrence_statistics','nutritional_roles','physicochemical_roles','cellular_metabolic_roles','chemical_properties'):
        assert d.get(k)==original.get(k),(p['proposal_id'],k)
    if d!=original:
        record_curation_event(d,curator='all-unmatched-worker08-issue1227-vitamins',action='BOUNDED_REVIEW_CORRECTION',changes='; '.join(changes)+'. Earlier history and all source, scientific, role, withheld and downstream holds remain. Isolated proposal only.',previous_status=original['mapping_status'],new_status=d['mapping_status'],llm_assisted=True,timestamp=NOW)
        dest=M/'proposed_owners'/Path(p['owner_path']).name
        write_validated_ingredient(d,dest);p['after_capture']=capture(dest)
    p['independent_review']={'status':'pending','evidence_ids':[]}
    p['evidence_ids']=list(dict.fromkeys(p.get('evidence_ids',[])+['vm1227-component-adjudication','vm1227-payload-assessment']))
    proposals.append(p)
    assessments.append({'proposal_id':p['proposal_id'],'predecessor_capture':p0['after_capture'],'successor_capture':p['after_capture'],'owner_path':p['owner_path'],'original_before_sha256':p['before_sha256'],'full_selected_payload_reviewed':True,'changes':changes,'component_count':len(d.get('components',[])),'new_catalog_references':newrefs,'scope':'Only the listed correction fields and audit event change. No owner-wide role, source membership or downstream approval.','primary_source_evidence_ids':[i for i in p.get('evidence_ids',[]) if i in E and E[i]['kind']=='primary_source'],'source_formulation_appraisal':d.get('component_assertion',{}),'history_preserved':True})

decisions=copy.deepcopy(A['decisions'])
for d in decisions:
    ids=set(d['proposal_ids'])
    if ids.intersection(p['proposal_id'] for p in proposals):
        d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+['vm1227-component-adjudication','vm1227-payload-assessment']))
    d['independent_review']={'status':'pending','evidence_ids':[]}
    d['issue_refs']=list(dict.fromkeys(d.get('issue_refs',[])+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1227']))
    if ids & {'vm-prop-jcm403-vitamin','vm-prop-jcm403-b12'}:
        add=' Issue 1227 correction: the preferred name explicitly identifies JCM 403, and the three providerless Medium No. 403 pointer spellings remain REJECTED_LABEL provenance. Occurrence links are preserved separately and no generic pointer becomes a resolving alias.'
        if 'vm-prop-jcm403-b12' in ids:add+=' The existing UNMAPPED_0567 is promoted as the documented 5 mg B12 plus 100 ml distilled-water preparation, with its filename/history preserved; the generic B12 component remains ungrounded and all vitamer/source holds remain.'
        d['reasoning']+=add;d['applicability']+=add
    if 'vm-prop-linsmaier-skoog' in ids:
        add=' Issue 1227 correction completes promotion of the same existing UNMAPPED_0427 to the Duchefa L0230 registry preparation, with the manufacturer\'s 15 dry-product components at their nominal mg/L reconstitution basis. It adds no water, culture supplements, historical lot claim or whole-product ontology shortcut.'
        d['reasoning']+=add;d['applicability']+=add
    if 'vm-prop-new-31' in ids:
        d['reasoning']+=' IR004 duplicate comparison: the same printed B12 mass and water volume in JCM 403 do not establish stock equivalence because JCM 403 does not name a vitamer. Neither chemical difference nor a cross-source merge is inferred; the explicit cyanocobalamin assertion remains specific to NBRC 1321.'
    if ids & {p['proposal_id'] for p in completeness if p['after']=='UNKNOWN'}:
        d['reasoning']=d['reasoning'].replace('PARTIAL assertion','UNKNOWN completeness assertion').replace('PARTIAL generic','named generic').replace('PARTIAL owner','owner with UNKNOWN component completeness')
        d['applicability']=d['applicability'].replace('PARTIAL assertion','UNKNOWN completeness assertion').replace('PARTIAL generic','named generic').replace('PARTIAL owner','owner with UNKNOWN component completeness')
        d['reasoning']+=' Issue 1227 distinguishes incomplete knowledge from explicit omitted constituents: the preparation remains supported, but its component completeness is UNKNOWN.'
    for k in ('case_id','case_input_sha256','source','occurrence_ids','preserved_native_decisions'):
        prev=next(x for x in A['decisions'] if x['case_id']==d['case_id']);assert d.get(k)==prev.get(k)

dump('proposals.json',proposals);dump('decisions.json',decisions)
dump('evidence-category-corrections.json',evidence_ledger)
dep_final=next(p for p in proposals if p['proposal_id']=='vm1201-prop-nbrc903-vitamin')
for c in components:
    if c['after'].get('component_id')=='kgmicrobe.ingredient:nbrc903_vitamin_solution':
        c['catalog_owners']=[{'path':str(R/dep_final['after_capture']['path']),'sha256':dep_final['after_capture']['sha256'],'preferred_term':'NBRC 903 vitamin solution','mapping_status':'MAPPED','admission_status':'conditional selected-proposal overlay; not maintained'}]
    elif c['after'].get('component_id')=='kgmicrobe.ingredient:deionized_water':
        c['catalog_owners'][0]['admission_status']='conditional selected-proposal overlay; not maintained'
dump('component-adjudications.json',components)
dump('payload-assessments.json',assessments)
dump('completeness-adjudications.json',completeness)
dump('promotion-obligations.json',promotions)
dep=next(p for p in proposals if p['proposal_id']=='vm1201-prop-nbrc903-vitamin')
dump('conditional-component-dependencies.json',[{'source_proposal_id':pid,'component_name':'JCM 197 trace vitamins','target_proposal_id':dep['proposal_id'],'target_after_capture':dep['after_capture'],'target_identifier':'kgmicrobe.ingredient:nbrc903_vitamin_solution','catalog_status':'selected proposal overlay only; not maintained','source_evidence_ids':['vm-fetch-0c1e7fd46063ca00','vm-fetch-2630e40c26a0b155'],'reason':reason('JCM 197 trace vitamins',dep['proposal_id']),'holds':'Requires joint independently approved integration. All source occurrences and native withheld/role/export decisions remain unchanged.'} for pid in ['vm1201-prop-jcm628-toplayer','vm1201-prop-jcm629-toplayer']])
dump('conditional-deionized-water-dependency.json',{'source_proposal_id':'vm-prop-new-26','target_proposal_id':di_proposal['proposal_id'],'predecessor_target_after_capture':di_proposal['after_capture'],'target_after_capture':capture(di_path),'target_identifier':'kgmicrobe.ingredient:deionized_water','status':'conditional selected-proposal entity; final issue1227 payload bound; joint integration and independent review required','source_evidence_ids':['if1201-primary-1394663ed57400f4'],'reason':reason('DI Water','kgmicrobe.ingredient:deionized_water')})
print(json.dumps({'decisions':len(decisions),'proposals':len(proposals),'mapping_evidence_entries_corrected':len(evidence_ledger),'payloads_with_category_correction':len({x['proposal_id'] for x in evidence_ledger}),'new_component_references':sum(x['new_catalog_references'] for x in assessments),'payloads_changed':sum(x['predecessor_capture']!=x['successor_capture'] for x in assessments),'UNKNOWN_corrections':len([x for x in completeness if x['after']=='UNKNOWN'])}))
