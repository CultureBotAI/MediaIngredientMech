# Unmapped ingredient review — 2026-09-01

## Outcome

This review uses the synchronized per-record corpus after the accepted synonym
merges. The authoritative collection now contains **274 records**: **263 UNMAPPED**
and **11 REJECTED**. The 263 active unmapped records consist of:

| Ingredient type | Count | Disposition |
|---|---:|---|
| `NAMED_MEDIUM` | 101 | Intentionally not identity-mapped as ingredients. A named medium is a formulation and belongs in the CultureMech reference/partonomy lane. |
| `UNDEFINED_MIXTURE` | 90 | Intentionally unmapped. A mixture, extract, solution, or incompletely specified preparation must not inherit the identity of one component. |
| `SINGLE_INGREDIENT` | 72 | Individually reviewed below. No additional exact ontology identity or safe mapped-record synonym was supported by the current evidence. |

The 11 `REJECTED` records are retained tombstones or parse artifacts and are not
active mapping targets.

Four formerly unmapped records were resolved as synonyms of existing mapped
records:

| Removed unmapped record | Mapped representative | Basis |
|---|---|---|
| `UNMAPPED_0401` — Homo-PIPES | `cas:202185-84-0` — HOMOPIPES | Same expanded reagent name, with the mapped record carrying CAS 202185-84-0. The source record's literature review independently expanded Homo-PIPES to homopiperazine-1,4-bis(2-ethanesulfonic acid). |
| `UNMAPPED_0456` — Mycobactine J | `CHEBI:205364` — Mycobactin J | Spelling variant. The source record's literature review explicitly recommended normalizing to Mycobactin J while retaining Mycobactine J as a variant. |
| `UNMAPPED_0081` — Na2Glycerophosphate.5H2O | `cas:13408-09-8` — Na2glycerophosphate•5H2O | Same stated pentahydrate and CAS 13408-09-8. |
| `UNMAPPED_0101` — Na2Glycerophosphate•5H2O | `cas:13408-09-8` — Na2glycerophosphate•5H2O | Same stated pentahydrate and CAS 13408-09-8. |

Their raw labels and catalog/CAS-bearing variants were retained as synonyms on
the mapped representatives. The two glycerophosphate records contributed two
occurrences across two media to the representative.

## Evidence and decision rules

- `reports/mim_unmapped_groundings.tsv` searched the pre-merge set of 76
  single-ingredient records. It reported 74 `NO_EXACT_HIT` results and two nominal
  `NEW_RECORD` results. Both nominal results are false positives: `X` matched
  `UBERON:0002687` "area X of ventral lateral nucleus", while `Ca` matched elemental
  calcium even though the record's source context denotes an incomplete
  calcium-nitrate-tetrahydrate label.
- A local comparison against every mapped preferred term and accepted synonym
  found the four duplicate records merged above. Other high-similarity pairs were
  rejected when they changed hydration, stoichiometry, counterion, oxidation state,
  stereochemistry, molecular-weight fraction, positional isomerism, or preparation
  identity.
- Existing record-level curation history and literature annotations were treated
  as evidence, not overwritten. They consistently support retaining the residual
  below as unmapped until an exact term, independent CAS identity, or source
  correction is available.
- Identity follows `MAPPING_SEMANTICS.md`: hydrates, salts, stereoisomers, polymers,
  mixtures, and generic family labels are not synonyms merely because their names
  are similar. A weak `closeMatch` was not used as a substitute for uncertainty.

The near-match report at `reports/culturemech_residual_near_matches.tsv` is a
different surface: it covers raw unresolved CultureMech labels rather than the
curated unmapped collection. Its risk flags were useful corroboration, but its
candidate rows are not curated mappings.

## Special cases among the 72 single ingredients

### Damaged, abbreviated, or under-specified source labels (13)

These cannot be assigned an identity without correcting or recovering the source
meaning. The apparent nearby terms would discard material distinctions.

