# Named-stock source review — worker01

Author: /root/primary_context. Refreshed 2026-11-08T04:16:35.185667+00:00. Exact allocation:44 cases;73 original occurrences;51 full frozen recipe objects. Independent review pending. No maintained records changed.

Native self-review: [20261108T041604Z-w01-ns-selenite431-proposal](../../../../../reviews/structured/20261108T041604Z-w01-ns-selenite431-proposal/review.md), exact copies native-review.yaml/md. Verdict needs_curation, completion partial;2 major findings (one current classification finding open, inherited identity/decomposition hold deferred). This is not full scientific or release approval.

The one proposal corrects the existing JCM431 stock classification and preserves three exact raw431 reference aliases, covering nine occurrences. It retains UNMAPPED and issue718. Remaining41 cases have source-specific stock/mixture context; no generic absence-of-composition holds are substituted for available recipes.

Raw labels/complete occurrence objects are retained in source-cases.json and bound by exact case digests. Fetch receipts record actual UTC and SHA256. Raw HTTP headers stay private; text derivatives aid reading and are not substitutes for full body captures. Frozen1921 trace binds the imported pointer to JCM887 Basal minerals and JCM431; worker03 KG1921 is not claimed completed.

## 0: Selenite-tungstate solution**

Both NBRC recipes explicitly define the stock as NaOH 0.4 g, Na2SeO3·5H2O 6 mg and Na2WO4·2H2O 8 mg in distilled water 1 L, autoclaved; each receiving recipe adds 1 ml. These amounts coincide with JCM431, but the raw name is a source-local footnote rather than an explicit JCM431 reference. Retain the two NBRC recipe stock contexts; no exact mapping to selenite, tungstate or either sodium salt represents the mixture.

Applicability: CultureMech:007467 ingredients/11, CultureMech:007472 ingredients/11

Remaining requirement: For any future shared owner, bind both NBRC footnotes and the full formula to the same preparation identity and retain their source-specific raw labels; do not globally normalize all selenite-tungstate stocks to this formulation.

## 1: Selenite tungstate solution (see Medium No. 431 )

Both JCM receiving recipes explicitly reference the selenite/tungstate stock in Medium431. JCM431 defines NaOH 0.4 g, Na2SeO3·5H2O 6 mg, Na2WO4·2H2O 8 mg and water 1 L. The actual MIM owner imports MediaDive ingredient1921, whose live label explicitly references Medium431. This source identity, rather than lexical similarity, supports the exact raw alias and STOCK_SOLUTION/MINERAL_STOCK classification proposal. JCM1400 and1468 use 1 and0.5 ml respectively; doses do not alter the stock identity. Frozen source1921 is independently traced to JCM887 Basal minerals (solution4878, recipe_order7) with the explicit431 reference; full admitted medium/solution exports contain that one unique row. LiveJCM887 returns Nothing found; the original response is preserved with its actual2026-11-05 retrieval time.

Applicability: CultureMech:015886 ingredients/8, CultureMech:015874 ingredients/10

Remaining requirement: The proposal leaves component/registry grounding and the inherited unresolved-identity/decomposition hold open; coordinator must review exact bytes and source-specific alias semantics before application.

## 6: Solution A (see below)

JCM1474 defines Solution A as K2HPO4 10 g plus KH2PO4 10 g in distilled water 100 ml, adding 10 ml to the receiving broth. It is the phosphate stock local to this recipe, distinct from NBRC323 or971 Solution A and from either neat phosphate salt.

Applicability: CultureMech:015890 ingredients/9

Remaining requirement: Any stock representation must retain JCM1474, the 100 ml preparation basis, both salts and the exact 10 ml receiving amount; a global Solution A alias would conflate unrelated recipes.

## 11: Bicarbonate solution***

NBRC1257 defines 1 M bicarbonate stock using NaHCO3 8.4 g and distilled water 100 ml, saturated with CO2 and autoclaved under CO2; the medium receives 30 ml. This is a prepared stock, not neat sodium bicarbonate. Frozen nested stock composition encodes 8.4 G_PER_L although the primary preparation is 8.4 g per100 ml: retain the primary denominator instead of reusing that normalized value.

