# `data/ingredients/mapped/Na-formate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:62965` sodium formate identity,
CAS-backed structure, occurrence count, synonym merge, and core final SSSOM row
pass, but both nutrient-role facets are provisional and final SSSOM publishes a
catalog-qualified surface as an unconstrained synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-formate.yaml`.
- Identifier and grounding: `identifier: CHEBI:62965` with
  `ontology_mapping.ontology_id: CHEBI:62965`, label `sodium formate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 222 CultureMech recipe occurrences across 222 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-formate` through `Na-laurate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- Fresh OLS4 and OAK lookups resolve `CHEBI:62965` as active `sodium formate`,
  with `cas:141-53-7`, formula `CHO2.Na`, the stored structure, and the accepted
  formate synonyms.
- The #337 occurrence refresh and #520 CultureMech alias backfill agree with the
  222/222 occurrence count and the single `Sodium formate (Wako)` recipe surface.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` are backed only by
  `COMPUTATIONAL_PREDICTION` evidence from name-pattern and automatic
  energy-source inference. Their curator notes both explicitly call the roles
  provisional.
- Major: the final SSSOM row `MIM:Na-formate` publishes
  `Sodium formate (Wako)` in `other`. The YAML correctly types that raw surface
  as `CATALOG_VARIANT`, but the final SSSOM output still treats the vendor
  variant as a synonym of unconstrained sodium formate.

## Completeness

- The active ChEBI target, CAS RN, formula, structure, exact synonyms, 222/222
  occurrence count, duplicate merge, and source alias backfill agree.
- The remaining gaps are the two unsupported role facets and the single final
  SSSOM `other` token that keeps vendor text.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-formate.yaml`, either remove the
  `CARBON_SOURCE` and `ENERGY_SOURCE` facets or replace their computational
  placeholders with source-backed evidence from maintained occurrence,
  role-text, or literature inputs. Rerun strict validation after the role facet
  change.
- Major: keep `Sodium formate (Wako)` as a non-published catalog surface rather
  than a final SSSOM `other` synonym, then rebuild final SSSOM and re-run final
  SSSOM validation plus product label validation.
