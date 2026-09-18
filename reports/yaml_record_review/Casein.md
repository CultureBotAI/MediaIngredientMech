# `data/ingredients/mapped/Casein.yaml`

## Verdict

Needs curation; major issue. The casein record is exactly grounded to active
`FOODON:03420180`, but `kg_microbe_node_id` still points at removed
`CHEBI:3448`.

## Identity

- Reviewed record: `data/ingredients/mapped/Casein.yaml`.
- Identifier and grounding: `identifier: FOODON:03420180`,
  `ontology_mapping.ontology_id: FOODON:03420180`,
  `ontology_label: casein`, `ontology_source: FOODON`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Direct OLS lookup for `FOODON:03420180` returns one active FoodOn term
  labelled `casein`.
- The main identifier and ontology mapping were repaired after `CHEBI:3448`
  disappeared from ChEBI, but `kg_microbe_node_id: CHEBI:3448` remains as a
  stale compatibility copy.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Caryomycin.yaml data/ingredients/mapped/Caryophyllene_T.yaml data/ingredients/mapped/Casamino_Acids.yaml data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml data/ingredients/mapped/Casein.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caryomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  unavailable for the kgmicrobe placeholder sibling because the local
  kgmicrobe OAK adapter has no `rdfs_label_statement` table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caryophyllene_T.yaml data/ingredients/mapped/Casamino_Acids.yaml data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml data/ingredients/mapped/Casein.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review-report directories,
  found the active `MIM:Casein` SSSOM row with `FOODON:03420180`, matching
  aggregate/docs rows, the confirmed OLS/FoodOn row-review disposition, and
  the node-id mismatch report row `FOODON:03420180` versus `CHEBI:3448`.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain 20
  distinct recipes and 20 total occurrences for `FOODON:03420180`, matching
  `occurrence_statistics`.
- The `NITROGEN_SOURCE` role is backed by a `DATABASE_ENTRY` evidence item
  that preserves the CultureMech source role text.

## Completeness

- The FoodOn identifier, CAS `9000-71-9`, CultureMech raw role synonym, 20/20
  occurrence count, SSSOM row, aggregate copy, and docs row are populated.

## Recommended Edits

- Major: update or remove the stale `kg_microbe_node_id: CHEBI:3448` in
  `data/ingredients/mapped/Casein.yaml`, then rerun
  `qc-kg-microbe-node-ids` and the standard strict, SSSOM, roundtrip, and diff
  checks.
