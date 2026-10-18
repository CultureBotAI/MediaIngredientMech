# `data/ingredients/mapped/Na2so4_X_10_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:32586` sodium sulfate decahydrate
identity, CAS-backed structure, occurrence count, and final exact row pass, but
final SSSOM still publishes an anhydrous sulfate label and the migrated role
facets lack source-backed evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2so4_X_10_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:32586` with
  `ontology_mapping.ontology_id: CHEBI:32586`, label
  `sodium sulfate decahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 6 CultureMech recipe occurrences across 6 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2so3_X_5_H2o` through `Na2wo4_X_2_H2o`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:32586` as active
  `sodium sulfate decahydrate`; it carries formula `10H2O.2Na.O4S`, CAS
  `7727-73-3`, and the same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `7727-73-3` resolves to the decahydrate formula
  and stored InChI, confirming the CAS-backed chemical block.
- Major: final SSSOM `other` publishes `sodium sulfate, anhydrous`, which is a
  same-substance synonym for anhydrous `CHEBI:32149`, not for the decahydrate.
- Major: `nutritional_roles.SULFUR_SOURCE` is still backed by the provisional
  `infer_roles_from_name_lists` name-pattern evidence, and
  `nutritional_roles.MINERAL_SOURCE` has an empty evidence list.

## Completeness

- The active ChEBI term, hydrate-specific CAS RN, formula, structure, 6/6
  occurrence count, and final exact row otherwise agree.
- The remaining consequential gaps are the anhydrous final synonym and
  unsupported role facets.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2so4_X_10_H2o.yaml`, reject or demote
  `sodium sulfate, anhydrous` so it no longer publishes as an exact
  `CHEBI:32586` synonym. Rebuild final SSSOM and rerun final SSSOM validation
  plus product label validation.
- Major: either remove `SULFUR_SOURCE` and `MINERAL_SOURCE` or replace their
  missing/provisional evidence with source-backed role evidence. Rerun strict
  validation and the role/output SSSOM checks after the role facet change.
