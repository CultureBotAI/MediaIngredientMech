# Materials source review

Reviewed51 exact source cases and 20 isolated proposal payloads. No maintained owner files changed. Independent skeptical review remains separately recorded.

All frozen source cases and full recipe snapshots were inspected; each exact source and occurrence is bound by hashes. Primary records distinguish original recipe/supplier/ontology captures from failed retrievals and unsupported provider annotations. Existing native/consumed/downstream holds are copied explicitly. Whole-owner release approval is outside this review.

JCM431, DSMZS777 and JCM852 selenite/tungstate formulas remain distinct. DSMZ1245 repeats a maltose row, so its proposal is qualitative and partial. JCM1404 percent basis and solvent are unknown, so its cellobiose-stock proposal is partial. Successful Togo API retries resolve M2596 sludge-supernatant preparation and25%(v/v) dose. ATCC1203 supports source-specific cellobiose identification in the CM4 carbon-source slot. Molasses currently grounds to beet root; exact material term FOODON03543005 supports a bounded repair.

## Case decisions

### 5: Sugar Stock Solution

`CM_NAME:09425422bf6f2b0272f897b60becd790003ebf354d175363effbe78ad3c5c152` — stock_product_mixture_context

MediaDive S2474 explicitly adds S5688, also named by DSMZ1245. The stock contains multiple sugars, pectin/starch, sodium pyruvate and thiamine pyrophosphate. Both the original DSMZ PDF and S5688 repeat Maltose 8 g in successive rows. Preserve a distinct stock identity; do not silently sum, delete or replace one maltose row. A partial qualitative component proposal is possible while the maltose amount remains unresolved.

Proposals: m-dsmz1245_sugar_stock_s5688. Evidence: m-frozen-shard, m-recipe-6ec8063661f55bae, m-mediadive-solution-2474, m-mediadive-solution-5688, m-dsmz-1245.

Remaining source requirement: Supplier/source clarification of the repeated Maltose 8 g rows is needed before quantitative complete partonomy or preparation use.

### 6: Anaerobic digestor sludge supernatant (SS)

`CM_NAME:096b6808ce08382d9ea8264b1eb5cb53111cd5f2a4e711c04d92a56eff66bef5` — new_distinct_ingredient_proposal

The complete Togo M2596 source defines SS from Ithaca wastewater digester sludge: sequential centrifugation, pH7 adjustment with1M HCl,0.8µm prefiltration, nitrogen purge and0.8–0.2µm sterile filtration. It explicitly adds25%(v/v) SS. Sludge fluid in the frozen flattened recipe is a nested preparation input, not a separate basal supplement. The source does not add yeast extract during SS preparation; DSMZ119 yeast-treated sludge fluid is a different product. Propose this source-defined processed material without representing sludge/HCl extraction inputs as final molecular components.

Proposals: m-togo_m2596_anaerobic_sludge_supernatant. Evidence: m-frozen-shard, m-recipe-2319d9f7ee32c279, m-togo-data-2596, m-dsmz-119.

### 8: 10% Cellobiose solution*

`CM_NAME:0d736c762ccd8b6f8a4e6af5c567d5dff1fd93e77e456ec459e44065f52629ba` — new_distinct_ingredient_proposal

JCM1404 explicitly calls for 10 ml of 10% Cellobiose solution, filter sterilized. This is a solution rather than cellobiose solid. The source does not explicitly state percent basis, solvent or hydrate. Propose a source-bound stock with partial qualitative component evidence; preserve the literal 10% in notes without converting it to g/L or inventing a solvent.

Proposals: m-jcm1404_cellobiose_solution_10pct. Evidence: m-frozen-shard, m-recipe-1b12d08b6b4e28b5, m-jcm-1404.

Remaining source requirement: Verify the 10% basis and solvent in JCM1404 stock preparation before a complete quantitative formulation or preparation use.

### 19: Purified water

`CM_NAME:18c71e232cc2db0d3794822c19642c9859413f54e2bf6dd62b1d653b14dc6e3a` — broad_parent_relation_only

The P4/P5 primary pages call the carrier purified H2O; P4 uses final-volume makeup and P5 uses nested stock solvent with unspecified added amounts. Purification is not specified as distillation. CHEBI15377 denotes molecular water, whereas the existing owner is distilled water and rejects related preparations. Keep chemical-family reference separate from material or purification equivalence and do not infer a 1 L water dose.

Proposals: none. Evidence: m-frozen-shard, m-recipe-f751bf318cda4d40, m-recipe-cb5a972f2d1da8e1, m-mediadive-medium-P4, m-mediadive-medium-P5, m-ontology-chebi-15377.

### 22: alginate (brown algae)

`CM_NAME:1d6d05bf890c16200e5a8b7f6420282713eeaa413cd397aabe173f14b47c2b74` — unresolved

Brown-algae origin qualifies a polymeric alginate preparation. The current Alginate owner grounds the alginate anion; the source does not state acid/salt, counterion, supplier or molecular-mass grade. Plant origin does not resolve that supplied-form boundary. No sodium-alginate or alginic-acid identity is inferred from the name. Togo M2313 prose confirms brown-algae alginate but its Alginic acid annotation does not establish acid versus salt; the carbon sources were alternatives, not a mixture.

Proposals: none. Evidence: m-frozen-shard, m-recipe-a1c2ef58d6c02968, m-ontology-alginate, m-togo-2313, m-togo-data-2313.

Remaining source requirement: Obtain the M2313 alginate supplier/catalog or preparation specifying acid versus salt and counterion; then select the appropriate source-qualified material owner.

### 25: Tryptic Digest of beef heart

`CM_NAME:2470d3e862d2d7bfaae284c1d8ed68217620196ba9aeea1b5f25c11f706360c0` — new_distinct_ingredient_proposal

