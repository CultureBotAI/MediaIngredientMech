# `data/ingredients/mapped/Phenylethylamine.yaml`

## Verdict

Pass. The MicrobeDecoder import maps exactly to active `CHEBI:50048`
phenylethylamine, and the final SSSOM row has no unsafe `other` values.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenylethylamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:50048` with
  `ontology_mapping.ontology_id: CHEBI:50048`, label `phenylethylamine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2 MicrobeDecoder occurrences from the BacDive metabolite
  utilization column and no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:50048` resolves `CHEBI:50048`
  `phenylethylamine`.
- The final SSSOM row was inspected directly and maps `MIM:Phenylethylamine`
  exactly to `CHEBI:50048`.

## Evidence

- The MicrobeDecoder lexical match was held for review and then promoted; the
  final SSSOM row records `manual:review-ingredients|APPROVED|2026-08-04`.
- The CHEBI primary identifier and mapping target are for phenylethylamine, not
  the neighboring hydrochloride record that now maps to `CHEBI:18397`
  2-phenylethylamine.
- The final SSSOM row does not export any `other` tokens.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
