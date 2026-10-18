# `data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml`

## Verdict

Needs curation; severity minor. The stem-match upgrade to `MICRO:0000193`
`brain heart infusion` is valid for Bacto brain heart infusion, the occurrence
count is refreshed, and the SSSOM row plus aggregate copy are synchronized, but
the top-level `notes` still describe the old unmapped state.

## Identity

- Reviewed record: `data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml`.
- Identifier and grounding: `identifier: MICRO:0000193` with
  `ontology_mapping.ontology_id: MICRO:0000193`,
  `ontology_label: brain heart infusion`, `ontology_source: MICRO`,
  `mapping_quality: LEXICAL_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `micro` resolves `MICRO:0000193` to
  `brain heart infusion`.
- The record denotes a named Bacto brain heart infusion medium/mixture rather
  than a single CHEBI chemical.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacto-tryptone.yaml data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml data/ingredients/mapped/Bacto_Peptone.yaml data/ingredients/mapped/Bacto_Soytone.yaml data/ingredients/mapped/Bacto_Tryptic_Soy_Agar.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `MICRO` is omitted from the OBO prefix set in `just validate-terms`; OLS
  exact search separately resolved `MICRO:0000193`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 527 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `MICRO:0000193` exactly, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` documents the older
  UNKNOWN_TERM row as a missing prefix-dispatch issue rather than a mapping
  problem.
- The 2026-08-27 occurrence refresh updated the CultureMech count from 0/0 to
  29 media and 29 total occurrences.

## Completeness

- The MICRO identifier, raw source synonym, `UNDEFINED_MIXTURE` ingredient
  type, provisional `PROTEIN_SOURCE` role, occurrence count, SSSOM row, and
  aggregate copy are populated.
- The top-level `notes` field is stale and should no longer say that the record
  needs curator review.

## Recommended Edits

- Remove or rewrite the top-level `notes` in
  `data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml`, synchronize
  `data/curated/mapped_ingredients.yaml`, and rerun focused strict validation,
  SSSOM invariants, product id/label correspondence, and flat-export coverage.
