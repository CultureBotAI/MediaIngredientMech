# `data/ingredients/mapped/Yeast_Extract-malt_Extract_Agar.yaml`

## Verdict

Pass. The local Yeast extract-malt extract agar identity, FoodOn malt-extract
close parent, aggregate row, and paired final SSSOM rows pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Yeast_Extract-malt_Extract_Agar.yaml`.
- Identifier and exact local identity:
  `kgmicrobe.ingredient:yeast_extract_malt_extract_agar`.
- Parent grounding: `ontology_mapping.ontology_id: FOODON:03301056`, label
  `malt extract`, source `FOODON`, and `mapping_quality: CLOSE_MATCH`.
- `mapping_status: MAPPED` and `ingredient_type: UNDEFINED_MIXTURE`.
- Synonyms: one raw `mim-queue` surface form,
  `Yeast extract-malt extract agar`.
- Occurrences: six CultureMech recipe occurrences across six media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xylotriose` through `Yeast_Extract_Gluconate`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary record in this
  batch; this local `kgmicrobe.ingredient` row has no OBO adapter for that
  focused check.

## Evidence

- Fresh OLS4 exact-label search for `malt extract` in FoodOn found active
  `FOODON:03301056`.
- The final SSSOM exports both the intended parent row,
  `MIM:Yeast_Extract-malt_Extract_Agar skos:closeMatch FOODON:03301056`, and
  an exact local registry row preserving
  `kgmicrobe.ingredient:yeast_extract_malt_extract_agar`.
- The `2026-05-05` curation history explains why a yeast-extract, malt-extract,
  and agar mixture is not identical to `malt extract`.

## Issues

None.

## Completeness

- The local exact identity, FoodOn close match, aggregate copy, occurrence
  count, and paired final SSSOM rows agree.

## Recommended Edits

None.
