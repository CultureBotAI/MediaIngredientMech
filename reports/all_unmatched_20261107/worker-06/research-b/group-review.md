# Worker06 research-b source review

Scope: indices 47–93 inclusive, 47 cases and 25 proposed payloads. Research A independently reviewed all 47 cases and all 25 final payloads in review-b-v6.json, with source limitations retained. No maintained YAML/SSSOM changed.

Original case digests, all occurrence IDs, raw labels, complete frozen contexts and real primary captures remain preserved. Proposals remain isolated; native owner/source/export release obligations are separate from completed source-specific proposals.

## 47: Bacto-yeast

The live TOGO M2497 record retains the raw Bacto-yeast label but explicitly assigns its component GMO_001018 and the label Bacto Yeast extract; its accompanying recipe specifies 5 g in the LB preparation. This supports a source-backed yeast-extract spelling alias, not a whole-cell yeast identity. FOODON:03315426 provides the yeast-extract class already used by the owner. No particular lot composition is inferred.

Applies to the single LB occurrence CultureMech:009070. The primary database component annotation resolves the otherwise truncated label; the other LB components and water remain separate.

Disposition: existing_identity_or_alias. Proposals: B-P-Yeast_Extract.

## 48: Trace mineral

TOGO M2760 supplies an explicit Trace mineral subrecipe and doses it at 10 ml, contradicting the frozen 10 G_PER_L interpretation. Its NTA-containing stock includes NaCl, CaCl2 dihydrate, boric acid, iron/manganese/cobalt/copper/zinc/selenium/nickel salts, and the raw formula Na2MoO3. That last formula cannot silently become ordinary sodium molybdate Na2MoO4. The generic existing trace-mineral owner is not an established formulation match.

Applies only to the PBBM occurrence CultureMech:009311. The full live component list is retained, including the questionable molybdenum formula; it is not evidence for every Trace mineral label.

Disposition: stock_product_mixture_context. Proposals: none.

Do not attach an exact generic-stock alias while the source formulation contains unresolved Na2MoO3.

Remaining requirement: Recover the primary PBBM formulation cited by TOGO (PMID:16232686) or a provider correction specifying the molybdenum reagent and its hydrate; then mint a PBBM-qualified stock with the exact formulation.

## 49: Pantothenic acid calcium salt

Both frozen occurrences trace to ATCC1191 vitamin stock. Its primary PDF names Pantothenic acid calcium salt, 50 mg in 500 ml vitamin stock; neither the recipe term nor the PDF specifies D or DL. CHEBI:31345 and the existing Calcium_Pantothenate owner denote the D salt. The existing owner aliases cannot supply missing stereochemistry, and the frozen 50 G_PER_L value is a flattened stock amount rather than a valid medium concentration.

Covers both CultureMech:009627 and009249, which reference the same vitamin stock despite differing whole-medium names.

Disposition: unresolved. Proposals: none.

No exact alias to a D-specific owner is justified by an unspecified calcium salt.

Remaining requirement: Obtain the ATCC1191 preparation specification or historical supplier/catalogue identity identifying D versus DL and hydration for the actual pantothenate reagent.

## 50: Haemin solution

MediaDive main solution606 explicitly links solution124, not a pure compound. Solution124 is 50 mg haemin with 1 ml 1 N NaOH, diluted to 100 ml and filter sterilized. Thus 0.05% w/v is stock strength and 2 ml is the recipe dose. MICRO:0001598 existing owner is an unformulated hemin-solution record and does not by itself establish equivalence to every alkaline haem stock.

The sole occurrence in CultureMech:014786 exposes solution_id124 and the parent solution606; the concrete proposed source-specific stock is bound to that explicit identifier.

Disposition: stock_product_mixture_context. Proposals: B-P-MediaDive124-haemin.

## 51: Na2CO3 (5% w/v)

DSMZ135 and339a use sodium carbonate as a 5% w/v solution for anaerobic pH adjustment. The supplied object is an aqueous stock, not anhydrous Na2CO3 or the carbonate anion. The current Sodium_Carbonate_Solution owner carries a solute CHEBI identity and lacks a verified formulation, so adding this concentration-bearing string there would perpetuate the stock/solute collapse.

Both source recipes preserve 5% w/v; their use as pH-adjustment reagent does not give a fixed final-medium concentration.

Disposition: new_distinct_ingredient_proposal. Proposals: B-P-DSMZ135-339a-carbonate5.

Remaining requirement: The source-specific proposal avoids the incorrect generic solute-grounded owner; exact solute hydrate and complete preparation remain unspecified.

## 52: Trace element mixture*

NBRC1257 and1321 print the same trace-element stock: acidified iron(II) sulfate heptahydrate plus the other specified trace constituents and water. The two frozen filenames have shifted numbers, so the embedded NBRC identifiers and live compositions, not filenames alone, establish equivalence. This supports one NBRC-qualified stock record. Amounts are preserved as batch inputs because12.5 ml HCl plus987 ml water is not an explicit volumetric make-up to1 L.

