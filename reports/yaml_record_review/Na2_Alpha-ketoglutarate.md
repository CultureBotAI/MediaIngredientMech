# `data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml`

## Verdict

Needs curation - major. The #315 salt/anion repair correctly keeps `Na2
alpha-ketoglutarate` as a local `kgmicrobe.compound` identity with
`CHEBI:30915` as the ChEBI acid parent, and the final SSSOM emits both the
parent and local registry rows, but both nutrient-role facets are provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:na2_alpha-ketoglutarate` with
  `ontology_mapping.ontology_id: CHEBI:30915`, label `2-oxoglutaric acid`,
  source `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 4 CultureMech recipe occurrences across 4 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2_Alpha-ketoglutarate` through `Na2co3`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for the
  `CHEBI:30915` parent label.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:30915` as active
  `2-oxoglutaric acid`; #315 records that no exact ChEBI term for the disodium
  salt surface had been found, so the local compound identity and
  `skos:narrowMatch` parent obey the salt/ion boundary.
- The final SSSOM for `MIM:Na2_Alpha-ketoglutarate` keeps the
  `CHEBI:30915` parent row and a sibling exact row to
  `kgmicrobe.compound:na2_alpha-ketoglutarate`. Its lone `other` value is the
  Greek-letter spelling of the same salt label rather than one of the rejected
  bare-ion labels.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` are backed only by
  `COMPUTATIONAL_PREDICTION` evidence from name-pattern and automatic
  energy-source inference. Their curator notes both call the roles
  provisional.

## Completeness

- The corrected local identifier, acid parent, rejected bare-ion labels,
  4/4 occurrence count, and final registry plus parent SSSOM rows agree.
- The remaining consequential gap is source-backed evidence for the two
  nutrient-role facets.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml`, either
  remove `CARBON_SOURCE` and `ENERGY_SOURCE` or replace their computational
  placeholders with source-backed evidence from maintained occurrence,
  role-text, or literature inputs. Rerun strict validation and the role/output
  SSSOM checks after the role facet changes.
