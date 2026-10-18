# `data/ingredients/mapped/Na-laurate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:131839` sodium dodecanoate identity,
CAS-backed structure, occurrence count, synonyms, and final SSSOM row pass, but
the `SURFACTANT` facet is still backed only by provisional ChEBI-ancestry
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-laurate.yaml`.
- Identifier and grounding: `identifier: CHEBI:131839` with
  `ontology_mapping.ontology_id: CHEBI:131839`, label `sodium dodecanoate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 6 CultureMech recipe occurrences across 6 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-formate` through `Na-laurate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- Fresh OLS4 and OAK lookups resolve `CHEBI:131839` as active
  `sodium dodecanoate`, with `cas:629-25-4`, formula `C12H23O2.Na`, the stored
  structure, and the accepted same-substance laurate synonyms.
- The final SSSOM exact row for `MIM:Na-laurate` keeps only true
  same-substance labels and the CAS token in `other`.
- Major: `physicochemical_roles.SURFACTANT` is backed only by
  `COMPUTATIONAL_PREDICTION` from ChEBI ancestry/has-role closure. The curator
  note marks it provisional and recommends review.

## Completeness

- The active ChEBI target, CAS RN, formula, structure, exact synonyms, 6/6
  occurrence count, and final exact mapping row agree.
- The only consequential gap is the unsupported `SURFACTANT` role facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-laurate.yaml`, either remove
  `physicochemical_roles.SURFACTANT` or replace its ChEBI-ancestry placeholder
  with source-backed evidence from a maintained role-text or literature input.
  Rerun strict validation and the role/output SSSOM checks after the role facet
  changes.
