# `data/ingredients/mapped/Oxalate.yaml`

## Verdict

Pass. The MicrobeDecoder `Oxalate` label exact-matches active `CHEBI:132952`
oxalate, and the record does not blur that anion identity with oxalic acid or
with any oxalate salt.

## Identity

- Reviewed record: `data/ingredients/mapped/Oxalate.yaml`.
- Identifier and grounding: `identifier: CHEBI:132952` with
  `ontology_mapping.ontology_id: CHEBI:132952`, label `oxalate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: two MicrobeDecoder `BacDive_Metabolite_utilization`
  source-column occurrences and zero CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps `MIM:Oxalate` exactly to
  `CHEBI:132952`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:132952` as active `oxalate`, a
  dicarboxylic-acid anion of oxalic acid, matching the record's exact
  MicrobeDecoder import.
- The MicrobeDecoder review table approved the exact label match before
  publication, and the final SSSOM row carries that review stamp.
- No final `other` tokens are present, so the record does not export broader
  oxalic-acid or salt labels as synonyms of the oxalate anion.
- No roles, supplied forms, components, or chemistry fields are asserted.

## Completeness

- The active ChEBI term, source occurrence count, and final SSSOM row agree.
- Separate oxalic-acid and disodium/potassium oxalate records remain separate
  in the corpus.

## Recommended Edits

- None.