Both occurrences are the starred Trace element mixture of NBRC1257/1321; each source doses1 ml into the parent medium. Generic star labels remain in evidence/notes instead of a global resolving synonym.

Disposition: new_distinct_ingredient_proposal. Proposals: B-P-NBRC1257-1321.

## 53: Trace element solution*

The three NBRC recipes1226,335 and392 define different trace-element solutions:1226 uses a high-NTA iron(III) formulation,335 uses a tartrate-based stock, and392 uses a lower-NTA magnesium-rich stock. Their shared starred label is a local table reference, not a substance identity. The335 source also prints H3BO4, which requires source clarification before chemical normalization. Separate exact payloads now capture NBRC1226 and392 for their own occurrence IDs. The NBRC335 occurrence remains unresolved because its primary boron formula is H3BO4; no global synonym or formulation-equivalence claim is made.

All three frozen occurrences are retained. B-P-NBRC1226-TRACE applies only to CultureMech:007465/nbrc.medium:1226; B-P-NBRC392-TRACE only to CultureMech:007492/nbrc.medium:392. CultureMech:007488/nbrc.medium:335 remains unresolved and is excluded from both proposals. Filename number offsets do not change the embedded source identifiers.

Disposition: stock_product_mixture_context. Proposals: B-P-NBRC1226-TRACE, B-P-NBRC392-TRACE.

Remaining requirement: Obtain a primary NBRC335 correction identifying the H3BO4 reagent and its supplied form before proposing that separate stock. Apply1226/392 proposals only to their enumerated occurrence IDs; no globally resolving Trace element solution* alias.

## 54: Proteose yeastolate (TC) (DIFCO 5577-15)

DSMZ403 BSK medium specifies Proteose yeastolate (TC), DIFCO5577-15, as a1 g commercial component. Its catalogue number and TC qualification are stronger identity constraints than the generic Proteose yeastolate placeholder. This is a complex commercial preparation; neither a single amino acid nor generic yeast extract is an exact identity. Baseline owner provenance specifically identifies MediaDive460, whose current primary entry points to DSMZ403. This permits a bounded catalogue/form annotation on that established owner, preserving UNMAPPED rather than minting a duplicate or inventing composition.

Applies to the sole BSK occurrence and the exact existing source460-derived owner. TC and Difco5577-15 are preserved as source qualifications; no generic global product-successor relationship is claimed.

Disposition: stock_product_mixture_context. Proposals: B-P-PROTEOSE-TC5577.

Remaining requirement: Legacy molecular composition, lot/version details and any successor relationship remain unverified. Those limits do not prevent the bounded source/catalogue annotation; full native changed-owner review and release remain separate.

## 55: Trace element solution SL7**

NBRC1117 explicitly defines SL7 with HCl25%, iron(II) chloride tetrahydrate, ZnCl2, manganese/cobalt/copper/nickel chlorides, boric acid and sodium molybdate dihydrate. Its boron/cobalt/copper/nickel/molybdate amounts differ from the commonly named SL10 stock; naming similarity cannot justify that alias. A source-qualified SL7 stock with its own component assertion is supported.

The sole frozen occurrence links NBRC1117 even though the normalized filename ends1118. The primary starred subsection resolves the double-star label precisely.

Disposition: new_distinct_ingredient_proposal. Proposals: B-P-NBRC1117-SL7.

## 56: Trace salts solution*

NBRC268 ISP4 defines the starred trace salts stock as0.1 g each FeSO4·7H2O, MnCl2·4H2O and ZnSO4·7H2O with100 ml distilled water. The parent recipe receives1 ml. This is a defined three-salt stock, not an alias for a trace-element chemical or a generic broad trace-mineral mixture.

The one frozen NBRC270 filename contains source identifier NBRC268; formulation provenance uses that actual source identifier. Batch amounts are transcribed without claiming an unreported final volumetric concentration.

Disposition: new_distinct_ingredient_proposal. Proposals: B-P-NBRC268-trace-salts.

## 57: Trace vitamins

JCM1009,825 and837 refer their Trace vitamins component to JCM197, a ten-vitamin stock. TOGO3181 instead explicitly defines biotin0.1 g, p-aminobenzoic acid1 g and thiamine1 g per litre for Rhodospirillaceae medium. This generic-label case therefore has at least two real formulations and cannot resolve globally to JCM197. A current-source-specific RM vitamin stock is now proposed from the mutually consistent narrative and component table. The other three occurrences explicitly reference JCM197 and may link to that existing proposed formulation only by occurrence scope.

B-P-TOGO3181-RM-VITAMINS applies only to CultureMech:009631 (RM). CultureMech:007583,013726 and013742 link to JCM197 by the source-defined references; they are explicitly excluded from the RM stock. A generic Trace vitamins synonym on either stock is prohibited.

Disposition: stock_product_mixture_context. Proposals: B-P-TOGO3181-RM-VITAMINS.

