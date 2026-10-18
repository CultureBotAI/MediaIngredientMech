# `data/ingredients/mapped/X10_Jamarin_S.yaml`

## Verdict

Pass. The local X10 Jamarin S identity, fallback registry grounding, aggregate
row, occurrence count, and final exact SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/X10_Jamarin_S.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:x10_jamarin_s`
  with matching `ontology_mapping.ontology_id`, label `X10 Jamarin S`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- `ingredient_type: STOCK_SOLUTION` and `solution_type: OTHER`.
- Synonyms: one raw `mim-queue` surface form, `X10 Jamarin S`.
- Occurrences: two CultureMech recipe occurrences across two media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Wolfes_Vitamin_Mix` through `Xanthine`: exited 0 and wrote zero ERROR rows.
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
  `MIM:X10_Jamarin_S skos:exactMatch kgmicrobe.ingredient:x10_jamarin_s`.
- The raw duplicate label is not exported into final SSSOM `other`.

## Issues

None.

## Completeness

- The local exact identity, stock-solution classification, aggregate copy,
  occurrence count, and final SSSOM row agree.

## Recommended Edits

None.
