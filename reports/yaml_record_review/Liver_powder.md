# `data/ingredients/mapped/Liver_powder.yaml`

## Verdict

Pass. The CultureMech residual exact-synonym grounding to FOODON:03000441,
one-recipe occurrence count, restored SSSOM evidence source, and final SSSOM row
are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Liver_powder.yaml`.
- Identifier and grounding: `identifier: FOODON:03000441` with
  `ontology_mapping.ontology_id: FOODON:03000441`, label
  `liver powder supplement`, source `FOODON`, `mapping_quality: SYNONYM_MATCH`,
  `match_level: NORMALIZED`, and `mapping_status: MAPPED`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file liver batch:
  exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Liver_powder.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0.

## Evidence

- EBI OLS4 resolves `FOODON:03000441` as active `liver powder supplement` and
  lists `liver powder` as a synonym.
- The final SSSOM publishes one `skos:exactMatch` row to `FOODON:03000441`,
  carries `MIM:culturemech:output/ingredient_occurrences.tsv` in `source`, and
  has an empty `other` field.
- The aggregate `data/curated/mapped_ingredients.yaml` copy matches the
  per-record identity, one-recipe occurrence count, status, and mapping.

## Completeness

- The active FOODON identity, source provenance, aggregate copy, occurrence
  count, and final SSSOM row are present and consistent.

## Recommended Edits

- None.
