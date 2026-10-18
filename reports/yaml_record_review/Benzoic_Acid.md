# `data/ingredients/mapped/Benzoic_Acid.yaml`

## Verdict

Pass. The exact `CHEBI:30746` neutral benzoic-acid identity, CultureBotHT CAS
value, formula, InChI, SMILES, refreshed 9/9 occurrence count, SSSOM row, and
aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Benzoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30746` with
  `ontology_mapping.ontology_id: CHEBI:30746`,
  `ontology_label: benzoic acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `chebi` resolves `CHEBI:30746` to `benzoic acid`.
- PubChem resolves CAS `65-85-0` to formula `C7H6O2` and the same standard
  InChI stored under `chemical_properties`.
- The record denotes neutral benzoic acid, not the `CHEBI:16150` benzoate
  conjugate base reviewed separately.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Benzbromarone.yaml data/ingredients/mapped/Benzene.yaml data/ingredients/mapped/Benzethonium_Chloride.yaml data/ingredients/mapped/Benzoate.yaml data/ingredients/mapped/Benzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Benzoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 557 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 384 marked the
  `CHEBI:30746` mapping `CONFIRMED`; the fresh Engine A and OLS checks still
  agree with that verdict.
- PubChem confirms that the CAS-backed compound carries the same formula and
  InChI as the stored CultureBotHT/ChEBI chemistry.
- `rg -c` over `mappings/culturemech_recipe_membership.tsv` found nine rows
  for `CHEBI:30746`, matching `occurrence_statistics: 9/9`.

## Completeness

- The exact CHEBI identifier, CAS registry number, formula, InChI, SMILES,
  occurrence count, SSSOM row, and aggregate copy are populated.
- No role, component list, or supplied-form split is required for this
  single-compound record.

## Recommended Edits

- None.