Remaining requirement: Apply exact occurrence scopes: RM is the three-vitamin stock; the other three occurrences use JCM197. Any future thiamine salt/hydrate or biotin stereochemistry mapping requires reagent evidence; historical-paper equivalence is not asserted.

## 58: Fresh yeast extract

The live SP4 source expands Fresh yeast extract to a25% solution of fresh baker's yeast extract and doses35 ml. It separately contains Difco TC yeastolate2% solution, demonstrating that these preparations are not interchangeable. The frozen nested ingredient lost part of the supplied-stock context. A generic dry yeast-extract alias would lose preparation and concentration identity.

Applies to CultureMech:009489 SP4, including its stock parent and neighbouring yeastolate component.

Disposition: stock_product_mixture_context. Proposals: none.

No extraction protocol, percentage basis or commercial product specification establishes a complete owner payload for this fresh preparation.

Remaining requirement: Obtain the SP4 fresh baker's yeast extraction procedure and the meaning of25% (biomass basis versus extract solids), preserving its35 ml medium dose separately.

## 59: 0.17 mM FeCl3 x 6 H2O

DSMZ1033 Thermus medium lists10 ml of0.17 mM FeCl3·6H2O stock. The label states a dilute stock made from a specific hydrate; neither10 G_PER_L nor pure ferric chloride hexahydrate is the identity of the supplied solution. Its concentration and hydrate can be represented without converting it into an anhydrous salt.

The single TOGO2298 occurrence uses the DSMZ1033 recipe. The proposed stock preserves the0.17 mM formulation and leaves the10 ml usage in occurrence provenance.

Disposition: stock_product_mixture_context. Proposals: B-P-DSMZ1033-ferric-stock.

## 60: Trace metal mix A5 + Co

The live TOGO2601 BG11 source provides a six-salt A5+Co stock, including0.390 g Na2MoO4·2H2O per litre and0.0494 g cobalt nitrate hexahydrate. ATCC957/1047 A5 in case73 instead uses0.039 g molybdate, a tenfold difference. Existing generic A5/BG11 stock owners lack a formulation binding, so neither label warrants collapsing the two versions.

The source-specific proposed TOGO2601 stock applies only to the BG11 occurrence CultureMech:009170; component masses are copied from its subrecipe.

Disposition: new_distinct_ingredient_proposal. Proposals: B-P-TOGO2601-A5Co.

## 61: Trace element solution (see below)

JCM1435 LN medium and JCM1465 modified NMS4 each say see below but define different trace-metal mixtures. The1435 stock is NTA-based with FeCl2 tetrahydrate, while1465 lists copper sulfate, iron sulfate and other metals at different amounts. The local pointer text cannot be exported as an exact synonym of one formulation. The1465 table also prints H3BO2, which should not be silently corrected. A source-qualified JCM1435 payload now transcribes its full listed inputs and KOH preparation reagent. The source-defined JCM1465 H3BO2 ambiguity remains unresolved; neither source label becomes a global stock alias.

CultureMech:015867/JCM1435 alone is covered by B-P-JCM1435-TRACE, with its10ml usage. CultureMech:015872/JCM1465 is retained and explicitly excluded from this stock proposal.

Disposition: stock_product_mixture_context. Proposals: B-P-JCM1435-TRACE.

Remaining requirement: Obtain a primary JCM1465 clarification of H3BO2 and preserve its separate formulation before proposing that occurrence. No final chemical speciation or unspecified titrant amount is inferred for JCM1435.

## 62: 5% Na2CO3

ATCC1612 uses sterile anaerobic5% sodium-carbonate solution,0.25 ml per10 ml culture medium, to reach pH8.2. Unlike case51, the primary text does not state w/v. It does establish a solution rather than a pure chemical and does not license borrowing the percentage basis from a differently sourced recipe. A bounded ATCC1612 stock proposal retains the literal5% qualification with unspecified basis, rather than treating the missing basis as a blocker to representing the observed preparation.

Only the acetobacterium occurrence CultureMech:009299 and its ATCC1612 preparation instructions support this conclusion.

Disposition: stock_product_mixture_context. Proposals: B-P-ATCC1612-CARBONATE5.

Remaining requirement: Percentage basis, solvent grade, starting carbonate hydrate and stock preparation details remain unspecified. They must be verified before any quantitative conversion or merge with an explicit5%w/v stock; they do not prevent the source-qualified literal5% proposal.

## 63: Trace Metals

ATCC1464 defines Trace Metals as five salts in1 L distilled water: cobalt chloride hexahydrate290 mg, sodium molybdate dihydrate240 mg, sodium selenite17 mg, manganese chloride tetrahydrate200 mg and zinc sulfate heptahydrate280 mg. It is distinct from the adjoining Wolfe vitamin stock and from generic Trace Metals owners. The exact ATCC-qualified mixture can be proposed.

The single Dictyoglomus occurrence doses10 ml of this five-salt stock; the source document defines the stock immediately below the medium.

