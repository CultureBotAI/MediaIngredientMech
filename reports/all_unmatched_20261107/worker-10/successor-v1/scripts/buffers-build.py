from pathlib import Path
import json, yaml, hashlib, copy, datetime, re
from dataclasses import asdict
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
R=Path.cwd(); B=R/'reports/all_unmatched_20261107/worker-10'; O=B/'successor-v1/buffers'; P=R/'.temp/all-unmatched-worker-10/successor-v1'; now=datetime.datetime.now(datetime.timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
dump=lambda p,x:Path(p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
inputs=json.loads((O/'reassessment-inputs.json').read_text()); cases={x['source_index']:x for x in inputs['cases']}
old={x['case_id']:x for x in json.loads((B/'decisions.json').read_text())['decisions']}
oldE={x['evidence_id']:x for x in json.loads((B/'evidence.json').read_text())['evidence']}
lookup=json.loads((O/'owner-lookup.json').read_text()); look={x['source_index']:x for x in lookup['case_lookups']}
# Each specification below is independently authored from the complete frozen recipes and cited primary captures.
specs=[]
def add(indices,slug,label,parts,text,unknown,ids=(),typ='STOCK_SOLUTION',solution='BUFFER_SOLUTION',method='LABEL_ENUMERATION',holds=()):
 specs.append(dict(indices=indices,slug=slug,label=label,parts=parts,text=text,unknown=unknown,ids=list(ids),typ=typ,solution=solution,method=method,holds=list(holds)))
add([0,62],'potassium_phosphate_0_1m_ph7_5_dsmz833_jcm753','0.1 M potassium phosphate buffer, pH 7.5 (DSMZ 833 / JCM 753)',
 [('Potassium phosphate','Salt species and their proportions are unspecified.')],
 'DSMZ 833 Solution B and JCM 753 explicitly supply a 0.1 M potassium phosphate buffer at pH 7.5, 10 mL per printed medium batch. These are source-defined stock specifications; no exact salt recipe is asserted. DSMZ 833 autoclaves Solution B under nitrogen; JCM 753 calls it an anaerobic autoclaved stock.',
 'Potassium phosphate salt species, ratio, solvent and titrant are not specified. They limit reconstruction and equivalence to other stocks, not the stated source preparation identity.',
 ['buffers-primary-8a790ec4cd07467f','buffers-primary-b45eb20b19e61138'])
add([1,56,100],'tris_hcl_0_1m_ph7_5_jcm900_979_995_dsmz600','0.1 M Tris-HCl buffer, pH 7.5 (JCM 900 / 979 / 995; DSMZ 600)',
 [('Tris-HCl','Source buffer system; no dry hydrochloride solid or addition of free HCl is inferred.')],
 'JCM 900, 979 and 995 and DSMZ 600 each specify 50 mL of 0.1 M Tris-HCl buffer at pH 7.5. This bounded record covers that explicitly printed stock specification only. JCM 900 changes the buffer to pH 8.5 for agar plates; that alternative is excluded. The shared concentration/pH/system boundary does not certify common preparation history.',
 'Solvent, titrant, reagent form and preparation ratio are not given. The pH 8.5 agar alternative needs a separate occurrence-specific choice; source-to-occurrence applicability here is limited to pH 7.5.',
 ['buffers-primary-cb3de946b9eb429a','buffers-primary-d78eaec3d48cf38b','buffers-primary-7994c01631f9607b','buffers-primary-094c5b650a091f4a'],holds=['Do not apply this pH 7.5 record to the pH 8.5 agar preparation in JCM 900.'])
add([7],'phosphate_1m_ph6_8_jcm149','1 M Na2HPO4-KH2PO4 buffer, pH 6.8 (JCM 149)',
 [('Na2HPO4','Hydration and proportion unspecified.'),('KH2PO4','Proportion unspecified.')],
 'JCM 149 Standard mineral base uses 40 mL of 1 M Na2HPO4-KH2PO4 buffer, pH 6.8. The named salts establish a mixed sodium/potassium buffer distinct from a pure phosphate salt. Other ingredients of the Standard mineral base are outside this stock.',
 'The two-salt ratio, hydration of Na2HPO4, solvent and titrant are not stated.', ['buffers-primary-9c2e840069cb8057'])
add([8],'potassium_phosphate_10mm_ph7_2_jcm1100','10 mM potassium phosphate buffer, pH 7.2 (JCM 1100)',
 [('Potassium phosphate','Salt species unspecified.')],
 'JCM 1100 uses 100 mL of 10 mM potassium phosphate buffer, pH 7.2, as the solvent stock for vitamin solution A (1000x). The vitamins belong to the receiving vitamin mixture and are not constituents of this buffer record. The 2 M KOH instruction elsewhere adjusts the medium and is not a buffer preparation instruction.',
 'Phosphate salt species, ratio, solvent identity and buffer titrant remain unspecified.', ['buffers-primary-692f41af8d398680'])
add([11,16],'potassium_phosphate_20mm_ph7_8_mmys_ii','20 mM potassium phosphate buffer, pH 7.8 (MMYS-II; JCM 194 / NBRC 372)',
 [('Potassium phosphate','Salt species unspecified.')],
 'JCM 194 and NBRC 372 define Solution II of MMYS-II as 500 mL of 20 mM potassium phosphate buffer, pH 7.8, sterilized separately. The final mixed medium pH 7.7-7.8 is not substituted for this stock specification.',
 'Exact phosphate salts, ratio, solvent and titrant are absent; concentration/pH and source use nevertheless establish the preparation boundary.', ['buffers-primary-b029597753af131b','buffers-primary-67571e41287e97f2'])
add([21],'carbonate_co2_nominal4percent_togo_m202','Nominal 4% Na2CO3-CO2 buffer (TOGO M202)',
 [('Na2CO3','Source label names this carbonate constituent; percent basis and salt hydration unspecified.'),('CO2','Source label names the carbonate/CO2 system; no gas dose or equilibration endpoint asserted.')],
 'TOGO M202 names 100 mL of 4% Na2CO3-CO2 buffer. The source-defined carbonate/CO2 preparation can be represented without inventing a CO2 saturation protocol. The final medium pH 6.7-6.8 is not assigned to the stock. Direct JCM 209 retrieval was unsuccessful; the captured TOGO recipe is the evidence used.',
 'The 4% basis, solvent, carbonate hydration and CO2 equilibration conditions are unknown. No numeric component concentration or exact equivalence to another carbonate stock is asserted.', ['buffers-primary-2b7e3ee4d3ec3dfb'])
add([24,107],'sodium_phosphate_0_5m_ph7_3_jcm296_1036','0.5 M Na2HPO4-NaH2PO4 buffer, pH 7.3 (JCM 296 / 1036)',
 [('Na2HPO4','Hydration and proportion unspecified.'),('NaH2PO4','Hydration and proportion unspecified.')],
 'JCM 296 Solution A and JCM 1036 Solution B each name 2 mL of 0.5 M Na2HPO4-NaH2PO4 buffer at pH 7.3. Their receiving vitamin/iron mixtures differ and are not merged. TOGO M1101, associated with JCM 1037, directs Solution B to the preceding medium; the JCM 1036 capture supplies that linked buffer context for case 107.',
 'Salt hydrations, ratio, solvent and titrant are not specified. The source cross-reference is needed to interpret case 107, and does not assert the two complete receiving solutions are identical.', ['buffers-primary-366c648a332e35b4','buffers-primary-3799e4c66cccca65','buffers-primary-2cd71a0cecaa19bd'])
add([48],'reducing_agent_100x_togo_m3163','100x reducing agent (Standard PETC; TOGO M3163)',
 [('NaOH','Printed 0.9 g per 100 mL preparation.'),('Cysteine-HCl','Printed 4 g per 100 mL; stereochemistry and hydration are not specified.'),('Na2S (60 weight%)','Literal source quantity is 2.17 g/L inside a per-100-mL recipe; no conversion or hydrate inference.'),('Anaerobic water','Source explicitly calls for anaerobic water; no extra water amount inferred beyond the printed batch context.')],
 'TOGO M3163 explicitly describes a 100x reducing-agent stock prepared in a nitrogen glovebox with NaOH, cysteine-HCl, Na2S (60 weight%) and anaerobic water, then autoclaved. A partial composition can be represented now. The sulfide quantity is printed as 2.17 g/L in a per-100-mL description; neither 2.17 g per batch nor another corrected amount is selected. Nitrogen atmosphere is preparation context, not a quantified material component.',
 'The sulfide quantity/batch inconsistency and supplied-form details prevent quantitative reconstruction, but not a source-qualified stock identity.', ['buffers-primary-411ee2f348a3eea9'],solution='OTHER',method='RECIPE_TRANSCRIPTION',holds=['Do not certify or normalize Na2S quantity; retain the 2.17 g/L versus per-100-mL context conflict.'])
add([49],'carbonate_paired100mm_ph10_nbrc944','100 mM NaHCO3 / 100 mM Na2CO3 buffer, pH 10 (NBRC 944)',
 [('NaHCO3','Source label prints 100 mM; ratio and mixing basis unspecified.'),('Na2CO3','Source label prints 100 mM; hydration and mixing basis unspecified.')],
 'NBRC 944 lists 1 L of a buffer labelled 100 mM NaHCO3 / 100 mM Na2CO3 at pH 10. The paired source concentrations are retained literally, without treating them as a verified 200 mM total or deriving a mixing ratio. This is not equated to the 1 M stock added in JCM 1452.',
 'Slash notation does not establish stock mixing volumes, total carbonate concentration, solvent or titrant.', ['buffers-primary-c0c62579f3d1a063'])
add([55],'penicillin_g_100000u_ml_nbrc400','Penicillin G stock, 100000 U/mL (NBRC 400)',
 [('Penicillin G','Potency concentration is stated; salt, hydration and mass concentration are not.')],
 'NBRC 400 adds 2.5 mL of Penicillin G 100000 U/mL under sterile conditions to M1D medium. The potency-labelled preparation is distinct from the dry sodium-salt owner and from the whole medium. No conversion of biological units to mass is justified.',
 'Salt, solvent, formulation excipients and preparation details are unspecified; these do not erase the explicit potency-stock boundary.', ['buffers-primary-e8abd935a388517e'],solution='OTHER')
add([60],'hepes_50mm_ph7_8_utex','50 mM HEPES buffer, pH 7.8 (UTEX vitamin stocks)',
 [('HEPES','UTEX specifies Sigma H3375, 2.4 g per 200 mL dH2O; source identifies the HEPES acid reagent.'),('Distilled water','UTEX explicitly states dH2O, 200 mL preparation basis.')],
 'UTEX vitamin B12, biotin and thiamine instructions prepare 200 mL of 50 mM HEPES buffer, adjust it to pH 7.8, and only then add the vitamin. The HEPES entry is 2.4 g/200 mL dH2O, Sigma H3375. All 68 frozen occurrences of this case were read. Vitamins and their later filtration instructions are not imported into this stand-alone buffer identity.',
 'The pH-adjusting reagent and its amount are unspecified. The source recipe supports HEPES and distilled water parts, but does not establish a complete final-species composition.', ['buffers-web-utex-b12','buffers-web-utex-biotin','buffers-web-utex-thiamine','buffers-web-hepes-supplier'],method='RECIPE_TRANSCRIPTION')
add([65,125],'concentrated_hcl_nbrc_togo_source_reagent','Concentrated HCl reagent (NBRC / TOGO source descriptions)',
 [('HCl','Qualitative concentrated reagent label; neither solvent identity nor numerical concentration is asserted.')],
 'NBRC 1116, 1195, 1196 and 1200 and TOGO M2186, M2708 and M3181 explicitly use volume-dosed concentrated HCl reagent. This record denotes the qualitative source-described acid preparation, with variable or unspecified strength, not pure gaseous HCl or a certified commercial formulation. It preserves the source reagent boundary at UNDEFINED_MIXTURE granularity. NBRC 1200 prints 51.3 mL where NBRC 1195/1196 print 51.3 microlitres; these receiving-stock quantities remain unresolved and are not used to derive acid strength.',
 'No percentage, molarity, aqueous solvent, supplier, grade, excipients or exact equivalence between source lots is established. This bounded qualitative preparation supports source association only; quantitative stock reconstruction and equivalence to a specified acid product remain unapproved.',
 ['buffers-primary-76e91583349d0f75','buffers-primary-f41f350dc810b643','buffers-primary-03edca67ae96a682','buffers-primary-ba7a82033a7b9478','buffers-final-M2186','buffers-final-M2708','buffers-final-M3181'],typ='UNDEFINED_MIXTURE',solution=None,holds=['The NBRC 1200 mL versus NBRC 1195/1196 microlitre difference remains a receiving-recipe conflict; no automatic dose repair.','Qualitative concentrated reagent identity is not a numerical-strength or common-product equivalence claim.'])
add([75],'phosphate_1m_ph7_2_pbbm_togo_m2760','Nominal 1 M phosphate buffer, pH 7.2 (PBBM; TOGO M2760)',
 [('1 M KH2PO4 solution','Source uses 10 mL of this input stock.'),('1 M Na2HPO4 solution','Source uses 10 mL of this input stock; supplied salt hydration unspecified.')],
 'TOGO M2760 PBBM defines its nominal 1 M phosphate buffer at pH 7.2 from 10 mL of 1 M KH2PO4 and 10 mL of 1 M Na2HPO4 solutions. The receiving medium adds 10 mL of the mixed stock. The input solutions remain parts, not pure-salt identity aliases. Equal input proportions resemble JCM 822 but do not prove common preparation identity or pH; no merge with the previous JCM 822 proposal is made.',
 'Input-stock solvent, salt hydration and pH adjustment details are absent. The cited primary paper full text was not obtained, but the captured primary TOGO formulation establishes the bounded preparation.', ['buffers-primary-2dca2ffb29c8ce04'],method='RECIPE_TRANSCRIPTION')
add([80],'tris_hcl_0_2m_ph7_5_dsmz273','0.2 M Tris-HCl buffer, pH 7.5 (DSMZ 273)',
 [('Tris-HCl','Source buffer system, not an assertion of dry reagent form or titrant.')],
 'DSMZ 273 adds 250 mL of 0.2 M Tris-HCl buffer at pH 7.5 to 750 mL seawater and other medium ingredients. This separately named stock differs from the 0.1 M Tris-HCl preparations; seawater and medium atmosphere are outside its component list.',
 'Solvent, titrant and exact Tris reagent form are not specified.', ['buffers-primary-f8881b46c26d0843'])
add([81],'potassium_phosphate_0_5m_ph7_jcm915_918_1430_1431','0.5 M potassium phosphate buffer, pH 7.0 (JCM 915 / 918 / 1430 / 1431)',
 [('Potassium phosphate','Source does not identify the phosphate salts or their ratio.')],
 'JCM 915, 918, 1430 and 1431 each add 1.8 mL of a 0.5 M potassium phosphate stock at pH 7.0, in sterilized anaerobic stock context. Later HCl/NaOH adjustment of the receiving medium is not a recipe for this buffer.',
 'Salt species, ratio, stock solvent and titrant remain unspecified; the explicit source stock specification is still distinguishable from the 0.25 M and 0.1 M preparations.', ['buffers-primary-f7ada6c0c960aa48','buffers-primary-b760a63b742c75a6','buffers-primary-6d72693fd96023c1','buffers-primary-e1ddc8bac4c87b3a'])
add([87],'hcl_nominal35percent_togo_m3216','Nominal 35% HCl reagent (TOGO M3216)',[('HCl','35% as printed; percentage basis and solvent are not specified.')],
 'TOGO M3216 uses 10 mL of 35% HCl in its trace-element stock. This source-specified acid reagent is distinct from dry/gaseous HCl and from nominal 25% or 32% preparations. The trace-element mixture and its water are not treated as the acid reagent recipe.',
 'Percent basis, solvent identity and supplied grade are unknown; no w/w, w/v, molarity or density is inferred.', ['buffers-primary-ded69954ea792c68'],typ='UNDEFINED_MIXTURE',solution=None)
add([94],'hcl_nominal32percent_jcm770','Nominal 32% HCl reagent (JCM 770)',[('HCl','32% as printed; percentage basis and solvent are not specified.')],
 'JCM 770 trace-element solution uses 1 mL of 32% HCl. The acid reagent has a nominal source strength and is not identical to its receiving aqueous trace-element mixture or the pure HCl owner.',
 'Percent basis, solvent and supplied grade are unknown; no w/w, w/v, density or molarity is asserted.', ['buffers-primary-b756bb7cb9a632e8'],typ='UNDEFINED_MIXTURE',solution=None)
add([101],'tpp_vfa_solution_jcm144','TPP/VFA solution (JCM 144)',
 [('0.2% thiamine pyrophosphate solution','Source input 1.5 mL; percent basis and supplied form unresolved.'),('VFA solution (JCM 144)','Source input 1 mL; same page specifies isobutyric, 2-methylbutyric, isovaleric and valeric acids, 0.5 mL each, with 0.1 N NaOH to 100 mL.'),('Distilled water','Source input 8.4 mL.')],
 'JCM 144 specifies TPP/VFA solution from 1.5 mL of 0.2% thiamine pyrophosphate, 1 mL of its VFA solution and 8.4 mL distilled water, then filter sterilization. The VFA input has its own same-page formulation; it is retained as a stock component. The inputs sum to 10.9 mL; the source does not certify a 10 mL final denominator, so none is invented.',
 'TPP stock percent basis and chemical form remain unknown. The part list is deliberately partial at preparation/speciation level, and no exact identity link to the defective existing 0.2% TPP owner is asserted.', ['buffers-primary-d282bb942d513790'],solution='COFACTOR_MIX',method='RECIPE_TRANSCRIPTION')
add([102],'hcl_nominal25percent_jcm431_899','Nominal 25% HCl reagent (JCM 431 / 899)',[('HCl','25% as printed; percentage basis and solvent unspecified.')],
 'JCM 431 and JCM 899 use nominal 25% HCl in trace-element preparation, respectively 12.5 mL and 5 mL per printed receiving stock. The common nominal acid-reagent boundary is represented without equating the two complete trace-element mixtures.',
 'Percent basis, solvent and supplied grade remain unknown. Different receiving-stock addition volumes are not evidence of different acid concentrations.', ['buffers-primary-a7277ddb9aa30cb4','buffers-primary-a95d21757d9f5e59'],typ='UNDEFINED_MIXTURE',solution=None)
add([112],'resazurin_2g_l_togo_m3155','Resazurin stock, 2 g/L (PETC-MES; TOGO M3155)',[('Resazurin','Source names resazurin without specifying acid or sodium salt.')],
 'TOGO M3155 PETC-MES adds 0.5 mL of a 2 g/L resazurin preparation per litre of medium. The mass-concentration stock is distinct from either dry resazurin acid or sodium salt; no salt choice or molarity is inferred.',
 'Resazurin supplied form, solvent, stock preparation and sterilization are not stated. These bound component resolution rather than erase the explicit 2 g/L stock.', ['buffers-primary-578bad19e849e0fe'],solution='OTHER')
add([114],'potassium_phosphate_0_25m_ph7_jcm1205','0.25 M potassium phosphate buffer, pH 7.0 (JCM 1205)',[('Potassium phosphate','Salt species and proportions unspecified.')],
 'JCM 1205 adds 5.6 mL of 0.25 M potassium phosphate at pH 7.0 from a sterilized anaerobic stock. Its declared concentration separates it from the 0.5 M and 0.1 M preparations even though the complete salt recipe is absent.',
 'Phosphate salt species, ratio, solvent and titrant are unknown.', ['buffers-primary-0bcac7f38d202632'])
add([115],'flucloxacillin_nominal100mg_ml_togo_m2927','Nominal 100 mg/mL flucloxacillin stock (KM2; TOGO M2927)',[('Flucloxacillin','Source adds 100 mg; supplied salt and hydration not given.'),('Distilled water','Source input 1 mL; not an independently certified final stock volume.')],
 'TOGO M2927 KM2 separately defines flucloxacillin stock from 100 mg flucloxacillin and 1 mL distilled water and labels it 100 mg/mL. Its 25 microlitre receiving-medium addition is not a stock mass. Preserve the nominal concentration and exact input recipe without inventing a final-volume operation.',
 'Supplied salt/hydrate, final volume after dissolution and sterilization are unspecified; no molar concentration or sodium-salt identity is asserted.', ['buffers-primary-429b78763024f2f9'],solution='OTHER',method='RECIPE_TRANSCRIPTION')
add([119],'azlocillin_nominal100mg_ml_togo_m2927','Nominal 100 mg/mL azlocillin stock (KM2; TOGO M2927)',[('Azlocillin','Source adds 100 mg; supplied salt and hydration not given.'),('Distilled water','Source input 1 mL; not an independently certified final stock volume.')],
 'TOGO M2927 KM2 separately defines azlocillin stock from 100 mg azlocillin and 1 mL distilled water and labels it 100 mg/mL. The 25 microlitre receiving addition is distinct. No final-volume operation or supplied sodium form is invented.',
 'Supplied salt/hydrate, final volume after dissolution and sterilization are unspecified.', ['buffers-primary-429b78763024f2f9'],solution='OTHER',method='RECIPE_TRANSCRIPTION')
add([123],'phosphate_nominal1m_ph7_2_jcm556','Nominal 1 M phosphate buffer, pH 7.2 (JCM 556)',[('1 M KH2PO4 solution','Source prints 28 mL of this stock.'),('1 M Na2HPO4 solution','Source prints 78 mL of this stock; supplied hydration unspecified.')],
 'JCM 556 names a 1 M phosphate buffer at pH 7.2 and directs mixing 28 mL of 1 M KH2PO4 with 78 mL of 1 M Na2HPO4 to prepare 100 mL. The 106 mL input sum conflicts with that stated final amount. A source-qualified nominal preparation with its two named stock parts can be represented while retaining the conflict; no amount is corrected and no quantitative recipe is certified.',
 'The 28+78 mL versus 100 mL conflict, input-stock solvent/hydration and pH-adjustment details remain unresolved. This prevents normalized quantities and equivalence to another formulation, not recognition of the named source preparation.', ['buffers-primary-a5a4ec5e544b62f0'],method='RECIPE_TRANSCRIPTION',holds=['Do not correct 78 to 72 mL, normalize the component concentrations, or certify the 100 mL final batch.','No merge with JCM 822 or TOGO M2760 based on phosphate family or nominal concentration.'])
add([124],'bicarbonate_basal_medium_togo_m2185','Bicarbonate basal medium, BBM (TOGO M2185)',[('NH4Cl','Printed 0.25 g per litre of basal medium.'),('NaH2PO4','Printed 0.6 g per litre; hydration unspecified.'),('KCl','Printed 0.1 g per litre.'),('NaHCO3','Printed 2.52 g per litre.'),('Vitamin solution (TOGO M2185)','Printed 10 mL input stock; same source lists its components.'),('Mineral solution (TOGO M2185)','Printed 10 mL input stock; same source lists its components.'),('Distilled water','Printed 1 L basal preparation context; no final-volume correction.')],
 'TOGO M2185 names BBM and gives the basal salts, vitamin solution, mineral solution and water. This NAMED_MEDIUM record denotes the basal medium used as an ingredient. Nitrate and varied acetate additions belong to the receiving experiment and are excluded. The Bruce et al. 1999 reference is source provenance; its full text was not obtained and is not claimed as evidence for these amounts.',
 'Some salt supplied forms, full quantitative stock reconstruction and final-volume interpretation remain unresolved. Partial source-supported decomposition is sufficient to identify this named basal preparation.', ['buffers-primary-912d33270672f032'],typ='NAMED_MEDIUM',solution=None,method='RECIPE_TRANSCRIPTION')
add([126],'artificial_seawater_spelling','Artificial seawater',[],
 'DSMZ 601 and NBRC 1183 describe artificial sea water prepared from marine aquarium salt mixtures without identifying a particular product. MicrO MICRO:0001715 defines the generic inorganic salts solution that mimics sea water, not one fixed formula. The spacing variant Artificial sea water therefore belongs to the existing generic Artificial seawater owner; no product-specific identity is selected.',
 'Specific aquarium product, batch formula and strength remain unknown; they are not prerequisites for this spelling-only association to the existing explicitly generic ontology sense.', ['buffers-primary-6490b59a55812105','buffers-primary-5939a819cce95c5d'],holds=['Inherited navigation aliases Artificial seawater (see below) and Artificial seawater (see Medium No. 736 ) are outside this bounded alias approval and require source-specific review before complete-owner publication.'])
add([130],'carbonate_1m_ph10_jcm1452','1 M NaHCO3 / Na2CO3 buffer, pH 10.0 (JCM 1452)',[('NaHCO3','Ratio unspecified.'),('Na2CO3','Ratio and hydration unspecified.')],
 'JCM 1452 uses 100 mL of a 1 M NaHCO3/Na2CO3 buffer at pH 10.0 with 900 mL water and states final 100 mM. The 1 M input stock has a distinct concentration boundary from the receiving diluted medium and from NBRC 944 paired-100-mM buffer.',
 'Mixing ratio, salt hydration, stock solvent and titrant remain unspecified.', ['buffers-primary-947e5eff24deb387'])
add([135],'hepes_2m_ph7_jcm556_1200','2 M HEPES buffer, pH 7.0 (JCM 556 / 1200)',[('HEPES','Source does not specify supplied acid or salt form or pH-adjusting reagent.')],
 'JCM 556 and JCM 1200 use 5 mL of 2 M HEPES buffer at pH 7.0 in sterilized stock context. The preparation is not the dry HEPES acid owner and is distinct from the UTEX 50 mM pH 7.8 stock.',
 'HEPES supplied form, solvent, titrant and titrant amount remain unspecified; no pure-form alias or full composition claim follows.', ['buffers-primary-a5a4ec5e544b62f0','buffers-primary-44445462ffa7bfa8'])
assert sorted(i for s in specs for i in s['indices'])==sorted(cases)
(O/'proposed_owners').mkdir(exist_ok=True)
records={str(p.relative_to(R)):yaml.safe_load(p.read_text()) for p in (R/'data/ingredients').rglob('*.yaml')}
assert len(records)==lookup['maintained_record_files_examined']
previous_props=json.loads((B/'proposals.json').read_text())['proposals']
existing_ids={r['identifier'] for r in records.values()}
E=[];decisions=[];proposals=[];newrecords={};collision=[]
def ev(eid,path,kind,locator,support,ids,url=None,accessed=None):
 d={'evidence_id':eid,'capture':{'root':'artifact','path':str(path.relative_to(B)),'sha256':sha(path)},'kind':kind,'locator':locator,'supports_or_contradicts':support,'url':url,'case_ids':ids}
 if accessed:d['accessed_at']=accessed
 E.append(d);return eid
allids=[cases[i]['case_id'] for i in sorted(cases)]
ev('sv1-buffers-owner-lookup',O/'owner-lookup.json','local_owner','case_lookups[*], including exact hits and family candidates','Ignored-inclusive inventory and actual owner hashes; lexical candidate names are not substance equivalence.',allids)
ev('sv1-buffers-context-review',O/'reassessment-inputs.json','source_snapshot','cases[*].full_snapshot_reads and primary_reads','Hash-verified full frozen occurrence reads and original captured primary source read bindings; no new retrieval timestamp is invented.',allids)
meta=json.loads((O/'captures/micro-reuse-provenance.json').read_text())
ev('sv1-buffers-micro1715',O/'captures/micro-73963269.owl','ontology','owl:Class http://purl.obolibrary.org/obo/MICRO_0001715','Definition is generic inorganic salts solution mimicking sea water; no fixed formulation or supplier qualifier.',[cases[126]['case_id']],meta['original_source_metadata']['url'],meta['original_source_metadata']['retrieved_at'])
ev('sv1-buffers-micro-reuse',O/'captures/micro-reuse-provenance.json','source_snapshot','original_source_metadata and fresh_http_retrieval=false','Exact historical primary ontology bytes reused with original timestamp; this is not a fresh HTTP capture.',[cases[126]['case_id']])
for n in (1,2,3):
 ev(f'sv1-buffers-search-{n}',O/f'captures/search-{n}.json','unsuccessful_search','queries and actual returned web results','Additional searches inform uncertainty only; no composition claim relies on secondary search snippets.',allids)
for s in specs:
 cis=[cases[i]['case_id'] for i in s['indices']];is_edit=s['indices']==[126]
 target='data/ingredients/mapped/Artificial_seawater.yaml' if is_edit else f"data/ingredients/mapped/{s['slug']}.yaml"
 identifier=records[target]['identifier'] if is_edit else 'kgmicrobe.ingredient:'+s['slug']
 proposed=O/'proposed_owners'/Path(target).name
 before=sha(R/target) if is_edit else None
 assert not any(x['owner_path']==target for x in previous_props),target
 if not is_edit:
  assert target not in records and identifier not in existing_ids,target
 collision.append({'owner_path':target,'identifier':identifier,'before_sha256':before,'maintained_path_exists':is_edit,'maintained_identifier_exists':is_edit,'prior_36_proposal_owner_overlap':False})
 evid=sorted(set(['sv1-buffers-owner-lookup','sv1-buffers-context-review']+s['ids']+[eid for i in s['indices'] for eid in old[cases[i]['case_id']]['evidence_ids']]))
 for eid in evid:
  assert eid in oldE or eid.startswith('sv1-'),eid
 sources=list(dict.fromkeys(oldE[eid]['url'] for eid in s['ids'] if oldE[eid].get('url')))
 provenance=' '.join(f"Provenance-only source text {old[cases[i]['case_id']]['source']['raw_source_label']!r} (case {cases[i]['case_id']})." for i in s['indices'])
 bounds=' Generic source-local labels are not added as globally resolving synonyms. No exact formulation link to a receiving CultureMech medium is asserted. Source-snapshot receiving amounts and embedded holds are preserved; stock-to-medium unit repair is separate from preparation identity.'
 if is_edit:
  r=copy.deepcopy(records[target]); r.setdefault('synonyms',[]).append({'synonym_text':'Artificial sea water','synonym_type':'RAW_TEXT','source':'; '.join(sources)})
  r['ontology_mapping'].setdefault('evidence',[]).append({'evidence_type':'MANUAL_CURATION','source':meta['original_source_metadata']['url'],'notes':s['text']+' Bounded spelling association only; no new endorsement of inherited navigation aliases.'})
  r['notes']=(r.get('notes','')+' '+s['text']+' '+s['unknown']+' '+provenance+' Inherited navigation aliases are not newly validated by this proposal.').strip()
  evid+=['sv1-buffers-micro1715','sv1-buffers-micro-reuse']
  record_curation_event(r,curator='all_unmatched_worker10_successor_buffers',action='ADDED_SYNONYMS',changes='Added source-verified spacing variant Artificial sea water to existing generic MICRO:0001715 owner; no supplier/formula selection or inherited-alias approval.',llm_assisted=True,timestamp=now)
 else:
  r={'identifier':identifier,'preferred_term':s['label'],'mapping_status':'MAPPED','ingredient_type':s['typ']}
  if s['solution']:r['solution_type']=s['solution']
  r['ontology_mapping']={'ontology_id':identifier,'ontology_label':s['label'],'ontology_source':'kgmicrobe.ingredient','mapping_quality':'FALLBACK_REGISTRY','evidence':[{'evidence_type':'MANUAL_CURATION','source':u,'notes':'Source-described preparation boundary retained under MAPPING_SEMANTICS section 3. No exact chemical or complete-formula equivalence is asserted. '+s['text']} for u in sources]}
  components=[]
  for name,source in s['parts']:
   c={'component_name':name,'reference_scope':'UNMAPPED','source':source}
   if name=='Distilled water':c.update(reference_scope='MIM_CATALOG',component_id='CHEBI:15377')
   if s['indices']==[60] and name=='HEPES':c.update(reference_scope='MIM_CATALOG',component_id='CHEBI:42334')
   components.append(c)
  if components:
   r['components']=components;r['component_assertion']={'method':s['method'],'completeness':'PARTIAL','evidence':[{'evidence_type':'RECIPE_SOURCE','source':u,'source_record':s['label'],'notes':s['text']} for u in sources if 'sigmaaldrich' not in u], 'notes':s['unknown']+' Source-named parts remain UNMAPPED where supplied form or stock identity is not established. MIM_CATALOG references identify only the supported constituent, not approval of that complete owner.'}
  r['notes']=s['text']+' '+s['unknown']+' '+provenance+bounds
  record_curation_event(r,curator='all_unmatched_worker10_successor_buffers',action='CREATED',changes='Created isolated source-qualified preparation proposal with partial source-proven components. Explicit unknowns and receiving-recipe conflicts are retained; no complete-formula, inherited-owner, role or publication approval.',new_status='MAPPED',llm_assisted=True,timestamp=now)
 write_validated_ingredient(r,proposed)
 newrecords[target]=r
 pid='sv1-buffers-'+s['slug']
 proposal={'proposal_id':pid,'case_ids':cis,'description':('Add the bounded spelling alias to the existing generic owner.' if is_edit else 'Create a source-qualified preparation identity with partial source-supported components.')+' '+s['text'],'evidence_ids':sorted(set(evid)),'owner_path':target,'kind':'edit_existing_owner' if is_edit else 'new_owner','after_capture':{'root':'artifact','path':str(proposed.relative_to(B)),'sha256':sha(proposed)},'before_sha256':before,'identity_predicate_consequences':('Existing MICRO:0001715 identifier and exact mapping retained. No formulation-specific exact equivalence asserted.' if is_edit else 'Local kgmicrobe.ingredient preparation identity with FALLBACK_REGISTRY mapping to its own identifier. No whole-to-constituent mapping, CAS, or exact external ontology equivalence. Registry exactMatch row would identify only this source-qualified preparation.'),'publication_review_obligations':'Proposal only. Full content-bound publication review, integration conflict checks, maintained-surface synchronization and native export QC remain required after acceptance. No roles or complete owner approval.','cross_shard_conflicts':'No overlap with the original 36 owner paths. New preparations must be compared against concurrent proposals before integration; similar names alone do not establish same formulation.','publication_holds':s['holds']+[s['unknown'],'Do not infer a complete formula from PARTIAL components or convert receiving-medium stock additions into mass concentrations.'],'independent_review':{'status':'pending','evidence_ids':[]}}
 proposals.append(proposal)
 for i in s['indices']:
  c=cases[i];d=copy.deepcopy(old[c['case_id']]); assert canon(d)==c['old_decision_sha256']
  d.update(disposition='alias_to_existing_owner' if is_edit else 'new_distinct_ingredient_proposal',reasoning=s['text']+' '+s['unknown'],applicability=f"All {len(c['full_snapshot_reads'])} full frozen occurrence snapshots and linked captured primary contexts were independently reread for case {i}. "+s['text']+' This association is source-bound; raw generic labels remain nonresolving provenance unless explicitly the spelling-only seawater alias.',evidence_ids=sorted(set(evid)),proposal_ids=[pid],no_change_reason=None,missing_requirement=None,independent_review={'status':'pending','evidence_ids':[]},reviewer='/root/buffers_research')
  d['owner_records']=[{'path':target,'sha256':before,'identifier':identifier}] if is_edit else []
  d['completion_reassessment']={'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1201','source_index':i,'prior_published_head':inputs['published_head'],'prior_decision_sha256':c['old_decision_sha256'],'prior_disposition':old[c['case_id']]['disposition'],'prior_missing_requirement':old[c['case_id']].get('missing_requirement'),'classification':'supported_identity_curation_completed_as_isolated_proposal','missing_fact_vs_deferred_work':s['unknown']+' These are explicit representation limits, not prerequisites for the proposed bounded identity.','owner_lookup_evidence':'sv1-buffers-owner-lookup','full_context_evidence':'sv1-buffers-context-review','actual_lookup':look[i],'preserved_frozen_occurrence_ids':[x['occurrence_id'] for x in c['full_snapshot_reads']],'embedded_holds_preserved':True,'quantitative_or_publication_holds':proposal['publication_holds'],'source_association_only':not is_edit,'no_new_http_capture_claim':True}
  decisions.append(d)
# Validate candidate corpus without touching either maintained surface.
base=list(records.values());candidate=[newrecords.get(p,r) for p,r in records.items()]+[r for p,r in newrecords.items() if p not in records]
base_v=validate_component_partonomy(base);cand_v=validate_component_partonomy(candidate);old_v={str(v) for v in base_v};delta=[v for v in cand_v if str(v) not in old_v]
assert not delta,[str(v) for v in delta]
dump(O/'decisions.json',{'schema_version':1,'worker_slot':10,'shard_sha256':'9767ffc8100e3cd8cd0c4101cc8e9ebe8d8fda8aaab4c42ba4e11b8c3c5693cc','phase':'successor-v1','decisions':sorted(decisions,key=lambda d:d['completion_reassessment']['source_index'])})
dump(O/'proposals.json',{'schema_version':1,'proposals':proposals})
dump(O/'evidence.json',{'schema_version':1,'evidence':E})
dump(O/'proposal-identity-lookup.json',{'checked_at':now,'ignored_files_included':True,'method':'Full pathlib.rglob maintained record identity/path inventory, combined with recorded label/synonym family lookup and original 36 isolated proposal paths.','maintained_records':len(records),'proposals':collision})
dump(O/'guarded-validation.json',{'checked_at':now,'guarded_writer':'mediaingredientmech.validation.write_validated.write_validated_ingredient','curation_event_helper':'mediaingredientmech.curate.curation_event.record_curation_event','payloads':[p['after_capture'] for p in proposals],'guarded_schema_writes_passed':len(proposals),'partonomy_baseline_violations':[asdict(v) for v in base_v],'partonomy_candidate_violations':[asdict(v) for v in cand_v],'partonomy_new_violations':[asdict(v) for v in delta],'maintained_files_written':False})
print(json.dumps({'decisions':len(decisions),'proposals':len(proposals),'new_evidence':len(E),'new_partonomy_violations':len(delta)}))