The primary DSMZ687/1331 formulations list tryptic digest of beef heart separately from the other peptones. It is a processed animal-tissue digest, distinct from beef-heart infusion, whole heart and the complete Columbia broth/agar. The retained capitalization variants carry the same explicitly named tissue and digestion process; no supplier interchangeability or nutrient-role claim is made.

Proposals: m-tryptic_digest_of_beef_heart. Evidence: m-frozen-shard, m-recipe-1bd1d60e982c9a02, m-recipe-d0aedeba249c6c01, m-recipe-6d69ad65bfe2e698, m-recipe-e5be5342ffb17e27, m-dsmz-687, m-dsmz-1331, m-mediadive-ingredient-662, m-ols-tryptic-heart, m-togo-data-2256.

### 26: BG-FPC (see below)

`CM_NAME:287416c04202852582ead36b6e03a848e0cb09cdd2201bbf189e91edcd472d66` — new_distinct_ingredient_proposal

JCM1231 explicitly defines BG-FPC as a nested stock of NaNO3, MgSO4·7H2O, CaCl2·2H2O, disodium EDTA, a separately defined trace-mineral mix and water. The frozen TOGO occurrence has 10 G_PER_L, whereas JCM specifies 10 ml stock addition. Propose source-bound stock identity and direct components, preserving the nested trace mix; flag the upstream dose-unit problem rather than treating the stock as any constituent.

Proposals: m-jcm1231_bg_fpc. Evidence: m-frozen-shard, m-recipe-b3b23751baad5066, m-jcm-1231, m-ols-specific-stocks.

### 27: Casein digest (Casitone, cat. no. 225930)

`CM_NAME:2981d40273a02dd3d797e382cff8b55963bef8e6fdf6fcaeb5d5ec16c2f4326c` — existing_identity_or_alias

CCAP MC names Casitone catalog225930, and the manufacturer225930 page confirms Bacto Casitone as pancreatic enzymatic casein digest. The exact catalog ties this source label to the Casitone product owner/MICRO0000606. The same manufacturer warns Casitone and alternative tryptone products have different digestion/nutritive profiles, so this alias does not merge those products.

Proposals: m-casitone_catalog_alias. Evidence: m-frozen-shard, m-recipe-130ffe6c71f41a82, m-ccap-MC, m-supplier-casitone, m-ontology-micro-0000606.

### 36: Papaic digest of soyabean meal

`CM_NAME:3c2e66ce0b1da63e6737d04ebdcb38eef107f22400330fa9afe50cc43c3055c6` — stock_product_mixture_context

Papaic digestion and soyabean-meal substrate define a vegetable peptone preparation. The frozen Frey broth lists it separately from casein enzymic hydrolysate. Phytone is a candidate commercial papaic soy product, but this source has no supplier/catalog, and the shared broad hydrolyzed-protein class does not prove product equivalence. Togo M2233 directly confirms2.5g papaic soy meal digest,7.5g casein enzymic hydrolysate and RM1239 horse serum; the latter is a useful HiMedia product lead, not proof of the digest catalog. Direct manufacturer M1050 sheet retrieval returned403; no BD Phytone product bridge was obtained.

Proposals: none. Evidence: m-frozen-shard, m-recipe-b8e52797931b2b88, m-togo-2233, m-supplier-casitone, m-togo-data-2233, m-himedia-failed.

Remaining source requirement: Recover the Frey broth original supplier/product definition for its papaic soy digest before selecting Phytone or another product owner.

### 41: Phosphates solution

`CM_NAME:4664d5f5ef483e152f8f8b2ef2dde380a273603d397082dc3d0804bf139213b0` — new_distinct_ingredient_proposal

JCM1199 defines the phosphates stock as Na2HPO4·2H2O 2.44 g, KH2PO4 1.52 g and distilled water1 L, pH6.9; it adds100 ml stock after autoclaving. MediaDive S5318 flattens the stock body alongside its100 ml input, so the provider-derived percentages must not be interpreted as the stock formula or whole-medium dose. Propose a JCM1199-specific buffer identity.

Proposals: m-jcm1199_phosphates_solution. Evidence: m-frozen-shard, m-recipe-35a45f49a4a83615, m-jcm-1199, m-mediadive-solution-5318.

### 42: Triptone

`CM_NAME:4a32eca47cf598b7cccc209ba1492e9dc92f6968bf87fef65903a9569141baaa` — unresolved

The complete Togo M3210 source prose labels10g/L digest triptone and its annotation maps Tryptone. The Luria broth context and annotation support a likely spelling correction, but no original citation, catalog or digestion specification resolves the product identity. MICRO0000182 verifies the tryptone concept; the annotation is not independent evidence of pancreatic casein digestion. Preserve source spelling pending the actual product/citation.

Proposals: none. Evidence: m-frozen-shard, m-recipe-39eecbe6c75d0ec9, m-togo-data-3210, m-ontology-micro-0000182.

Remaining source requirement: Identify the primary study or supplier specification behind M3210 triptone and confirm tryptone digestion/product scope; Togo annotation plus LB recipe pattern alone is insufficient for exact product mapping.

### 43: Sterile

`CM_NAME:4ba585285bcf878810bd999f17ae1e57a8b19c653af064c1b7c1ef86aef7e33e` — malformed_or_nonchemical_token

CCAP HSM has a stock heading Sterile 1% Marmite solution and a 1 ml addition of that stock; it has no ingredient called Sterile. The frozen token with1% was severed from this heading. This is a malformed extraction of a preparation qualifier. Preserve raw token as provenance and repair the upstream stock structure, not an ontology synonym.

Proposals: none. Evidence: m-frozen-shard, m-recipe-8e23a83a001ba7d8, m-ccap-HSM.

