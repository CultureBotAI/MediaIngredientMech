# `data/ingredients/mapped/Phenanthrene.yaml`

## Verdict

Pass. The MicrobeDecoder import maps exactly to active `CHEBI:28851`
phenanthrene, and the final SSSOM row has no unsafe `other` values.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenanthrene.yaml`.
- Identifier and grounding: `identifier: CHEBI:28851` with
  `ontology_mapping.ontology_id: CHEBI:28851`, label `phenanthrene`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1 MicrobeDecoder `BacDive_Metabolite_utilization` occurrence
  and no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:28851` resolves `CHEBI:28851`
  `phenanthrene`.
- The final SSSOM row was inspected directly and maps `MIM:Phenanthrene`
  exactly to `CHEBI:28851`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, SMILES, and
  InChI all describe phenanthrene.
- The MicrobeDecoder lexical match was held for review and then promoted; the
  final SSSOM row records `manual:review-ingredients|APPROVED|2026-08-04`.
- The final SSSOM row does not export any `other` tokens.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
