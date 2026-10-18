# `data/ingredients/mapped/Vitox.yaml`

## Verdict

Pass. The local Vitox identity, fallback registry grounding, aggregate row, and
final exact SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vitox.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:vitox` with
  matching `ontology_mapping.ontology_id`, label `Vitox`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- `ingredient_type: STOCK_SOLUTION` and `solution_type: OTHER`.
- Synonyms: one raw `mim-queue` surface form, `Vitox`.
- Occurrences: four CultureMech recipe occurrences across four media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vitamins` through `Voso4_X_5_H2o`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary records in this
  batch; this local `kgmicrobe.ingredient` row has no OBO adapter for that
  focused check.

## Evidence

- The `#288` curation history records this as a named multi-component
  preparation that had no exact CHEBI, NCIT, MeSH, FOODON, or ENVO term and
  should keep a local fallback identifier.
- The final SSSOM correctly exports
  `MIM:Vitox skos:exactMatch kgmicrobe.ingredient:vitox`.
- The raw duplicate label is not exported into final SSSOM `other`.

## Issues

None.

## Completeness

- The local exact identity, stock-solution classification, aggregate copy,
  occurrence count, and final SSSOM row agree.

## Recommended Edits

None.
