"""Package the materials agent's independent scientific assessments; no input writes."""
import json, hashlib, pathlib, datetime, yaml

T = pathlib.Path('.temp/w04-authoritative-successor-science-v1')
R = T / 'reviews/biological'
S = json.loads((T/'scopes/biological.json').read_text())
I = json.loads((R/'input-checks.json').read_text())
E = {x['evidence_id']:x for x in I['captures']}
reviewer = 'Codex /root/materials, independent W04 biological reviewer'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
sha = lambda b: hashlib.sha256(b).hexdigest()
canon = lambda x: json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()

# These are scientific judgments written after reading the complete selected payloads,
# their before records, original captures and full frozen recipe contexts.
# Numeric keys are zero-based biological-scope indices, never shard indices.
PN = {
0: ('The two added labels explicitly retain filtration of natural seawater. MICRO:0001773 defines an undefined inorganic mixture derived by filtering natural seawater; CCAP input instructions and JCM1102 support these aliases.', 'The inherited resolving RAW_TEXT Natural seawater omits filtration and is not supported as an exact alias by these sources. The 95%-strength RELATED_SYNONYM must remain non-exact. Environmental ENVO00002149 is contextual ocean water, not an identity substitution. Historical 7/7 occurrence counts are not recomputed here.'),
1: ('JCM492 Modified MJ stock has twelve top-level entries, including 30g NaCl, 0.5g each CaCl2 dihydrate/NH4Cl, 10ml trace minerals and 1L added water. Every selected component name, hydrate, amount and batch unit agrees with the primary table. The receiving medium uses 1L stock and adds other solutions separately.', 'Keep trace minerals as the source-named nested stock; no exact constituent ontology identity or final-volume concentration is inferred. The component assertion is complete only at the disclosed top level; no atmosphere is a component.'),
2: ('DSMZ611 seawater mix has sixteen top-level entries; 47.15g NaCl,18.10g MgCl2 hexahydrate,3.13g CaCl2 dihydrate and all minor mg/ug quantities match page1. Its1000ml water and125ml receiving dose have separate meanings.', 'The main-medium final1012ml header does not establish the stock final volume. Unspecified sodium-silicate chemistry remains unresolved. Do not equate this concentrated stock with natural seawater or use a receiving-medium atmosphere as partonomy.'),
3: ('JCM512 DL minerals is a fifteen-entry refrigerated sulfate-bearing nitrilotriacetate stock. The source names trisodium NTA, MgSO4 heptahydrate and MnSO4 xH2O; selected quantities/forms match without guessing x. Existing Sulfur-free_DL_Minerals instead uses chloride salts and disodium NTA.', 'No exact merge with the sulfur-free owner or stereochemical interpretation of DL. Retain source-named components without inferred hydration, and keep10ml stock dose separate from1L added water in the stock.'),
4: ('DSMZ946a page2 defines eleven stock entries. All selected amounts match, including55.40g NaCl,14g MgSO4 heptahydrate,11g MgCl2 hexahydrate,0.10mg KI and1000ml added distilled water. The main medium receives500ml stock.', 'Selected YAML correctly uses source-batch units. Decision49 overstates this as55.4g/L and needs the bounded wording correction W04-BIO-SR-01. Neither the2x name nor1L added water proves a measured final stock volume.'),
5: ('JCM651 explicitly supplies15g NaCl,0.35g KCl,5.4g MgCl2 hexahydrate,2.7g MgSO4 heptahydrate,0.5g CaCl2 dihydrate and1L water for its0.5x artificial seawater. The six selected entries agree.', 'The0.5x state belongs to this formulation, not every artificial seawater. Keep all component amounts as preparation-batch quantities and the source liquid dose separate.'),
6: ('JCM910 explicitly replaces JCM6510.5x artificial seawater with1.0x. The selected salt masses are exactly doubled at the same1L water basis; the assertion method CURATED_INTERPRETATION and second evidence note correctly identify that calculation.', 'The first evidence note saying all components were transcribed is imprecise beside the explicit calculation. Read this as a disclosed curator derivation, not a verbatim JCM910 table; W04-BIO-OBS-01 recommends clarifying that note. No proof of measured final volume or generic1x-stock equivalence.'),
7: ('DSMZ1009 defines artificial seawater using32g sea salt, for example Instant Ocean, in1000ml distilled water. Both selected components and the preparation-qualified label preserve this recipe; the frozen receiving quantities already retain volume units.', 'COMPLETE covers sea-salt preparation plus water, not the molecular composition of the sea-salt product. Instant Ocean is an example rather than a compulsory identified lot. No equivalence to natural seawater.'),
8: ('JCM1269 supplies a four-fold stock with twelve top-level entries:80g NaCl,12g MgCl2 hexahydrate,24g MgSO4 heptahydrate,4g ammonium sulfate,3.2g NaHCO3,1.2g CaCl2 dihydrate,2g KCl,1.68g K2HPO4,0.2g NaBr,0.08g SrCl2 hexahydrate,0.04g ferric ammonium citrate and1000ml water. The selected transcription agrees.', 'Ferric ammonium citrate remains UNMAPPED source text. This review neither adjudicates its composition nor approves any W09 FAC proposal/coalescence.200ml receiving-stock dose is distinct from stock strength and added-water basis.'),
9: ('DSMZ781 defines an aqueous horse-dung filtrate: boil an average-sized fresh or frozen piece in150ml water in a water bath for2h, filter and use immediately. The medium uses100ml filtrate with900ml water. The new local owner accurately preserves this output.', 'Unknown starting dung mass and extraction yield do not prevent this protocol-qualified material. They do prevent a quantitative retained-composition assertion. No horse-to-cow transfer; the frozen separate-sterilization note is not present in the primary and is not adopted.'),
10: ('The existing colloidal-chitin owner receives only a DSMZ1681 protocol annotation. The primary describes crab/shrimp shell flakes, HCl treatment, cold-water precipitation, centrifugation and washing to pH6-6.5;5g colloidal chitin or commercial powder is allowed.', 'CHEBI17029 denotes a chitin polymer, not a unique prepared suspension, purity or acetylation distribution. Keep UNMAPPED0361 and do not universalize this protocol or collapse the commercial-powder alternative. Historical research prose is provenance only.'),
11: ('DSMZ1752 explicitly names Biomaris Seawater as the liquid base. The source-qualified product material can be represented while lot, salinity, treatment and mineral composition are unknown.', 'The alternative multi-salt replacement is not the bottled-product formulation. No new global alias or natural-seawater exact mapping. Unknown product composition limits stronger claims, not this bounded material identity.'),
12: ('The recipe family uses potato tuber tissue before boiling, sieving or filtering. The selected local material represents that input, with peeled/cut occurrences separately qualified. FOODON03315354 names a Solanum tuberosum tuber and00002796 a whole/piece derivative; neither is installed as an exact claim that erases preparation.', 'Do not equate the input mass with retained filtrate solids or adopt MediaDive CAS93348-51-7. No common extraction yield, cultivar, universally peeled state or final-medium concentration is established. More-specific peeled/cut occurrences require their separate scope.'),
13: ('JCM30/54/55/116 explicitly say peeled and cut; NBRC recipes with peeling/cutting instructions corroborate the tissue preparation. JCM30 boils200g in1L for20min then sieves;54/55 combine potato and carrot then filter. Those outputs are not the owner.', 'Restrict this preparation to occurrences whose primary explicitly discloses both peeling and cutting. The broad citation list includes other potato contexts and is not proof they are all peeled/cut. Cut alone does not define dice size or identify the existing Diced Potato material exactly.'),
14: ('TOGOM2231 describes bubbling cultures with5% CO2-containing sterile air. A source-qualified sterile-air carrier input is representable; selected notes distinguish the carrier, enriched gas and aeration operation.', 'No N2/O2 percentages, sterilization method, gas flow or unspecified5% basis is inferred. This is a gas input, not a liquid medium component amount or evidence for a nutrient role.'),
15: ('NBRC355 explicitly acidifies warmed milk with HCl to coagulate it, centrifuges and uses the supernatant as cheese whey. The local output is separated from the generic cheese-whey material and tied only to the NBRC355 occurrence.', 'Milk species, acid dose, temperature, centrifugation and yield are absent. No has-part assertion that starting milk/HCl or removed precipitate is quantitatively retained. Other cheese-whey occurrences cannot inherit this preparation.'),
16: ('DSMZ775/JCM162 identify cheese whey as a liquid input without an acid or rennet production protocol. The broad source-stated cheese-whey class correctly covers the six non-NBRC355 occurrences without a fabricated formula.', 'Primary1L/1000ml amounts do not support frozen mass or1000%-volume readings. No equivalence between all batches, purified lactose, whole milk or the specifically acid-precipitated NBRC355 output is claimed.'),
17: ('NBRC985 explicitly names sterilized natural seawater in the Porphyra cultivation context. The treatment-qualified local material retains that disclosed boundary.', 'The source does not disclose sterilization method or receiving amount. Do not assume pasteurization, autoclaving, untreated water, synthetic salts or whole-culture identity; missing parameters limit reproducibility, not the stated prepared-material class.'),
18: ('NBRC15/TOGOM1418 explicitly direct stirring about300ml V8 with3g CaCO3 for2h then centrifuging.200ml of the supernatant is used with800ml2%-salinity seawater and15g agar. The selected owner denotes this processed supernatant.', 'No transfer of starting CaCO3 or complete V8 constituents into retained output partonomy. Yield and residual calcium are unknown. pH7 is the receiving medium pH, not the stock pH. Whole V8 product owners are distinct.'),
19: ('NBRC16/17/24/1114 and TOGO counterparts repeatedly identify cornmeal extract, typically2g per recipe. The new material preserves the disclosed extract boundary without merging raw cornmeal or complete Corn Meal Agar.', 'No solvent, manufacturer, physical supply state, extraction yield or fixed composition is supplied. These are genuine limits on stronger product/formulation claims, not a reason to leave the named extract unrepresented.'),
20: ('Supplier COA C9322-1G batch0000495897/source batch0000402808 identifies bovine-liver catalase, lyophilized powder and2000-5000units/mg protein. TOGOM2399/M2402/M2404 explicitly bind C-9322. The retained CAS9001-05-2/MeSHD002374 species-neutral parent pattern is compatible; NCITC61062 expressly denotes human CAT and is excluded.', '3190units/mg and86%protein are lot results only. Uncatalogued beef and generic catalase are not identified with C9322 or assigned its activity. Existing Properties entries are non-names already excluded by the pinned synonym policy, not active alias leaks. C--10 is a separate resolving catalog spelling unverified by the C9322 COA, and three mapping/export holds persist. Historical counts are not newly approved.'),
21: ('JCM730 defines2g malted wheat meal as an input alongside40g rye bran,0.8g trypsin and1L water,50C24h then500xg15min and filtration. The new local material is the malted-wheat input, not the resulting extract or purified carbohydrate.', 'FOODON03306061 adds medium/coarse grinding and unheated processing; neither is stated. FOODON03460755 explicitly requires Triticum aestivum, not independently established here. Neither term is forced as exact or parent mapping. CHEBI1881/MediaDive1881 numeric coincidence remains rejected.'),
22: ('M3127 identifies1L MJ synthetic seawater base and separately describes MMJ/MMJS modifications. Author papers establish MJ lineage and show a2012 MJ formula, but version identity to this preparation is unproved. An opaque source-qualified stock preserves the actual named input.', 'No later MJ formula, Modified MJ492 recipe, MMJ additions or culture gas becomes a constituent by inference. The unresolved exact base recipe/version is a genuine limitation on decomposition, not a blocker to the bounded stock record.'),
23: ('TOGOM2313 names xylan from oat spelts among alternative carbon substrates in minimal medium. The selected source-material preparation retains the botanical-source qualifier.', 'Do not assign generic xylan CAS9014-63-5 or a purified molecular identity from the name. The source0.2% does not establish an unreported percent basis; listed carbon alternatives are not simultaneous constituents of this material.'),
24: ('NBRC1130/TOGO source labels disclose seawater at stated3% salinity. The material is retained as a salinity-qualified source class without asserting natural origin or a salt recipe.', 'Three-percent salinity is not three-percent NaCl and does not establish w/v or a fixed ionic composition. No artificial/natural equivalence or exact cross-recipe stock identity is granted.'),
25: ('JCM52 and NBRC304 explicitly name3g powdered Quaker White Oats. Adding this source-supplied form to Oatmeal records actual preparation evidence without inventing catalog or colloidal processing.', 'NCITC29298 explicitly defines fine colloidal whole-oat powder; generic MediaDive471/DSMZ425 oatmeal and an ordinary powder label do not prove that identity. The unchanged exact mapping and kg_microbe_node_id remain scientifically held. Historical18-count membership is not settled by newer23 rows; no mapping release or whole-owner reidentification.'),
26: ('NBRC1429 supplies seawater at stated1.75% salinity. The selected local material preserves this parameter and source context.', 'No NaCl percentage conversion, salt inventory, natural/synthetic origin, measured density or equivalent-stock claim is justified. Amounts used in the recipe remain separate from salinity.'),
27: ('JCM1216 BSW3 Agar explicitly lists1000ml artificial seawater0.1x, without a1x formula or product identifier. An opaque source-qualified diluted stock is supported.', 'Do not import a1x base from unrelated JCM651/910/1269 stocks. The unprovided reference formula prevents component decomposition but not representation of the source-named dilution state.'),
28: ('NBRC14 names a corn and fish meal mixture used as bird feed;20g is boiled for1h in about1L water, filtered and made back to1L. Selected qualitative corn/fish-meal components describe the feed input.', 'PARTIAL RECIPE_TRANSCRIPTION is appropriate: no ingredient proportions or assertion that these are the only feed ingredients. The boiled filtrate is not the input feed, and20g is not retained extract composition.'),
29: ('DSMZ1008 requires800ml charcoal-filtered natural seawater with200ml distilled water. The separate charcoal-treatment boundary is supported and the rejected Distilled Water alias remains rejected.', 'Biomaris is a permitted replacement, not proof of equivalent composition. No charcoal-bed/contact parameters or complete ionic composition is invented. Frozen mass/percent unit substitutions must not change the source800ml dose.'),
30: ('NBRC1347/JCM995 explicitly identify aged seawater, supporting a treatment-qualified material. Receiving doses and medium preparation stay contextual.', 'No universal aging duration, light exposure, filtration or storage regime may be transferred from the different Hutner protocols in JCM149/900. The class can be retained with its process parameters unknown.'),
31: ('NBRC22/1071 disclose seawater at stated2% salinity, supporting a bounded material class for those occurrences.', 'Two-percent salinity does not disclose exact salt composition or percent basis. This owner is not an exact resolution of the NBRC13 natural-or-artificial disjunction, nor a warrant to merge all2%-salinity products.'),
32: ('TOGOM2843 says potato extract from200g boiled potato per litre. The existing UNMAPPED0251 owner receives a source-bounded note/supplied-form entry, preserving the different historical4g/L infusion context without asserting equivalence.', 'Starting tissue mass is not retained extract solids. No CAS93348-51-7, generic whole-tissue alias or mapped-owner promotion. Historical supply state, extraction duration/yield and exact relation between preparations remain unresolved; the note does not settle them.'),
33: ('NBRC984 explicitly identifies Porphyra yezoensis thalli cultivated in IMK medium with seawater. The selected source-qualified biomass retains cultivation context.', 'No dry clean-biomass state, taxon-only chemical identity, purified polymer, retained growth-medium composition or whole-culture synonym is inferred. Amount and separation/washing method remain unspecified.'),
34: ('MediaDive1624/JCM99 identify larchwood xylan, with Sigma attribute. The existing botanical-preparation owner can be promoted to its local registry identity without requiring fixed polymer purity.', 'CHEBI37166 defines generic xylose polysaccharides; exact equivalence to the entire source preparation is unproved. No CAS9014-63-5 transfer from automatic provider annotations. Preserve#294 provenance correction and historical research as history, not support; Sigma is not a catalog/lot.'),
35: ('MediaDive728/DSMZ789 specify diced potato20g; boil in1L water for30min, filter and restore1L. Promotion of the existing diced-tissue owner preserves physical-form identity, not the output filtrate.', 'The historical research quotation200g/L is expressly not adopted. No universal concentration, dice dimension, cultivar or extraction yield is asserted. The raw source input cannot be equated with potato extract.'),
36: ('MediaDive481/DSMZ440 specify bovine horn meal10g. A processed bovine-horn meal material is supported even without lot composition or exact particle size.', 'FOODON00002939 is horn AND hoof meal, not an exact term for the horn-only source. No purified keratin, fixed protein fraction, drying temperature or equivalence to separately supplied skim milk is inferred. Historical research is not independent evidence.'),
}

