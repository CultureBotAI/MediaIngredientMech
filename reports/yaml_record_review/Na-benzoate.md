# `data/ingredients/mapped/Na-benzoate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:113455` sodium benzoate identity,
CAS-backed structure, occurrence count, synonyms, and final SSSOM row pass, but
the `CARBON_SOURCE` facet is still an unsupported provisional LLM assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-benzoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:113455` with
  `ontology_mapping.ontology_id: CHEBI:113455`, label `sodium benzoate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 50 CultureMech recipe occurrences across 50 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-benzoate` through `Na-crotonate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:113455` as active `sodium benzoate`,
  with `cas:532-32-1`, formula `C7H5O2.Na`, the stored sodium-benzoate
  structure, and the accepted same-substance ChEBI synonyms.
- The final SSSOM exact row for `MIM:Na-benzoate` keeps only true
  same-substance labels and the CAS token in `other`; the raw `Properties: ...`
  CultureMech strings are correctly filtered from the published synonym set.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by a
  `COMPUTATIONAL_PREDICTION` whose curator note calls it a provisional
  in-session LLM assignment. No inspected source in this record supports sodium
  benzoate's use as a carbon source.

## Completeness

- The active ChEBI target, CAS RN, structure, exact synonyms, 50/50 occurrence
  count, duplicate merge, and final exact mapping row agree.
- No final SSSOM cleanup is needed for this record; only the provisional role
  facet is unsupported.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-benzoate.yaml`, either remove
  `nutritional_roles.CARBON_SOURCE` or replace its computational placeholder
  with source-backed evidence from the maintained CultureMech occurrence or
  literature input that specifically says sodium benzoate serves as a carbon
  source. Rerun strict validation and the role/output SSSOM checks after the
  role facet changes.