Disposition: new_distinct_ingredient_proposal. Proposals: B-P-ATCC1464-trace-metals.

## 64: 20% (w/v) Glucose

JCM977 VNG medium supplies100 ml of20% w/v glucose stock to the basal ingredients. The raw term denotes a200 g/L aqueous glucose stock, not a100 g/L pure glucose ingredient. The recipe says Glucose without an anomer or hydrate; the stock proposal preserves that unspecified solute name instead of assigning alpha-D or monohydrate.

Applies to the sole TOGO1030 VNG occurrence and its separately sterilized glucose solution; final-medium glucose concentration is not substituted for stock identity.

Disposition: new_distinct_ingredient_proposal. Proposals: B-P-JCM977-glucose20.

## 65: Trace vitamins solution (see Medium No.284)

JCM1188 explicitly sends this vitamin stock to JCM284. The live284 formulation is a ten-vitamin mixture including DL-calcium pantothenate9.5 mg and vitaminB12 27.1 mg per litre, distinct from the much lowerB12 JCM197 stock. The numbered reference is sufficient to bind the stock formulation.

CultureMech:015391 is the JCM1188 marine Chloroflexi recipe and uses2 ml of the numbered stock. Research-c authors the shared C-P-JCM284 payload.

Disposition: stock_product_mixture_context. Proposals: C-P-JCM284.

Concrete shared payload C-P-JCM284 is authored by the designated parallel author and must be linked by the coordinator when combining fragments; no duplicate after-payload is created.

## 66: Glucose (sterilized separately)

DSMZ357 Flexibacter canadensis medium names Glucose1 g and specifies separate sterilization as a preparation instruction. That parenthetical does not create a different molecule, salt, hydrate or stock strength. The source gives no anomeric orD/L restriction beyond glucose, so the generic glucose identity is the appropriate scope.

The one TOGO2591 source occurrence can resolve its identity-bearing glucose token while retaining sterilization separately in the recipe.

Disposition: existing_identity_or_alias. Proposals: none.

Do not export the complete procedural parenthesis as an exact global synonym; the appropriate change belongs to occurrence parsing/preparation metadata rather than the chemical owner.

Remaining requirement: Retain the primary instruction in CultureMech and resolve only the glucose identity token; independently verify any selected generic-glucose owner ontology boundary before publication.

## 67: Castenholz Salts, 2x

Both source occurrences use ATCC461 CastenholzTYE medium and the explicitly defined2x salts. The stock contains NTA, Nitsch trace elements, dilute ferric chloride solution, calcium sulfate dihydrate, magnesium sulfate heptahydrate, NaCl, KNO3, NaNO3 and Na2HPO4. A500 ml dose is mixed into the parent medium. The2x factor is relative to that recipe, not a universal salt identity.

Both CultureMech:008898 and008899 cite the same ATCC461 formulation. The proposed source-specific stock preserves the nested Nitsch and FeCl3 solution components without replacing them with JCM versions.

Disposition: new_distinct_ingredient_proposal. Proposals: B-P-ATCC461-Castenholz2x.

## 68: MnCl3 . 4H2O

The ATCC2133 OSU967 primary PDF itself prints MnCl3·4H2O in its trace stock, matching the frozen malformed-looking label. MnCl2·4H2O is a familiar nutrient reagent, but familiarity is not evidence that the source intended it. No supplier identifier or correction establishes the oxidation state or stoichiometry.

This is a single explicit ATCC2133 stock constituent, not a generic manganese label. The raw MnCl3 formula must remain visible.

Disposition: malformed_or_nonchemical_token. Proposals: none.

Replacing MnCl3 with MnCl2 would be an unsupported chemical correction.

Remaining requirement: Obtain an ATCC2133 erratum, original preparation record, or reagent supplier/catalogue specification confirming the intended manganese chloride and hydration.

## 69: Growth stimulating factors (see below)

JCM301 defines Growth stimulating factors as six organic acids in100 ml water, adjusted to pH9 with NaOH. It is a preparation with acid/base transformation and unspecified added NaOH amount, not one growth factor. The proposed record retains all six source reagent names, water and the pH-adjusting base, with batch masses and no inferred stereochemistry for2-methylbutyrate.

The single TOGO296 occurrence receives1 ml of this JCM301-defined stock. Component assertion represents preparation inputs rather than claiming the post-neutralization molecular species remain free acids.

Disposition: new_distinct_ingredient_proposal. Proposals: B-P-JCM301-growth-factors.

## 70: dl-Ca-pantothenate

The frozen TOGO3131 label explicitly says dl-Ca-pantothenate, whereas the retrieved DSMZ854 primary PDF (2022 version) names Calcium D-(+)-pantothenate50 mg in Wolin vitamin stock10x. This is a real stereochemical/version discrepancy, not interchangeable spelling. CHEBI:31345 denotes theD salt; a currentD recipe cannot erase the frozenDL observation.

