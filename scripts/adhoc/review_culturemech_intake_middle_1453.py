#!/usr/bin/env python3
"""Inspect and record explicit middle-owner source judgments for #1453.

Date: 2026-11-16. Inputs: exact pinned final-v3 owner packets 109..218
(except delegated 118) and separately delegated 285..299 and 300..349 owners.
Outputs: lossless claim display (coordinates separately pinned) or an explicitly
authored case-decision JSON. No mapping inference, recipe edits or network calls.
"""

import argparse
import hashlib
import json
import re
from pathlib import Path

from review_culturemech_intake_second_1453 import factor_payloads, field_values, text_templates

SUMMARY_SHA256 = "c166a20a7874dab2fe7c4812ed733d5065008a75a89841aae0e92a6e6811451b"
INTAKE_SHA256 = "6bcc92540daba081d8180346d135c2ae40471c9fb0a7005b46aa5c9902d684f7"
PACKET_SHA256 = "8fa677ea9ed591941564c24d4e190e943f6bb84f22f03f909342c58cf3617760"
ROOT = Path(__file__).resolve().parents[2]
PARTITIONS = ROOT / ".temp/1453/review-partitions-final-v3-6f1b1d18a5"
OWNERS = tuple(index for index in range(109, 219) if index != 118)
EXTRA_OWNERS = tuple(range(300, 350))
LATE_OWNERS = tuple(range(285, 300))