### 47: Double-distilled water

`CM_NAME:542bcb7906d3e7b505234f1f1f21e24df8439cddbaed833fea25ea52a4626069` — new_distinct_ingredient_proposal

Double distillation is an explicit preparation qualifier. MediaDive ingredient1021 names double distilled water and its filtered/anaerobic variants; CHEBI15377 supplies only the water molecular parent. The Distilled_Water owner explicitly rejects Double distilled water as an exact alias. Propose a separate material registry identity with broad water parent, preserving that rejection and without adding generic purified/tap-water synonyms.

Proposals: m-double_distilled_water. Evidence: m-frozen-shard, m-recipe-e1ed2566b12c2bf4, m-mediadive-ingredient-1021, m-ontology-chebi-15377, m-togo-data-3140.

### 52: Carbon source (i.e. cellobiose)

`CM_NAME:5ad29989465c45bf8f4a5ea9db78e4b2ca67fd2bc0cd1d0874a9061561187998` — existing_identity_or_alias

The original ATCC1203 CM4 PDF explicitly names cellobiose in parentheses in its6g carbon-source slot, matching the frozen Togo M2693 component. CHEBI17057 verifies the cellobiose concept. This supports a source-bound cellobiose interpretation of this exact recipe entry; it does not make the generic phrase Carbon source or unrelated alternatives resolving synonyms. Preserve role wording as occurrence context and the6g amount separately. The current Cellobiose owner has inherited generic role and alternative aliases that need complete payload review before release.

Proposals: none. Evidence: m-frozen-shard, m-recipe-0ec55e4c7fd007cf, m-atcc-cm4, m-ontology-cellobiose, m-togo-data-2693.

### 53: Cellobiose or Cellulose (MN 300)

`CM_NAME:5b1cb9f1f04660a2718ed741664db52ae12d885fb279849af97737920f36ebc7` — malformed_or_nonchemical_token

The word or joins cellobiose and cellulose MN300 as alternative substrates. JCM112 confirms that choice explicitly in CM3. The frozen cases retain varying amounts and source recipes; no single identity encompasses the disjunction. Preserve each original case and model a recipe alternative upstream, rather than merging cellobiose and cellulose or minting a false mixture.

Proposals: none. Evidence: m-frozen-shard, m-recipe-248c9f50441d6d77, m-jcm-112, m-togo-data-1849.

### 56: Methanol solution (see below)

`CM_NAME:606affef587ae82fbc1e2facd239d116a6bde1b08f7a1890f9ce14a67f4f8184` — new_distinct_ingredient_proposal

MediaDive S4591 belongs to JCM687 MB medium with methanol. The original JCM687 recipe defines Methanol solution as2.28 ml methanol plus50.0 ml distilled water. These are batch additions, not evidence of a52.28 ml measured final volume, pure methanol identity or an inferred molarity. Propose the specifically named JCM687 stock with unconverted component amounts.

Proposals: m-jcm687_methanol_solution. Evidence: m-frozen-shard, m-recipe-e7b5069dad091d1c, m-mediadive-solution-4591, m-jcm-687, m-mediadive-ingredient-1863.

### 57: Cellobiose or Cellulose MN 300

`CM_NAME:60fef9da8c390cc136078e4eab52f26bec12565c3ffc747e0e0e15d838019597` — malformed_or_nonchemical_token

The word or joins cellobiose and cellulose MN300 as alternative substrates. JCM112 confirms that choice explicitly in CM3. The frozen cases retain varying amounts and source recipes; no single identity encompasses the disjunction. Preserve each original case and model a recipe alternative upstream, rather than merging cellobiose and cellulose or minting a false mixture.

Proposals: none. Evidence: m-frozen-shard, m-recipe-3944082c46adb80b, m-recipe-30ccf0a48bbe19b4, m-recipe-f31ba08e0cd1491b, m-recipe-0689bbcbcbd85c54, m-recipe-b554d4b47ea40403, m-jcm-112, m-togo-data-1849.

### 58: Salt Solution I

`CM_NAME:633c7fc241861e69fcbda5b7af25616475ee0db2400677c1d9e1048c3ee7be11` — new_distinct_ingredient_proposal

Both frozen CultureMech contexts and MediaDive S4084/S5072 explicitly refer Salt Solution I to JCM133. JCM133 defines salt solution No.1 as K2HPO4 0.78 g and distilled water100 ml; salt solution No.2 is a different multicomponent stock. Preserve the stock stage and source-specific numbering; no identity with K2HPO4 solid or generic Salt Solution II.

Proposals: m-jcm133_salt_solution_i. Evidence: m-frozen-shard, m-recipe-d16869d4d19d35cf, m-recipe-9e1ad6dcdcc5646e, m-mediadive-solution-4084, m-mediadive-solution-5072, m-jcm-133.

### 63: Selenite-tungstate solution (see Medium No. 431)

`CM_NAME:7af57ea537b7e7a3a0e90c926bc62a599ba905329b046dfd8f311a2ebca109ab` — new_distinct_ingredient_proposal

The source recipe context, rather than the bare see Medium No.431 pointer, identifies the JCM431 selenite-tungstate formulation: NaOH0.4 g, Na2SeO3·5H2O6 mg, Na2WO4·2H2O8 mg, distilled water1 L. JCM1081 hyperlinks the JCM431 record; MediaDive S4878 uses ingredient1921 in its basal-minerals context. This differs from DSMZ S777 and JCM852. Promote only the matching current owner; retain both parenthesized and inherited unparenthesized source pointers as REJECTED_LABEL with their provenance, because neither pointer names its provider and neither supports global identity routing.