Only the DSMZ854-derived frozen occurrence is at issue; otherDL cases in the campaign may have independent evidence and must be assessed separately.

Disposition: unresolved. Proposals: none.

Neither adding aDL alias to theD owner nor silently rewriting the source toD is defensible across the conflicting versions.

Remaining requirement: Recover the exact historical DSMZ854/TOGO3131 formulation underlying this snapshot or a documented correction establishing whether its rawDL label was a transcription error or a genuine reagent change.

## 71: N--Z amine, type A (Sheffield)

All six primary JCM recipes44,45,47,80,103 and104 specify N-Z amine typeA from Sheffield. This supports the typeA product family, not the broader unqualified N-Z_Amine owner. The existing N-Z-Amine_A placeholder is already explicitly a complex protein hydrolysate and the raw typography is a source label variation. Its chemical composition and ontology promotion remain distinct unresolved product-level questions.

All six occurrences were compared to their respective JCM pages; typeA and manufacturer qualification agree despite different medium names. Root is coordinating this shared owner with the KG case.

Disposition: existing_identity_or_alias. Proposals: none.

A shared-owner alias proposal is delegated to the coordinator to avoid conflicting complete after-payloads; no promotion to a pure-chemical identifier is authorized.

Remaining requirement: The coordinator may add this raw typeA alias to the exact typeA owner, retaining UNDEFINED_MIXTURE and its unresolved supplier/ontology questions.

## 72: Mn(II) x EDTA

JCM1273 and its MediaDive5415 rendition both list Mn(II)·EDTA332 micrograms per litre, not the frozen332 G_PER_L. The manganese oxidation state is explicit, but the formula, charge-balancing counterion and hydration of the supplied chelate are not. A sodium manganeseEDTA salt or bare metal-EDTA anion cannot be chosen solely from this label.

Both occurrences share the same0.01% LB seawater recipe; the two live primary representations agree on microgram units and the unspecified chelate label.

Disposition: unresolved. Proposals: none.

No exact supplied-form owner can be justified while counterion/stoichiometry/hydration remain unspecified.

Remaining requirement: Obtain the JCM1273 reagent catalogue or stock preparation identifying the exactMn(II)-EDTA compound; correct the upstream microgram-to-g/L import error separately.

## 73: Trace Metals A-5 (see below)

ATCC1047 points to ATCC957 MN marine medium and defines Trace MetalsA5 with0.039 g sodium molybdate dihydrate per litre. Its other salts include boric acid, manganese chloride tetrahydrate, zinc sulfate heptahydrate, copper sulfate pentahydrate and cobalt nitrate hexahydrate. The0.039 g value differs tenfold from the explicitly captured TOGO2601 A5+Co stock; the generic A5 owner cannot choose between versions.

The one MN marine occurrence uses the ATCC957 formulation through the1047 source. A separate source-qualified stock is proposed; no generic A5 exact alias is added.

Disposition: new_distinct_ingredient_proposal. Proposals: B-P-ATCC957-A5.

## 74: 2-Mercaptoethanesulfonate (coenzyme M)

DSMZ1280 lists2-mercaptoethanesulfonate (coenzymeM) without a sodium qualifier in SolutionE. CHEBI:17905 supplies the coenzymeM organosulfonic-acid identity and this spelling as a synonym. The existing owner contains an unrelated sodium-salt synonym that remains a separate correction requirement; this source must not be used to validate that sodium synonym.

The single methanoregula peat occurrence is a specified coenzymeM ingredient in a solution, not the solution as a whole.

Disposition: existing_identity_or_alias. Proposals: none.

The existing owner has an unresolved acid/sodium-salt synonym conflict. Root must reconcile it before adding further published aliases or claiming the complete owner reviewed.

Remaining requirement: Remove or reject the sodium-salt alias under independent owner review, verify the sodium sibling separately, then add only the unqualified coenzymeM source spelling if its resolver policy permits acid/anion lexical usage.

## 75: D-pantothenate acid hemicalcium salt (B5)

The source label explicitly names D-pantothenate hemicalcium, which is compatible with theD-calcium pantothenate identityCHEBI:31345 rather thanDL salt or free pantothenic acid. The hemicalcium wording expresses the calcium:pantothenate stoichiometry and does not by itself assert a hydrate. The shared owner has erroneousDL and capsaicin-related aliases that this case cannot validate. A single corrected A-P-CALCIUM-D payload now carries the exact source label; this resolves the local proposal-writing dependency while preserving the P5 primary ingredient-table coverage gap.

Applies to the nutrient-component occurrence of MediaDiveP5 RS medium; it is a vitamin constituent rather than the whole nutrient mixture. Research-a is correcting the sharedD-salt owner.

Disposition: existing_identity_or_alias. Shared proposal: A-P-CALCIUM-D.

Remaining requirement: The isolated A-P-CALCIUM-D payload now corrects the baseline unsafe DL/capsaicin aliases and carries this exact D-hemicalcium raw label. Primary MediaDiveP5 currently returns medium metadata only, so recipe-level confirmation of this ingredient remains missing. Retain the P5 source-release hold and require independent native changed-owner/source review; the concrete alias proposal does not establish unpublished source context.

