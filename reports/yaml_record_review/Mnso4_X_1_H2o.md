# `data/ingredients/mapped/Mnso4_X_1_H2o.yaml`

## Verdict

Pass with minor issues. The explicit 1-water manganese sulfate duplicate is
correctly tombstoned as `REJECTED` after merging into the monohydrate record,
but stale pre-merge synonym, structure, and role fields remain on the
tombstone.

Severity: minor.

## Identity

- Reviewed record: `data/ingredients/mapped/Mnso4_X_1_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86364` with
  `ontology_mapping.ontology_id: CHEBI:86364`, label
  `manganese(II) sulfate monohydrate`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: REJECTED`,
  `kg_microbe_node_id: CHEBI:86364`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero active occurrences after the same-substance merge into
  `Mnso4_X_H2o`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mnso4_X_1_H2o` through `Mnso4_X_6_H2o`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` was skipped for this rejected
  tombstone; the active CHEBI-primary rows in the same batch passed.

## Evidence

- The 2026-08-15 `fix_hydrate_terms_and_twins` pass merged `MnSO4 x 1 H2O`
  into `MnSO4 x H2O` because those labels denote the same monohydrate.
- The 2026-08-15 tombstone refresh corrected the advertised ontology ID from
  the anhydrous parent `CHEBI:86360` to the monohydrate `CHEBI:86364`.
- The 2026-09-09 compatibility-node repair also updated
  `kg_microbe_node_id` to `CHEBI:86364`.
- No final SSSOM row is published for `MIM:Mnso4_X_1_H2o`.

## Completeness

- Rejection, occurrence transfer, `ontology_id`, and `kg_microbe_node_id` now
  point at the monohydrate merge target.
- The rejected tombstone still carries stale 7-water and anhydrous synonyms, an
  anhydrous InChI/SMILES pair, and a provisional `TRACE_ELEMENT` role.
- Because the record is rejected, those stale fields do not publish to final
  SSSOM.

## Recommended Edits

- Minor: optionally prune stale pre-merge synonyms, chemistry, and role fields
  from this rejected tombstone.
