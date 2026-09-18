# `data/ingredients/mapped/Testosterone.yaml`

## Verdict

Pass. The residual CultureMech surface `testosterone` maps exactly to active
`CHEBI:17347`, and the aggregate row and final SSSOM export preserve that exact
grounding without leaking extra `other` tokens.

## Identity

- Reviewed record: `data/ingredients/mapped/Testosterone.yaml`.
- Identifier and grounding: `identifier: CHEBI:17347` with
  `ontology_mapping.ontology_id: CHEBI:17347`, label `testosterone`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: 1 CultureMech recipe occurrence in 1 medium.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tertiomycin_B` through `Tetrachloroethene`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:17347` as `testosterone`.
- The structured `ontology_mapping.evidence` cites the CultureMech occurrence
  table and records that the grounding was restored from this record's creation
  history.
- The final SSSOM has exactly one exact CHEBI row for `MIM:Testosterone`,
  points at `CHEBI:17347`, names `obo:chebi.owl`, and publishes no unsafe
  `other` synonyms.

## Completeness

- The CHEBI identity, CultureMech provenance, occurrence count, aggregate row,
  and final SSSOM row agree.
- No local components, chemical-property fields, environmental contexts, or
  derived roles are asserted.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureMech residual
  grounding, aggregate, final SSSOM, and generated rows.

## Recommended Edits

- None.