## 76: Trace vitamins* (see Medium No. 197 )

Each of the twelve primary JCM recipes explicitly names the trace-vitamin stock in Medium197, or inherits the same recipe with only the stated salt change (1463 from1462). The stock identity is therefore shared even though doses differ:1388/1389 use2 ml and1404 uses1 ml while most list10 ml. JCM197 defines ten vitamins, with unspecified calcium-pantothenate stereochemistry retained rather than guessed.

All twelve occurrence IDs remain in this case. Source pages1341,1351,1365,1388,1389,1404,1415,1435,1444,1462,1463 and1475 were reviewed with197. Research-c authors C-P-JCM197.

Disposition: stock_product_mixture_context. Proposals: C-P-JCM197.

Concrete shared payload C-P-JCM197 is authored by the designated parallel author and must be linked by the coordinator when combining fragments; no duplicate after-payload is created.

## 77: Ca pantothenate

ATCC1439 vitamin solution says Ca pantothenate5 mg per litre withoutD/DL. A generic calcium abbreviation does not select theD-only CHEBI:31345 owner, especially while that owner contains known stereochemical alias conflicts. The medium use supports vitamin-mixture context, not a unique stereoisomer or hydrate.

Only CultureMech:009165 Methanogenium medium is covered. The other vitamin ingredients and source concentration do not determine pantothenate stereochemistry.

Disposition: unresolved. Proposals: none.

An exactD-owner alias would introduce specificity absent from the primary source.

Remaining requirement: Obtain the ATCC1439 reagent specification or lot/catalogue identity establishingD versusDL and hydration of calcium pantothenate.

## 78: 3-[N-morpho- lino] propanesulfonic acid (MOPS)

The literal name specifies3-(N-morpholino)propanesulfonic acid; morpho- lino is a broken-line spelling and MOPS is its abbreviation. CHEBI:44115 denotes the acid explicitly and the existing acid owner matches that boundary. CHEBI:39074 is the broaderMOPS entity, so its name similarity does not override the acid-specific wording. No sodium salt is stated.

The single bufferedLB occurrence is50 mM MOPS acid as named by the source; the exact acid owner receives the raw broken-word alias, while broaderMops owner is retained as a competing-owner finding.

Disposition: existing_identity_or_alias. Proposals: B-P-3-_N-morpholinopropanesulfonic_Acid.

## 79: Glucose (α-, D+)

DSMZ403 explicitly specifies Glucose(alpha-,D+)3 g in SolutionA. The stereochemical notation selects alpha-D-glucoseCHEBI:17925, not unspecified glucose, beta-D-glucose or alpha-D-glucose monohydrate. Neither the source term nor its primary recipe names water of crystallization.

This alias applies only to the BSK glucose occurrence; the other BSK ingredients, including theDIFCO yeastolate product, were not used as evidence for glucose hydration.

Disposition: existing_identity_or_alias. Proposals: B-P-Alpha-d-glucose.

## 80: DI WATER

ATCC2686 gives DI WATER1 L. DI indicates deionized water, while the current Distilled_Water owner specifically represents distillation and already rejects several other preparation labels. The common H2O molecular identityCHEBI:15377 does not prove preparation equivalence, and the frozen1 G_PER_L is an import unit error.

The sole Nautilia profundicola medium occurrence is solvent water prepared by deionization; its1 L quantity is not1 g/L solute.

Disposition: supplied_form_correction. Proposals: none.

Do not addDI WATER as an exact synonym of the distilled-water preparation.

Remaining requirement: Represent deionized-water preparation separately or use a verified preparation-neutral water owner with deionization retained at the occurrence; do not collapse the distinct water-preparation records.

## 81: Trace Mineral Supplement, Catalog No. MD-TMS

ATCC2485 explicitly requests Trace Mineral Supplement catalogMD-TMS,10 ml. The current ATCC product is a sterile multi-salt stock, withEDTA and cobalt nitrate; older Wolfe recipes may instead useNTA and cobalt chloride. Therefore the catalog identifier is the identity anchor and every generic Wolfe-stock name must not be treated as equivalent without version comparison.

Applies to the MD-TMS commercial-product occurrence inMH-OCM medium. Root/research-a coordinates a shared catalogue-product owner across campaign occurrences.

Disposition: stock_product_mixture_context. Proposals: A-P-ATCC-MDTMS.

Concrete shared payload A-P-ATCC-MDTMS is authored by the designated parallel author and must be linked by the coordinator when combining fragments; no duplicate after-payload is created.

Remaining requirement: Keep the explicit catalogue identity and do not transfer currentMD-TMS formulation to historic homemade Wolfe stock occurrences without evidence.

## 82: pectin (apple)

