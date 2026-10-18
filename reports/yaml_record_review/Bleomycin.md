# `data/ingredients/mapped/Bleomycin.yaml`

## Verdict

Pass. The exact `CHEBI:22907` bleomycin-family identity, reviewed
MicrobeDecoder source occurrence, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bleomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:22907` with
  `ontology_mapping.ontology_id: CHEBI:22907`,
  `ontology_label: bleomycin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS exact search for `Bleomycin` returns `CHEBI:22907`; the term
  explicitly denotes the bleomycin family rather than a single A2, B2, or salt
  form.

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
  review directories, found the MicrobeDecoder raw label in
  `data/custom/microbedecoder/unmapped_labels.tsv`, the approved import-review
  row in `mappings/microbedecoder_auto_mapped_review.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 611, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Bleomycin` to `CHEBI:22907` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI family identifier, MicrobeDecoder source occurrence, reviewed
  auto-import evidence, SSSOM row, and aggregate copy are populated.
- Chemical structure fields are correctly absent because `CHEBI:22907` denotes
  a family of structurally related compounds rather than one structure.

## Recommended Edits

- None.
