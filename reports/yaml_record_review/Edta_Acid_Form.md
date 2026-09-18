# `data/ingredients/mapped/Edta_Acid_Form.yaml`

## Verdict

Pass with minor issues. `EDTA (acid form)` is a rejected zero-occurrence
duplicate of the active EDTA record and publishes no final SSSOM row; only stale
post-merge role data remains on the tombstone.

## Identity

- Reviewed record: `data/ingredients/mapped/Edta_Acid_Form.yaml`.
- Identifier and grounding: `identifier: CHEBI:4735` with matching
  `ontology_mapping.ontology_id`, canonical label
  `ethylenediaminetetraacetic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: REJECTED`, zero
  occurrences, and `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:4735` to
  `ethylenediaminetetraacetic acid`.
- The 2026-08-13 history records that this record was merged into the active
  `EDTA` representative and tombstoned because it was an unused duplicate of
  the same free-acid substance.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ectoine.yaml data/ingredients/mapped/Edta.yaml data/ingredients/mapped/Edta_Acid_Form.yaml data/ingredients/mapped/Edta_Chelating_Agent.yaml data/ingredients/mapped/Edta_Stock.yaml --out /tmp/mim_edta_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Edta_Acid_Form.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  `REJECTED` status, duplicate-merge history, ChEBI identifier, exact
  synonyms, zero occurrence count, and residual `CHELATOR` role as the
  per-record YAML.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records this row as
  `REPAIRED_MAPPING_EDTA_ACID_FORM` after the 2026-05-10 correction from
  `CHEBI:42191` `EDTA(4-)` to `CHEBI:4735`.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` found the active tombstone and aggregate copy
  but no final `mappings/ingredient_mappings.sssom.tsv` row for
  `MIM:Edta_Acid_Form`.

## Completeness

- The tombstone has enough history to explain why its SSSOM row was dropped
  and which active record absorbed it.
- Minor: the rejected record still carries `physicochemical_roles.CHELATOR`
  with only provisional `COMPUTATIONAL_PREDICTION` evidence. It is not exported
  to the final SSSOM, but it is stale baggage on the tombstone.

## Recommended Edits

- Minor: remove the residual `physicochemical_roles.CHELATOR` block from
  `data/ingredients/mapped/Edta_Acid_Form.yaml` during a future tombstone
  cleanup. Rerun `sync-curated` and strict validation afterward.
