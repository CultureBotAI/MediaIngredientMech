# `data/ingredients/mapped/Mgso47h2o.yaml`

## Verdict

Pass with minor tombstone cleanup. This 7-water magnesium sulfate spelling has
correctly been rejected and merged into the canonical `MgSO4 x 7 H2O`
heptahydrate record, and it no longer emits final SSSOM rows; several
pre-merge active fields remain on the tombstone but do not affect publication.

Severity: minor.

## Identity

- Reviewed record: `data/ingredients/mapped/Mgso47h2o.yaml`.
- Tombstone state: `identifier: CHEBI:31795`,
  `ontology_mapping.ontology_id: CHEBI:31795`, label
  `magnesium sulfate heptahydrate`, `mapping_status: REJECTED`,
  `kg_microbe_node_id: CHEBI:31795`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- The August 15 curation history marks this record `MERGED_INTO` the canonical
  `MgSO4 x 7 H2O` record after recognizing that this dot-separated label and
  `MgSO4 x 7 H2O` are the same heptahydrate.
- The August 15, #360, and #554 follow-up events repaired
  `ontology_mapping.ontology_id` and `kg_microbe_node_id` so the tombstone no
  longer points at the old anhydrous `CHEBI:32599` target.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgcl2x_6_H2o` through `Mgso4_X_6_H2o`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this rejected
  CHEBI-identified tombstone and the other CHEBI-identified records in the same
  batch.

## Evidence

- EBI OLS4 resolves `CHEBI:31795` as active
  `magnesium sulfate heptahydrate`, and PubChem resolves its CAS
  `10034-99-8` to the same seven-water InChI.
- The final SSSOM has no `MIM:Mgso47h2o` row, matching the merge history that
  says this record was tombstoned and its SSSOM rows were dropped.
- The active `data/ingredients/mapped/Mgso4_X_7_H2o.yaml` row now owns the
  exact `CHEBI:31795` heptahydrate mapping and active occurrence counts.
- The rejected tombstone still carries pre-merge synonym, chemistry, and role
  fields. Because the record is `REJECTED`, those leftovers do not publish.

## Completeness

- The tombstone's rejected status, repaired ChEBI target, and lack of final
  SSSOM output are consistent with the merge into `MgSO4 x 7 H2O`.

## Recommended Edits

- Minor: prune stale active fields on the rejected
  `data/ingredients/mapped/Mgso47h2o.yaml` tombstone if tombstones are meant to
  carry only compact merge pointers.