CN = {
0:'DSMZ1752 names the branded liquid; its salt replacement remains an alternative, not a manufacturer formulation.',
1:'All seven frozen occurrences retain the filtered-natural input boundary. CCAP MErds/NSS-low fill to1L; MY75S/ZM10 dilute the input. Synthetic alternatives in NSS-low/2SNA remain alternatives. Finished-medium autoclaving is not a supplied-form claim.',
2:'All potato occurrences were compared across complete preparations: peeled/cubed NBRC1/3/4/856/1115/1232; sliced NBRC201/202; peeled/sliced NBRC2; JCM333 cubes; washed/sliced DSM129; peeled/sliced DSM411; TOGOM2308 cut potato. Generic tissue and explicitly peeled/cut scopes are separate; extracted filtrates are not200g/L retained potato.',
3:'TOGOM2231 aeration wording identifies a sterile-air carrier with5%CO2 context. The source row is not a liquid dose, pure CO2 or merely an operation with no material input.',
4:'NBRC13 footnote explicitly permits natural OR artificial seawater diluted with distilled water to2% salinity. This is a genuine unresolved choice, not a failed material lookup. Existing filtered/artificial seawater and bounded2%-class owners cannot each denote the entire disjunction. Preserve both branches; branch selection or a typed alternative group is required for exact source association.',
5:'Seven occurrences are intentionally split: NBRC355 identifies HCl-coagulated/centrifuged milk supernatant; the other six DSMZ775/JCM162/TOGO contexts name generic liquid cheese whey. Primary litres/ml override neither frozen bytes nor correctable source-unit defects; no acid process is silently transferred.',
6:'NBRC985 names sterilized natural seawater with Porphyra thalli but gives no receiving dose/method. Preserve the treated-water input, not the complete culture.',
7:'Both NBRC15 and TOGOM1418 identify the centrifuged CaCO3-treated V8 supernatant. The proposed preparation resolves the actual input; whole V8 and receiving agar remain distinct.',
8:'NBRC16/17/24/1114 and TOGO duplicates retain the same cornmeal-extract input while the receiving water/seawater/agar differs. Unknown production details do not justify deferring the material class.',
9:'NBRC335 footnote resolves ** as filtered aged seawater OR Daigo artificial seawater SP (Wako). No selected branch is disclosed. Existing FilteredSeawater, ArtificialSeawater and aged-seawater proposals are branch-level candidates, not exact synonyms for this alternative group; retain the named product and both process qualifiers.',
10:'JCM492 identifies a distinct Modified MJ stock, not generic MJ or ocean water. Primary1L receiving stock dose conflicts with frozen1G_PER_L; the twelve-entry proposal preserves the complete top-level table. Decision per-litre shorthand needs correction under W04-BIO-SR-01.',
11:'DSMZ611 identifies a concentrated sixteen-entry seawater mix dosed125ml; frozen125G_PER_L is a unit substitution. Its main-medium final1012ml is separate from the stock1000ml water. Decision per-litre wording needs correction under W04-BIO-SR-01.',
12:'The exact C-9322 spelling is present in three TOGO OADC recipes. Supplier batch evidence supports bovine-liver lyophilized catalase, not human CAT, catalogC--10 or a universal3190units/mg activity.',
13:'JCM51210ml DL minerals is a stock-dose context; the full sulfate-bearing recipe is not the sulfur-free chloride stock found in the existing catalog. Frozen10G_PER_L is not a mineral concentration.',
14:'All three CultureMech occurrences point to JCM730 rye-bran extract preparation. Malted wheat meal is the2g starting material and retains the meal/malt distinction; no coarse-ground/unheated or species-specific ontology qualifier is established.',
15:'DSMZ1054 explicitly permits Biomaris0890.75 bottle, natural or artificial seawater. These are mutually allowed source choices rather than one recipe formula. The DSMZ1752 Biomaris owner is only a possible branch, not proof of the same product version; no single-owner resolution can be supported without a branch or alternative representation.',
16:'Uncatalogued beef catalase appears in OADC/ADC source formulations, including DSMZ645 and TOGOM2328/M2397/M2403.4mg/3mg source input amounts do not identify C9322 or establish stock final-volume concentrations; evidence supports bovine reagent scope only.',
17:'DSMZ946a500ml two-fold stock dose and eleven-entry stock formula are well supported. Only the active reasoning55.4g/L contradicts the bounded batch basis used by the proposal; W04-BIO-SR-01 requires wording correction.',
18:'M3127 is a named MJ base with separate MMJ/MMJS modifications.2012 and2005 author papers support lineage but do not prove the exact source version. The opaque stock proposal is useful bounded curation, not a declaration that lookup is complete for component identity.',
19:'TOGOM2313 presents oat-spelt xylan as one alternative carbon source. Preserve the source-specific preparation; do not combine all substrate alternatives, invent w/v for0.2%, or equate with larchwood xylan.',
20:'JCM1102 names filtrated natural seawater and contains the relevant receiving recipe context. This supports the second exact filtration-preserving alias, while the existing unqualified Natural seawater alias still needs separate curation.',
21:'NBRC1130/TOGO disclose3% salinity without a defined salt recipe. Bounded salinity-qualified material is supported; frozen normalization must not be read as a3%NaCl formulation.',
22:'JCM52 explicitly names powdered Quaker White Oats3g. This proves source physical form, not NCIT fine colloidal manufacturing or a universal oat-meal mapping.',
23:'DSMZ781 explicitly supplies horse-dung extract protocol and100ml dose. The source method justifies the preparation-qualified owner despite unknown starting mass/yield; no manure-tissue identity or frozen sterilization embellishment is adopted.',
24:'NBRC1429 reports1.75% salinity. Keep source salinity and receiving amount separate; do not invent percent basis, composition or natural/synthetic origin.',
25:'JCM910 explicitly replaces the JCM6510.5x base with1.0x. The proposed doubled salts are a disclosed curator interpretation and preserve stock identity separately from the frozen1G_PER_L dose error.',
26:'JCM1216 supplies0.1x artificial seawater1000ml but no reference1x recipe. The named dilution-state material is representable; components cannot be borrowed from different artificial-seawater recipes.',
27:'JCM1269 complete4x stock is distinct from the200ml receiving dose. Ferric ammonium citrate remains an unresolved source-named component; this biological review does not review W09FAC identity or approve coalescence.',
28:'NBRC14 bird feed is the corn/fish-meal input before boiling/filtering; its two disclosed qualitative ingredients support PARTIAL partonomy without proportions. The extract output is a different material.',
29:'DSMZ1008 and its frozen occurrences specify charcoal-treated natural seawater800ml with200ml distilled water. Biomaris replacement and the DistilledWater rejected alias remain separate; no frozen mass/percent unit error is adopted.',
30:'NBRC1347/JCM995 identify aged seawater. Extra Hutner source protocols are context only, not a universal aging process. The bounded aged-material class is supported.',
31:'NBRC22 and linked TOGO recipe identify2%-salinity seawater. The proposed class carries that disclosed parameter without equating natural/artificial choices or treating2% as NaCl mass fraction.',
32:'JCM30/54/55/116 explicitly identify peeled/cut tissue, with differing boiling/sieving/potato-carrot extraction protocols. Input form is supported; outputs are not interchangeable.',
33:'NBRC1071/TOGO preserve the capitalized2%-salinity label. Case folding is harmless for this scoped material, but it does not select the branch of the starred NBRC13 alternative.',
34:'NBRC304 explicitly names powdered Quaker White Oats3g. This agrees with JCM52 supplied-form evidence; it does not establish a fine colloidal pharmacologic preparation or approve generic oatmeal471.',
35:'JCM651 provides the six-entry0.5x table and1L water basis. Its relation to JCM910 is explicit, while the frozen1G_PER_L receiving dose is a separate upstream unit defect.',
36:'DSMZ1009 resolves see-below to32g sea salt(example InstantOcean) with1000ml water. Both frozen occurrences already retain the volume dose; no unsupported source defect is invented.',
37:'NBRC336 footnote resolves * as filtered aged seawater OR Daigo artificial seawater SP. This preserves the same disjunction as NBRC335 without assuming a selected branch. Existing filtered/aged/artificial owners are partial candidates; the missing fact is which source option was used, unless an explicit alternative group is retained.',
38:'TOGOM2843 explicitly calls for extract from200g boiled potato per litre. This is input-based preparation description, not200g retained solids; the bounded note on UNMAPPED0251 does not equate older4g/L infusion preparations or promote the owner.',
39:'NBRC984 identifies living/cultivated Porphyra thalli in IMK/seawater context, not a purified chemical or complete seawater medium. Unknown mass and carry-over do not block the bounded biomass class.',
40:'MediaDive1624 original record has10g larchwood xylan withSigma attribute. JCM99 independently supports that source material; generic CHEBI37166 and automaticCAS metadata are not exact preparation evidence. Existing owner is reused with local registry promotion and#294 history retained.',
41:'MediaDive270 original record is35000Units with filter-sterilized15000-35000units/1000ml attribute. It is generic catalase, with no bovine/C9322 procurement assertion; preserve its generic scope and all three mapping holds. Activity cannot be converted to mass or lot activity.',
42:'MediaDive728 original record has20g diced potato; DSMZ789 supports that input before boiling/filtering. The historical200g/L research quote is not relied on. Existing physical-form owner is promoted without a universal concentration.',
43:'MediaDive1606 original record has200g potato. JCM333/family recipes support tissue input; CAS93348-51-7 extraction-target claims remain quarantined. No tissue-to-extract or generic molecular formula conversion is allowed.',
44:'MediaDive481 original record has10g bovine horn meal and DSMZ440 corroborates it. Horn-only processed meal is not purified keratin or horn-and-hoof feed; reuse of the existing owner is supported.',
45:'MediaDive725 original100ml dung extract and its DSMZ781 recipe support the same horse-dung filtrate proposal as the CultureMech case, not every generic dung extract elsewhere.',
46:'MediaDive1707 original50g Cow manure is clarified by JCM248:50g dry cow manure, boil1h in1L, filter and restore1L. Thus the existing dry-cow material denotes this starting input. The filtered infusion and withheld ENVOparent/whole-alias claims are not approved; no owner edit is needed for this exact source.',
47:'MediaDive1506 original5g colloidal chitin plus DSMZ1681 recipe supports an added preparation note. The commercial-powder option, unmeasured solids basis and chemical polymer/preparation distinction justify retaining UNMAPPED0361.',
48:'MediaDive2142 original800ml charcoal-filtered natural seawater is corroborated by DSMZ1008. DistilledWater is a rejected lexical hit, not an exact owner; the new treated-water class preserves that exclusion.',
49:'MediaDive471 original10g Oatmeal and DSMZ425 food oatmeal are not demonstrated colloidal fine powder. The C29298 mapping remains held even though other source occurrences justify a separate powdered-Quaker supplied-form note.',
50:'MediaDive1881 original2g malted wheat meal and JCM730 jointly support the starting biological material. Historical CHEBI1881 is an unrelated molecular claim and remains quarantined. No T.aestivum, particle grade or no-heat inference is made.',
}