Proposals: m-jcm431_selenite_tungstate_solution. Evidence: m-frozen-shard, m-recipe-0c3498798fff516f, m-jcm-431, m-mediadive-solution-4878.

### 65: Solution A

`CM_NAME:80e5c7a588b15ce98b46cc30b94a6fa2d25a940ecc71ba04170bfb85ef58961f` — new_distinct_ingredient_proposal

MediaDive ingredient485 is used in S5359 and S5414. Both embedded Solution A sections contain MgSO4·7H2O0.123 g and CaCl2·2H2O0.015 g in10 ml distilled water. The preceding media differ, but this named supplement has the same explicit composition. Retain those two source-specific contexts; the generic name Solution A cannot become a universal alias for unrelated solutions.

Proposals: m-jcm1229_1272_solution_a. Evidence: m-frozen-shard, m-recipe-7ac2c80dd41008a1, m-recipe-b9159b567db82abb, m-mediadive-solution-5359, m-mediadive-solution-5414, m-mediadive-ingredient-485.

### 71: crystallized cane sugar

`CM_NAME:8c8cb4df5402a40f8cad687484b98bea494cccdb46541dd0e4ef2d654a233e9d` — unresolved

Crystallized cane sugar is a botanical-source food material, not necessarily analytical pure sucrose. FoodOn distinguishes refined cane sugar from brown cane sugar, and the source does not specify refinement or grade. A molecular sucrose link would erase material information. Togo M2844 prose confirms100g/L crystallized cane sugar andpH6, without refining the sugar grade.

Proposals: none. Evidence: m-frozen-shard, m-recipe-e9387801abfaa5c8, m-ols-sugar-cane-sugar, m-togo-2844, m-togo-data-2844.

Remaining source requirement: Recover the M2844 LGI source sugar grade/refinement or supplier specification to distinguish refined cane sugar, brown sugar and another crystallized cane product.

### 82: Tryptic Digest of Beef Heart

`CM_NAME:a12008c32afcfbe79a064472f43034a05d626eadd98d83e386d16ff2652efd3f` — new_distinct_ingredient_proposal

The primary DSMZ687/1331 formulations list tryptic digest of beef heart separately from the other peptones. It is a processed animal-tissue digest, distinct from beef-heart infusion, whole heart and the complete Columbia broth/agar. The retained capitalization variants carry the same explicitly named tissue and digestion process; no supplier interchangeability or nutrient-role claim is made.

Proposals: m-tryptic_digest_of_beef_heart. Evidence: m-frozen-shard, m-recipe-f9a3bf6a4e557151, m-dsmz-687, m-dsmz-1331, m-mediadive-ingredient-662, m-ols-tryptic-heart, m-togo-data-2256.

### 88: sludge from an anaerobic digester

`CM_NAME:a6b8c27c9e71456e8c2cfb1f12f93dffc7e3463a16ced6f6a140a1e990dd371a` — stock_product_mixture_context

Every KOMODO occurrence literally states sludge from an anaerobic digester at the provider rate49.46 g/L. The referenced DSMZ119 instead defines treated sludge fluid prepared with yeast extract, incubation, centrifugation and sterilization. That is useful contrasting primary evidence, not permission to rewrite all KOMODO raw material observations as the prepared supernatant or infer density. Retain source labels and existing source-material holds.

Proposals: none. Evidence: m-frozen-shard, m-recipe-64d7389f562312aa, m-recipe-c15b61ed6be41868, m-recipe-e7f55f29b5120302, m-recipe-0f97cd8635b94586, m-recipe-662388e4063d2270, m-recipe-ea3d658f456884ad, m-recipe-b6eab993e367b24e, m-recipe-d9bee896841c20b8, m-recipe-64e6175631ce45d0, m-recipe-091e32649b85c3d3, m-recipe-a6e19a5070dfb9ab, m-recipe-23d5cdb0db7ad181, m-recipe-dc95596dbe88ebce, m-recipe-2b27bde039af5029, m-recipe-da16ef17c9167a84, m-recipe-0d4a6e7d530e8078, m-dsmz-119.

Remaining source requirement: Source-level reconciliation is required to determine whether each KOMODO rate represents raw sludge or the DSMZ119 processed supernatant; preserve rate units until that is resolved.

### 89: Metals "44"

`CM_NAME:a6e208f605caf46b65f9a1a1a59f4fdc932fa99f2eda3152cb614b0d75aa2b54` — existing_identity_or_alias

JCM900 and JCM304 route their Metals44 supplement to JCM149. Its trace-metal formulation and MICRO0000456 exact synonyms support the punctuation variants Metals "44" and Metals44 on the current owner, preserving the source recipe and nested stock dose. No substitution for an arbitrary trace-metal mixture is supported.

Proposals: m-metals44_source_aliases. Evidence: m-frozen-shard, m-recipe-6b36dddf6465e371, m-jcm-149, m-jcm-304, m-jcm-900, m-ontology-micro-0000456.

### 94: arabinan (sugar beet)

`CM_NAME:b7090f12b13a2d567fe1e3962a3ce2907e42826a7f4b588f70d9b78b1eccbae6` — existing_identity_or_alias

The source explicitly qualifies arabinan by sugar-beet origin. The current Arabinan_From_Sugar_Beet owner preserves that source and CAS11078-27-6 with an asymmetric CHEBI22590 arabinan parent; manufacturer P-ARAB independently corroborates the botanical material and CAS. Add the parenthesized source-qualified alias without erasing origin or changing the resolved #312 parent decision. This does not assert a specific Megazyme product/grade was used in M2313. Togo M2313 original prose explicitly identifies the sugar-beet arabinan option at0.2%; its other carbon sources are alternatives, not co-components.

