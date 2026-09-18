# `data/ingredients/mapped/Tea.yaml`

## Verdict

Pass. The residual CultureMech surface `Tea` is grounded to active
`FOODON:03315081` by an exact FOODON synonym, and the aggregate row and final
SSSOM export preserve that synonym match without leaking extra `other` tokens.

## Identity

- Reviewed record: `data/ingredients/mapped/Tea.yaml`.
- Identifier and grounding: `identifier: FOODON:03315081` with
  `ontology_mapping.ontology_id: FOODON:03315081`, label `tea food product`,
  source `FOODON`, `mapping_quality: SYNONYM_MATCH`, and
  `mapping_status: MAPPED`.
- Occurrences: 2 CultureMech recipe occurrences across 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Taurine` through `Tea`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this FOODON
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `FOODON:03315081` as `tea food product`
  with exact synonym `tea`.
- The structured `ontology_mapping.evidence` cites the CultureMech occurrence
  table and records that the grounding was restored from this record's creation
  history.
- The final SSSOM has exactly one exact FOODON row for `MIM:Tea`, points at
  `FOODON:03315081`, names `obo:foodon.owl`, and publishes no unsafe `other`
  synonyms.

## Completeness

- The FOODON identity, CultureMech provenance, occurrence count, aggregate row,
  and final SSSOM row agree.
- No local components, chemistry fields, environmental contexts, or derived
  roles are required for this simple food-ingredient surface.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureMech residual
  grounding, aggregate, final SSSOM, and generated rows.

## Recommended Edits

- None.
