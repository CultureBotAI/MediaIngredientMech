# `data/ingredients/mapped/2-Sulfobenzoic_Acid.yaml`

## Verdict

Needs curation, minor. The `mesh:C028805` grounding itself resolves through
prefix-specific OLS as `2-sulfobenzoic acid`, but the top-level `notes` field
still describes the obsolete pre-promotion unmapped state.

## Identity

- Reviewed record: `data/ingredients/mapped/2-Sulfobenzoic_Acid.yaml`.
- Identifier and grounding: `identifier: mesh:C028805` with
  `ontology_mapping.ontology_id: mesh:C028805`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS check: the refreshed EBI OLS MESH payload resolves
  `http://id.nlm.nih.gov/mesh/C028805` and the `C028805` CURIE with label
  `2-sulfobenzoic acid`.
- Source occurrence support is current: `occurrence_statistics` reports 2 total
  occurrences in 2 media, and `mappings/culturemech_recipe_membership.tsv`
  lists two `mesh:C028805` CultureMech recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Piperidinone.yaml data/ingredients/mapped/2-Sulfobenzoic_Acid.yaml data/ingredients/mapped/2-_Methylthioethanol.yaml data/ingredients/mapped/2-aminobenzoate.yaml data/ingredients/mapped/2-aminopentanoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-Sulfobenzoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Sulfobenzoic_Acid` to `mesh:C028805` row.

## Evidence

- The active EBI OLS lookup confirms the MESH CURIE and label.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` already
  records `mesh:C028805` as `RESOLVED_EXACT_CURIE`, and
  `mappings/ingredient_mappings_unknown_term_triage.tsv` records the older
  UNKNOWN_TERM row as a prefix-coverage issue in the synonym-review dispatcher.
- Stale: top-level `notes` still says there was no CHEBI/NCIT match and
  curator review was needed. The record was promoted to MESH on 2026-05-02.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `reports`
  found the current YAML/aggregate/SSSOM rows, the OLS exact-CURIE triage row,
  and older stale research/batch rows that predate the explicit OLS check.

## Completeness

- MESH-backed rows do not always carry ChEBI-derived structure data; the missing
  `chemical_properties` field is not itself proof of a wrong mapping.
- Empty component and role slots are acceptable for this single acid record.
- The only actionable gap in the YAML is the stale top-level note.

## Recommended Edits

1. In `data/ingredients/mapped/2-Sulfobenzoic_Acid.yaml`, replace the stale
   `notes` text with a short statement that `mesh:C028805` was verified through
   prefix-specific EBI OLS lookup.
2. Run `just sync-curated`, `just validate-strict
   data/ingredients/mapped/2-Sulfobenzoic_Acid.yaml`, `just validate-terms
   data/ingredients/mapped/2-Sulfobenzoic_Acid.yaml`, `just qc-sssom`, and
   `just qc-flat-coverage` after that curation edit.
