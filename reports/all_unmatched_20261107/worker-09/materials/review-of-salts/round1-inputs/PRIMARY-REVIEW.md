# Worker09 salts primary review

All 69 assigned cases were reviewed against their complete frozen source contexts. There are 14 isolated owner proposals; maintained records and generated mappings were not changed. Independent skeptical review remains pending.

Exact input/output hashes and checks are in `subset-integrity.json`. Successful HTTP retrieval is distinguished from primary content: JCM empty pages, NIES redirect-to-homepage,404 and supplier blocks are unsuccessful attempts. The shared JCM1118 capture preserves its original materials-researcher timestamp and exact bytes.

## Findings requiring coordinator/source follow-up

- Existing issue344 covers contradictory hydrate metadata. No nonexistent-hydrate assumption or sulfate-slip repair is made. Source label, CAS and derived molecular weight can contradict one another.
- Existing CultureMech408 covers dose-unit defects; BB MoO loses subscript3 and stock boundary, and MDY-V ZnCl2 gains unsupported six-water annotation. ATCC1925 has Titanium(III) citrate versus TiCl2 internal contradiction.
- FeCl2 dihydrate is supported by NBRC1326, OECD CAS16399-77-2 and PubChem. The new CAS proposal requires fresh exact-term search/native review, asymmetric parent mapping and registry rows before integration.
- Supplier P3556 is egg-yolk phosphatidylcholine with varied acyl composition, incompatible with the single CHEBI86658 molecular species; preserve quarantines.
- Merck35675 and UTEX source CAS13408-09-8 support only the beta/disodium/pentahydrate cases. Issues1053/1118 and generic-source ambiguity remain.
- CaCl2 and cobalt hexahydrate owner payloads contain inherited conflicting aliases. Exact new aliases do not approve those payloads; retain WITHHOLD until full review.
- Mncl2_X_4_H2o is also referenced by worker02. No byte adoption or cross-shard completion is inferred.

## Per-case scientific decisions

### 0 — Na3-NTA

`CM_NAME:004ac4f55986c1785d86b001779e3dcfcc81b0bb9ad6242272e899c412924111` — existing_identity_or_alias

Na3-NTA states three sodium counterions, and TOGO M2562 uses it as a weighed component. ChEBI132766 explicitly defines sodium:nitrilotriacetate 3:1. This supports the unqualified trisodium-salt name; it does not identify the separate monohydrate stock in MediaDive1482.