The source specifies apple-derived pectin as an alternate carbon material. CHEBI:17309 is a pectin class, not a guarantee of identical esterification, molecular-weight distribution or botanical preparation. An apple-source restriction is meaningful for a heterogeneous polysaccharide material; a broad parent relation can support it, but generic pectin exact identity would erase that restriction.

Applies to the sole minimal-media occurrence and its explicit apple qualifier; no supplier or grade is specified in the frozen recipe.

Disposition: broad_parent_relation_only. Proposals: none.

A separate source-qualified apple-pectin identity needs a primary procurement/material specification; genericPectin is only a parent candidate.

Remaining requirement: Identify the recipe's actual apple-pectin supplier/grade and whether source-specific material identity can be represented with a stable registry identifier and broad pectin mapping.

## 83: Bacto-Yeast Nitrogen Base w/o Amino Acids and Ammonium Sulfate (Difco)

NBRC113 explicitly specifies Bacto/Difco yeast nitrogen base without both amino acids and ammonium sulfate,1.7 g. The surrounding recipe separately supplies nitrogen and amino-acid additions. This is a formulated commercial basal mixture, distinct from completeYNB and from products omitting only amino acids. The double exclusion must survive normalization. A bounded manufacturer-qualified family proposal preserves both exclusions without assigning the current233520SKU to the historical recipe or inventing a complete formulation.

The sole TOGO1435 occurrence is sourced toNBRC113; its exact two exclusions are the crucial product boundary. OfficialBD product evidence identifies233520 as the matching double-exclusion product family.

Disposition: stock_product_mixture_context. Proposals: B-P-BD-DIFCO-YNB-DOUBLE-EXCLUSION.

Remaining requirement: The historical NBRC113 catalogue/lot and full quantitative formulation remain unverified. CurrentBD233520 corroborates family wording only; no completecomposition or historicalSKU identity is asserted, and native source/owner/export release remains separate.

## 84: FeSO2·7H2O

Both NBRC406 and808 primary pages repeatFeSO2·7H2O as printed, matching the frozen source labels. AlthoughFeSO4·7H2O appears elsewhere in medium stocks and is chemically familiar, that is not a correction notice. Changing oxygen stoichiometry would change the substance identity and cannot be presented as harmless normalization.

Both methanogen-medium occurrences are included; the source typo candidate is retained verbatim rather than folded onto ferrous sulfate heptahydrate.

Disposition: malformed_or_nonchemical_token. Proposals: none.

No exact source correction establishes the intended formula.

Remaining requirement: ObtainNBRC406/808 provider errata, historical originals or reagent specifications confirming the iron compound; separately repair the frozenmg-to-G_PER_L flattening where source amounts are2 mg.

## 85: Trace vitamins solution (see Medium No. 284)

MediaDive5112 (JCM1051) lists the numberedJCM284 vitamin solution as1 ml in a declared1004 ml batch. This is0.0996016% v/v; the frozen0.9960159% value is tenfold higher and must be corrected upstream. Although the API models it as a compound identifier, the primary284 definition is a ten-component stock; the API field type does not convert it to one chemical. ItsDL pantothenate and highB12 distinguish it from197.

OnlyCultureMech:014025 is covered; the exact numbered284 reference links it to the sharedresearch-c payloadC-P-JCM284, preserving1 ml as the primary parent recipe dose and flagging the frozen percentage discrepancy.

Disposition: stock_product_mixture_context. Proposals: C-P-JCM284.

Concrete shared payload C-P-JCM284 is authored by the designated parallel author and must be linked by the coordinator when combining fragments; no duplicate after-payload is created.

## 86: Nitsch's trace elements

The primary chainJCM625 to624 to273 defines Nitsch trace elements usingMnSO4·xH2O, ZnSO4·7H2O, boric acid, copper sulfate pentahydrate, molybdate dihydrate, cobalt chloride hexahydrate and sulfuric acid. The unspecifiedx hydrate is genuine source uncertainty. ATCC461 Nitsch formulation nested under case67 is a separate source version and must not supply missing details.

The soleTOGO637 occurrence follows the actualJCM reference chain, all of whose full source pages were inspected.

Disposition: new_distinct_ingredient_proposal. Proposals: B-P-JCM273-Nitsch.

Remaining requirement: Retain unknown manganese hydration and sulfuric acid strength; do not map component forms until a reagent specification resolves them.

## 87: Fe-EDTA(III)

NBRC1201 MMA medium specifiesFe-EDTA(III)5 mg per litre, not the frozen5 G_PER_L. Iron oxidation state is constrained toIII, but counterion, ligand protonation, hydration and supplier preparation are unspecified. Neither bareFeEDTA anion nor a particular sodiumferricEDTA salt is uniquely identified.

The singleTOGO1934 occurrence is a chelate reagent in theNBRC1201 recipe; its lowmg amount confirms a trace supplement without resolving supplied form.

Disposition: unresolved. Proposals: none.

An exact chemical identifier would assert counterion/hydration absent from the source.

