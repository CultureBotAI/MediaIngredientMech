# `data/ingredients/mapped/Brainheart_infusion_agar.yaml`

## Verdict

Pass. The `MICRO:0000566` brain heart infusion agar identity, synonym match,
restored CultureMech residual evidence, occurrence count, SSSOM row, and
aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Brainheart_infusion_agar.yaml`.
- Identifier and grounding: `identifier: MICRO:0000566` with
  `ontology_mapping.ontology_id: MICRO:0000566`,
  `ontology_label: brain heart infusion agar`, `ontology_source: MICRO`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Brain heart infusion agar` returns
  `MICRO:0000566`, matching the ontology target selected after normalizing the
  CultureMech surface form.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Brain_Heart_Infusion_Broth.yaml data/ingredients/mapped/Brainheart_infusion_agar.yaml data/ingredients/mapped/Brazilein.yaml data/ingredients/mapped/Bromocresol_Purple.yaml data/ingredients/mapped/Bromophenol_blue.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation is intentionally skipped for this record because
  `MICRO` has no OBO sqlite adapter; live OLS exact search resolved
  `MICRO:0000566`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the CultureMech residual triage and grounding rows,
  the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 629, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Brainheart_infusion_agar` to `MICRO:0000566`
  with `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact MICRO identifier, CultureMech residual source evidence, occurrence
  count, SSSOM row, and aggregate copy are populated.

## Recommended Edits

- None.