# Explicit manual case-order decisions; ordering is bound by each packet digest.
# The display prints these indices beside the full case ID and source payloads.
DECISIONS = {
    285: {
        0: ("SUPPORTED", "All 301 distinct Nicotinic acid descriptors were inspected with reconstruction-verified factoring, including every source qualifier and evidence text. MediaDive, JCM, DSMZ, TOGO, KOMODO and BacDive labels preserve the neutral acid name; no salt or nicotinate identity is substituted. Stock/batch quantities, historical duplicate sums and inferred denominators remain separate and are not approved."),
        1: ("SUPPORTED", "All six lowercase nicotinic-acid descriptors were read. The primary yeast-paper excerpts explicitly restore nicotinic acid despite historical MediaDB Nicotinate labels; the remaining descriptors preserve the acid name. The neutral owner matches without accepting historical cross-reference identities or certifying doses."),
        2: ("WITHHOLD", "The inspected MediaDive2006 descriptor explicitly preserves Nicotinate and CHEBI32544, which live ChEBI defines as the conjugate-base anion. The native owner CHEBI15940 is neutral nicotinic acid. Its exact synonym alone does not resolve supplied-form identity for the complete case."),
        3: ("SUPPORTED", "All18 Nicotinic Acid descriptors retain the neutral acid, including CAS59-67-6 and Wolfe/Thauer/CCAP stock contexts. The owner matches the named solute; DL vitamins is retained as a stock name rather than stereochemistry, and no stock formulation or dose is approved."),
        4: ("SUPPORTED", "All16 Niacin descriptors and MediaDive610 source excerpts were inspected. They preserve the chemical niacin/nicotinic-acid name used by this owner, with no nicotinamide or salt qualifier. Named stocks and quantities remain explicit; this does not generalize vitaminB3 activity into chemical equivalence."),
        5: ("SUPPORTED", "The sole lowercase niacin descriptor preserves the same nicotinic-acid chemical name and no contradictory material qualifier. Binding the owner does not certify the legacy50g/L quantity or vitamin efficacy.")},
    286: {
        0: ("SUPPORTED", "All three Nitrate descriptors preserve the bare nitrate-anion name, including MediaDB287 and KEGGno3 context. Live ChEBI17632 confirms this anion concept. No supplied salt, actual solution speciation or quantitative validity is inferred."),
        1: ("WITHHOLD", "The complete held mention explicitly retains IDENTITY_FORM and OPERATION uncertainty: nitrate absence describes a separate BG110 comparator, not a removal from the nitrate-replete BG11 variant. Its source does not establish a specific nitrate material or operational event; preserve the held case.")},
    287: {0: ("SUPPORTED", "The sole source explicitly names nitrilotriacetic acid trisodium salt. The reviewed native owner preserves three sodium ions per NTA and distinguishes disodium stock history; this matches the named salt without adding hydration or approving concentration.")},
    288: {
        0: ("SUPPORTED", "Both N2O descriptors preserve the nitrous-oxide formula, matching the native molecular owner. Their legacy percent-w/v gas quantities are not approved or converted; no nitric oxide or nitrogen dioxide identity is substituted."),
        1: ("SUPPORTED", "The sole descriptor names N2O and explicitly retains gas/variable-amount context. Nitrous oxide matches the owner; unspecified dosage and gas handling remain outside this identity binding.")},
    289: {
        0: ("SUPPORTED", "The complete Carini2014 REPLACE payload preserves O-phospho-L-serine only as the displaced inherited parent label. That historical context label matches the owner; the new source phosphoserine remains stereochemically unspecified. This does not assert L reagent presence or establish the inherited base recipe experimentally."),
        1: ("WITHHOLD", "The positive AMS1 parent descriptor inherits O-phospho-L-serine and KEGG:pser-L, but the same recipe's primary-source-bound replacement explicitly records that Carini2014 does not establish D/L stereochemistry. Preserve the unresolved supplied-material specificity rather than promote the inherited L annotation.")},
    290: {0: ("SUPPORTED", "Both descriptors explicitly name OADC Enrichment, matching the maintained local named-preparation owner. It remains an opaque multicomponent stock; no fixed formulation, equivalence to an individual constituent, or inconsistent mass/volume dose is approved.")},
    291: {0: ("SUPPORTED", "All nine Oat flakes descriptors and DSMZ189/1815, MediaDive512/316/855/425 source contexts preserve the flaked oat preparation. The FOODON material matches without substituting oatmeal powder or approving dose and extraction yield.")},
    292: {
        0: ("WITHHOLD", "Source Quaker White Oats is retained as a brand-qualified oatmeal ingredient in JCM50/148 and TOGO M42. Live NCITC29298 instead denotes colloidal oatmeal milled to fine powder. The actual source does not independently establish that processing scope; a synonym cannot bridge it."),
        1: ("WITHHOLD", "The aggregate case includes unqualified Oatmeal with no powder/colloidal preparation evidence, while NCITC29298 explicitly denotes finely milled colloidal oatmeal. Other descriptors saying powdered do not establish every source member's preparation; preserve the complete case pending source-specific resolution.")},
    293: {
        0: ("SUPPORTED", "The TOGO M2407 OADC stock descriptor explicitly names Oleic Acid. The neutral oleic-acid owner matches the named input, not the entire enrichment; the volume-only dose and absent final denominator remain separate."),
        1: ("SUPPORTED", "Both descriptors explicitly name9Z-octadecenoic acid, preserving the cis9 geometry of oleic acid. The owner matches without accepting a different geometric isomer or certifying the molar quantities."),
        2: ("SUPPORTED", "All16 Oleic acid descriptors and complete DSMZ645/911, KOMODO and TOGO OADC source excerpts were inspected. They preserve the named neutral acid; stock composition, volume-only inputs, provider rates and final-medium doses remain separate and receive no new quantity or growth approval.")},
    294: {0: ("SUPPORTED", "All seven Olive oil descriptors preserve the named food oil across NBRC103, JCM188 and MediaDive3848/6326. The generic olive-oil material matches; no purity grade, triglyceride composition, mass-volume conversion or dose is inferred.")},
    295: {0: ("SUPPORTED", "The sole Orotate descriptor retains the bare anion name and KEGGorot context. Live ChEBI30839 confirms the orotate anion distinct from orotic acid. This binds the maintained concept without selecting a salt or approving actual solution protonation or concentration.")},
    296: {0: ("SUPPORTED", "All six Orotic acid descriptors retain the neutral acid, including CAS65-86-1 in Soil Defined Carbon Mix and Northen stocks and CCAP UCM context. The acid owner matches without substituting orotate or approving stock doses.")},
    297: {0: ("SUPPORTED", "All three Orthophosphate descriptors retain the bare orthophosphate name in MediaDB287/37/36. Live ChEBI18367 lists Orthophosphate as the named phosphate-anion concept. Binding this maintained concept does not establish the supplied salt, actual solution protonation, medium pH, or the legacy quantities.")},
    298: {0: ("SUPPORTED", "Both Ox-bile descriptors retain bovine bile material, including MediaDive502. The native MICRO owner explicitly preserves the compositionally variable bile preparation. No fixed chemical composition, specific processing subtype, or amount is inferred.")},
    299: {0: ("SUPPORTED", "Both p-hydroxybenzyl-alcohol descriptors retain the para substitution, independently named in the primary Table2 excerpt for MediaDB466/441. The owner matches that neutral alcohol, without approving inherited dose, entire cobalt-variant composition or growth.")},
    300: {
        0: ("SUPPORTED", "All three 4-Hydroxybenzoate descriptors, including the primary Table2 p-hydroxybenzoate excerpt, preserve the para/4 anion name. The bare-anion concept matches the maintained owner; no supplied salt, neutral acid, solution protonation or dose is inferred."),
        1: ("SUPPORTED", "Both p-Hydroxybenzoate descriptors retain the para-substituted anion label, matching 4-hydroxybenzoate. MediaDive compound332 and the source quantities remain scoped; no counterion is selected.")},
    301: {0: ("SUPPORTED", "Both TOGO M2891/M2887 descriptors name PPLO medium as an opaque complex preparation. The named medium owner matches without inventing composition, concentration basis or growth efficacy.")},
    302: {0: ("SUPPORTED", "The sole TOGO M2179/ATCC2616 descriptor explicitly names Pancreatic Digest of Gelatin (Hardy C6540), matching the product-qualified owner. Binding the named digest does not certify proprietary formulation or interchangeability with every gelatin digest.")},
    303: {
        0: ("SUPPORTED", "The LowMOPS REPLACE event keeps Pantothenate only as the displaced parent. That generic anion label matches the owner; the complete calcium-pantothenate replacement and its pantothenate-basis amount remain separate, with no presence or free-anion form inferred for the replacement."),
        1: ("SUPPORTED", "The Jensen BL REPLACE payload identifies old Pantothenate as context only. Its generic label matches the owner without equating the new calcium salt, approving its amount, or restoring the old material's presence."),
        2: ("WITHHOLD", "The inspected UTEX DAS descriptor retains Sigma P2250, whose manufacturer specification identifies D-pantothenic acid hemicalcium salt. The native owner is generic free pantothenate; the product witness blocks treating the complete case as that ion. Direct manufacturer-page retrieval was unavailable, with indexed primary specification evidence retained in #1515."),
        3: ("SUPPORTED", "The Jensen BL ArgSerTrp REPLACE keeps the old generic Pantothenate descriptor as displaced context. This matches the anion owner without approving the new calcium-salt identity or its pantothenate-basis quantity."),
        4: ("SUPPORTED", "The Jensen BL Arg REPLACE preserves the old Pantothenate label only as context. The generic anion binding is supported; the new calcium preparation, source basis and replacement semantics remain distinct."),
        5: ("SUPPORTED", "The Jensen BL Asp REPLACE retains old Pantothenate as the displaced input. The owner matches that context label without implying presence, calcium-salt equivalence or a concentration conversion.")},
    304: {
        0: ("WITHHOLD", "The complete case contains an embedded D-pantothenic-acid source annotation while its preferred source label and candidate owner are generic pantothenic acid. The unresolved stereo scope is not established by the source amount evidence; quarantine rather than silently discard the conflicting annotation."),
        1: ("WITHHOLD", "All three DL-Pantothenic acid descriptors preserve explicit racemic material, including MediaDive compound1371. The generic CHEBI7916 target and automatic synonym/duplicate history do not independently establish exact racemate scope."),
        2: ("SUPPORTED", "The sole descriptor names generic Pantothenic Acid, matching the generic acid target without selecting an enantiomer or salt. Its 'From DL vitamins' stock-context note is retained and is not interpreted as chemical stereochemistry or approval of the stock formulation.")},
    305: {0: ("SUPPORTED", "All 21 descriptors name Pasteurized Seawater. The reviewed local owner explicitly preserves this heat-treated preparation and does not impose fixed salinity, filtration, or product composition. Source filtration/salinity qualifiers remain visible; this does not equate the preparation with generic seawater or approve quantities.")},
    306: {0: ("SUPPORTED", "All 16 Pectin descriptors and DSMZ1245, MediaDive J145/3792/5688/3791 and P5 source contexts preserve the pectin material family. No polymer distribution, degree of esterification, receiving-medium dose or journal validation is inferred from the stock or user-contributed evidence.")},
    307: {
        0: ("SUPPORTED", "The lowercase penicillin descriptor names the generic penicillin family, consistent with the owner. Its variable amount remains unknown; no particular penicillin, salt or activity-to-mass conversion is selected."),
        1: ("SUPPORTED", "All four Penicillin descriptors preserve the generic antibiotic-family label. TOGO M2887/M154 and JCM163 activity-unit contexts remain explicit. Legacy mass fields inconsistent with activity units are not approved by this identity binding, and no specific penicillin salt is inferred.")},
    308: {0: ("SUPPORTED", "Both Pentachlorophenol descriptors retain the five-chloro phenol identity, including MediaDive compound2115. The neutral owner matches; no phenolate salt or source dose is inferred.")},
    309: {0: ("SUPPORTED", "All four Phenanthrene descriptors retain the same aromatic solute. The NBRC1339 250mM stock in DMSO remains a preparation context; the binding does not equate the entire DMSO stock with pure phenanthrene or validate its receiving dose.")},
    310: {0: ("SUPPORTED", "All five Phenylacetic acid descriptors preserve the neutral acid, including MediaDive1545/5113. The owner's reviewed corrected acid identity matches; the old MIM annotation and amount fields do not select phenylacetate or the constitutional ester phenyl acetate.")},
    311: {0: ("WITHHOLD", "The source descriptor annotates CHEBI18401 phenylacetate (phenylacetic-acid anion), but the native owner is CHEBI8082 phenyl acetate (phenol acetate ester). Live ChEBI definitions confirm distinct connectivity/form. The ambiguous spaced label cannot resolve this conflict; no whitespace-only equivalence is accepted.")},
    312: {0: ("SUPPORTED", "All eight descriptors retain generic Phosphate buffer, including the explicitly unresolved P10 salt proportions. The generic buffer owner matches at that family scope; no fixed formulation, constituent phosphate salts or quantitative basis is invented.")},
    313: {0: ("WITHHOLD", "The source explicitly names MediaDive compound1900 phosphate buffer stock, while the owner has only CultureMech placeholder2 and a preparation-variant distinction from generic phosphate buffer. No independently established formulation/source relation connects this exact stock; the shared name is insufficient.")},
    314: {
        0: ("SUPPORTED", "The complete Tang tracer-with-salt SET_CONCENTRATION event names PIPES, matching the maintained buffer identity. Its study stage and stated20mM remain separate; this is not growth or amount certification."),
        1: ("WITHHOLD", "The Hartzell1999 PIPES mention explicitly retains SOURCE_CLAIM because the primary chapter was unavailable and Reed2001 does not verify this distinct preparation. A plausible PIPES label cannot clear that source-claim gate; preserve the complete held case without promoting occurrence, dose or source identity."),
        2: ("SUPPORTED", "The complete Tang tracer-medium SET_CONCENTRATION event explicitly names PIPES, matching the buffer owner while preserving the study-specific stage and quantity independently."),
        3: ("SUPPORTED", "All 79 base PIPES descriptors and distinct MediaDive/JCM/DSMZ source snippets were inspected. They consistently preserve the named buffer, without inferring a sodium salt, validating stock strengths or approving inferred final volumes."),
        4: ("SUPPORTED", "The complete Tang salt-and-amino-acid tracer event retains PIPES and its separate SET_CONCENTRATION stage. The owner matches identity; other additions and amounts remain independent."),
        5: ("SUPPORTED", "The complete Tang amino-acid tracer event names PIPES. The source-specific concentration-change context is preserved without universalizing the formulation or asserting growth.")},
    315: {
        0: ("SUPPORTED", "The descriptor explicitly names polyethylene glycol over molecular-weight range106–20000. The generic PEG polymer-family owner accommodates the retained range; no single molecular mass, chain length or whole-stock identity is asserted."),
        1: ("SUPPORTED", "Both archived DSMZ296/299 descriptors retain PEG molecular-weight range106–20000 and distinct replacement contexts. Binding the PEG family does not collapse that range to a single molecule or certify the substitutions' growth effects.")},
    316: {0: ("SUPPORTED", "TOGO M2964 names optional Polymyxin B activity-unit stock. The native owner explicitly preserves the B1/B2 mixture and excludes B1-only and sulfate identity; the descriptor states no narrower salt. Its stock/activity and optional context remain unapproved quantities, not mass conversion.")},
    317: {0: ("SUPPORTED", "The sole descriptor names polyvinyl alcohol, matching the generic macromolecule owner. No polymer mass, chain length, degree of hydrolysis or interpretation of the molar dose is inferred.")},
    318: {0: ("SUPPORTED", "Both Porcine serum descriptors preserve the animal species and serum material, matching MICRO0001238. No processing subtype or composition is inferred, and anomalous mass/percentage fields receive no quantity approval.")},
    319: {0: ("WITHHOLD", "The source Potassium descriptors retain explicit K+ annotations, whereas NCITC765 is the elemental/NOS potassium concept (live NCI definition and CAS7440-09-7). The source does not independently resolve the supplied ionic/material form; neither metal nor ion identity is inferred from the generic label.")},
    320: {0: ("WITHHOLD", "Both source descriptors say only Potassium Aspartate. Live NCI C87343 additionally encodes L-aspartate potassium/monopotassium aspartate hemihydrate, CAS7259-25-8. Source solution2115 does not establish those stereochemical or hydration qualifiers.")},
    321: {0: ("SUPPORTED", "All four KF descriptors preserve the potassium-fluoride formula, including JCM1120 and MediaDive5211 compound2005. The corrected canonical potassium-fluoride owner matches; rejected duplicate Kf and provider-derived quantities are not newly adopted.")},
    322: {0: ("WITHHOLD", "The sole source descriptor names Potassium Gluconate without D/L or independent product/CAS evidence, whereas CHEBI32032 carries a D-specific structure. An inherited ontology ID or exact lexical label does not establish the source enantiomer.")},
    323: {
        0: ("SUPPORTED", "The sole capitalized Potato Flour descriptor names the flour material, matching FOODON03302378. No starch-only composition or particular product is inferred."),
        1: ("WITHHOLD", "The case contains a BD220908 descriptor whose preferred label is Potato flour but whose manually assigned term is potato starch FOODON03307543. Other DSMZ354 flour evidence does not establish the BD material independently; retain the concrete flour/starch conflict rather than equate these preparations.")},
    324: {
        0: ("WITHHOLD", "The descriptor label selects Propane-1-ol, but the retained primary Table2 excerpt only says propanol and explicitly does not certify the inherited chemical form. The primary text does not establish the1-isomer over another propanol; preserve that unresolved scope."),
        1: ("WITHHOLD", "Archived DSMZ868 source text states propanol stock without an isomer position. The inherited propan-1-ol annotation cannot independently supply that missing specificity; the complete case remains held.")},
    325: {0: ("SUPPORTED", "Both Propanoate descriptors and primary Table2 excerpts explicitly name propionate. Live ChEBI17272 confirms the same bare-anion concept. No counterion, neutral acid or actual solution protonation is inferred, and quantities remain separate.")},
    326: {
        0: ("SUPPORTED", "All four Proteose peptone no.2 descriptors, including DSMZ1245/403 and MediaDive2474, preserve this numbered peptone preparation. The pinned MICRO recovery in #759 supports the named owner; generic peptone is not substituted and amounts remain scoped."),
        1: ("SUPPORTED", "Both KOMODO1245 descriptors explicitly name Proteose Peptone no.2. They match the numbered preparation owner without approving SEED aggregate composition or quantitative inference."),
        2: ("SUPPORTED", "The sole source names Proteose peptone No2 (DIFCO0121-01-3), a catalog variant retained by the owner and corroborated by DSMZ403 context. No other peptone formulation is treated as interchangeable.")},
    327: {0: ("SUPPORTED", "All three Pullulan descriptors preserve the named polysaccharide, including MediaDive5012 compound1959. No molecular-weight grade, chain-length distribution, mixture composition or dose is inferred.")},
    328: {
        0: ("SUPPORTED", "DSMZ194 explicitly names putrescine replacing sodium propionate for DSM5092. The neutral putrescine owner matches the retained source name; replacement context, concentration and growth remain separate."),
        1: ("WITHHOLD", "Two inspected Putrescine descriptors retain explicit1,4-butanediammonium CHEBI326268 annotations while the native owner is neutral putrescine. The generic source label does not independently resolve this protonation/form conflict, so the complete case is held.")},
    329: {
        0: ("SUPPORTED", "All three pyridoxamine dihydrochloride descriptors retain the two-HCl form, including CAS524-36-7. The dihydrochloride owner matches without substituting monohydrochloride or free pyridoxamine."),
        1: ("SUPPORTED", "The Pyridoxamine・2HCl descriptor explicitly retains two hydrochlorides, matching the dihydrochloride owner independently of its dose."),
        2: ("SUPPORTED", "The spaced Pyridoxamine . 2HCl descriptor retains two hydrochlorides. Punctuation does not change the salt stoichiometry or imply monohydrochloride."),
        3: ("SUPPORTED", "All seven Pyridoxamine Dihydrochloride descriptors and solution3179/3430/2814/3534 excerpts preserve the two-HCl salt. Stock doses and preparation volumes are retained without new quantity approval."),
        4: ("SUPPORTED", "Both CCAP MR_UCM Pyridoxamine.2HCl descriptors explicitly preserve dihydrochloride identity. Their distinct quantities remain separate from the material binding.")},
    330: {
        0: ("SUPPORTED", "Pyridoxamine・HCl explicitly names the one-HCl form, matching CHEBI131531 rather than the separately maintained dihydrochloride."),
        1: ("SUPPORTED", "Both Pyridoxamine-HCl descriptors retain the one-HCl formula. The monohydrochloride owner matches without changing salt stoichiometry or validating doses."),
        2: ("SUPPORTED", "All12 pyridoxamine hydrochloride descriptors and solution3482/2791/2703/5073/1867/4848/2512/926 source excerpts preserve the hydrochloride name. No evidence selects the distinct dihydrochloride; preparation quantities remain independent."),
        3: ("SUPPORTED", "The lowercase pyridoxamine-HCl descriptor preserves the monohydrochloride form; case does not change its salt identity."),
        4: ("SUPPORTED", "Both Pyridoxamine HCl descriptors retain one hydrochloride. Their molar quantities do not authorize substituting dihydrochloride or free base.")},
    331: {0: ("SUPPORTED", "All three Pyromelitic acid descriptors and MediaDive2576/1283 evidence retain the misspelling explicitly resolved by the native owner as pyromellitic acid. Neutral acid identity is preserved; no salt or anhydride is inferred.")},
    332: {0: ("SUPPORTED", "Both descriptors explicitly name pyrrole-2-carboxylic acid, including MediaDive2108. The position2 neutral acid matches the owner; their extreme amount field is not validated by identity review.")},
    333: {
        0: ("SUPPORTED", "The complete Carini2014 aminoethylphosphonic-acid assay event names pyruvate. Live ChEBI15361 supports the bare-anion concept; assay stage,100µM and other nutrient changes remain independent."),
        1: ("SUPPORTED", "The complete Carini2014 phosphoserine-assay SET_CONCENTRATION names pyruvate. The bare-anion owner matches without selecting a supplied salt or certifying100µM/growth."),
        2: ("SUPPORTED", "The complete Carini2014 phosphite-assay event preserves pyruvate as the named anion concept, without converting its stage-specific dose to a universal formulation or inferring a counterion."),
        3: ("SUPPORTED", "The complete Carini2014 glucose6-phosphate assay names pyruvate. The owner matches the bare-anion scope while source dose and phosphorus substitution remain separate."),
        4: ("SUPPORTED", "The complete Carini2014 methylphosphonic-acid assay event names pyruvate, matching the maintained anion concept. No supplied salt or solution-speciation inference follows from the binding."),
        5: ("SUPPORTED", "The complete Carini2014 ribose5-phosphate assay preserves pyruvate and its own concentration stage. The anion-name binding does not approve other ingredients, amounts or growth."),
        6: ("SUPPORTED", "All19 base Pyruvate descriptors and primary Table2/DSMZ1829/650/1521 and stock6374/3148/1378 snippets were inspected. The consistent bare-anion name matches CHEBI15361; supplied salt, neutral acid, stock quantities and actual solution protonation are not inferred."),
        7: ("SUPPORTED", "The complete Carini2013 serine-substitution event names pyruvate at its separate assay stage. The bare-anion owner matches;50µM and methionine stereochemistry remain source-scoped, not new chemical or growth approvals."),
        8: ("SUPPORTED", "The complete Carini2013 glycine-substitution event retains pyruvate and its distinct50µM assay context. Binding the anion label does not infer a salt or certify other formulation claims.")},
    334: {0: ("SUPPORTED", "Both Quinoline descriptors, including MediaDive2107, retain quinoline rather than isoquinoline or a salt. The maintained aromatic heterocycle owner matches the source name.")},
    335: {
        0: ("WITHHOLD", "The source explicitly names sterile defibrinated rabbit blood, including JCM586/70. Native Rabbit blood marks the defibrinated form as only RELATED_SYNONYM; a generic blood identity does not preserve this processed preparation as exact equivalence."),
        1: ("SUPPORTED", "All four unqualified Rabbit blood descriptors retain species-specific blood without a defibrination qualifier. The generic rabbit-blood owner matches this scope; quantities and processing assumptions are not approved.")},
    336: {
        0: ("SUPPORTED", "The lowercase rabbit serum descriptor matches the species-specific serum owner, whose MICRO identity is independently restored from pinned KGX in #759. No processing or concentration interpretation is inferred."),
        1: ("SUPPORTED", "All15 Rabbit serum descriptors were inspected, including DSMZ1829, TOGO M2583 and JCM896 sterile non-hemolyzed young Pel-Freez31125 context. The generic species/serum material is retained with those qualifications visible; the binding does not certify product interchangeability, age, sterilization equivalence or anomalous legacy quantities.")},
    337: {0: ("SUPPORTED", "All six Raffinose descriptors and MediaDive3764/482, DSMZ222 and J124 source excerpts preserve the named trisaccharide. No hydrate, grade or concentration is inferred beyond that named material.")},
    338: {0: ("SUPPORTED", "Both source descriptors say generic Rhamnose. Live CHEBI26546 is a generic family with D and L children, matching the preferred owner and canonical row. The owner's more specific chemical-properties InChI is not accepted as source stereochemical evidence; this binding does not choose L or D.")},
    339: {0: ("WITHHOLD", "The complete case includes a source Ribose descriptor carrying D-ribose CHEBI16988, whereas the canonical owner is generic ribose CHEBI33942 with D/L children. The KOMODO78b.1 source label does not independently resolve whether the narrower annotation represents supplied D material; preserve the conflict rather than silently broaden it.")},
    340: {0: ("SUPPORTED", "JCM364/TOGO M358 explicitly retains rice straw as the input used to prepare plant-residue extract. The rice-straw owner identifies that starting material, not the final soluble extract; extraction ratio and unavailable final concentration remain separate.")},
    341: {0: ("SUPPORTED", "All10 Rifampicin descriptors preserve the named compound across NBRC915/917/918/919/1249/1250 and J1168. Methanol carrier, filter sterilization and stock doses remain explicit preparation context; the entire stock is not equated with pure rifampicin.")},
    342: {0: ("SUPPORTED", "Both Rolled oats descriptors, including MediaDive146 compound188, preserve the rolled cereal preparation. The FOODON material matches without inferring flour, extract, brand or dose equivalence.")},
    343: {0: ("SUPPORTED", "All three RbCl descriptors explicitly preserve rubidium chloride, including P4 stock and CCAP MR_S88. The formula matches the owner; water carrier, stock strength, receiving dose and user-contributed evidence scope remain separate.")},
    344: {
        0: ("SUPPORTED", "All three lowercase rumen-fluid descriptors retain generic fluid, with KOMODO330/119 source labels and no processing qualifier. The generic ruminal-fluid owner matches; provider gram quantities are not conversions from liquid volumes or preparation approvals."),
        1: ("WITHHOLD", "The complete Rumen fluid case includes descriptors explicitly qualified as clarified. Native owner history #114/#204 excludes clarified processed material from this generic ruminal-fluid identity; preserve the preparation distinction rather than erase the notes."),
        2: ("SUPPORTED", "The sole capitalized Rumen Fluid descriptor contains no clarified or other processing qualifier. The generic ruminal-fluid owner matches the named material without approving its quantity.")},
    345: {0: ("SUPPORTED", "Both Rye-bran descriptors and JCM730/MediaDive4657 source rows identify the bran input used for an extract. The rye-bran material owner matches that input without equating it with the completed extract or approving its soluble concentration.")},
    346: {0: ("SUPPORTED", "All three Sake descriptors preserve the named fermented beverage in JCM20/TOGO M13. The FOODON sake material matches without selecting a product, alcohol strength or approving the inconsistent legacy percentage representation.")},
    347: {0: ("SUPPORTED", "Both Salicylate descriptors, including MediaDive2101, retain the bare salicylate anion name. The maintained anion concept matches without inferring salicylic acid, a counterion or actual solution protonation.")},
    348: {0: ("WITHHOLD", "The descriptor identifies MediaDive compound1144 Salt Solution II; the owner originated from ingredient1144 and preserves an otherwise undefined stock under#288. Shared label and numeric suffix do not independently establish namespace correspondence or preparation scope.")},
    349: {0: ("SUPPORTED", "All four Salt water descriptors retain generic saline-water scope, matching ENVO00002010. No fixed salinity, salt composition, natural seawater origin or quantitative interpretation is inferred.")},
    144: {
        0: ("SUPPORTED", "The complete DSM9467 REMOVE event names FeSO4 x 7 H2O. The heptahydrate owner preserves the removed material's explicit hydration and iron(II) scope; this context-only binding does not assert presence in current DSMZ670."),
        1: ("SUPPORTED", "Both FeSO4 7H2O descriptors explicitly retain seven waters and match iron(II) sulfate heptahydrate. No anhydrous or different-hydrate identity is inferred."),
        2: ("SUPPORTED", "Both spaced FeSO4·7H2O descriptors preserve the seven-water iron(II) sulfate formula and fit the maintained heptahydrate owner without approving their amounts."),
        3: ("SUPPORTED", "All 96 FeSO4·7H2O descriptors were read with their distinct notes and evidence. The literal sulfate formula consistently retains seven waters, matching the owner; preparation stocks, provider quantities and source qualifications remain separate."),
        4: ("SUPPORTED", "The complete NBRC1002 heterotrophic ADD explicitly names ferrous sulfate heptahydrate at its stated preparation stage. The binding preserves that material and does not combine its dose with the autotrophic alternative."),
        5: ("SUPPORTED", "All nine FeSO4.7H2O descriptors retain explicit heptahydrate stoichiometry. The punctuation variation does not change the iron(II) sulfate material; amount evidence remains outside identity approval."),
        6: ("SUPPORTED", "All 788 distinct FeSO4 x 7 H2O descriptors were inspected through reconstruction-verified field/text factoring, including every source qualifier and evidence text. The formula and retained primary snippets consistently identify the heptahydrate solute. Acid carriers, trace stocks, zero or variable doses, withdrawn denominators and historical duplicate sums are retained without approving quantities, final-volume inference, growth, or equivalence of the whole prepared solution to pure heptahydrate."),
        7: ("SUPPORTED", "All 24 FeSO4 x 7H2O descriptors retain seven waters across CCAP, JCM and TOGO source contexts. The spacing difference preserves heptahydrate identity; source preparation and quantities remain scoped."),
        8: ("SUPPORTED", "All 12 spaced FeSO4.7H2O descriptors preserve the seven-water sulfate formula. The maintained owner matches the named solute without selecting another hydrate or certifying stock dilution."),
        9: ("SUPPORTED", "The complete NBRC1002 autotrophic ADD names ferrous sulfate heptahydrate and retains its distinct 13.9g/L preparation context. The identity matches the owner without mixing it with the heterotrophic route or approving growth."),
        10: ("SUPPORTED", "The complete DSM9463 REMOVE explicitly names FeSO4 x 7 H2O. Matching the heptahydrate owner preserves removed/context-only status and does not restore the ingredient to the current DSMZ670 variant."),
        11: ("SUPPORTED", "The complete DSM9466 REMOVE retains the seven-water ferrous sulfate descriptor. Its heptahydrate identity is supported solely as removed context; current variant presence is not inferred."),
        12: ("SUPPORTED", "All 108 FeSO4・7H2O descriptors and their distinct TOGO/JCM source payloads were inspected. The seven-water material is consistent, including acidified and trace-stock preparations. Batch masses, stated stock strengths and final-medium denominators remain distinct and are not newly certified."),
        13: ("SUPPORTED", "The complete M. sedula transcriptomic iron-arm ADD explicitly names FeSO4·7H2O. The owner matches that heptahydrate while the two-of-four-cultures study context is preserved; no universal addition, pyrite equivalence or growth guarantee is asserted."),
        14: ("SUPPORTED", "All 30 Iron(II) sulfate heptahydrate descriptors retain the explicit oxidation state and seven-water form, including CAS7782-63-0 and Wolfe/Planctomyces/UW stocks. Identity matches without merging prepared solutions or approving their quantities."),
        15: ("SUPPORTED", "All 14 Ferrous sulfate heptahydrate descriptors were read, including the primary MEDIADB4–15 formulation and the separately scoped 1000X stock. Explicit FeSO4·7H2O supports the maintained heptahydrate; the rejected historical anhydrous annotation and source amounts are not silently adopted."),
        16: ("SUPPORTED", "All 13 FeSO4 x 7 H2O descriptors with extra formula spacing preserve seven waters, including MediaDive3223/6200 compound1418. The owner matches material identity without treating whitespace or provider rates as a new form."),
        17: ("SUPPORTED", "The complete DSM9468 ADD explicitly names FeSO4 x 7 H2O in the current DSMZ670 acidified stock. The binding identifies the heptahydrate solute and preserves 40%w/v stock, acid carrier, filtration and receiving-dose context without equating the whole stock to pure material or deriving a final concentration.")},
    191: {0: ("SUPPORTED", "All 68 descriptors retain KOH/potassium hydroxide, with explicit JCM1219/929, UTEX, TOGO, DSMZ and MediaDive source snippets. The owner matches the named solute/titrant; reagent strengths, null or variable doses, pH endpoints and stock stages remain distinct and are not new quantitative approvals or claims that a KOH solution equals pure KOH.")},
    122: {
        0: ("WITHHOLD", "All five descriptors explicitly name DL-methionine. The owner retains DL but its exact target is an unspecified methionine parent with D/L children; mechanical synonym regrading in #317 does not resolve racemate-material scope."),
        1: ("WITHHOLD", "The phosphite-assay REPLACE retains DL-methionine only as the displaced parent. Its exact native target lacks an independently established racemate scope; the source's new unspecified methionine is not certified as DL or present under this old descriptor."),
        2: ("WITHHOLD", "The phosphoserine-assay REPLACE preserves displaced-parent DL-methionine context. The unresolved native racemate-to-unspecified target cannot be approved by an inherited synonym; the new source methionine remains unspecified."),
        3: ("WITHHOLD", "The methylphosphonic-acid assay retains DL-methionine solely as the old REPLACE descriptor. The native exact row has unresolved racemate scope; neither presence nor the new methionine's stereochemistry is inferred."),
        4: ("WITHHOLD", "The glucose-6-phosphate assay's displaced DL-methionine is context only. Its exact binding to the unspecified target remains unresolved independently of the complete source's new generic methionine dose."),
        5: ("WITHHOLD", "The serine-substitution assay explicitly replaces imported DL-methionine with unspecified methionine. The old descriptor's native racemate scope remains unresolved and is withheld without changing replacement semantics or claiming presence."),
        6: ("WITHHOLD", "All three DL-Methionine descriptors, including MediaDive2609 compound1162, retain explicit racemic material. The candidate exact target has unspecified stereochemistry; its synonym/CAS and mechanical #317 regrade do not independently establish exact racemate scope."),
        7: ("WITHHOLD", "The glycine-substitution assay keeps DL-methionine only as the displaced imported parent. Its unresolved exact racemate-to-parent binding is withheld; the source's new methionine remains stereochemically unspecified."),
        8: ("WITHHOLD", "The aminoethylphosphonic-acid assay retains the old DL-methionine in a complete REPLACE event. The unresolved native material scope blocks the binding while preserving context-only status and the source's unspecified replacement."),
        9: ("WITHHOLD", "The ribose-5-phosphate assay's old DL-methionine descriptor has unresolved racemate-to-unspecified exact scope. This hold preserves the replacement context and does not approve DL identity for the new methionine.")},
    120: {
        0: ("SUPPORTED", "All three DL-6,8-thioctic acid descriptors retain the racemic acid scope explicitly established by owner curation #454. This does not select an isolated enantiomer or validate stock doses."),
        1: ("SUPPORTED", "All 156 Lipoic acid descriptors and their retained MediaDive, JCM, TOGO, DSMZ and KOMODO evidence were inspected. Their generic acid labels and CAS1077-28-7 fit the owner's independently curated generic/racemic acid scope in #454; stock quantities, calculations and preparation volumes remain unapproved context."),
        2: ("SUPPORTED", "All four alpha-lipoic acid descriptors retain the acid without an R/S-only source qualifier. The established generic/racemic owner scope in #454 applies; inherited stereospecific annotations are not used to infer source chirality."),
        3: ("SUPPORTED", "All four DL-alpha-lipoic acid descriptors explicitly preserve the racemate. The owner's curated generic/racemic acid scope supports the binding without selecting R or S material."),
        4: ("WITHHOLD", "The six descriptors explicitly name Lipoate and retain KEGG lipoate context, while the candidate is neutral lipoic acid. Existing #1376 documents this charge/form conflict; the #454 racemate decision does not authorize acid/anion equivalence."),
        5: ("SUPPORTED", "Both Thioctic Acid descriptors retain the generic acid. Their old R-specific annotations are rejected as source-identity evidence under the owner's explicit #454 generic/racemic correction; no R form is inferred."),
        6: ("SUPPORTED", "Both lowercase lipoic acid descriptors match the independently curated generic/racemic acid owner. They supply no different salt, charge or isolated-enantiomer claim."),
        7: ("SUPPORTED", "The complete Nordkvist REMOVE event and descriptor explicitly name dl-6,8-thioctic acid, matching the curated racemic acid scope. The binding preserves removed/context-only status and does not imply presence, acetate equivalence or concentration approval."),
        8: ("SUPPORTED", "All 11 Thioctic acid descriptors retain the generic acid source label. Old R-specific annotations do not override the literal source; #454 establishes the owner's generic/racemic scope without promoting an isolated enantiomer."),
        9: ("SUPPORTED", "The sole D,L-6,8-Thioctic Acid descriptor explicitly states the racemate. Its old S-specific annotation is rejected under #454; the maintained generic/racemic acid owner preserves the source material."),
        10: ("SUPPORTED", "The sole alpha-lipoic acid descriptor does not state an isolated enantiomer. Its inherited S annotation is not source evidence; the independently curated generic/racemic acid scope applies."),
        11: ("SUPPORTED", "The alpha--Lipoic acid source label denotes the acid without an isolated-enantiomer qualifier. The legacy S annotation is rejected under the documented #454 correction; no salt or source chirality is invented."),
        12: ("SUPPORTED", "All 18 (DL)-alpha-Lipoic acid descriptors explicitly preserve DL/racemic material and fit the owner's reviewed generic/racemic acid scope. Their preparation stages and doses are retained without new quantitative approval.")},
    119: {
        0: ("WITHHOLD", "Source 2-Methyl-butyric acid omits stereochemistry, whereas the native owner explicitly names DL material. The unspecified external target does not resolve this source-to-owner scope ambiguity."),
        1: ("WITHHOLD", "The alpha-Methylbutyric acid source labels and JCM266 excerpts do not establish a racemic preparation. The DL preferred owner and unspecified target require an independent scope resolution."),
        2: ("WITHHOLD", "KOMODO829 and stock2027 name generic 2-methylbutyric acid. They do not support narrowing to the owner's explicit DL material; provider quantities supply no stereochemical evidence."),
        3: ("WITHHOLD", "The source explicitly names DL-alpha-Methyl butyric acid, including JCM1029/stock3774. Although the owner name retains DL, its exact CHEBI37070 target is stereochemically unspecified without an established racemate-scope decision."),
        4: ("WITHHOLD", "KOMODO1245 explicitly retains generic 2-Methylbutyric Acid without a racemic qualifier. The DL owner cannot supply that missing specificity; null amounts are unrelated to identity."),
        5: ("WITHHOLD", "All16 descriptors retain explicit DL-2-Methylbutyric acid, including original DSMZ119/161/330/323 and JCM1203. The native preferred name matches, but the exact external row points to an unspecified parent with R/S children and no demonstrated racemate scope. Preserve the DL distinction pending owner resolution."),
        6: ("WITHHOLD", "The source explicitly names DL-2-Methyl butyric acid. Its racemic qualifier is not established as exact identity to the unspecified CHEBI37070 target merely by the native synonym or automated duplicate merge."),
        7: ("WITHHOLD", "TOGO M258 and JCM266 name alpha-Methylbutyric acid without a DL qualifier. The native racemic preferred name adds specificity which the source and stock dose do not establish."),
        8: ("WITHHOLD", "The inspected MediaDive480 and KOMODO279/532 descriptors explicitly name generic 2-Methylbutyric acid. The owner is DL-labelled; this concrete stereochemical scope ambiguity quarantines the complete case without attesting the remaining uninspected descriptors."),
        9: ("WITHHOLD", "MEDIADB473/474 name generic 2-methylbutanoic acid and explicitly leave chemical-form validation outside their amount evidence. They do not establish the DL material named by the owner.")},
    181: {
        0: ("SUPPORTED", "The sole descriptor names 3-Methyl-butyric acid, matching the isovaleric-acid owner's branch position and neutral acid scope."),
        1: ("SUPPORTED", "All24 iso-Valeric acid descriptors preserve the neutral acid identity, including DSMZ330/1006/212a, JCM1203/1029 and stock6552/608/3774. The legacy MediaIngredientMech000378 annotation does not change source form; dilution, density and quantity claims remain unapproved context."),
        2: ("SUPPORTED", "All five 3-Methylbutyric acid descriptors match the isovaleric-acid owner; DSMZ829/829b, TOGO M2587 and MediaDive4008/1680 retain the same branch and acid wording. No final-volume inference is approved."),
        3: ("WITHHOLD", "The database names 3-Methylbutanoic acid, but the inspected primary Table2 evidence explicitly names isovalerate and declines to certify ionization or supplied salt. Binding the complete case to neutral isovaleric acid would ignore this unresolved primary/database form conflict."),
        4: ("SUPPORTED", "Both KOMODO1245 descriptors explicitly name Isovaleric Acid, matching the neutral branched acid owner while their null quantities remain unknown."),
        5: ("SUPPORTED", "All53 Isovaleric acid descriptors retain the neutral acid name, with CAS503-74-2 and JCM266/675, DSMZ119/161/436/1245 and stock source excerpts. No different branch, salt or ion is substituted, and quantity calculations and stage-specific preparation volumes remain separate."),
        6: ("SUPPORTED", "All four lowercase 3-methylbutyric acid descriptors retain the branched neutral acid in KOMODO829 variants and standalone2027. The owner matches identity without approving provider rates or stock dilution.")},
    136: {
        0: ("SUPPORTED", "All85 descriptors preserve ferric ammonium citrate, including DSMZ911/857 and MediaDive/JCM stocks. The generic ferric-ammonium-citrate owner matches the supplied compound name without inferring a definite complex stoichiometry, hydrate or concentration."),
        1: ("SUPPORTED", "All15 descriptors name ammonium ferric citrate, including solution5349/5102/5237/5411 evidence. Reversed word order preserves the same ammonium-containing iron(III) citrate scope; no fixed stoichiometry or dose is asserted."),
        2: ("SUPPORTED", "All25 descriptors and their source snippets explicitly name Fe(NH4)citrate, retaining ammonium. This literal formula supports the ferric-ammonium-citrate owner. Secondary CHEBI:144421 iron(III)citrate annotations are expressly rejected as conflicting identity evidence and tracked in #1491; no source bytes or quantities are changed."),
        3: ("SUPPORTED", "The sole ferric ammmonium citrate descriptor retains the complete ammonium-containing name despite its extra m; the maintained alias matches the ferric-ammonium-citrate owner without selecting another iron citrate."),
        4: ("SUPPORTED", "All10 descriptors preserve Ferric Ammonium Citrate, including exact TOGO M2403/2404/2402/2397/2400/2401/2407 table inputs and UTEX stocks. The binding retains this compound scope and does not approve unverified mass denominators or molar stock calculations."),
        5: ("SUPPORTED", "The complete DSMZ645 alternative-preparation ADD explicitly names ferric ammonium citrate. Its owner matches the material name while the 0.04g batch input and from-scratch stage remain independent source context; no hydration or stoichiometry is invented.")},
    180: {
        0: ("SUPPORTED", "Both KOMODO1245 source descriptors explicitly name Isobutyric Acid; their null amounts remain unknown. The neutral branched acid owner matches the source label without inferring a salt or dose."),
        1: ("SUPPORTED", "All61 descriptors explicitly name Isobutyric acid, including CAS79-31-2, JCM266/675, DSMZ119/161/829/1245 and source-bound fatty-acid-stock inputs. The neutral acid owner matches identity; the different preparation volumes, provider rates and missing amounts remain unapproved quantity context."),
        2: ("WITHHOLD", "All four source descriptors name 2-Methylpropanoate or isobutyrate, whereas the candidate owner is neutral isobutyric acid. The source evidence explicitly leaves ionization and supplied salt unvalidated; an exact alias cannot justify acid/anion equivalence."),
        3: ("SUPPORTED", "All23 iso-Butyric acid descriptors preserve the same branched neutral acid, with DSMZ330/1006/212a and JCM1203/1029 preparation contexts retained. Binding identity does not validate provider-derived density conversions, missing amounts or final-stock volumes."),
        4: ("SUPPORTED", "All four lowercase isobutyric acid descriptors explicitly retain the acid in KOMODO829 variants and standalone stock2027. The same acid owner is supported while provider quantity scope remains separate.")},
    202: {
        0: ("SUPPORTED", "The complete REPLACE payload explicitly identifies L-Serine only as the displaced local-parent descriptor; the new source Serine intentionally lacks stereochemistry. Binding the old L descriptor preserves context-only status and does not confer L specificity on the new assay ingredient."),
        1: ("SUPPORTED", "All42 descriptors identify L-Serine, including CAS56-45-1, KEGG ser-L, MediaDB289 and the retained MediaDive/KOMODO source snippets. The L-specific owner matches the source labels; unknown quantities and stock stages remain unchanged."),
        2: ("SUPPORTED", "Both L-Serin descriptors, including solution5565 compound162, retain the L qualifier. This spelling variant matches the L-serine owner without selecting a salt or racemate.")},
    195: {0: ("SUPPORTED", "All44 descriptors explicitly identify L-Arginine, including CAS74-79-3, KEGG arg-L, ATCC2746 stock, J1045 and solution3065/5286/5184/5105. The free L-amino-acid owner matches the stated form; no hydrochloride, racemate or inferred stock mixture is substituted.")},
    193: {
        0: ("SUPPORTED", "All31 descriptors explicitly identify L-Alanine, with CAS56-41-7, KEGG ala-L, P5 MEM, MediaDB289 and solution994/5184/3065 supporting the retained L label. Stock and unavailable-quantity contexts stay separate; no racemate is inferred."),
        1: ("WITHHOLD", "The source descriptors say only Alanine, without independent stereochemical evidence. An inherited L-alanine annotation and owner synonym cannot establish L specificity for these sources; withhold the complete case rather than infer biological chirality.")},
    198: {
        0: ("SUPPORTED", "The descriptor explicitly names L-cystine, matching the oxidized L-cysteine disulfide owner and preserving its stereochemistry."),
        1: ("SUPPORTED", "All12 descriptors explicitly name L-Cystine, including J460/J14/153 and solution4207/4281/3635/268/4004. The owner preserves the L disulfide identity, not reduced cysteine or an unspecified stereoisomer; dose context is unchanged.")},
    199: {
        2: ("SUPPORTED", "All45 descriptors explicitly name L-Glutamine, with CAS56-85-9, KEGG gln-L, P5 single-stock and DSMZ403/1670 source context. The L amino-acid owner preserves identity; no generic-glutamine stereochemistry is inferred from these separate L-labelled sources and stock quantities remain unapproved context."),
        0: ("WITHHOLD", "Tang's AA-S-18 exclusion names only glutamine and explicitly leaves local stereochemical terms uncertified. The L-glutamine owner adds unsupported stereochemistry. The operation hold remains intact; no whole-medium removal or absence is inferred."),
        1: ("WITHHOLD", "The salt-and-amino-acid variant retains the same generic glutamine exclusion without stereochemical evidence. Binding to L-glutamine would narrow the source; the source's OPERATION hold is preserved."),
        3: ("WITHHOLD", "The inspected descriptors name generic Glutamine, including DSMZ1311; no independent source CAS or L qualifier resolves stereochemistry. An inherited L-specific annotation or synonym is not evidence for narrowing the complete case to L-glutamine."),
        4: ("SUPPORTED", "The sole descriptor explicitly names L-glutamine, matching the L-specific amino-acid owner without selecting glutamate or a salt.")},
    156: {
        0: ("SUPPORTED", "All six descriptors identify gelatin/gelatine, including DSMZ403 and solution820/2964. The maintained class-level gelatin owner preserves the undefined material; the stock solute is distinct from its water preparation and no animal origin is inferred."),
        1: ("SUPPORTED", "All three descriptors name gelatin. TOGO M194 retains gelatin inside the stock composition with an unspecified percentage basis; binding the gelatin material does not approve its stock strength or equate it with the entire stock."),
        2: ("SUPPORTED", "All five descriptors identify gelatin, including JCM173, TOGO M2410 Difco and J201 stock evidence. Vendor context is retained without inferring animal source or preparation equivalence; percentage bases remain explicitly unspecified."),
        3: ("SUPPORTED", "The sole lowercase gelatine descriptor is the British spelling of gelatin, matching the maintained material-class owner without narrowing grade or source species.")},
    182: {
        0: ("SUPPORTED", "The source names Isovitalex, matching the maintained local named enrichment preparation. Its multicomponent formulation is not collapsed to an individual substance."),
        1: ("SUPPORTED", "TOGO M2975 explicitly names BD Biosciences IsoVitaleX, matching the owner's retained manufacturer/product variant. The preparation is preserved without inventing its composition or equating its dose to another formulation."),
        2: ("SUPPORTED", "Both descriptors identify the named Isovitalex preparation, including compound977. The local preparation owner preserves that scope; the discordant quantity representations are not approved."),
        3: ("SUPPORTED", "The source explicitly gives IsoVitaleX BD211876, and the maintained owner retains that catalogue variant. The binding identifies the named supplement while preserving the source product detail and does not claim universal product interchangeability.")},
    158: {
        0: ("SUPPORTED", "All14 descriptors identify glutathione/GSH, including KEGG gthrd and J595/solution4443/5570. The maintained reduced-glutathione owner preserves that compound; no oxidized disulfide form is stated."),
        1: ("SUPPORTED", "Both descriptors explicitly name L-Glutathione, consistent with the canonical reduced L-glutathione owner and its separately documented duplicate-owner resolution. No oxidized form is introduced."),
        2: ("SUPPORTED", "Both KOMODO78b variants name glutathione and match the maintained GSH material scope. Their differing final-component quantities are retained without new dose approval."),
        3: ("SUPPORTED", "Both descriptors explicitly name L-glutathione reduced and retain CAS70-18-8. This supports the canonical GSH owner under its explicit #260 identity clarification, without converting the source to oxidized glutathione.")},
    172: {
        0: ("SUPPORTED", "The source explicitly names horse blood without a more specific processing state. The MICRO horse-blood owner preserves species identity and does not infer defibrination or a serum preparation."),
        1: ("SUPPORTED", "The REPLACE event retains horse blood solely as the displaced parent descriptor, matching the horse-blood owner. Sheep blood is the new ingredient; source quantity disagreement stays unresolved and this context-only binding is not presence."),
        2: ("WITHHOLD", "The JCM1099 source explicitly requires sterile defibrinated horse blood, whereas the candidate owner is generic horse blood. The preparation qualifier is source-supported and cannot be erased by the generic preferred label; this complete case remains held for a preparation-specific binding.")},
    204: {
        0: ("SUPPORTED", "TOGO M2287 explicitly names lactalbumin hydrolysate in the basal formulation before serum supplementation. The undefined-mixture owner matches that material without inferring casein hydrolysate or final diluted quantity."),
        1: ("SUPPORTED", "The DSMZ1021 replacement explicitly retains lactalbumin hydrolysate as the displaced Solution A input. Binding its identity does not mark it present in the casein alternative or approve both hydrolysates together."),
        2: ("SUPPORTED", "Both descriptors and DSMZ1021/solution2074 evidence identify lactalbumin hydrolysate, retaining the casein alternative separately. The owner denotes the same hydrolysate mixture; stock batch and concentration contexts are not independently approved.")},
    196: {
        0: ("SUPPORTED", "The descriptor explicitly names L-ascorbic acid, matching the L-specific acid owner without inferring a salt or another stereoisomer."),
        1: ("SUPPORTED", "All17 descriptors preserve L-Ascorbic acid, including JCM210/179 vitamin stocks and solution5932/5351/5185/1535 excerpts. Stock solute identity is supported; concentrations, dilution and efficacy remain source context, with no salt or D-form inference.")},
    201: {
        0: ("SUPPORTED", "All eight descriptors explicitly retain L-Rhamnose, including P5 single-stock and solution3069/1001 sources. The owner preserves L stereochemistry without selecting an anomer, hydrate or carrier mixture."),
        1: ("SUPPORTED", "TOGO M2313 explicitly names L-rhamnose as an alternative carbon source. The L-rhamnose owner matches identity; the alternative is not asserted to be present together with other substrates.")},
    163: {0: ("SUPPORTED", "All12 descriptors identify guanine, including CAS73-40-5 across Soil Defined Carbon Mix, Northen and NLDM sources and KEGG gua. The nucleobase owner preserves that identity without confusing guanosine or approving the various dose fields.")},
    165: {
        0: ("SUPPORTED", "All15 descriptors explicitly identify H2SeO3/selenous acid, including solution3223/4194/2300, UTEX Sigma211176 and P4 stock-solute evidence. The owner preserves the acid rather than a selenite salt; preparation and concentration contexts stay separate."),
        1: ("SUPPORTED", "The Planctomyces trace-element descriptor names selenous acid with CAS7783-00-8, matching the H2SeO3 owner. No selenium salt or different oxidation state is inferred.")},
    192: {
        0: ("SUPPORTED", "The source explicitly names potassium thiocyanate, matching the KSCN salt owner. No free thiocyanate or other counterion is substituted."),
        1: ("SUPPORTED", "All nine KSCN descriptors retain the potassium thiocyanate salt, including JCM310, MediaDive805 and solution1636. Stock contexts and anomalous percentage representations do not change identity or receive quantity approval.")},
    109: {
        0: ("SUPPORTED", "The replacement's inspected DSMZ693 and BacDive14567 snippets both identify defibrinated sheep blood, matching the specific MICRO preparation owner. Horse blood remains the displaced descriptor; conflicting 5% and 50g/L quantities are not approved by this identity binding."),
        1: ("SUPPORTED", "The source explicitly names defibrinated sheep blood and the owner denotes that preparation, rather than generic blood or untreated sheep blood. The stated 5% w/v remains source occurrence context, not a new quantity approval."),
        2: ("SUPPORTED", "This named claim holds QUANTITY only and explicitly states that sheep-blood identity is supported separately. The defibrinated sheep-blood owner fits the source label; retaining its identity does not promote the held claim or choose between DSMZ5% and BacDive50g/L."),
        3: ("SUPPORTED", "All nine inspected descriptors explicitly name defibrinated sheep blood; generic UBERON blood annotations do not erase that preparation/species wording. The specific MICRO owner preserves it. Concentration variation, including the unexplained 47.619% representation, is not validated by this source-identity binding."),
    },
    110: {
        0: ("SUPPORTED", "All four Dextrin descriptors and inspected MediaDive658/solution1389 snippets denote dextrin, consistent with the owner's dextrin scope. No product grade, different polymer or form is asserted; stock versus main-recipe quantities remain attached to their source contexts."),
        1: ("SUPPORTED", "Both lowercase dextrin descriptors retain the same generic dextrin material; the P2 source explicitly names dextrin. Different 0.1 and 0.5g/L inputs do not imply a different identity or validate growth/quantity claims."),
    },
    111: {0: ("SUPPORTED", "The five descriptors consistently name diaminopimelic acid, with MediaDive118/5575 excerpts and existing 2,6-diaminopimelic-acid annotations. The owner also leaves stereochemistry unspecified; this does not select a meso or D/L isomer.")},
    112: {0: ("WITHHOLD", "The source descriptor and concentration evidence name only diammonium tartrate. The owner's CHEBI:63075 target is diammonium L-tartrate, a stereochemical narrowing unsupported by the inspected source. A synonym lookup and inherited resolved identifier cannot establish the L form.")},
    113: {0: ("SUPPORTED", "All three inspected descriptors explicitly denote dibenzofuran and agree with the owner's unsubstituted dibenzofuran structure. Source quantities differ but no substituted congener, mixture or form conflict is present.")},
    114: {0: ("SUPPORTED", "Both source descriptors name diethyl phosphonate, matching the specific owner and retained MediaDive2089 compound label. The 100%v/v versus100g/L representations are not equated or approved by the identity binding.")},
    115: {0: ("SUPPORTED", "Both source descriptors explicitly specify digested serum, matching the MICRO digested-serum preparation. The generic serum annotation is broader ancillary context; the source preparation remains digested, with no animal species or digestion protocol inferred.")},
    116: {
        0: ("SUPPORTED", "Both NBRC1339/TOGO M2041 descriptors explicitly identify DMSO as the phenanthrene-stock solvent. Binding to dimethyl sulfoxide preserves the solvent identity without promoting phenanthrene's250mM stock strength to a DMSO concentration."),
        1: ("SUPPORTED", "All five descriptors explicitly name dimethyl sulfoxide and preserve its matching formula/identity. Their different dose fields, including1000%v/v, remain unvalidated source quantities; they do not justify a prepared-mixture identity or alter DMSO's material scope."),
    },
    117: {
        0: ("SUPPORTED", "Both Na-oxalate descriptors identify the sodium oxalate salt; the MediaDive850 snippet retains that label and the owner explicitly records Na-oxalate as an alias for disodium oxalate. No hydrogen-oxalate, hydrate or alternative counterion is stated."),
        1: ("SUPPORTED", "All five descriptors and MediaDive J1262/J1263/5402/5403 excerpts explicitly identify disodium oxalate, matching the sodium-oxalate owner's two-sodium formula. No hydrate or other salt is inferred from the concentration evidence."),
    },
    121: {0: ("SUPPORTED", "Both descriptors explicitly name DL-carnitine, including the MediaDive3068 compound1351 excerpt. This matches the owner's DL material scope without selecting an isolated L/D enantiomer or validating the reported dose.")},
    123: {0: ("SUPPORTED", "All five descriptors explicitly identify DL-mevalonic acid; the J21/93/163/3644 source excerpts retain DL. The owner preserves that acid/racemate scope, rather than mevalonolactone or an isolated enantiomer. The secondary label typo does not override the source form.")},
    124: {0: ("SUPPORTED", "The sole descriptor explicitly names Dried Bovine Hemoglobin (BD212392), matching the specific product-labelled owner. Bovine origin, dried preparation and catalogue detail remain attached; this does not claim interchangeability with other hemoglobin products.")},
    125: {
        0: ("SUPPORTED", "Both descriptors explicitly name dry cow-manure, including the MediaDive657 extraction starting material. Binding preserves the dry manure input; it does not equate manure with the resulting filtered extract or approve extraction yield."),
        1: ("WITHHOLD", "The MediaDive3932 compound1707 descriptor states only Cow manure and does not establish drying, whereas the candidate owner specifically denotes dry cow-manure. Another descriptor explicitly says dry, but cannot supply the missing preparation state for this distinct source. The complete case remains withheld."),
    },
    126: {0: ("SUPPORTED", "All six descriptors identify ectoine; the NLDM notes retain CAS96702-03-3 and the paper excerpts distinguish ectoine from hydroxyectoine alternatives. The binding does not select hydroxyectoine, combine alternative substrates or newly validate concentrations/growth.")},
    127: {
        0: ("SUPPORTED", "All 129 EDTA descriptors were inspected, including CAS60-00-4, UTEX explicit acid-form, MediaDive and primary MediaDB source excerpts. The owner's explicit #319/#320 free-acid scope resolves plain EDTA separately from sodium salts and specific anions. Its stale charge-specific chemical-properties fields are not relied on; quantity aggregation, final volume and stock calculations remain unapproved context."),
        1: ("SUPPORTED", "The UTEX stock source explicitly says EDTA, acid form, and preserves the 50g/1L source context and CHEBI4735 free-acid formula. The owner is explicitly curated as the free acid; this does not authorize an EDTA anion or sodium-salt substitution.")},
    128: {
        0: ("SUPPORTED", "All three descriptors explicitly name erythromycin, including the TOGO M2490 antibiotic. One carries generic Solution/Complex-component metadata but no carrier, salt or distinct formulation claim; this binding identifies the named antimicrobial only, not an inferred stock composition or its dose."),
        1: ("SUPPORTED", "Both descriptors name erythromycin, including MediaDive470 compound315. No salt, ester or different antibiotic is stated; the retained dose remains context rather than a fresh quantity or efficacy approval.")},
    129: {0: ("SUPPORTED", "The sole source descriptor explicitly names ethyl octanoate, matching the ester owner. No octanoic acid, other ester or mixture is inferred from the 10mM dose context.")},
    130: {0: ("SUPPORTED", "JCM1380 explicitly names Eugon agar (BD-Difco), matching the product-labelled Eugon-agar owner. Manufacturer detail and medium formulation scope remain retained; this is not generic agar identity.")},
    131: {0: ("SUPPORTED", "NBRC220 explicitly identifies farm soil as the starting material for soil extract. The farm-soil owner matches that input; the binding does not equate soil with the resulting extract or infer a farm location/composition.")},
    132: {0: ("SUPPORTED", "Both descriptors explicitly name Fe(III)PO4 x4H2O, including MediaDive5554 compound179. The ferric phosphate tetrahydrate owner preserves oxidation state and four waters; no anhydrous phosphate collapse is authorized.")},
    133: {
        0: ("SUPPORTED", "All16 descriptors retain FeCl2/iron dichloride identity. Explicit JCM1162 and TOGO M1137 stock contexts describe FeCl2 as the stock solute; no hydrate or ferric chloride is stated. Stock concentrations and volume percentages are not approved as final-medium quantities."),
        1: ("SUPPORTED", "All three descriptors name ferrous chloride, matching the Fe(II) chloride owner. No hydrate or Fe(III) salt is introduced; the millimolar dose differences remain occurrence context."),
    },
    134: {0: ("SUPPORTED", "All three descriptors retain the literal FeCl2 x7H2O source, including MediaDive1938 compound840. The owner uses a distinct local identifier and only closeMatch to anhydrous FeCl2, preserving the unresolved stated hydrate rather than claiming CHEBI30812 exact identity or correcting seven waters silently.")},
    135: {0: ("SUPPORTED", "All three descriptors explicitly name FePO4, including MediaDive2723 compound1200. This matches ferric phosphate without a stated hydrate; no tetrahydrate or ferrous-phosphate substitution is inferred.")},
    137: {0: ("SUPPORTED", "All four descriptors explicitly identify ferric citrate monohydrate, including MediaDive3116/3238 compound2378. The owner preserves Fe(III) and one water; neither anhydrous citrate nor the historically corrected cadmium identifier is approved.")},
    138: {0: ("SUPPORTED", "The source explicitly identifies Fe3+ with a KEGG fe3 cross-reference. The ferric-ion owner preserves charge +3; the binding does not infer a supplied chloride/sulfate salt or elemental iron.")},
    139: {0: ("SUPPORTED", "The sole descriptor explicitly names ferric nitrilotriacetate, matching the Fe(III) nitrilotriacetate complex owner. No free iron ion, NTA acid alone or different oxidation state is substituted.")},
    140: {0: ("WITHHOLD", "The four source descriptors state only ferrous citrate, including MediaDive4437 compound1816. The canonical target is specifically monoferrous acid citrate; neither the source labels nor the concentration excerpt establish that protonation/stoichiometric form. Name normalization alone cannot authorize that narrowing.")},
    141: {0: ("SUPPORTED", "All three MediaDB37/36/287 source descriptors explicitly name Fe2+, matching the ferrous-ion owner. No supplied salt or elemental iron is inferred, and the dose values remain source context.")},
    142: {0: ("WITHHOLD", "The source only identifies ferrous ammonium sulfate; MediaDB474 evidence explicitly leaves supplied hydrate form unvalidated. The owner's CHEBI76243 target is anhydrous, an unstated source-form restriction. Neither a bare label nor inherited routing proves absence of hydration.")},
    143: {0: ("SUPPORTED", "All four descriptors retain FeSO4 x5H2O. The owner preserves that stated hydrate with a distinct local identity, rather than exactly identifying it with its anhydrous parent or replacing five waters with six/seven. This binding does not validate the historical parent predicate or dose fields.")},
    145: {0: ("SUPPORTED", "Both descriptors name the Fildes Enrichment preparation, including MediaDive compound744. The owner denotes that preparation rather than a purified component; the unusual volume percentage is not a quantity approval.")},
    146: {0: ("SUPPORTED", "All four descriptors identify fish peptone, including compound1950. The undefined-mixture owner preserves fish origin and peptone preparation without selecting a species, vendor or digestion protocol.")},
    147: {0: ("SUPPORTED", "Both descriptors identify flavin adenine dinucleotide, including compound1339, matching the FAD owner. No reduced FADH2, mononucleotide or sodium-salt form is selected.")},
    148: {0: ("SUPPORTED", "The sole descriptor explicitly names flucloxacillin, matching that antibiotic owner. Antimicrobial-role metadata does not select a sodium salt or establish dose efficacy.")},
    149: {0: ("SUPPORTED", "All three descriptors identify fluoranthene, including KOMODO457b.1 and compound2113. The owner is the same named aromatic hydrocarbon; no substituted congener or alternative substrate is introduced.")},
    150: {0: ("SUPPORTED", "The inspected descriptor and REMOVE event explicitly name formate. The matching formate owner supplies identity only; the O'Hanlon plain-versus-supplemented ATCC1490 contrast remains an omission event and is not converted to ingredient presence or an inferred salt.")},
    151: {0: ("SUPPORTED", "All three descriptors retain generic fucose, including the P5 single-stock component and compound2050. The owner likewise leaves D/L and anomer unspecified; stock carrier constituents remain separate and their quantities are not newly approved.")},
    152: {
        0: ("SUPPORTED", "The descriptor and REMOVE event explicitly say fumarate, matching the maintained bare-fumarate owner scope documented in its #213 curation. The event remains context-only; no supplied counterion, presence or zero-dose statement is inferred."),
        1: ("SUPPORTED", "The source names fumarate and retains KEGG fum, matching the maintained bare-fumarate owner. No fumaric acid or counterion is introduced, and the recorded30mM remains unvalidated quantity context."),
    },
    153: {0: ("SUPPORTED", "The sole descriptor names galactitol with KEGG galt, matching the galactitol owner rather than galactose or a different sugar alcohol. No quantity/growth approval is implied.")},
    154: {0: ("SUPPORTED", "All13 descriptors name generic galactose, including J124/222/3764/910/4297/482 and the P5 solute stock. The owner retains generic galactose rather than choosing D/L or anomer; stock carrier and dose contexts are preserved separately.")},
    155: {0: ("SUPPORTED", "All four descriptors explicitly identify garden soil, including the vessel soil-layer note and compound2159. The owner preserves garden-soil material scope without equating it to an extract or standardizing its composition; dose representations are not approved.")},
    159: {0: ("WITHHOLD", "Source MediaDive compound1928 names Glycine-NaOH buffer, but the owner records only ingredient1928 import and an undefined local stock identity. No independent preparation or namespace relation establishes the same material scope; dose fields cannot supply it.")},
    160: {0: ("SUPPORTED", "The source explicitly names glycolate with KEGG glyclt, matching the glycolate owner. No sodium salt or glycolic-acid supplied form is inferred.")},
    161: {0: ("SUPPORTED", "All nine UTEX descriptors retain Green House Soil and their specific preparation/dose context. The local owner preserves greenhouse source beyond generic soil; teaspoons and input-volume ratios are not reinterpreted as validated final concentrations.")},
    162: {0: ("SUPPORTED", "The sole descriptor names guaiacol, matching the 2-methoxyphenol owner. No other methoxyphenol regioisomer or mixture is asserted.")},
    164: {0: ("SUPPORTED", "All three descriptors retain guanosine, including NLDM CAS118-00-3 and the P5 single-stock solute. This matches the guanosine owner rather than guanine, deoxyguanosine or a nucleotide; carrier and dose context remain separate.")},
    157: {0: ("SUPPORTED", "The complete P5 MEM descriptor names bare Glutamate without conflicting salt or stereochemical qualifiers. The authoritative MAPPING_SEMANTICS protonation section explicitly names CHEBI29987 as the Glutamate family precedent; live ChEBI confirms its definition and glutamate name. This supports the maintained source-name/concept binding only, not actual medium speciation, pH or a supplied salt. The earlier charge-only allegation is explicitly withdrawn in issue1472.")},
    166: {0: ("SUPPORTED", "All20 descriptors explicitly retain H2WO4, including the JCM/KOMODO and seven MediaDive solution excerpts. The tungstic-acid owner preserves that formula rather than a tungstate salt; source dose and dilution calculations are not freshly validated.")},
    167: {0: ("SUPPORTED", "The extracted pH-buffer descriptor explicitly names H3PO4, matching phosphoric acid. No phosphate salt or buffer mixture is selected, and the unspecified quantity remains unspecified.")},
    168: {0: ("WITHHOLD", "One descriptor labels the ingredient H3BO2 but explicitly annotates boric acid CHEBI33118, whereas the owner denotes boronic acid CHEBI38267. The conflicting chemical identity is not resolved by other H3BO2-labelled descriptors or by inherited routing; preserve the complete case for source clarification.")},
    169: {0: ("SUPPORTED", "Both descriptors name heptadecane, matching the straight-chain C17 owner; no branched isomer or blend is stated. Grams and volume-percent dose representations are not equated.")},
    170: {0: ("WITHHOLD", "The DSMZ138 descriptor explicitly adds the lindane qualifier. Lindane is the gamma isomer, while the candidate owner has unspecified-stereochemistry hexachlorocyclohexane. The generic source label does not erase the more specific source note; an exact binding would discard that form distinction.")},
    171: {0: ("SUPPORTED", "All11 descriptors retain hexadecane, including MediaDive1887/917 and compound687. The owner preserves the named C16 hydrocarbon; no other alkane or oil mixture is introduced. Unusual dose percentages are outside this identity approval.")},
    173: {0: ("SUPPORTED", "The descriptor and source-bound ADD event explicitly identify hydrogen peroxide at the peroxide-exposure stage. The chemical owner fits H2O2; this does not endorse the abstract-only growth-stimulation claim, recommend an exposure dose or materialize a complete growth formulation.")},
    174: {0: ("SUPPORTED", "All10 descriptors identify hypoxanthine, including CAS68-94-0, KEGG hxan and MediaDive3068 compound1348. No xanthine, inosine or nucleotide is substituted; quantities and role claims remain source context.")},
    175: {0: ("SUPPORTED", "The sole descriptor uses the established IPTG name, matching the IPTG/isopropyl beta-D-thiogalactopyranoside owner. No different inducer, sugar or supplied preparation is stated.")},
    176: {
        0: ("SUPPORTED", "All three Indigo carmine descriptors retain that named dye, including MediaDive3779 compound1641. They match the indigo-carmine owner rather than indigo itself; pH-indicator role and doses are not newly approved."),
        1: ("SUPPORTED", "All six Indigocarmine descriptors preserve the same named dye, including MediaDive1402/1403 compound652. The spacing variation does not introduce a different chemical or formulation."),
    },
    177: {
        0: ("SUPPORTED", "All10 Inosine descriptors retain the nucleoside, with CAS58-63-9 and KEGG ins supporting the same owner scope. No hypoxanthine base, deoxyinosine or nucleotide is substituted."),
        1: ("SUPPORTED", "Both Inosin descriptors retain the same inosine synonym and compound546, consistent with the owner's explicitly recorded Inosin alias. No other nucleoside or preparation is stated."),
    },
    178: {
        0: ("SUPPORTED", "Both descriptors explicitly specify iron powder, matching the maintained elemental-iron owner. Powder form remains occurrence context; no ferrous/ferric salt or particle-size equivalence is inferred."),
        1: ("SUPPORTED", "Both descriptors explicitly name iron metal, matching iron(0). This does not equate the metal with soluble Fe2+/Fe3+ or infer any oxidation reaction."),
        2: ("SUPPORTED", "The source explicitly names iron powder, matching the elemental-iron owner while retaining the physical preparation wording. The10g/L value is not newly validated."),
        3: ("SUPPORTED", "Both descriptors retain the literal Iron material input addressed by the owner's explicit #631 curation. Binding uses that maintained elemental-material scope; the inherited iron-atom annotation is not treated as proof of ion charge, supplied salt or chemical behavior."),
    },
    179: {0: ("SUPPORTED", "Both descriptors identify isobutyramide, including compound2144, matching the 2-methylpropanamide owner rather than isobutyric acid or straight-chain butyramide.")},
    183: {0: ("WITHHOLD", "Source MediaDive compound283 K-phosphate buffer is not independently connected to the owner's ingredient283 import or a defined preparation scope. The shared name and two dose fields do not resolve formulation/namespace equivalence; retain the case pending evidence.")},
    184: {0: ("SUPPORTED", "All eight descriptors retain K2CO3, including the documented CCAP subscript repair and MediaDive6198 source. The potassium-carbonate owner preserves the dipotassium carbonate formula rather than bicarbonate; extracted pH context does not establish a quantity.")},
    185: {0: ("SUPPORTED", "All three descriptors explicitly name K2CrO4, including P4's restored stock solute and compound2356. The potassium-chromate owner preserves the formula; no dichromate or other chromium salt is selected, and stock/final contribution quantities remain contextual.")},
    186: {
        0: ("SUPPORTED", "All20 descriptors retain K2S4O6, including DSMZ72's explicit substitution for thiosulfate and the MediaDive5316/4587/2456/5312/2644/2399 excerpts. The owner preserves tetrathionate and potassium counterions; this does not infer a thiosulfate identity or approve biological-role/dose claims."),
        1: ("SUPPORTED", "Both descriptors explicitly name potassium tetrathionate, including compound1917, matching the tetrathionate salt owner without a different sulfur oxyanion or counterion."),
    },
    187: {0: ("SUPPORTED", "All three descriptors explicitly retain KH2PO3, including MediaDive3859 compound1677. The owner's distinct CAS grounding preserves the monopotassium phosphite formula, rather than collapsing it to phosphonic acid or a phosphate salt.")},
    188: {0: ("SUPPORTED", "The descriptor explicitly names Kao and Michayluk vitamin solution. The distinct local preparation owner retains that named formulation; the generic vitamin-solution parent is not treated as exact identity and no composition is invented.")},
    189: {0: ("SUPPORTED", "All21 descriptors retain KHCO3, including DSMZ522/418, JCM1120 and MediaDive591/5211/588/3923/1821/592. The owner preserves potassium hydrogencarbonate, without substitution of carbonate or a different cation; the dose basis is not newly approved.")},
    190: {0: ("SUPPORTED", "Both descriptors retain KNO2, with the MediaDive2808 excerpt explicitly naming that formula. The potassium-nitrite owner preserves nitrite rather than nitrate and does not infer any biological activity.")},
    194: {0: ("WITHHOLD", "Both sources only name L-alpha-phosphatidylcholine without acyl-chain specification. Live authoritative OLS CHEBI86658 exposes a specific C42H80NO8P structure with hexadecanoyl and9E,12E-octadecadienoyl chains. Label equality does not establish those chains or distinguish a lecithin mixture; the exact target is too specific for the inspected source.")},
    197: {0: ("SUPPORTED", "All13 descriptors explicitly identify L-Aspartate, retaining KEGG asp-L and source MediaDB289 membership. Live ChEBI29991 identifies L-aspartate as a synonym of the maintained L-aspartate(1-) concept. This is source-name binding, not a claim about actual solution speciation or a supplied salt; the unavailable amount remains unavailable.")},
    200: {0: ("SUPPORTED", "The sole source explicitly names L-Inositol, matching the owner's specifically curated L-inositol/1L-chiro-inositol scope. No myo-inositol or opposite enantiomer is substituted.")},
    203: {0: ("SUPPORTED", "All three descriptors explicitly retain L-tyrosine disodium salt with CAS69847-45-6. The owner preserves the L configuration and two sodium ions rather than tyrosine free acid or monosodium material.")},
    205: {
        0: ("SUPPORTED", "The JCM119 descriptor explicitly names commercial BD-Difco Legionella agar enrichment. The maintained local enrichment owner retains that catalogue variant; it is not agar identity and does not claim all suppliers are compositionally interchangeable."),
        1: ("SUPPORTED", "The descriptor explicitly names Legionella agar enrichment (compound1630), matching the local multicomponent preparation owner rather than agar alone or a single nutrient."),
    },
    206: {0: ("SUPPORTED", "Both descriptors name Lemon, including compound2091. The owner retains the same named food material; no lemon juice, peel, extract, cultivar or standardized composition is inferred from the dose fields.")},
    207: {0: ("SUPPORTED", "The sole descriptor explicitly names levulinic acid and the corresponding 4-oxopentanoic-acid label. The owner preserves that keto acid rather than levulinate salt or another positional isomer.")},
    208: {0: ("SUPPORTED", "The source identifies generic lipopolysaccharide, matching the generic owner scope. No bacterial strain, chemotype, purity or universal endotoxin potency is inferred.")},
    209: {0: ("SUPPORTED", "All six descriptors name liver digest, including compound2352. The undefined-mixture owner preserves digestion preparation, without selecting animal species, hydrolysis protocol or a liver extract instead.")},
    210: {0: ("SUPPORTED", "All seven descriptors name liver extract. The UTEX Difco Bacto0133 product and pre-filtration preparation context remain attached to that input; binding does not equate its filtered infusion with the starting extract or infer recovery/composition.")},
    211: {0: ("SUPPORTED", "Both JCM13 source descriptors identify liver powder as the extraction starting material. The powder owner retains that preparation; the resulting heated/filtered extract is not treated as the same material and animal species is not inferred.")},
    212: {0: ("SUPPORTED", "All five descriptors retain generic lysine, matching the stereo-unspecified owner. The binding does not infer L/D, hydrochloride or a racemate from role or dose context.")},
    213: {0: ("WITHHOLD", "The complete source case includes compound835 with a CHEBI39005 acid annotation and a simple-organic-compound descriptor, whereas the native owner explicitly denotes a prepared MES stock distinct from pure MES. Its ingredient835 import and name do not independently resolve this source/stock ambiguity or establish the same preparation.")},
    214: {0: ("SUPPORTED", "TOGO M2938 explicitly specifies MH agar as a prepared medium input. The MH-agar owner preserves the formulation rather than treating it as agar polymer alone; no dry-powder conversion is inferred.")},
    215: {0: ("SUPPORTED", "TOGO M2940 explicitly specifies MRS agar from Oxoid. The product-labelled owner preserves that preparation and supplier detail, without collapsing it into agar polymer or asserting equivalent formulations from all suppliers.")},
    216: {0: ("WITHHOLD", "The MediaDB source notes only name Magnesium; they do not independently specify ion charge or supplied chemical form. The candidate is specifically magnesium(2+), while the rejected elemental owner confirms a meaningful sense distinction. An inherited CHEBI annotation and millimolar dose cannot resolve that source ambiguity.")},
    217: {
        0: ("WITHHOLD", "The alternative-preparation descriptor explicitly leaves unstated salt forms unresolved, but the owner structure is malachite-green chloride. The source label and0.25mg input do not establish the chloride counterion; retain the full source-bound event without binding to that specific salt."),
        1: ("WITHHOLD", "The inspected KOMODO645 source explicitly declines to infer an unreported chemical identifier and says only Malachite green. The owner specifically denotes its chloride salt; concentration evidence does not establish that counterion. This witness quarantines the whole immutable case, without attesting uninspected remaining descriptors."),
        2: ("WITHHOLD", "The TOGO M2401/M2407 source excerpts only specify Malachite Green and explicitly avoid inferring a chemical identifier. Neither establishes chloride, which is part of the owner structure; the complete case retains salt-form uncertainty."),
    },
    218: {0: ("SUPPORTED", "The sole descriptor explicitly names maltodextrin, matching the generic owner. No dextrose-equivalent grade, chain-length distribution or specific commercial product is inferred.")},
}

