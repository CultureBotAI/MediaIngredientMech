# `data/ingredients/mapped/Pefloxacin.yaml`

## Verdict

Pass. The MicrobeDecoder import maps exactly to active `CHEBI:50199`
pefloxacin, and the final SSSOM row has no unsafe `other` values.

## Identity

- Reviewed record: `data/ingredients/mapped/Pefloxacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:50199` with
  `ontology_mapping.ontology_id: CHEBI:50199`, label `pefloxacin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1 MicrobeDecoder `BacDive_Antibiotic_sensitivity` occurrence
  and no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:50199` resolves `CHEBI:50199`
  `pefloxacin`.
- The final SSSOM row was inspected directly and maps `MIM:Pefloxacin` exactly
  to `CHEBI:50199`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, SMILES, and
  InChI all describe pefloxacin.
- The MicrobeDecoder lexical match was held for review and then promoted; the
  final SSSOM row records `manual:review-ingredients|APPROVED|2026-08-04`.
- The final SSSOM row does not export any `other` tokens.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
