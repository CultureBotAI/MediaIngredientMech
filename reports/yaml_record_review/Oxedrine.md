# `data/ingredients/mapped/Oxedrine.yaml`

## Verdict

Pass. The CultureBotHT CAS-RN `94-07-5` resolves to active `CHEBI:29081`
synephrine, and `Oxedrine` plus the exported structured synonym are genuine
same-compound labels for that term.

## Identity

- Reviewed record: `data/ingredients/mapped/Oxedrine.yaml`.
- Identifier and grounding: `identifier: CHEBI:29081` with
  `ontology_mapping.ontology_id: CHEBI:29081`, label `synephrine`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences; the record was imported from
  CultureBotHT CAS-RN `94-07-5`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps `MIM:Oxedrine` exactly
  to `CHEBI:29081`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:29081` as active `synephrine`,
  reports CAS `94-07-5`, and carries `Oxedrine` as a same-term synonym.
- The YAML formula `C9H13NO2`, InChI, and SMILES agree with the live ChEBI
  structure.
- The final SSSOM `other` values,
  `1-(4-Hydroxyphenyl)-2-(methylamino)ethanol` and `CAS:94-07-5`, are backed
  by the ChEBI exact synonym and CAS xref respectively.
- The row-review manifest already confirmed the `CHEBI:29081` ontology row.
- No roles, supplied forms, or components are asserted.

## Completeness

- The active ChEBI term, CAS-RN, formula, structure, exact synonym, and final
  SSSOM row agree.

## Recommended Edits

- None.
