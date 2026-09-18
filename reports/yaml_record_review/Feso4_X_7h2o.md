# `data/ingredients/mapped/Feso4_X_7h2o.yaml`

## Verdict

Pass with minor tombstone cleanup. `FeSO4 x 7H2O` has correctly been rejected
and merged into the canonical `FeSO4 x 7 H2O` heptahydrate record, and it no
longer emits final SSSOM rows; several pre-merge active fields remain on the
tombstone but do not affect publication.

## Identity

- Reviewed record: `data/ingredients/mapped/Feso4_X_7h2o.yaml`.
- Tombstone state: `identifier: CHEBI:75836`,
  `ontology_mapping.ontology_id: CHEBI:75836`, canonical label
  `iron(2+) sulfate heptahydrate`, `mapping_status: REJECTED`,
  `kg_microbe_node_id: CHEBI:75836`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- The August 15 curation history marks this record `MERGED_INTO` the canonical
  `FeSO4 x 7 H2O` record after recognizing the label as the same heptahydrate
  with a missing space before `H2O`.
- The August 15 and September 9 follow-up events repaired
  `ontology_mapping.ontology_id` and `kg_microbe_node_id` so the tombstone no
  longer points at the old anhydrous `CHEBI:75832` target.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Feso4.yaml data/ingredients/mapped/Feso4_X_5_H2o.yaml data/ingredients/mapped/Feso4_X_6_H2o.yaml data/ingredients/mapped/Feso4_X_7_H2o.yaml data/ingredients/mapped/Feso4_X_7h2o.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Feso4_X_7h2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  rejected status, repaired ChEBI target, zero occurrence count, and no
  surviving final SSSOM row as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` contains no
  `MIM:Feso4_X_7h2o` row; the active heptahydrate label is published through
  `MIM:Feso4_X_7_H2o`.
- The label-index precedence tests explicitly cover this family so a rejected
  `CHEBI:75836` tombstone cannot steal `FeSO4 x 7H2O` from the active
  `FeSO4 x 7 H2O` record.
- Minor: pre-merge sibling-hydrate and anhydrous labels are still typed as
  `HYDRATE_FORM` or `EXACT_SYNONYM`, and the tombstone still carries
  `chemical_properties` and `nutritional_roles.IRON_SOURCE` from its active
  state. Because the record is `REJECTED` and emits no final SSSOM row, these
  are stale tombstone leftovers rather than live mapping defects.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for `Feso4_X_7h2o`,
  `FeSO4 x 7H2O`, and related FeSO4 hydrate labels found the active tombstone,
  aggregate copy, canonical merge target, hydrate review rows, label-index
  precedence tests, occurrence routing helpers, and ignored aggregate backups.

## Completeness

- The tombstone's rejected status, repaired ChEBI target, and lack of final
  SSSOM output are consistent with the merge into `FeSO4 x 7 H2O`.
- The only cleanup is stale pre-merge synonym, role, and structure detail that
  should no longer be interpreted as active curation.

## Recommended Edits

- Minor: prune or retype stale active fields on the rejected
  `data/ingredients/mapped/Feso4_X_7h2o.yaml` tombstone, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation plus the
  final SSSOM invariant gates.
