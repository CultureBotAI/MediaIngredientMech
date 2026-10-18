# `data/ingredients/mapped/Na-caproate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:114126` sodium hexanoate identity,
CAS-backed structure, occurrence count, synonyms, and final SSSOM row pass, but
the `CARBON_SOURCE` facet is still backed only by provisional name-pattern
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-caproate.yaml`.
- Identifier and grounding: `identifier: CHEBI:114126` with
  `ontology_mapping.ontology_id: CHEBI:114126`, label `sodium hexanoate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 10 CultureMech recipe occurrences across 10 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-benzoate` through `Na-crotonate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:114126` as active
  `sodium hexanoate`, with `cas:10051-44-2`, formula `C6H11O2.Na`, the stored
  structure, and the accepted sodium caproate, sodium capronate, and sodium
  hexanoate synonyms.
- The final SSSOM exact row for `MIM:Na-caproate` keeps only true
  same-substance labels and the CAS token in `other`; the raw
  `Role: Carbon source` CultureMech string is correctly filtered from the
  published synonym set.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists`; the
  curator note marks it provisional and recommends review. The imported
  CultureMech raw role text was not migrated as structured source evidence.

## Completeness

- The active ChEBI target, CAS RN, formula, structure, exact synonyms, 10/10
  occurrence count, duplicate merge, and final exact mapping row agree.
- The only consequential gap is the unsupported `CARBON_SOURCE` role facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-caproate.yaml`, either remove
  `nutritional_roles.CARBON_SOURCE` or replace its name-pattern placeholder with
  source-backed evidence from the maintained CultureMech role-text input that
  says this ingredient is a carbon source. Rerun strict validation and the
  role/output SSSOM checks after the role facet changes.
