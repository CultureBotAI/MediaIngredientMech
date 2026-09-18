# `data/ingredients/mapped/Na-pyruvate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:50144` sodium pyruvate identity,
CAS-backed structure, source-backed carbon role, occurrence count, duplicate
merge, and dead-ID repair pass, but `ENERGY_SOURCE` is provisional and final
SSSOM still publishes a concentration-qualified solution label.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-pyruvate.yaml`.
- Identifier and grounding: `identifier: CHEBI:50144` with
  `ontology_mapping.ontology_id: CHEBI:50144`, label `sodium pyruvate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 807 CultureMech recipe occurrences across 805 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-orotate` through `Na-silicate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:50144` as active `sodium pyruvate`,
  with `cas:113-24-6`, formula `C3H3O3.Na`, the stored structure, and the
  accepted same-substance ChEBI synonyms.
- The 2026-04-19 repair corrected the transient unrelated `CHEBI:113246`
  pyruvate overclaim to `CHEBI:50144`, and the current synonym list no longer
  includes the contaminated triazine label recorded in history.
- The `CARBON_SOURCE` facet is source-backed by CultureMech original role text
  that explicitly says `Carbon source`.
- Major: `nutritional_roles.ENERGY_SOURCE` is backed only by automatic
  `COMPUTATIONAL_PREDICTION` evidence, and its curator note explicitly marks it
  provisional.
- Major: the final SSSOM row `MIM:Na-pyruvate` publishes
  `1 M Sodium pyruvate*` in `other`. That denotes a concentration-qualified
  recipe surface, not unconstrained sodium pyruvate itself.

## Completeness

- The active ChEBI target, CAS RN, formula, structure, 807/805 occurrence count,
  duplicate merge, wrong-term repair, source-backed `CARBON_SOURCE` role, and
  core final exact mapping row agree.
- The remaining gaps are the unsupported inferred energy role and the
  concentration-qualified final SSSOM synonym.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-pyruvate.yaml`, either remove
  `nutritional_roles.ENERGY_SOURCE` or replace its computational placeholder
  with source-backed evidence from maintained occurrence, role-text, or
  literature inputs. Rerun strict validation after the role facet change.
- Major: demote or remove `1 M Sodium pyruvate*` from the publishable exact
  synonym set, then rebuild final SSSOM and re-run final SSSOM validation plus
  product label validation.