def ref(eid, reason):
    e=E[eid]
    return {'evidence_id':eid,'path':e['source_path'],'sha256':e['sha256'],
            'url':e.get('url'),'original_accessed_at':e.get('original_accessed_at'),
            'locator':e.get('declared_locator') or 'Complete captured primary record',
            'applicability_checked':reason}

def refs(ids, reason):
    return [ref(eid,reason) for eid in sorted(set(ids)) if eid in E and E[eid]['kind'] in ('primary_source','ontology')]

COMMON = 'This receipt assesses the complete selected YAML scientifically, but authorizes only the stated source outcome/delta. It is not a native full-owner release approval, role review, export authorization, cross-shard coalescence decision or approval of prior research/review assertions. All frozen source-specific holds and coordinator gates persist.'

case_rows=[]
for i,(c,d,b) in enumerate(zip(S['source_cases'],S['active_decisions'],S['case_bindings'])):
    assert sha(canon(c))==b['case_input_sha256']
    assert sha(canon(d))==b['decision_sha256']
    ps=[p for p in S['selected_payloads'] if p['proposal_id'] in d['proposal_ids']]
    evid=refs(d['evidence_ids'],CN[i])
    # Evidence listed on a selected proposal may supply direct support omitted from a
    # source-only decision's short list. Preserve the scientific scope in each locator.
    if not evid:
        evid=refs([eid for p in ps for eid in p['selected_proposal']['evidence_ids']],CN[i])
    assert evid, (i,c['case_id'])
    fid=['W04-BIO-SR-01'] if i in (10,11,17) else []
    if i in (1,20): fid+=['W04-BIO-HOLD-01']
    if i in (12,16,41):fid+=['W04-BIO-HOLD-02']
    if i in (22,34,49):fid+=['W04-BIO-HOLD-03']
    if i==25:fid+=['W04-BIO-OBS-01']
    if i in (4,9,15,37):fid+=['W04-BIO-ALT-01']
    rr=[]
    for o in c.get('occurrences',[]):
        path=pathlib.Path(S['source_root'])/o['full_recipe_snapshot']
        assert sha(path.read_bytes())==o['source_file_sha256']
        rr.append({'occurrence_id':o['occurrence_id'],'recipe_id':o['recipe_id'],'path':str(path),
                   'sha256':o['source_file_sha256'],'locator':o['component_path'],
                   'full_recipe_context_reviewed':True,'raw_label':o.get('raw_preferred_term')})
    case_rows.append({'review_id':f'W04-BIO-CASE-{b["index"]:03d}', 'reviewer':reviewer,
        'biological_scope_index_zero_based':i,'global_shard_index':b['index'],
        'case_id':c['case_id'],'case_input_sha256':b['case_input_sha256'],
        'decision_sha256':b['decision_sha256'],'raw_source_label':c['raw_source_label'],
        'w04_recorded_primary_reviewer':d.get('primary_reviewer'),
        'verdict':'BOUNDED_DECISION_CORRECTION_REQUIRED' if i in (10,11,17) else 'SOURCE_OUTCOME_SUPPORTED_WITH_LIMITS',
        'source_outcome_verdict':'Supported bounded identity/preparation or documented alternative/hold; original source bytes are preserved.',
        'full_owner_verdict':'NOT_APPROVED_FOR_RELEASE', 'reasons':[CN[i]],
        'selected_proposal_ids':d['proposal_ids'],'actual_primary_references':evid,
        'frozen_occurrence_contexts':rr,
        'kg_original_source_record':c.get('original_kg_entry',{}).get('source_record'),
        'preserved_source_holds':d.get('preserved_holds',[]),'finding_ids':fid,
        'acceptance_conditions': [PN[S['selected_payloads'].index(p)][1] for p in ps] +
            ([CN[i]] if not ps else []) +
            (['Replace per-litre or g/L shorthand with the source-batch amount and stated added-water basis; no after-YAML amount changes are needed.'] if i in (10,11,17) else [])+
            [COMMON], 'completed_at':now})