| Identifier | Label | Why it remains unmapped |
|---|---|---|
| `UNMAPPED_0818` | X | Placeholder-like label; the ontology hit is an anatomical false positive. |
| `UNMAPPED_0049` | Ca | Source context indicates a truncated calcium nitrate tetrahydrate label, not elemental calcium. |
| `UNMAPPED_0385` | FeSO43 x n H2O | Malformed iron-sulfate formula with unspecified hydration. |
| `UNMAPPED_0398` | HBO3 | Malformed/ambiguous boron oxoacid formula; mapping to H3BO3 would assume a correction. |
| `UNMAPPED_0172` | LL17-29 | Opaque code with no source-backed chemical identity. |
| `UNMAPPED_0450` | MnCl4 x 6 H2O | Nonstandard/internally suspect manganese-chloride hydrate formula. |
| `UNMAPPED_0517` | Se-acid | Abbreviation conflicts with source chemistry; selenous and selenic acid are not interchangeable. |
| `UNMAPPED_0542` | Titriplex1 | Trade-name-like token not verified to one NTA/EDTA form. |
| `UNMAPPED_0477` | NaSiO3 x 9 H2O | Missing sodium stoichiometry; not safely identical to mapped Na2SiO3·9H2O. |
| `UNMAPPED_0460` | Na-Nitrilotriacetat | `Na-` does not specify mono-, di-, or trisodium NTA or hydration state. |
| `UNMAPPED_0606` | Iron-EDTA | Oxidation state, counterions, and salt state are unspecified. |
| `UNMAPPED_0604` | Iron (as FeCl3 in EDTA) | A preparation description, not an exact identity for Fe(III)-EDTA or iron. |
| `UNMAPPED_0325` | Amphotericin | Family-level label spanning amphotericin A/B and formulations; cannot be collapsed to amphotericin B. |

### Metal chelates with no exact supported term (12)

The metal and ligand are known, but the exact complex, oxidation state, charge,
or salt form lacks a verified ontology identity. Mapping these to the free metal,
free NTA/EDTA, or another metal complex would be false identity.

| Identifier | Label |
|---|---|
| `UNMAPPED_0157` | Aluminum-NTA |
| `UNMAPPED_0156` | Cadmium-NTA |
| `UNMAPPED_0153` | Chromium-NTA |
| `UNMAPPED_0154` | Cobalt-NTA |
| `UNMAPPED_0151` | Copper-NTA |
| `UNMAPPED_0149` | Ferric-NTA |
| `UNMAPPED_0155` | Manganese-NTA |
| `UNMAPPED_0152` | Nickel-NTA |
| `UNMAPPED_0150` | Zinc-NTA |
| `UNMAPPED_0143` | cobalt (III)-EDTA |
| `UNMAPPED_0451` | MnII x EDTA |
| `UNMAPPED_0618` | Titanium(III) citrate |

### Exact salt or hydrate absent or unsupported (11)

These are plausible single substances, but no exact resolvable term or independent
identity evidence currently supports promotion. Parent/anion terms and other
hydrates are not exact substitutes.

| Identifier | Label | Blocking distinction |
|---|---|---|
| `UNMAPPED_0355` | CeNO33 x 6 H2O | Cerium nitrate hexahydrate-specific identity. |
| `UNMAPPED_0423` | LaNO33 x 6 H2O | Lanthanum nitrate hexahydrate-specific identity. |
| `UNMAPPED_0465` | Na2 beta-glycerol PO4 x 5 H2O | Disodium beta-glycerophosphate pentahydrate; exact hydrate/CAS needs confirmation. |
| `UNMAPPED_0475` | Na3-NTA x H2O | Trisodium NTA hydrate-specific identity. |
| `UNMAPPED_0479` | NdCl3 x 6 H2O | Neodymium chloride hexahydrate-specific identity. |
| `UNMAPPED_0498` | PrCl3 x H2O | Praseodymium chloride hydrate stoichiometry/identity. |
| `UNMAPPED_0587` | α-D-Glucose monohydrate | Crystalline monohydrate must not share an anhydrous glucose identifier. |
| `UNMAPPED_0463` | Na-tetrathionate | Sodium salt is not mapped potassium tetrathionate or bare tetrathionate. |
| `UNMAPPED_0524` | Sodium crotonate | Sodium salt is not the bare crotonate anion. |
| `UNMAPPED_0615` | Sodium phosphate monobasic (phosphorus source) | Role-qualified label lacks exact hydrate/form evidence; existing CHEBI:37586 is retained only as a broader parent proposal. |
| `UNMAPPED_0159` | Ethanolamine acetate | Exact salt identity lacks a verified term; components are not substitutes for the salt. |

### Cholinium salts with no exact supported term (5)