Applicability: CultureMech:007467 ingredients/12

Remaining requirement: Correct the CultureMech nested stock quantity basis with the 100 ml source preparation and preserve CO2 handling; source-backed stock context is resolved but the current flattened concentration must not become a new MIM assertion.

## 15: Modified Wolfe’s mineral solution (see Medium No. 915 )

All three receiving recipes explicitly point to JCM915. Its modified Wolfe mineral stock starts with JCM151 trace minerals and changes final Na2MoO4·2H2O to0.4 g/L, CuSO4·5H2O to0.02 g/L and NiCl2·6H2O to0.01 g/L. This differs from JCM628, JCM265, and the existing MIM Modified Wolfes Minerals and EDTA-based ATCC/Wolfes records. JCM151 retains MnSO4·xH2O and AlK(SO4)2 as printed; unprovided hydration must not be supplied.

Applicability: CultureMech:015865 ingredients/10, CultureMech:015866 ingredients/7, CultureMech:015877 ingredients/3

Remaining requirement: Preserve the JCM151 base plus JCM915 modifications as a versioned recipe, including unresolved MnSO4 hydration; do not alias by the shared Wolfe name.

## 41: Mineral solution 1

MediaDive main882 recipe_order5 identifies solution883 and40 ml. Solution883 and DSMZ436 define Mineral solution1 as K2HPO4 0.6%; the PDF does not specify a percent basis, while the API reports derived g_l=6. The exact source solution and existing CultureMech:015243 recipe reference establish stock context. Neither a percent-to-g/L assumption nor mapping the whole stock to K2HPO4 is warranted.

Applicability: CultureMech:015242 composition/8

Remaining requirement: If quantitative stock curation is needed, establish the percent basis and solvent/preparation volume from a primary clarification; preserve source883 and the existing CultureMech stock reference meanwhile.

## 45: Salt solution stock

CCAP PE defines salt stock with NaNO3 200 g and Na2HPO4·12H2O 20 g per1000 cm3, adding1 cm3 to the receiving medium. The full stock contains both salts, including explicit phosphate dodecahydrate; it is not an alias of either salt. The frozen recipe already carries both individual salts and a stock row, so a downstream expansion must avoid double counting.

Applicability: CultureMech:000110 ingredients/4

Remaining requirement: Represent the CCAP PE stock with its 1000 cm3 basis and source-local dose; verify the frozen phosphate identifier/label and whether individual rows are stock components before numerical expansion. No MIM alias is proposed for this source-local phrase.

## 48: Modified Wolfe's solution (see Medium No. 628 )

JCM1347 uses1000 ml modified Wolfe solution from JCM628. The referenced recipe is NH4Cl1 g, MgSO4·7H2O0.2 g, CaCl2·2H2O0.1 g, KH2PO4 0.05 g and water1 L. It is a defined mineral base, distinct from the trace-element recipes named modified Wolfe in JCM915 and MIM.

Applicability: CultureMech:015883 ingredients/0

Remaining requirement: Retain the exact JCM628 base recipe and its four salts in a recipe/stock representation; any alias to an existing Wolfe owner requires full component/basis agreement, absent for the inspected candidates.

## 58: FeS slurry solution*****

NBRC1356 prepares FeS by combining 0.5 M FeSO4·7H2O and0.5 M Na2S·9H2O, washing the precipitate repeatedly and resuspending to a20% slurry, then autoclaving at110 C for30 min under N2. The receiving medium uses2 ml. This is a prepared precipitate suspension, not either precursor salt and not automatically a specified solid FeS phase.

Applicability: CultureMech:007474 ingredients/10

Remaining requirement: Obtain the basis of the stated20% slurry and, if a phase-specific chemical identity is required, characterize/identify the precipitated FeS phase. The stock context and preparation remain usable without inventing those attributes.

## 68: Wolfe's mineral solution (see Medium No. 265 )