Remaining requirement: ObtainNBRC1201 Fe(III)-EDTA supplier/catalogue or preparation formula; repair the independentmg/G_PER_L import error.

## 88: 50x Vogel-Bonner salts

The live TOGO2788 EMA source defines50x Vogel-Bonner salts as10 g magnesium sulfate heptahydrate,500 g anhydrous dipotassium hydrogenphosphate,175 g sodium ammonium hydrogenphosphate tetrahydrate and100 g citric acid monohydrate with1 L water. The parent-medium dose is20 ml, contradicting the frozen20 G_PER_L. Its comment explicitly specifies50-fold dilution to single-strength mediumE. This is a source-defined mineral stock, not whole EMA medium.

The singleEMA occurrence is directly linked to the completeTOGO2788 stock subsection and dilution instruction. The proposed batch amounts retain the source formulation and exact hydrate distinctions.

Disposition: new_distinct_ingredient_proposal. Proposals: B-P-TOGO2788-VogelBonner50x.

## 89: NaHSeO3

NaHSeO3 occurs in fourteen frozen contexts. CurrentDSMZ1344/1147/1381/1469 andMediaDive2304/2700 explicitly retain this one-sodium hydrogen-selenite formula; archivedDSMZ311 uses10^-7M. CHEBI:29924 is hydrogenselenite anion without sodium, whileCHEBI:48843 is disodium selenite, so neither is an exact identity. The source trail also contains inherited311/777 variants and imported stock contexts; these do not independently establish a purchased solid or hydrate.

All fourteen occurrence IDs and full recipes are retained. Where source documents refer to other media, the inherited component is distinguished from a newly specified reagent. Existing frozenCHEBI:29924 grounding is treated as an anion-level claim, not proof ofNaHSeO3 identity.

Disposition: unresolved. Proposals: none.

A common exact sodiumhydrogenselenite owner is not justified by anion/disodium alternatives or ambiguous supplied preparation.

Remaining requirement: Obtain a primary supplier/registry identity or original preparation protocol for the actualNaHSeO3 reagent (including whether made by acidifyingNa2SeO3, and any hydration), then use its distinct identity with only justified parent/anion relations.

## 90: Yeast extrakt

DSMZ29 prints Yeast extrakt; DSMZ40 explicitly follows29 with addedNaCl. This is a direct orthographic source spelling of yeast extract, with no fresh-cell, stock-strength or specialproduct qualifier. FOODON:03315426 and the existingYeast_Extract owner match the ingredient class.

BothTOGO2258 and2595 occurrences share the source spelling through the29/40 recipe relationship. The proposal adds that raw spelling without changing product composition or occurrence statistics.

Disposition: existing_identity_or_alias. Proposals: B-P-Yeast_Extract.

## 91: Trypticase soy yeast broth

The frozenTOGO2414 recipe names Trypticase soy yeast broth as an entire broth preparation, with its1 L amount flattened to1 G_PER_L. Trypticase, soy digest and yeast material are not established as independent components merely by splitting the name. A whole medium/formulated mixture identity is required.

Applies only to the singleTSY broth occurrence and its complete frozen source context; the successful liveTOGO2414 response confirms the wholeTSY broth at1 L and supplies culture conditions but no constituent formulation.

Disposition: stock_product_mixture_context. Proposals: none.

The exactTSY formulation, supplier and version are not yet bound to a verifiedowner.

Remaining requirement: Recover the originalTOGO2414 formulation or commercialcatalogue recipe defining theTSY broth; then create or match a whole-medium owner without inventing constituents from the label.

## 92: EBIOS* (dried yeast tablets)

JCM969 EBIOS-glucose agar explicitly uses10 g EBIOS dried yeast tablets and identifiesAsahiFood&Healthcare. A branded tablet preparation can contain excipients and is not synonymous with generic yeast extract or fresh baker's yeast. The source supports the historical product family but not a complete tablet composition.

The soleTOGO1019 occurrence is tied toJCM969 and itsasterisk manufacturer note; the tablet state remainspart of identity.

Disposition: stock_product_mixture_context. Proposals: none.

No supplier formulation for the source-eraEBIOS tablets has been bound to the recipe.

Remaining requirement: CaptureAsahi historicalEBIOS tablet composition/version (driedyeast plus excipients) and its product identifier before proposing a complete product owner.

## 93: CrCl3.6H2O

CrCl3·6H2O unambiguously specifies chromium(III) chloride hexahydrate. CHEBI:53442 is the exact hexahydrate and provides hydratedSMILES/InChI. The existingowner already has the correctidentifier and empiricalformula but retains anhydrous structure strings from an earlierstate. The proposal adds the sourcealias and corrects those structures against theexact ontology term.

The sole nitrogen-limited mineral-salts occurrence is the hydrate, not parentchromiumchlorideCHEBI:53351. The sourcealias does not imply a particularcoordination isomer beyond theChEBI hexahydrateclass.

Disposition: existing_identity_or_alias. Proposals: B-P-Chromium_Iii_Chloride_Hexahydrate.

