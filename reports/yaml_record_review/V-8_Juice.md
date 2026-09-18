# `data/ingredients/mapped/V-8_Juice.yaml`

## Verdict

Pass. The local V-8 Juice identity, FOODON parent, aggregate row, and paired
final SSSOM rows pass.

## Identity

- Reviewed record: `data/ingredients/mapped/V-8_Juice.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:v-8_juice` with a
  `FOODON:03400264` parent grounding to `vegetable juice (us cfr)`, source
  `FOODON`, `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- The local identifier preserves exact V-8 Juice identity because the old
  `MICRO:0002250` term was an OLS4 non-defining MicrO IRI.
- Occurrences: three CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Uridine_5-monophosphate_Disodium_Salt` through `V-8_Juice`: exited 0 and
  wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch;
  this local `kgmicrobe.ingredient` row has no OBO adapter for that focused
  check.

## Evidence

- Fresh OLS4 lookup for `FOODON:03400264` returns active label
  `vegetable juice (us cfr)`, which is a suitable broader anchor for V-8 Juice
  but not an exact V-8 Juice identity.
- The final SSSOM exports both the intended parent row,
  `MIM:V-8_Juice skos:narrowMatch FOODON:03400264`, and an exact local
  registry row preserving `kgmicrobe.ingredient:v-8_juice`.
- The final rows do not export the record's raw duplicate `V-8 Juice` synonym
  or the broader FOODON synonym into `other`.

## Issues

None.

## Completeness

- The local exact identity, FOODON parent, aggregate copy, occurrence count, and
  paired final SSSOM rows agree.

## Recommended Edits

None.
