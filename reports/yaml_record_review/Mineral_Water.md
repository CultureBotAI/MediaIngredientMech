# `data/ingredients/mapped/Mineral_Water.yaml`

## Verdict

Pass. The exact `FOODON:03301328` mineral water identity, OLS row-review
confirmation, occurrence count, undefined-mixture type, and final SSSOM row
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mineral_Water.yaml`.
- Identifier and grounding: `identifier: FOODON:03301328` with
  `ontology_mapping.ontology_id: FOODON:03301328`, label `mineral water`,
  source `FOODON`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mineral_3B_Solution_Minus_Phosphorus` through `Minerals`: exited 0 and
  wrote zero ERROR rows.
- Direct CHEBI-focused LinkML term validation was skipped for this FOODON
  record in the mixed batch.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm
  `MIM:Mineral_Water` to `FOODON:03301328`.
- A fresh FOODON-scoped EBI OLS4 exact lookup resolves `FOODON:03301328` as
  active `mineral water`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mineral_Water` to `FOODON:03301328` with empty `other`.

## Completeness

- The FOODON identity, undefined-mixture type, 1/1 occurrence count, and final
  row agree.
- The record does not publish raw synonyms or unsupported roles.

## Recommended Edits

- None.
