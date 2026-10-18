# `data/ingredients/mapped/Beef.yaml`

## Verdict

Pass. The exact `NCIT:C71932` beef identity, refreshed 2/2 occurrence count,
provisional protein-source role, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Beef.yaml`.
- Identifier and grounding: `identifier: NCIT:C71932` with
  `ontology_mapping.ontology_id: NCIT:C71932`,
  `ontology_label: Beef`, `ontology_source: NCIT`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Prefix-specific OLS exact search in `ncit` resolves `NCIT:C71932` to `Beef`.
- The record denotes beef as meat from domestic cattle and is correctly typed
  as `UNDEFINED_MIXTURE`, not as a single chemical.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bathophenanthrolinedisulfonic_Acid_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Bedaquiline.yaml data/ingredients/mapped/Beef.yaml data/ingredients/mapped/Beef_Brain_Powder.yaml data/ingredients/mapped/Beef_Extract.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Beef.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 543 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` already
  records that prefix-specific OLS resolves `NCIT:C71932` exactly. The old
  `UNKNOWN_TERM` NCIT review row is a validator-prefix coverage artifact, not
  evidence of an invalid NCIT identifier.
- `rg -c` over `mappings/culturemech_recipe_membership.tsv` found two rows for
  `NCIT:C71932`, matching `occurrence_statistics: 2/2`.
- The provisional `PROTEIN_SOURCE` role is explicitly marked as a
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with review
  recommended; it is not presented as literature-backed evidence.

## Completeness

- The exact NCIT identifier, occurrence count, provisional role, SSSOM row, and
  aggregate copy are populated.
- No CAS, formula, InChI, SMILES, supplied form, or component list is required
  for this un-decomposed beef material.

## Recommended Edits

- None.
