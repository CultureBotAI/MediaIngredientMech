# `data/ingredients/mapped/Manganese.yaml`

## Verdict

Pass. The MicrobeDecoder exact NCIT element identity, reviewed promotion,
occurrence counts, empty `other` field, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Manganese.yaml`.
- Identifier and grounding: `identifier: NCIT:C624` with
  `ontology_mapping.ontology_id: NCIT:C624`, label `Manganese`, source
  `NCIT`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: two total occurrences in two CultureMech recipes and four
  MicrobeDecoder `BacDive_Metabolite_utilization` source occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mandelic_Acid` through `Mannitol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  NCIT-primary record.

## Evidence

- EBI OLS4 resolves `NCIT:C624` as active `Manganese`, an element with atomic
  symbol `Mn`, atomic number 25, CAS `7439-96-5`, and linked ChEBI ids
  `CHEBI:18291` and `CHEBI:35154`.
- The 2026-08-04 MicrobeDecoder review promoted the auto-grounding after the
  local OAK adapter resolved the id and canonical label.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Manganese` to
  `NCIT:C624` with an empty `other` field.

## Completeness

- The CultureMech and MicrobeDecoder occurrence counts are both preserved.
- No unsupported roles or stale synonyms publish for this record.

## Recommended Edits

- None.
