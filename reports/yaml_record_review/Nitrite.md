# `data/ingredients/mapped/Nitrite.yaml`

## Verdict

Pass. The MicrobeDecoder `Nitrite` record exact-maps to active
`CHEBI:16301` nitrite with matching structure data and no final SSSOM synonym
payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Nitrite.yaml`.
- Identifier and grounding: `identifier: CHEBI:16301` with
  `ontology_mapping.ontology_id: CHEBI:16301`, label `nitrite`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 319 MicrobeDecoder source-column occurrences and zero
  CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:16301` as active `nitrite` with
  formula `NO2`, CAS `14797-65-0`, InChI
  `InChI=1S/HNO2/c2-1-3/h(H,2,3)/p-1`, and SMILES `O=N[O-]`, matching the
  record.
- The final SSSOM row maps `MIM:Nitrite` exactly to `CHEBI:16301`, has no
  `other` tokens, and carries the manual MicrobeDecoder review stamp.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, canonical label, formula, structure, and final
  SSSOM row agree.
- No optional slots are missing for the reviewed MicrobeDecoder trait import.

## Recommended Edits

- None.
