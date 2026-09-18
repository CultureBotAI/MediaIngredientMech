# `data/ingredients/mapped/Mgso47h2o_2.yaml`

## Verdict

Pass with minor tombstone cleanup. The compact `MgSO47H2O` duplicate is
correctly tombstoned after its occurrences were merged into the canonical
`MgSO4 x 7 H2O` heptahydrate record, and no stale exact-synonym payload reaches
the final SSSOM.

Severity: minor.

## Identity

- Reviewed record: `data/ingredients/mapped/Mgso47h2o_2.yaml`.
- Tombstone state: `identifier: CHEBI:31795`,
  `ontology_mapping.ontology_id: CHEBI:31795`, label
  `magnesium sulfate heptahydrate`, `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: REJECTED`, and `ingredient_type: SINGLE_INGREDIENT`.
- The August 15 curation history marks this compact 7-water spelling
  `MERGED_INTO` the canonical `MgSO4 x 7 H2O` record.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgcl2x_6_H2o` through `Mgso4_X_6_H2o`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this rejected
  CHEBI-identified tombstone and the other CHEBI-identified records in the same
  batch.

## Evidence

- EBI OLS4 resolves `CHEBI:31795` as active
  `magnesium sulfate heptahydrate`, and PubChem resolves its CAS
  `10034-99-8` to formula `H14MgO11S` with a seven-water InChI.
- The final SSSOM has no `MIM:Mgso47h2o_2` row, so the tombstone's malformed
  pre-merge synonyms do not export.
- The active `data/ingredients/mapped/Mgso4_X_7_H2o.yaml` record now owns the
  exact `CHEBI:31795` heptahydrate mapping and active occurrence counts.

## Completeness

- The tombstone correctly retains its merge history and is absent from final
  SSSOM output.
- The tombstone still carries malformed exact synonyms, active chemistry, and
  active role facets from the pre-merge state. These are inert while the record
  stays `REJECTED`.

## Recommended Edits

- Minor: prune stale active fields on the rejected
  `data/ingredients/mapped/Mgso47h2o_2.yaml` tombstone if tombstones are meant
  to carry only compact merge pointers.