Proposals: m-arabinan_source_alias. Evidence: m-frozen-shard, m-recipe-a1c2ef58d6c02968, m-arabinan-supplier, m-ontology-arabinan, m-togo-2313, m-togo-data-2313.

### 97: Liver digest (Oxoid LP0027)

`CM_NAME:bea2e3317eb75071d036f3149b10993facf75005d43e101c07afa7579794db14` — new_distinct_ingredient_proposal

CCAP MC explicitly names Oxoid LP0027. The manufacturer product description identifies neutralized papaic ox-liver digest; generic MICRO0001668 liver digest does not encode that supplier/process specificity. Propose a distinct LP0027 material with broad liver-digest parent, preserving catalog identity rather than making every liver digest interchangeable.

Proposals: m-oxoid_lp0027_liver_digest. Evidence: m-frozen-shard, m-recipe-130ffe6c71f41a82, m-ccap-MC, m-liver-spec, m-ontology-micro-0001668.

### 101: CAS amino acids

`CM_NAME:c60717c13b3c741d3abd4431ec51ccab46ac3962ea46ff95e70c8b97f9d9cc3a` — unresolved

The label CAS amino acids is consistent with an abbreviation of Casamino acids but has no supplier/catalog or explicit acid-hydrolysis statement. The frozen BSM contains a50 g/L entry alongside other suspiciously scaled nutrients. Do not infer acid-hydrolyzed casein identity or a corrected dose from the spelling alone. Togo M2237 confirms raw CAS amino acids50g and Casamino acid annotation, while naming a modified Hareland1975 basal medium; annotation alone does not establish acid-hydrolysis supplier identity or repair scaling.

Proposals: none. Evidence: m-frozen-shard, m-recipe-3b7a45d113c023b8, m-togo-2237, m-supplier-casitone, m-togo-data-2237.

Remaining source requirement: Recover TOGO M2237 original preparation and supplier identity for CAS amino acids, including whether it is Casamino acids and the unscaled ingredient amount.

### 111: Metals 44

`CM_NAME:dd759eba8ada7b3e6aa498104056de938ddf68f3a132837431aaec01a06f2d7b` — existing_identity_or_alias

JCM900 and JCM304 route their Metals44 supplement to JCM149. Its trace-metal formulation and MICRO0000456 exact synonyms support the punctuation variants Metals "44" and Metals44 on the current owner, preserving the source recipe and nested stock dose. No substitution for an arbitrary trace-metal mixture is supported.

Proposals: m-metals44_source_aliases. Evidence: m-frozen-shard, m-recipe-eb5c4a19c88aead0, m-recipe-0eac42ce93708326, m-recipe-a690776fde78ed2d, m-recipe-e99e029eb5df3532, m-jcm-149, m-jcm-304, m-jcm-900, m-ontology-micro-0000456.

### 112: Desiccated ox bile

`CM_NAME:dde7aedb87c8cbe3a8ee2c895bd1bc57bf06f833138d09fbba441bedbbd58def` — existing_identity_or_alias

JCM1449 uses desiccated ox bile20 g per liter. The manufacturer describes oxgall/oxbile as dehydrated bile; this supports the processing-qualified material name and correction of the existing Desicatted_Ox-bile spelling. Retain that owner as unmapped pending reconciliation with the separate Oxgall and Ox-bile records; this alias proposal does not merge them or promote a broad ontology parent to exact identity.

Proposals: m-desiccated_ox_bile_label. Evidence: m-frozen-shard, m-recipe-9bcf0e5b9d1f9c0a, m-jcm-1449, m-supplier-oxgall-alpha, m-ontology-micro-0000610.

### 123: Selenite-tungstate solution

`CM_NAME:fef0391344c383fe93459d6562a1fd9689c473ab98703b37785de5d40ca7a8df` — stock_product_mixture_context

This one source-name case spans three stock identities: TOGO/JCM1081 contexts reference JCM431 (0.4g NaOH/6mg Se salt/8mg W salt per source L); S446/S453 explicitly reference DSMZ S777 (0.5g/3mg/4mg); S5270/S5299/S5300/S5307 reference JCM852 (1.7mg Se salt/3.3mg W salt, no NaOH). Keep all8 occurrences and split routing by source context. Never assign the unqualified label as a resolving global alias of any one formulation. The inherited unparenthesized Medium No.431 pointer is also REJECTED_LABEL; only the retained source-context routing identifies JCM431.

Proposals: m-jcm431_selenite_tungstate_solution, m-dsmz_s777_selenite_tungstate_solution, m-jcm852_se_w_solution. Evidence: m-frozen-shard, m-recipe-db1df4848f160fd4, m-recipe-7f44410f46ff4844, m-recipe-ea2919b5394e74b2, m-recipe-8fddb698da662d43, m-recipe-2af7a5cc23abf6a5, m-recipe-6568f6204e55ff39, m-recipe-65c1faf090410dd2, m-recipe-da7ea7e5241db528, m-jcm-431, m-jcm-1081, m-mediadive-solution-777, m-jcm-852, m-mediadive-solution-446, m-mediadive-solution-453, m-mediadive-solution-5270, m-mediadive-solution-5299, m-mediadive-solution-5300, m-mediadive-solution-5307.

### 125: Sugar beet molasses

`KG_CASE:1a6656cf3993232e8ecb72099874b08672ee59d89b7cdc5c77f717f37a8e3f99` — supplied_form_correction

The current FOODON00003412 term is sugar-beet root, while the material is molasses, a sugar-refining syrup. Exact FOODON03543005 explicitly includes molasses obtained from sugar beet and is nonobsolete in the retrieved ontology. Propose that exact material concept and canonical label, preserving original history and the WITHHOLD release obligation until the changed complete payload is independently reviewed.

