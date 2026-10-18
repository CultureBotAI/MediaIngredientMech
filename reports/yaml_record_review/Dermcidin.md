# `data/ingredients/mapped/Dermcidin.yaml`

## Verdict

Pass. The CultureBotHT no-CAS label was promoted to the exact MeSH
`mesh:C442243` dermcidin term, live prefix-specific OLS resolves the same
CURIE, and the final SSSOM row has no unsafe synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Dermcidin.yaml`.
- Identifier and grounding: `identifier: mesh:C442243` with
  `ontology_mapping.ontology_id: mesh:C442243`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS exact search in the `mesh` ontology for `Dermcidin` returns the
  exact `mesh:C442243` row with label `dermcidin`; the query also returns a
  plural `Dermcidins` descriptor, which is adjacent but is not the stored CURIE.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Delta-Undecalactone.yaml data/ingredients/mapped/Deoxycholic_Acid.yaml data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml data/ingredients/mapped/Dermcidin.yaml data/ingredients/mapped/Desferrioxamine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Delta-Undecalactone.yaml data/ingredients/mapped/Deoxycholic_Acid.yaml data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml data/ingredients/mapped/Dermcidin.yaml data/ingredients/mapped/Desferrioxamine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `curl -L ... q=Dermcidin&ontology=mesh&exact=true`: live OLS returned the
  exact `mesh:C442243` row.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  exact prefix-specific EBI OLS resolution of `mesh:C442243` to `dermcidin`.
- The older generic `mappings/ingredient_mappings_oak_ols_review.tsv`
  `UNKNOWN_TERM` row is already triaged in
  `mappings/ingredient_mappings_row_review_manifest.tsv` as
  `missing_prefix_validator_coverage_issue`: the prefix-specific OLS query
  resolves this exact CURIE, but the old dispatcher lacked full prefix
  coverage.
- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML for `mesh:C442243`.
- The same hidden/ignored-inclusive search found no
  `mappings/culturemech_recipe_membership.tsv` row for `mesh:C442243`,
  matching `occurrence_statistics.total_occurrences: 0` and `media_count: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Dermcidin`
  to `mesh:C442243` with `skos:exactMatch`, `registry:mesh`, and empty
  `other`.

## Completeness

- The MeSH identifier, OLS upgrade evidence, empty final SSSOM payload,
  occurrence statistics, and generated docs rows are populated and agree.
- No CAS RN, chemical structure, component list, or ingredient roles are
  asserted; leaving those empty is appropriate for this MeSH-only exact mapping
  with 0/0 CultureBotHT occurrences.

## Recommended Edits

- None.
