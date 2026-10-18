# `data/ingredients/mapped/Vitamins-solution.yaml`

## Verdict

Pass. This hyphenated stock-solution spelling is a rejected tombstone for the
live `Vitamins_solution` record; the aggregate row is synchronized and the
final SSSOM correctly omits the tombstone subject.

## Identity

- Reviewed record: `data/ingredients/mapped/Vitamins-solution.yaml`.
- Tombstone target: `identifier: kgmicrobe.ingredient:vitamins_solution` with
  matching `ontology_mapping.ontology_id` and label `Vitamins solution`.
- `mapping_status: REJECTED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: VITAMIN_MIX`.
- Synonyms: one raw `mim-queue` surface form, `Vitamins-solution`.
- Occurrences: zero.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vitamin_K1` through `Vitamins-solution`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary record in this
  batch; this rejected local tombstone has no OBO adapter for that focused
  check.

## Evidence

- The `2026-08-07` curation history merged this record into
  `kgmicrobe.ingredient:vitamins_solution` because `Vitamins-solution` and
  `Vitamins solution` denoted the same named preparation under hyphenated and
  unhyphenated spellings.
- The `2026-08-15` tombstone repair repointed both the record identifier and
  ontology identifier to the live `Vitamins_solution` target.
- The final SSSOM has no `MIM:Vitamins-solution` row.
- The live final row for `MIM:Vitamins_Solution` retains `Vitamins-solution` as
  an alternate `other` label on the surviving exact local registry row.

## Issues

None.

## Completeness

- The rejected status, tombstone pointer, aggregate copy, and final SSSOM
  omission agree.

## Recommended Edits

None.
