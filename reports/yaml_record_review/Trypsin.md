# `data/ingredients/mapped/Trypsin.yaml`

## Verdict

Pass. The CultureMech residual exact match, exact CHEBI identity, occurrence
count, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Trypsin.yaml`.
- Identifier and grounding: `identifier: CHEBI:9765` with matching
  `ontology_mapping.ontology_id`, label `Trypsin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Synonyms: none.
- Occurrences: 1 CultureMech recipe occurrence in 1 medium.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Triton_X-100` through `Tryptamine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 term lookup for `CHEBI:9765` returns `Trypsin` and confirms the
  target is active.
- The final SSSOM row has `MIM:Trypsin skos:exactMatch CHEBI:9765` and
  exports no `other` tokens.

## Issues

None.

## Completeness

- The CHEBI identity, source-backed occurrence count, aggregate copy, and final
  SSSOM row agree.

## Recommended Edits

None.
