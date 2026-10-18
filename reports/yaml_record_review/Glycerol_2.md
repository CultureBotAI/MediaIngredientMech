# `data/ingredients/mapped/Glycerol_2.yaml`

## Verdict

Pass with minor stale-tombstone issues. This rejected lowercase `glycerol`
duplicate no longer publishes final SSSOM rows after the merge into
`Glycerol.yaml`, but stale pre-merge role, synonym, mapping, and chemistry
fields remain on the tombstone.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycerol_2.yaml`.
- Current disposition: `mapping_status: REJECTED`, `preferred_term: glycerol`,
  `identifier: CHEBI:17754`, and the same `kg_microbe_node_id`.
- The August 2026 merge event records that this case variant was merged into
  the active `CHEBI:17754` `Glycerol` record and tombstoned so its SSSOM rows
  would be dropped.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gly-Glu.yaml data/ingredients/mapped/Glycerate.yaml data/ingredients/mapped/Glycerol.yaml data/ingredients/mapped/Glycerol_2.yaml data/ingredients/mapped/Glycerol_3-phosphate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Gly-Glu.yaml data/ingredients/mapped/Glycerate.yaml data/ingredients/mapped/Glycerol.yaml data/ingredients/mapped/Glycerol_2.yaml data/ingredients/mapped/Glycerol_3-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five ChEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` tombstone
  carries the same rejected status, duplicate identifier, stale raw role
  synonyms, stale nutritional roles, and stale chemical properties as the
  per-record YAML.
- No `MIM:Glycerol_2` subject appears in the final
  `mappings/ingredient_mappings.sssom.tsv`, so this tombstone is not publishing
  its stale role or synonym payload.
- Minor: the tombstone still carries pre-merge `ontology_mapping`, exact
  glycerol synonyms, `nutritional_roles`, `chemical_properties`, and
  `ingredient_type`. Those fields are inert for SSSOM because the record is
  `REJECTED`, but they make the rejected copy look current.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, the active
  `Glycerol` sibling, OAK/OLS review rows for the old lowercase subject,
  generated indexes, old batch validation reports, and ignored aggregate
  backups.

## Completeness

- The rejected disposition and merge history are present.
- Stale pre-rejection content needs cleanup if these tombstones are expected to
  carry only rejection metadata.

## Recommended Edits

- Minor: trim stale pre-merge structure, role, and synonym fields from
  `data/ingredients/mapped/Glycerol_2.yaml`, or add a tombstone note that these
  retained fields are historical and not exported.
