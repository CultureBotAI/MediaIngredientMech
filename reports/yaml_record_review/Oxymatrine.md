# `data/ingredients/mapped/Oxymatrine.yaml`

## Verdict

Pass. The CultureBotHT CAS-RN `16837-52-8` resolves to active `CHEBI:2672`,
whose current ChEBI label is `Ammothamnine` and whose related synonyms include
`Oxymatrine`.

## Identity

- Reviewed record: `data/ingredients/mapped/Oxymatrine.yaml`.
- Identifier and grounding: `identifier: CHEBI:2672` with
  `ontology_mapping.ontology_id: CHEBI:2672`, label `Ammothamnine`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences; the record was imported from
  CultureBotHT CAS-RN `16837-52-8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps `MIM:Oxymatrine`
  exactly to `CHEBI:2672`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:2672` as active `Ammothamnine`,
  reports CAS `16837-52-8`, and carries both `Oxymatrine` and `oxymatrine` as
  related synonyms.
- The YAML formula `C15H24N2O2`, InChI, and SMILES agree with the live ChEBI
  structure.
- The final SSSOM row keeps only `CAS:16837-52-8` in `other`, which matches
  the structured CAS-RN and ChEBI xref.
- The row-review manifest already confirmed the `CHEBI:2672` ontology row.
- No roles, supplied forms, or components are asserted.

## Completeness

- The active ChEBI term, CAS-RN, formula, structure, and final SSSOM row
  agree.

## Recommended Edits

- None.