payload_rows=[]
for i,p in enumerate(S['selected_payloads']):
    raw=(T/p['snapshot']).read_bytes();a=yaml.safe_load(raw);assert sha(raw)==p['after_sha256']
    # Binding provided by the manifest is verified in prepare_inputs.py; preserve it
    # alongside the raw after hash, without guessing a different native serializer.
    support,limit=PN[i]
    evid=refs(p['selected_proposal']['evidence_ids'],support+' '+limit)
    if not evid:
        evid=refs([eid for d in S['active_decisions'] if p['proposal_id'] in d['proposal_ids'] for eid in d['evidence_ids']],support+' '+limit)
    assert evid,(i,p['proposal_id'])
    fields={}
    for k,v in a.items():
        if k in ('identifier','preferred_term','mapping_status','ingredient_type','solution_type','ontology_mapping'):
            fields[k]={'verdict':'SUPPORTED_FOR_SOURCE_SCOPE' if i not in (0,20,25) else 'SOURCE_DELTA_ONLY_EXISTING_ASSERTIONS_HELD', 'assessment':support+' '+limit}
        elif k=='components':
            fields[k]={'verdict':'SUPPORTED_SOURCE_TRANSCRIPTION' if i!=28 else 'SUPPORTED_PARTIAL_INPUT_COMPOSITION',
                'assessment':support+' '+limit,
                'items_checked':[{'component_index':j,'complete_selected_component':v1,
                    'assessment':'Compared with the primary stock table, preserving source form and batch unit.' if i!=28 else 'Source names this feed constituent qualitatively; no amount or completeness inferred.'} for j,v1 in enumerate(v)]}
        elif k=='component_assertion':
            fields[k]={'verdict':'SUPPORTED_WITH_METHOD_LIMITS','assessment':support+' '+limit,'method':v['method'],'completeness':v['completeness']}
        elif k=='supplied_form':
            fields[k]={'verdict':'SUPPORTED_SCOPED_ANNOTATION','assessment':support+' '+limit,'items_checked':v}
        elif k=='synonyms':
            fields[k]={'verdict':'HELD_INHERITED_SCOPE' if i in (0,20,25) else 'SOURCE_LABEL_PROVENANCE_PRESERVED',
                'assessment':limit,'complete_selected_aliases':v}
        elif k=='occurrence_statistics':
            fields[k]={'verdict':'CONTEXT_ONLY_NOT_NEWLY_VALIDATED_CORPUS_COUNTS','assessment':'Read in full; retained values do not prove identity, source frequency, or publication eligibility. New recipe-scoped counts are not a corpus rebuild.','values':v}
        elif k=='curation_history':
            fields[k]={'verdict':'AUDIT_TRAIL_ONLY','assessment':'All events read, including superseded mappings and research quotations. They are authorship/provenance, not independent scientific evidence.',
                'all_recorded_curators':list(dict.fromkeys(x.get('curator') for x in v)), 'w04_proposal_events':[x for x in v if str(x.get('curator','')).startswith('codex_worker04')]}
        elif k=='environmental_context':
            fields[k]={'verdict':'SUPPORTED_AS_NATURAL_SOURCE_CONTEXT_ONLY','assessment':'ENVO00002149 current captured label is ocean water with seawater synonym. This context does not identify filtered seawater exactly with untreated ocean water or create a role.','values':v}
        elif k=='chemical_properties':
            fields[k]={'verdict':'SUPPORTED_GENERIC_ENZYME_CAS_ONLY','assessment':'CAS9001-05-2 is corroborated by the supplier COA. No single molecular structure, human protein or universal lot activity is asserted.','values':v}
        elif k=='kg_microbe_node_id':
            fields[k]={'verdict':'WITHHOLD_EXACT_GENERIC_OATMEAL_IDENTITY','assessment':'The unchanged NCITC29298 identifier is part of the unresolved colloidal/fine-powder identity claim, not corroboration of it.'}
        elif k=='notes':
            fields[k]={'verdict':'SUPPORTED_SCOPED_INTERPRETATION','assessment':support+' '+limit}
        else:raise AssertionError((i,k))
    fids=[]
    if i in (1,2,4):fids+=['W04-BIO-SR-01']
    if i==0:fids+=['W04-BIO-HOLD-01']
    if i==20:fids+=['W04-BIO-HOLD-02']
    if i==25:fids+=['W04-BIO-HOLD-03']
    if i==6:fids+=['W04-BIO-OBS-01']
    payload_rows.append({'review_id':f'W04-BIO-PAYLOAD-{i:02d}','reviewer':reviewer,
        'biological_payload_index_zero_based':i,'proposal_id':p['proposal_id'], 'case_ids':p['case_ids'],
        'owner_path':p['owner_path'],'selected_snapshot':p['snapshot'],
        'after_sha256':p['after_sha256'],'canonical_payload_sha256':p['payload_sha256'],
        'before_snapshot':p.get('before_snapshot'),'before_sha256':p['selected_proposal'].get('before_sha256'),
        'w04_recorded_curator':a['curation_history'][-1]['curator'],
        'verdict':'SOURCE_DELTA_SUPPORTED_WITH_EXPLICIT_INHERITED_HOLDS' if i in (0,20,25) else 'BOUNDED_PAYLOAD_SUPPORTED',
        'source_delta_verdict':'SUPPORTED','full_owner_verdict':'NOT_APPROVED_FOR_RELEASE',
        'reason':support,'full_field_assessment':fields,'actual_primary_references':evid,
        'finding_ids':fids,'residual_full_owner_holds':[limit,COMMON],
        'bounded_fix': 'Correct linked decision quantity-basis wording only; selected YAML component quantities are already correct.' if i in (1,2,4) else ('Clarify first component-assertion evidence note to say derived from the referenced0.5x table, as its method and second evidence note already state.' if i==6 else None),
        'acceptance_conditions':[limit,COMMON],'completed_at':now})

