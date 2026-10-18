# `data/ingredients/mapped/Novobiocin.yaml`

## Verdict

Pass. The MicrobeDecoder `Novobiocin` record exact-maps to active
`CHEBI:28368` with matching structure data and no final SSSOM synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Novobiocin.yaml`.
- Identifier and grounding: `identifier: CHEBI:28368` with
  `ontology_mapping.ontology_id: CHEBI:28368`, label `novobiocin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 394 MicrobeDecoder source-column occurrences and zero
  CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:28368` as active `novobiocin` with
  formula `C31H36N2O11` and the same InChI and SMILES as the record.
- The final SSSOM row maps `MIM:Novobiocin` exactly to `CHEBI:28368`, has no
  `other` tokens, and carries the manual MicrobeDecoder review stamp.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, canonical label, formula, structure, and final
  SSSOM row agree.
- No optional slots are missing for the reviewed MicrobeDecoder trait import.

## Recommended Edits

- None.