Proposals: m-sugar_beet_molasses_identity. Evidence: m-frozen-shard, m-ontology-foodon-00003412, m-ontology-foodon-03543005, m-mediadive-ingredient-346.

### 131: Pancreatic digest of casein

`KG_CASE:318a9bc7039f8ac67acef5c4e33723891a22947a53d1b1d1e1af1989094c760a` — stock_product_mixture_context

The supplier and primary MediaDive ingredient pages distinguish pancreatic/enzymatic casein digestion and commercial alternatives; they do not make every acid, enzymatic, tryptone and Casitone preparation identical. The current Casein_Peptone owner carries a broad hydrolyzed milk-protein grounding plus conflicting process/product aliases and a native WITHHOLD. Source-level digest identity is supported, but this review does not clear that complete owner payload or select a proprietary digest not named in the frozen occurrence.

Proposals: none. Evidence: m-frozen-shard, m-mediadive-ingredient-531, m-mediadive-ingredient-645, m-supplier-casitone.

Remaining source requirement: Reconcile Casein_Peptone acid-versus-enzymatic aliases and product-specific evidence under #669/#704 before admitting these source-specific assertions.

### 132: sugar

`KG_CASE:33c13b23fafbf9588be9c5570e87b1ec40a840bd1da2c1616a3cd9f3913d1478` — unresolved

These are distinct MicrobeDecoder records1200 (Alkaliflexus imshenetskii) and6810 (Gardnerella vaginalis), each with literal sugar in Bergey_Substrates_for_end_products. Their retained material policy explicitly preserves separate record-scoped unresolved nodes and forbids substitution with NCIT:C71939 or merger. Full raw records were inspected; both Bergey DOI retrievals failed. Organism sugar metabolism does not identify the unspecified substrate.

Proposals: none. Evidence: m-frozen-shard, m-bergey-failed, m-microbedecoder-1200.

Remaining source requirement: Obtain the exact cited Bergey chapter passage naming the substrate for this record; absent explicit identity retain its existing record-scoped unresolved node and original citation.

### 136: V8 canned vegetable juice

`KG_CASE:499d227e7accc36224f67658431757734c8009a5119d0f586ced6b81c3258f3a` — stock_product_mixture_context

The frozen record identifies Campbell V8 canned vegetable juice; the manufacturer has Original, Low Sodium and Spicy products with differing recipes. Its current Original product ingredient list is a complex vegetable blend with additives, not evidence that the unspecified historical can was that exact variant. Preserve the current source-specific unmapped owner rather than map to a vegetable taxon or invent exact formulation.

Proposals: none. Evidence: m-frozen-shard, m-mediadive-ingredient-1616, m-supplier-v8.

Remaining source requirement: Identify source product variant, era/catalog and preparation (e.g. clarification) before an exact formulation or product-owner promotion.

### 138: sugar

`KG_CASE:4fb6d439270ed94097d3ade71c3f52468c7b915b2bcff39b0fadcbc4b223aa19` — unresolved

These are distinct MicrobeDecoder records1200 (Alkaliflexus imshenetskii) and6810 (Gardnerella vaginalis), each with literal sugar in Bergey_Substrates_for_end_products. Their retained material policy explicitly preserves separate record-scoped unresolved nodes and forbids substitution with NCIT:C71939 or merger. Full raw records were inspected; both Bergey DOI retrievals failed. Organism sugar metabolism does not identify the unspecified substrate.

Proposals: none. Evidence: m-frozen-shard, m-bergey-failed, m-microbedecoder-6810.

Remaining source requirement: Obtain the exact cited Bergey chapter passage naming the substrate for this record; absent explicit identity retain its existing record-scoped unresolved node and original citation.

### 140: Cellobiose or Cellulose MN 300

`KG_CASE:565623accabec87a86753ba261837da0a705a3465b4ea23c6c697d65b475c410` — malformed_or_nonchemical_token

The word or joins cellobiose and cellulose MN300 as alternative substrates. JCM112 confirms that choice explicitly in CM3. The frozen cases retain varying amounts and source recipes; no single identity encompasses the disjunction. Preserve each original case and model a recipe alternative upstream, rather than merging cellobiose and cellulose or minting a false mixture.

Proposals: none. Evidence: m-frozen-shard, m-jcm-112.

### 142: Salt Solution I

`KG_CASE:5c5fe7ef6f3ecf34a969a0c5f3c88dc09cb6964cd17232b9afff94dfdf52808d` — new_distinct_ingredient_proposal

Both frozen CultureMech contexts and MediaDive S4084/S5072 explicitly refer Salt Solution I to JCM133. JCM133 defines salt solution No.1 as K2HPO4 0.78 g and distilled water100 ml; salt solution No.2 is a different multicomponent stock. Preserve the stock stage and source-specific numbering; no identity with K2HPO4 solid or generic Salt Solution II.

Proposals: m-jcm133_salt_solution_i. Evidence: m-frozen-shard, m-mediadive-solution-4084, m-mediadive-solution-5072, m-jcm-133.

### 144: Selenite-tungstate solution

`KG_CASE:5f2bca14ac1099323f6fd9d78e58180bd53c8b26eeb0ebc2c3c9aebf314d9e06` — new_distinct_ingredient_proposal

The raw mediadive.ingredient:88 occurrence explicitly says Medium No.852. JCM852 defines an aqueous selenium/tungsten stock containing Na2SeO3·5H2O1.7 mg and Na2WO4·2H2O3.3 mg per source liter, no NaOH. The embedded historic CHEBI88 citronellol candidate is unrelated and stays quarantined; the numeric compound ID is not a ChEBI accession. Propose only the JCM852 source-qualified stock.

Proposals: m-jcm852_se_w_solution. Evidence: m-frozen-shard, m-jcm-852, m-mediadive-solution-5270.

