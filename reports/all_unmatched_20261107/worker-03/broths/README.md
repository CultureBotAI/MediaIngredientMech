# Worker03 broth source review

The authored batch accounts for all 86 assigned cases and 82 full frozen recipe occurrences. It contains 20 isolated YAML proposals. Primary evidence, raw source labels, source identifiers, all occurrence IDs, candidate-owner bytes and inherited hold context are retained. No maintained YAML, aggregate, SSSOM or generated output was changed.

The author-local integrity checks and strict LinkML validation pass. Independent skeptical review is performed separately by the materials reviewer; this document does not grant native full-record or downstream publication approval. The coordinator must combine this subbatch with the other102cases before running the complete-shard outcome auditor.

The final proposal and evidence bytes are bound in `local-integrity-check.json`. Evidence dates are actual acquisition times (UTC2026-11-08); the campaign label remains20261107. URL-bearing evidence retains raw primary captures or exact web-tool source extracts, hashes and locators. Failed attempts remain explicitly unsuccessful.

## Concrete proposals

| Proposal | Cases (frozen indices) | Application condition |
|---|---|---|
| b-proposal-chopped-filtrate | 1 | Create a source-defined filtered broth identity and retain the frozen850g/L versus primary850mL discrepancy. |
| b-proposal-gam_broth_mod_powder | 10, 147 | DSMZ1715 and MediaDive1564 identify modified HyServe GAM at41.7g/L. Standard59g/L GAM is a different product. Product composition is not inferred from whole recipient medium. |
| b-proposal-veal_infusion_broth | 12, 137 | DSMZ577 and MediaDive579 identify Difco0344 veal infusion broth25g/L; separate yeast extract5g/L belongs to VY medium, not this product. |
| b-proposal-gam_broth_powder | 105, 178 | DSMZ1713 and MediaDive1563 identify standard HyServe GAM59g/L. Modified41.7g/L GAM remains a distinct owner. |
| b-proposal-marine-aliases | 62, 108, 124 | Add two source-qualified Difco Marine2216 aliases; keep existing native hold and component-review obligations. |
| b-proposal-bd211065 | 76 | Concrete BD211065 BBL BHI agar candidate; incompatible current heart-only owner must be reconciled before application. |
| b-proposal-daigo-r2a | 86, 87 | Create DAIGO R2A broth candidate with full JCM839 formula, separately from R2Aagar. |
| b-proposal-mem-p0440 | 128 | Annotate the exact P0440 powder/exclusion scope while retaining the generic owner UNMAPPED. |
| b-proposal-pplo-255420 | 34, 38, 99 | Separate catalog-specific255420 basal broth identity; no generic PPLO alias merge. |
| b-proposal-pplo-211458 | 11 | Separate catalog-specific211458 basal broth identity; no generic PPLO alias merge. |
| b-proposal-kyokuto-551024807 | 3 | NBRC1296 explicitly identifies Kyokuto551-02480-7 nutrient broth powder at6g, with pyruvate and optional agar separate. This catalog-bound preparation does not inherit Difco or Oxoid nutrient-broth equivalence. The vendor formulation is not disclosed; no components are invented. |
| b-proposal-bd211443 | 60 | TOGO M2583 names BD211443 MuellerHintonBroth and adds100mL rabbitserum separately. Manufacturer-submitted GUDID identifies211443 as BBL MuellerHintonBroth500g, commercially discontinued in the UnitedStates in2022. This historical catalog remains a stable source identity; it is not cation-adjusted MuellerHintonII nor the serum-supplemented final medium. |
| b-proposal-liver-filtrate | 74 | Preparation-defined liquid liver filtrate in NBRC201/202:25g sliced liver,150mLwater, gentle boiling30minutes, cloth filtration to remove solids. The species and recovered volume are not specified. Starting liver mass is not final extract concentration, and no dried-extract equivalence is claimed. |
| b-proposal-oxoid-cm0077 | 114 | DSMZ77 names OxoidCM77 LiverBroth. Official CM0077 specification identifies the product and four-part typical formula, including30g/L extracted liver tissue in addition to23g/L infusion. This particulate broth is not the filtered NBRC liver infusion. |
| b-proposal-columbia-m2256 | 115 | TOGO M2256 explicitly names BBL Columbia broth and provides its12-component basal subformula. NAD0.01% andCaCl225mM are parent supplements and excluded here. This record denotes the source-defined basal formulation, not every product named Columbia broth. |
| b-proposal-standard-i | 134 | Original source630 is Merck StandardI broth in DSMZ637. Official Merck12thEdition manual identifies1.07882 StandardI nutrientbroth and its15/3/6/1g/L formula,25g/L preparation. Malt extract,CaCO3 andagar inDSMZ637 are separate supplements. |
| b-proposal-bd238400 | 146 | Original MediaDive1460 explicitly identifiesBD238400; BD catalog confirmsDifco HeartInfusionBroth. ATCC254 gives25g/L and10g beef-heart infusion solids from500g tissue,10g tryptose,5gNaCl, with agar omitted for broth. This is distinct from BHI and heartinfusionagar. |
| b-proposal-difco-nutrient | 31 | NBRC885 names Difco BactoNutrientBroth8g/L; ATCC3 identifies correspondingDifcoBD2340008g/L and3g beefextract+5gpeptone. Sodiumcarbonate inNBRC885 andagar inATCC3 are excluded. Current Nutrient_Broth_No_2 incorrectly combines the distinctOxoidCM0067 product withDifco aliases and must be reconciled before applying this powder-product proposal. |
| b-proposal-cm0149-form | 29 | NBRC902 identifiesOxoidCM0149. Current supplierIFU0539 explicitly callsCM0149 semi-solid, with0.5g/Lagar and13g/Lyeast extract; it distinguishesCM0151agar. Historical supplier specification search describes3gyeast+10gLabLemco instead, so formulation revision cannot be silently erased. |
| b-proposal-cm0643 | 161, 179 | Original source2093 isOxoid WilkinsChalgrenbroth; its existingCM0643alias and source2140 explicitCM643 identify the same catalog family. OfficialCM0643 specification supplies nine constituents. Themisspelled separateownerWilkins_Chalgrene_Anaerobe_Broth retains independent source2140provenance and must be reconciled before integration. |

## Findings and unresolved source boundaries

The detailed findings ledger is `findings.json`. The most consequential boundaries are BD211065 BBLbrain-heartagar versus the currentheart-onlyowner; OxoidNo2 versus Difconutrientbroth; Difco255420 versusBBL211458 PPLO; sourcefrozen/unitconflicts; and the dextrose-freeTSB exclusion. These are evidence-backed distinctions, not lexical-normalization decisions.

