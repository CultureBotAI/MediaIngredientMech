"""Build isolated #1201 biological proposals. Never write maintained records."""
from pathlib import Path
import json, hashlib, datetime, copy, subprocess, re
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient

ART = Path('reports/all_unmatched_20261107/worker-04')
S = ART / 'successors/issue-1201-v1'
F = S / 'fragments'
CAP = S / 'captures/biological'
OUT = S / 'proposals/biological'
QUEUE = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
rows = json.loads((F/'biological-assignment.json').read_text())['cases']
A = {r['index']:r for r in rows}
OLD_E = {e['evidence_id']:e for e in json.loads((ART/'evidence.json').read_text())['evidence']}
OLD_P = json.loads((ART/'proposals.json').read_text())['proposals']
all_decisions = json.loads((ART/'decisions.json').read_text())['decisions']
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canonical(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def write_json(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def prose(s):
    """Separate ordinary prose quantities; never call this on IDs or URLs."""
    s=re.sub(r'(?<=[a-z])(?=\d)', ' ', s)
    s=re.sub(r'(?<=\d)(?=(?:ml|mg|g|L|h|min|units|C)\b)', ' ', s)
    s=re.sub(r'(?<=\d)(?=(?:g|ml|min|h|C|L)\d)', ' ', s)
    s=re.sub(r'\b(DSMZ|NBRC|JCM|CHEBI|NCIT|FOODON|MediaDiveingredient)(?=\d)', r'\1 ', s)
    return s

# These actual searches include ignored files. Search results are evidence of the
# searched universe, not proof that string similarity entails identity.
searches=[]
for name,pattern in [('seawater',r'sea.?water|Biomaris'),('potato',r'potato'),('oats',r'oatmeal|Quaker|oat.spelt'),('whey_juice',r'whey|V.?8|vegetable.juice'),('grain_feed',r'malted.wheat|corn.*fish|cornmeal.extract|horn.meal|larchwood'),('catalase_biomass_air',r'Catalase|Porphyra|sterile.air')]:
    cmd=['rg','-uu','-n','-i',pattern,'data/ingredients','docs/data/label_index.csv',str(ART/'proposals'),str(ART/'decisions.json')]
    r=subprocess.run(cmd,capture_output=True,text=True)
    searches.append({'name':name,'command':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
catalog=[]
for p in sorted(Path('data/ingredients').rglob('*.yaml')):
    d=yaml.safe_load(p.read_text())
    catalog.append({'path':str(p),'sha256':sha(p),'identifier':d['identifier'],'preferred_term':d['preferred_term'],'synonyms':d.get('synonyms',[])})
catalog_ids={x['identifier'] for x in catalog}
catalog_labels={x['preferred_term'].casefold() for x in catalog}
old_payloads=[]
for p in OLD_P:
    f=ART/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256']
    d=yaml.safe_load(f.read_text());old_payloads.append({'proposal_id':p['proposal_id'],'owner_path':p['owner_path'],'identifier':d['identifier'],'preferred_term':d['preferred_term'],'case_ids':p['case_ids'],'after_sha256':sha(f)})
preflight={'performed_at':now,'ignored_files_included':True,'searches':searches,'baseline_catalog':catalog,'published_proposals':old_payloads,'all188_case_labels':[{'case_id':d['case_id'],'source':d['source']} for d in all_decisions]}
write_json(CAP/'catalog-searches.json',preflight)

# Full frozen snapshot bytes and prior evidence bindings are checked again. This
# does not supply new retrieval dates for reused captures.
bindings=[]
for r in rows:
    d=r['published_decision'];c=r['frozen_case']
    assert canonical(c)==d['case_input_sha256']
    for o in c.get('occurrences',[]):
        p=QUEUE/o['full_recipe_snapshot'];assert sha(p)==o['source_file_sha256'];yaml.safe_load(p.read_text())
        bindings.append({'case_id':c['case_id'],'occurrence_id':o['occurrence_id'],'path':o['full_recipe_snapshot'],'sha256':sha(p)})
    for eid in d['evidence_ids']:
        e=OLD_E[eid];root=ART if e['capture']['root']=='artifact' else QUEUE
        p=root/e['capture']['path'];assert sha(p)==e['capture']['sha256'],(eid,p)
write_json(CAP/'reused-input-bindings.json',{'scope':'All38 complete frozen cases, every linked full recipe snapshot and each reused evidence body; prior URL and retrieval metadata remain unchanged.','bindings':bindings})
EV=[]
def evidence(eid,path,kind,claim,case_nums,locator='$',url=None,accessed=None):
    x={'evidence_id':eid,'kind':kind,'capture':{'root':'artifact','path':str(path.relative_to(ART)),'sha256':sha(path)},'url':url,'locator':locator,'supports_or_contradicts':claim,'case_ids':[A[n]['frozen_case']['case_id'] for n in case_nums]}
    if accessed:x['accessed_at']=accessed
    EV.append(x);return eid
SEARCH=evidence('I1201-BIO-CATALOG',CAP/'catalog-searches.json','local_validation','Ignored-inclusive baseline catalog, label-index and all63 published payload searches; full188 label comparison. Candidate identities still require the per-case scientific comparison.',list(A))
BIND=evidence('I1201-BIO-REUSED-BINDINGS',CAP/'reused-input-bindings.json','local_validation','All reused source bodies and frozen snapshots match their recorded hashes; no old retrieval timestamp was replaced.',list(A))
for file,nums,claim in [('mesh-catalase-v2.json',[42,48,141],'Official NLM descriptor D002374 is active and has label Catalase; retained species-neutral parent, not human CAT gene identity.'),('mj-izumi2012-v2.pdf',[52],'Author manuscript explicitly gives an MJ synthetic seawater formula citing Sako1996. This is a candidate formulation lineage, not automatic proof of the exact M3127 preparation version.'),('mj-takai2005-v2.pdf',[52],'Primary author manuscript supplies MJ/MMJ usage and bibliography for formulation-lineage review; source applicability must be established separately.')]:
    r=json.loads((CAP/(file+'.receipt.json')).read_text());assert r['curl_exit_code']==0
    evidence('I1201-BIO-'+file.split('.')[0],CAP/file,'primary_source',claim,nums,url=r['url'],accessed=r['accessed_at'])
for file,nums in [('mesh-catalase.json',[42,48,141]),('mj-izumi2012.pdf',[52]),('mj-takai2005.pdf',[52])]:
    p=CAP/(file+'.receipt.json');r=json.loads(p.read_text())
    assert r['curl_exit_code']!=0
    evidence('I1201-BIO-FAILED-'+file.split('.')[0],p,'unsuccessful_search','Initial sandboxed network request failed and produced no source body. This is a retrieval limitation, not negative identity evidence; later v2 capture succeeded.',nums,url=r['url'],accessed=r['accessed_at'])
for file in ['oatmeal-owner-lineage.json','oatmeal-owner-historical-reconstruction.json']:
    evidence('I1201-BIO-'+file[:-5],CAP/file,'source_snapshot','Actual full-owner lineage investigation: current23 matching rows,18 MediaRecipe candidates, original18-count historical table absent from git, and historical recipe readbacks. Equality of counts is not claimed to prove historical membership.',[72,106,165])
for p in sorted(CAP.glob('oatmeal-owner-*-recipes/**/*.yaml')):
    evidence('I1201-BIO-OAT-RECIPE-'+sha(p)[:20],p,'source_snapshot','Complete copied recipe bytes read for oatmeal input versus filtered infusion, commercial agar and source-form boundaries. Copy time is not source retrieval time.',[72,106,165],locator='complete YAML')

plans=[]
def plan(key,nums,label,notes,missing='',existing=None,components=None,stock=False,parent=None):
    plans.append(dict(key=key,nums=nums,label=label,notes=prose(notes),missing=prose(missing),existing=existing,components=components,stock=stock,parent=parent))

plan('biomaris_seawater',[9],'DSMZ 1752 Biomaris seawater',
 'DSMZ1752 names Biomaris Seawater as the liquid base. The separately supplied salt replacement is an alternative and is not the bottled product formula. This record retains the branded seawater material without asserted lot, constituents, salinity or treatment. No equivalent owner exists among baseline sea-water classes or published seawater stocks.',
 'Product lot/formulation is unspecified; this limits composition and equivalence claims, not a bounded product-material record.')
plan('potato_tuber_tissue',[16,144],'Potato tuber tissue',
 'Potato material supplied as tuber tissue in the linked recipes. The material input is distinct from liquid potato infusion or extract after boiling and filtration. Case16 occurrences carrying peeled-and-cut notes are additionally bound to the more specific peeled/cut material proposal. Starting potato masses are process input amounts, not measured retained solids in a filtrate. FOODON03315354 names a potato tuber; FOODON00002796 covers whole/piece derivatives, but no exact claim erases a recipe-specific preparation.',
 'Extraction yield and tissue removal vary by recipe; no single output preparation or finished-medium potato concentration is asserted.')
plan('peeled_cut_potato',[16,104],'Peeled and cut potato tuber tissue',
 'JCM30/54/55/116 and the explicitly qualified frozen rows supply peeled, cut potato as a preparation input. Cut does not specify a dice size, so the existing Diced Potato owner is not an exact substitute. JCM30 boils200g in1L for20min then sieves; JCM54/55 combine potato and carrot and filter through cheesecloth. Those outputs remain distinct; the record describes the peeled/cut tissue before extraction.',
 'Only explicitly peeled-and-cut source occurrences are within this material scope; no inference to unqualified or boiled-extract rows.')
plan('m2231_sterile_air',[20],'TOGO M2231 sterile air carrier gas',
 'TOGO M2231 describes cultures bubbled with5% CO2-containing sterile air. This record denotes the sterile air carrier input, not CO2 alone, liquid-medium volume, or the aeration operation. The supplied gas is used with CO2; no invented N2/O2 percentages or sterility process are asserted. The5% figure is preserved as source context and is not converted to an unstated molar/volume basis.',
 'Air sterilization technique, gas flow rate and5% basis are absent; these limit process reproduction, not identity of the stated carrier gas.')
plan('nbrc355_acid_whey',[23],'NBRC 355 acid-precipitated milk supernatant',
 'NBRC355 directs adding HCl to warmed milk to coagulate it, centrifuging, and using the supernatant as cheese whey. The source-defined output can be represented without a quantified yield. Starting milk and HCl are processing inputs; precipitated milk proteins are removed, and their masses or final retained fractions are not asserted as has-part components. Applies only to CultureMech015901/nbrc.medium355 in case23.',
 'Milk source, acid quantity, temperature and centrifugation settings are not stated; no acid/rennet or formulation equivalence is asserted for the other six case23 occurrences.')
plan('cheese_whey_unspecified',[23],'DSMZ 775 and JCM 162 cheese whey',
 'DSMZ775 and JCM162 name cheese whey as the liquid substrate without the NBRC355 acid-coagulation preparation. This is the source-stated cheese-whey material class, with unspecified production process and composition, not purified lactose, whole milk or a1g/L chemical. The six non-NBRC355 occurrences are covered; primary1L/1000ml quantities and malformed frozen G_PER_L or PERCENT_V_V values remain distinct evidence.',
 'Production method and composition are unspecified. No claim of equivalence to the separately defined NBRC355 acid whey is made.')
plan('nbrc985_sterilized_natural_seawater',[26],'NBRC 985 sterilized natural seawater',
 'NBRC985 explicitly identifies sterilized natural seawater in the Porphyra cultivation context. The preparation boundary is retained without equating it to untreated natural seawater, pasteurized water or synthetic salt medium. No sterilization method or receiving dose is inferred.',
 'Sterilization method and receiving-medium dose are not supplied; neither is needed to preserve this source-stated prepared material.')
plan('nbrc15_treated_v8_supernatant',[29],'NBRC 15 calcium-carbonate-treated V8 supernatant',
 'Stir approximately300ml V-8 juice with3g CaCO3 for2h, then centrifuge and retain the supernatant. NBRC15 uses200ml of that output with800ml2% seawater and15g agar. CaCO3 and initial juice volumes are processing inputs, not proven retained output components or concentrations. Final medium pH7.0 belongs to the receiving agar, not an independently measured stock pH. This preparation differs from whole V8 Juice/V8 Canned Vegetable Juice owners.',
 'Yield, residual CaCO3 and product lot are unknown; the preparation protocol already defines the authorized isolated material.')
plan('nbrc_cornmeal_extract',[33],'NBRC cornmeal extract ingredient',
 'NBRC16/17/24/1114 and their TOGO counterparts identify cornmeal extract, usually2g per source recipe. It is a biological extract ingredient; the existing Corn Meal material and complete Corn Meal Agar are not the extract. No extraction solvent, brand or chemical composition is supplied. This bounded source-stated extract class has no asserted processing yield or global cornmeal alias.',
 'Extract production protocol and supplier remain unknown; this blocks exact product/formula equivalence, not the disclosed extract material identity.')
plan('catalase_c9322',[42,48,141],'Catalase',
 'Add only the supplier-verified C9322 supplied form to the existing cas9001-05-2 owner. Supplier COA names bovine-liver catalase, lyophilized powder,2,000-5,000units/mg protein. The retained MeSHD002374 broad parent is species-neutral and #312 human NCITC61062 exclusion remains. Case42 supplies the exact catalog binding. Case48 establishes bovine catalase without that catalog; case141 is generic enzyme reagent. Neither is silently identified with C9322. Existing non-name Properties aliases are not approved by this delta.',
 'Whole-owner publication review and inherited holds persist; uncatalogued case48 and generic141 cannot inherit C9322 form/activity.',existing='data/ingredients/mapped/Catalase.yaml')
plan('malted_wheat_meal',[45,185],'Malted wheat meal',
 'JCM730 names2g malted wheat meal as an input in rye-bran extract preparation with40g rye bran,0.8g trypsin and1L water incubated50C24h, centrifuged500xg15min and filtered. MediaDiveingredient1881 and all three CultureMech occurrences refer to that input. Malted wheat meal is distinct from whole wheat grains, malt extract, wheat arabinoxylan and the resulting rye-bran extract. FOODON wheat malt is a candidate broader material; additional coarse-ground/unheated qualifiers are not inferred.',
 'Particle size and detailed malt processing are unspecified; no exact coarse-ground ontology term is claimed.')
plan('m3127_mj_synthetic_seawater',[52],'TOGO M3127 MJ synthetic seawater base',
 'M3127 specifies1L MJ synthetic seawater, with separate modifications to make MMJ/MMJS. The source points to Sako1996 and Takai1999; newly captured author papers give MJ lineage and a2012 formulation, but exact version continuity to the M3127 preparation is not proven. Preserve the named base as an opaque source-qualified stock. It is distinct from the published JCM492 Modified MJ owner; neither later formula nor MMJ additions are silently installed as MJ constituents.',
 'Exact base formulation/version linkage remains unverified despite primary-paper retrieval; source-qualified named stock representation is nevertheless authorized.',stock=True)
plan('oat_spelt_xylan',[66],'Oat-spelt xylan preparation',
 'M2313 names xylan from oat spelts as an alternative carbon-substrate input. This is a botanical xylan preparation distinct from larchwood and beechwood products. CHEBI37166 is the generic xylose-residue polymer class; no purity or molecular equivalence of the complete botanical preparation is proven. Use a registry identity without invented CAS, purity or has-part constituents.',
 'Supplier/catalog and purity are unspecified, limiting chemical equivalence but not botanical preparation scope.')
plan('nbrc1130_seawater_3pct',[70],'NBRC 1130 seawater at stated 3 percent salinity',
 'TOGO M1886/NBRC1130 specifies1L seawater at3% salinity. Preserve that concentration qualifier and source provenance. It does not specify3% sodium chloride, a molecular formula, or an artificial seawater brand. The distinct salinity-qualified material is not reduced to bare seawater.',
 'Salinity definition/basis and source water are unstated; no conversion to NaCl mass or specific artificial recipe is authorized.')
plan('oatmeal_supplied_form',[72,106,165],'Oatmeal',
 'Record the explicitly powdered Quaker White Oats input from JCM52/NBRC304 in supplied_form, without creating a second brand owner or adding global aliases. This physical form is not automatically the fine colloidal whole-oat form in NCITC29298. MediaDive471/DSMZ425 generic food oatmeal is not automatically powdered. Existing whole-owner mapping is retained under an explicit unresolved identity hold, rather than silently regrounded from three cases. Current23 matching source rows and full recipe bytes plus18 historical candidate readbacks were inspected; exact membership of the old18-count untracked table is not established.',
 'The old18-member occurrence table at CultureMech15a4da5c08 is absent from git; current23 rows include18 MediaRecipes and5 SolutionRecipes. Exact historical membership and fine/colloidal form scope require reconciliation before whole-owner reidentification. This does not block adding the supported source-stated supplied form.',existing='data/ingredients/mapped/Oatmeal.yaml')
plan('nbrc1429_seawater_175pct',[79],'NBRC 1429 seawater at stated 1.75 percent salinity',
 'NBRC1429 names1L seawater with1.75% salinity. Retain the qualifier as written. Neither a1:1 dilution of3.5% water, a NaCl solution nor a particular natural/artificial origin is specified.',
 'Salinity basis and source-water preparation are unstated; detailed composition remains unknown.')
plan('jcm1216_artificial_seawater_01x',[83],'JCM 1216 artificial seawater 0.1x',
 'JCM1216 BSW3 Agar specifies0.1x artificial seawater as the liquid base. The retrieved complete recipe does not give the1x formula or a product identifier. This is a source-qualified dilution-state stock, kept distinct from published JCM6510.5x, JCM9101x and JCM12694x stocks. No assumed1x composition is copied from those other media.',
 'The identity/formula of the1x base remains missing; a bounded source stock can still preserve the specified0.1x state.',stock=True)
plan('nbrc14_corn_fish_feed',[91],'NBRC 14 corn and fish meal bird feed',
 'NBRC14 identifies a corn and fish meal mixture sold as bird feed.20g is boiled in approximately1L water for1h, filtered, and the liquid restored to1L before agar addition. This record denotes the feed input, not its aqueous extract. Named corn and fish meal components are recorded as a partial qualitative enumeration with no ratios. Neither commercial feed brand nor exact formulation is inferred.',
 'Feed ratios, brand and further ingredients are unknown; qualitative composition is explicitly partial.',components=['Corn material','Fish meal'])
plan('charcoal_filtered_natural_seawater',[93,163],'Charcoal-filtered natural seawater',
 'DSMZ1008 specifies charcoal-filtered natural seawater800ml with200ml distilled water; MediaDiveingredient2142 and both source cases point to this preparation. Charcoal filtration is a retained process boundary. The existing Distilled Water rejected label remains rejected, and generic filtered/natural seawater is not exact identity. Biomaris is a separately allowed substitute, not proof of identical composition. The800ml dose is not converted from faulty frozen mass/percentage units.',
 'Charcoal bed/contact parameters are unstated; this does not prevent representing the disclosed treated-water class.')
plan('aged_seawater',[100],'Aged seawater preparation',
 'NBRC1347 and JCM995 identify aged seawater as a liquid input. JCM995 uses700ml with other separately listed stock additions; NBRC1347 specifies1L. JCM900/149 references belong to Hutner stock context, not an aging protocol. No aging time, sterilization, filtration or salinity is guessed. This class is distinct from source-disjunctive filtered-aged-water OR DaigoSP choices in38/116.',
 'Aging duration/conditions are not stated; they constrain detailed reproducibility but not the explicit aged-material scope.')
plan('nbrc_seawater_2pct',[101,105],'NBRC seawater at stated 2 percent salinity',
 'NBRC15/16/22/24/1071 source inputs retain a2% salinity qualifier; case101 and case105 differ only capitalization and resolve to this same stated material class. No assumption of pure NaCl, natural provenance or artificial seawater formulation is made. Case22 explicitly offers natural/artificial alternatives and is not collapsed into this proposal as a resolved choice.',
 'Salinity basis and detailed source composition are unstated; no molecular concentration is inferred.')
plan('m2843_boiled_potato_extract',[127],'TOGO M2843 boiled-potato extract',
 'M2843 comments explicitly say potato extract from200g boiled potato per litre. The component surface boiled potato is a preparation-input shorthand, not200g/L retained extract solids. Represent the source-qualified extract output, without assigning CAS93348-51-7 or mapping to whole potato tissue. Existing Infusion From Potatoes is tied to different unspecified source recipes and is not proven protocol-equivalent.',
 'Boiling duration, extraction/solid separation method and yield are unspecified; the bounded extract identity remains supported.')
plan('nbrc984_porphyra_thalli',[129],'NBRC 984 Porphyra yezoensis thalli cultivated in IMK seawater',
 'NBRC984 describes thalli of Porphyra yezoensis cultivated in IMK medium with seawater. This is a source-qualified cultivated biological material, not a pure polysaccharide, taxon alone, or the entire IMK formula. Cultivation context is preserved in its identity; no harvested dry mass, sterilization or residual growth-medium composition is invented.',
 'Harvest state, inoculum amount and carried-over culture fluid are not specified; no cleaned/dried biomass or complete medium formulation is asserted.')
plan('larchwood_xylan',[136],'Larchwood xylan',
 'JCM99 names larchwood xylan (Sigma) as a material input; MediaDiveingredient1624 identifies the existing owner. Promote this original owner to a botanical-preparation registry identity, retaining prior history including#294. The prior CHEBI parent was removed for misattributed provenance; newly reviewed CHEBI37166 still defines a generic xylan polymer, not an exact complete preparation. No exact chemical parent, CAS or purity is needed for this bounded promotion.',
 'Product catalog and purity remain unspecified; source-specific publication holds persist.',existing='data/ingredients/unmapped/Larchwood_Xylan.yaml')
plan('diced_potato',[143],'Diced potato',
 'MediaDiveingredient728 and DSMZ789 identify diced potato as an input:20g potato is boiled in1L water30min, filtered and restored to1L. Promote the existing physical-form material owner, not the filtrate. The inherited historical report quotation claiming200g/L is preserved as historical prose but explicitly not adopted as current primary evidence. No universal20g/L concentration belongs on the tissue owner.',
 'Dice dimensions and extraction yield are absent; they do not block the identified diced-tissue class.',existing='data/ingredients/unmapped/Diced_Potato.yaml')
plan('bovine_horn_meal',[146],'Bovine horn meal',
 'MediaDiveingredient481 and DSMZ440 identify bovine horn meal10g as a material input. Promote the existing owner to a registry identity for processed bovine-horn meal. It is not purified keratin, horn-and-hoof mixed meal or skim milk separately present in the source. No unsupported processing temperature, protein percentage or exact food ontology subtype is asserted.',
 'Processing details and lot composition are unspecified; known animal/tissue/meal scope supports a registry owner.',existing='data/ingredients/unmapped/Bovine_Horn_Meal.yaml')

P=[];bycase={n:[] for n in A}
for spec in plans:
    nums=spec['nums'];key=spec['key'];before=spec['existing'];pid='I1201-BIO-P-'+key
    assert all(n in A for n in nums)
    oldrecord=yaml.safe_load(Path(before).read_text()) if before else None
    d=copy.deepcopy(oldrecord) if oldrecord else {'identifier':'kgmicrobe.ingredient:'+key,'preferred_term':spec['label'],'mapping_status':'MAPPED','ingredient_type':'STOCK_SOLUTION' if spec['stock'] else 'UNDEFINED_MIXTURE'}
    eidrefs=sorted({x for n in nums for x in A[n]['published_decision']['evidence_ids']}|{SEARCH,BIND})
    urls=sorted({OLD_E[e].get('url') for e in eidrefs if e in OLD_E and OLD_E[e].get('kind')=='primary_source' and OLD_E[e].get('url')})
    if key=='catalase_c9322':
        d.setdefault('supplied_form',[]).append({'name':'Catalase from bovine liver','cas_rn':'9001-05-2','form':'lyophilized powder','supplier':'Sigma-Aldrich','catalog_number':'C9322','notes':'Supplier COA C9322-1G batch0000495897/source batch0000402808 names2,000-5,000units/mg protein. Batch result3190units/mg and86% protein are lot-specific, not universal material properties. TOGO M2399/M2402/M2404 bind this catalog to case42 OADC input. Case48 uncatalogued beef catalase and case141 generic catalase are not assigned this product. Source: https://www.sigmaaldrich.cn/certificates/sapfs/PROD/sap/certificate_pdfs/COFA/Q14/C9322-1G0000495897.pdf'})
        eidrefs.append('I1201-BIO-mesh-catalase-v2')
    elif key=='oatmeal_supplied_form':
        d.setdefault('supplied_form',[]).append({'name':'Quaker White Oats (powdered)','form':'powder, as stated by JCM52 and NBRC304','supplier':'Quaker','notes':'JCM52 Oatmeal-Nitrate Agar and NBRC304 specify3g powdered Quaker White Oats as input. No catalog, grain-size limit, colloidal manufacture or NCITC29298 exact identity is inferred. This source-form addition does not establish powder processing for generic MediaDive471 oatmeal. Sources: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=52 ; https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=304'})
        eidrefs += [x['evidence_id'] for x in EV if x['evidence_id'].startswith('I1201-BIO-OAT') or x['evidence_id'].startswith('I1201-BIO-oatmeal')]
    else:
        if oldrecord:d['identifier']='kgmicrobe.ingredient:'+key;d['mapping_status']='MAPPED'
        if not oldrecord:
            assert d['identifier'] not in catalog_ids and d['preferred_term'].casefold() not in catalog_labels,(key,'baseline collision')
            assert d['identifier'] not in {p['identifier'] for p in old_payloads},(key,'published proposal collision')
        d['ontology_mapping']={'ontology_id':d['identifier'],'ontology_label':d['preferred_term'],'ontology_source':'kgmicrobe.ingredient','mapping_quality':'FALLBACK_REGISTRY','evidence':[{'evidence_type':'MANUAL_CURATION','source':'; '.join(urls),'notes':spec['notes']}]}
        if spec['stock']:d['solution_type']='MINERAL_STOCK'
        if spec['components']:
            d['components']=[{'component_name':x,'reference_scope':'UNMAPPED'} for x in spec['components']]
            d['component_assertion']={'method':'RECIPE_TRANSCRIPTION','completeness':'PARTIAL','evidence':[{'evidence_type':'RECIPE_SOURCE','source':urls[0],'source_record':'NBRC14 feed ingredient','notes':'Source names corn and fish meal; proportions and any other feed ingredients are not given.'}],'notes':'Qualitative components of feed input only. Starting feed mass is not retained extract composition.'}
    d['notes']=(d.get('notes','')+'\n\n#1201 isolated proposal: '+spec['notes']+' '+spec['missing']+' Raw source spellings are retained in case evidence and this source scope; no new globally resolving source-local alias is added. Full-owner publication approval and all source-specific holds remain pending.').strip()
    # Preserve all existing supplied forms byte-semantically; only improve prose
    # spacing in the newly appended form. No identity or URL token is rewritten.
    event={'timestamp':now,'curator':'codex_worker04_biological_issue1201','action':'PROPOSED_SOURCE_BOUND_CURATION','changes':spec['notes'],'new_status':d['mapping_status'],'llm_assisted':True}
    if oldrecord:event['previous_status']=oldrecord['mapping_status']
    d.setdefault('curation_history',[]).append(event)
    filename=Path(before).name if before else ''.join(w.capitalize() for w in key.split('_'))+'.yaml'
    target=OUT/filename;assert target.parent==OUT
    write_validated_ingredient(d,target)
    owner=before or 'data/ingredients/mapped/'+filename
    p={'proposal_id':pid,'case_ids':[A[n]['frozen_case']['case_id'] for n in nums],'description':spec['notes'],'evidence_ids':sorted(set(eidrefs)),'owner_path':owner,'kind':'edit_existing_owner' if before else 'new_owner','before_sha256':sha(before) if before else None,'after_capture':{'root':'artifact','path':str(target.relative_to(ART)),'sha256':sha(target)},'publication_obligations':['Retain all inherited source-specific holds and do not infer complete-owner publication approval.','Coordinator must compare original baseline beforehash and all other worker proposals; synchronize maintained surfaces only during separately guarded integration.','No new generic source-local resolving aliases are authorized.'],'cross_shard_owner_conflict':'Check exact beforehash and active proposal owner registry; never apply last-writer-wins.','supersedes_proposal_ids':[]}
    if before and '/unmapped/' in before:p['integration_target_path']=before.replace('/unmapped/','/mapped/');p['integration_action']='Promote original owner and move its path; never retain a duplicate unmapped copy.'
    P.append(p)
    for n in nums:bycase[n].append(p)

# Four genuine unresolved alternatives and one already-correct owner require no
# material payload. Every other case receives the supported bounded work above.
kept={
22:('NBRC13 explicitly permits natural OR artificial seawater diluted to2% salinity. These alternatives can have different preparation identities. Catalog lookup found natural-water and artificial-stock classes but neither selects the actual source alternative. A generic source-qualified disjunction record would not denote one distinct substance.','The chosen natural versus artificial preparation, and for the artificial option its base recipe/product, are missing identity facts.'),
38:('NBRC335 explicitly permits filtered aged natural seawater OR Daigo Artificial Seawater SP. These are alternatives, not synonyms or components of one mixture. Existing filtered/natural-water owners and published artificial stocks do not establish which option was used.','The actual selected alternative is missing; no source-local pointer alias can choose it.'),
46:('DSMZ1054 explicitly permits Biomaris089, natural or artificial seawater. The separately proposed DSMZ1752 Biomaris material forcase9 does not select the alternative in this case or establish exact089 product/version equivalence.','The chosen product/natural/artificial branch is missing; a source-disjunction owner would conflate distinct substances.'),
116:('NBRC336 explicitly permits filtered aged seawater OR Daigo Artificial Seawater SP. Full source and catalog comparison retain the same genuine alternative boundary ascase38.','The selected alternative is missing; the source does not assert a mixture of both.'),
155:('MediaDiveingredient1707 traces to JCM248, whose preparation explicitly starts with50g dry cow manure, boils in1L water for1h, and filters. Existing Dry_Cow-manure already represents the dry material input and preserves #391. The filtrate is a different output; the raw Cow manure source input does not justify splitting or reversing the already-correct owner.','No material-edit requirement remains for this source input. Extract yield is not needed to affirm the dry-input scope and no full-owner hold is released.')}

D=[];R=[]
for n,r in A.items():
    old=r['published_decision'];new=copy.deepcopy(old);ps=bycase[n]
    performed=['Read complete frozen case and linked full recipe snapshots; verify their hashes.','Inspect original decisions/evidence/owner history and reused primary captures.','Run ignored-inclusive baseline owner and label-index search, inspect all63 published proposal identities, and compare all188 source labels.']
    if ps:
        specs=[s for s in plans if n in s['nums']]
        reasoning=' '.join(s['notes'] for s in specs)
        missing=' '.join(s['missing'] for s in specs)
        new.update({'reasoning':reasoning,'proposal_ids':[p['proposal_id'] for p in ps],'no_change_reason':None,'missing_requirement':missing,'independent_review':{'status':'pending','evidence_ids':[]},'primary_reviewer':'Codex /root/biological #1201 successor','evidence_ids':sorted(set(old['evidence_ids']+[e for p in ps for e in p['evidence_ids']]))})
        new['disposition']='stock_product_mixture_context'
        new['publication_scope']='Successor source-case disposition and isolated delta only; all frozen source-specific holds and complete-owner publication gates remain in force.'
        new['native_record_review_applicability']='Proposed complete owner payload requires coordinator native review packaging; source-specific evidence does not approve unrelated owner assertions.'
        for p in ps:
            if p['kind']=='edit_existing_owner' and not any(o['path']==p['owner_path'] for o in new['owner_records']):new['owner_records'].append({'path':p['owner_path'],'sha256':p['before_sha256']})
        D.append(new);status='changed';performed.append('Created guarded, closed-schema validated isolated owner payload(s): '+', '.join(p['proposal_id'] for p in ps))
    else:
        reasoning,missing=map(prose,kept[n]);status='kept';performed.append('Confirmed that no authorized owner delta is justified after actual alternative/owner comparison; no generic future-curation deferral remains.')
    R.append({'index':n,'case_id':old['case_id'],'old_decision_sha256':canonical(old),'status':status,'work_performed':performed,'actual_searches_evidence_id':SEARCH,'reasoning':reasoning,'missing_fact_vs_authorized_work':missing,'evidence_ids':sorted(set(old['evidence_ids']+[SEARCH,BIND]+([e for p in ps for e in p['evidence_ids']]))),'proposal_ids':[p['proposal_id'] for p in ps],'independent_review':{'status':'pending','evidence_ids':[]}})
    if n in [48,141]:R[-1]['change_scope']='Shared-owner proposal binding and explicit non-transfer of the C9322 form; no catalog-specific identity change is asserted for this case.'
    if n==165:R[-1]['change_scope']='Shared-owner note explicitly records the unresolved whole-owner form boundary; source165 is not assigned the supplied powder form.'

# Per-occurrence applicability is explicit for the mixed-scope Potato and whey
# cases. Generic source labels must not turn these proposals into blanket maps.
for n in [16,23,104]:
    new=next(d for d in D if d['case_id']==A[n]['frozen_case']['case_id']);app=[]
    for o in A[n]['frozen_case'].get('occurrences',[]):
        text=json.dumps(o).lower()
        if n==23:key='nbrc355_acid_whey' if 'nbrc_355' in text or 'nbrc.medium:355' in text else 'cheese_whey_unspecified';scope='source-defined liquid output/material, not starting milk or an inferred lactose solution'
        else:key='peeled_cut_potato' if n==104 or 'peeled and cut' in text else 'potato_tuber_tissue';scope='plant-tissue preparation input only; no claim of retained solids or exact liquid extract identity'
        app.append({'occurrence_id':o['occurrence_id'],'proposal_id':'I1201-BIO-P-'+key,'scope':scope})
    new['successor_occurrence_applicability']=app

write_json(F/'biological-reassessments.json',{'reassessments':R})
write_json(F/'biological-decisions.json',{'decisions':D})
write_json(F/'biological-evidence.json',{'evidence':EV})
write_json(F/'biological-proposals.json',{'proposals':P})
write_json(CAP/'guarded-write-receipt.json',{'created_at':now,'writer':'mediaingredientmech.validation.write_validated.write_validated_ingredient','schema_sha256':sha('src/mediaingredientmech/schema/mediaingredientmech.yaml'),'payloads':[p['after_capture'] for p in P],'all_validated_before_write':True,'maintained_files_written':False,'scientific_approval':False})
print(json.dumps({'reassessments':len(R),'changed_decisions':len(D),'new_evidence':len(EV),'proposals':len(P)},indent=2))
