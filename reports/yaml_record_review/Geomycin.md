# `data/ingredients/mapped/Geomycin.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The exact MeSH synonym
grounding for Geomycin to oxytetracycline passes through the external-prefix
OLS table, but `physicochemical_roles.SELECTIVE_AGENT` is still only a
provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Geomycin.yaml`.
- Identifier and grounding: `identifier: mesh:D010118` with matching
  `ontology_mapping.ontology_id`, canonical label `Oxytetracycline`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `mesh:D010118` exactly to Oxytetracycline; the mapping evidence records that
  EBI OLS returned the same MeSH term through exact synonym search for
  `Geomycin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gentisic_Acid.yaml data/ingredients/mapped/Geomycin.yaml data/ingredients/mapped/Gepotidacin.yaml data/ingredients/mapped/Geraniol.yaml data/ingredients/mapped/Ginger.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `Geomycin.yaml` was intentionally skipped for LinkML Engine A label
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
- The final SSSOM row maps `MIM:Geomycin` to `mesh:D010118` by
  `skos:exactMatch`, with object label `Oxytetracycline` and empty `other`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by a
  `COMPUTATIONAL_PREDICTION` whose reference text is an inferred curated
  media-role name pattern and whose curator note says the role is provisional.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM row, external-prefix OLS validation, generated indexes, stale batch
  validation reports from before prefix-specific OLS handling, and ignored
  aggregate backups.

## Completeness

- The exact Geomycin identity and final SSSOM row are populated.
- The selective-agent role needs curator review before it can be treated as
  supported.

## Recommended Edits

- Major: replace `SELECTIVE_AGENT` with source-backed evidence or remove the
  role, then rerun strict validation.
