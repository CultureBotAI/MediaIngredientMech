# `data/ingredients/mapped/Nicl2_X_5_H2o.yaml`

## Verdict

Needs curation - major. The malformed 5-water nickel chloride surface is
localized to a distinct `kgmicrobe.compound` identity with a close anhydrous
parent and no stale structure, but its `TRACE_ELEMENT` role is still only a
provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Nicl2_X_5_H2o.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:nicl2_x_5_h2o`
  with `ontology_mapping.ontology_id: CHEBI:34887`, label
  `nickel dichloride`, source `CHEBI`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2 CultureMech recipe occurrences across 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nicl2_X_2_H2o` through `Nicotinamide_N-oxide`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` was skipped for this local
  `kgmicrobe.compound` identity; the repository routes non-OBO registry CURIEs
  through Engine B product validation instead.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:34887` as active anhydrous
  `nickel dichloride` with formula `Cl2Ni`.
- A fresh EBI OLS4 search for nickel chloride pentahydrate returned no ChEBI
  candidate, matching the #344 decision to retain only a local unresolved
  identity for the source's 5-water label.
- Final SSSOM has both the `skos:closeMatch` row to `CHEBI:34887` and the
  required `skos:exactMatch` row to
  `kgmicrobe.compound:nicl2_x_5_h2o`; the surviving middle-dot 5-water `other`
  token is scoped to that same local identity.
- Major: `nutritional_roles.TRACE_ELEMENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule.

## Completeness

- The record intentionally has no CAS RN, InChI, or SMILES because no exact CAS
  or structure has been verified for the 5-water label.
- The active ChEBI close parent, local registry row, rejected wrong-hydrate
  labels, empty `chemical_properties`, 2/2 occurrence count, and final SSSOM
  rows otherwise agree.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nicl2_X_5_H2o.yaml`, replace the
  provisional `TRACE_ELEMENT` role with inspected claim-level evidence or
  remove it.