# Explicit inspected blocking witnesses; a witness quarantines the complete case
# without claiming that every other payload in that case was inspected.
WITNESSES = {
    (159, 0): ("descriptor", "8d8a6b8ab05688e9b759feb27dc4b652f446a094a62114d7322c842090bb9239", "/term/id", "Source compound1928 is not independently connected to owner ingredient1928 or a defined shared preparation scope."),
    (183, 0): ("descriptor", "60a2eaf4433c05be9c2128bfacc4cf72e286ed7a191aa4a4cb461df739851563", "/term/id", "Source compound283 and owner ingredient283 lack independently established stock/formulation equivalence."),
    (213, 0): ("descriptor", "ac3312a0239d9a483a543dffd4c0280827b50b34dc8699a659c4fecc4cdfc058", "/chebi_term/id", "MES acid annotation conflicts with the explicitly distinct prepared-stock scope; numeric835/name alone does not resolve it."),
    (313, 0): ("descriptor", "890b1a86a7757e16afc16c3266b71541cf2a27b518bb00fffe58af50ae17d025", "/term/id", "Compound1900 stock lacks a source-specific scope relation to the owner's CultureMech placeholder2 preparation."),
    (348, 0): ("descriptor", "44b0fd8caa2267cec96c7ff2e0848bad9c2bfe56003e78182870c859320b73f5", "/term/id", "Compound1144 and owner ingredient1144 have no independently established namespace/formulation relation."),
    (285, 2): ("descriptor", "014cde6ace63bcf377fff59b6b8b751e27cf8bf3d0eb15f78ae21ef644aa016d", "/chebi_term/id", "Explicit CHEBI32544 nicotinate anion conflicts with native neutral nicotinic acid CHEBI15940; source form remains unresolved."),
    (286, 1): ("held", "2bd5d2871ba53ffbdf5d89fa078df8fa2efdd9cae40fe52c9ab216d16b171f52", "/reason", "The source describes nitrate absence in a separate BG110 comparator and explicitly leaves identity/form and operational membership unresolved."),
    (289, 1): ("descriptor", "5a2a86f69a77d471156da0655dc64572adc374caf6074dd64aa419b98bcd6cb0", "/preferred_term", "Inherited L-specific positive descriptor lacks primary stereochemical support; the same recipe's exact reviewed replacement event explicitly records the paper's unspecified D/L form."),
    (292, 0): ("descriptor", "30206fb3c484fb82265b3c761c6d7270112d6807d775e3cd9dc4189cfec43f51", "/preferred_term", "Brand-qualified Quaker White Oats does not establish the colloidal fine-powder preparation required by NCITC29298."),
    (292, 1): ("descriptor", "0432302efb1c594c992b663dfadfe6c8ca25cd0a781bad577f2bc1f6ace49bf2", "/preferred_term", "Unqualified oatmeal does not independently establish the narrower colloidal fine-powder preparation in NCITC29298."),
    (314, 1): ("held", "be0c4fa6954a08e17723bac8b9ea3abe36d8c43bc621153c3be500d032b61ce4", "/reason", "The exact Hartzell1999 primary chapter was unavailable; the separately verified Reed2001 preparation does not establish this source claim."),
    (303, 2): ("descriptor", "c2b45e454ccf390d7f564f76a4828e0c647e72f47d15a642521890d4aeb4f073", "/supplier_catalog/catalog_number", "P2250 is identified by manufacturer primary specification as D-pantothenic acid hemicalcium salt, incompatible with an unqualified free-pantothenate binding."),
    (304, 0): ("descriptor", "0c51a4af4fa6e5049f43d631fd2b8fa63a7f5bfb4eff2233002175d6aa548bfc", "/evidence/0/snippet", "KOMODO212 retains D-Panthothenic acid alongside the generic source label; the unresolved stereo specificity blocks generic exact material binding."),
    (304, 1): ("descriptor", "b6e37823e88547abca9a51e950fe12b4ccc7764746aa6dc14a3715d6b06ebbbd", "/preferred_term", "Explicit DL material lacks an independently established exact racemate scope on the generic acid owner."),
    (311, 0): ("descriptor", "3b44c3a3fabc2acedf79f4cb0db997dc10eb40fb4a96f9e632a5b5a816abce9e", "/chebi_term/id", "CHEBI18401 phenylacetate anion conflicts constitutionally with native CHEBI8082 phenyl acetate ester."),
    (319, 0): ("descriptor", "9011caf4021271db6e55298afb2d2833f7e5781413171af13b6e2b34ba122bcb", "/term/id", "The explicit K+ annotation is not equivalent to native NCITC765 elemental/NOS potassium; source material scope remains unresolved."),
    (320, 0): ("descriptor", "f4405542642e737d79a0b8e288b445c66d5aa0cc0aa2b9cf1596f29758d43087", "/evidence/0/snippet", "Source potassium aspartate does not establish the L and hemihydrate qualifiers encoded by live NCITC87343."),
    (322, 0): ("descriptor", "e6903298cdf1d88b2fa8ef32f54f13ef293f33765f38ae80ba88327115e7d2d0", "/preferred_term", "Unqualified potassium gluconate lacks independent D-stereochemical evidence required by the target structure."),
    (323, 1): ("descriptor", "bb8ff4f9d28243bd2255781842d5dfff4cf1e5ff6f4434819344eb99a40033b2", "/term/label", "BD220908 descriptor calls the ingredient potato flour but assigns potato starch; the specific product material has not been independently resolved."),
    (324, 0): ("descriptor", "57da7ea25bebb54c1e1d0f31051bc0a5586d25617dc58dbd43842918da1a8ebf", "/evidence/0/snippet", "Primary table states only propanol, not the1-isomer selected by the descriptor and owner."),
    (324, 1): ("descriptor", "24eae3e5969882379f6f6ed3417bfb22322c17a5f02a0db45fb79c2023ff0237", "/notes", "Archived DSMZ868 says propanol without independent isomer-position evidence."),
    (328, 1): ("descriptor", "0df7daf886d452b24b1bc0ba2e35e562b18ac0c1d4d26d7ab545a2e381aa6df7", "/term/id", "Explicit1,4-butanediammonium annotation conflicts with the neutral putrescine owner."),
    (335, 0): ("descriptor", "2347b4981c95c961b9099cddd3b02fbc2a2eb4a077ffa610f6b8531eb25a1a92", "/notes", "JCM586 explicitly requires sterile defibrinated rabbit blood, which native generic rabbit blood treats only as related preparation."),
    (339, 0): ("descriptor", "e60a5e72eda4199480b7c43596017b3a4dca11a085b6896d703579af8337825c", "/term/id", "Source Ribose retains a D-ribose-specific annotation; generic exact identity cannot silently discard unresolved supplied stereochemistry."),
    (344, 1): ("descriptor", "0e2764284d59fd42a428b6710081f91c471e25e3d6d2806ff4611bbbb47ec378", "/notes", "Source explicitly says clarified, a processed rumen-fluid form excluded by the generic native owner's reviewed scope."),
    (122, 0): ("descriptor", "0d25c0ca0de3db971a644eaf9f516358effd0080a76bbbcec4fe8ec427402516", "/preferred_term", "Explicit DL source material lacks an independently established exact racemate binding to the unspecified target."),
    (122, 1): ("descriptor", "ef9c34225d43ebdee8c7bf30134fb6d0be3c077ab899c6becf14129e2165820f", "/preferred_term", "Displaced-parent DL material has unresolved exact racemate scope; preserve context-only status."),
    (122, 2): ("descriptor", "ef9c34225d43ebdee8c7bf30134fb6d0be3c077ab899c6becf14129e2165820f", "/preferred_term", "Displaced-parent DL material has unresolved exact racemate scope; preserve context-only status."),
    (122, 3): ("descriptor", "ef9c34225d43ebdee8c7bf30134fb6d0be3c077ab899c6becf14129e2165820f", "/preferred_term", "Displaced-parent DL material has unresolved exact racemate scope; preserve context-only status."),
    (122, 4): ("descriptor", "ef9c34225d43ebdee8c7bf30134fb6d0be3c077ab899c6becf14129e2165820f", "/preferred_term", "Displaced-parent DL material has unresolved exact racemate scope; preserve context-only status."),
    (122, 5): ("descriptor", "ef9c34225d43ebdee8c7bf30134fb6d0be3c077ab899c6becf14129e2165820f", "/preferred_term", "Displaced-parent DL material has unresolved exact racemate scope; preserve context-only status."),
    (122, 6): ("descriptor", "0d25df7ebc3be9a51aed350bb698124ef3a0aa5db3f0359f4fcc3d16b8a4dea9", "/preferred_term", "Explicit DL-Methionine source material lacks a reviewed exact racemate-to-target scope resolution."),
    (122, 7): ("descriptor", "ef9c34225d43ebdee8c7bf30134fb6d0be3c077ab899c6becf14129e2165820f", "/preferred_term", "Displaced-parent DL material has unresolved exact racemate scope; preserve context-only status."),
    (122, 8): ("descriptor", "ef9c34225d43ebdee8c7bf30134fb6d0be3c077ab899c6becf14129e2165820f", "/preferred_term", "Displaced-parent DL material has unresolved exact racemate scope; preserve context-only status."),
    (122, 9): ("descriptor", "ef9c34225d43ebdee8c7bf30134fb6d0be3c077ab899c6becf14129e2165820f", "/preferred_term", "Displaced-parent DL material has unresolved exact racemate scope; preserve context-only status."),
    (120, 4): ("descriptor", "097a1995a6f6221b7a2d469927ae6e8dac6c8330bde9e5261da9d02f10c2ac81", "/preferred_term", "Source Lipoate is an anionic label, not evidence for the neutral lipoic-acid owner; the exact alias conflict is documented in #1376."),
    (119, 0): ("descriptor", "67374f0ad746ff3b2a1288318a19c9e124b9a21108b7996dcc88e4c25e04d88c", "/preferred_term", "Generic 2-Methyl-butyric acid does not establish the native owner's explicit DL material scope."),
    (119, 1): ("descriptor", "4ca3c8689e33f99b89f36f2d3696dc5ea2a8357c6e0afc4ae0b4b17f2b104f0b", "/preferred_term", "Generic alpha-Methylbutyric acid does not establish the native owner's DL qualifier."),
    (119, 2): ("descriptor", "193696116425a28ff1a8a65a7de1a2bfa3d0538570837337c422facc72ea5a86", "/preferred_term", "Generic 2-methylbutyric acid does not establish the native owner's DL qualifier."),
    (119, 3): ("descriptor", "a1f007938ebee432b8bc174dbe8a4e6d913d475b6bb07bb297a8de8e68acc302", "/preferred_term", "Explicit DL-alpha-Methyl butyric acid is routed to a stereochemically unspecified external target without an established racemate-scope decision."),
    (119, 4): ("descriptor", "793c444265cbad609492b99bb0031239c4e7bb7e61f898df202e771b08b7e29f", "/preferred_term", "Generic 2-Methylbutyric Acid does not establish the native owner's DL qualifier."),
    (119, 5): ("descriptor", "46ca5eff3da01666395eddd5b303d80d8dcf25800ee4cc8b3dbeeb3335c40b72", "/preferred_term", "Explicit DL-2-Methylbutyric acid is routed to a stereochemically unspecified external target without an established racemate-scope decision."),
    (119, 6): ("descriptor", "0a508ca1f6f0ad2e4c94c367bd21f5cf1894ccfb0f7d819a26668c3aec4aefbf", "/preferred_term", "Explicit DL-2-Methyl butyric acid is not independently established as exact identity to the unspecified target."),
    (119, 7): ("descriptor", "8b22984778573fafa252d540553068c355beac178e48577212bde6fc7ff25a54", "/preferred_term", "Generic alpha-Methylbutyric acid does not establish the owner's DL material scope."),
    (119, 8): ("descriptor", "1501452e99a1eeec298a7e4f0b55da424cb52147b92198d94d0e93e53fe7434f", "/preferred_term", "Generic 2-Methylbutyric acid does not establish the owner's DL material scope."),
    (119, 9): ("descriptor", "4e1c0f651262ff170f831a23ae18257c63bc2e9b5909477c0657982579a96a6d", "/preferred_term", "Generic 2-methylbutanoic acid does not establish the owner's DL material scope."),
    (181, 3): ("descriptor", "09f44ef3bb3ebd54b4375e3a5b5cfdf0dc92af4c9baf5da7036d45f475e1b4d0", "/evidence/1/snippet", "The primary excerpt says isovalerate while the database and native owner select neutral isovaleric acid; ionization and supplied salt remain explicitly uncertified."),
    (180, 2): ("descriptor", "00bb27298af96ca9368d401a9e659b4c1ef4a2acd64be40a5041d28a7e7a6fe8", "/preferred_term", "The source explicitly names 2-Methylpropanoate/isobutyrate but the candidate is neutral isobutyric acid; no supplied acid or salt form is established."),
    (193, 1): ("descriptor", "067d5feaf162d58d738ddfc83b9e61d7c4a07496bf4aa3e24ddea3eaa6845427", "/preferred_term", "Generic Alanine lacks source stereochemistry; inherited L-alanine annotation cannot establish the L-specific source form."),
    (199, 0): ("held", "4931a08c99fb3c8deb61579c5730aad1c497080b0d6af595f1932b9275521196", "/source_text", "The generic glutamine exclusion explicitly does not certify local stereochemical terms; the candidate owner is L-specific."),
    (199, 1): ("held", "4931a08c99fb3c8deb61579c5730aad1c497080b0d6af595f1932b9275521196", "/source_text", "The generic glutamine exclusion explicitly does not certify local stereochemical terms; the candidate owner is L-specific."),
    (199, 3): ("descriptor", "03ca31f63296bba0bd3449e06fe59bba743b58dd5de99a84e0c3f463a20c0089", "/preferred_term", "Generic Glutamine has no source stereochemical qualifier but the candidate owner is L-glutamine."),
    (172, 2): ("descriptor", "5021081bf6850a4c6f99169505102fabe5d9ee95a11c4218d1dfcf03bbdb1cf4", "/notes", "JCM1099 explicitly specifies sterile defibrinated horse blood; the candidate owner states only generic horse blood and loses that preparation distinction."),
    (112, 0): ("descriptor", "601536faa02d9428b3320a1e380e8090a70405a805bffae125657c4b349aef73", "/preferred_term", "Source omits L stereochemistry required by CHEBI63075; https://github.com/CultureBotAI/MediaIngredientMech/issues/1469"),
    (125, 1): ("descriptor", "990b8041c10dfbc9b71a09d4b109959a48c68f04ccfd833d8dbaed9db49dc26f", "/preferred_term", "Cow manure source does not establish the dry preparation required by the owner."),
    (140, 0): ("descriptor", "99995528816f251e2a63bf313345dcae9a761df0868525d559a9bc4a0964c2ec", "/preferred_term", "Ferrous citrate source does not establish monoferrous acid citrate stoichiometry/protonation."),
    (142, 0): ("descriptor", "db513cad86a6cdc330fb773ee53dc2e0c272e714f93ab8bf4bd4e23a033fc65d", "/preferred_term", "Ferrous ammonium sulfate source explicitly leaves supplied hydration unvalidated, rather than establishing anhydrous material."),
    (168, 0): ("descriptor", "1382c7817ad28ffd63edc9bfa8d2758ecae15024085448d08382afd92c9e5557", "/term/label", "Boric acid annotation conflicts with H3BO2 label and boronic-acid owner."),
    (170, 0): ("descriptor", "f3358846f9f43c2234c4f8e098625ad5ee70c6df692251889f8e5571edbf65f2", "/notes", "Source explicitly names lindane, whose gamma-isomer specificity is absent from the generic hexachlorocyclohexane owner."),
    (194, 0): ("descriptor", "540892fb197a0cb65fda3d059b5379572bb55886cfb9f2219955bc73160ad44f", "/preferred_term", "Source L-alpha-phosphatidylcholine does not specify the particular acyl chains encoded by CHEBI86658."),
    (216, 0): ("descriptor", "00bc1ab5b7186517ac6095fc810e156ba36b538da10dfe716a1643a972b3e91c", "/notes", "MediaDB source says Magnesium without establishing the candidate's specific +2 ionic form."),
    (217, 0): ("descriptor", "41cabbfa84e84b952cdfd6670b10fdf7b9f039ea4b912ab4ae7899a23859c568", "/notes", "Source explicitly leaves salt form unresolved, whereas owner structure includes chloride."),
    (217, 1): ("descriptor", "4446a8ae74264b538b972f9aa0b69e8f99a85de2bcf836b64414ebe0003e2b71", "/evidence/0/snippet", "Generic Malachite green source excerpt does not establish chloride counterion."),
    (217, 2): ("descriptor", "61861ab5a865f6f4ed3f19418394679a74e552e656635d6752510931f9103eac", "/evidence/0/snippet", "TOGO source only names Malachite Green without the owner's chloride counterion."),
}


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def pinned(path, expected):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError(f"Pinned bytes changed: {path}")
    return json.loads(raw)


