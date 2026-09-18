# `data/ingredients/mapped/Na3-edta.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:63125` EDTA trisodium salt identity,
structure, occurrence count, and final exact row pass, but final SSSOM still
publishes a disodium EDTA alias and the `CHELATOR` role is a provisional
name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Na3-edta.yaml`.
- Identifier and grounding: `identifier: CHEBI:63125` with
  `ontology_mapping.ontology_id: CHEBI:63125`, label `EDTA trisodium salt`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 30 CultureMech recipe occurrences across 30 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na3-citrate_X_2_H2o` through `Nabr`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:63125` as active
  `EDTA trisodium salt` with formula `C10H13N2O8.3Na` and the same InChI and
  SMILES as the record.
- A fresh PubChem CAS lookup for `150-38-9` resolves to trisodium EDTA with the
  same InChI, so the CAS-backed structure denotes the same trisodium salt even
  though the current OLS payload for `CHEBI:63125` no longer lists that CAS.
- Major: `EDTA di sodium salt` remains active and publishes in final SSSOM
  `other`; it crosses the disodium/trisodium salt boundary.
- Major: `physicochemical_roles.CHELATOR` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists`, and
  the curator note explicitly marks the role provisional.

## Completeness

- The active ChEBI term, formula, structure, 30/30 occurrence count, and final
  exact row otherwise agree.
- The remaining consequential gaps are the disodium alias and source-backed
  evidence for the chelator role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na3-edta.yaml`, reject or delete
  `EDTA di sodium salt` so it no longer publishes as an exact `CHEBI:63125`
  synonym. Rebuild final SSSOM and rerun final SSSOM validation plus product
  label validation.
- Major: either remove `physicochemical_roles.CHELATOR` or replace its
  name-pattern placeholder with source-backed evidence from maintained role-text
  or literature inputs. Rerun strict validation and the role/output SSSOM checks
  after the role facet change.