No broth was mapped to a single nutrient, raw animal tissue, or an organism. Parent recipes and supplements remain separate from basal products. Preparation inputs that are removed by extraction are not asserted as final retained components. Literal component transcriptions deliberately use `UNMAPPED` component references instead of inventing chemical forms.

The20proposals include source-defined liver and chopped-meat filtrates, a12-componentColumbia basal formulation, specific supplier products, three new primary-supported existing-owner promotions, and narrow supplied-form annotations. Existing mixed-owner and native hold conflicts are integration dependencies, not silently cleared by the proposal.

## Individual case assessments

### 0: Difco PPLO Broth

TOGO M2785 calls the input PPLO and annotates it Difco PPLO Broth; it is 17.7 g of basal product supplemented separately with yeast extract, DNA and horse serum. This is neither the entire Hayflick medium nor a single molecule. No catalog is supplied, so BD BBL 211458 must not be inferred from the PPLO stem.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Locate the catalog or supplier formulation used by TOGO M2785 before attaching its unqualified DifcoPPLO wording to either255420 or a generic owner.

### 1: Chopped Meat Broth

ATCC 1016 explicitly defines Chopped Meat Broth as the filtrate obtained after heating fat-free ground beef with water and NaOH, removing fat and filtering, then restoring 1 L. The complete medium adds 850 mL of this stock. The frozen 850 G_PER_L value is a unit-flattening error; raw ground beef and optional meat particles are not equivalent to the filtered broth.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-chopped-filtrate.

Remaining scope condition: No final chemical composition is asserted: beef andNaOH are extraction inputs. Broad source wording retained as REJECTED_LABEL must remain nonresolving; no whole cooked-meat owner merge.

### 3: Nutrient Broth Powder (Kyokuto*)

NBRC1296 identifies Kyokuto Nutrient Broth Powder code 551-02480-7 at 6 g with separately added sodium pyruvate and optional agar. This named commercial preparation is not evidence for the Difco 8 g/L formulation or Oxoid No.2 25 g/L formulation. Supplier code must remain attached before any product identity is introduced. NBRC1296 supplies sufficient stable catalog scope for a concrete new registry proposal; absent manufacturer composition limits partonomy, not the product identity proposal.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-kyokuto-551024807.

Remaining scope condition: Catalog source identity supported by NBRC1296. Historical product formulation is undisclosed; no formula or equivalence to another vendor is approved.

### 4: PPLO broth base without crystal violet (Difco)

Both M2888 and M2223 explicitly use Difco PPLO broth base without crystal violet, 21 g, followed by different serum supplements. The basal product may be shared, but the finished serum-containing media are different. The word base does not establish the separate BBL211458 catalog identity.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Obtain Difco catalog/version for M2888 and M2223 or an explicit supplier no-CV product bridge; retain separately supplemented serum recipes.

### 10: GAM Broth mod. powder (HyServe)

DSMZ1715 names HyServe modified GAM powder at 41.7 g/L. HyServe identifies its modified product separately from standard GAM and excludes agar. Frozen MediaDive1564 is the same DSMZ1715 product context, supporting an isolated identity/alias proposal with no generic GAM merge.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-gam_broth_mod_powder.

Remaining scope condition: Promotion preserves the existing stem and complete historical payload. Before integration verify the entire owner against native rules; no standard/modified or cross-supplier GAM merger, generic extract equality, new components, or roles are asserted.

### 11: PPLO Broth Base w/o CV (Mycoplasma Broth Base) (BD 211458)

ATCC1106 explicitly specifies BD211458 Mycoplasma Broth Base without crystal violet and adds glucose, bovine serum and yeast extract separately. The current BD catalog identifies 211458 as Mycoplasma Broth Base, distinct from Difco255420 PPLO broth. Retain the ATCC21g recipe input without using that number to assert the two product formulations equal.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-pplo-211458.

Remaining scope condition: Competing generic PPLO_Broth/PPLO_medium ownership requires reconciliation; no maintained aliases are removed here. Formula revision/lot is not documented; only source/catalog product identity is proposed. Native new-owner admission remains blocked by1165 until coordinator integration prerequisites land.

### 12: Veal infusion broth (Difco 0344)

DSMZ577 names Difco0344 Veal infusion broth at 25 g and adds 5 g yeast extract separately. MediaDive579 references medium577 and the frozen attribute is Difco0344. The source-specific product identity is supported; it is not purified veal tissue, a single extract chemical, or the complete supplemented VY medium.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-veal_infusion_broth.

Remaining scope condition: Promotion preserves the existing stem and complete historical payload. Before integration verify the entire owner against native rules; no standard/modified or cross-supplier GAM merger, generic extract equality, new components, or roles are asserted.

### 14: de Man-Rogosa-Sharpe (MRS) broth (LabM)

TOGO M2944 records one litre of LabM MRS broth and cultivation at37C but supplies no catalog or ingredient amounts. Its product annotation points to Neogen Lactobacilli MRS. This supports the named preparation context only; Biokar and Difco MRS formulation equality is not established.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Identify the LabM/Neogen catalog/version and full basal MRS formula used in M2944 before any cross-vendor or generic-owner alias transfer.

### 15: Bacto Tryptic Soy Broth w/o Dextrose (Difco)

NBRC1035 deliberately specifies Bacto Tryptic Soy Broth WITHOUT DEXTROSE and uses it at one-tenth strength. It adds NaCl and phosphate separately. A standard dextrose-containing TSB owner would erase an explicit exclusion; the MediaDive99 synonym list itself mixes these variants and is not equivalence evidence.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Verify the Difco dextrose-free TSB catalog and its sugar exclusion against the mixed Trypticase_Soy_Broth owner; a dextrose-containing owner is unsafe.

### 24: PPLO broth powder (Difco)

M2215 specifies Difco PPLO powder at22.5g plus serum, DNA, glucose, IsoVitaleX and phenol red. The powder input remains distinct from that finished supplemented broth; no catalog or no-crystal-violet declaration is given in this exact raw name, so nearby PPLO products are candidate links only.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Obtain the M2215 Difco powder catalog and crystal-violet status; the22.5g dose cannot select255420 or211458.

### 29: CM0149 Broth (OXOID)

NBRC902 explicitly names Oxoid CM0149, and the manufacturer identifies CM0149 as Reinforced Clostridial Medium, a semisolid dehydrated preparation. The source also permits additional agar. Treating CM0149 as a chemical or inferring brain-heart broth from a generic broth label would be wrong. The officialCM0149 IFU was retrieved, confirming semi-solid state and current13gyeast formulation. Historical manufacturer search shows a different3gyeast/10gLabLemco formulation; a supplied-form annotation is proposed while revision and mixed-owner partition remain unresolved.

