# `data/ingredients/mapped/Casamino_Acids.yaml`

## Verdict

Needs curation; major issues. The record was re-grounded from the unrelated
`CHEBI:78020` heptacosanoate identity to the FoodOn casein-hydrolysate term,
but the stale `kg_microbe_node_id`, the `carbocerate` exact synonym, and the
provisional `PROTEIN_SOURCE` role still need cleanup.

## Identity

- Reviewed record: `data/ingredients/mapped/Casamino_Acids.yaml`.
- Identifier and grounding: `identifier: FOODON:03315719`,
  `ontology_mapping.ontology_id: FOODON:03315719`,
  `ontology_label: mammalian milk protein (hydrolyzed)`,
  `ontology_source: FOODON`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- Direct OLS lookup for `FOODON:03315719` returns one active FoodOn term
  labelled `mammalian milk protein (hydrolyzed)`.
- The main identity was intentionally repaired away from
  `CHEBI:78020 heptacosanoate`, but `kg_microbe_node_id: CHEBI:78020` and the
  exact synonym `carbocerate` remain as live assertions from the obsolete
  fatty-acid grounding.

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
  found the active `MIM:Casamino_Acids` SSSOM row with `FOODON:03315719`,
  matching aggregate/docs rows, and the node-id mismatch report row
  `FOODON:03315719` versus `CHEBI:78020`.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain 1247
  distinct recipes and 1313 total occurrences for `FOODON:03315719`, matching
  `occurrence_statistics`.
- The `PROTEIN_SOURCE` role has only `COMPUTATIONAL_PREDICTION` evidence with
  a curator note that explicitly labels it a provisional name-pattern rule.

## Completeness

- The FoodOn identifier, retained CAS `65072-00-6`, 1247/1313 occurrence
  count, SSSOM row, aggregate copy, and docs row are populated.
- Chemical structure fields are correctly absent from this undefined protein
  hydrolysate mixture after the heptacosanoate regrounding.

## Recommended Edits

- Major: update or remove the stale `kg_microbe_node_id: CHEBI:78020` in
  `data/ingredients/mapped/Casamino_Acids.yaml`, then rerun
  `qc-kg-microbe-node-ids` and the standard strict, SSSOM, roundtrip, and diff
  checks.
- Major: remove `carbocerate` as an exact synonym, or move the rejected
  heptacosanoate label into a non-live review/audit note.
- Major: either replace the provisional
  `nutritional_roles.PROTEIN_SOURCE` evidence with inspected evidence for this
  acid casein hydrolysate scope, or remove the role.