def ids(indices):return [S['source_cases'][i]['case_id'] for i in indices]
findings=[
 {'finding_id':'W04-BIO-SR-01','status':'OPEN_BOUNDED_CORRECTION','severity':'scientific wording; selected payloads unaffected',
  'case_ids':ids([10,11,17]),'global_shard_indices':[39,41,49],
  'proposal_ids':[S['selected_payloads'][i]['proposal_id'] for i in [1,2,4]],
  'reproduction':'Read active reasoning for39 (components per litre),41 (47.15g NaCl/18.10g MgCl2 hexahydrate per litre),49 (NaCl55.4g/L); compare JCM492 stock table1L distilled water, DSMZ611 stock table1000ml distilled water and DSMZ946a p2 stock table1000ml distilled water. None of those stock sections declares final volumetric makeup. DSMZ611 final1012ml header belongs to the receiving medium. Selected after YAML correctly records g per source batch.',
  'proposed_bounded_fix':'Change only the reasoning to source-batch masses with the stated1L/1000ml added-water amount. Preserve stock-dose values, all eleven/sixteen/twelve components, source bytes, outcome and holds. No unmeasured final-stock concentration is claimed.',
  'evidence':refs(['BIO-PRIMARY-6b74fe99558a128c','BIO-PRIMARY-f93c582c16f11798','BIO-PRIMARY-251d30ed6e239c8a'],'Stock sections and added-water rows versus active decision reasoning'),
  'issue_context':'Within #1201 source-qualified curation. It is not Mg-citrate#1190, EDTA#1191 or the separate parser/source conflicts#1192; coordinator deduplicates any issue action.'},
 {'finding_id':'W04-BIO-HOLD-01','status':'RETAINED_FULL_OWNER_HOLD','case_ids':ids([1,20]),
  'proposal_ids':[S['selected_payloads'][0]['proposal_id']],
  'reproduction':'Filtered_Seawater after retains Natural seawater as resolving RAW_TEXT although MICRO0001773 and the primary inputs require filtration.',
  'proposed_bounded_fix':'Do not release the whole alias row on the strength of the two new filtration-preserving aliases. Reconcile the inherited unqualified label to its original occurrences and retain a non-resolving or explicitly scoped disposition when justified. No inherited alias edited in this review.',
  'evidence':refs(['BIO-PRIMARY-e985257a8f05541b','BIO-PRIMARY-c9440f55c5fd86de'],'MICRO definition and JCM1102 filtrated input'), 'issue_context':'Preserved publication obligation, not a failure of the proposed two-alias delta.'},
 {'finding_id':'W04-BIO-HOLD-02','status':'RETAINED_FULL_OWNER_HOLD','case_ids':ids([12,16,41]),
  'proposal_ids':[S['selected_payloads'][20]['proposal_id']],
  'reproduction':'Catalase after retains two Properties metadata labels and C--10 catalog variant. Independently executed pinned synonym_policy excludes both Properties entries; they are not active alias leaks. C--10 still resolves and its product identity is not verified by the C9322 COA. Frozen generic ingredient270 retains mapping/export holds.',
  'proposed_bounded_fix':'Keep source-scoped C9322 supplied form and #312 human exclusion; do not clear any complete-row/export hold. Later alias/product curation requires its own provenance and exact payload review.',
  'evidence':refs(['BIO-PRIMARY-supp-8bb907b6a644b834','BIO-PRIMARY-de6aeb89029c0b8a','I1201-BIO-mesh-catalase-v2'],'COA lot scope, human NCIT definition and species-neutral MeSH descriptor'), 'issue_context':'#312 is historical/contextual evidence of the exclusion, not inherited scientific approval.'},
 {'finding_id':'W04-BIO-HOLD-03','status':'RETAINED_FULL_OWNER_HOLD','case_ids':ids([22,34,49]),
  'proposal_ids':[S['selected_payloads'][25]['proposal_id']],
  'reproduction':'Oatmeal after retains NCITC29298 exact mapping/kg_microbe_node_id. NCIT defines fine colloidal whole-oat powder; JCM52/NBRC304 disclose ordinary powdered Quaker Oats and DSMZ425 generic food oatmeal.',
  'proposed_bounded_fix':'Retain the supported supplied-form note and hold complete exact mapping/export until all owner occurrences and material boundaries are reconciled. Do not infer colloidal processing from an ontology synonym or provider automaticCAS.',
  'evidence':refs(['BIO-PRIMARY-3decc23cfde472e5','BIO-PRIMARY-ce222a987d4a5a05','BIO-PRIMARY-e1adda7567ff336b','BIO-PRIMARY-followup-61f3ff18e6d53970'],'Ontology definition and actual powdered/generic recipe inputs'), 'issue_context':'#1201 bounded curation can proceed without clearing the preexisting whole-owner identity mismatch.'},
 {'finding_id':'W04-BIO-ALT-01','status':'SCIENTIFICALLY_JUSTIFIED_SOURCE_ALTERNATIVES','case_ids':ids([4,9,15,37]),'global_shard_indices':[22,38,46,116],
  'reproduction':'NBRC13 permits natural/artificial2%-salinity seawater;335/336 permit filtered aged water or Wako Daigo SP; DSMZ1054 permits Biomaris/natural/artificial sources. No recipe records a selected branch.',
  'proposed_bounded_fix':'No new single-identity owner is justified for the disjunction. Accept the source disposition with explicit branches intact; any later exact association must select a source-demonstrated branch or represent alternatives explicitly. Existing bounded filtered/aged/Biomaris/2%-salinity and artificial-stock owners are candidates only, not whole-disjunction identities.',
  'evidence':refs(['BIO-PRIMARY-eed17390da1da1c6','BIO-PRIMARY-577ba095c05db6c8','BIO-PRIMARY-dd5b2e6cd4382f73','BIO-PRIMARY-5310c00ebd34b2d0'],'Complete recipes and alternative footnotes'),
  'issue_context':'Distinguishes genuine ambiguity from #1201 deferral of already-supported bounded materials. No missing-composition blanket hold.'},
 {'finding_id':'W04-BIO-OBS-01','status':'NONBLOCKING_PROVENANCE_WORDING','case_ids':ids([25]),'proposal_ids':[S['selected_payloads'][6]['proposal_id']],
  'reproduction':'JCM910 after component_assertion.method is CURATED_INTERPRETATION and second evidence note explicitly says doubling is a curator calculation. First evidence note still says all components transcribed.',
  'proposed_bounded_fix':'Clarify the first note to match the correctly declared method and second note. Quantities and scientific outcome are supported as a disclosed calculation, not verbatim transcription.',
  'evidence':refs(['BIO-PRIMARY-ba94778d8e851661','BIO-PRIMARY-ea90e577fff6331e'],'JCM910 replacement instruction and JCM6510.5x table'),
  'issue_context':'No separate identity or quantitative blocker; coordinator may include this small clarity correction with source-evidence cleanup.'}
]