def packet(index):
    if index not in OWNERS and index not in EXTRA_OWNERS and index not in LATE_OWNERS:
        raise ValueError("Owner outside assigned complete range")
    summary = pinned(PARTITIONS / "summary.json", SUMMARY_SHA256)
    name = f"owner-{index:04d}.json"
    value = pinned(PARTITIONS / name, summary["files"][name]["sha256"])
    if value["intake_sha256"] != INTAKE_SHA256 or value["review_packet_sha256"] != PACKET_SHA256:
        raise ValueError("Owner belongs to another source packet")
    return value


def descriptor_signatures(payloads, cases):
    """Factor only concentration objects; retain every other source field.

    Each displayed signature includes all identity, form, notes and evidence.
    Exact distinct concentration objects remain visible without interpretation.
    Reconstruction is checked against every original complete descriptor.
    """
    groups = {}
    for sha, item in payloads.items():
        signature = {key: val for key, val in item.items() if key != "concentration"}
        key = canonical(signature)
        group = groups.setdefault(key, {"signature": signature, "quantities": {}, "hashes": []})
        quantity = {"present": "concentration" in item, "value": item.get("concentration")}
        group["quantities"][canonical(quantity)] = quantity
        rebuilt = dict(signature)
        if quantity["present"]:
            rebuilt["concentration"] = quantity["value"]
        if canonical(rebuilt) != canonical(item):
            raise ValueError("Descriptor signature reconstruction failed")
        group["hashes"].append(sha)
    for group in groups.values():
        hashes = set(group["hashes"])
        yield {
            "identity_form_qualifier_evidence_signature": group["signature"],
            "uninterpreted_concentration_variants": list(group["quantities"].values()),
            "case_indices": [i for i, case in enumerate(cases) if hashes.intersection(case.get("descriptors", {}))],
            "descriptor_count": len(hashes),
            "descriptor_hash_set_sha256": hashlib.sha256(canonical(sorted(hashes)).encode()).hexdigest(),
            "first_descriptor_sha256": group["hashes"][0],
            "reconstruction": "EXACT_ALL_DESCRIPTORS",
        }


