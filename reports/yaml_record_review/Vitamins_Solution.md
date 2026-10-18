# `data/ingredients/mapped/Vitamins_Solution.yaml`

## Verdict

Pass. The local Vitamins solution identity, fallback registry grounding,
aggregate row, hyphenated synonym, and final exact SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vitamins_Solution.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:vitamins_solution`
  with matching `ontology_mapping.ontology_id`, label `Vitamins solution`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- `ingredient_type: STOCK_SOLUTION` and `solution_type: VITAMIN_MIX`.
- Synonyms: raw `Vitamins solution` plus the merged alternate spelling
  `Vitamins-solution`.
- Occurrences: two CultureMech recipe occurrences across two media.

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
  `MIM:Vitamins_Solution skos:exactMatch kgmicrobe.ingredient:vitamins_solution`.
- `Vitamins-solution` is a legitimate spelling variant from a merged duplicate
  record and is retained as final SSSOM `other`.

## Issues

None.

## Completeness

- The local exact identity, solution classification, aggregate copy, occurrence
  count, and final SSSOM row agree.

## Recommended Edits

None.
