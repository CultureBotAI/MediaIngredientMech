# `data/ingredients/mapped/Orthophosphate.yaml`

## Verdict

Pass. `Orthophosphate` is an exact synonym for active `CHEBI:18367`
phosphate(3-), and the final SSSOM row preserves the exact-match publication
semantics without exporting note text as synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Orthophosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:18367` with
  `ontology_mapping.ontology_id: CHEBI:18367`, label `phosphate(3-)`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and no
  ingredient-type or structure assertion.
- Occurrences: three CultureMech occurrences across three media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- The final SSSOM row was inspected directly and maps
  `MIM:Orthophosphate` exactly to `CHEBI:18367`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:18367` as active `phosphate(3-)` and
  reports `Orthophosphate` as a related synonym.
- The record is explicit that the CultureMech residual grounding was made from
  an exact ontology-synonym match, not a canonical-label match, so the YAML
  provenance describes the narrower evidence path.
- The final SSSOM row carries the CultureMech occurrence source and has no
  `other` tokens to triage.
- No roles, supplied forms, components, or chemical properties are asserted.

## Completeness

- The active ChEBI term, YAML identifier, ontology mapping, occurrence counts,
  and final SSSOM object all agree.
- The final SSSOM row correctly publishes an exact match: the MIM surface is a
  synonym for the same CHEBI term, not a broader phosphate parent.

## Recommended Edits

- None.