def exact_fragments(value):
    """Intern exact sentence/line fragments, retaining all text and reconstruction."""
    fragments, lookup, strings, string_lookup = [], {}, [], {}

    def encode(item):
        if isinstance(item, dict):
            return {key: encode(child) for key, child in item.items()}
        if isinstance(item, list):
            return [encode(child) for child in item]
        if not isinstance(item, str) or len(item) < 120:
            return item
        if item not in string_lookup:
            indices = []
            for fragment in re.split(r"(?<=\n)|(?<=; )|(?<=\. )", item):
                if fragment not in lookup:
                    lookup[fragment] = len(fragments)
                    fragments.append(fragment)
                indices.append(lookup[fragment])
            string_lookup[item] = len(strings)
            strings.append(indices)
        return {"$fragments_string": string_lookup[item]}

    encoded = encode(value)

    def decode(item):
        if isinstance(item, dict):
            if set(item) == {"$fragments_string"}:
                return "".join(fragments[i] for i in strings[item["$fragments_string"]])
            return {key: decode(child) for key, child in item.items()}
        if isinstance(item, list):
            return [decode(child) for child in item]
        return item

    if canonical(decode(encoded)) != canonical(value):
        raise ValueError("Exact fragment reconstruction failed")
    return {"contract": "Every source field is retained. Repeated exact sentence/line fragments are displayed once; strings are ordered concatenations. Complete reconstruction verified. No scientific inference.", "fragments": dict(enumerate(fragments)), "strings": dict(enumerate(strings)), "payload": encoded}