JCM1362 and1429 explicitly reference JCM265 Wolfe mineral stock. JCM265 adds NiCl2·6H2O0.02 g, Na2SeO3 0.001 g and Na2WO4·2H2O0.01 g to1 L JCM151 trace minerals. This is an NTA-based modified recipe; existing EDTA-based MIM Wolfe/ATCC stocks and Modified Wolfes Minerals have materially different compositions. The receiving doses10 and1 ml must stay occurrence-specific.

Applicability: CultureMech:015840 ingredients/7, CultureMech:015864 ingredients/3

Remaining requirement: Preserve the JCM151 base plus the three JCM265 additions, and unresolved MnSO4 hydration in the base, before component-level grounding. No global Wolfe alias is supported.

## 69: Mineral solution A (see Medium No. 1353 )

JCM1366 explicitly references Mineral solution A in JCM1353, the EDTA/KOH trace-metal recipe: EDTA2.5 g, KOH2.2 g, FeSO4·7H2O1.1 g, MnCl2·4H2O98.4 mg, ZnSO4·7H2O28.8 mg, CoCl2·6H2O23.8 mg, CuCl2·2H2O17.2 mg, Na2MoO4·2H2O24.2 mg, H3BO3 31 mg and water1 L, pH6.5 with HCl. It shares the source-defined stock with the JCM1353 see-below case, not other generic mineral A labels.

Applicability: CultureMech:015844 ingredients/6

Remaining requirement: Use an exact recipe-level JCM1353 stock cross-reference with its pH titrant context; no maintained MIM owner was established by source identity.

## 70: Mineral solution A (see below)

The local Mineral solution A table in JCM1353 defines the EDTA2.5 g/KOH2.2 g/FeSO4·7H2O1.1 g trace-metal stock with Mn, Zn, Co, Cu, Mo and B salts per1 L, adjusted to pH6.5 with HCl. JCM1353 adds5 ml. The see-below phrase resolves by this recipe, and is not a universal ingredient name.

Applicability: CultureMech:015836 ingredients/7

Remaining requirement: Retain the full JCM1353 Mineral A table, its1 L basis and HCl pH adjustment. This can share source context with JCM1366 explicit1353 reference but does not justify a global generic Mineral A alias.

## 71: Ni-Se-W solution (see below)

JCM1462 defines Ni-Se-W stock with NiCl2·6H2O30 mg, Na2SeO3·5H2O0.3 mg, printed Na2WO2·2H2O0.4 mg and water1 L. JCM1463 explicitly uses1462 with21 g/L NaCl instead of9 g/L, so the stock is inherited unchanged. The W formula is preserved as printed; it cannot be silently corrected toNa2WO4.

Applicability: CultureMech:015871 ingredients/7, CultureMech:015881 ingredients/7

Remaining requirement: Primary confirmation/correction of Na2WO2·2H2O is required before grounding that component. Preserve the source recipe and1463 inheritance; no exact chemical/registry promotion is proposed.

## 72: Wolfe’s mineral solution (see Medium No. 265 )

JCM1412 uses10 ml of the explicitly referenced JCM265 Wolfe mineral stock: JCM151 trace minerals1 L plus NiCl2·6H2O20 mg, Na2SeO3 1 mg and Na2WO4·2H2O10 mg. The curly apostrophe is an orthographic variation within this explicit source reference; identity is supported with the JCM1362/1429 stock context, not with existing compositionally different MIM Wolfe stocks.

Applicability: CultureMech:015857 ingredients/6

Remaining requirement: A source-level shared stock representation can preserve the three JCM265 references and JCM151 base; unresolved base hydration and distinct MIM candidate recipes preclude a blind alias.

## 86: Se/W solution***

Both NBRC pages list Na2SeO3 4 mg and Na2WO4 4 mg. NBRC1020 explicitly gives distilled water1 L; NBRC824 omits a solvent/volume row for this stock. Both receiving media add1 ml. Their component names differ from hydrated JCM317/JCM852/JCM431 recipes, and the absent NBRC824 denominator cannot be supplied from another recipe.

Applicability: CultureMech:007450 ingredients/9, CultureMech:007496 ingredients/8

