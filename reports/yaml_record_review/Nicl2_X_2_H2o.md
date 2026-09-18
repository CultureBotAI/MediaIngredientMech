# `data/ingredients/mapped/Nicl2_X_2_H2o.yaml`

## Verdict

Needs curation - major. The record now keeps the nickel chloride dihydrate as a
local `kgmicrobe.compound` identity and close-matches the anhydrous ChEBI
parent with a required registry sibling row, but it still carries anhydrous
structure, anhydrous final synonyms, and a provisional `TRACE_ELEMENT` role.

## Identity

- Reviewed record: `data/ingredients/mapped/Nicl2_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:nicl2_x_2_h2o`
  with `ontology_mapping.ontology_id: CHEBI:34887`, label
  `nickel dichloride`, source `CHEBI`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 21 CultureMech recipe occurrences across 20 media.

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
- Fresh EBI OLS4 searches for nickel chloride dihydrate returned no exact
  ChEBI term, so the local registry identity plus `skos:closeMatch` to
  anhydrous `CHEBI:34887` remains appropriate.
- Final SSSOM has both the `skos:closeMatch` row to `CHEBI:34887` and the
  required `skos:exactMatch` row to
  `kgmicrobe.compound:nicl2_x_2_h2o`.
- Major: `chemical_properties` now has the corrected formula `Cl2Ni.2H2O`, but
  the InChI and SMILES still describe anhydrous `CHEBI:34887`.
- Major: final SSSOM `other` on the close-match row still exports anhydrous
  parent labels `nickel(2+) chloride` and `nickel(II) chloride`; parent mapping
  rows should keep only synonyms for this dihydrate.
- Major: `nutritional_roles.TRACE_ELEMENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule.

## Completeness

- The local identity row, close parent, formula, hydrate synonym rejection, and
  20/21 occurrence count otherwise agree.
- The remaining consequential gaps are the stale anhydrous structure, parent
  synonyms in final SSSOM, and unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nicl2_X_2_H2o.yaml`, either replace the
  stale anhydrous InChI/SMILES with dihydrate-specific structure evidence or
  clear them until that evidence exists.
- Major: reject or demote `nickel(2+) chloride` and `nickel(II) chloride` on
  the local dihydrate record, then rebuild final SSSOM so the close-match row
  does not publish anhydrous parent synonyms.
- Major: replace the provisional `TRACE_ELEMENT` role with inspected
  claim-level evidence or remove it.