Disposition: `supplied_form_correction`. Proposals: b-proposal-cm0149-form.

Remaining scope condition: The existing owner also carriesBD-Difco and historicalOxoid aliases. The captured currentIFU formula must not be retroactively applied to unknown recipe revisions. Registry promotion requires an explicit scope partition; this form annotation is safe and concrete without it.

### 31: Bacto Nutrient Broth (Difco)

NBRC885 identifies Difco Bacto Nutrient Broth at8g/L, with sodium carbonate separately added. OLS MICRO0000082 describes the Difco 3g beef-extract/5g peptone formula. This contradicts equating the input with Oxoid Nutrient Broth No.2; the existing No.2 owner's mixed supplier aliases require separation before reuse. ATCC3 primary formula now corroborates the Difco8g/L preparation and supports a concrete supplier/source-specific powder candidate, while the competingOxoidNo2 owner and liquid-ontology relation remain explicit integration conditions.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-difco-nutrient.

Remaining scope condition: Catalog234000 is primary comparator, not silently added toNBRC885. Integration must resolve competing Nutrient_Broth_No_2 aliases and decide exact/broad ontology relation for the supplier powder before release; registry candidate is source-specific, not a new generic nutrientbroth concept.

### 34: PPLO Broth w/o Crystal Violet (BD 255420)

ATCC2616 explicitly names Difco255420 PPLO broth without crystal violet,3.5g in basal medium, followed by a large additive solution. Its concentration is a recipe dose and does not identify the full broth product or justify replacement by casein/gelatin digests added separately.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-pplo-255420.

Remaining scope condition: Competing generic PPLO_Broth/PPLO_medium ownership requires reconciliation; no maintained aliases are removed here. Formula revision/lot is not documented; only source/catalog product identity is proposed. Native new-owner admission remains blocked by1165 until coordinator integration prerequisites land.

### 35: M17 broth (Oxoid)

M2883 and M2892 name Oxoid M17 basal product at37.25g, with carbohydrate supplementation in separate tables. Their comments specify glucose while recipe tables also carry lactose preparation text, a source conflict. Preserve the M17 base and the conflicting carbohydrate context instead of merging a completed GM17 recipe with an unmodified M17 product.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Reconcile glucose-versus-lactose source text in M2883/M2892 and identify OxoidM17 catalog to distinguish unsupplemented base from final GM17.

### 37: Nissui GAM Broth*

NBRC312 names Nissui GAM Broth at59g/L and identifies the supplier in its footnote. This is the standard GAM product; the modified Nissui product in NBRC1509 is41.7g/L. Do not normalize away modified or assume HyServe distributor/formulation equivalence solely from matching dose.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Verify an explicit Nissui-to-HyServe product/manufacturer bridge and corresponding formula revision before sharing a GAM owner; matching59g/L alone is insufficient.

### 38: PPLO broth w/o Crystal Violet (BD-Difco 255420)

JCM1303 explicitly names BD-Difco255420 at2.1g in its100mL preparation. The frozen21g/L normalization preserves this product identity, with hipolypepton, bovine calf serum and urea/yeast stock added separately. It remains the basal PPLO product, not the completed Ureaplasma medium.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-pplo-255420.

Remaining scope condition: Competing generic PPLO_Broth/PPLO_medium ownership requires reconciliation; no maintained aliases are removed here. Formula revision/lot is not documented; only source/catalog product identity is proposed. Native new-owner admission remains blocked by1165 until coordinator integration prerequisites land.

### 39: Bacto Todd Hewitt Broth (Difco)

NBRC311 and315 both name Difco Bacto Todd Hewitt Broth at30g/L;315 separately adds horse serum. Existing Todd_Hewitt_Broth carries both Difco and Oxoid aliases without a verified cross-vendor composition comparison, so additional global aliases would extend an unreviewed merged scope.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Compare Difco ToddHewitt with the Oxoid variant already in Todd_Hewitt_Broth before broadening resolving aliases; serum supplementation belongs to NBRC315.

### 40: Heart muscle infusion solids

The frozen record calls this heart muscle infusion solids from BD BBL211037 blood-agar base, whereas JCM70 itself only instructs use of BD-Difco blood agar base. It is an animal-tissue extract component rather than whole heart, BHI or the complete blood agar. The2g assertion needs the exact211037 specification, not JCM70's generic product direction.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Retrieve BD BBL211037 component specification establishing heart-muscle solids and2g amount; JCM70 alone names generic blood-agar base.

### 45: Brain heart infusion (BD Difico)

JCM1427 directly names Brain heart infusion (BD Difico) at6g alongside proteose peptone and other ingredients. The supplier spelling is raw provenance, not a new material. The source does not identify a catalog or dextrose variant; existing generic BHI holds therefore remain unresolved for product equivalence.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Identify the JCM1427 BHI catalog and dextrose status; then reassess held Bacto/BrainHeartInfusion owner payloads before any exact alias release.

### 46: PPLO broth without crystal violet (BD-Difco)

The frozen JCM1476 recipe and current primary JCM1476 differ in serum type, stock preparation and batch scale. Current JCM names BD-Difco255420 explicitly, supporting the basal product family, but it cannot silently replace the frozen source context. Reconcile source-version drift before a context-wide alias or quantitative recipe repair.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Reconcile frozen versus current JCM1476 revision, serum choice and stock volumes before assigning source-specific catalog or quantitative repairs.

### 48: PPLO Broth w/o  Crystal Violet (Difco)

M2578 specifies Difco PPLO without crystal violet at11g in a basal medium, then adds a separately sterilized serum/yeastolate/CMRL supplement. The duplicated space in the raw label is lexical; product identity still requires preservation of the no-crystal-violet qualifier and must not absorb the complete Spiroplasma formulation.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Find the exact Difco no-CV catalog in the source study underlying M2578; keep the11g basal input distinct from added serum/CMRL.

### 49: Difco brain-heart infusion broth (BD Biosciences)

M2976 raw text says Difco brain-heart infusion broth, but its GMO annotation says without dextrose; the frozen concentration1g/L is also inconsistent with the source1L. These contradicting fields prevent silently selecting a generic BHI product. Preserve source label and seek the original publication/catalog for the dextrose variant.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Resolve raw BHI versus without-dextrose annotation and1g/L versus1L inconsistency in M2976 using original study/catalog.

### 55: Bacto PPLO Broth (Difco)

