# `data/ingredients/mapped/Pancreatic_Digest_of_Gelatin_Hardy_C6540.yaml`

## Verdict

Pass. The CultureMech residual record is grounded to `MICRO:0000466`
`pancreatic digest of gelatin`, carries the occurrence-table evidence needed
for that grounding, and publishes a clean exact SSSOM row.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Pancreatic_Digest_of_Gelatin_Hardy_C6540.yaml`.
- Identifier and grounding: `identifier: MICRO:0000466` with
  `ontology_mapping.ontology_id: MICRO:0000466`, label
  `pancreatic digest of gelatin`, source `MICRO`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Occurrences: 1 CultureMech occurrence in 1 recipe.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Pancreatic Digest of Gelatin` resolves
  `MICRO:0000466` `pancreatic digest of gelatin`.
- The final SSSOM row was inspected directly and maps
  `MIM:Pancreatic_Digest_of_Gelatin_Hardy_C6540` exactly to `MICRO:0000466`
  with no `other` tokens.

## Evidence

- The CultureMech residual grounding provenance says this record was created
  from the occurrence table on an exact match to an exact ontology synonym, and
  the restored `ontology_mapping.evidence` now carries the same source into the
  structured mapping field consumed by the SSSOM builder.
- There are no components, roles, synonyms, or chemical properties requiring
  additional source support.

## Completeness

- The MICRO term is enough for this imported pancreatic-digest identity.
- The `Hardy C6540` qualifier is preserved only in the MIM source label; it is
  not exported as an ontology or `other` synonym.

## Recommended Edits

- None.
