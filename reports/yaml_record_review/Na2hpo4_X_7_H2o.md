# `data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml`

## Verdict

Needs curation - major. The record preserves the seven-water disodium phosphate
surface instead of collapsing it to anhydrous `CHEBI:34683`, but it still misses
the available CAS exact identity, stores an anhydrous structure under a
heptahydrate formula, and carries a provisional `BUFFER` role.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:na2hpo4_x_7_h2o` with
  `ontology_mapping.ontology_id: CHEBI:34683`, label
  `disodium hydrogenphosphate`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 26 CultureMech recipe occurrences across 26 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2hpo4_X_2_H2o` through `Na2moo4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for the
  `CHEBI:34683` parent label.

## Evidence

- A fresh EBI OLS4 lookup resolves parent `CHEBI:34683` as active
  `disodium hydrogenphosphate`.
- Major: a fresh PubChem lookup for CAS RN `7782-85-6` resolves disodium
  hydrogenphosphate heptahydrate with seven waters in the formula and InChI.
  Because this record already carries that exact CAS RN, Section 3 should use
  the CAS identifier before falling back to a minted `kgmicrobe.compound`.
- Major: the YAML has a heptahydrate formula, but `chemical_properties.inchi`
  and `chemical_properties.smiles` still describe only the anhydrous
  `CHEBI:34683` salt.
- The final SSSOM rows include the close parent row and the exact local
  registry row; sibling dodecahydrate, dihydrate, and monohydrate strings are
  now rejected.
- Major: `physicochemical_roles.BUFFER` is backed only by a
  `COMPUTATIONAL_PREDICTION` evidence object from in-session LLM reasoning, and
  the curator note explicitly marks it provisional.

## Completeness

- The seven-water surface, 26/26 occurrence count, local exact row, close parent
  row, and same-hydrate aliases agree.
- The consequential gaps are the missed CAS exact identity, the stale anhydrous
  structure, and the unsupported `BUFFER` role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml`, promote the exact
  `7782-85-6` CAS identity or otherwise record why Section 3 should not use it,
  then rebuild final SSSOM so the exact CAS row is present alongside any local
  registry row.
- Major: replace the inherited anhydrous InChI and SMILES with structure values
  that include seven waters of hydration.
- Major: either remove `physicochemical_roles.BUFFER` or replace its LLM
  placeholder with source-backed evidence. Rerun strict validation and the
  final SSSOM plus product label validators after the curation changes.