NBRC246 and823 both use21g Difco Bacto PPLO, but their serum, yeast and arginine supplements differ. Neither exact raw label supplies a catalog. This supports a common Difco basal-broth family, not identity of the full media nor substitution with BBL Mycoplasma Broth Base.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Establish exact Difco catalog/version for NBRC246 and823; preserve their different supplements and do not substitute BBL211458.

### 60: Mueller Hinton Broth (BD 211443)

M2583 names BD211443 Mueller Hinton Broth at22g in900mL water, with100mL rabbit serum added later. The catalog-qualified basal medium must remain distinct from cation-adjusted variants and the final serum-supplemented recipe; no single-chemical identifier represents it. The captured manufacturer-submitted GUDID record establishes the historical BBL211443 product, so a specific registry payload is now concrete; absence of a molecular identifier is not a blocker.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-bd211443.

Remaining scope condition: No full composition transcribed because retrieved product record is identity/label evidence. Historical distribution status does not invalidate recipe identity. No new organism or susceptibility claims.

### 61: De Man-Rogosa-Sharpe (MRS) broth (Biokar Diagnostic)

M2225 explicitly names Biokar Diagnostic MRS at55.3g/L and pH6.4+/-0.2. This is product-specific evidence and does not prove equality with55g/L Difco MRS or LabM products. Preserve the Biokar supplier qualifier even though the expansion of MRS is unambiguous.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Obtain Biokar catalog/revision for M2225 and compare55.3g/L formulation to the existing multiple MRS owners before merging aliases.

### 62: Difco Bacto Marine Broth (DIFCO 2216)

DSMZ514a defines half-strength Difco Bacto Marine Broth as18.7g/L. The ingredient is the2216 basal product dosed at half strength, not a new chemical. The frozen recipe also contains flattened full-strength constituent rows and milligram-to-gram artifacts; those rows must not be treated as corroborating product composition.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-marine-aliases.

Remaining scope condition: Separate Difco_Marine_Broth and Marine_Broth owners are not merged. Inherited component IDs and complete assertion are preserved without scientific approval; the duplicated frozen514a decomposition must not justify them.

### 64: Middlebrook 7H9 broth (Difco)

M2406 uses prepared Difco7H9 broth by volume, whereas M2880 records2.35g powder plus separate ADC/Tween supplementation and does not assert a final-volume denominator. Preserve both supplied states and their source amounts; do not collapse7H9 with7H10/7H11 agar or absorb the enrichment.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Resolve supplied state and stock strength separately for M2406 and M2880; retain ADC/Tween supplements and avoid assumed final-volume normalization.

### 67: Bacto PPLO Broth w/o CV (Difco)

NBRC400 uses2g Difco PPLO without CV in a multistage M1D preparation;NBRC1407 uses14.7g with serum, yeast and MEM vitamins. The differing doses are contextual rather than distinct solute identities. The frozen2g/L in NBRC400 should not be used as a product concentration specification.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Verify catalog for both NBRC400 and1407 Difco no-CV inputs; keep2g multistage recipe amount distinct from finished-product concentration.

### 68: Lab-Lemco Broth (Oxoid)

NBRC19 calls for Lab-Lemco BROTH from Oxoid at2g, alongside peptic pepton, plant salts and sucrose. Lab-Lemco powder/meat extract and complete Lab-Lemco broth need separate catalog/formula evidence; the common brand stem does not establish that the listed ingredient is pure meat extract.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Determine whether NBRC19 means LabLemco prepared broth or meat-extract powder by supplier catalog/formula; the brand stem alone is insufficient.

### 74: Liver infusion

NBRC201 and202 explicitly prepare liver infusion by boiling sliced liver in150mL water for30minutes and cloth-filtering. The25g quantity refers to liver starting material, not25g of dried extract or a finished broth solute. The preparation-defined filtrate is not interchangeable with dehydrated liver extract or Oxoid liver broth. The common explicit extraction procedure supports a bounded NBRC201/202 filtrate registry proposal despite the unspecified animal species; global liver-extract equivalence remains unasserted.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-liver-filtrate.

Remaining scope condition: Specific preparation scope only. Tissue species and final filtrate yield remain unspecified; no formula, dry weight or global LiverInfusion resolving alias is asserted.

### 75: brain-heart infusion broth (Difco Laboratories)

M2974 uses one litre Difco BHI with added Tris and thiamine monophosphate. Its raw prose says BHI while its annotation specifies without dextrose. Preserve that unresolved qualifier conflict; a supplier-wide alias to generic BHI would hide which basal formulation was used.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Resolve M2974 raw BHI versus without-dextrose annotation using the primary cited study/catalog; do not hide the qualifier conflict in a generic alias.

### 76: Brain Heart Infusion Agar (BD 211065)

ATCC44 and official BD catalog identify211065 as BBL Brain Heart Infusion Agar. Current MIM Heart_Infusion_Agar_BD_211065 instead targets MICRO0000567 heart infusion agar and carries heart-only Difco/Eiken aliases. OLS defines that target as heart infusion plus tryptose, a different formulation. Propose a catalog-specific BBL identity with an explicit competing-owner reconciliation blocker.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-bd211065.

Remaining scope condition: Blocking competing-owner reconciliation: Heart_Infusion_Agar_BD_211065.yaml falsely carries211065 but real heart-only Difco/Eiken aliases. Catalog identity is established; no full component formula or generic BHI/heart-agar alias scope is approved.

### 80: brain-heart infusion broth (Difco)

M2830 says Difco brain-heart infusion broth, one litre, with glucose additionally brought to0.1%. That added glucose does not establish whether the basal product initially contained dextrose. The source supports a BHI medium context while catalog/variant equivalence with held MIM owners remains unproven.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Identify Difco BHI catalog/initial glucose status in M2830 before linking the held BHI owners;0.1% added glucose does not establish basal formulation.

### 81: Brain infusion solids

M2211's Oxoid BHI subformula lists12.5g brain infusion solids and5g beef-heart infusion solids. Brain solids are an extracted animal-tissue mixture, not whole calf brain and not the combined BHI medium. The frozen recipe incorrectly mixes a separate Difco decomposition with the Oxoid source, so do not adopt its duplicate component rows as identity evidence.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Remove/reconcile the frozen Difco component expansion against M2211 Oxoid source and identify the supplied brain-infusion-solids preparation rather than whole brain.

### 83: Man-Rogosa-Sharpe (MRS) broth (Biokar Diagnostic, Beauvais, France)

