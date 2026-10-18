# `data/ingredients/mapped/Gardimycin.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The exact MeSH grounding
for gardimycin now passes through the external-prefix OLS table, but
`physicochemical_roles.SELECTIVE_AGENT` is still only a provisional
name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Gardimycin.yaml`.
- Identifier and grounding: `identifier: mesh:C012993` with matching
  `ontology_mapping.ontology_id`, canonical label `gardimycin`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `mesh:C012993` exactly to gardimycin and documents that EBI OLS returned the
  exact OBO id in the requested ontology.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gamma-cyclodextrin.yaml data/ingredients/mapped/Garden_Soil.yaml data/ingredients/mapped/Gardimycin.yaml data/ingredients/mapped/Gelatine.yaml data/ingredients/mapped/Gelrite.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `Gardimycin.yaml` was intentionally skipped for LinkML Engine A label
  validation because lowercase `mesh:` is outside the CHEBI/OBO subset checked
  by this batch; Engine B and
  `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` cover the
  identifier.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same MeSH exact mapping, empty occurrence counts, empty synonym set,
  single-ingredient type, and provisional selective-agent role as the
  per-record YAML.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records that the older
  `UNKNOWN_TERM` row was a missing-prefix-validator-coverage issue and that
  prefix-specific EBI OLS lookup resolves the exact CURIE.
- The final SSSOM row maps `MIM:Gardimycin` to `mesh:C012993` by
  `skos:exactMatch` with object label `gardimycin` and empty `other`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by a
  `COMPUTATIONAL_PREDICTION` whose reference text is an inferred curated
  media-role name pattern and whose curator note says the role is provisional.
  The inspected mapping, history, and row-review rows do not supply a
  source-backed selective-agent assertion.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM row, the external-prefix OLS validation, generated indexes, stale batch
  validation reports from before prefix-specific OLS handling, and ignored
  aggregate backups.

## Completeness

- The exact gardimycin identity and final SSSOM row are populated.
- The selective-agent role needs curator review before it can be treated as
  supported.

## Recommended Edits

- Major: replace `SELECTIVE_AGENT` with source-backed evidence or remove the
  role, then rerun strict validation.
