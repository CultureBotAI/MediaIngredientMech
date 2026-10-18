# `data/ingredients/mapped/Garden_Soil.yaml`

## Verdict

Pass with a minor stale-note issue. The record correctly maps literal garden
soil to exact `ENVO:00002263`, keeps air-dried garden soil on its own narrower
local record, and exports a clean SSSOM row, but the top-level `notes` still
repeat the original unresolved import text.

## Identity

- Reviewed record: `data/ingredients/mapped/Garden_Soil.yaml`.
- Identifier and grounding: `identifier: ENVO:00002263` with matching
  `ontology_mapping.ontology_id`, canonical label `garden soil`, source `ENVO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- `environmental_context` also points to `ENVO:00002263` as the natural source,
  which is appropriate because the ingredient is garden soil itself.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gamma-cyclodextrin.yaml data/ingredients/mapped/Garden_Soil.yaml data/ingredients/mapped/Gardimycin.yaml data/ingredients/mapped/Gelatine.yaml data/ingredients/mapped/Gelrite.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Garden_Soil.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the ENVO primary record.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ENVO exact mapping, 5 CultureMech occurrences, undefined-mixture
  ingredient type, and natural-source environment context as the per-record
  YAML.
- `tests/test_culturemech_membership.py` and
  `tests/test_refresh_occurrence_statistics.py` cover the intended split:
  source rows for air-dried garden soil are reassigned to
  `kgmicrobe.ingredient:air-dried_garden_soil`, while exact garden soil rows
  stay on `ENVO:00002263`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the current
  `Garden soil` to `ENVO:00002263` row as `CONFIRMED_NO_ACTION`.
- The final SSSOM row maps `MIM:Garden_Soil` to `ENVO:00002263` by
  `skos:exactMatch`, with object label `garden soil`, empty `other`, and an
  `OAK+OLS` confirmed review marker.
- Minor: the top-level `notes` still say the original mim-queue import had no
  CAS-RN or CHEBI/NCIT match and needed curator review. That is stale after
  promotion to ENVO.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM and row-review rows, the air-dried garden soil tests, generated
  indexes, and ignored aggregate backups.

## Completeness

- The garden-soil identity, mixture type, environment context, occurrence
  count, and final SSSOM row are populated.
- Only the obsolete import note needs cleanup.

## Recommended Edits

- Minor: replace the top-level `notes` value with text that describes the
  current exact ENVO garden-soil identity, or remove the stale note if the
  mapping evidence and curation history are sufficient.