M2495 names Biokar Diagnostic MRS by one-litre prepared-medium volume and records cultivation conditions. This is the same supplier family as M2225, but no exact formulation/catalog is given in this occurrence. Do not translate a volume-only prepared broth into55.3g powder or equate it with another vendor's product.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Identify Biokar catalog and prepared stock strength for M2495; do not infer powder mass from its1L prepared-medium amount.

### 84: M17 broth

M2492 and2493 use unspecified M17 broth, with glucose versus lactose added to1% separately. The original label denotes the basal formulation family; supplier and base-carbohydrate composition are absent. A generic M17 concept cannot resolve those finished carbon-source variants by name alone.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Obtain supplier and basal carbohydrate formula for M2492/M2493 M17 before distinguishing shared base identity from separately added glucose/lactose.

### 85: Murashige and Skoog plant salt mixture (Wako)

NBRC19 names Wako Murashige and Skoog PLANT SALT MIXTURE at1.15g and adds40g sucrose and organic nutrients separately. Preserve salts-only scope; do not map this to a complete MS medium with vitamins/sugar or infer the exact Wako catalog from a broad MS label.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Find the Wako salts-only MS catalog and ionic/formulation composition; exclude vitamins and sucrose separately added in NBRC19.

### 86: R2A broth (DAIGO) (Nihon Pharm. Co.)

JCM805 explicitly uses DAIGO R2A powder at0.32g/L;JCM839 gives the full R2A recipe and says premixed DAIGO powder is available from Nihon Pharm. The product is the basal powder used at1/10 strength, not a new diluted-powder identity. Keep1/10 dose in occurrence context.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-daigo-r2a.

Remaining scope condition: Component list is literal source transcription, with component identities unresolved. No roles or organism-specific capabilities asserted. Manufacturer-name history does not authorize new vendor aliases beyond cited exact product sources.

### 87: R2A Broth "DAIGO"

NBRC1455 names DAIGO R2A broth code395-01681 at3.2g/L, with optional agar separate; the current Wako catalog confirms that exact product. This supports a DAIGO broth identity separate from R2A agar. The unrelated NBRC1509 URL in historical context is not evidence for R2A.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-daigo-r2a.

Remaining scope condition: Component list is literal source transcription, with component identities unresolved. No roles or organism-specific capabilities asserted. Manufacturer-name history does not authorize new vendor aliases beyond cited exact product sources.

### 90: TPGY broth

M2807 reports pre-reduced TPGY broth in anaerobic jars but provides neither formula nor catalog. TPGY expands to a formulation family, not a uniquely identified substance. Exact peptone/glucose/yeast proportions and reducing treatment must be obtained from the cited original study before a new fixed formulation is asserted.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Retrieve the actual TPGY formula and pre-reduction preparation from the study cited by M2807; the source only gives broth family and incubation.

### 91: Heart Infusion from (solids)

M2786's Todd-Hewitt component table identifies3.1g heart-infusion solids, with peptone, salts and sugar separately. It denotes the extract fraction, not500g original tissue or complete Todd-Hewitt broth. The source label alone does not establish whether commercially dried extract or prepared infusion was supplied.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Identify supplied physical state/process of the3.1g heart-infusion solids in M2786; avoid replacing with raw heart or complete ToddHewitt.

### 98: Bacto pleuropneumonia-like organisms (PPLO) broth without crystal violet

M2228 nests PPLO without CV inside Solution1, itself inside basal broth for Friis medium. The frozen recipe flattens this16g amount to the root and expands separate BHI ingredients. Preserve the PPLO product qualifier and nested source scope; do not interpret16g as finished-medium concentration or identify it with BHI.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Preserve M2228 nested Solution1/basal broth hierarchy and establish PPLO catalog before correcting the flattened16g quantity or attaching product aliases.

### 99: PPLO Broth w/o CV (Mycoplasma Broth) (BD 255420)

ATCC668 explicitly uses Difco255420 PPLO without CV at21g with Tryptone, sorbitol and later serum/sugar/arginine stocks. Its specific catalog supports the basal product only; the additional nutrients cannot be treated as components proving the powder's formulation.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-pplo-255420.

Remaining scope condition: Competing generic PPLO_Broth/PPLO_medium ownership requires reconciliation; no maintained aliases are removed here. Formula revision/lot is not documented; only source/catalog product identity is proposed. Native new-owner admission remains blocked by1165 until coordinator integration prerequisites land.

### 102: Todd Hewitt broth (Becton, Dickinson and Company, Franklin Lakes, NJ, USA)

M2963 names BD Todd Hewitt broth by one-litre prepared volume and adds1% Nacalai yeast extract. It is a broth input, not the finished THY medium. Existing Todd_Hewitt_Broth carries multiple manufacturers; exact source-specific formulation comparison is needed before extending that record's global resolving aliases.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Identify BD ToddHewitt catalog/stock strength for M2963 and reconcile the existing mixed Difco/Oxoid owner;1% yeast is recipient supplementation.

### 103: Beef heart infusion solids

M2211's Oxoid BHI subformula names5g beef-heart infusion solids. This is tissue extract, distinct from12.5g brain solids and from combined BHI. Frozen duplicate Difco-derived decomposition is contradictory provenance; any MIM beef-heart infusion link must preserve extracted-solids rather than raw heart scope.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Reconcile M2211 Oxoid5g beef-heart-solids against frozen duplicated Difco component rows; verify extract-solids state before any raw-heart link.

### 104: YEM broth

M2899 states YEM broth following Vincent1970 for rhizobia but does not provide the recipe. Yeast-extract/mannitol broth is a likely expansion; it must not become an exact alias for YM yeast/malt broth. Verify the cited edition/formulation before minting a fixed product identity.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Inspect the Vincent1970 formulation cited in M2899 and distinguish YEM yeast-extract/mannitol from YM yeast/malt; name expansion alone is not a fixed recipe.

### 105: GAM Broth powder (HyServe)

DSMZ1713 identifies HyServe standard GAM powder at59g/L, distinct from DSMZ1715 modified GAM at41.7g/L. The supplier page describes the standard product and removal of agar from GAM agar. MediaDive1563 links exactly to1713, supporting a source-bound local registry proposal.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-gam_broth_powder.

Remaining scope condition: Promotion preserves the existing stem and complete historical payload. Before integration verify the entire owner against native rules; no standard/modified or cross-supplier GAM merger, generic extract equality, new components, or roles are asserted.

### 106: Tryptose phosphate broth

The frozen occurrences use Tryptose phosphate broth as a liquid supplement, including10mL in BME/CTVM2 cell medium. DSMZ1670 confirms the liquid dose. The source does not disclose stock strength or supplier, so no conversion from mL or percent to grams of dehydrated powder is justified.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Determine supplier and stock concentration for the liquid/percent tryptose-phosphate supplement; retain DSMZ1670 10mL without mass conversion.

