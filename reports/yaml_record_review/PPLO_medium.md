# `data/ingredients/mapped/PPLO_medium.yaml`

## Verdict

Pass. The CultureMech residual record is exactly grounded to `MICRO:0000094`
`PPLO medium`, carries the occurrence-table evidence needed for that grounding,
and publishes a clean exact SSSOM row.

## Identity

- Reviewed record: `data/ingredients/mapped/PPLO_medium.yaml`.
- Identifier and grounding: `identifier: MICRO:0000094` with
  `ontology_mapping.ontology_id: MICRO:0000094`, label `PPLO medium`, source
  `MICRO`, `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Occurrences: 2 CultureMech occurrences across 2 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 lookup resolves `MICRO:0000094` as active `PPLO medium`.
- The final SSSOM row was inspected directly and maps `MIM:PPLO_medium`
  exactly to `MICRO:0000094` with no `other` tokens.

## Evidence

- The CultureMech residual grounding provenance says this record was created
  from the occurrence table on an exact match to the ontology label, and the
  restored `ontology_mapping.evidence` now carries the same source into the
  structured mapping field consumed by the SSSOM builder.
- There are no components, roles, synonyms, or chemical properties requiring
  additional source support.

## Completeness

- The exact MICRO term is enough for this imported medium identity.
- No optional fields are being filled speculatively.

## Recommended Edits

- None.
