# `data/ingredients/mapped/Tryptone_Peptone.yaml`

## Verdict

Pass. The manually reviewed mapping to the exact MICRO tryptone term,
undefined-mixture classification, occurrence count, aggregate row, and final
SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Tryptone_Peptone.yaml`.
- Identifier and grounding: `identifier: MICRO:0000182` with matching
  `ontology_mapping.ontology_id`, label `tryptone`, source `MICRO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Synonyms: one raw mim-queue label identical to the preferred term.
- Occurrences: 1600 CultureMech recipe occurrences in 1583 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trypticase-glucose-yeast_Extract` through `Tryptone_Peptone`: exited 0 and
  wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh MICRO-scoped OLS4 exact search for `tryptone` resolves `MICRO:0000182`
  with label `tryptone`.
- The final SSSOM row has
  `MIM:Tryptone_Peptone skos:exactMatch MICRO:0000182` and exports no
  `other` tokens.

## Issues

None.

## Completeness

- The MICRO identity, occurrence count, aggregate copy, and final SSSOM row
  agree.
- The duplicate-identifier baseline already tracks that `MICRO:0000182`
  currently has several exact MIM subjects whose own-ID/member semantics remain
  undecided.

## Recommended Edits

None for this record specifically.
