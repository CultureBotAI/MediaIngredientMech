# `data/ingredients/mapped/Phenylacetate.yaml`

## Verdict

Pass. The MicrobeDecoder import maps exactly to active `CHEBI:18401`
phenylacetate, and the final SSSOM row has no unsafe `other` values.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenylacetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:18401` with
  `ontology_mapping.ontology_id: CHEBI:18401`, label `phenylacetate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1 CultureMech occurrence in 1 recipe and 77 MicrobeDecoder
  occurrences from BacDive metabolite production or utilization columns.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:18401` resolves `CHEBI:18401`
  `phenylacetate`.
- The final SSSOM row was inspected directly and maps `MIM:Phenylacetate`
  exactly to `CHEBI:18401`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, SMILES, and
  InChI all describe phenylacetate, the deprotonated acid.
- The MicrobeDecoder lexical match was held for review and then promoted; the
  final SSSOM row records `manual:review-ingredients|APPROVED|2026-08-04`.
- The final SSSOM row does not export any `other` tokens.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
