# `data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml`

## Verdict

Needs curation - major. The local stock-solution identity and close
`NCIT:C29321` phosphate-buffer parent pass, but the `BUFFER` role is
provisional and final SSSOM publishes concentration and pH-specific buffer
formulations as synonyms of the generic sodium phosphate buffer subject.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:sodium_phosphate_buffer` with
  `ontology_mapping.ontology_id: NCIT:C29321`, label `Phosphate Buffer`, source
  `NCIT`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Occurrences: 19 source occurrences across 19 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Perchlorate` through `Sodium_Phosphate_Buffer`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this NCIT-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `NCIT:C29321` with label
  `Phosphate Buffer`, agreeing with the stored close parent.
- The exact kg-microbe registry row correctly preserves the local sodium
  phosphate buffer identity alongside the close NCIT parent row.
- Major: final SSSOM publishes `10 mM` and `25 mM` pH-qualified formulations in
  `other`. Those raw occurrence forms describe narrower prepared buffers, not
  exact synonyms of the generic sodium phosphate buffer subject.
- Major: `physicochemical_roles.BUFFER` is backed only by
  `reference_type: COMPUTATIONAL_PREDICTION` from a curated name-pattern rule
  with a `review recommended` note.

## Completeness

- The local identifier, NCIT parent, occurrence count, and exact registry row
  agree.
- The consequential gaps are the concentration-qualified final synonyms and the
  unsupported role facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml`, retype or
  suppress the four concentration and pH-qualified CultureMech surface forms so
  final SSSOM no longer emits them in `other`.
- Major: remove `physicochemical_roles.BUFFER` unless the buffer role is
  supported by checked source evidence for this record.