Remaining requirement: Recover the missing NBRC824 solvent/preparation volume before asserting identical concentrations or merging quantitative stock identities; preserve two source contexts and the exact unhydrated printed salt formulas.

## 89: Mineral solution II (see below)

JCM1385 says to use Medium1130 with0.2% mannitol. JCM1130 Mineral solutionII is KH2PO4 3 g,(NH4)2SO4 6 g,NaCl6 g,MgSO4·7H2O0.6 g,CaCl2·2H2O0.6 g and water1 L; the receiving recipe uses150 ml. The roman numeral is local to this recipe and distinct from DSMZ436 Mineral2.

Applicability: CultureMech:015879 ingredients/8

Remaining requirement: Preserve the JCM1385→1130 inheritance, five-salt formula,1 L basis and150 ml input; do not normalize roman/Arabic solution numbers across sources.

## 90: KOH solution

All four frozen occurrences are nested preparation reagents of JCM151/TOGO M142 trace minerals. JCM151 adjusts NTA to pH6.5 with KOH solution and final stock to pH7; it supplies no KOH concentration or dose. TOGO source records explicitly connect M725/M708/M1070/M253 to M142. Live JCM703/688 searches return Nothing found; MediaDive and TOGO preserve their source identity/inheritance. The frozen CHEBI potassium-hydroxide IDs identify the solute only, not a quantified stock. Available primary base recipesJCM702 and687 explicitly reference JCM151, corroborating MediaDive J703→702 andJ688→687 inheritance.

Applicability: CultureMech:003049 solutions/0/composition/12, CultureMech:007588 solutions/1/composition/13, CultureMech:003033 solutions/0/composition/12, CultureMech:009109 solutions/1/composition/13

Remaining requirement: A quantitative KOH stock requires source concentration/solvent and titrant amount, currently unspecified. Preserve VARIABLE/unquantified preparation context rather than creating a standard-strength solution.

## 93: FeCl2 solution (see Medium No. 187 )

All eleven receiving recipes explicitly reference JCM187 FeCl2 solution. It contains25% HCl(7.7 M)10 ml, FeCl2·4H2O1.5 g and distilled water990 ml. This acidic stock is not identical to neat FeCl2 or its tetrahydrate. JCM1456 uses10 ml while the other ten frozen occurrences use1 ml; the shared stock identity does not license a common dose.

Applicability: CultureMech:015860 ingredients/11, CultureMech:015861 ingredients/10, CultureMech:015888 ingredients/6, CultureMech:015835 ingredients/6, CultureMech:015843 ingredients/4, CultureMech:015848 ingredients/5, CultureMech:015849 ingredients/5, CultureMech:015856 ingredients/6, CultureMech:015862 ingredients/4, CultureMech:015874 ingredients/8, CultureMech:015875 ingredients/8

Remaining requirement: Represent the JCM187 acidic stock with the exact hydrate, HCl strength, preparation quantities and each occurrence dose. Current MIM Fecl2/Fecl2_X_4_H2o records are component candidates only.

## 99: Solution A*

The same raw Solution A* label denotes different recipes. NBRC323 defines yeast extract1 g,(NH4)2SO4 0.2 g,MgSO4·7H2O0.5 g,CaCl2·2H2O0.25 g,KH2PO4 0.6 g and water500 ml,pH3–4;500 ml is used. NBRC971 defines ferric ammonium citrate5 g andCaCl2 0.5 g per1 L;10 ml is used. A single label-level ingredient identity would merge chemically different mixtures.

Applicability: CultureMech:007487 ingredients/0, CultureMech:007509 ingredients/4

Remaining requirement: Split downstream resolution by original recipe source (NBRC323 versus971), retaining their distinct formulas and preparation denominators; do not create a global Solution A synonym.

## 102: NaOH solution

This exact nested NaOH solution occurrence is the pH9 adjustment for the DSMZ829 Growth-stimulating factors preparation. Its strength and amount are not stated. A separate Na-dithionite stock on the same source page uses0.5 ml1 N NaOH; that numeric strength does not apply to this occurrence.

Applicability: CultureMech:009155 solutions/5/composition/8

