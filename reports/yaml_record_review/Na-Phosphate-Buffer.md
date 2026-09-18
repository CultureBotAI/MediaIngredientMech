# `data/ingredients/mapped/Na-Phosphate-Buffer.yaml`

## Verdict

Pass. This duplicate sodium phosphate buffer tombstone points at the live
`kgmicrobe.ingredient:na-phosphate_buffer` winner and is correctly absent from
the final SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-Phosphate-Buffer.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:na-phosphate_buffer` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:na-phosphate_buffer`,
  label `Na-phosphate buffer`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: REJECTED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Occurrences: zero occurrences after transfer into the live
  `Na-phosphate buffer` record.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-3-hydroxybutyrate` through `Na-ascorbate`: exited 0 and wrote zero ERROR
  rows.
- Engine A term validation was skipped for this non-OBO
  `kgmicrobe.ingredient` target; the repository's prefilter rejects the file
  before OAK tries to open an empty local-registry sqlite adapter.

## Evidence

- `mappings/unmapped_ingredients_ols_exact_audit.tsv` records no exact OLS hit
  for the original `UNMAPPED_0462` label.
- The #288 curation history records the fallback registry decision for sodium
  phosphate buffer, and the #360 events repointed this tombstone to the live
  underscore-form target after its duplicate was merged.
- A fresh ignored/hidden-inclusive search of
  `mappings/ingredient_mappings.sssom.tsv` found no final
  `MIM:Na-Phosphate-Buffer` row; only the live `MIM:Na-phosphate_Buffer` row
  remains and retains this punctuation variant in `other`.

## Completeness

- The rejected status, tombstone target, label-index entries, occurrence count,
  and final SSSOM suppression agree.
- The old stock-solution details are preserved in history; this tombstone does
  not need a component list.

## Recommended Edits

- None.
