# `data/ingredients/mapped/Na2-fumarate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:115156` disodium fumarate identity,
canonical CAS-backed structure, duplicate merge, occurrence count, synonyms, and
final SSSOM row pass, but both nutrient-role facets are still provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2-fumarate.yaml`.
- Identifier and grounding: `identifier: CHEBI:115156` with
  `ontology_mapping.ontology_id: CHEBI:115156`, label `disodium fumarate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 135 CultureMech recipe occurrences across 135 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2-edta_X_2_H2o` through `Na2HPO4-NaH2PO4_Buffer`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:115156` as active
  `disodium fumarate`, with `cas:17013-01-3`, formula `C4H2O4.2Na`, the stored
  structure, and the accepted fumarate synonyms.
- The 2026-04-19 CAS conflict resolution correctly selected `17013-01-3` via the
  OAK canonical xref and left the final SSSOM row with the canonical CAS token.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` are backed only by
  `COMPUTATIONAL_PREDICTION` evidence from name-pattern and automatic
  energy-source inference. Their curator notes both explicitly call the roles
  provisional.

## Completeness

- The active ChEBI target, canonical CAS RN, formula, structure, exact synonyms,
  135/135 occurrence count, duplicate merge, and final exact mapping row agree.
- The only consequential gaps are the two unsupported nutrient-role facets.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2-fumarate.yaml`, either remove the
  `CARBON_SOURCE` and `ENERGY_SOURCE` facets or replace their computational
  placeholders with source-backed evidence from maintained occurrence,
  role-text, or literature inputs. Rerun strict validation and the role/output
  SSSOM checks after the role facet changes.
