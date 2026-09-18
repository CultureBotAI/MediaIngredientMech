# `data/ingredients/mapped/Yeast.yaml`

## Verdict

Pass. The restored CultureMech residual grounding to the exact FoodOn yeast
label, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Yeast.yaml`.
- Identifier and grounding: `identifier: FOODON:03411345` with matching
  `ontology_mapping.ontology_id`, label `yeast`, source `FOODON`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Occurrences: three CultureMech recipe occurrences across three media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xylotriose` through `Yeast_Extract_Gluconate`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary record in this
  batch; this FoodOn row has no CHEBI/OBO adapter for that focused check.

## Evidence

- Fresh OLS4 lookup for `FOODON:03411345` returns active label `yeast`.
- The final SSSOM row correctly has
  `MIM:Yeast skos:exactMatch FOODON:03411345` with
  `MIM:culturemech:output/ingredient_occurrences.tsv` provenance.

## Issues

None.

## Completeness

- The exact FoodOn mapping, occurrence count, aggregate copy, and final SSSOM
  row agree.

## Recommended Edits

None.