Remaining requirement: Keep this titrant unquantified until a source explicitly states its strength/amount. Do not transfer1 N from the adjacent Na-dithionite preparation or exact-map the whole solution to neat NaOH.

## 103: K solution**

NBRC989 K solution is KH2PO4 90 g,NaCl90 g,(NH4)2SO4 90 g and water1 L; the receiving medium adds5 ml. It is a three-salt macro-mineral stock; the letter K does not mean pure potassium or potassium chloride.

Applicability: CultureMech:007510 ingredients/4

Remaining requirement: Use the NBRC989 K stock table and exact1 L basis; no global K solution alias or single-component identity is justified.

## 104: Mineral solution B* (see below)

JCM1353 Mineral solutionB is Na2WO4·2H2O1.65 g,Ni(NH4)2(SO4)2·6H2O19.8 mg,VOSO4 0.82 mg and water1 L, filter sterilized; the receiving medium adds1 ml. This W/Ni/V stock is distinct from the EDTA-based MineralA in the same recipe.

Applicability: CultureMech:015836 ingredients/11

Remaining requirement: Preserve exact printed VOSO4 form, double-salt nickel identity, filter sterilization and1 L basis before any component grounding. No general MineralB owner identified.

## 110: Se/W solution (see Medium No. 317 )

JCM1425 explicitly references JCM317 Se/W solution: Na2SeO3 4 mg,Na2WO4·2H2O4 mg,water1 L. Its1 ml addition is source-specific. This formulation differs from NBRC1020/824 printed Na2WO4, from JCM852 hydrated selenite and lower amounts, and from the alkaline JCM431 stock.

Applicability: CultureMech:015862 ingredients/6

Remaining requirement: Use the JCM317 stock reference and preserve its exact two salt forms; avoid a general Se/W alias across incompatible formulations.

## 111: Ni-Se-W solution (see Medium No. 1462 )

JCM1464 explicitly references the Ni-Se-W stock in1462, containing NiCl2·6H2O30 mg,Na2SeO3·5H2O0.3 mg,printed Na2WO2·2H2O0.4 mg,water1 L. This establishes the same source stock as the1462/1463 local-label case, while preserving the source tungsten-formula problem.

Applicability: CultureMech:015889 ingredients/7

Remaining requirement: Confirm/correct Na2WO2·2H2O with JCM before component grounding; retain1464→1462 source cross-reference and do not silently repair it.

## 112: Sulfide solution****

NBRC1257 defines1 M sulfide solution withNa2S·9H2O12 g and water50 ml, filter sterilized under N2; the medium uses1 ml. Frozen nested composition reports12 G_PER_L, losing the50 ml preparation denominator. Neither the stock nor its redox handling is represented by a neat sodium sulfide alias.

Applicability: CultureMech:007467 ingredients/13

Remaining requirement: Repair the CultureMech nested quantity basis to retain12 g per50 ml and N2/filter handling before deriving concentrations. Any chemical component must preserve the nonahydrate.

## 116: Modified Hutner's solution

Modified Hutner stock in NBRC943 contains NTA10 g,MgSO4·7H2O29.7 g,CaCl2·2H2O3.34 g,(NH4)6Mo7O24·2H2O9.25 mg,FeSO4·7H2O99 mg and50 ml Metal salt44; total preparation1 L. NTA is neutralized with7.3 g KOH,pH6.6–6.8. Metal salt44 itself has NaEDTA250 mg,ZnSO4·7H2O1095 mg,FeSO4·7H2O0.5 g,MnSO4·H2O154 mg,CuSO4·5H2O39.2 mg,Co(NO3)2·6H2O24.8 mg,Na2B4O7·10H2O17.7 mg per100 ml plus drops concentratedH2SO4. It is a nested prepared mixture.

Applicability: CultureMech:015904 ingredients/5

Remaining requirement: Preserve both preparation denominators and titrants; explicitly resolve unspecified NaEDTA form before exact component grounding. Do not substitute a generic Hutner formulation or flatten all amounts asg/L.

## 119: Phenanthrene solution