### 150: Polar lipid fraction

`KG_CASE:8c71bc7f5602194dfc3edfd54b9ec2e2bf092e9c1cff30e7191ff9e90dff981b` — stock_product_mixture_context

The source explicitly allows a polar lipid fraction aqueous suspension prepared from any Archaeon, filter sterilized, with adjustable10 ml/L dose. This is a variable extracted biological fraction, not one archaeal lipid molecule or pure solvent. Preserve its existing unmapped material record and do not infer organism, extraction method, concentration or chemical composition.

Proposals: none. Evidence: m-frozen-shard, m-mediadive-ingredient-2081.

Remaining source requirement: For a narrower molecular/recipe mapping obtain archaeal source, extraction/fractionation method and measured suspension composition; the generic source intentionally permits multiple preparations.

### 153: Methanol solution (see below)

`KG_CASE:9323fac188d298c472186217daf59a7ce3f8ef448bcc384eabad54757cddb173` — new_distinct_ingredient_proposal

MediaDive S4591 belongs to JCM687 MB medium with methanol. The original JCM687 recipe defines Methanol solution as2.28 ml methanol plus50.0 ml distilled water. These are batch additions, not evidence of a52.28 ml measured final volume, pure methanol identity or an inferred molarity. Propose the specifically named JCM687 stock with unconverted component amounts.

Proposals: m-jcm687_methanol_solution. Evidence: m-frozen-shard, m-mediadive-solution-4591, m-jcm-687, m-mediadive-ingredient-1863.

### 157: Enzymatic digest of casein

`KG_CASE:9b2349c9e187b643df526d23631199af18b9ef91ad3edc94b94d2a9167bf1b70` — stock_product_mixture_context

The supplier and primary MediaDive ingredient pages distinguish pancreatic/enzymatic casein digestion and commercial alternatives; they do not make every acid, enzymatic, tryptone and Casitone preparation identical. The current Casein_Peptone owner carries a broad hydrolyzed milk-protein grounding plus conflicting process/product aliases and a native WITHHOLD. Source-level digest identity is supported, but this review does not clear that complete owner payload or select a proprietary digest not named in the frozen occurrence.

Proposals: none. Evidence: m-frozen-shard, m-mediadive-ingredient-531, m-mediadive-ingredient-645, m-supplier-casitone.

Remaining source requirement: Reconcile Casein_Peptone acid-versus-enzymatic aliases and product-specific evidence under #669/#704 before admitting these source-specific assertions.

### 158: Liver Concentrate

`KG_CASE:9c6af5ad4e367fe67a70da6bb5dea66d7fe5d8a365159cec4bd8318d2d8f792b` — stock_product_mixture_context

Liver Concentrate is retained as a separate source material. MediaDive assigns a CAS through automatic enrichment, while the neighboring Liver_Extract_Concentrate owner itself has only stem-match history to a generic liver-extract term. Neither establishes the source process, concentration basis or equality to digest/powder/extract. Preserve source identity and no inferred biochemical composition.

Proposals: none. Evidence: m-frozen-shard, m-mediadive-ingredient-935.

Remaining source requirement: Recover the source supplier/catalog and concentration/extraction process for mediadive.ingredient:935 before merging with liver-extract or liver-digest owners.

### 162: Phosphates solution

`KG_CASE:a64bd5c62e3a2e633891b9ef9eb9f584614fce02b6d8a00e8443dde07ccdd6b4` — new_distinct_ingredient_proposal

JCM1199 defines the phosphates stock as Na2HPO4·2H2O 2.44 g, KH2PO4 1.52 g and distilled water1 L, pH6.9; it adds100 ml stock after autoclaving. MediaDive S5318 flattens the stock body alongside its100 ml input, so the provider-derived percentages must not be interpreted as the stock formula or whole-medium dose. Propose a JCM1199-specific buffer identity.

Proposals: m-jcm1199_phosphates_solution. Evidence: m-frozen-shard, m-jcm-1199, m-mediadive-solution-5318.

### 163: Double distilled water

`KG_CASE:a7586381b4a8cdecd6dd067c3f49195e03577deba5715f29d907d4379803ac71` — new_distinct_ingredient_proposal

Double distillation is an explicit preparation qualifier. MediaDive ingredient1021 names double distilled water and its filtered/anaerobic variants; CHEBI15377 supplies only the water molecular parent. The Distilled_Water owner explicitly rejects Double distilled water as an exact alias. Propose a separate material registry identity with broad water parent, preserving that rejection and without adding generic purified/tap-water synonyms.

Proposals: m-double_distilled_water. Evidence: m-frozen-shard, m-mediadive-ingredient-1021, m-ontology-chebi-15377.

### 165: Selenite-tungstate solution (see Medium No. 431)

`KG_CASE:aa90b6b77f1a663fb5586f7b823e46b7037b9838ff6f881eb339966cd909872b` — new_distinct_ingredient_proposal

The source recipe context, rather than the bare see Medium No.431 pointer, identifies the JCM431 selenite-tungstate formulation: NaOH0.4 g, Na2SeO3·5H2O6 mg, Na2WO4·2H2O8 mg, distilled water1 L. JCM1081 hyperlinks the JCM431 record; MediaDive S4878 uses ingredient1921 in its basal-minerals context. This differs from DSMZ S777 and JCM852. Promote only the matching current owner; retain both parenthesized and inherited unparenthesized source pointers as REJECTED_LABEL with their provenance, because neither pointer names its provider and neither supports global identity routing.

Proposals: m-jcm431_selenite_tungstate_solution. Evidence: m-frozen-shard, m-jcm-431, m-mediadive-solution-4878.

### 167: Sugar