used={r['evidence_id'] for x in case_rows+payload_rows for r in x['actual_primary_references']}
used|={r['evidence_id'] for f in findings for r in f['evidence']}
evidence_rows=[]
for eid in sorted(used):
    e=dict(E[eid]);assert sha(pathlib.Path(e['source_path']).read_bytes())==e['sha256']
    e['reviewer']=reviewer;e['reuse_status']='ORIGINAL_BYTES_HASH_VERIFIED_AND_SCIENTIFIC_APPLICABILITY_INDEPENDENTLY_ASSESSED'
    e['reviewed_at']=now;e['retrieval_claim']='Reused archived primary capture. Original retrieval timestamp is preserved; reviewed_at is not represented as a fresh retrieval.'
    e['applies_to_case_ids']=[x['case_id'] for x in case_rows if any(r['evidence_id']==eid for r in x['actual_primary_references'])]
    e['applies_to_proposal_ids']=[x['proposal_id'] for x in payload_rows if any(r['evidence_id']==eid for r in x['actual_primary_references'])]
    evidence_rows.append(e)

header={'reviewer':reviewer,'reviewed_w04_head':S['worker_head'],'scope':'All51 biological cases and all37 selected complete payloads; no superseded payload adopted; no role/export/full-owner release approval.',
        'assignment_sha256':sha((T/'assignment.json').read_bytes()),'scope_sha256':sha((T/'scopes/biological.json').read_bytes()),'completed_at':now,'scientific_approval_inherited':False}
