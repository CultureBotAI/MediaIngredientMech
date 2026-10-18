# `data/ingredients/mapped/Na2-edta.yaml`

## Verdict

Needs curation - major. The `CHEBI:64734` anhydrous EDTA disodium salt identity,
CAS-backed structure, duplicate merge, occurrence count, and exact final row
pass, but the `CHELATOR` facet is provisional and final SSSOM still publishes a
malformed EDTA hydrate-like token.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2-edta.yaml`.
- Identifier and grounding: `identifier: CHEBI:64734` with
  `ontology_mapping.ontology_id: CHEBI:64734`, label
  `EDTA disodium salt (anhydrous)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 614 CultureMech recipe occurrences across 612 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-stearate` through `Na2-edta`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:64734` as active
  `EDTA disodium salt (anhydrous)`, with `cas:139-33-3`, formula
  `C10H14N2O8.2Na`, the stored structure, and the accepted ChEBI anhydrous
  disodium EDTA synonyms.
- The 2026-08-24 regrade correctly leaves the own-identifier SSSOM predicate as
  `skos:exactMatch` while recording that preferred term `Na2-EDTA` matches a
  ChEBI synonym rather than the primary label.
- Major: `physicochemical_roles.CHELATOR` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists`; the
  curator note marks it provisional and recommends review.
- Major: the final SSSOM row `MIM:Na2-edta` publishes `EDTA.Na .2H O` in
  `other`. That token is malformed and hydrate-like, not a synonym for the
  anhydrous `CHEBI:64734` salt.

## Completeness

- The active ChEBI target, canonical CAS RN, formula, structure, 614/612
  occurrence count, duplicate merge, grade repair, and final exact row agree.
- The remaining gaps are the unsupported `CHELATOR` role facet and the malformed
  EDTA token in final SSSOM `other`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2-edta.yaml`, either remove
  `physicochemical_roles.CHELATOR` or replace its name-pattern placeholder with
  source-backed evidence from a maintained role-text or literature input. Rerun
  strict validation after the role facet change.
- Major: demote `EDTA.Na .2H O` so it is no longer published as an exact
  anhydrous disodium EDTA synonym, then rebuild final SSSOM and re-run final
  SSSOM validation plus product label validation.