NBRC1339/TOGO M2041 phenanthrene stock is250 mM phenanthrene in DMSO, added10 ml and filter sterilized through a DMSO-safe filter. The solvent and strength are part of the supplied preparation. MIM Phenanthrene is a contextual solute candidate, not an exact owner for this solution.

Applicability: CultureMech:008631 ingredients/4

Remaining requirement: Preserve250 mM,DMSO and the10 ml source input in a recipe/stock context; a global alias to neat phenanthrene would discard the solvent.

## 121: VFA solution

MediaDive5080 recipe_order5 uses3.1 ml solution3774. The source stock comprises acetic acid17 ml,propionic6 ml,n-butyric4 ml,and1 ml each iso-butyric,n-valeric,iso-valeric,DL-alpha-methylbutyric acids, summing31 ml; no solvent is stated. Live JCM1029 returns Nothing found, so the available exact MediaDive stock body is the source evidence. The stock is a seven-acid mixture, not a broad volatile-fatty-acid class or one acid.

Applicability: CultureMech:013996 composition/15

Remaining requirement: Retain solution3774 and its31 ml mixture composition with the3.1 ml receiving input; do not supply water or infer standardized VFA recipes from another medium.

## 123: M solution***

NBRC989 M solution containsMnCl2·4H2O4 g andCoCl2·6H2O4 g in water1 L; the medium adds2.5 ml. Both specified hydrates belong to this stock; the letter M is source-local.

Applicability: CultureMech:007510 ingredients/5

Remaining requirement: Keep the NBRC989 two-salt formula and1 L basis, separate from K andC stocks; no generic mineral or single manganese identity is sufficient.

## 125: Mineral solution

Both frozen occurrences explicitly identify MediaDive solution607 and add38 ml (main5080/J1029 and606/DSMZ330). Solution607 and DSMZ330 giveKH2PO4 6 g,NaCl12 g,(NH4)2SO4 6 g,CaCl2·2H2O1.6 g,MgSO4·7H2O2.5 g,water1000 ml. Shared source accession and formula establish the exact stock across these two contexts; the generic Mineral solution label alone would not. Existing CultureMech:014792 stock reference should remain.

Applicability: CultureMech:013996 composition/14, CultureMech:014786 composition/13

Remaining requirement: Preserve source607 and the existing CultureMech stock link with all five salts and1000 ml basis; no MIM owner is identified merely by the generic mineral label.

## 129: Mineral solution 2

Main882 recipe_order6 adds40 ml solution884. DSMZ436 and the API both printKH2PO4 0.6%,(NH4)2SO4 2%,NaCl1.2%,MgSO4·7H2O0.25%,CaCl2·7H2O0.16%. The unusual calcium hydrate is in the primary PDF itself, not solely a MediaDive transcription. Percent basis is unstated. Keep existing CultureMech:015244 stock context; no inferred dihydrate or g/L replacement is justified.

Applicability: CultureMech:015242 composition/9

Remaining requirement: Obtain primary clarification of CaCl2·7H2O and percent basis before component-specific quantitative grounding. Retain literal source formula and source884 while these remain unresolved.

## 130: Modified Wolin's mineral solution

Main277/DSMZ161 adds10 ml solution241, the modified Wolin mineral stock inherited from DSMZ141. DSMZ161 listsNTA1.5 g,MgSO4·7H2O3 g,MnSO4·H2O0.5 g,NaCl1 g,FeSO4·7H2O0.1 g,CoSO4·7H2O0.18 g,CaCl2·2H2O0.1 g,ZnSO4·7H2O0.18 g,CuSO4·5H2O0.01 g,AlK(SO4)2·12H2O0.02 g,H3BO3 0.01 g,Na2MoO4·2H2O0.01 g,NiCl2·6H2O0.03 g,Na2SeO3·5H2O0.3 mg,Na2WO4·2H2O0.4 mg andwater1 L;pH6.5 then7 withKOH. This differs from inspected MIM Wolfe candidates in chelator, salts and amounts.

Applicability: CultureMech:012076 composition/15

