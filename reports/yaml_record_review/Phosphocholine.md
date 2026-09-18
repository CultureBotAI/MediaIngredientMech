# `data/ingredients/mapped/Phosphocholine.yaml`

## Verdict

Pass. The MicrobeDecoder import maps exactly to active `CHEBI:18132`
phosphocholine, and the final SSSOM row has no unsafe `other` values.

## Identity

- Reviewed record: `data/ingredients/mapped/Phosphocholine.yaml`.
- Identifier and grounding: `identifier: CHEBI:18132` with
  `ontology_mapping.ontology_id: CHEBI:18132`, label `phosphocholine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1 MicrobeDecoder occurrence from the BacDive metabolite
  utilization column and no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:18132` resolves `CHEBI:18132`
  `phosphocholine`.
- The final SSSOM row was inspected directly and maps `MIM:Phosphocholine`
  exactly to `CHEBI:18132`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, SMILES, and
  InChI all describe phosphocholine.
- The MicrobeDecoder lexical match was held for review and then promoted; the
  final SSSOM row records `manual:review-ingredients|APPROVED|2026-08-04`.
- The final SSSOM row does not export any `other` tokens.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
