# `data/ingredients/mapped/Air-dried_Garden_Soil.yaml`

## Verdict

Needs curation. The local exact identity plus `ENVO:00002263` parent mapping and
the 10 reassigned CultureMech occurrences are coherent, but the exact
`kgmicrobe.ingredient:air-dried_garden_soil` identifier is not registered in
the local kg-microbe ingredient registry and the record still has stale
unresolved-import notes.

## Identity

- Reviewed record: `data/ingredients/mapped/Air-dried_Garden_Soil.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:air-dried_garden_soil`
  with `ontology_mapping.ontology_id: ENVO:00002263`, source `ENVO`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `ENVO:00002263` to canonical label `garden soil`.
- `kg_microbe_node_id` matches the local identifier, and
  `ingredient_type: UNDEFINED_MIXTURE` is present.
- The two-row SSSOM pattern is correct for this modeled form: a
  `skos:narrowMatch` from `MIM:Air-dried_Garden_Soil` to the broader ENVO
  garden-soil term plus a `skos:exactMatch` companion row that preserves the
  local `kgmicrobe.ingredient:air-dried_garden_soil` identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Agave.yaml data/ingredients/mapped/Air-dried_Garden_Soil.yaml data/ingredients/mapped/Air.yaml data/ingredients/mapped/Al2_So43_X_18_H2o.yaml data/ingredients/mapped/Alanosine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Air-dried_Garden_Soil.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:envo aliases ENVO:00002263 ENVO:00002005`:
  returned canonical `garden soil` and `air`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 10
  `kgmicrobe.ingredient:air-dried_garden_soil` rows, matching both
  `occurrence_statistics` counters.
- `mappings/ingredient_mappings.sssom.tsv` rows 356 and 357 carry the intended
  parent and exact registry rows for `MIM:Air-dried_Garden_Soil`.
- A whole-repo hidden/ignored-inclusive search found
  `kgmicrobe.ingredient:air-dried_garden_soil` in the active YAML, aggregate,
  SSSOM, occurrence membership, docs, tests, coverage, and ignored backups, but
  found no row for that CURIE in `data/custom/kgmicrobe_ingredients.tsv`.
- The top-level `notes` still say the MIM queue import had no ontology match
  and needed curator review even though the September 2026 curation now models
  an exact local identity plus the broader ENVO parent.

## Completeness

- Source occurrence counts, local exact identity, parent ontology mapping,
  curation history, and `ingredient_type` are populated.
- No CAS, formula, component, role, environmental context, discussion, or
  dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Register `kgmicrobe.ingredient:air-dried_garden_soil` in the maintained local
  ingredient registry that already owns the greenhouse and Vermont soil local
  IDs, preserving `ENVO:00002263` as its broader parent.
- Refresh the stale top-level `notes` to describe the exact local identity and
  ENVO parent rather than the obsolete no-match import state.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Air-dried_Garden_Soil.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