| Identifier | Label | Note |
|---|---|---|
| `UNMAPPED_0164` | Cholinium alpha ketoglutarate | Not sodium alpha-ketoglutarate or the free acid. |
| `UNMAPPED_0163` | Cholinium aspartate | Counterion-specific salt. |
| `UNMAPPED_0161` | Cholinium glutamate | Counterion-specific salt. |
| `UNMAPPED_0162` | Cholinium hydrogen phosphate | Must not be merged with cholinium dihydrogen phosphate. |
| `UNMAPPED_0160` | Cholinium phosphate | Protonation/salt form unresolved. |

### Precise specialty small molecules with no exact term (18)

These labels denote specific positional isomers, natural products, complexes, or
derivatives. Nearby ontology terms are chemically different and therefore are not
synonyms.

| Identifier | Label |
|---|---|
| `UNMAPPED_0196` | 2-Carene-3-One |
| `UNMAPPED_0190` | 2',2'-Bisepigallocatechin Digallate |
| `UNMAPPED_0195` | 3Beta-Hydroxydeoxodihydrodeoxygedunin |
| `UNMAPPED_0194` | 4,4'-Dimethoxydalbergione |
| `UNMAPPED_0320` | 6-methylnicotinate |
| `UNMAPPED_0199` | 7,2'-Dimethoxyflavone |
| `UNMAPPED_0189` | 7,4'-Dimethoxyisoflavone |
| `UNMAPPED_0197` | Acetyl-Dihydro-7-Epikhivorin |
| `UNMAPPED_0198` | Agelasine |
| `UNMAPPED_0239` | apo-yersiniabactin |
| `UNMAPPED_0187` | Avocatin A |
| `UNMAPPED_0200` | Deoxysappanone B 7,3'-Dimethyl Ether |
| `UNMAPPED_0192` | Dihydrodehydroerosone |
| `UNMAPPED_0188` | Epitheaflavic Acid |
| `UNMAPPED_0193` | Gossypol-Acetic Acid Complex |
| `UNMAPPED_0234` | isopropyl 3-keto-N-acetyl-a-D-glucosamine |
| `UNMAPPED_0191` | Khayasin C |
| `UNMAPPED_0233` | methyl 3-keto-a-D-glucopyranoside |

### Cobamide variants (5)

The lower-ligand variants are distinct cobamides. They must not be treated as
synonyms of cobalamin/vitamin B12 or of one another.

| Identifier | Label |
|---|---|
| `UNMAPPED_0182` | 2-methyladeninyl cobamide |
| `UNMAPPED_0180` | 5-methoxybenzimidazolyl cobamide |
| `UNMAPPED_0179` | 5-methylbenzimidazolyl cobamide |
| `UNMAPPED_0181` | adeninyl cobamide |
| `UNMAPPED_0178` | benzimidazolyl cobamide |

### Polymers and molecular-weight-specific materials (6)

Polymer stereochemistry, repeat-unit identity, and molecular-weight fractions are
material distinctions. Generic dextran, xylan, or PHB records are not automatically
synonymous with these preparations.

| Identifier | Label |
|---|---|
| `UNMAPPED_0167` | dextran, Mw ~1,270 |
| `UNMAPPED_0168` | dextran, Mw ~200,000 |
| `UNMAPPED_0227` | O-methyl-D-glucuronoxylan |
| `UNMAPPED_0493` | poly-ß-hydroxybutyric acid |
| `UNMAPPED_0494` | Poly[R-3-hydroxybutyric acid] |
| `UNMAPPED_0492` | Poly hexamethylene carbonate |

### Protein/reagent variants (2)

| Identifier | Label | Why it remains unmapped |
|---|---|---|
| `UNMAPPED_0229` | Calprotectin S1 | Specific subunit/reagent label, not synonymous with generic calprotectin. |
| `UNMAPPED_0230` | Calprotectin S1S2 | Specific complex/reagent label, not synonymous with generic calprotectin or S1 alone. |

## Follow-up conditions

The residual should only move when one of the following becomes available:

1. a resolvable ontology term at the same hydration, salt, stereochemical, and
   preparation granularity;
2. an independent CAS or other stable registry identifier for the exact substance,
   allowing the documented CAS-primary plus parent mapping pattern;
3. an upstream source correction that resolves a malformed or abbreviated label;
4. source evidence proving that a label is a true synonym of an existing mapped
   record rather than merely a related material.

Absent one of those conditions, retaining these records as explicitly reviewed
`UNMAPPED` entries is the ontologically safer result.
