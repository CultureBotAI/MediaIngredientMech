# `data/ingredients/mapped/Benzbromarone.yaml`

## Verdict

Pass. The exact `CHEBI:3023` identity, CultureBotHT CAS value, ChEBI exact
synonym, formula, InChI, SMILES, SSSOM row, and aggregate copy all describe
benzbromarone.

## Identity

- Reviewed record: `data/ingredients/mapped/Benzbromarone.yaml`.
- Identifier and grounding: `identifier: CHEBI:3023` with
  `ontology_mapping.ontology_id: CHEBI:3023`,
  `ontology_label: benzbromarone`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `chebi` resolves `CHEBI:3023` to `benzbromarone` and
  returns the stored systematic name as an exact synonym.
- PubChem resolves CAS `3562-84-3` to formula `C17H12Br2O3` and the same
  standard InChI stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Benzbromarone.yaml data/ingredients/mapped/Benzene.yaml data/ingredients/mapped/Benzethonium_Chloride.yaml data/ingredients/mapped/Benzoate.yaml data/ingredients/mapped/Benzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Benzbromarone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 553 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 382 marked the
  `CHEBI:3023` mapping `CONFIRMED`; the fresh Engine A and OLS checks still
  agree with that verdict.
- PubChem confirms that the CAS-backed compound carries the same formula and
  InChI as the stored CultureBotHT/ChEBI chemistry.

## Completeness

- The exact CHEBI identifier, CAS registry number, formula, InChI, SMILES,
  ChEBI exact synonym, SSSOM row, and aggregate copy are populated.
- No source occurrence, role, component list, or supplied-form split is required
  for this single-compound record with zero recorded medium occurrences.

## Recommended Edits

- None.