**Applicability:** CultureMech:009131 ingredients/24 {"concentration": {"unit": "G_PER_L", "value": "1.63"}, "notes": "Role: Mineral source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "Na3-NTA"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-chebi-132766, sa-togo-M2562, sa-recipe-3dc4c7f1f4ea96, sa-owner-nitrilotriacetic_acid_trisodium_salt

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 1 — 1M CaCl2

`CM_NAME:0b702f7e3bfef3e6092fdd40fb55407351b5640bbbf53d6c8ffff71b4ac4bc7b` — stock_product_mixture_context

1M CaCl2 is a concentration-qualified preparation. TOGO M2790 specifies a 10 microlitre addition; frozen 10 G_PER_L is a source-unit error. Neither a 1M stock nor its volume dose is the identity of solid calcium chloride.

**Applicability:** CultureMech:009338 ingredients/0 {"concentration": {"unit": "G_PER_L", "value": "10"}, "notes": "Role: Mineral source; Properties: Solution, Inorganic compound, Defined component", "preferred_term": "1M CaCl2"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-chebi-3312, sa-togo-M2790, sa-recipe-374c97a949cebe, sa-owner-cacl2

**Next requirement:** Recover the 1M stock preparation and carrier, then represent the stock and its volume dose separately from its calcium chloride component.

### 2 — beta-Glycerol phosphate disodium salt pentahydrate

`CM_NAME:0d80a0eb98381c2b6f4b4518408fc3b7f282acf824ce941695dffbc830f8d274` — existing_identity_or_alias

The four UTEX occurrences are components of ES enrichment stock, with beta positional identity, two sodium ions and five waters explicit. Their source annotations give CAS13408-09-8. This is the existing disodium glycerol2-phosphate pentahydrate, distinct from anhydrous CHEBI132089 and glycerol3-phosphate. The proposed synonym names the nested solute, not the complete seawater or enrichment stock.

**Applicability:** CultureMech:000163 solutions/0/composition/2 {"concentration": {"unit": "G_PER_L", "value": "0.49"}, "evidence": [{"explanation": "Claim: solutions[0].composition[2].concentration. 0.98 g/2 L in this explicitly declared stock volume gives 0.98 g / 2 L = 0.49 g/L. Retain as stock composition, not final-medium concentration. Exact component cell: \"Na 2 glycerophosphate • 5H 2 O (CAS: 13408-09-8)\". Locator: Ingredient table row 2, Amount column; component cell quoted separately. The packaged MIM alias reproduces the wrong sn-glycerol-3-phosphate mapping; do not use it as independent confirmation.", "reference": "https://utex.org/products/enrichment-solution-for-seawater-medium", "snippet": "0.98 g/2 L", "supports": "SUPPORT"}, {"explanation": "Identity only for solutions[0].composition[2]. Remove the unsupported primary and MIM identifiers; retain source-specified mass, pentahydrate and CAS. No exact replacement ID is established by this bounded review. The linked UTEX component identifies the supplied form/catalog or CAS; this chemical source does not support a recipe amount. Locator: Product 50020 heading; separate CAS Number field is 13408-09-8.", "reference": "https://www.sigmaaldrich.com/US/en/product/sigma/50020", "snippet": "β-Glycerol phosphate disodium salt pentahydrate", "supports": "SUPPORT"}, {"explanation": "Identity only for solutions[0].composition[2]. Remove the unsupported primary and MIM identifiers; retain source-specified mass, pentahydrate and CAS. No exact replacement ID is established by this bounded review. The linked UTEX component identifies the supplied form/catalog or CAS; this chemical source does not support a recipe amount. Locator: ChEBI Name; separate formula and registry fields.", "reference": "https://www.ebi.ac.uk/chebi/CHEBI:15978", "snippet": "sn-glycerol 3-phosphate", "supports": "SUPPORT"}], "notes": "Converted from 0.98 g/2 L in the UTEX Enrichment Solution for Seawater Medium recipe. Source CAS 13408-09-8 denotes the disodium beta-glycerophosphate pentahydrate, not sn-glycerol 3-phosphate. No exact replacement ontology identifier is asserted.", "nutritional_roles": ["PHOSPHATE_SOURCE"], "preferred_term": "beta-Glycerol phosphate disodium salt pentahydrate"} | CultureMech:000164 solutions/0/composition/2 {"concentration": {"unit": "G_PER_L", "value": "0.49"}, "evidence": [{"explanation": "Claim: solutions[0].composition[2].concentration. 0.98 g/2 L in this explicitly declared stock volume gives 0.98 g / 2 L = 0.49 g/L. Retain as stock composition, not final-medium concentration. Exact component cell: \"Na 2 glycerophosphate • 5H 2 O (CAS: 13408-09-8)\". Locator: Ingredient table row 2, Amount column; component cell quoted separately. The packaged MIM alias reproduces the wrong sn-glycerol-3-phosphate mapping; do not use it as independent confirmation.", "reference": "https://utex.org/products/enrichment-solution-for-seawater-medium", "snippet": "0.98 g/2 L", "supports": "SUPPORT"}, {"explanation": "Identity only for solutions[0].composition[2]. Remove the unsupported primary and MIM identifiers; retain source-specified mass, pentahydrate and CAS. No exact replacement ID is established by this bounded review. The linked UTEX component identifies the supplied form/catalog or CAS; this chemical source does not support a recipe amount. Locator: Product 50020 heading; separate CAS Number field is 13408-09-8.", "reference": "https://www.sigmaaldrich.com/US/en/product/sigma/50020", "snippet": "β-Glycerol phosphate disodium salt pentahydrate", "supports": "SUPPORT"}, {"explanation": "Identity only for solutions[0].composition[2]. Remove the unsupported primary and MIM identifiers; retain source-specified mass, pentahydrate and CAS. No exact replacement ID is established by this bounded review. The linked UTEX component identifies the supplied form/catalog or CAS; this chemical source does not support a recipe amount. Locator: ChEBI Name; separate formula and registry fields.", "reference": "https://www.ebi.ac.uk/chebi/CHEBI:15978", "snippet": "sn-glycerol 3-phosphate", "supports": "SUPPORT"}], "notes": "Converted from 0.98 g/2 L in the UTEX Enrichment Solution for Seawater Medium recipe. Source CAS 13408-09-8 denotes the disodium beta-glycerophosphate pentahydrate, not sn-glycerol 3-phosphate. No exact replacement ontology identifier is asserted.", "nutritional_roles": ["PHOSPHATE_SOURCE"], "preferred_term": "beta-Glycerol phosphate disodium salt pentahydrate"} | CultureMech:000165 solutions/0/composition/2 {"concentration": {"unit": "G_PER_L", "value": "0.49"}, "evidence": [{"explanation": "Claim: solutions[0].composition[2].concentration. 0.98 g/2 L in this explicitly declared stock volume gives 0.98 g / 2 L = 0.49 g/L. Retain as stock composition, not final-medium concentration. Exact component cell: \"Na 2 glycerophosphate • 5H 2 O (CAS: 13408-09-8)\". Locator: Ingredient table row 2, Amount column; component cell quoted separately. The packaged MIM alias reproduces the wrong sn-glycerol-3-phosphate mapping; do not use it as independent confirmation.", "reference": "https://utex.org/products/enrichment-solution-for-seawater-medium", "snippet": "0.98 g/2 L", "supports": "SUPPORT"}, {"explanation": "Identity only for solutions[0].composition[2]. Remove the unsupported primary and MIM identifiers; retain source-specified mass, pentahydrate and CAS. No exact replacement ID is established by this bounded review. The linked UTEX component identifies the supplied form/catalog or CAS; this chemical source does not support a recipe amount. Locator: Product 50020 heading; separate CAS Number field is 13408-09-8.", "reference": "https://www.sigmaaldrich.com/US/en/product/sigma/50020", "snippet": "β-Glycerol phosphate disodium salt pentahydrate", "supports": "SUPPORT"}, {"explanation": "Identity only for solutions[0].composition[2]. Remove the unsupported primary and MIM identifiers; retain source-specified mass, pentahydrate and CAS. No exact replacement ID is established by this bounded review. The linked UTEX component identifies the supplied form/catalog or CAS; this chemical source does not support a recipe amount. Locator: ChEBI Name; separate formula and registry fields.", "reference": "https://www.ebi.ac.uk/chebi/CHEBI:15978", "snippet": "sn-glycerol 3-phosphate", "supports": "SUPPORT"}], "notes": "Converted from 0.98 g/2 L in the UTEX Enrichment Solution for Seawater Medium recipe. Source CAS 13408-09-8 denotes the disodium beta-glycerophosphate pentahydrate, not sn-glycerol 3-phosphate. No exact replacement ontology identifier is asserted.", "nutritional_roles": ["PHOSPHATE_SOURCE"], "preferred_term": "beta-Glycerol phosphate disodium salt pentahydrate"} | CultureMech:000166 solutions/0/composition/2 {"concentration": {"unit": "G_PER_L", "value": "0.49"}, "evidence": [{"explanation": "Claim: solutions[0].composition[2].concentration. 0.98 g/2 L in this explicitly declared stock volume gives 0.98 g / 2 L = 0.49 g/L. Retain as stock composition, not final-medium concentration. Exact component cell: \"Na 2 glycerophosphate • 5H 2 O (CAS: 13408-09-8)\". Locator: Ingredient table row 2, Amount column; component cell quoted separately. The packaged MIM alias reproduces the wrong sn-glycerol-3-phosphate mapping; do not use it as independent confirmation.", "reference": "https://utex.org/products/enrichment-solution-for-seawater-medium", "snippet": "0.98 g/2 L", "supports": "SUPPORT"}, {"explanation": "Identity only for solutions[0].composition[2]. Remove the unsupported primary and MIM identifiers; retain source-specified mass, pentahydrate and CAS. No exact replacement ID is established by this bounded review. The linked UTEX component identifies the supplied form/catalog or CAS; this chemical source does not support a recipe amount. Locator: Product 50020 heading; separate CAS Number field is 13408-09-8.", "reference": "https://www.sigmaaldrich.com/US/en/product/sigma/50020", "snippet": "β-Glycerol phosphate disodium salt pentahydrate", "supports": "SUPPORT"}, {"explanation": "Identity only for solutions[0].composition[2]. Remove the unsupported primary and MIM identifiers; retain source-specified mass, pentahydrate and CAS. No exact replacement ID is established by this bounded review. The linked UTEX component identifies the supplied form/catalog or CAS; this chemical source does not support a recipe amount. Locator: ChEBI Name; separate formula and registry fields.", "reference": "https://www.ebi.ac.uk/chebi/CHEBI:15978", "snippet": "sn-glycerol 3-phosphate", "supports": "SUPPORT"}], "notes": "Converted from 0.98 g/2 L in the UTEX Enrichment Solution for Seawater Medium recipe. Source CAS 13408-09-8 denotes the disodium beta-glycerophosphate pentahydrate, not sn-glycerol 3-phosphate. No exact replacement ontology identifier is asserted.", "nutritional_roles": ["PHOSPHATE_SOURCE"], "preferred_term": "beta-Glycerol phosphate disodium salt pentahydrate"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-utex-es, sa-merck-35675, sa-chebi-17270, sa-chebi-132089, sa-merck-35675-retry, sa-utex-es-retry, sa-merck35675-web, sa-recipe-b7714041bc413b, sa-recipe-728c009eb4a704, sa-recipe-9a2e045b69386e, sa-recipe-6642eee19a4eda, sa-owner-na2glycerophosphate5h2o

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 3 — NaS2・9H2O

`CM_NAME:0ebb457daee39ac7ed0501894bfd84d71292f3452c3db184cfd0e29bc9a517f3` — unresolved

JCM197 and JCM317 primary tables themselves print NaS2·9H2O. JCM197 preparation instead says Na2S·9H2O and prepares a 5% solution; JCM317 does not resolve that discrepancy. This is direct source contradiction, not permission for a global NaS2-to-Na2S alias.

**Applicability:** CultureMech:008487 solutions/2/composition/0 {"evidence": [{"explanation": "solutions[2].composition[0].concentration: Source batch input: 0.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. This is the contribution specified for the receiving medium batch, not the mass for preparing an unspecified volume of stock. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[0].items[6]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.\n\nAdditional exact excerpt: \"Mix ingredients except NaHCO3, Trace vitamins, Na2S・9H2O and cysteine・HCl・H2O, and autoclave under a N2--CO2 (80:20) atmosphere. Filter--sterilize NaHCO3 as an 8% solution and Trace vitamins while gassing with N2. Separately autoclave Na2S・9H2O and cysteine・HCl・H2O as 5% solutions under a N2 atmosphere. Aseptically and anaerobically add NaHCO3 and Trace vitamins to the medium under a N2--CO2 (80:20) atmosphere. Prior to inoculation, add the sterile Na2S・9H2O and cysteine・HCl・H2O solutions, and adjust pH to 6.8.\"\nsolutions[2].composition[0].notes: The preparation uses the different Na2S spelling; the discrepancy remains unresolved. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=comments[0].comment; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "snippet": "{\n          \"component_name\": \"NaS2・9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\"", "supports": "SUPPORT"}, {"explanation": "solutions[2].composition[0].notes: Unresolved source identity discrepancy: the original JCM197 table spells NaS2, while its preparation spells Na2S. MediaDive normalizes the table to Na2S; TOGO retains NaS2. The existing label/grounding is preserved, not recertified, and no numeric sulfide concentration is asserted. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=original recipe text; accessed=2026-10-08T13:22:48.135690+00:00; capture SHA256=39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532.", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "snippet": "NaS2·9H2O 0.5 g", "supports": "SUPPORT"}], "notes": "Role: Reducing agent; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. This is the contribution specified for the receiving medium batch, not the mass for preparing an unspecified volume of stock.\n\nUnresolved source identity discrepancy: the original JCM197 table spells NaS2, while its preparation spells Na2S. MediaDive normalizes the table to Na2S; TOGO retains NaS2. The existing label/grounding is preserved, not recertified, and no numeric sulfide concentration is asserted.", "preferred_term": "NaS2・9H2O"} | CultureMech:009600 ingredients/6 {"concentration": {"unit": "G_PER_L", "value": "0.3"}, "notes": "Role: Reducing agent; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "NaS2・9H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-0c1e7fd46063, sa-recipe-4bbd24e702b8, sa-recipe-9fc455e18d05b0, sa-recipe-f47970b10af966, sa-togo-M190, sa-togo-M312

**Next requirement:** Obtain a source-author correction or original stock reagent specification reconciling NaS2 versus Na2S independently for JCM197 and JCM317; preserve the 5% stock step.

### 4 — NiCl2-6H2O

`CM_NAME:11c0f762f4802961c56fb41d854f82d4c846d16d56ef9e7f31ded9e71fd66162` — existing_identity_or_alias

JCM1304 Modified trace element mixture explicitly lists NiCl2-6H2O at24mg per litre of STOCK and doses1mL stock per litre medium. ChEBI53542 provides the exact hexahydrate and CAS7791-20-0. Add the punctuation variant only to the active Nickel(II) chloride hexahydrate owner; the rejected formula-named tombstone is not reactivated. Frozen24G_PER_L loses the mg unit and stock nesting.

**Applicability:** CultureMech:007938 ingredients/15 {"concentration": {"unit": "G_PER_L", "value": "24"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "NiCl2-6H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-93465b6b7e03, sa-chebi-53542, sa-recipe-a3e92d8f5b4a6f, sa-togo-M1401, sa-owner-nickel_ii_chloride_hexahydrate, sa-owner-nicl2_x_6_h2o

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 5 — β-Na2glycerophosphate· 5H2O

`CM_NAME:16b7f8d6d0c0a3e6cf83fe51f2687dc2f95d7306e62f7d018dc6a433b756ab4e` — existing_identity_or_alias

TOGO M2368 records beta/disodium/pentahydrate explicitly. Beta identifies the central-position glycerophosphate; no alpha or mixed-isomer identity is inferred. Merck35675 supports the same specific CAS13408-09-8 form. This punctuation variant is suitable for the pentahydrate owner, preserving the separate unspecific-pentahydrate cases in issue1053.

**Applicability:** CultureMech:008952 ingredients/12 {"concentration": {"unit": "G_PER_L", "value": "10"}, "notes": "Role: Mineral source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "β-Na2glycerophosphate· 5H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-togo-M2368, sa-merck-35675, sa-chebi-17270, sa-merck-35675-retry, sa-nies-ma, sa-merck35675-web, sa-recipe-bb89b877b84f50, sa-owner-na2glycerophosphate5h2o

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 6 — Tri-ammonium citrate

`CM_NAME:1a2613d2ed9c6a245073acd890d0507d440c3d861ce6c267bd58898f800f4e1c` — existing_identity_or_alias

Tri-ammonium citrate explicitly supplies the three-ammonium salt, matching CHEBI63037. It is not evidence that the other bare ammonium citrate cases mean this salt. TOGO M2782 records2g as a medium component.

**Applicability:** CultureMech:009331 ingredients/8 {"concentration": {"unit": "G_PER_L", "value": "2"}, "notes": "Role: Nitrogen source; Properties: Organic compound, Simple component, Defined component", "preferred_term": "Tri-ammonium citrate"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-togo-M2782, sa-chebi-63037, sa-recipe-82766d1d3cd573, sa-owner-nh43_citrate

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 7 — CaCl2·2H20

`CM_NAME:1e2506ecaefa9035df3c799cecc689ed8d0535a050dc8e0a427548a369892e90` — malformed_or_nonchemical_token

NBRC966 and its TOGO derivative both print CaCl2·2H20 with digit zero in the terminal group. Calcium chloride dihydrate is a plausible intended identity, but the primary source repeats the malformed token. Preserve this exact label and ask for source correction; do not silently convert it into an unrestricted hydrate alias. The recipe specifies10mg, whereas the frozen normalization records10G_PER_L.

**Applicability:** CultureMech:008319 ingredients/1 {"concentration": {"unit": "G_PER_L", "value": "10"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "CaCl2·2H20"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-5822a9e091f7, sa-togo-M1755, sa-chebi-86158, sa-recipe-c93db00b74c9ca, sa-owner-cacl2_x_2_h2o

**Next requirement:** Obtain NBRC966 clarification that H20 means H2O, and repair the10mg source dose and stock context in CultureMech.

### 8 — CoCl2-6H2O

`CM_NAME:2dc433b978bd09e7a5b337175547a59fb5bfa281f977b3730b8def8ca4ef6e16` — existing_identity_or_alias

JCM1304 explicitly identifies CoCl2-6H2O in the Modified trace element STOCK at190mg/L, not190g/L final medium. CHEBI53503 and CAS7791-13-1 verify the six-water substance. The active owner is Cobalt_chloride_hexahydrate; its current water(1/7) alias is a separate unresolved full-payload conflict and must not be blessed by this new raw alias.

**Applicability:** CultureMech:007938 ingredients/14 {"concentration": {"unit": "G_PER_L", "value": "190"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "CoCl2-6H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-93465b6b7e03, sa-chebi-53503, sa-recipe-a3e92d8f5b4a6f, sa-togo-M1401, sa-owner-cobalt_chloride_hexahydrate, sa-owner-cocl2_x_6_h2o

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 9 — PbCl2

`CM_NAME:33aeeadd45b5ef0bd8a7097c1eae417ed05c3f934b1256934f4c66413534f7b6` — existing_identity_or_alias

RS NNM preserves PbCl2 as the nested solute of a separately represented1mg/mL stock. PbCl2 has two chlorides and lead(II), matching CHEBI88212. The chemical synonym applies to that nested ingredient only; the stock and its volume addition remain independent recipe assertions.

**Applicability:** CultureMech:010434 solutions/20/composition/0 {"concentration": {"unit": "G_PER_L", "value": "1"}, "evidence": [{"explanation": "ingredients[29].concentration -> solutions[20].composition[0].concentration: Restore the stock stage: 1 mg / 1 ml = 1 g/L stock. Source addition 0.0200 μl/l = 0.00002 ml/L. The previous final contribution 0.00000002 g/L matches 1 * 0.00002 / 1000; it was not a wrong numeric value but must not remain a duplicate direct ingredient. Exact excerpt: \"PbCl2 (Stock solution 1mg/mL. Heavy metal. Store in the dark) 0.0200 μl/l - -\"; locator=sol-0 / recipe-30; table headings=['Compound', 'Amount', 'Unit', 'Conc. [g/L]', 'Conc. [mM]']. Exact excerpt: \"prepare stock solutions in H2O at the specified concentration\"; locator=sol-0 preparation step 2. Exact excerpt: \"Fill to a total volume of 1 liter with purified H2O.\"; locator=sol-0 preparation step 4. User-contributed MediaDive P4 page, accessed 2026-10-07; source_type=user_contributed_dataset_page; page_sha256=c1b66217611ac37036f1550d0c3ade9bb6b4a9ef733f0547494547e574668a4b; figure_sha256=245e477ae6e3c0f514270e7e62fc4c000110c022ae18c153c7ec8ceb9f03e4a2. Numeric evidence is the page text, not OCR of the inspected diagram. No journal validation or growth claim is implied.", "reference": "https://mediadive.dsmz.de/medium/P4", "snippet": "PbCl2 (Stock solution 1mg/mL. Heavy metal. Store in the dark) 0.0200 μl/l - -", "supports": "SUPPORT"}], "notes": "Restore the stock stage: 1 mg / 1 ml = 1 g/L stock. Source addition 0.0200 μl/l = 0.00002 ml/L. The previous final contribution 0.00000002 g/L matches 1 * 0.00002 / 1000; it was not a wrong numeric value but must not remain a duplicate direct ingredient.", "preferred_term": "PbCl2", "source": "MediaDive public Medium P4"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-chebi-88212, sa-recipe-72eb9df03ffb19, sa-owner-lead_ii_chloride

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 10 — Ammonium tartrate

`CM_NAME:37f2016e53937478077c0f71f107c670abe38933a51105ff1170559fe7648010` — unresolved

NBRC887 and TOGO M1682 say only ammonium tartrate. Neither ammonium:tartrate ratio nor tartrate stereochemistry is given. The nearby CHEBI63075 owner is diammonium L-tartrate, which adds both unsupported stoichiometry and stereochemistry.

**Applicability:** CultureMech:008241 ingredients/2 {"concentration": {"unit": "G_PER_L", "value": "0.2"}, "notes": "Role: Nitrogen source; Properties: Simple component, Organic compound, Defined component", "preferred_term": "Ammonium tartrate"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-210d6f521436, sa-togo-M1682, sa-chebi-63075, sa-recipe-ad0de432829f21, sa-owner-diammonium_tartrate

**Next requirement:** A reagent CAS/catalogue or source clarification for NBRC887 establishing ammonium stoichiometry and tartrate stereochemistry.

### 11 — Ammonium Citrate

`CM_NAME:3cbb11d1aeb3f36b22268594f37e9078402bc4ad3e886fbc93f083da408d332f` — unresolved

Both frozen ATCC416 scratch formulations use generic Ammonium Citrate. The solid recipe adds agar but does not establish whether citrate is di- or tri-ammonium. ChEBI63076 and63037 are distinct salt ratios; medium-name convention cannot select one.

**Applicability:** CultureMech:008839 ingredients/5 {"concentration": {"unit": "G_PER_L", "value": "2.0"}, "notes": "ATCC Medium 416 lists 2 g/L Ammonium Citrate in the Lactobacilli MRS Broth scratch formula; this generic name is retained without choosing a specific ammonium citrate salt.", "preferred_term": "Ammonium Citrate", "source": "TOGO M2250 / ATCC Medium 416"} | CultureMech:008837 ingredients/5 {"concentration": {"unit": "G_PER_L", "value": "2.0"}, "notes": "ATCC Medium 416 lists 2 g/L Ammonium Citrate in the Lactobacilli MRS Broth scratch formula; this generic name is retained without choosing a specific ammonium citrate salt.", "preferred_term": "Ammonium Citrate", "source": "TOGO M2249 / ATCC Medium 416"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-atcc-416, sa-chebi-63076, sa-chebi-63037, sa-recipe-33fb2f99dce2be, sa-recipe-f7be3059bb89bc, sa-owner-nh42_citrate, sa-owner-nh43_citrate

**Next requirement:** ATCC416 reagent specification or corrected formula identifying the ammonium:citrate ratio; then apply separately to the broth and agar occurrences.

### 12 — CaCl2 (100 mM)

`CM_NAME:3e7f4518c07b3583e3929053d27719746832f11478589c7a5a464d0d10d54a1d` — stock_product_mixture_context

NBRC1160 specifies20mL of100mM calcium chloride; the frozen20G_PER_L does not express that addition. The label denotes a stock solution. Identifying a calcium-chloride component does not authorize collapse of the100mM preparation into a solid-salt alias.

**Applicability:** CultureMech:008478 ingredients/0 {"concentration": {"unit": "G_PER_L", "value": "20"}, "notes": "Role: Mineral source; Properties: Defined component, Inorganic compound, Solution", "preferred_term": "CaCl2 (100 mM)"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-070a3a93ee5e, sa-togo-M1901, sa-chebi-3312, sa-recipe-ec0da9d2c945d7, sa-togo-M190, sa-owner-cacl2

**Next requirement:** Represent NBRC1160 stock strength, carrier and20mL dose in the recipe; recover preparation/supplied salt if a reusable stock owner is needed.

### 13 — TiCl2

`CM_NAME:4a86709a44261f62c05fd80520ed7d7d057d0cea20719ae8fc0f41807916b2b6` — unresolved

ATCC1925 original formulation is internally contradictory: the added stock is headed Titanium(III) citrate, neutralized, but the stock recipe explicitly prints TiCl2 at0.75g with2.58g trisodium citrate in50mL. Titanium(II) chloride and titanium(III) chloride have different oxidation states. The source preparation cannot be assigned to either by silently choosing the heading or formula.

**Applicability:** CultureMech:009244 ingredients/14 {"concentration": {"unit": "G_PER_L", "value": "0.75"}, "notes": "Properties: Defined component, Simple component, Inorganic compound", "preferred_term": "TiCl2"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-ticl2-atcc, sa-togo-M2692, sa-recipe-56c31850d0a7ae

**Next requirement:** ATCC1925 source-author correction or original reagent catalogue reconciling Titanium(III) citrate heading versus TiCl2 precursor, retaining the50mL stock preparation and1mL/L dose.

### 14 — MnCl2 x 6H2O

`CM_NAME:4b524ea6e88ead41d9c6e4014ca2ac6b170cd1ffbca01fdeb04e82ba8c8c18fb` — unresolved

The Ethane-C source context specifies MnCl2 x6H2O in a metal mixture at4.55mg/L. The retrieved JCM1120 page has no recipe; MediaDive2003 preserves the six-water label without CAS/formula. This supports the recorded claim but does not establish a purchasable exact hydrate or justify replacing it by tetrahydrate. A separately retrieved official JCM1118 HTML capture succeeds and explicitly prints MnCl2·6H2O at4.55mg per litre of metal stock, added1mL/L. This establishes the source claim and stock boundary, but supplies no reagent CAS and does not resolve whether the six-water label is correct. Earlier empty HTTP200 JCM captures are retained as unsuccessful attempts, superseded only for recipe availability.

**Applicability:** CultureMech:007723 solutions/1/composition/3 {"concentration": {"unit": "MG_PER_L", "value": "4.55"}, "notes": "JCM Medium 1120 / MediaDive J1120 lists 4.55 mg/L MnCl2 x 6H2O.", "preferred_term": "MnCl2 x 6H2O", "source": "JCM Medium 1120 / MediaDive J1120"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-7084e7a0008b, sa-mediadive-2003, sa-ols-mn-hexahydrate, sa-jcm1118-shared, sa-jcm1119-retry, sa-jcm1120-retry, sa-recipe-ec2bfe98ebe33d

**Next requirement:** Original JCM1120 metal-mixture reagent identity, or supplier/CAS evidence tied to its six-water manganese chloride; resolve rather than silently normalize the hydration count.

### 15 — Na-glycerol phosphate

`CM_NAME:4c6fff23a48ccf39cb39a2d9c8469adbb8b285dadc2751a054c93b963a905a21` — unresolved

Na-glycerol phosphate in the two DSMZ608 contexts does not state phosphate position, sodium ratio or hydration. MediaDive604 retains a generic source ingredient. Specific disodium beta and pentahydrate owners would add unprovided identity; the NCIT generic sodium glycerophosphate mixture is considered separately but does not prove the supplied DSMZ grade.

**Applicability:** CultureMech:010797 composition/7 {"concentration": {"unit": "G_PER_L", "value": "23.5"}, "evidence": [{"explanation": "Concentration evidence for composition[7].concentration (Na-glycerol phosphate) in MediaDive solution 1307; locator=$.data.recipe[7] (compound_id=604). Provider explicitly reports g_l=23.5. Arithmetic check: 23.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 23.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 1000. Retrieved 2026-10-07T08:51:19.049494+00:00; response SHA256=8ba6bb33421bfa538ca8b579f367ff979e689ef21666f2c36e4ad31ca0e3bcaf.", "reference": "https://mediadive.dsmz.de/rest/solution/1307", "snippet": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Na-glycerol phosphate\",\n                \"compound_id\": 604,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 23.5,\n                \"unit\": \"g\",\n                \"g_l\": 23.5,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "supports": "SUPPORT"}], "preferred_term": "Na-glycerol phosphate", "term": {"id": "mediadive.compound:604", "label": "Na-glycerol phosphate"}} | CultureMech:015365 ingredients/7 {"concentration": {"unit": "G_PER_L", "value": "23.5"}, "evidence": [{"explanation": "Concentration evidence for ingredients[7].concentration (Na-glycerol phosphate) in MediaDive medium 608; locator=$.data.solutions[0].recipe[7]. Provider explicitly reports g_l=23.5; check: 23.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 23.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:21.231867+00:00; response SHA256=e3643cf3455361cdf1c194697c325ff06b1e373f6b150c11bcb91848bb9d11c0.", "reference": "https://mediadive.dsmz.de/rest/medium/608", "snippet": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na-glycerol phosphate\",\n                        \"compound_id\": 604,\n                        \"amount\": 23.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 23.5,\n                        \"optional\": 0\n                    }", "supports": "SUPPORT"}], "preferred_term": "Na-glycerol phosphate"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-86ee5d6b1588, sa-mediadive-604, sa-ncit-C120561, sa-chebi-132089, sa-recipe-e629642e55f683, sa-recipe-54cf52a3141b8d, sa-owner-sodium_glycerophosphate, sa-owner-sodium_beta-glycerophosphate, sa-owner-na2glycerophosphate5h2o

**Next requirement:** Original DSMZ608 reagent catalogue/CAS or explicit composition establishing isomer mixture or positional isomer, salt ratio and hydration.

### 16 — Fe(III) ammonium citrate

`CM_NAME:4e834342ffd256476ce499957d900c5168dbed13a7a1d330943c1e4385f4af43` — existing_identity_or_alias

The three NBRC1049/1050 occurrences explicitly state Fe(III) ammonium citrate. CHEBI31604 describes ferric ammonium citrate as a mixture of indefinite composition. The word order is an alias for that material scope, not a stoichiometric molecular formula or a claim about red/green grade.

**Applicability:** CultureMech:007452 ingredients/11 {"concentration": {"unit": "G_PER_L", "value": "0.01"}, "preferred_term": "Fe(III) ammonium citrate"} | CultureMech:008389 ingredients/13 {"concentration": {"unit": "G_PER_L", "value": "0.01"}, "notes": "Role: Nitrogen source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "Fe(III) ammonium citrate"} | CultureMech:008388 ingredients/14 {"concentration": {"unit": "G_PER_L", "value": "0.01"}, "notes": "Role: Nitrogen source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "Fe(III) ammonium citrate"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-1962216682cc, sa-recipe-f92e3cf55090, sa-chebi-31604, sa-recipe-4d03075e31f542, sa-recipe-ed72135a7f5480, sa-recipe-35217cf958929b, sa-togo-M1818, sa-togo-M1817, sa-owner-ferric_ammonium_citrate

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 17 — Amonium phosphate-dibasic

`CM_NAME:50c53f0367cee7787a3ae1417367cee69f22c72037c7eea0bb7daab2cf8641f8` — existing_identity_or_alias

NBRC1398 spells Amonium phosphate-dibasic; dibasic ammonium phosphate names two ammonium cations per hydrogen phosphate, matching CHEBI63051. The missing m is a word spelling error without competing stoichiometry. Preserve the raw source spelling and do not change dose claims.

**Applicability:** CultureMech:008678 ingredients/4 {"concentration": {"unit": "G_PER_L", "value": "0.25"}, "notes": "Role: Nitrogen source; Properties: Simple component, Inorganic compound, Defined component", "preferred_term": "Amonium phosphate-dibasic"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-b284157ef4cb, sa-chebi-63051, sa-recipe-1207987fcc0f26, sa-togo-M2088, sa-owner-nh42hpo4

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 18 — MgCl2 x 6 H2O (200.0 g/l)

`CM_NAME:5186a837fc13f65b72eb03fa8c0082571b329faffd68f0c1489b87cee5e7eeed` — stock_product_mixture_context

DSMZ925 defines a200.0g/L magnesium chloride hexahydrate stock. The parenthesized strength is material context and cannot become a synonym of pure MgCl2 or pure hexahydrate. The stock addition and formulation remain source recipe assertions.

**Applicability:** CultureMech:009037 ingredients/15 {"concentration": {"unit": "G_PER_L", "value": "1"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "MgCl2 x 6 H2O (200.0 g/l)"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-b243b8aefc2d, sa-chebi-6636, sa-recipe-4f9ad47f62c919, sa-togo-M2459

**Next requirement:** Separate the200g/L stock and its addition volume in the recipe, including carrier and preparation if a stock owner is proposed.

### 19 — Diammonium hydrogencitrate

`CM_NAME:5ad4d015ca55c7f44e6cabd3ba25c775afbc2bb06500f75dd236f16f4364e7e3` — existing_identity_or_alias

All four NBRC355/366/820 occurrences explicitly use diammonium hydrogencitrate. Two ammoniums plus the remaining acidic hydrogen match CHEBI63076 and CAS3012-65-5; the concatenated hydrogencitrate spelling does not imply triammonium citrate.

**Applicability:** CultureMech:007490 ingredients/7 {"concentration": {"unit": "G_PER_L", "value": "2"}, "preferred_term": "Diammonium hydrogencitrate"} | CultureMech:008175 ingredients/5 {"concentration": {"unit": "G_PER_L", "value": "3.5"}, "mediaingredientmech_term": {"id": "MediaIngredientMech:000400", "label": "Diammonium hydrogencitrate"}, "notes": "Role: Nutrient source; Properties: Organic compound, Simple component, Defined component", "preferred_term": "Diammonium hydrogencitrate"} | CultureMech:015901 ingredients/5 {"concentration": {"unit": "G_PER_L", "value": "2"}, "preferred_term": "Diammonium hydrogencitrate"} | CultureMech:008113 ingredients/7 {"concentration": {"unit": "G_PER_L", "value": "2"}, "mediaingredientmech_term": {"id": "MediaIngredientMech:000400", "label": "Diammonium hydrogencitrate"}, "notes": "Role: Nutrient source; Properties: Defined component, Organic compound, Simple component", "preferred_term": "Diammonium hydrogencitrate"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-26feba90a898, sa-recipe-65105976aace, sa-recipe-25ba45ec76b0, sa-chebi-63076, sa-recipe-c2907356863a73, sa-recipe-6d92be2e3f3eba, sa-recipe-8595994e450c30, sa-recipe-8119d63cbe890e, sa-togo-M1620, sa-togo-M1564, sa-owner-nh42_citrate

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 20 — 0.4% CaCl2・2H2O

`CM_NAME:6131e3f66e8c31e81d15dff2eeae38d2eb6686708b248626597107a8762c7a2a` — stock_product_mixture_context

JCM665 lists0.4% CaCl2·2H2O as a separately added preparation. Dihydrate identity is explicit, but the percentage-qualified solution is not the solid. Retain the solution and preparation context rather than importing an unrestricted pure-hydrate synonym.

**Applicability:** CultureMech:010088 ingredients/10 {"concentration": {"unit": "G_PER_L", "value": "0.1"}, "notes": "Role: Mineral source; Properties: Defined component, Inorganic compound, Solution", "preferred_term": "0.4% CaCl2・2H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-06c82845cf85, sa-chebi-86158, sa-recipe-18c91ad240b3f9, sa-togo-M683, sa-owner-cacl2_x_2_h2o

**Next requirement:** Recover the percentage basis and stock preparation/dose for JCM665 and model the calcium chloride dihydrate as the stock component.

### 21 — SrCl2・H2O

`CM_NAME:63d3d4ae7341d502f8b41620560d0a7ec11f16d69ea3e288622c6da08d7ade83` — broad_parent_relation_only

JCM369 and508 explicitly list SrCl2·H2O. PubChem returns a monohydrate structure, so the label is not dismissed as chemically impossible. The available evidence does not establish a source-specific orderable CAS/ontology form; strontium chloride anhydrous and hexahydrate cannot substitute.

**Applicability:** CultureMech:009744 ingredients/19 {"concentration": {"unit": "G_PER_L", "value": "0.01"}, "notes": "Role: Mineral source; Properties: Defined component, Simple component", "preferred_term": "SrCl2・H2O"} | CultureMech:009899 ingredients/23 {"concentration": {"unit": "G_PER_L", "value": "0.01"}, "notes": "Role: Mineral source; Properties: Defined component, Simple component", "preferred_term": "SrCl2・H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-55c33e835e2d, sa-recipe-24208a22d896, sa-pubchem-sr-monohydrate, sa-ols-sr-monohydrate, sa-recipe-db7d81e66eec5b, sa-recipe-194e188c7eaac2, sa-togo-M363, sa-togo-M509

**Next requirement:** A monohydrate supplier/registry identifier tied to the JCM reagent, or original source correction; retain only non-exact parent context meanwhile.

### 22 — Ammonium citrate

`CM_NAME:712de2de2b575e9b000356c7112e53e3133cde8fe2751cfdcd8ddcce19929082` — unresolved

The seven occurrences span TOGO and MediaDB recipes and preserve bare ammonium citrate. None of their frozen source annotations specifies di- versus tri-ammonium. Shared MRS-like medium context is insufficient to apply one salt ratio to all seven independent recipe claims.

**Applicability:** CultureMech:008827 ingredients/14 {"concentration": {"unit": "G_PER_L", "value": "0.6"}, "notes": "Role: Nitrogen source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "Ammonium citrate"} | CultureMech:007092 ingredients/40 {"concentration": {"unit": "MILLIMOLAR", "value": "2.65269"}, "preferred_term": "Ammonium citrate"} | CultureMech:007222 ingredients/32 {"concentration": {"unit": "MILLIMOLAR", "value": "28.69"}, "preferred_term": "Ammonium citrate"} | CultureMech:007307 ingredients/11 {"concentration": {"unit": "MILLIMOLAR", "value": "2.467"}, "preferred_term": "Ammonium citrate"} | CultureMech:007297 ingredients/6 {"concentration": {"unit": "MILLIMOLAR", "value": "28.69"}, "preferred_term": "Ammonium citrate"} | CultureMech:007296 ingredients/6 {"concentration": {"unit": "MILLIMOLAR", "value": "28.69"}, "preferred_term": "Ammonium citrate"} | CultureMech:007202 ingredients/22 {"concentration": {"unit": "MILLIMOLAR", "value": "2.65269"}, "preferred_term": "Ammonium citrate"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-togo-M2239, sa-chebi-63076, sa-chebi-63037, sa-recipe-4b8c414e2be273, sa-recipe-6e5a687980d83e, sa-recipe-9fe45a2738b15c, sa-recipe-aed8ca1f85dfa1, sa-recipe-276bd81ddf3611, sa-recipe-0e631d399dbd47, sa-recipe-9ca2ad108a36af, sa-owner-nh42_citrate, sa-owner-nh43_citrate

**Next requirement:** Per-source primary recipe/catalogue evidence for ammonium:citrate stoichiometry in every cited MediaDB/TOGO occurrence; split interpretations if they differ.

### 23 — MoO

`CM_NAME:75d52d9f7d5b45ad6946c61474cb1f4c0e640d76c41680ab8fc544b6ca555b43` — malformed_or_nonchemical_token

The CCAP BB original explicitly lists MoO3 at0.71g/L in trace-element stock7 and adds1mL of that stock per litre. The frozen token MoO loses the subscript3 and places0.71G_PER_L at root. This is a source transcription and stock-boundary defect. A global MoO synonym would hide both defects.

**Applicability:** CultureMech:000053 ingredients/2 {"concentration": {"unit": "G_PER_L", "value": "0.71"}, "notes": "Ontology mapping not yet available; From CCAP Medium MR_BB.pdf; Curated from CCAP Medium MR_BB.pdf specification", "preferred_term": "MoO", "source": "CCAP Medium MR_BB.pdf"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-0d78f07fa21b, sa-ccap-bb, sa-recipe-99f94fdaf3d6d7

**Next requirement:** Correct the CCAP BB source component to MoO3 within trace stock7, retaining the1mL/L stock dose and source provenance before rerunning mapping.

### 24 — Na-glycerophosphate

`CM_NAME:7d55b59067133c3d1b5d88bb0a92e715068bd4c680ce9c4d8a72f150733c8823` — unresolved

The NBRC1183 and DSMZ357 sources specify Na-glycerophosphate without positional isomer, salt ratio or hydrate. The three occurrences include a trace-element stock context, which must be retained. Neither beta-pentahydrate nor a particular glycerophosphate mixture can be inferred from this abbreviation.

**Applicability:** CultureMech:007462 ingredients/1 {"concentration": {"unit": "G_PER_L", "value": "0.1"}, "preferred_term": "Na-glycerophosphate"} | CultureMech:009158 ingredients/7 {"concentration": {"unit": "G_PER_L", "value": "0.1"}, "notes": "Role: Mineral source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "Na-glycerophosphate"} | CultureMech:008497 ingredients/3 {"concentration": {"unit": "G_PER_L", "value": "0.1"}, "notes": "Role: Mineral source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "Na-glycerophosphate"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-5939a819cce9, sa-recipe-19093134ac94, sa-ncit-C120561, sa-chebi-132089, sa-recipe-4709ca10c6bdd4, sa-recipe-e82ad4a147456a, sa-recipe-75368455d4cb68, sa-togo-M2591, sa-togo-M1919, sa-owner-sodium_glycerophosphate, sa-owner-sodium_beta-glycerophosphate, sa-owner-na2glycerophosphate5h2o

**Next requirement:** NBRC1183 and DSMZ357 reagent identity/composition, including isomer, sodium stoichiometry and hydration; do not propagate one source choice to the other.

### 25 — 130 mM FeCl2

`CM_NAME:807c4f43db33f78e8fb227f45085a77de5dbe9c1c14a23f4150861b79096b95b` — stock_product_mixture_context

JCM665 calls for130mM FeCl2 as a stock preparation. The molarity specifies dissolved iron chloride concentration, not a particular hydrated solid used to make it; a pure FeCl2 alias would erase preparation scope.

**Applicability:** CultureMech:010088 ingredients/12 {"concentration": {"unit": "G_PER_L", "value": "0.1"}, "notes": "Role: Mineral source; Properties: Defined component, Solution, Inorganic compound", "preferred_term": "130 mM FeCl2"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-06c82845cf85, sa-chebi-30812, sa-recipe-18c91ad240b3f9, sa-togo-M683

**Next requirement:** Recover stock carrier and preparation, preserve the130mM concentration and addition volume, and identify any specified starting hydrate separately.

### 26 — FeCl2·2H2O

`CM_NAME:81014f441fc6c9f61a5fc3f1af6aa9bbf513f24ce47f0bd641d9183e0b6f106d` — new_distinct_ingredient_proposal

NBRC1326 explicitly lists FeCl2·2H2O at10mg in its main recipe. OECD SIDS describes iron dichloride dihydrate crystals and lists CAS16399-77-2; PubChem CID168436557 records Cl2FeH4O2. Bounded ChEBI name/CAS searches returned no term, and a gitignore-independent maintained-owner search found no dihydrate owner. Propose a distinct CAS identity and asymmetric parent mapping to iron dichloride; never equate it to anhydrous or tetrahydrate. The frozen10G_PER_L unit is separately wrong.

**Applicability:** CultureMech:008622 ingredients/8 {"concentration": {"unit": "G_PER_L", "value": "10"}, "notes": "Role: Mineral source", "preferred_term": "FeCl2·2H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-04a18945016c, sa-oecd-iron, sa-pubchem-fe-dihydrate, sa-ols-fe-dihydrate, sa-ols-fe-dihydrate-cas, sa-chebi-30812, sa-supplier-fe-page, sa-recipe-78a26182e1b5b2, sa-togo-M2033

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 27 — CaCO3 (reagent grade)

`CM_NAME:82bec32eb2b673ed06681a63fc9d97056944082cf9d9820a91989fe62f0b49bd` — existing_identity_or_alias

NBRC319 specifies calcium carbonate reagent grade. The grade is procurement detail on the same CaCO3 substance, matching CHEBI3311; retain the exact grade-bearing label as a sourced alias without inventing purity percentage or a polymorph.

**Applicability:** CultureMech:008078 ingredients/2 {"concentration": {"unit": "G_PER_L", "value": "1"}, "notes": "Role: Protective agent, Mineral source; Properties: Defined component, Simple component, Inorganic compound", "preferred_term": "CaCO3 (reagent grade)"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-ef563061bcd3, sa-chebi-3311, sa-recipe-2122768fb21e75, sa-togo-M1531, sa-owner-caco3

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 28 — CuCl2⋅4H2O

`CM_NAME:838860c9ad4afce04ccdb97264977f4b9272cc0bf3f18d278727ee462e1b8014` — unresolved

NBRC1507 itself specifies CuCl2·4H2O in a trace-element stock at0.025g/L. It also contains other unusual hydrate labels, but neither that pattern nor the common dihydrate establishes a correction. Bounded ontology search did not resolve the exact four-water form.

**Applicability:** CultureMech:008747 ingredients/24 {"concentration": {"unit": "G_PER_L", "value": "0.025"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Simple component, Complex component", "preferred_term": "CuCl2⋅4H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-74b89743eed1, sa-ols-cu-tetrahydrate, sa-chebi-49553, sa-recipe-57d6dac8e517e9, sa-togo-M2152

**Next requirement:** NBRC1507 source-author or reagent-catalogue evidence identifying the four-water copper chloride, or an explicit corrected hydration count; preserve nested trace-stock context.

### 29 — MnCl2 x 6 H2O

`CM_NAME:8a74260086570a129b6c2deed91212baad0827b513e03d538d1d7c1f3a1da434` — unresolved

All four occurrences name manganese chloride hexahydrate in the JCM1118/1119/1120 metal-mixture lineage, including MediaDive solution context. Current JCM pages return no recipe and MediaDive2003 offers no CAS/formula. Repetition across imports is one source lineage, not independent confirmation of an exact six-water product. A separately retrieved official JCM1118 HTML capture succeeds and explicitly prints MnCl2·6H2O at4.55mg per litre of metal stock, added1mL/L. This establishes the source claim and stock boundary, but supplies no reagent CAS and does not resolve whether the six-water label is correct. Earlier empty HTTP200 JCM captures are retained as unsuccessful attempts, superseded only for recipe availability.

**Applicability:** CultureMech:002294 ingredients/9 {"concentration": {"unit": "G_PER_L", "value": "0.00455"}, "preferred_term": "MnCl2 x 6 H2O"} | CultureMech:014120 composition/3 {"concentration": {"unit": "G_PER_L", "value": "0.00455"}, "evidence": [{"explanation": "Concentration evidence for composition[3].concentration (MnCl2 x 6 H2O) in MediaDive solution 5210; locator=$.data.recipe[3] (compound_id=2003). Provider explicitly reports g_l=0.00455. Arithmetic check: 4.55 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.00455 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 1000. Retrieved 2026-10-07T09:52:13.462520+00:00; response SHA256=868b14a66e4cb0bbef911dd7f864c843ddd873086e8b6c60f2e85ea6c2672f7c.", "reference": "https://mediadive.dsmz.de/rest/solution/5210", "snippet": "{\n                \"recipe_order\": 4,\n                \"compound\": \"MnCl2 x 6 H2O\",\n                \"compound_id\": 2003,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4.55,\n                \"unit\": \"mg\",\n                \"g_l\": 0.00455,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "supports": "SUPPORT"}], "preferred_term": "MnCl2 x 6 H2O", "term": {"id": "mediadive.compound:2003", "label": "MnCl2 x 6 H2O"}} | CultureMech:002291 ingredients/12 {"concentration": {"unit": "G_PER_L", "value": "0.00455"}, "preferred_term": "MnCl2 x 6 H2O"} | CultureMech:002292 ingredients/10 {"concentration": {"unit": "G_PER_L", "value": "0.00455"}, "preferred_term": "MnCl2 x 6 H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-82ea031bb124, sa-recipe-5f1a1396d2bc, sa-recipe-7084e7a0008b, sa-mediadive-2003, sa-ols-mn-hexahydrate, sa-jcm1118-shared, sa-jcm1119-retry, sa-jcm1120-retry, sa-recipe-bc03cda75be48a, sa-recipe-7871d34644795e, sa-recipe-c31627b5a2b510, sa-recipe-67fe9cc15d8776

**Next requirement:** Recover original JCM metal-mixture documents or source supplier identity for MnCl2·6H2O; reconcile hydration and4.55mg/L STOCK dosage before publication.

### 30 — beta-Na2glycerophosphate·5H2O

`CM_NAME:93eca46c5d13fcece967587a265c49000dd65448d8b5a2d1feb7711d276265b4` — existing_identity_or_alias

NBRC966 explicitly gives beta-Na2glycerophosphate·5H2O at4mg. The beta position, disodium stoichiometry and five waters match CAS13408-09-8; the label is not the unqualified pentahydrate ambiguity in1053. Frozen4G_PER_L also needs unit repair.

**Applicability:** CultureMech:008319 ingredients/8 {"concentration": {"unit": "G_PER_L", "value": "4"}, "notes": "Role: Mineral source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "beta-Na2glycerophosphate·5H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-5822a9e091f7, sa-merck-35675, sa-chebi-17270, sa-merck-35675-retry, sa-merck35675-web, sa-recipe-c93db00b74c9ca, sa-togo-M1755, sa-owner-na2glycerophosphate5h2o

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 31 — MnCl2・6H2O

`CM_NAME:96e876d0a4cf3c69ad97395b20acd748c363b279d41e0206197606eb98b7b1c3` — unresolved

TOGO M1196 reproduces JCM1118 manganese chloride six-water metal-mixture text. The frozen4.55G_PER_L and cross-source4.55mg/L stock values require unit review; neither resolves the hydrate. Current JCM1118 provides no recipe, and MediaDive2003 lacks exact identifiers. A separately retrieved official JCM1118 HTML capture succeeds and explicitly prints MnCl2·6H2O at4.55mg per litre of metal stock, added1mL/L. This establishes the source claim and stock boundary, but supplies no reagent CAS and does not resolve whether the six-water label is correct. Earlier empty HTTP200 JCM captures are retained as unsuccessful attempts, superseded only for recipe availability.

**Applicability:** CultureMech:007722 ingredients/16 {"concentration": {"unit": "G_PER_L", "value": "4.55"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "MnCl2・6H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-82ea031bb124, sa-mediadive-2003, sa-ols-mn-hexahydrate, sa-jcm1118-shared, sa-jcm1119-retry, sa-jcm1120-retry, sa-recipe-4b5dc539516ea7, sa-togo-M1196

**Next requirement:** Original JCM1118 metal-mixture page or catalogue confirming hydration and4.55mg stock quantity; preserve this punctuation-specific source label.

### 32 — MgCl2 x 4 H2O

`CM_NAME:a262c8026d2e49e66661614678c8f644aa13f8e7d0ab5b6d90ab578da8cc855d` — unresolved

DSMZ976 explicitly prints MgCl2 x4H2O at5mg/L trace stock, and PubChem establishes a tetrahydrate structure. However the linked MediaDive871 metadata uses anhydrous95.2104g/mol. These are contradictory source fields. Do not replace the explicit four-water form by anhydrous/hexahydrate or adopt the malformed mass calculation as proof.

**Applicability:** CultureMech:006934 ingredients/8 {"concentration": {"unit": "G_PER_L", "value": "0.005"}, "preferred_term": "MgCl2 x 4 H2O"} | CultureMech:011407 composition/2 {"concentration": {"unit": "G_PER_L", "value": "0.005"}, "evidence": [{"explanation": "Concentration evidence for composition[2].concentration (MgCl2 x 4 H2O) in MediaDive solution 2002; locator=$.data.recipe[2] (compound_id=871). Provider explicitly reports g_l=0.005. Arithmetic check: 5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.005 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 1000. Retrieved 2026-10-07T08:58:37.635639+00:00; response SHA256=1e29abadb0d1692011281457837b6b0131c117ef71591233bdd435d2905b7d37.", "reference": "https://mediadive.dsmz.de/rest/solution/2002", "snippet": "{\n                \"recipe_order\": 3,\n                \"compound\": \"MgCl2 x 4 H2O\",\n                \"compound_id\": 871,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.005,\n                \"mmol_l\": 0.0525153,\n                \"optional\": 0\n            }", "supports": "SUPPORT"}], "preferred_term": "MgCl2 x 4 H2O", "term": {"id": "mediadive.compound:871", "label": "MgCl2 x 4 H2O"}} | CultureMech:002158 ingredients/8 {"concentration": {"unit": "G_PER_L", "value": "0.005"}, "preferred_term": "MgCl2 x 4 H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-2b1e0672d2fb, sa-pubchem-mg-tetrahydrate, sa-mediadive-871, sa-ols-mg-tetrahydrate, sa-recipe-4c94e9eca29968, sa-recipe-4b89ee27087f16, sa-recipe-2f554e30e13926

**Next requirement:** Source-author reconciliation of DSMZ976 tetrahydrate reagent with MediaDive871 anhydrous mass, plus a supplier/registry identity tied to the exact product.

### 33 — Spermine phosphate

`CM_NAME:a6d79182fedf6107d5a24adb5281644de61a97deb178c04acb1fe800767f8c39` — unresolved

The MediaDB recipe tied to PMID14325885 says Spermine phosphate at0.1004mM. A supplier supports diphosphate hexahydrate as one purchasable product, but the bare source label does not state phosphate stoichiometry or hydration. It cannot be treated as free spermine or automatically as that supplier product.

**Applicability:** CultureMech:007212 ingredients/12 {"concentration": {"unit": "MILLIMOLAR", "value": "0.1004"}, "preferred_term": "Spermine phosphate"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-pubmed-spermine, sa-spermine-scbt, sa-spermine-scbt-web, sa-recipe-48262c9af0348c

**Next requirement:** Read the original PMID14325885 methods/reagent specification or catalogue to establish phosphate ratio and hydration for this exact MediaDB occurrence.

### 34 — Na2-ß-glycerophosphate x 5 H2O

`CM_NAME:ab9556be29577d30d742defe6231500fdfe424cf471d9335852044be001e2d25` — existing_identity_or_alias

The DSMZ122 and KOMODO122 occurrences explicitly name disodium beta-glycerophosphate pentahydrate. MediaDive230 in this lineage specifies Merck35675, CAS13408-09-8 and306.11g/mol, agreeing with the supplier. Both original and cellobiose substitution variant retain this component. Add only the raw beta-pentahydrate alias to the existing CAS owner.

**Applicability:** CultureMech:003985 ingredients/5 {"concentration": {"unit": "G_PER_L", "value": "6"}, "preferred_term": "Na2-ß-glycerophosphate x 5 H2O"} | CultureMech:000688 ingredients/5 {"concentration": {"unit": "G_PER_L", "value": "6"}, "preferred_term": "Na2-ß-glycerophosphate x 5 H2O"} | CultureMech:003972 ingredients/5 {"concentration": {"unit": "G_PER_L", "value": "6"}, "preferred_term": "Na2-ß-glycerophosphate x 5 H2O"} | CultureMech:011601 composition/5 {"concentration": {"unit": "G_PER_L", "value": "6"}, "preferred_term": "Na2-ß-glycerophosphate x 5 H2O", "term": {"id": "mediadive.compound:230", "label": "Na2-ß-glycerophosphate x 5 H2O"}} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-99cf18e8cb22, sa-mediadive-230, sa-merck-35675, sa-chebi-17270, sa-merck-35675-retry, sa-merck35675-web, sa-recipe-1af8f9f6a54308, sa-recipe-a02b0a8b3db33b, sa-recipe-2f3656c39f1ebd, sa-recipe-77dba90ba07b0a, sa-owner-na2glycerophosphate5h2o

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 35 — Ammonium Fe(III) citrate

`CM_NAME:acb8383a6fcc62cffb1b72cb225ef8380eb43c2cdb7c4e3594744cd7447314ce` — existing_identity_or_alias

JCM1042/1137/1269 use Ammonium Fe(III) citrate. This explicitly ferric material matches CHEBI31604 ferric ammonium citrate, whose scope is indefinite mixture composition. No molecular stoichiometry, hydrate, or red/green formulation is inferred from the word order.

**Applicability:** CultureMech:007626 ingredients/17 {"concentration": {"unit": "G_PER_L", "value": "0.01"}, "notes": "Role: Nitrogen source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "Ammonium Fe(III) citrate"} | CultureMech:007745 ingredients/5 {"concentration": {"unit": "G_PER_L", "value": "1.42"}, "notes": "Role: Nitrogen source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "Ammonium Fe(III) citrate"} | CultureMech:007903 ingredients/15 {"concentration": {"unit": "G_PER_L", "value": "0.04"}, "notes": "Role: Nitrogen source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "Ammonium Fe(III) citrate"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-recipe-424e6e3dc840, sa-recipe-75410edb34dd, sa-chebi-31604, sa-recipe-44f2e960bfce02, sa-recipe-e8eff3c1dc74d7, sa-recipe-2349c03951a143, sa-togo-M1107, sa-togo-M1217, sa-recipe-f0fa77fefe0d, sa-togo-M1365, sa-owner-ferric_ammonium_citrate

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 36 — MgCl2 (anhydrous)

`CM_NAME:af3b3568fdab93be4dbbe475f0ec037bed6b757bab6f4490e10698ed8e7b1ecb` — existing_identity_or_alias

All four DSMZ514/514a-derived occurrences explicitly say MgCl2 anhydrous. This qualifier agrees with water-free CHEBI6636 and excludes the mono/four/six/seven-water cases reviewed separately. Preserve the source qualifier and doses, adding no hydrate equivalence.

**Applicability:** CultureMech:008832 ingredients/15 {"concentration": {"unit": "G_PER_L", "value": "5.9"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "MgCl2 (anhydrous)"} | CultureMech:008923 ingredients/14 {"concentration": {"unit": "G_PER_L", "value": "5.9"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "MgCl2 (anhydrous)"} | CultureMech:009175 ingredients/14 {"concentration": {"unit": "G_PER_L", "value": "5.9"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "MgCl2 (anhydrous)"} | CultureMech:008906 ingredients/14 {"concentration": {"unit": "G_PER_L", "value": "5.9"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "MgCl2 (anhydrous)"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-chebi-6636, sa-recipe-ae5507c0ce68, sa-recipe-26b65b3e913a, sa-recipe-288e3f86069e1e, sa-recipe-e4db307c2fb812, sa-recipe-67e01fc2be20e5, sa-recipe-963f1a3f529325, sa-togo-M2243, sa-togo-M2336, sa-togo-M2608, sa-togo-M2319, sa-owner-mgcl2

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 37 — CaCl2 (anhydrous)

`CM_NAME:b27fa65cdc306c1c2a6683ff6bf3099237566a1d8828cbac10d8fce011584aa0` — existing_identity_or_alias

All five source occurrences explicitly say CaCl2 anhydrous, matching CHEBI3312. An anhydrous alias is chemically supported independently of the unqualified/monohydrate source conflicts. The current owner contains a CaCl .6H O token and role fragments; the proposal does not approve these and requires a complete-payload review before publication.

**Applicability:** CultureMech:008816 ingredients/20 {"concentration": {"unit": "G_PER_L", "value": "1.4"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Simple component, Defined component", "preferred_term": "CaCl2 (anhydrous)"} | CultureMech:009627 ingredients/33 {"concentration": {"unit": "G_PER_L", "value": "100"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "CaCl2 (anhydrous)"} | CultureMech:009605 ingredients/29 {"concentration": {"unit": "G_PER_L", "value": "0.1"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "CaCl2 (anhydrous)"} | CultureMech:009202 ingredients/23 {"concentration": {"unit": "G_PER_L", "value": "0.1"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "CaCl2 (anhydrous)"} | CultureMech:009199 ingredients/22 {"concentration": {"unit": "G_PER_L", "value": "0.1"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "CaCl2 (anhydrous)"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-chebi-3312, sa-recipe-69c7dede331ed9, sa-recipe-cf74e900022cd6, sa-recipe-8777f601c7a1d9, sa-recipe-dd45d080511395, sa-recipe-2a64491d231814, sa-togo-M2228, sa-togo-M3174, sa-togo-M3136, sa-togo-M2646, sa-togo-M2642, sa-owner-cacl2

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 38 — β-glycerophosphate-2Na

`CM_NAME:ba62a33e9b4bee06375c54b95b7a14372083566511cfae1a774478b59c7cd279` — existing_identity_or_alias

NBRC1042/1463 explicitly name beta-glycerophosphate with2Na. This identifies the unqualified disodium glycerol2-phosphate salt sense in CHEBI132089; no hydrate is specified or inferred. It does not resolve the explicitly pentahydrate or generic isomer-mixture cases.

**Applicability:** CultureMech:008383 ingredients/14 {"concentration": {"unit": "G_PER_L", "value": "2"}, "notes": "Role: Mineral source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "β-glycerophosphate-2Na"} | CultureMech:008725 ingredients/11 {"concentration": {"unit": "G_PER_L", "value": "20"}, "notes": "Role: Mineral source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "β-glycerophosphate-2Na"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-chebi-132089, sa-recipe-5fa72073c6c6, sa-recipe-88cfae7776e4, sa-recipe-a2a04243d88075, sa-recipe-34614659ec75db, sa-togo-M1812, sa-togo-M2131, sa-owner-sodium_beta-glycerophosphate

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 39 — CaCl2·2H2O (2.5 g/L)

`CM_NAME:c67ff1de8ad274e2e689f9373b5c9baedd4bc5c3b66b05e461be5d8d678a9ed9` — stock_product_mixture_context

The Allen-medium occurrence names calcium chloride dihydrate at2.5g/L as a strength-qualified preparation. Its source amount cannot be read as a pure-solute identity. Preserve the2.5g/L stock and addition amount, and do not add a concentration-bearing chemical alias.

**Applicability:** CultureMech:008820 ingredients/6 {"concentration": {"unit": "G_PER_L", "value": "10"}, "preferred_term": "CaCl2·2H2O (2.5 g/L)"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-chebi-86158, sa-recipe-f465bb9cce36cc, sa-togo-M2231, sa-owner-cacl2_x_2_h2o

**Next requirement:** Retrieve TOGO M2231 stock preparation and dose unit, then separate stock strength from the amount added and final-medium concentration.

### 40 — di-Na-ß-glycerophosphate

`CM_NAME:d4ffd09291040a9dde73e064c08ab89968b757cdca2f257ced13c28e73d30b22` — existing_identity_or_alias

The DSMZ958-derived label di-Na-beta-glycerophosphate explicitly supplies disodium stoichiometry and beta positional identity, without hydration specification. It matches the unqualified salt sense CHEBI132089; this review does not add five waters or equate it with supplier35675.

**Applicability:** CultureMech:008887 ingredients/14 {"concentration": {"unit": "G_PER_L", "value": "0.01"}, "notes": "Role: Mineral source; Properties: Organic compound, Defined component, Simple component", "preferred_term": "di-Na-ß-glycerophosphate"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-chebi-132089, sa-recipe-3506d0253600, sa-recipe-48e685b2fe76fb, sa-togo-M2300, sa-owner-sodium_beta-glycerophosphate

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 41 — ZnCl2 x 6 H2O

`CM_NAME:d920033ebfa2c759c4a418e0bc1c4321ae910ac99e434dc2109a8fe37f40f9b2` — unresolved

Six frozen CCAP/MediaDive occurrences name ZnCl2 x6H2O, but the captured originals differ: C Modified and MAF6:SE explicitly print ZnCl2·6H2O at5mg/L trace stock; MDY-V prints ZnCl2 without hydrate at5mg/L trace stock; MBBM retrieval returned404. The MDY-V occurrence therefore has a demonstrable source-label discrepancy, while the other six-water claims still need exact product evidence. MediaDive2351 nominal244.4g/mol lacks CAS/formula; frozen CHEBI49976 anhydrous annotations cannot certify six waters. Treat each recipe lineage separately.

**Applicability:** CultureMech:000328 ingredients/9 {"concentration": {"unit": "G_PER_L", "value": "0.005"}, "preferred_term": "ZnCl2 x 6 H2O"} | CultureMech:000356 ingredients/10 {"concentration": {"unit": "G_PER_L", "value": "0.005"}, "preferred_term": "ZnCl2 x 6 H2O"} | CultureMech:000358 ingredients/12 {"concentration": {"unit": "G_PER_L", "value": "0.005"}, "preferred_term": "ZnCl2 x 6 H2O"} | CultureMech:000363 ingredients/12 {"concentration": {"unit": "G_PER_L", "value": "0.005"}, "preferred_term": "ZnCl2 x 6 H2O"} | CultureMech:014843 composition/4 {"chebi_term": {"id": "CHEBI:49976", "label": "zinc dichloride", "match_type": "manual_curated"}, "concentration": {"unit": "G_PER_L", "value": "0.005"}, "evidence": [{"explanation": "Concentration evidence for composition[4].concentration (ZnCl2 x 6 H2O) in MediaDive solution 6141; locator=$.data.recipe[4] (compound_id=2351). Provider explicitly reports g_l=0.005. Arithmetic check: 5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.005 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 1000. Retrieved 2026-10-07T10:00:32.988725+00:00; response SHA256=fd819e79c44b18b439550e627fa16401e1c4ab52e3cf08dd762920cbb04786a6.", "reference": "https://mediadive.dsmz.de/rest/solution/6141", "snippet": "{\n                \"recipe_order\": 6,\n                \"compound\": \"ZnCl2 x 6 H2O\",\n                \"compound_id\": 2351,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.005,\n                \"mmol_l\": 0.0204583,\n                \"optional\": 0\n            }", "supports": "SUPPORT"}], "preferred_term": "ZnCl2 x 6 H2O", "term": {"id": "mediadive.compound:2351", "label": "ZnCl2 x 6 H2O"}} | CultureMech:014886 composition/4 {"chebi_term": {"id": "CHEBI:49976", "label": "zinc dichloride", "match_type": "manual_curated"}, "concentration": {"unit": "G_PER_L", "value": "0.005"}, "evidence": [{"explanation": "Concentration evidence for composition[4].concentration (ZnCl2 x 6 H2O) in MediaDive solution 6187; locator=$.data.recipe[4] (compound_id=2351). Provider explicitly reports g_l=0.005. Arithmetic check: 5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.005 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00; response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916.", "reference": "https://mediadive.dsmz.de/rest/solution/6187", "snippet": "{\n                \"recipe_order\": 6,\n                \"compound\": \"ZnCl2 x 6 H2O\",\n                \"compound_id\": 2351,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.005,\n                \"mmol_l\": 0.0204583,\n                \"optional\": 0\n            }", "supports": "SUPPORT"}], "preferred_term": "ZnCl2 x 6 H2O", "term": {"id": "mediadive.compound:2351", "label": "ZnCl2 x 6 H2O"}} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-2351, sa-chebi-49976, sa-recipe-4004466c272e, sa-recipe-cc362088b0d0, sa-recipe-0db6aaa81bda, sa-recipe-66288f1e439a, sa-recipe-5be35385c03067, sa-recipe-8e9ce4e8bff7da, sa-recipe-baa3d65bef6b9f, sa-recipe-e4c7ce8bacdb9d, sa-recipe-c612e2504da46d, sa-recipe-722ae4dc30ff1f

**Next requirement:** Repair the MDY-V source discrepancy against its original ZnCl2 table; retrieve the missing MBBM recipe; obtain supplier/source-author identity for the explicit six-water C/MAF6/MediaDive lineage and reconcile anhydrous ontology annotations.

### 42 — ZnCl2·2H2O

`CM_NAME:dc9c9ff379875169bbcb8b3bd09810883d7154905d37b6ee18f5b4cbd1fb97b1` — unresolved

NBRC278/TOGO M1495 says ZnCl2·2H2O. This is distinct from both anhydrous zinc chloride and the six-water source cases. Bounded ChEBI search did not establish an exact term; no supplier/CAS linked to this recipe was verified. The retrieved NBRC278 original confirms the literal dihydrate at0.1mg per litre, rather than the frozen0.1G_PER_L; this verifies the source claim, not an exact supplier identity.

**Applicability:** CultureMech:008040 ingredients/9 {"concentration": {"unit": "G_PER_L", "value": "0.1"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component", "preferred_term": "ZnCl2·2H2O"} | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-ols-zn-dihydrate, sa-chebi-49976, sa-recipe-79b97c9e010a, sa-recipe-4fe6645e8da588, sa-togo-M1495

**Next requirement:** Primary NBRC278 reagent identity or correction with exact hydrate/CAS, and a source-linked supplier/ontology identifier for the dihydrate.

### 43 — FeCl2 x 6 H2O

`KG_CASE:047c6ac16709ad384bc5cef712feb73aa03bd8ea898ba6249061d9ed1bb4e11c` — unresolved

MediaDive555 preserves the FeCl2 six-water label while its primary compound response carries anhydrous CAS7758-94-3, CHEBI30812 and126.75g/mol. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries. OECD separately recognizes iron chloride hydrates, including the six-water CAS listing; this refutes a blanket nonexistence claim but does not identify the reagent used in this occurrence.

**Applicability:** Exact KG source record: {"amount": 0.01, "compound": "FeCl2 x 6 H2O", "compound_id": 555, "g_l": 0.01, "mmol_l": 0.0788955, "optional": 0, "recipe_order": 6, "unit": "g"} | Reviewed all 4 consumed-name hits, 2 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-555, sa-chebi-30812, sa-oecd-iron, sa-owner-fecl2_x_6_h2o, sa-owner-fecl2_x_7_h2o

**Next requirement:** Reconcile the exact MediaDive555 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.

### 44 — NiCl2 x H2O

`KG_CASE:05098d4fa5cd11f19fceaca7ef41657e43b97efb8f65e1a1981523abb91b6259` — unresolved

MediaDive1892 preserves the NiCl2 monohydrate label while its primary compound response carries anhydrous CAS7718-54-9, CHEBI34887 and129.599g/mol. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries.

**Applicability:** Exact KG source record: {"amount": 0.05, "compound": "NiCl2 x H2O", "compound_id": 1892, "g_l": 0.04995, "mmol_l": 0.38542, "optional": 0, "recipe_order": 9, "unit": "g"} | Reviewed all 0 consumed-name hits, 4 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-1892, sa-chebi-34887, sa-owner-nicl2, sa-owner-nicl2_x_2_h2o, sa-owner-nicl2_x_5_h2o, sa-owner-nicl2_x_6_h2o

**Next requirement:** Reconcile the exact MediaDive1892 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.

### 45 — NiCl2 x 2 H2O

`KG_CASE:09932bd7abe95bcdf69324e94b9cdc2a2f7ad6f883b74375b11089cc0733f210` — unresolved

MediaDive981 preserves the NiCl2 dihydrate label while its primary compound response carries anhydrous CAS7718-54-9, CHEBI34887 and129.599g/mol. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries. Current owner history records prior primary experimental support for nickel chloride dihydrate, so the substance itself is not rejected; the source CAS/mass conflict and withheld published payload remain.

**Applicability:** Exact KG source record: {"amount": 0.02, "compound": "NiCl2 x 2 H2O", "compound_id": 981, "g_l": 0.02, "mmol_l": 0.154322, "optional": 0, "recipe_order": 8, "unit": "g"} | Reviewed all 4 consumed-name hits, 4 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-981, sa-chebi-34887, sa-owner-nicl2, sa-owner-nicl2_x_2_h2o, sa-owner-nicl2_x_5_h2o, sa-owner-nicl2_x_6_h2o

**Next requirement:** Reconcile the exact MediaDive981 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.

### 46 — MgCl2 x H2O

`KG_CASE:19a44db1a0ac0c488a9d9a49d393fed1b0022627771a4345324355eb2a1a6bc4` — existing_identity_or_alias

MediaDive912 supplies monohydrate CAS22756-14-5, formula Cl2H2MgO and113.226g/mol; its raw100g/883.189mmol agrees. ChEBI86355 and current MgCl2 xH2O owner denote precisely this form. This is an existing source-specific identity with no new alias needed; inherited synonym/role/publication holds are not cleared.

**Applicability:** Exact KG source record: {"amount": 100, "compound": "MgCl2 x H2O", "compound_id": 912, "g_l": 100, "mmol_l": 883.189, "optional": 0, "recipe_order": 2, "unit": "g"} | Reviewed all 2 consumed-name hits, 1 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-912, sa-chebi-86355, sa-owner-mgcl2_x_h2o

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 47 — NiCl2 x 5 H2O

`KG_CASE:296ff706c39397b120ded30cbf892931966cea1cca4d84b25c47b52c24dc6193` — unresolved

MediaDive2037 preserves the NiCl2 pentahydrate label while its primary compound response carries anhydrous CAS7718-54-9, CHEBI34887 and129.599g/mol. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries.

**Applicability:** Exact KG source record: {"amount": 0.025, "compound": "NiCl2 x 5 H2O", "compound_id": 2037, "g_l": 0.025, "mmol_l": 0.192903, "optional": 0, "recipe_order": 9, "unit": "g"} | Reviewed all 4 consumed-name hits, 4 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-2037, sa-chebi-34887, sa-owner-nicl2, sa-owner-nicl2_x_2_h2o, sa-owner-nicl2_x_5_h2o, sa-owner-nicl2_x_6_h2o

**Next requirement:** Reconcile the exact MediaDive2037 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.

### 48 — MgCl2 x 4 H2O

`KG_CASE:3c48a8089257dee61f916cd9953aacadf9cd3937239a03a3c4410d5c6351f757` — unresolved

MediaDive871 preserves the MgCl2 tetrahydrate label while its primary compound response carries 95.2104g/mol anhydrous mass without exact hydrate CAS. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries.

**Applicability:** Exact KG source record: {"amount": 5, "compound": "MgCl2 x 4 H2O", "compound_id": 871, "g_l": 0.005, "mmol_l": 0.0525153, "optional": 0, "recipe_order": 3, "unit": "mg"} | Reviewed all 0 consumed-name hits, 0 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-871, sa-pubchem-mg-tetrahydrate, sa-chebi-6636

**Next requirement:** Reconcile the exact MediaDive871 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.

### 49 — CoCl2 x 2 H2O

`KG_CASE:4228a1c6b7abaa025d1536c765e72d7abc99a55255ed2365863aa7a9880a02ff` — unresolved

MediaDive578 preserves the CoCl2 dihydrate label while its primary compound response carries anhydrous CAS7646-79-9, CHEBI35696 and129.839g/mol. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries.

**Applicability:** Exact KG source record: {"amount": 28, "compound": "CoCl2 x 2 H2O", "compound_id": 578, "g_l": 0.028, "mmol_l": 0.215652, "optional": 0, "recipe_order": 1, "unit": "mg"} | Reviewed all 4 consumed-name hits, 3 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-578, sa-chebi-35696, sa-owner-cocl2_x_2_h2o, sa-owner-cocl2_x_4_h2o, sa-owner-cocl2_x_6_h2o

**Next requirement:** Reconcile the exact MediaDive578 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.

### 50 — Manganese Sulfate

`KG_CASE:476f4d78d98f3dbdfbef462c921a80f0a791a2d978841b88aa7cf4b16dc826fd` — existing_identity_or_alias

Although the source label says only Manganese Sulfate, MediaDive939 independently specifies CAS10034-96-5, CHEBI86364 and169.016g/mol, and raw0.42g/2.48497mmol is consistent with monohydrate. This source-specific metadata identifies the existing monohydrate owner; do not add Manganese Sulfate as an unrestricted hydrate synonym.

**Applicability:** Exact KG source record: {"amount": 0.42, "compound": "Manganese Sulfate", "compound_id": 939, "g_l": 0.42, "mmol_l": 2.48497, "optional": 0, "recipe_order": 11, "unit": "g"} | Reviewed all 2 consumed-name hits, 1 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-939, sa-chebi-86364, sa-owner-mnso4_x_h2o

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 51 — MnCl2 x 4 H2O

`KG_CASE:4a2e9c4280f6e484dc1768416f4d4b9c32371cc8cd9c0e87adb2c8b3324c43a6` — existing_identity_or_alias

MediaDive36 specifies manganese chloride tetrahydrate CAS13446-34-9, CHEBI86368 and197.905g/mol; raw0.03g/0.151588mmol agrees. Current exact owner already preserves this label. Worker02 separately reviews MnCl4 x4H2O against the same owner hash, so any later byte change requires coordinator conflict reconciliation; no cross-shard result is adopted here.

**Applicability:** Exact KG source record: {"amount": 0.03, "compound": "MnCl2 x 4 H2O", "compound_id": 36, "g_l": 0.03, "mmol_l": 0.151588, "optional": 0, "recipe_order": 4, "unit": "g"} | Reviewed all 2 consumed-name hits, 1 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-36, sa-chebi-86368, sa-owner-mncl2_x_4_h2o

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 52 — Tryptose-phosphate

`KG_CASE:4d7c7ef17e3749f1d246dba57456564b84a8091914c1fd6ff77ee37f0933ca07` — stock_product_mixture_context

MediaDive1165 Tryptose-phosphate is added as2mL and has group Tryptose with no single-compound identifiers. Tryptose phosphate broth is a multi-component formulation; the short label does not identify a precise commercial formulation/strength. Preserve the UNDEFINED_MIXTURE placeholder and do not map the whole preparation to tryptose or phosphate.

**Applicability:** Exact KG source record: {"amount": 2, "compound": "Tryptose-phosphate", "compound_id": 1165, "optional": 0, "recipe_order": 3, "unit": "ml"} | Reviewed all 0 consumed-name hits, 1 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-1165, sa-fda-tryptose, sa-owner-tryptose-phosphate

**Next requirement:** Original recipe or catalogue specifying which tryptose-phosphate preparation and concentration was used for the2mL addition; represent component assertions only from that formulation.

### 53 — NaSiO3 x 9 H2O

`KG_CASE:5bd26afe54ceed1b68ce9e505f2c5b37aaa77991f2638030a505bfd81039eb77` — supplied_form_correction

MediaDive175 label NaSiO3 x9H2O drops a sodium subscript, but its independent CAS13517-24-3 identifies disodium metasilicate nonahydrate. Wako SDS and GSRS identify that exact nine-water substance, consistent with the existing Na2SiO3 x9H2O owner. Source formula metadata also carries extra hydrogens, so correct the source-specific interpretation rather than creating a global malformed alias. Preserve both the unmapped raw-label owner and mapped hydrate pending reviewed consolidation.

**Applicability:** Exact KG source record: {"amount": 5, "compound": "NaSiO3 x 9 H2O", "compound_id": 175, "g_l": 0.005, "optional": 0, "recipe_order": 8, "unit": "mg"} | Reviewed all 0 consumed-name hits, 1 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-175, sa-wako-silicate9, sa-gsrs-silicate9, sa-chebi-132108, sa-owner-na2sio3_x_9_h2o, sa-owner-nasio3_x_9_h2o

**Next requirement:** Coordinator/source-author correction of the Na2SiO3 formula and source-specific routing; review both owners and duplicate consolidation before publication.

### 54 — HBO3

`KG_CASE:5d0ce252b889447ca5ae13779f4ef660e3ca4c56ed3ad060f7a0df5e050cf3c6` — malformed_or_nonchemical_token

MediaDive915 repeats HBO3 in its formula and59.82g/mol; the raw0.01g/0.167168mmol follows that same malformed formula. These internally consistent derived values do not independently show boric acid H3BO3. Preserve the raw placeholder until original reagent evidence supplies the missing stoichiometry.

**Applicability:** Exact KG source record: {"amount": 10, "compound": "HBO3", "compound_id": 915, "g_l": 0.01, "mmol_l": 0.167168, "optional": 0, "recipe_order": 11, "unit": "mg"} | Reviewed all 0 consumed-name hits, 1 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-915, sa-chebi-33118, sa-owner-hbo3

**Next requirement:** Original source recipe/catalogue establishing intended boron reagent and correcting HBO3 plus derived molecular weight; do not guess H3BO3 from nutrient role.

### 55 — NaSiO3 x 5 H2O

`KG_CASE:5ef66b1b22618252e5456a27f17102edebec95fe96e463a02220f7ab2c338654` — stock_product_mixture_context

MediaDive2420 is NaSiO3 x5H2O with CAS10213-79-3 but the actual source occurrence adds1mL of a3.73g/L stock. The exact source is a preparation with a malformed sodium subscript; neither the nonahydrate owner nor anhydrous sodium silicate identifies the stock as a whole. This is related to the distinct MediaDive2160 hold in1157, not the same occurrence.

**Applicability:** Exact KG source record: {"amount": 1, "attribute": "3.73 g/l stock solution", "compound": "NaSiO3 x 5 H2O", "compound_id": 2420, "optional": 0, "recipe_order": 4, "unit": "ml"} | Reviewed all 0 consumed-name hits, 0 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-2420, sa-chebi-60720

**Next requirement:** Exact pentahydrate-stock recipe, corrected Na2SiO3 formula and3.73g/L preparation/dose relationship, with verified reagent specification.

### 56 — ZnCl2 x 6 H2O

`KG_CASE:698cf64944cb92c17cb25ae8ec9b250b036f66f281adac46948ecb64c55663bb` — unresolved

MediaDive2351 records ZnCl2 x6H2O and244.4g/mol but no CAS/ontology/formula. A mass computed from the label is not independent identification of the supplied hydrate. Its CCAP lineage requires source-author/product confirmation; do not map it to anhydrous CHEBI49976.

**Applicability:** Exact KG source record: {"amount": 5, "compound": "ZnCl2 x 6 H2O", "compound_id": 2351, "g_l": 0.005, "mmol_l": 0.0204583, "optional": 0, "recipe_order": 6, "unit": "mg"} | Reviewed all 0 consumed-name hits, 0 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-2351, sa-chebi-49976

**Next requirement:** Primary source/supplier identity for MediaDive2351 six-water zinc chloride, with exact hydrate CAS or explicit source correction.

### 57 — MgCl2 x 7 H2O

`KG_CASE:7778a20f86a0785c78cedc561dc7c1dc46552efa52e29f03abc7ccd22d15fb9e` — unresolved

MediaDive632 preserves the MgCl2 heptahydrate label while its primary compound response carries anhydrous formula Cl2Mg and95.2104g/mol. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries.

**Applicability:** Exact KG source record: {"amount": 0.1, "compound": "MgCl2 x 7 H2O", "compound_id": 632, "g_l": 0.0994036, "mmol_l": 1.04404, "optional": 0, "recipe_order": 4, "unit": "g"} | Reviewed all 4 consumed-name hits, 3 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-632, sa-chebi-6636, sa-owner-mgcl2_x_6_h2o, sa-owner-mgcl2_x_7_h2o, sa-owner-mgcl2x_6_h2o

**Next requirement:** Reconcile the exact MediaDive632 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.

### 58 — MnCl2 x 2 H2O

`KG_CASE:79561e6680c4536f764e8b244fb78bcd54b18347dab5104f741b866e7a52dd73` — existing_identity_or_alias

MediaDive63 supplies CAS20603-88-7 and formula MnCl2·2H2O, and ChEBI131395 describes manganese dichloride dihydrate. The current exact dihydrate owner matches this source-specific form. No new owner or cross-hydrate alias is needed, and existing full-payload holds remain.

**Applicability:** Exact KG source record: {"amount": 50, "compound": "MnCl2 x 2 H2O", "compound_id": 63, "g_l": 0.05, "optional": 0, "recipe_order": 4, "unit": "mg"} | Reviewed all 2 consumed-name hits, 1 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-63, sa-chebi-131395, sa-owner-mncl2_x_2_h2o

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 59 — CoCl2 x 6 H2O

`KG_CASE:9732bb704373e55707bb613086c396ecca4455bc7d99e05079cf6d8f0254c465` — unresolved

MediaDive38 preserves the CoCl2 hexahydrate label while its primary compound response carries anhydrous CAS7646-79-9, CHEBI35696 and129.839g/mol. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries.

**Applicability:** Exact KG source record: {"amount": 0.2, "compound": "CoCl2 x 6 H2O", "compound_id": 38, "g_l": 0.2, "mmol_l": 1.54037, "optional": 0, "recipe_order": 6, "unit": "g"} | Reviewed all 2 consumed-name hits, 4 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-38, sa-chebi-53503, sa-chebi-35696, sa-owner-cobalt_chloride_hexahydrate, sa-owner-cocl2_x_2_h2o, sa-owner-cocl2_x_4_h2o, sa-owner-cocl2_x_6_h2o

**Next requirement:** Reconcile the exact MediaDive38 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.

### 60 — CuCl2 x 6 H2O

`KG_CASE:9ddeb17521470c9c17c5a253d1b7f6a433866f718645dfc3f2e3b48c4ef70f70` — unresolved

MediaDive1056 preserves the CuCl2 hexahydrate label while its primary compound response carries anhydrous CAS7447-39-4, CHEBI49553 and134.452g/mol. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries.

**Applicability:** Exact KG source record: {"amount": 1, "compound": "CuCl2 x 6 H2O", "compound_id": 1056, "g_l": 0.001, "mmol_l": 0.0074376, "optional": 0, "recipe_order": 4, "unit": "mg"} | Reviewed all 4 consumed-name hits, 2 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-1056, sa-chebi-49553, sa-owner-cucl2, sa-owner-cucl2_x_6_h2o

**Next requirement:** Reconcile the exact MediaDive1056 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.

### 61 — CaCl2 x H2O

`KG_CASE:a0a4f599c8b3c5da1fc63f4ce96dccf50da2def9458fb7621eebb3891ae7bbbc` — unresolved

MediaDive356 preserves the CaCl2 monohydrate label while its primary compound response carries anhydrous CAS10043-52-4, CHEBI3312 and110.983g/mol. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries.

**Applicability:** Exact KG source record: {"amount": 0.14, "compound": "CaCl2 x H2O", "compound_id": 356, "g_l": 0.138477, "mmol_l": 1.24773, "optional": 0, "recipe_order": 5, "unit": "g"} | Reviewed all 0 consumed-name hits, 2 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-356, sa-chebi-3312, sa-owner-cacl2, sa-owner-cacl2_x_7_h2o

**Next requirement:** Reconcile the exact MediaDive356 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.

### 62 — L-α-Phosphatidylcholine

`KG_CASE:bf2b7dbfeb8408eecd00d201503c35afa9eec47205bee90cbe2a197c81ad7150` — stock_product_mixture_context

MediaDive2082 explicitly specifies Sigma P3556. Supplier P3556 is egg-yolk L-alpha-phosphatidylcholine material; this product has a molecular-species distribution. The consumed owner CHEBI86658 describes one particular acyl-chain/geometry species, so it cannot identify the entire P3556 product. Preserve both embedded downstream material quarantines and the exact catalogue anchor.

**Applicability:** Exact KG source record: {"amount": 5, "attribute": "SIGMA P3556", "compound": "L-α-Phosphatidylcholine", "compound_id": 2082, "g_l": 5, "optional": 0, "recipe_order": 1, "unit": "mg"} | Reviewed all 2 consumed-name hits, 1 original owner records, and 2 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-2082, sa-sigma-p3556, sa-chebi-86658, sa-sigma-p3556-retry, sa-sigma-p3556-web, sa-owner-l-alpha-phosphatidylcholine

**Next requirement:** Product-scoped composition and exact material owner reconciliation, followed by review of the CHEBI86658 species mismatch; no chain-specific identity replacement for the whole product.

### 63 — Na3-NTA x H2O

`KG_CASE:bfb99789e68e3fbe86a70b16da919940fa2b0b518b1c757a09fd4bd9f70e71e7` — stock_product_mixture_context

MediaDive1482 specifies trisodium NTA monohydrate CAS18662-53-8, but the source occurrence adds4.8mL of0.5M solution. Both hydration and solution scope differ from unqualified trisodiumNTA CHEBI132766. Preserve the monohydrate raw placeholder and source stock; the related1930 hold in1157 is not a substitute for this occurrence review.

**Applicability:** Exact KG source record: {"amount": 4.8, "attribute": "0.5 M solution", "compound": "Na3-NTA x H2O", "compound_id": 1482, "mmol_l": 2.4, "optional": 0, "recipe_order": 2, "unit": "ml"} | Reviewed all 0 consumed-name hits, 1 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-1482, sa-chebi-132766, sa-owner-na3-nta_x_h2o

**Next requirement:** Verified0.5M stock preparation, carrier and hydrated reagent specification for MediaDive1482; model the preparation separately from any new monohydrate component owner.

### 64 — CoCl2 x 4 H2O

`KG_CASE:cea1f6b97226d1359f537e3414a6ce68de919e59e7d182ec4e0309299cdc79df` — unresolved

MediaDive626 preserves the CoCl2 tetrahydrate label while its primary compound response carries anhydrous CAS7646-79-9, CHEBI35696 and129.839g/mol. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries.

**Applicability:** Exact KG source record: {"amount": 0.3, "compound": "CoCl2 x 4 H2O", "compound_id": 626, "g_l": 0.3, "mmol_l": 2.31055, "optional": 0, "recipe_order": 4, "unit": "g"} | Reviewed all 4 consumed-name hits, 3 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-626, sa-chebi-35696, sa-owner-cocl2_x_2_h2o, sa-owner-cocl2_x_4_h2o, sa-owner-cocl2_x_6_h2o

**Next requirement:** Reconcile the exact MediaDive626 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.

### 65 — MnCl2 x 6 H2O

`KG_CASE:d1ae10fb33b343e84c036ee949eda29b7304a42ebb49b58e597e256428fa83cc` — unresolved

MediaDive2003 retains MnCl2 x6H2O but has no exact CAS/formula/molecular-weight support. The raw4.55mg dose belongs to the JCM metal-mixture lineage also represented by CultureMech cases14/29/31. Shared import ancestry is explicit evidence reuse, not independent validation of a six-water product. A separately retrieved official JCM1118 HTML capture succeeds and explicitly prints MnCl2·6H2O at4.55mg per litre of metal stock, added1mL/L. This establishes the source claim and stock boundary, but supplies no reagent CAS and does not resolve whether the six-water label is correct. Earlier empty HTTP200 JCM captures are retained as unsuccessful attempts, superseded only for recipe availability.

**Applicability:** Exact KG source record: {"amount": 4.55, "compound": "MnCl2 x 6 H2O", "compound_id": 2003, "g_l": 0.00455, "optional": 0, "recipe_order": 4, "unit": "mg"} | Reviewed all 0 consumed-name hits, 0 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-2003, sa-ols-mn-hexahydrate, sa-jcm1118-shared, sa-jcm1119-retry, sa-jcm1120-retry

**Next requirement:** Original JCM metal-mixture reagent identity or source-author correction resolving six-water manganese chloride for MediaDive2003.

### 66 — Na2-ß-glycerophosphate x 5 H2O

`KG_CASE:ddfa4e9d7b01c1872029368c74bbb5c939227e33bded259e75a7e48b09689441` — existing_identity_or_alias

MediaDive230 explicitly names beta/disodium/pentahydrate, supplies Merck35675 and CAS13408-09-8, and gives306.11g/mol consistent with6g/19.6008mmol. Supplier evidence supports the same exact form. Reuse the existing CAS13408-09-8 owner and source alias shared with the DSMZ122 CultureMech case; do not infer a glycerol3 isomer.

**Applicability:** Exact KG source record: {"amount": 6, "attribute": "MERCK 35675", "compound": "Na2-ß-glycerophosphate x 5 H2O", "compound_id": 230, "g_l": 6, "mmol_l": 19.6008, "optional": 0, "recipe_order": 6, "unit": "g"} | Reviewed all 0 consumed-name hits, 0 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-230, sa-merck-35675, sa-chebi-17270, sa-merck-35675-retry, sa-merck35675-web, sa-owner-na2glycerophosphate5h2o

**Next requirement:** No additional source-identity requirement within this decision; complete-payload/native review and coordinator publication obligations remain.

### 67 — CuCl2 x H2O

`KG_CASE:e3620d5ad1c5b3a95a5467a08ea999e3c7712f6080e8095ef7409cf27c6b08ee` — unresolved

MediaDive591 preserves the CuCl2 monohydrate label while its primary compound response carries anhydrous CAS7447-39-4, CHEBI49553 and134.452g/mol. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries.

**Applicability:** Exact KG source record: {"amount": 0.05, "compound": "CuCl2 x H2O", "compound_id": 591, "g_l": 0.5, "mmol_l": 3.7188, "optional": 0, "recipe_order": 4, "unit": "g"} | Reviewed all 0 consumed-name hits, 2 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-591, sa-chebi-49553, sa-owner-cucl2, sa-owner-cucl2_x_6_h2o

**Next requirement:** Reconcile the exact MediaDive591 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.

### 68 — NiCl2 x 6 H2O

`KG_CASE:f527458e161f77cc363140a6708e6cd18be73f9432b5d565e017b2fac4d84b63` — unresolved

MediaDive40 preserves the NiCl2 hexahydrate label while its primary compound response carries anhydrous CAS7718-54-9, CHEBI34887 and129.599g/mol. The frozen g/L-to-mmol/L conversion follows the parent mass, so it is not independent hydrate evidence. A known hydrate or local owner does not decide which conflicting source field is authoritative. Preserve all existing WITHHOLD/REJECTED and source-specific routing boundaries.

**Applicability:** Exact KG source record: {"amount": 0.02, "compound": "NiCl2 x 6 H2O", "compound_id": 40, "g_l": 0.02, "mmol_l": 0.154322, "optional": 0, "recipe_order": 8, "unit": "g"} | Reviewed all 2 consumed-name hits, 5 original owner records, and 0 downstream holds. Helper occurrence count is not measured recipe frequency. | Evidence reuse is scoped to this exact label and recipe lineage; shared ontology or supplier captures do not resolve contradictory source fields elsewhere. No inherited WITHHOLD, REJECTED_LABEL, downstream quarantine or unsupported role is released.

**Evidence:** sa-frozen-shard, sa-mediadive-40, sa-chebi-53542, sa-chebi-34887, sa-owner-nickel_ii_chloride_hexahydrate, sa-owner-nicl2, sa-owner-nicl2_x_2_h2o, sa-owner-nicl2_x_5_h2o, sa-owner-nicl2_x_6_h2o

**Next requirement:** Reconcile the exact MediaDive40 reagent/source recipe hydration with its conflicting CAS/formula/molecular-weight fields using a supplier or source-author record; then independently review the complete owner payload and existing holds.
