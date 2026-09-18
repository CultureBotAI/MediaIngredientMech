# `data/ingredients/mapped/Bakers_Yeast.yaml`

## Verdict

Needs curation, minor. The `FOODON:03413797` `baker's yeast` mapping, refreshed
17/17 occurrence count, provisional protein-source role, SSSOM row, and
aggregate copy pass, but the top-level `notes` still describe the obsolete
imported-unmapped state.

## Identity

- Reviewed record: `data/ingredients/mapped/Bakers_Yeast.yaml`.
- Identifier and grounding: `identifier: FOODON:03413797` with
  `ontology_mapping.ontology_id: FOODON:03413797`,
  `ontology_label: baker's yeast`, `ontology_source: FOODON`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `foodon` resolves `FOODON:03413797` to
  `baker's yeast`.
- The record denotes baker's yeast as a commercial yeast material and is
  correctly typed as `UNDEFINED_MIXTURE`, not as a single chemical.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Baicalein.yaml data/ingredients/mapped/Bakers_Yeast.yaml data/ingredients/mapped/Balhimycin.yaml data/ingredients/mapped/Bandamycin.yaml data/ingredients/mapped/Bathocuproine_Disulfonic_Acid_Disodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Bakers_Yeast.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 534 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 367 marked the
  `FOODON:03413797` mapping `CONFIRMED`; the fresh Engine A and OLS checks
  still agree with that verdict.
- Hidden/ignored-inclusive search of `mappings/culturemech_recipe_membership.tsv`
  found 17 rows for `FOODON:03413797`, matching `occurrence_statistics:
  17/17`.
- The provisional `PROTEIN_SOURCE` role is explicitly marked as a
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with review
  recommended; it is not presented as literature-backed evidence.
- The only stale claim is the top-level `notes` field: it still says this
  mim-queue import had no ontology match and needed curator review, even though
  the record was later label-exact mapped to FOODON and occurrence-refreshed.

## Completeness

- The exact FOODON identifier, raw source synonym, provisional role, occurrence
  count, SSSOM row, and aggregate copy are populated.
- No CAS, formula, InChI, SMILES, supplied form, or component list is required
  for this un-decomposed yeast material.

## Recommended Edits

- Minor: update `notes` in `data/ingredients/mapped/Bakers_Yeast.yaml` to
  describe the current exact FOODON mapping and refreshed CultureMech occurrence
  count, then run `just sync-curated`.
