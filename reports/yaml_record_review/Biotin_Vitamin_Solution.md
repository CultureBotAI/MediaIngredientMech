# `data/ingredients/mapped/Biotin_Vitamin_Solution.yaml`

## Verdict

Pass. The local registry identity, deliberate `MICRO:0000460` close match,
stock-solution classification, SSSOM registry pattern, occurrence count, and
aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Biotin_Vitamin_Solution.yaml`.
- Local primary identity:
  `identifier: kgmicrobe.ingredient:biotin_vitamin_solution` with
  `kg_microbe_node_id: kgmicrobe.ingredient:biotin_vitamin_solution`,
  `ingredient_type: STOCK_SOLUTION`, and `mapping_status: MAPPED`.
- Related ontology anchor: `ontology_mapping.ontology_id: MICRO:0000460`,
  `ontology_label: vitamin solution`, `ontology_source: MICRO`, and
  `mapping_quality: CLOSE_MATCH`.
- Live OLS search in MicrO returns `MICRO:0000460` as `vitamin solution`; the
  2026-05-05 review correctly kept this record distinct because a
  biotin-specific solution is a formulation variant rather than exact identity
  with the generic class.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bimuno.yaml data/ingredients/mapped/Biochanin_A_Diacetate.yaml data/ingredients/mapped/Biotin.yaml data/ingredients/mapped/Biotin_Vitamin_Solution.yaml data/ingredients/mapped/Biphenyl.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bimuno.yaml data/ingredients/mapped/Biotin.yaml data/ingredients/mapped/Biphenyl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the NCIT/CHEBI records in this batch.
- Engine A term validation is intentionally skipped for this local registry
  record. `mappings/ingredient_mappings_external_prefix_ols_validation.tsv`
  separately resolves `MICRO:0000460` through prefix-specific EBI OLS lookup.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative MICRO close-match SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 598, the kg-microbe identity row
  at row 599, the triaged unknown-term rows in
  `mappings/ingredient_mappings_unknown_term_triage.tsv`, and the aggregate
  copy in `data/curated/mapped_ingredients.yaml`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The local kg-microbe identifier, MICRO close match, registry identity row,
  stock-solution classification, provisional vitamin-source role, occurrence
  count, and aggregate copy are populated.
- No exact MICRO, CHEBI, or NCIT mapping should replace the registry identity
  unless an ontology adds a term for the specific biotin vitamin-solution
  formulation.

## Recommended Edits

- None.