def numeric_templates(value):
    """Losslessly factor only exact nonnumeric text, displaying every slot value.

    Dates, identifiers and arithmetic often differ in otherwise repeated source
    text. Chemical formula numbers are retained as common or varying slots too;
    no digits, words, qualifiers, or evidence are discarded by this view.
    """
    groups, lookup, strings = [], {}, []
    pattern = re.compile(r"(\b[0-9a-f]{64}\b|\d+(?:\.\d+)?(?:[Ee][+-]?\d+)?)")

    def encode(item):
        if isinstance(item, dict):
            return {key: encode(child) for key, child in item.items()}
        if isinstance(item, list):
            return [encode(child) for child in item]
        if not isinstance(item, str) or len(item) < 120:
            return item
        split = pattern.split(item)
        literal, numbers = split[::2], split[1::2]
        key = canonical(literal)
        if key not in lookup:
            lookup[key] = len(groups)
            groups.append({"literal_parts": literal, "values": []})
        group = lookup[key]
        if numbers not in groups[group]["values"]:
            groups[group]["values"].append(numbers)
        variant = groups[group]["values"].index(numbers)
        reconstructed = "".join(part + (numbers[i] if i < len(numbers) else "") for i, part in enumerate(literal))
        if reconstructed != item:
            raise ValueError("Numeric text reconstruction failed")
        strings.append(item)
        return {"$numeric_text": [group, variant]}

    encoded = encode(value)
    for group in groups:
        width = len(group["values"][0])
        common = {i: group["values"][0][i] for i in range(width)
                  if all(row[i] == group["values"][0][i] for row in group["values"])}
        varying = [i for i in range(width) if i not in common]
        original = group.pop("values")
        group["common_slots"] = common
        group["varying_slots"] = varying
        group["variants"] = [[row[i] for i in varying] for row in original]
        for variant, row in zip(group["variants"], original, strict=True):
            restored = {**common, **dict(zip(varying, variant, strict=True))}
            if [restored[i] for i in range(width)] != row:
                raise ValueError("Numeric slot reconstruction failed")
    return {"contract": "Every source field and text span retained; exact text and slot reconstruction verified. Formula digits are explicit slots, never inferred. Descriptor key list separately pinned by count/hash.", "text_templates": groups, "payload": encoded}


