# `data/ingredients/mapped/Na-gallate.yaml`

## Verdict

Pass. The record asserts active `CHEBI:115197` sodium gallate, stores the
matching CAS-backed structure, carries no unsupported role facets, and publishes
a clean final SSSOM exact row.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-gallate.yaml`.
- Identifier and grounding: `identifier: CHEBI:115197` with
  `ontology_mapping.ontology_id: CHEBI:115197`, label `sodium gallate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2 CultureMech recipe occurrences across 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-formate` through `Na-laurate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- Fresh OLS4 and OAK lookups resolve `CHEBI:115197` as active
  `sodium gallate`, with `cas:2053-21-6`, formula `C7H5O5.Na`, the stored
  structure, and `sodium 3,4,5-trihydroxybenzoate` as an accepted ChEBI synonym.
- The final SSSOM row for `MIM:Na-gallate` maps exactly to `CHEBI:115197` and
  publishes only the accepted IUPAC synonym plus `CAS:2053-21-6` in `other`.

## Completeness

- The active ChEBI target, CAS RN, formula, structure, exact synonym, 2/2
  occurrence count, and final exact mapping row agree.
- No media role facets, mixture members, or component decomposition are expected
  for this single-ingredient salt record.

## Recommended Edits

- None.
