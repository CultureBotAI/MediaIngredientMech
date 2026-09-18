# `data/ingredients/mapped/Washed_agar.yaml`

## Verdict

Pass. The restored CultureMech residual grounding to the exact MicrO washed
agar label, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Washed_agar.yaml`.
- Identifier and grounding: `identifier: MICRO:0001723` with matching
  `ontology_mapping.ontology_id`, label `washed agar`, source `MICRO`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Voso4_X_N_H2o` through `Washed_agar`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary records in this
  batch; this MicrO row has no CHEBI/OBO adapter for that focused check.

## Evidence

- Fresh OLS4 exact-label search for `washed agar` in `MICRO` found one active
  result, `MICRO:0001723`, with label `washed agar`.
- The final SSSOM row correctly has
  `MIM:Washed_agar skos:exactMatch MICRO:0001723` with
  `MIM:culturemech:output/ingredient_occurrences.tsv` provenance.

## Issues

None.

## Completeness

- The exact MicrO mapping, occurrence count, aggregate copy, and final SSSOM row
  agree.

## Recommended Edits

None.
