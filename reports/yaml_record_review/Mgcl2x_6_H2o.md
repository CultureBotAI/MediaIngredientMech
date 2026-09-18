# `data/ingredients/mapped/Mgcl2x_6_H2o.yaml`

## Verdict

Pass with minor tombstone cleanup. `MgCl2x 6 H2O` has correctly been rejected
and merged into the canonical `MgCl2 x 6 H2O` hexahydrate record, and it no
longer emits final SSSOM rows; stale anhydrous chemistry and wrong-hydrate
synonyms remain on the tombstone but do not affect publication.

Severity: minor.

## Identity

- Reviewed record: `data/ingredients/mapped/Mgcl2x_6_H2o.yaml`.
- Tombstone state: `identifier: CHEBI:86345`,
  `ontology_mapping.ontology_id: CHEBI:6636`, `mapping_status: REJECTED`,
  `kg_microbe_node_id: CHEBI:86345`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- The #414 merge history marks this record `MERGED_INTO` the canonical
  `MgCl2 x 6 H2O` record after recognizing the label as a hexahydrate spelling
  that had been grounded to the anhydrous salt.
- The #554 follow-up repaired `kg_microbe_node_id` to `CHEBI:86345` so same
  prefix compatibility points at the surviving hexahydrate identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgcl2x_6_H2o` through `Mgso4_X_6_H2o`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this rejected
  CHEBI-identified tombstone and the other CHEBI-identified records in the same
  batch.

## Evidence

- The final SSSOM has no `MIM:Mgcl2x_6_H2o` row, matching the #414 history
  that says this record was merged into `MgCl2 x 6 H2O` and tombstoned.
- The active `data/ingredients/mapped/Mgcl2_X_6_H2o.yaml` row now owns
  `CHEBI:86345` with the verified hexahydrate CAS `7791-18-6` and formula
  `2Cl.6H2O.Mg`.
- The rejected tombstone still carries an anhydrous
  `ontology_mapping.ontology_id`, anhydrous `chemical_properties`, and active
  mineral-role data, but those stale fields are not published while the record
  stays `REJECTED`.
- Wrong-hydrate and anhydrous labels also remain on the tombstone as
  `HYDRATE_FORM` or `EXACT_SYNONYM`; these are inert for final SSSOM because
  the tombstone does not emit a row.

## Completeness

- The tombstone preserves the merge target and no longer appears as a final
  SSSOM subject.
- The active hexahydrate row owns the mapped occurrence counts and generated
  graph output.

## Recommended Edits

- Minor: prune or retype stale active fields on the rejected
  `data/ingredients/mapped/Mgcl2x_6_H2o.yaml` tombstone if tombstones are meant
  to carry only compact merge pointers.
