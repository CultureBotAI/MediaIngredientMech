# `data/ingredients/mapped/Liver_Extract_Concentrate.yaml`

## Verdict

Needs curation. The record represents liver extract concentrate but reuses the
generic `MICRO:0001363` liver-extract identifier as an exact final SSSOM row,
and its `nutritional_roles.PROTEIN_SOURCE` facet is still provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Liver_Extract_Concentrate.yaml`.
- Identifier and grounding: `identifier: MICRO:0001363` with
  `ontology_mapping.ontology_id: MICRO:0001363`, label `liver extract`, source
  `MICRO`, `mapping_quality: LEXICAL_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file liver batch:
  exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Liver_powder.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the FOODON-grounded record. The four MICRO-grounded records were
  skipped from the CHEBI/OBO Engine A subset and checked against OLS manually.

## Evidence

- EBI OLS4 resolves `MICRO:0001363` as active `liver extract`.
- EBI OLS4 search for exact `liver extract concentrate` found no MICRO term.
- Major: `Liver extract concentrate` is source-form qualified, but the record
  uses the plain `MICRO:0001363` identifier and final SSSOM publishes an exact
  row to that generic term. The stem-substring hit needs either a local
  concentrate identity with a parent relation or a curator decision that the
  concentrate wording is not a distinct form.
- Major: `nutritional_roles.PROTEIN_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated media-role name pattern and
  says review is recommended.
- The final SSSOM row has an empty `other` field, and the aggregate
  `data/curated/mapped_ingredients.yaml` copy matches the per-record mapping and
  ten-recipe occurrence count.

## Completeness

- The undefined-mixture classification, aggregate copy, occurrence count, and
  current final SSSOM row are present.
- The generic exact mapping and provisional protein-source role need curation
  before this record is fully supported.

## Recommended Edits

- Major: remap `data/ingredients/mapped/Liver_Extract_Concentrate.yaml` so it
  no longer uses the plain liver-extract MICRO identifier as an exact identity
  if concentrate is a distinct supplied form.
- Major: either replace `nutritional_roles.PROTEIN_SOURCE` with inspected
  source evidence for exact liver extract concentrate use, or remove the
  provisional role.
- Sync the aggregate copy and regenerate final SSSOM after the YAML changes;
  rerun strict, round-trip, component, and SSSOM validation.
