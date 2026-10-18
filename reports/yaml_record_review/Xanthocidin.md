# `data/ingredients/mapped/Xanthocidin.yaml`

## Verdict

Pass. The reviewed kg-microbe Xanthocidin placeholder, aggregate row, and final
SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Xanthocidin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:xanthocidin` with
  matching `ontology_mapping.ontology_id`, label `Xanthocidin`, source
  `kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`, and
  `mapping_status: MAPPED`.
- `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: zero.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xanthocidin` through `Xylan_From_Beechwood`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary records in this
  batch; this local `kgmicrobe.compound` row has no OBO adapter for that
  focused check.

## Evidence

- The `2026-05-10` placeholder review retained
  `kgmicrobe.compound:xanthocidin` after a no-hit OLS review found no exact
  promotion target and no normalized local mapped duplicate.
- Fresh OLS4 exact search for `Xanthocidin` still returned no hits.
- The final SSSOM correctly exports
  `MIM:Xanthocidin skos:exactMatch kgmicrobe.compound:xanthocidin` with no
  `other` labels.

## Issues

None.

## Completeness

- The local exact identity, aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
