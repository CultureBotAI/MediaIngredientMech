# `data/ingredients/mapped/Na-orotate.yaml`

## Verdict

Pass. The record asserts active `CHEBI:132101` sodium orotate, stores the
matching CAS-backed structure, carries accepted same-substance synonyms, and
publishes a clean final SSSOM exact row.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-orotate.yaml`.
- Identifier and grounding: `identifier: CHEBI:132101` with
  `ontology_mapping.ontology_id: CHEBI:132101`, label `sodium orotate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 3 CultureMech recipe occurrences across 3 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-orotate` through `Na-silicate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:132101` as active `sodium orotate`,
  with `cas:154-85-8`, formula `C5H3N2O4.Na`, the stored structure, and the
  accepted orotate synonyms.
- The final SSSOM row for `MIM:Na-orotate` maps exactly to `CHEBI:132101` and
  publishes only true same-substance labels plus `CAS:154-85-8` in `other`.

## Completeness

- The active ChEBI target, CAS RN, formula, structure, exact synonyms, 3/3
  occurrence count, and final exact mapping row agree.
- No media role facets, mixture members, or component decomposition are expected
  for this single-ingredient salt record.

## Recommended Edits

- None.