for name,key,rows in [('case-reviews.json','case_reviews',case_rows),('payload-reviews.json','payload_reviews',payload_rows),('findings.json','findings',findings),('evidence.json','evidence',evidence_rows)]:
    content=header|{key:rows}
    if name=='evidence.json':
        content|={'frozen_full_recipes_checked':I['recipes'],'all_declared_capture_hash_check_receipt':'reviews/biological/input-checks.json',
                  'historical_review_treatment':'Prior validation and approval artifacts were inspected for context/provenance only, not counted as primary scientific support.',
                  'retrievals_during_this_review':[],'capture_reuse_count':len(rows),'full_recipe_count':len(I['recipes']),
                  'pinned_alias_policy_check':{'path':'reviews/biological/synonym-resolution-check.json','sha256':sha((R/'synonym-resolution-check.json').read_bytes()),'purpose':'Distinguishes retained metadata from labels allowed to resolve; a resolving-policy result is not scientific approval or proof of release.'}}
    (R/name).write_text(json.dumps(content,ensure_ascii=False,indent=2)+'\n')

assert len(case_rows)==51 and len(payload_rows)==37
assert {x['case_id'] for x in case_rows}=={x['case_id'] for x in S['source_cases']}
assert {x['proposal_id'] for x in payload_rows}=={x['proposal_id'] for x in S['selected_payloads']}
for p,r in zip(S['selected_payloads'],payload_rows):
    assert set(yaml.safe_load((T/p['snapshot']).read_text()))==set(r['full_field_assessment'])
receipt=header|{'status':'PASS','case_count':len(case_rows),'payload_count':len(payload_rows),'primary_capture_count':len(evidence_rows),'full_recipe_count':len(I['recipes']),
 'checks':['Exact51-case coverage and canonical case/decision hashes','Exact37-payload coverage and after-byte hashes; canonical payload hashes independently checked by prepare_inputs','Every present top-level YAML field assessed; every stock component retained in review','Every case/payload has actual primary capture path/hash/locator','All cited primary byte hashes rechecked','All frozen occurrence recipe byte hashes verified','No input or maintained data mutations by review scripts'],
 'open_bounded_scientific_corrections':['W04-BIO-SR-01'],'retained_full_owner_holds':['W04-BIO-HOLD-01','W04-BIO-HOLD-02','W04-BIO-HOLD-03'],
 'files':{f:sha((R/f).read_bytes()) for f in ['case-reviews.json','payload-reviews.json','findings.json','evidence.json','input-checks.json','prepare_inputs.py','write_review.py','synonym-resolution-check.json','pinned-synonym-policy.py']}}
(R/'validation-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k in ['status','case_count','payload_count','primary_capture_count','full_recipe_count','files']},indent=2))
