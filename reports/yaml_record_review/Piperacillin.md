# `data/ingredients/mapped/Piperacillin.yaml`

## Verdict

Pass. The MicrobeDecoder import maps exactly to active `CHEBI:8232`
piperacillin, and the final SSSOM row has no unsafe `other` values.

## Identity

- Reviewed record: `data/ingredients/mapped/Piperacillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:8232` with
  `ontology_mapping.ontology_id: CHEBI:8232`, label `piperacillin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 42 MicrobeDecoder occurrences from BacDive antibiotic resistance
  or sensitivity columns and no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:8232` resolves `CHEBI:8232`
  `piperacillin`.
- The final SSSOM row was inspected directly and maps `MIM:Piperacillin`
  exactly to `CHEBI:8232`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, SMILES, and
  InChI all describe piperacillin.
- The MicrobeDecoder lexical match was held for review and then promoted; the
  final SSSOM row records `manual:review-ingredients|APPROVED|2026-08-04`.
- The final SSSOM row does not export any `other` tokens.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
