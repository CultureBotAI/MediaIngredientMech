"""Independent skeptical review by /root/primary_a; notes are agent-authored.

This file assembles recorded review observations, not chemical conclusions from
string matching. Re-run only after inspecting any changed B primary inputs.
"""
import datetime
import hashlib
import json
from pathlib import Path

R = Path(__file__).resolve().parents[1]
NOTES = {
70: 'The three MRS occurrences specify three waters explicitly. I checked the trihydrate ontology against the anhydrous alternative; adding the formula alias does not erase hydration. Historical flattened quantities are not independently approved.',
71: 'The CCAP UCM label supplies calcium but no D/L designation. The D-specific calcium pantothenate owner and a differently stereospecified salt cannot be chosen from vitamin function or a typographical similarity. Hold remains precise.',
72: 'BBL trypticase is a commercial digest. A generic casein/peptone mapping cannot stand in for exact commercial material; the source catalogue and product-scope gap is real.',
73: 'Dihydrogen orthophosphate and monohydrate are both explicit. CHEBI114249 preserves Na:H:phosphate and one water; neither generic phosphate nor anhydrous sodium phosphate is equivalent.',
74: 'The original M2653 component is a 20% stock addition. The proposed nominal stock preserves an unspecified percent basis and separate addition amount, and makes no exact whole-stock identity to sodium formate solute.',
75: 'CHEBI17905 defines coenzyme M as the organosulfonic acid, supporting the source acid name. Existing owner preferred label 2-Mercaptoethanesulfonate is misleading inherited wording; approval is restricted to the bounded new acid alias, with full-owner review remaining separate.',
76: 'The existing CAS9049-37-0 sodium-polygalacturonate identity is distinct from free polygalacturonic acid CHEBI62969. The proposed name does not change the asymmetric parent relationship or invent a single polymer chain formula.',
77: 'I compared all frozen DSM1053/188 and solution contexts, including existing hydrate-to-parent annotations. Current DSM1053 differs; current DSM188 retains hydrated ferric sulfate. Neither live replacement nor bare x notation proves a fixed water count for every frozen row.',
78: 'I inspected calcium folinate CHEBI31340 and folinic acid CHEBI15640. Calcium salt is supported; the proposal adds no levofolinate-specific stereochemical assertion beyond the existing calcium-folinate identity.',
79: 'The complete KOMODO/DSM645/911 contexts preserve distinct provider rates and OADC stock preparation. Fraction V is preparation-grade information, not a newly exact molecular identity; copied LB history remains superseded. No generic albumin approval follows.',
80: 'Magnesium sulfate with seven waters is explicit even within a 20x basal salt preparation. The alias is to the heptahydrate constituent, not to the containing solution or a recalculated receiving-medium concentration.',
81: 'The n-hexanoate name fixes the straight-chain C6 carboxylate sodium salt, unlike branched hexanoate alternatives or free acid. CHEBI114126 is consistent.',
82: 'M2568 uses the 4% L-cysteine hydrochloride material as a stock. L and HCl survive in the nominal preparation; unspecified percent basis and starting hydrate are retained instead of assigning monohydrate.',
83: 'Na2S2O4 is dithionite, not dithionate. I separately checked CHEBI66870 versus scutellarin CHEBI61278; rejecting the six flavonoid labels is chemically supported and does not justify rejecting unrelated inherited fields.',
84: 'The 3 M HCl entry is a variable pH reagent. The new nominal stock separates molar strength from its unquantified addition and does not assert final-medium acid concentration.',
85: 'DSM1203a specifies an Oxoid basal broth at35.4g/L. A current differently named broth at29.7g/L is insufficient catalogue proof. Source product and prepared medium remain distinct; the explicit identification gap is appropriate.',
86: 'The frozen CHEBI86416 is a phosphatidylcholine and plainly contradicts the dodecahydrate phosphate name. CHEBI91259 is the named salt hydrate; no source mass conversion is approved by the identity correction.',
87: 'The source explicitly says cyano, so the vitamin-B12 parenthetical does not broaden the ingredient to all cobalamins. Exact cyanocobalamin alias is defensible.',
88: 'Correcting HC1 to HCl cannot resolve L versus DL or hydration. The source has no accompanying catalogue/CAS; a convenient existing L owner is insufficient.',
89: 'Both original ATCC2467/2485 repeat dehydrate. I checked that the hold concerns the original ambiguity, not merely an OCR token in CultureMech. Dihydrate cannot be silently substituted without an authoritative formula/product witness.',
90: 'Sodium EDTA spans seven MediaDB contexts. I challenged the ontology-only evidence coverage because separate Fischer/Sauer, Mogensen and Shcolnick references must be pursued; salt sodium count and hydration require family-specific evidence.',
91: 'I found Sigma V6629 in the complete frozen UTEX DAS component evidence, contradicting the initial class-only rationale. This exact catalogue lead must determine the source-specific vitamer before approval; generic cobalamin must not become a global cyano synonym.',
92: 'CHEBI131531 explicitly contains one equivalent HCl; it is distinct from pyridoxamine dihydrochloride. The proposed spelling repair retains the single-HCl name and makes no inferred extra-acid assertion.',
93: 'The source JCM1415 stock is 8% NaHCO3,25ml, filter-sterilized as marked. Typographical soluiton is preserved in source context; the nominal stock keeps percent basis unknown and avoids treating25ml as grams.',
94: 'The same generic basal-medium label occurs in JCM1013 and JCM431 with different complete preparations. Two source-qualified proposals correctly avoid a single global alias; parent supplements are not all included in the basal stocks.',
95: 'The13 chopped-meat contexts use1N NaOH in preparation, often25ml. Normality and separate stock/preparation scope must remain explicit; final broth concentration cannot be calculated from these flattened rows.',
96: 'The P5 RS NM nested stock is explicitly cyanocobalamin at1g/L solute. I checked the surrounding five mix stages and NNM carrier notes: correcting the class pointer is supported, whereas assigning this1g/L to final nutrient medium would not be.',
97: 'The cysteine hydrochloride monohydrate formula fixes hydration but not stereochemistry. Tryptic-soy commercial expansion provides no independent cysteine catalogue, so L cannot be inferred from common laboratory practice.',
98: 'PPLO Difco is a product-level input within a complex KM2 recipe. BHI supplier metadata belongs to another input and cannot supply PPLO catalogue identity or crystal-violet status.',
99: 'Powder describes the physical form of elemental sulfur. The source differentiates powdered sulfur from sulfide ore and trace solution; an elemental-sulfur alias is supported without assigning a particular allotrope.',
100: 'ATCC593/735 describe fat removal, cooking, retention of meat and filtrate, and possible horse substitution. Preparation-qualified raw meat must not become a global generic ground-beef synonym or an already prepared broth identity.',
101: 'Both Pyrococcus and BacDive/DSM181 sulfur occurrences denote elemental sulfur but have different quantity stages. In Pyrococcus it is separately added per tube; no common final-medium dose or basal-stock inclusion is inferred.',
102: 'JCM946 Korthof10x preparation is distinct from serum-supplemented final medium. The full input list,450ml plus50ml water preparations and calcium addition are preserved without an experimentally verified final-volume assumption.',
103: 'JCM665 supplies2M sodium acetate atpH7.0. The nominal buffer stock retains pH and unknown titrant without assigning exact acetate starting hydrate or a final-medium2M concentration.',
104: 'The NBRC shrimp-agar source states dried shrimp but no taxon, catalogue, or precise processed fraction. Generic shrimp food cannot prove exact equivalence to this prepared growth-medium input.',
105: 'Both NBRC869/870 specify D(+), which supports the D-calcium-pantothenate identity despite spelling. The existing owner has wider inherited stereo claims under native review; this bounded added label does not approve those.',
106: 'The M2405 BSM subrecipe retains literal (NH4)SO4 and CaCl2·7H2O, plus agar percent with unspecified basis. I checked that the nominal source-qualified stock does not silently repair these into ordinary ammonium sulfate or calcium dihydrate.',
107: 'The Vitox proposal represents one Oxoid vial reconstituted in10ml fluid and its separate2ml addition. The vial and rehydration fluid are preparation inputs, not inferred complete molecular ingredients or an unsupported catalogue match.',
108: 'Anhydrous is explicit in the M2256 component name; CHEBI32599 agrees and the heptahydrate is excluded. Exact primary-source follow-up was requested after earlier access failures.',
109: 'Tribasic and dihydrate together fix trisodium citrate with two waters. The precise alias is safe unlike a generic sodium-citrate stock name; current primary retrieval was requested to corroborate the frozen source.',
110: 'I independently compared the exact JCM900 primary Hutner table and preparation text with every proposed part. NTA10g,Mg29.7g,Ca3.335g,malformed(NH4)6MoO24·4H2O9.25mg,Fe99mg,Metals44 50ml,water950ml,KOH about7.3g and alternative pH reagents agree. COMPLETE concerns the input list, not resolved chemistry. JCM979 duplicate identity requires coordinator integration review.',
111: 'The explicit CH3COONa formula contrasts with the separate trihydrate case70. Identity proposal does not reuse the anomalous200 flattened source amount as a final-medium concentration; current source follow-up was requested.',
112: 'The M2653 reducing-agent proposal preserves5gL-cysteineHCl,40ml12.5%sulfide stock,330mlwater and30ml N NaOH. It is expressly limited to this recovered recipe, not automatically the second M2707 occurrence with a different preparation context.',
113: 'RGCA source CysteineHCl fixes hydrochloride but not stereo/hydrate. The legacy MIM accession is not independent chemical evidence, and issue905 directly cautions against conflating L and DL.',
114: 'I read JCM923:20mM sodium acetate is added from sterile anaerobic stock,0.05ml to each5ml tube. That explicit stock instruction supports the nominal preparation; the20mM is not asserted as final tube concentration.',
115: 'DL and sodium are explicit but sodium stoichiometry is absent. I independently checked CHEBI91260 racemate versus91261(S): rejecting DL aliases from the L owner is justified while mapping this source to disodium remains unproved.',
116: 'The17 occurrences include Schaechter salt media,Hassan glucose-limited media,E2 and Vogel-Bonner contexts. I challenged extrapolation from a single DOI; hydration and stoichiometry must be pursued by each distinct source family.',
117: 'NBRC981 specifies0.1MTris-HCl,pH7.5,50ml. The nominal buffer identity does not assume pure protonated Tris atthatpH or infer acid/base ratio from stock name.',
118: 'The full MediaDive4784/JCM825 recipe explicitly adds10ml/L of3% L-cysteine hydrochloride monohydrate solution from sterile anaerobic stock. The new stock remains distinct from CHEBI91248 solute, with basis unknown; current original retrieval was requested.',
119: 'The1% sodium fumarate input is a stock, and unqualified sodium does not establish one versus two sodium ions. Its nominal proposal properly keeps both chemical stoichiometry and percent basis unresolved.',
120: 'A60% syrup is supplied material, not pure sodium L-lactate. The new nominal stock does not manufacture a w/w basis, hydration, or stereochemistry, and preserves the source addition separately.',
121: 'The14 JCM contexts differ in addition amount,gas atmosphere,sterilization and pH handling. Every raw occurrence remains bound; a universal solution alias or common final dose is unsafe. Nominal-source-stock representability was raised with coordinator for consistency.',
122: 'I independently checked the original JCM1209 basal-salts table against all8 proposed inputs: NH4NO3 50mg,MgCl2·6H2O8.5mg,SiO2 7.5mg,MnSO4·xH2O4.5mg,CaCl2·2H2O4.2mg,methylene blue4mg,FeSO4·7H2O1.8mg,water1L. The10ml receiving-recipe addition is separate. This is payload review for B122; C156 applicability is independently reviewed by its assigned reviewer.',
123: 'The Tris1M pH8 reagent is an input to TiNTA preparation,7.2ml, also inherited by JCM924. The new nominal buffer does not identify it as pure solid Tris or invent unreported titrant and final stock volume.',
124: 'CHEBI6637 magnesium dihydroxide is incompatible with the source magnesium citrate. BD220908 identifies the commercial parent preparation but does not establish citrate stoichiometry/hydration; hold cannot be resolved by generic citrate name alone.',
125: 'DSM1144 Hutner has3.34gCaCl2·2H2O and a separately malformed ammonium molybdate string. Both differ from blind normalizations; proposed source amounts,KOHapproximation and nestedMetals44 are preserved. No global Hutner alias is justified.',
126: 'I compared SAG12/19 references to official MerckTitriplexIII108418, which specifies disodiumEDTA dihydrate. The source-specific correction is supported by exactproduct linkage; the generic DisodiumEDTA label stays unsuitable as a universal dihydrate alias.',
127: 'All17 FEBA contexts explicitly carry the heptahydrate name andCAS7782-85-6/MW268.07. Those agree with NCITC61946; different recipes and dosage units do not erase seven waters or authorize quantity normalization.',
128: 'L and hydrochloride are explicit. CHEBI91247 describes that named salt; no extra water can be introduced solely because another owner is the monohydrate. Current exact source retrieval was requested; full inherited owner restrictions remain separate.',
129: 'C6H9NO6 independently supports the neutral nitrilotriacetic acid identity and excludes sodiumNTA. The proposed alias preserves the formula without importing a sodium chelator merely because it dissolves atalkalinepH.',
130: 'The marine-source DL malate label cannot map exactly to(S)-specific CHEBI91261. Shared claim-rejection proposal is sound; absence of an explicit sodium count keeps the sourceidentity unresolved.',
131: 'The two chopped-meat carbohydrate recipes specify fat-free ground beef in preparation contexts. Generic FOODONgroundbeef lacks that preparation scope, and source protein content alone does not identify a commercial prepared ingredient.',
132: 'The original NBRC1382 itself repeats H4MoNa2O6·2H2O. The base elemental formula already includes two waters relative to Na2MoO4, so the extra suffix cannot be silently stripped; authoritative original-form correction remains necessary.',
133: 'JCM1479 explicitly requires a5% L-cysteineHClmonohydrate stock atpH7.0,1ml addition. This differs from unadjusted5%stocks; nominalbuffer identity preserves unknownpHadjustment reagent and percentbasis.',
134: 'Seven JCM-derived occurrences use the5% doublehyphen cysteine hydrochloride monohydrate label in different parent preparations. Raw labels and individualdosages must survive; nominal-source-stock representability was raised with coordinator separately.',
135: 'The0.2M sodiumcitrate is a reagent for titaniumcitrate preparation. Its molarity is distinct from finalculture dose; source name doesnotselect trisodium startingmaterial or hydrate. Nominalstock keeps that uncertainty.',
136: 'DisodiummagnesiumEDTA is not simple disodiumEDTA,freeacidEDTA ormagnesium sulfate. FourBG11 sources were compared, with suppliedhydrate stillunresolved. Supplierexamples without exactsourcecatalogue do not establish sharedhydration.',
137: 'Na2MoO3 retains oxygen3 in the source. Repairing to ordinary molybdate would alter chemicalidentity; association with a familiar traceelement recipe is insufficient independentproof.',
138: 'CuSO2·5H2O in oneBG11 source conflicts with sulfateformula despite parallelrecipesusingCuSO4. The literalbadtoken staysunmapped; similarrecipeevidence is a correctionlead,not an activeglobalalias.',
139: 'Caseinsodium denotes sodiumcaseinate,matching MICRO0001611 suppliedprotein material. The proposal doesnot equate itwith freecasein, a specificproteinsequence, or a wholematerial molecularformula.',
}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    decisions = json.loads((R/'parts/b-decisions.json').read_text())['decisions']
    proposals = json.loads((R/'parts/b-proposals.json').read_text())['proposals']
    cases = json.loads((R/'parts/b-input.json').read_text())['cases']
    findings = json.loads((R/'parts/a-review-b-findings-initial.json').read_text())['findings']
    rows=[]
    for i,(c,d) in enumerate(zip(cases,decisions),70):
        assert c['case_id']==d['case_id']
        rows.append({'index':i,'case_id':c['case_id'],'raw_source_label':c['raw_source_label'],
            'occurrence_ids':[o['occurrence_id'] for o in c['occurrences']],
            'case_input_sha256':d['case_input_sha256'],
            'status':'findings_open' if i in [90,91,116] else 'reviewed_with_scope_limits',
            'independent_assessment':NOTES[i],
            'evidence_ids_examined':d['evidence_ids'],
            'proposal_ids_examined':d['proposal_ids']})
    out={'reviewer':'/root/primary_a','primary_author':'/root/primary_b',
         'reviewed_at':datetime.datetime.now(datetime.UTC).isoformat(),
         'status':'findings_open','scope':'All70 cases indices70:140 and44 initial exact owner proposals; complete frozen recipe pointers checked for all193occurrences. Claim-level source review, not native full-owner publication approval.',
         'input_hashes':{f:sha(R/f) for f in ['parts/b-input.json','parts/b-decisions.json','parts/b-evidence.json','parts/b-proposals.json']},
         'cases':rows,'findings':findings,
         'proposal_payloads':[{'proposal_id':p['proposal_id'],'path':p['after_capture']['path'],'sha256':p['after_capture']['sha256'],'status':'requires_primary_followup' if p['proposal_id']=='B-PROPOSAL-Vitamin_B12' else 'bounded_payload_reviewed'} for p in proposals],
         'shared_review_separation':{'JCM900':'I review B110 exact primary stock payload; C reviews A38/47 source applicability. JCM979 equivalent preparation requires separate coordinator integration review.','JCM1209':'I review B122 exact stock payload against original table; B independently reviews C156 source applicability.','C-P01':'B reviews C-authored NTA payload; C reviews A55 source applicability. No self-reviewed author claim is substituted.'},
         'limitations':['Inherited complete owner payloads, release eligibility and maintained-surface changes require coordinator native review.','Proposal-only outputs do not lift WITHHOLD or REJECTED gates.','Source normalization quantities and final-volume assumptions were not broadly recertified.']}
    (R/'parts/a-review-b-draft.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print('Wrote independent draft',len(rows),'cases',len(proposals),'payloads')
if __name__=='__main__': main()