def display(index, selected_cases=None, summary_only=False, search=None, group_start=0, group_stop=None, payloads_only=False, templates=False, fragments=False, numeric=False):
    value = packet(index)
    owner = {key: item for key, item in value["owner_payload"].items()
             if key not in {"curation_history", "occurrence_statistics", "nutritional_roles",
                            "biological_roles", "medium_roles", "functional_roles"}}
    if not payloads_only:
        print(canonical({"owner_index": index, "owner_record": value["owner_record"],
                     "owner_identity_payload": owner,
                     "display_scope": "Source-binding view excludes owner history/statistics/roles only; complete owner remains pinned. All source descriptor/change/hold fields follow."}))
    all_payloads = {field: {} for field in ("descriptors", "change_payloads", "held_payloads")}
    for number, case in enumerate(value["cases"]):
        if selected_cases is not None and number not in selected_cases:
            continue
        shown = {k: v for k, v in case.items() if k not in (*all_payloads, "source_mentions", "candidate")}
        shown["case_index"] = number
        shown["candidate"] = {key: item for key, item in case["candidate"].items()
                              if key not in {"owner_record", "owner_record_sha256", "owners"}}
        for field in all_payloads:
            payloads = case.get(field, {})
            shown[field] = {"count": len(payloads), "locator": f"owner-{index:04d}.json#/cases/{number}/{field}"}
            for key, item in payloads.items():
                if key in all_payloads[field] and canonical(all_payloads[field][key]) != canonical(item):
                    raise ValueError("One source hash denotes different values")
                all_payloads[field][key] = item
        coordinates = case.get("source_mentions", [])
        shown["coordinate_evidence"] = {
            "count": len(coordinates),
            "sha256": hashlib.sha256(canonical(coordinates).encode()).hexdigest(),
            "locator": f"owner-{index:04d}.json#/cases/{number}/source_mentions",
        }
        if not payloads_only:
            print(canonical(shown))
    for field, payloads in all_payloads.items():
        if payloads and not summary_only:
            if templates or fragments or numeric:
                selected = dict(list(payloads.items())[group_start:group_stop])
                transposed = field_values(selected)
                if numeric:
                    keys = transposed.pop("descriptor_keys")
                    transposed["descriptor_key_count"] = len(keys)
                    transposed["descriptor_keys_sha256"] = hashlib.sha256(canonical(keys).encode()).hexdigest()
                    rendered = numeric_templates(transposed)
                else:
                    rendered = exact_fragments(transposed) if fragments else text_templates(transposed)
                print(canonical({"payload_type": field, "total_payloads": len(payloads), "display_start": group_start, "display_count": len(selected), "exact_field_and_text_templates": rendered}))
                continue
            if field == "descriptors":
                for number, group in enumerate(descriptor_signatures(payloads, value["cases"])):
                    if number < group_start or (group_stop is not None and number >= group_stop):
                        continue
                    if search and not re.search(search, canonical(group), flags=re.IGNORECASE):
                        continue
                    group["signature_index"] = number
                    print(canonical({"payload_type": field, **group}))
            else:
                print(canonical({"payload_type": field, "exact_factored_payloads": factor_payloads(payloads)}))


