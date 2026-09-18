# `data/ingredients/mapped/CMC_PY_Horse_Serum.yaml`

## Verdict

Needs curation, minor. The local fallback identity, four curated component
assertions, SSSOM row, and aggregate copy agree, but stale top-level and
mapping-evidence notes still describe the earlier unresolved import and the
older two-of-three label split.

## Identity

- Reviewed record: `data/ingredients/mapped/CMC_PY_Horse_Serum.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:cmc_py_horse_serum` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:cmc_py_horse_serum`,
  `ontology_label: CMC + PY + Horse Serum`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `ingredient_type: UNDEFINED_MIXTURE`,
  and `mapping_status: MAPPED`.
- Live OLS exact search for `CMC + PY + Horse Serum` returned no exact public
  ontology term, matching the curated decision to keep a local kg-microbe
  ingredient identity and decompose the label into constituents.
- The current component assertion contains all four researched constituents:
  carboxymethylcellulose, peptone, yeast extract, and horse serum.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/CHIR-090.yaml data/ingredients/mapped/CMC_PY_Horse_Serum.yaml data/ingredients/mapped/Ca-folinate.yaml data/ingredients/mapped/Ca-pantothenate.yaml data/ingredients/mapped/Ca_No32.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/CHIR-090.yaml data/ingredients/mapped/CMC_PY_Horse_Serum.yaml data/ingredients/mapped/Ca-folinate.yaml data/ingredients/mapped/Ca-pantothenate.yaml data/ingredients/mapped/Ca_No32.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed on `kgmicrobe.ingredient:cmc_py_horse_serum` because the local
  kg-microbe ingredient adapter lacks `rdfs_label_statement`.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/CHIR-090.yaml data/ingredients/mapped/Ca-folinate.yaml data/ingredients/mapped/Ca-pantothenate.yaml data/ingredients/mapped/Ca_No32.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four ChEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the MicrobeDecoder source provenance for
  `kgmicrobe.compound:cmc_py_horse_serum`, the authoritative fallback SSSOM row
  at `mappings/ingredient_mappings.sssom.tsv` row 648, and the aggregate copy
  in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:CMC_PY_Horse_Serum` to
  `kgmicrobe.ingredient:cmc_py_horse_serum` with `skos:exactMatch`,
  `object_source: kgm:ingredient`, and manual curation provenance, matching the
  primary `identifier` and `ontology_mapping`.
- The current `component_assertion` evidence points at
  `mappings/microbedecoder_residual_research_decomposition.tsv`, uses
  `method: ABBREVIATION_EXPANSION`, and correctly scopes the components as an
  ingredient/mixture has-part assertion rather than an ontology identity
  mapping.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The local fallback ID, raw MicrobeDecoder label, UNDEFINED_MIXTURE
  classification, four components, component assertion, source occurrence,
  SSSOM row, and aggregate copy are populated.
- Minor gap: top-level `notes` still say no CAS/CHEBI/NCIT match was found and
  curator review was needed, which is stale after the curated decomposition and
  fallback promotion.
- Minor gap: `ontology_mapping.evidence[0].notes` still says only two of the
  three plus-separated constituents resolved and `PY` carried no
  `component_id`; the curated research decomposition now resolves four
  constituents, including the expansion of `PY` into peptone and yeast extract.

## Recommended Edits

- Minor: update `data/ingredients/mapped/CMC_PY_Horse_Serum.yaml` top-level
  `notes` and `ontology_mapping.evidence[0].notes` to describe the current
  four-component curated decomposition; then run `just sync-curated`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and focused
  strict/SSSOM validation.