### 107: Man-Rogosa-Sharpe (MRS) broth

M2484 names MRS broth as the growth medium but gives only a one-litre placeholder, no supplier or composition. The MRS family is clear; formulation-specific identity and relation to the multiple Difco/Biokar/LabM source cases remain unspecified.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Obtain M2484 supplier/catalog or complete recipe and reconcile the multiple MRS owners before exact identity assignment.

### 108: Bacto Marine Broth 2216 (Difco)

All14 frozen occurrences name Difco Bacto Marine Broth2216. Corresponding NBRC sources vary its dose and separately add agar, salt, alginate, pyruvate or solvents. Those changes describe recipient recipes, not different powder identities. Add the exact supplier-qualified alias only; preserve inherited hold and separately review the existing full component payload.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-marine-aliases.

Remaining scope condition: Separate Difco_Marine_Broth and Marine_Broth owners are not merged. Inherited component IDs and complete assertion are preserved without scientific approval; the duplicated frozen514a decomposition must not justify them.

### 110: Nissui Modified GAM Broth

Both frozen sources point to NBRC1509 Nissui Modified GAM at41.7g/L, with optional agar separate. This supports the modified Nissui preparation, distinct from59g/L standard GAM. A HyServe marketing relationship is not yet a verified cross-supplier identity bridge.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Obtain explicit Nissui modified-GAM catalog/formula and any proposed HyServe distributor identity bridge;41.7g/L alone is insufficient.

### 114: Liver Broth (Oxoid CM 77)

DSMZ77 explicitly identifies Oxoid CM77 liver broth and directs preparation according to the bottle under nitrogen, without quantity or formula. This is a commercial preparation rather than simple liver infusion. The bottle/specification revision is needed before selecting a stable exact formulation or component list. Official CM0077 specification was retrieved and supports a concrete catalog-specific payload with four literal components; it explicitly retains liver tissue and differs from filtered infusions.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-oxoid-cm0077.

Remaining scope condition: Typical formula from current supplier specification, adjusted as required for performance. Source does not identify animal species or potassium-phosphate protonation; components remain literal and unmapped.

### 115: Columbia broth

M2256 names BBL Columbia broth and provides a nested12-component subformula, with NAD and25mM CaCl2 added to the parent medium. The components are evidence for the named broth, not independent exact identities for the whole product. Its disclosed formula and manufacturer provide a useful follow-up target; supplier catalog/version remains needed to compare commercial variants. The full12-component source formula now supports a source-defined registry payload; lacking catalog/version limits external synonym scope but does not prevent the concrete proposal.

Disposition: `new_distinct_ingredient_proposal`. Proposals: b-proposal-columbia-m2256.

Remaining scope condition: Complete source-defined basal formula, with literal component references. Generic ColumbiaBroth alias remains nonresolving. No catalog/version equivalence beyond TOGOM2256 is asserted.

### 117: Mycoplasma Broth Base

M2964's raw Mycoplasma Broth Base is annotated as Difco PPLO, while current BD separately sells BBL211458 Mycoplasma Broth Base. The source annotation does not override this lexical/catalog ambiguity. Preserve the3.5g SP4 basal input and require a source-specific catalog before attaching a resolving product alias.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Resolve the M2964 raw MycoplasmaBrothBase versus DifcoPPLO annotation using a catalog; BD211458 and255420 have distinct products.

### 118: GAM broth, modified (Nissui)

JCM1461 directly identifies Nissui modified GAM at41.7g/L. This can share the Nissui modified-family evidence of NBRC1509, but remains separate from standard GAM and from a HyServe product until an explicit manufacturer/distributor identity bridge is documented.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Establish Nissui modified-GAM catalog and explicit identity bridge before sharing HyServe owner;JCM1461 supplier/41.7g/L scope stays distinct.

### 120: M17 broth (Difco)

M2882 identifies Difco M17 broth by volume and adds0.5% glucose separately. The supplier differs from Oxoid M17 cases, and one-litre prepared broth cannot be assumed to have the37.25g powder formulation. Preserve the Difco prepared-base context.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Obtain DifcoM17 catalog/prepared stock strength for M2882; compare to Oxoid base only after excluding separately added0.5% glucose.

### 121: Heart, Infusion from 500 g

M2260 and2261 distinguish3.1g heart-infusion solids from the500g source tissue used to make them; one recipient adds sheep blood and agar. Treat the ingredient as extract solids rather than fresh heart, complete Todd-Hewitt broth, or a500g final ingredient dose.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Verify source2260/2261 heart-extract solids specification and physical state before mapping;500g denotes starting tissue, while3.1g is retained solids.

### 124: Marine broth 2216

MediaDive1607 identifies Marine broth2216 and the frozen attribute isBD-Difco at37.4g/L. MIM already has its local registry identity, but the native row is WITHHOLD. Identity-family evidence supports retaining the existing owner and proposed supplier aliases, not clearing the complete published payload's hold.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-marine-aliases.

Remaining scope condition: Separate Difco_Marine_Broth and Marine_Broth owners are not merged. Inherited component IDs and complete assertion are preserved without scientific approval; the duplicated frozen514a decomposition must not justify them.

### 126: Man Rogosa Sharp broth

MediaDive1112 records Man Rogosa Sharp broth with frozen MRS,Difco attribute. The spelling is a source variant of the MRS family, but current MIM has several separate MRS owners. Exact record consolidation needs a product-level comparison and occurrence reconciliation, not string similarity.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Reconcile ManRogosaSharp, MRS, Lactobacillus and Lactobacilli owners using catalog/formulation/source-ID evidence; keep1112 raw spelling.

### 127: MRS broth

MediaDive1899 records BD-Difco MRS broth,55g; it is a complex broth with no molecular registry identifier in the source. It is not a single nutrient, and separate MRS owners cannot be merged without supplier/formulation and source-ID reconciliation.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Identify source1899 Difco catalog and compare55g formulation across the separate MRS owners before consolidation.

### 128: MEM alpha Modification

The frozen MediaDive1923 attribute explicitly identifies BioWestP0440. The manufacturer's technical sheet confirms powder MEM-alpha with Earle salts and L-glutamine, WITHOUT sodium bicarbonate. The source's complex_compound=0 conflicts with this multicomponent preparation; annotate exact supplied form while retaining the generic owner's unmapped status pending its scope reconciliation.

Disposition: `supplied_form_correction`. Proposals: b-proposal-mem-p0440.

