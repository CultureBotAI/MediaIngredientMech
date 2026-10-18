# `data/ingredients/mapped/Blood.yaml`

## Verdict

Pass. The exact `UBERON:0000178` blood identity, restored CultureMech residual
evidence, occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Blood.yaml`.
- Identifier and grounding: `identifier: UBERON:0000178` with
  `ontology_mapping.ontology_id: UBERON:0000178`,
  `ontology_label: blood`, `ontology_source: UBERON`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Live OLS search for `Blood` in UBERON returns `UBERON:0000178`; the term is
  canonically labeled `blood` and denotes the whole-blood material named by the
  CultureMech residual label.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bleomycin.yaml data/ingredients/mapped/Bleomycin_Sulfate.yaml data/ingredients/mapped/Blood.yaml data/ingredients/mapped/Bluensomycin.yaml data/ingredients/mapped/Bold_Trace_Stock.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bleomycin.yaml data/ingredients/mapped/Bleomycin_Sulfate.yaml data/ingredients/mapped/Blood.yaml data/ingredients/mapped/Bluensomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four OBO-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the CultureMech residual triage and grounding rows,
  the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 613, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Blood` to `UBERON:0000178` with
  `skos:exactMatch` and carries the restored
  `MIM:culturemech:output/ingredient_occurrences.tsv` source token required by
  the structured `ontology_mapping.evidence` field.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact UBERON identifier, CultureMech residual source evidence,
  occurrence count, SSSOM row, and aggregate copy are populated.

## Recommended Edits

- None.
