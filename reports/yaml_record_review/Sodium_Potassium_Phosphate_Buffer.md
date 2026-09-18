# `data/ingredients/mapped/Sodium_Potassium_Phosphate_Buffer.yaml`

## Verdict

Needs curation - major. The local stock-solution identity and close
`NCIT:C29321` phosphate-buffer parent pass, but the `BUFFER` role is still a
provisional name-pattern prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Sodium_Potassium_Phosphate_Buffer.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:sodium_potassium_phosphate_buffer` with
  `ontology_mapping.ontology_id: NCIT:C29321`, label `Phosphate Buffer`, source
  `NCIT`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Occurrences: 6 source occurrences across 6 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Phosphate_Dibasic` through `Sodium_Pyrophosphate_Dibasic`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this NCIT-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `NCIT:C29321` with label
  `Phosphate Buffer`, agreeing with the close parent row.
- Final SSSOM preserves the close NCIT parent row and exact
  `kgmicrobe.ingredient:sodium_potassium_phosphate_buffer` registry row without
  unsafe `other` payload.
- Major: `physicochemical_roles.BUFFER` is backed only by
  `reference_type: COMPUTATIONAL_PREDICTION` from a curated name-pattern rule
  with a `review recommended` note.

## Completeness

- The local identifier, NCIT parent, occurrence count, and exact registry row
  agree.
- The only consequential gap is the unsupported role facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Sodium_Potassium_Phosphate_Buffer.yaml`,
  remove `physicochemical_roles.BUFFER` unless the buffer role is supported by
  checked source evidence for this record.
