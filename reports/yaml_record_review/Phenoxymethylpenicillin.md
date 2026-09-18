# `data/ingredients/mapped/Phenoxymethylpenicillin.yaml`

## Verdict

Pass. The MicrobeDecoder import maps exactly to active `CHEBI:27446`
phenoxymethylpenicillin, and the final SSSOM row has no unsafe `other` values.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenoxymethylpenicillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:27446` with
  `ontology_mapping.ontology_id: CHEBI:27446`, label
  `phenoxymethylpenicillin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1 MicrobeDecoder `BacDive_Antibiotic_resistance` occurrence
  and no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:27446` resolves `CHEBI:27446`
  `phenoxymethylpenicillin`.
- The final SSSOM row was inspected directly and maps
  `MIM:Phenoxymethylpenicillin` exactly to `CHEBI:27446`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, SMILES, and
  InChI all describe phenoxymethylpenicillin.
- The MicrobeDecoder lexical match was held for review and then promoted; the
  final SSSOM row records `manual:review-ingredients|APPROVED|2026-08-04`.
- The final SSSOM row does not export any `other` tokens.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
