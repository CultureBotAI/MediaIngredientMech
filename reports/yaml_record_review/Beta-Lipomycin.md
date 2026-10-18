# `data/ingredients/mapped/Beta-Lipomycin.yaml`

## Verdict

Needs curation, minor. The exact `mesh:C000601869` beta-lipomycin identity,
synonym, SSSOM row, external-prefix OLS resolution, selective-agent role
migration, and aggregate copy pass, but the top-level notes still describe the
old unmapped state.

## Identity

- Reviewed record: `data/ingredients/mapped/Beta-Lipomycin.yaml`.
- Identifier and grounding: `identifier: mesh:C000601869` with
  `ontology_mapping.ontology_id: mesh:C000601869`,
  `ontology_label: beta-lipomycin`, `ontology_source: MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS search in `mesh` resolves `mesh:C000601869` to `beta-lipomycin`.
- The record denotes beta-lipomycin and preserves the case variant `Beta
  Lipomycin` as an exact synonym from the duplicate kg-microbe placeholder.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beta-D-xylose.yaml data/ingredients/mapped/Beta-Glycerophosphate_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Beta-Lapachone.yaml data/ingredients/mapped/Beta-Lipomycin.yaml data/ingredients/mapped/Beta-alanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-D-xylose.yaml data/ingredients/mapped/Beta-Glycerophosphate_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Beta-Lapachone.yaml data/ingredients/mapped/Beta-Lipomycin.yaml data/ingredients/mapped/Beta-alanine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 577 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` row 88
  resolved `mesh:C000601869` to the same exact MeSH CURIE and label.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` row 145 kept the
  mapping and attributed the historical `UNKNOWN_TERM` status to missing
  prefix coverage in the synonym-review OLS dispatcher.
- The `SELECTIVE_AGENT` role is explicitly computational and provisional, and
  it was migrated to `physicochemical_roles` in the current schema.

## Completeness

- The exact MeSH identifier, exact synonym, SSSOM row, selective-agent role, and
  aggregate copy are populated.
- Minor gap: the top-level `notes` still end in `Curator review needed` even
  though the 2026-05 curation promoted the record to an exact MeSH mapping.

## Recommended Edits

- Minor: update `notes` in `data/ingredients/mapped/Beta-Lipomycin.yaml` so
  they no longer describe the record as pending review, then run
  `just sync-curated`.
