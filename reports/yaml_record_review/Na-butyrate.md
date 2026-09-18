# `data/ingredients/mapped/Na-butyrate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:64103` sodium butyrate identity, CAS
provenance, structure, duplicate merge, and occurrence count pass, but both
nutrient-role facets are provisional and the final SSSOM still publishes a
concentration-qualified solution label as an unconstrained synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-butyrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:64103` with
  `ontology_mapping.ontology_id: CHEBI:64103`, label `sodium butyrate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 35 CultureMech recipe occurrences across 35 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-benzoate` through `Na-crotonate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:64103` as active `sodium butyrate`,
  with `cas:156-54-7`, formula `C4H7O2.Na`, the stored structure, and the
  accepted same-substance ChEBI synonyms.
- The #505 merge corrected the older generic-butyrate mapping by absorbing the
  duplicate `Butyrate_(sodium_Salt)` surface into this sodium butyrate record.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` are backed only by
  `COMPUTATIONAL_PREDICTION` evidence from name-pattern and automatic
  energy-source inference. Their curator notes both explicitly call the roles
  provisional.
- Major: the final SSSOM row `MIM:Na-butyrate` publishes
  `1 M Sodium butyrate` in `other`. That denotes a concentration-qualified
  solution, not sodium butyrate itself. The raw `Butyrate (sodium salt)` token is
  acceptable as a sodium-butyrate source surface.

## Completeness

- The active ChEBI target, CAS RN, formula, structure, exact synonyms, 35/35
  occurrence count, and duplicate merge agree.
- The remaining gaps are the two unsupported role facets and the single final
  SSSOM synonym that keeps solution concentration text.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-butyrate.yaml`, either remove the
  `CARBON_SOURCE` and `ENERGY_SOURCE` facets or replace the computational
  placeholders with source-backed evidence from maintained occurrence,
  role-text, or literature inputs. Rerun strict validation after the role facet
  change.
- Major: demote or remove `1 M Sodium butyrate` from the publishable exact
  synonym set, then rebuild final SSSOM and re-run final SSSOM validation plus
  product label validation.