`KG_CASE:abc1616e7755bfd211934d5dd7d9116e1e50981eb3c4fe8f6cd481a6c5ecedec` — new_distinct_ingredient_proposal

The raw Sugar occurrence is explicitly a solution containing250 mM each of xylose, maltose and cellobiose. JCM537 confirms that stock and its0.1 ml dose per5 ml culture. The MediaDive page adds automatic sucrose identifiers despite that qualifier; they are contradicted by the source formulation. Preserve the downstream material hold and propose a distinct mixed-sugar stock, never NCIT food sugar or sucrose.

Proposals: m-jcm537_sugar_solution_250mm. Evidence: m-frozen-shard, m-jcm-537, m-mediadive-ingredient-1795.

### 168: Wheat Grains

`KG_CASE:ac0116dac4cc79abb99c7353b23d72128d477c526686419a591869eeaadb46ca` — stock_product_mixture_context

The source material is wheat grains autoclaved121C20min, not wheat flour, starch or a single carbohydrate. The primary ingredient page corroborates the processing qualifier. FoodOn search returns species/refinement-specific grain classes, which do not identify the unstated source cultivar/species and whole-versus-processed grain. Preserve the current raw-material owner without forcing an unsupported class.

Proposals: none. Evidence: m-frozen-shard, m-mediadive-ingredient-2346, m-ols-wheat-grain.

Remaining source requirement: Verify grain botanical species and processing state or a directly matching generic material term before promotion; retain autoclaving as preparation context.

### 169: Solution A

`KG_CASE:ac86285e735a1fbe85d3e405260aba228a279205ab264a40635d07caab6be3a3` — new_distinct_ingredient_proposal

MediaDive ingredient485 is used in S5359 and S5414. Both embedded Solution A sections contain MgSO4·7H2O0.123 g and CaCl2·2H2O0.015 g in10 ml distilled water. The preceding media differ, but this named supplement has the same explicit composition. Retain those two source-specific contexts; the generic name Solution A cannot become a universal alias for unrelated solutions.

Proposals: m-jcm1229_1272_solution_a. Evidence: m-frozen-shard, m-mediadive-solution-5359, m-mediadive-solution-5414, m-mediadive-ingredient-485.

### 170: Tryptic Digest of beef heart

`KG_CASE:afe662a4ecdc143ab8b82d6f649c7fb2cb4079ddef964b2157953343c4cd7309` — new_distinct_ingredient_proposal

The primary DSMZ687/1331 formulations list tryptic digest of beef heart separately from the other peptones. It is a processed animal-tissue digest, distinct from beef-heart infusion, whole heart and the complete Columbia broth/agar. The retained capitalization variants carry the same explicitly named tissue and digestion process; no supplier interchangeability or nutrient-role claim is made.

Proposals: m-tryptic_digest_of_beef_heart. Evidence: m-frozen-shard, m-dsmz-687, m-dsmz-1331, m-mediadive-ingredient-662, m-ols-tryptic-heart, m-togo-data-2256.

### 176: Oxgall

`KG_CASE:d10da097ff2bcd5a27f755db528ff5e86af9e25a33ad8e5483a935c2b8f28857` — stock_product_mixture_context

The manufacturer defines oxgall/oxbile as dehydrated fresh bile, supporting a complex processed animal material rather than a single bile acid. Current Oxgall, Desicatted_Ox-bile and Ox-bile owners represent overlapping but not yet reconciled scope and provenance; MICRO0000610 only names ox bile. This case supports a deduplication investigation, not an automatic identity merge or exact fresh-bile equivalence.

Proposals: none. Evidence: m-frozen-shard, m-supplier-oxgall-alpha, m-mediadive-ingredient-1656, m-ontology-micro-0000610.

Remaining source requirement: Reconcile the three existing bile owners and source product/process evidence before promoting Oxgall or transferring aliases.

### 186: Tap water

`KG_CASE:f49035acede4ed56123d290fc9800b00eaf48f760845a84ec91178bc1bd7c741` — stock_product_mixture_context

The frozen source calls for1000 ml Tap water. The public ingredient page automatically associates molecular water, but tap water is a compositionally variable supplied material; the existing distilled-water owner explicitly rejects this alias. Retain that rejection. No chemical purity, distillation or specific mineral composition follows from a water molecular formula.

Proposals: none. Evidence: m-frozen-shard, m-mediadive-ingredient-322, m-ontology-chebi-15377.

Remaining source requirement: A material-level tap-water concept or locality/supply characterization is needed; do not reinstate the rejected distilled-water alias.


Independent skeptical review completed by `/root/chemicals`: [review capture](../chemicals/independent-review-of-materials.json), SHA256 `2625ce3c28ccf98b774e18ab27298e2902e9ea7d4c56bbb7b2bf2379c658ac99`. All51 cases and20 proposal payloads are bound by exact hashes; no blocking findings remain. This does not clear native publication holds.


The initial material review missed one inherited resolving JCM431 pointer alias. Its prior exact inputs and payload remain in `superseded/jcm431-pointer-v1`; `jcm431-pointer-correction.json` records the correction and supersession. The inherited label now remains as REJECTED_LABEL with its original mim-queue provenance. Fresh independent review of the changed bytes is pending. The named Metals44 stock remains supported by the matching JCM149 and MICRO0000456 formulas; see `metals44-pointer-assessment.json`.

The corrected JCM431 bytes have now passed renewed independent review by `/root/chemicals`; the final receipt is `chemicals/independent-review-of-materials.json`, SHA256 `538eaf7b66609279db6e4d6544b53d4a87a3aa469fab256bfa81dc1fcbde70af`. `post-review-adjudication.json` records the final status without changing the reviewer-bound correction receipt. No blocking material findings remain; publication and inherited-owner holds remain intact.
