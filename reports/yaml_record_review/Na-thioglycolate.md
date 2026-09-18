# `data/ingredients/mapped/Na-thioglycolate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:86481` sodium thioglycolate identity,
CAS-backed structure, occurrence count, duplicate merge, synonyms, and final
SSSOM row pass, but the `REDUCING_AGENT` facet is still backed only by
provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-thioglycolate.yaml`.
- Identifier and grounding: `identifier: CHEBI:86481` with
  `ontology_mapping.ontology_id: CHEBI:86481`, label `sodium thioglycolate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 170 CultureMech recipe occurrences across 170 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-stearate` through `Na2-edta`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:86481` as active
  `sodium thioglycolate`, with `cas:367-51-1`, formula `C2H3O2S.Na`, the stored
  structure, and the accepted thioglycolate synonyms.
- The final SSSOM exact row for `MIM:Na-thioglycolate` keeps only true
  same-substance labels and the CAS token in `other`; raw `Properties: ...`
  strings are correctly filtered out.
- Major: `physicochemical_roles.REDUCING_AGENT` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists`; the
  curator note marks it provisional and recommends review.

## Completeness

- The active ChEBI target, CAS RN, formula, structure, exact synonyms, 170/170
  occurrence count, duplicate merge, and final exact mapping row agree.
- The only consequential gap is the unsupported `REDUCING_AGENT` role facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-thioglycolate.yaml`, either remove
  `physicochemical_roles.REDUCING_AGENT` or replace its name-pattern placeholder
  with source-backed evidence from a maintained role-text or literature input.
  Rerun strict validation and the role/output SSSOM checks after the role facet
  changes.
