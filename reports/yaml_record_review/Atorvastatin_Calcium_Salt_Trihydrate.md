# `data/ingredients/mapped/Atorvastatin_Calcium_Salt_Trihydrate.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed record denotes atorvastatin calcium
trihydrate, and `CHEBI:2911`, CAS `344423-98-9`, the formula with three waters,
InChI, SMILES, SSSOM row, and hydrate review row all agree on that exact form.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Atorvastatin_Calcium_Salt_Trihydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:2911` with
  `ontology_mapping.ontology_id: CHEBI:2911`,
  `ontology_label: atorvastatin calcium trihydrate`,
  `ontology_source: CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, and
  `mapping_status: MAPPED`.
- OLS resolves `CHEBI:2911` to non-obsolete
  `atorvastatin calcium trihydrate`, with CAS xref `344423-98-9`, formula
  `2C33H34FN2O5.Ca.3H2O`, and the same InChI and SMILES stored on the record.
- PubChem resolves CAS `344423-98-9` to CID 656846 with formula
  `C66H74CaF2N4O13`, equivalent to two atorvastatin anions, one calcium, and
  three waters, plus the same InChI as ChEBI and the local record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Asparagine.yaml data/ingredients/mapped/Aspartate.yaml data/ingredients/mapped/Astaxanthin.yaml data/ingredients/mapped/Astromicin.yaml data/ingredients/mapped/Atorvastatin_Calcium_Salt_Trihydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Atorvastatin_Calcium_Salt_Trihydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:2911` resolved the expected non-obsolete trihydrate
  term and confirmed its CAS, formula, InChI, and SMILES.
- PubChem lookup for CAS `344423-98-9` confirmed the formula and InChI for the
  same trihydrate.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 493 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/hydrate_review.tsv` records this row as `CORRECT` with
  `MATCHES_HYDRATE` and notes that the named trihydrate is established and that
  the ChEBI identity/formula agree.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the
  synonym-enrichment proposal as already represented.

## Completeness

- The exact identifier, CAS RN, hydrate stoichiometry, formula, InChI, SMILES,
  aggregate copy, SSSOM row, and exact IUPAC synonym are populated.
- The 0/0 occurrence count is correct for a CultureBotHT-only compound not
  present in CultureMech recipe memberships.
- No components, roles, or literature references are required for this
  single-ingredient CAS import.

## Recommended Edits

- None.