Remaining scope condition: This is bounded ingredient identity/form evidence, not a complete scientific review of inherited roles, component identifiers, synonyms, or whole published record payload.

### 129: Trypticase soy broth

MediaDive99 calls this complex Trypticase soy broth but its live synonym list also includes Bacto Tryptic Soy Broth without Dextrose. The frozen30g dose does not resolve that contradiction. A sugar-containing standard TSB formulation must not absorb an explicitly dextrose-free material by source synonym transfer.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Resolve the MediaDive99 mixed standard versus without-dextrose synonym list against the original TSB catalog and current owner scope.

### 134: Standard I Broth

MediaDive630 identifies Merck StandardI Broth at25g/L and links medium637. This is a named complex medium; a simple chemical or nutrient-broth ontology superclass does not establish its exact formula. Merck catalog/specification tied to this source is required before promotion or cross-product merging. Primary DSMZ637 and Merck manufacturer manual have now been retrieved; the matched source-specific formulation supports promotion of the existing owner, with four literal components.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-standard-i.

Remaining scope condition: Full inherited owner still requires native review; no cross-vendorStandardI alias or finalDSMZ637 identity is asserted.

### 135: Difco marine broth

MediaDive530's frozen attribute Difco2216 and37.4g dose make Marine2216 a supported candidate. However a separate Difco_Marine_Broth owner exists with its own import history. Do not silently adopt the canonical owner's bytes or merge records; coordinator must reconcile these owners and their source claims explicitly.

Disposition: `existing_identity_or_alias`. Proposals: none.

Remaining scope condition: Integration dependency only: reconcile the source530 Difco_Marine_Broth owner with Marine_Broth_2216 and retain the latter native full-payload hold until its own review passes. The source product identity is supported.

### 137: Veal infusion broth

MediaDive579 explicitly links DSMZ577; its frozen attribute Difco0344 matches the primary VY recipe exactly. This supports the same product as case12. The additional5g yeast extract belongs to VY, not to the source label Veal infusion broth.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-veal_infusion_broth.

Remaining scope condition: Promotion preserves the existing stem and complete historical payload. Before integration verify the entire owner against native rules; no standard/modified or cross-supplier GAM merger, generic extract equality, new components, or roles are asserted.

### 141: Lactobacillus MRS broth

MediaDive1776 identifies BD-Difco Lactobacillus MRS broth at55g/L inJ509. Singular Lactobacillus and plural Lactobacilli source spellings are lexical leads, but multiple MIM owners and supplier formulas require a scoped duplicate decision before consolidation.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Compare exact catalog/formulation and reconcile source1776 J509 with the other three MRS owners before consolidating singular/plural labels.

### 143: Todd Hewitt Broth

MediaDive1705 identifies BD-Difco Todd Hewitt broth at30g/L. It supports the named commercial broth context; the existing owner additionally carries an Oxoid alias. Keep the mixed-supplier boundary visible until the complete owner's product scope is resolved.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Compare Difco source1705 with the Oxoid alias in Todd_Hewitt_Broth; a mixed-vendor owner cannot be extended on30g dose alone.

### 146: Bacto Heart Infusion Broth

MediaDive1460 explicitly specifies BD238400 Bacto Heart Infusion Broth,25g/L. Heart-only broth is distinct from brain-heart infusion and heart agar; supplier catalog must remain attached. The existing placeholder preserves identity scope but does not yet verify a catalog-level ontology/registry promotion. Official BD catalog and ATCC254 now establish the product and three-part broth formula, supporting promotion of its existing Bacto owner. The separate genericHeartInfusionBroth owner remains unmerged.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-bd238400.

Remaining scope condition: Separate generic Heart_Infusion_Broth owner is not automatically merged; source1104 cases must be individually reconciled. Tissue500g is starting material, not final component concentration.

### 147: GAM Broth mod. powder

MediaDive1564 is the HyServe modified GAM powder inDSMZ1715,41.7g/L; primary DSMZ recipe and HyServe product evidence agree. Propose promotion of this existing owner, not creation of a duplicate or transfer of standard-GAM aliases.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-gam_broth_mod_powder.

Remaining scope condition: Promotion preserves the existing stem and complete historical payload. Before integration verify the entire owner against native rules; no standard/modified or cross-supplier GAM merger, generic extract equality, new components, or roles are asserted.

### 148: Lactobacilli MRS broth

MediaDive1711 records BD-Difco Lactobacilli MRS broth at55g/L across its source-medium list. This supports the MRS family but not automatic equality to the separate Lactobacillus/MRS/Man-Rogosa owners. Preserve all source IDs for a future explicit product-level merge assessment.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Reconcile source1711 media list and exact Difco formulation against separate Lactobacillus/MRS/ManRogosa owners before merge.

### 151: Meat infusion

MediaDive491 calls the ingredient Meat infusion and supplies no tissue species, extraction process or catalog. An animal-tissue extract mixture is supported; heart, liver, beef extract and commercial complete broths are not interchangeable. Species, extraction method and dried-versus-liquid state remain necessary for exact identity.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Determine tissue species, extraction method and liquid/dried state of source491 MeatInfusion; generic extract family does not select an exact substance.

### 152: PPLO broth

MediaDive953 groups PPLO spellings and has several recipient media, while its frozen row lacks catalog and crystal-violet detail. The existing placeholder also carries Difco aliases. Different BBL and Difco catalog products show why PPLO stem equality cannot settle a complete product identity.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Disambiguate source953 PPLO catalog/crystal-violet and existing generic Difco aliases before any overlap with new255420 or211458 candidates.

### 156: Brucella Broth

MediaDive1136 says Becton Dickinson Brucella Broth at35g/L. This supports a named broth preparation, not a Brucella organism or molecular nutrient. The exact BBL/Difco catalog and formulation revision are needed to decide whether an existing generic identity covers this product.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Identify the BBL/Difco catalog and formulation revision for source1136 BrucellaBroth35g/L before promotion; supplier BD alone is insufficient.

### 159: YM broth

MediaDive1683 specifies BD-Difco YM broth in75mL rather than dry mass. Preserve the liquid prepared medium and distinguish YM (yeast/malt family) from YEM rhizobial medium. Stock strength and catalog are not supplied by the frozen input.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Retrieve Difco YM catalog and prepared-broth strength for source1683;75mL cannot establish dry mass or identity with YEM.

### 160: GAM broth

MediaDive1620 specifies Nissui GAM at59g/L and maps toJCM source media. This agrees with standard Nissui GAM family, not modified41.7g/L GAM. No current supplier equivalence assertion justifies folding it into the HyServe owner.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Verify Nissui standard GAM formulation and explicit any HyServe product bridge; keep modified41.7g/L excluded.