def build(output, extra=False, late=False):
    rows = []
    for index in LATE_OWNERS if late else EXTRA_OWNERS if extra else OWNERS:
        value = packet(index)
        decisions = DECISIONS.get(index, {})
        if set(decisions) != set(range(len(value["cases"]))):
            raise ValueError(f"Incomplete explicit owner review: {index}")
        for number, case in enumerate(value["cases"]):
            disposition, reason = decisions[number]
            if disposition not in {"SUPPORTED", "WITHHOLD"} or not reason.strip():
                raise ValueError("Missing explicit case judgment")
            row = {
                "case_id": case["case_id"],
                "row_sha256": value["case_payload_sha256"][case["case_id"]],
                "disposition": disposition,
                "review_reason": reason,
                "inspected_descriptor_sha256": list(case.get("descriptors", {})),
                "inspected_change_sha256": list(case.get("change_payloads", {})),
                "inspected_held_sha256": list(case.get("held_payloads", {})),
                "evidence_locators": [
                    f"owner-{index:04d}.json#/owner_payload",
                    f"owner-{index:04d}.json#/cases/{number}",
                ],
            }
            if disposition == "SUPPORTED":
                if set(case["context"].get("held_fields", [])) & {"SOURCE_CLAIM", "IDENTITY_FORM"}:
                    raise ValueError("Source identity/source-claim hold cannot be supported (#1530)")
                choices = case["candidate"]["supported_canonical_rows"]
                if len(choices) != 1:
                    raise ValueError("Supported case needs one explicitly reviewed canonical row")
                row["canonical_row_sha256"] = choices[0]["row_sha256"]
            else:
                kind, sha, pointer, witness_reason = WITNESSES[(index, number)]
                field = {"descriptor": "descriptors", "change": "change_payloads", "held": "held_payloads"}[kind]
                payload = case[field][sha]
                for token in pointer.split("/")[1:]:
                    token = token.replace("~1", "/").replace("~0", "~")
                    payload = payload[int(token)] if isinstance(payload, list) else payload[token]
                for name in ("descriptor", "change", "held"):
                    row[f"inspected_{name}_sha256"] = [sha] if name == kind else []
                row["blocking_witnesses"] = [{"payload_kind": kind, "sha256": sha, "field_path": pointer, "reason": witness_reason}]
                row["evidence_locators"].append(f"owner-{index:04d}.json#/cases/{number}/{field}/{sha}{pointer}")
                if (index, number) == (112, 0):
                    row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1469")
                if (index, number) in {(125, 1), (140, 0), (142, 0)}:
                    row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1470")
                if (index, number) in {(168, 0), (170, 0)}:
                    row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1472")
                if index in {194, 217}:
                    row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1478")
                if (index, number) in {(172, 2), (216, 0), (193, 1), (199, 0), (199, 1), (199, 3)}:
                    row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1484")
            if index == 194:
                row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1372")
                row["evidence_locators"].append("https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86658")
            if index == 119:
                row["evidence_locators"].extend(["https://github.com/CultureBotAI/MediaIngredientMech/issues/1494", "https://www.ebi.ac.uk/chebi/CHEBI:37070"])
            if index == 120:
                row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/454")
                if number == 4:
                    row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1376")
            if index == 122:
                row["evidence_locators"].extend(["https://github.com/CultureBotAI/MediaIngredientMech/issues/1499", "https://www.ebi.ac.uk/chebi/CHEBI:16811", "https://github.com/CultureBotAI/MediaIngredientMech/issues/317"])
            if index == 127:
                row["evidence_locators"].extend(["https://github.com/CultureBotAI/MediaIngredientMech/issues/319", "https://github.com/CultureBotAI/MediaIngredientMech/issues/320"])
            if (index, number) == (136, 2):
                row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1491")
            if (index, number) in {(180, 2), (181, 3)}:
                row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1492")
            if index == 157:
                row["evidence_locators"].extend(["MAPPING_SEMANTICS.md#protonation-state-bare-anion-labels", "https://www.ebi.ac.uk/chebi/CHEBI:29987", "https://github.com/CultureBotAI/MediaIngredientMech/issues/1472#issuecomment-6934100446"])
            if index == 170:
                row["evidence_locators"].append("https://www.ebi.ac.uk/chebi/CHEBI:32888")
            if (index, number) == (314, 1):
                row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1530")
            if (index, number) in {(303, 2), (304, 1), (311, 0), (320, 0), (324, 0), (324, 1)}:
                row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1515")
            if (index, number) in {(304, 0), (319, 0), (322, 0), (323, 1), (328, 1), (335, 0), (338, 0), (339, 0), (344, 1)}:
                row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1528")
            if index == 303 and number == 2:
                row["evidence_locators"].extend(["https://utex.org/products/DAS-vitamin-cocktail", "https://www.sigmaaldrich.com/specification-sheets/364/729/P2250-BULK________SIGMA____.pdf", "https://www.sigmaaldrich.com/US/en/sds/SIGMA/P2250"])
            if index == 304:
                row["evidence_locators"].append("https://www.ebi.ac.uk/chebi/CHEBI:7916")
            if index == 307:
                row["evidence_locators"].append("https://github.com/CultureBotAI/CultureMech/issues/798")
            if index == 311:
                row["evidence_locators"].extend(["https://www.ebi.ac.uk/chebi/CHEBI:8082", "https://www.ebi.ac.uk/chebi/CHEBI:18401"])
            if index == 319:
                row["evidence_locators"].append("https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C765?include=summary")
            if index == 320:
                row["evidence_locators"].append("https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C87343?include=summary")
            if index == 322:
                row["evidence_locators"].append("https://www.ebi.ac.uk/chebi/CHEBI:32032")
            if index == 338:
                row["evidence_locators"].append("https://www.ebi.ac.uk/chebi/CHEBI:26546")
            if index == 339:
                row["evidence_locators"].append("https://www.ebi.ac.uk/chebi/CHEBI:33942")
            if index in {300, 325, 333, 347}:
                identifier = {300: "17879", 325: "17272", 333: "15361", 347: "30762"}[index]
                row["evidence_locators"].extend(["MAPPING_SEMANTICS.md#protonation-state-bare-anion-labels", "https://www.ebi.ac.uk/chebi/CHEBI:" + identifier])
            if index in {318, 336, 346, 349}:
                row["evidence_locators"].append("https://github.com/CultureBotAI/CultureMech/issues/794#issuecomment-6934783778")
            if index in {159, 183, 213, 313, 348}:
                row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1485#issuecomment-6934947399")
            if (index, number) in {(285, 2), (289, 1), (292, 0), (292, 1)}:
                row["evidence_locators"].append("https://github.com/CultureBotAI/MediaIngredientMech/issues/1532")
            if index == 285 and number == 2:
                row["evidence_locators"].append("https://www.ebi.ac.uk/chebi/CHEBI:32544")
            if index == 289:
                row["evidence_locators"].extend(["doi:10.1038/ncomms5346#Methods-p5", "owner-0289.json#/cases/0/change_payloads/d6f526fae5040cd1dee4e900b8bc0023e61ce3a681de6fbfb805661bbe233224"])
            if index == 292:
                row["evidence_locators"].append("https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C29298?include=full")
            if index in {286, 295, 297}:
                identifier = {286: "17632", 295: "30839", 297: "18367"}[index]
                row["evidence_locators"].extend(["MAPPING_SEMANTICS.md#protonation-state-bare-anion-labels", "https://www.ebi.ac.uk/chebi/CHEBI:" + identifier])
            rows.append(row)
    partition = "owners-0285-through-0299" if late else "owners-0300-through-0349" if extra else "owners-0109-through-0218-except-0118-delegated-root"
    document = {"intake_sha256": INTAKE_SHA256, "partition": partition, "decisions": rows}
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(document, ensure_ascii=False, indent=2) + "\n")
    print(canonical({"decision_count": len(rows), "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", type=int, action="append")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--index", action="store_true")
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--extra", action="store_true", help="Use delegated owners300–349 for index/progress/output")
    parser.add_argument("--late", action="store_true", help="Use delegated owners285–299 for index/progress/output")
    parser.add_argument("--case", type=int, action="append")
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument("--payloads-only", action="store_true")
    parser.add_argument("--templates", action="store_true", help="Lossless field/text factoring; group boundaries index complete payloads")
    parser.add_argument("--fragments", action="store_true", help="Lossless exact sentence/line interning; group boundaries index complete payloads")
    parser.add_argument("--numeric", action="store_true", help="Lossless numeric-slot factoring; all literal text and numbers remain visible")
    parser.add_argument("--search", help="Display matching full signatures as leads, never decisions")
    parser.add_argument("--group-start", type=int, default=0)
    parser.add_argument("--group-stop", type=int)
    args = parser.parse_args()
    if args.extra and args.late:
        parser.error("Choose only one delegated partition")
    if args.progress:
        missing = {}
        for index in LATE_OWNERS if args.late else EXTRA_OWNERS if args.extra else OWNERS:
            value = packet(index)
            absent = sorted(set(range(len(value["cases"]))) - set(DECISIONS.get(index, {})))
            if absent:
                missing[index] = absent
        print(canonical({"explicit_case_decisions": sum(len(x) for x in DECISIONS.values()), "incomplete_owners": missing}))
    elif args.index:
        for index in LATE_OWNERS if args.late else EXTRA_OWNERS if args.extra else OWNERS:
            value = packet(index)
            print(canonical({"owner_index": index, "owner": value["owner_record"], "cases": len(value["cases"])}))
    elif args.output:
        build(args.output, args.extra, args.late)
    elif args.owner:
        for index in args.owner:
            display(index, args.case, args.summary_only, args.search, args.group_start, args.group_stop, args.payloads_only, args.templates, args.fragments, args.numeric)
    else:
        parser.error("Supply --owner or --output")


if __name__ == "__main__":
    main()
