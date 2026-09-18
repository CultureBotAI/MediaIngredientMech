# `data/ingredients/mapped/Beta-D-galacto-pyranosyl-D-arabinose.yaml`

## Verdict

Needs curation, minor. The `kgmicrobe.compound` fallback, SSSOM row, aggregate
copy, and lack of a CHEBI term pass, but the top-level notes still describe the
old unmapped review state.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Beta-D-galacto-pyranosyl-D-arabinose.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:beta-d-galacto-pyranosyl-d-arabinose` with
  `ontology_mapping.ontology_id` set to the same kg-microbe CURIE,
  `ontology_label: Beta-D-galacto-pyranosyl-D-arabinose`,
  `ontology_source: kgmicrobe.compound`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- OLS search in `chebi` for `Beta-D-galacto-pyranosyl-D-arabinose` found no
  CHEBI candidate.
- The record preserves the microbedecoder source label as a raw synonym and as
  the kg-microbe fallback identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beta-Amyrin.yaml data/ingredients/mapped/Beta-D-fucose.yaml data/ingredients/mapped/Beta-D-galacto-pyranosyl-D-arabinose.yaml data/ingredients/mapped/Beta-D-galactoside.yaml data/ingredients/mapped/Beta-D-glucuronic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-Amyrin.yaml data/ingredients/mapped/Beta-D-fucose.yaml data/ingredients/mapped/Beta-D-galacto-pyranosyl-D-arabinose.yaml data/ingredients/mapped/Beta-D-galactoside.yaml data/ingredients/mapped/Beta-D-glucuronic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed on this intentional `kgmicrobe.compound` fallback because the term
  validator tried to resolve it through the ontology SQL label table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-Amyrin.yaml data/ingredients/mapped/Beta-D-fucose.yaml data/ingredients/mapped/Beta-D-galactoside.yaml data/ingredients/mapped/Beta-D-glucuronic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-backed records in the same batch.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 570 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/record_research_validation.tsv` row 929 already marks this
  `kgmicrobe.compound` primary as agreeing with the fallback registry decision:
  no ontology term denotes the compound available to that review.

## Completeness

- The kg-microbe primary ID, raw synonym, microbedecoder source occurrence,
  SSSOM row, and aggregate copy are populated.
- Minor gap: the top-level `notes` still end in `Curator review needed` even
  though the 2026-08-06 promotion resolved the record to a fallback registry
  identity.

## Recommended Edits

- Minor: update `notes` in
  `data/ingredients/mapped/Beta-D-galacto-pyranosyl-D-arabinose.yaml` so they
  no longer describe the record as pending review, then run
  `just sync-curated`.
