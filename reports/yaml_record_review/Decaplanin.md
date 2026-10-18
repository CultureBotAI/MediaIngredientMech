# `data/ingredients/mapped/Decaplanin.yaml`

## Verdict

Pass. The kg-microbe placeholder was promoted to the exact MeSH
`mesh:C076135` decaplanin term, live prefix-specific OLS resolves the same
CURIE, and the record exports a clean final SSSOM row with no unsupported
roles or synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Decaplanin.yaml`.
- Identifier and grounding: `identifier: mesh:C076135` with
  `ontology_mapping.ontology_id: mesh:C076135`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS exact search in the `mesh` ontology for `Decaplanin` returned one
  active result, `mesh:C076135` with label `decaplanin` and synonym
  `M86-1410`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Decanoic_Acid.yaml data/ingredients/mapped/Decaplanin.yaml data/ingredients/mapped/Decoyinine.yaml data/ingredients/mapped/Decyl_Alcohol.yaml data/ingredients/mapped/Defibrinated_horse_blood.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Decanoic_Acid.yaml data/ingredients/mapped/Decaplanin.yaml data/ingredients/mapped/Decoyinine.yaml data/ingredients/mapped/Decyl_Alcohol.yaml data/ingredients/mapped/Defibrinated_horse_blood.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the four CHEBI/MeSH rows, including this record, then failed on
  `MICRO:0001572` with the known local sqlite `rdfs_label_statement` lookup
  error.
- `curl -L ... q=Decaplanin&ontology=mesh&exact=true`: live OLS returned the
  exact `mesh:C076135` row.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  exact prefix-specific EBI OLS resolution of `mesh:C076135` to `decaplanin`.
- The older generic `mappings/ingredient_mappings_oak_ols_review.tsv`
  `UNKNOWN_TERM` row is already triaged in
  `mappings/ingredient_mappings_row_review_manifest.tsv` as
  `missing_prefix_validator_coverage_issue`: the prefix-specific OLS query
  resolves this exact CURIE, but the old dispatcher lacked full prefix
  coverage.
- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML for `mesh:C076135`.
- The same hidden/ignored-inclusive search found no
  `mappings/culturemech_recipe_membership.tsv` row for `mesh:C076135`,
  matching `occurrence_statistics.total_occurrences: 0` and `media_count: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Decaplanin` to `mesh:C076135` with `skos:exactMatch`,
  `registry:mesh`, and empty `other`.

## Completeness

- No roles, synonyms, CAS RN, parent mappings, or chemical structure fields are
  asserted; leaving those empty is appropriate for this MeSH-only exact mapping
  with 0/0 CultureMech occurrences.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
