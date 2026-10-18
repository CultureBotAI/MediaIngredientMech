# `data/ingredients/mapped/Gluconic_Acid.yaml`

## Verdict

Needs curation, with major unsupported-role issues. The exact `CHEBI:24266`
gluconic acid identity, PubChem CAS xref, formula, and final SSSOM row pass,
but both `CARBON_SOURCE` and `ENERGY_SOURCE` are still provisional
computational predictions.

## Identity

- Reviewed record: `data/ingredients/mapped/Gluconic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:24266` with matching
  `ontology_mapping.ontology_id`, canonical label `gluconic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:24266` as active gluconic acid with formula `C6H11O7`
  and mass `195.148`, matching the YAML formula.

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
  the same ChEBI exact mapping, 2 CultureMech occurrences, CAS RN, formula,
  single-ingredient type, and provisional nutritional roles as the per-record
  YAML.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the current
  `Gluconic acid` to `CHEBI:24266` row as `CONFIRMED_NO_ACTION`.
- The final SSSOM row maps `MIM:Gluconic_Acid` to `CHEBI:24266` by
  `skos:exactMatch` and exports only `CAS:526-95-4` in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` is supported only by a
  `COMPUTATIONAL_PREDICTION` from ChEBI carbohydrate ancestry whose curator
  note says the role is provisional.
- Major: `nutritional_roles.ENERGY_SOURCE` is supported only by a
  `COMPUTATIONAL_PREDICTION` whose reference text is a generic energy-substrate
  assertion and whose curator note says review is recommended.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM and row-review rows, the sibling D-Gluconic acid record, generated
  indexes, old batch validation reports, and ignored aggregate backups.

## Completeness

- The exact gluconic acid identity, CAS RN, formula, occurrence count, and final
  SSSOM row are populated.
- Both nutritional roles need curator review before they can be treated as
  supported.

## Recommended Edits

- Major: replace `CARBON_SOURCE` and `ENERGY_SOURCE` with source-backed
  evidence or remove the roles, then rerun strict validation.