Remaining requirement: Preserve solution241 and existing CultureMech:011798 stock reference with the whole recipe and unquantified KOH adjustments; Wolin/Wolfe name similarity does not establish an MIM owner.

## 134: C solution****

NBRC989 C solution isCaCl2·2H2O10.6 g andwater1 L, added2.5 ml. This is a source-defined aqueous stock of the dihydrate and is distinct from neat calcium chloride or its other hydrates.

Applicability: CultureMech:007510 ingredients/6

Remaining requirement: Preserve the10.6 g/1 L stock basis and2.5 ml source input; a component-level CaCl2·2H2O identity must not replace the whole solution.

## 136: 10xM9 solution**

NBRC1339 10xM9 solution containsKH2PO4 30 g,Na2HPO4 60 g,NH4Cl10 g,NaCl5 g andwater1 L, separately autoclaved;100 ml is added. The explicit formula defines this stock more precisely than the label10x, and matches the TOGO M2041 10xM9 context. It is not complete M9 medium because phenanthrene,DMSO and other receiving ingredients are separate.

Applicability: CultureMech:007473 ingredients/1

Remaining requirement: Retain the source recipe, four printed salt forms and1 L preparation; do not fill unspecified Na2HPO4 hydration or alias to complete M9 medium.

## 137: Selenite-tungstate solution* (see Medium No. 431 )

JCM1364 explicitly references Medium431 selenite-tungstate stock and uses1 ml; the asterisk is a footnote marker, not a new substance. JCM431 specifiesNaOH0.4 g,Na2SeO3·5H2O6 mg,Na2WO4·2H2O8 mg,water1 L. MIM UNMAPPED_0519 importsMediaDive1921 with the same explicit431 source reference. The bounded proposal adds this exact raw alias and stock classification only. Frozen source1921 is independently traced to JCM887 Basal minerals (solution4878, recipe_order7) with the explicit431 reference; full admitted medium/solution exports contain that one unique row. LiveJCM887 returns Nothing found; the original response is preserved with its actual2026-11-05 retrieval time.

Applicability: CultureMech:015842 ingredients/10

Remaining requirement: Keep the inherited decomposition/grounding hold; review proposed bytes before application. The star-free generic name and JCM1365 formula are outside this alias claim.

## 138: Se/W solution (Medium No.852)

JCM1188 inherits Medium1187, which references JCM852 Se/W stock. JCM852 definesNa2SeO3·5H2O1.7 mg andNa2WO4·2H2O3.3 mg inwater1 L. The receiving marineChloroflexi medium uses1 ml. This differs from JCM317,NBRC1020/824 and JCM431 stocks in forms and/or amounts.

Applicability: CultureMech:015391 ingredients/9

Remaining requirement: Retain the1188→1187→852 source chain and exact hydrated salts; do not collapse allSe/W labels or use a generic selenite owner for the mixture.

## 144: Selenite-tungstate solution (see Medium No. 431 )

All six frozen occurrences explicitly reference JCM431 and add1 ml. The referenced alkalineNaOH0.4 g/Na2SeO3·5H2O6 mg/Na2WO4·2H2O8 mg/water1 L stock matches the source identity imported by actual MIMownerUNMAPPED_0519 fromMediaDive1921. The exact raw alias plus stock classification is supported; the source reference distinguishes it from other selenium/tungsten stocks. Frozen source1921 is independently traced to JCM887 Basal minerals (solution4878, recipe_order7) with the explicit431 reference; full admitted medium/solution exports contain that one unique row. LiveJCM887 returns Nothing found; the original response is preserved with its actual2026-11-05 retrieval time.

Applicability: CultureMech:015860 ingredients/13, CultureMech:015861 ingredients/12, CultureMech:015841 ingredients/10, CultureMech:015848 ingredients/7, CultureMech:015849 ingredients/7, CultureMech:015856 ingredients/8

Remaining requirement: Retain UNMAPPED and the inherited identity/decomposition hold; component/registry promotion and release support are not part of the proposal.

## 147: 10xM9 solution

