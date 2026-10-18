# `data/ingredients/mapped/Glucose_2.yaml`

## Verdict

Pass with minor tombstone cleanup issues. The duplicate lowercase glucose record
was rejected and no longer publishes final SSSOM rows, but it still retains
stale single-ingredient, structure, and nutritional-role fields from before the
merge.

## Identity

- Reviewed record: `data/ingredients/mapped/Glucose_2.yaml`.
- Identifier and grounding: `identifier: CHEBI:17234` with matching
  `ontology_mapping.ontology_id`, canonical label `glucose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: REJECTED`.
- The record is a tombstone for the duplicate lowercase `glucose` import that
  previously pointed at open-chain `CHEBI:42758`; issue `#360` refreshed the
  tombstone ontology id to the surviving generic `CHEBI:17234` target, and
  issue `#554` refreshed the kg-microbe node id to match.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gluconic_Acid.yaml data/ingredients/mapped/Glucosamine.yaml data/ingredients/mapped/Glucose.yaml data/ingredients/mapped/Glucose_1-phosphate.yaml data/ingredients/mapped/Glucose_2.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gluconic_Acid.yaml data/ingredients/mapped/Glucosamine.yaml data/ingredients/mapped/Glucose.yaml data/ingredients/mapped/Glucose_1-phosphate.yaml data/ingredients/mapped/Glucose_2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same rejected tombstone state, corrected ChEBI identifier, corrected
  kg-microbe node id, pre-merge roles, and pre-merge structure fields as the
  per-record YAML.
- A hidden/ignored-inclusive search over the final SSSOM confirmed there is no
  `MIM:Glucose_2` row.
- The active `data/ingredients/mapped/Glucose.yaml` record carries the
  published `CHEBI:17234` generic glucose identity and the transferred
  occurrence counts.
- Minor: because the tombstone retained its pre-merge `ingredient_type`,
  `chemical_properties`, and `nutritional_roles`, these fields now duplicate
  assertions that are not active for a rejected record.
- A broader hidden/ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, and `reports` found the active YAML, the active
  Glucose winner, final SSSOM rows for the winner and sibling
  glucose-containing records, generated indexes, old batch validation reports,
  and ignored aggregate backups.

## Completeness

- The tombstone status, corrected survivor identifier, corrected kg-microbe node
  id, and SSSOM suppression are in place.
- Stale pre-merge fields can be removed from the rejected record.

## Recommended Edits

- Minor: remove stale structure, type, and nutritional-role fields from the
  rejected tombstone if tombstones are intended to retain only merge
  provenance.