### 161: Wilkins-Chalgren-Anaerobe-Broth

MediaDive2093 records Oxoid Wilkins-Chalgren Anaerobe Broth as1000mL prepared medium. Existing owner contains CM0643 catalog alias, while case179 separately names the same catalog with a spelling error. Full owner/source-dose reconciliation is needed before merging them; the liquid dose is not powder identity. Retrieved officialCM0643 specification supports a concrete promotion payload for the correctly spelled owner, with the competing source2140 owner as explicit integration dependency.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-cm0643.

Remaining scope condition: Apply only after provenance-preserving reconciliation withWilkins_Chalgrene_Anaerobe_Broth.yaml; this payload neither deletes that record nor silently copies its aliases/history. The source1000mLpreparedbroth remains an occurrence amount, not33g inferred productdose.

### 164: Tryptose-phosphate broth

MediaDive2163 has complex_compound=0 despite its explicit tryptose-phosphate broth label and a5% recipe dose. The separate DSMZ1670 liquid-supplement evidence confirms this is a broth preparation family, not phosphate or tryptose alone. The source's50g/L derived value cannot establish stock concentration without a percent basis.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Correct source2163 noncomplex classification only after establishing percent basis and tryptose-phosphate stock strength;50g/L derived value is not product evidence.

### 166: Bacto brain heart infusion

MediaDive965 records Bacto brain-heart infusion, and the existing MIM exact MICRO0000193 row is WITHHOLD for unproved product equivalence. OLS defines a broad hot-water heart/brain extract, not a specific Bacto formulation. Retain that hold and do not turn a brand stem into exact ontology identity.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Resolve held BactoBHI product/catalog equality and complete published payload before releasing exact MICRO0000193; broad extract definition is insufficient.

### 171: Bacto m TGE broth

MediaDive1896 names BD-Difco Bacto mTGE broth,18g/L, a membrane-filter medium preparation. This must stay distinct from generic TGE agar or an individual tryptone/glucose component. Exact catalog and formula needed for a local registry proposal remain unverified in the frozen source.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Retrieve BD-Difco mTGE catalog and18g/L formulation for1896; keep mTGEbroth distinct from TGEagar or individual nutrients.

### 177: Heart Infusion Broth

MediaDive1104 names Heart Infusion Broth with no catalog in the frozen5g dose. The source lists several media but does not establish that they all use BD238400. Preserve heart-only broth scope and avoid mapping it to raw heart or BHI.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Disambiguate the source1104 heart-broth media list and catalog/formula; do not assume all5g uses are BD238400.

### 178: GAM Broth powder

MediaDive1563 names HyServe GAM powder,59g/L, and referencesDSMZ1713. This exact source-to-recipe chain supports the same standard-GAM promotion as case105; modified GAM is a separate owner and formulation.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-gam_broth_powder.

Remaining scope condition: Promotion preserves the existing stem and complete historical payload. Before integration verify the entire owner against native rules; no standard/modified or cross-supplier GAM merger, generic extract equality, new components, or roles are asserted.

### 179: Wilkins Chalgrene Anaerobe Broth

MediaDive2140 explicitly names Oxoid CM643 but misspells Chalgren as Chalgrene. The corresponding current MIM duplicate has its own history, while2093 carries CM0643 as a synonym. Treat these as a strong product-duplicate candidate requiring explicit merge/provenance reconciliation; no source case is dropped. Retrieved officialCM0643 specification supports a concrete promotion payload for the correctly spelled owner, with the competing source2140 owner as explicit integration dependency.

Disposition: `existing_identity_or_alias`. Proposals: b-proposal-cm0643.

Remaining scope condition: Apply only after provenance-preserving reconciliation withWilkins_Chalgrene_Anaerobe_Broth.yaml; this payload neither deletes that record nor silently copies its aliases/history. The source1000mLpreparedbroth remains an occurrence amount, not33g inferred productdose.

### 180: Nutrient broth No. 2

MediaDive501 explicitly identifies Oxoid Nutrient BrothNo.2 at25g/L. Manufacturer CM0067 specification is10g special meat extract+10g peptone+5gNaCl; MICRO0000082 cites Difco3g beef extract+5g peptone. The current exact row and mixed BD/Difco aliases are scientifically incompatible; preserve WITHHOLD and require owner split before export.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Split/reconcile OxoidCM0067 10/10/5 formula from DifcoMICRO0000082 3/5 formula and inherited aliases; retain native exact-row hold.

### 182: Brain heart infusion broth

MediaDive827 calls this Brain heart infusion broth with no supplier/catalog in its frozen row. Its current MIM row remains WITHHOLD despite earlier mapping-only language. OLS's broad tissue-extract definition cannot select a commercial BBL/Difco/Oxoid formulation; preserve the unresolved exact-relation obligation.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Obtain supplier/catalog for source827 and reassess complete held BHI owner; broad tissue-extract ontology definition cannot establish commercial equality.

### 183: Marine Broth

MediaDive545 says Marine Broth with Difco attribute but does not say2216 in its raw name. The low0.5g recipe dose is not a formulation fingerprint. Its separate owner and multiple source media require catalog/formulation confirmation before a merge with Marine_Broth_2216.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Determine whether source545 DifcoMarineBroth is2216 and reconcile separate owner/provenance before merge;0.5g dose is not diagnostic.

### 187: Infusion Broth

Captured DSMZ1029 and its MediaDiveAPI identify source930 InfusionBroth as a25g subcomponent of BBLActinomycesBroth(BBL210920), alongside phosphate, salts, dextrose, cysteine, caseindigest,yeastextract andstarch. Neither full primary source names the infusion tissue or its internal formulation. The parent catalog does not identify this subingredient asheartbroth orBHI; remaining ambiguity is genuine after following the available mediumlead.

Disposition: `unresolved`. Proposals: none.

Remaining scope condition: Obtain supplierBBL210920 constituent documentation that identifies the tissue/process/formula of its25g InfusionBroth fraction. DSMZ1029 and its full API were retrieved and leave that fraction undefined; do not transfer the parent210920 identity to the subingredient.

## Validation limits

Strict LinkML validates record shape, not scientific adequacy. Parent worker runs the combined outcome auditor, native review/check gates and overlay collision/partonomy checks. No old positive review transfers automatically to changed payload bytes. New-owner release remains subject to issue1165. No roles, toxicity, causal graphs, whole-owner publication clearance, downstream build, branch merge or record application is claimed.