TOGO M2041 identifies originalNBRC1339 and its10xM9 stock:KH2PO4 30 g,Na2HPO4 60 g,NH4Cl10 g,NaCl5 g,water1 L,100 ml receiving input and separate autoclaving. This is the same source stock as the starred NBRC1339 case, not an inferred equivalence from10x lettering.

Applicability: CultureMech:008631 ingredients/1

Remaining requirement: Preserve NBRC1339/TOGO source equivalence and exact forms/basis; do not extend to all10xM9 commercial or differentlyhydrated formulations.

## 148: Reducing agent solution (see Medium No. 521 )

JCM1344 explicitly references JCM521 reducing-agent solution. JCM521 definesNa2S·9H2O12.5 g plusL-cysteine hydrochloride monohydrate12.5 g andwater1 L, autoclaved/stored underN2; the receiving medium uses10 ml. The MIM Reducing_Agent class and either individual reductant do not denote this prepared mixture.

Applicability: CultureMech:015834 ingredients/13

Remaining requirement: Keep the JCM521 two-component formula and N2 preparation context; a broad reducing-agent role/class cannot serve as an exact chemical or stock owner.

## 153: Mineral solution I (see below)

JCM1385 inherits1130 with0.2%mannitol. JCM1130 Mineral solutionI isK2HPO4 3 g andwater1 L, added150 ml. It is distinct from1130 MineralII and fromDSMZ436 Mineral1, which states0.6% with unspecified percent basis.

Applicability: CultureMech:015879 ingredients/7

Remaining requirement: Preserve the1385→1130 reference,3 g/1 L preparation and150 ml receiving dose; do not normalize local roman/Arabic stock numbers or collapse to neatK2HPO4.

## 154: Solution B (see below)

JCM1474 SolutionB containsMgSO4·7H2O4 g,NaCl0.2 g,FeSO4·7H2O0.2 g,MnSO4·xH2O0.2 g andwater100 ml;5 ml is added. The unspecified Mn hydrate is explicit. This differs from NBRC323 glucose/agar SolutionB and NBRC971 sucrose SolutionB.

Applicability: CultureMech:015890 ingredients/10

Remaining requirement: Preserve the100 ml basis and unresolved MnSO4·xH2O form; obtain hydration only if exact component grounding is needed. No global SolutionB synonym is safe.

## 156: Selenite-tungustate solution (see below)

JCM1365 itself prints the misspelled Selenite-tungustate label and definesNaOH0.4 g,Na2SeO3·5H2O0.06 g,Na2WO4·2H2O0.08 g andwater1 L. Relative to JCM431 the two selenium/tungsten salt amounts are10×, whileNaOH remains0.4 g/L. The stock is not a uniform10× JCM431 preparation and must not share its exact alias merely by correcting the spelling.

Applicability: CultureMech:015843 ingredients/6

Remaining requirement: Retain the source typo as raw provenance and the distinct component ratios. Any normalized display label must remain bound to JCM1365 and cannot imply JCM431 identity.

## 157: Solution B**

SolutionB** denotes two different stocks: NBRC323 glucose1 g plus optionalagar20 g inwater500 ml, used500 ml; NBRC971 sucrose100 g inwater1 L, used10 ml. Neither recipe nor sugar identity is interchangeable. The optional agar also means the NBRC323 solid/liquid preparation branch must remain explicit.

Applicability: CultureMech:007487 ingredients/1, CultureMech:007509 ingredients/5

Remaining requirement: Resolve by originalNBRC source and preserve the optionalagar branch and preparation denominators; do not add a global SolutionB alias or collapse both stocks to generic sugar.

## 160: Resazurin solution****

Both NBRC1020 and824 explicitly define resazurin1 g pluswater1 L, added1 ml. This source agreement supports a common recipe context across the two occurrences. It does not establish resazurin sodium salt, and a neat-resazurin MIM record cannot represent the entire1 g/L solution.

Applicability: CultureMech:007450 ingredients/10, CultureMech:007496 ingredients/9

Remaining requirement: Keep the source stock identity and solvent/basis; obtain an explicit source reagent specification before choosing free compound versus sodium salt at component level.

