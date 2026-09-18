# `data/ingredients/mapped/Na-stearate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:132109` sodium octadecanoate identity,
CAS-backed structure, occurrence count, synonyms, and final SSSOM row pass, but
the `SURFACTANT` facet is still backed only by provisional ChEBI-ancestry
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-stearate.yaml`.
- Identifier and grounding: `identifier: CHEBI:132109` with
  `ontology_mapping.ontology_id: CHEBI:132109`, label `sodium octadecanoate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 3 CultureMech recipe occurrences across 3 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-stearate` through `Na2-edta`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:132109` as active
  `sodium octadecanoate`, with `cas:822-16-2`, formula `C18H35O2.Na`, the stored
  structure, and the accepted same-substance stearate synonyms.
- The final SSSOM exact row for `MIM:Na-stearate` keeps only true
  same-substance labels and the CAS token in `other`.
- Major: `physicochemical_roles.SURFACTANT` is backed only by
  `COMPUTATIONAL_PREDICTION` from ChEBI ancestry/has-role closure. The curator
  note marks it provisional and recommends review.

## Completeness

- The active ChEBI target, CAS RN, formula, structure, exact synonyms, 3/3
  occurrence count, and final exact mapping row agree.
- The only consequential gap is the unsupported `SURFACTANT` role facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-stearate.yaml`, either remove
  `physicochemical_roles.SURFACTANT` or replace its ChEBI-ancestry placeholder
  with source-backed evidence from a maintained role-text or literature input.
  Rerun strict validation and the role/output SSSOM checks after the role facet
  changes.
