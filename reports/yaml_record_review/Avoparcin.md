# `data/ingredients/mapped/Avoparcin.yaml`

## Verdict

Pass. The kg-microbe placeholder was exact-mapped to non-obsolete
`NCIT:C169798` `Avoparcin`, the NCIT prefix/source mismatch was corrected, and
the aggregate and SSSOM rows publish the same NCIT identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Avoparcin.yaml`.
- Identifier and grounding: `identifier: NCIT:C169798` with
  `ontology_mapping.ontology_id: NCIT:C169798`,
  `ontology_label: Avoparcin`, `ontology_source: NCIT`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `NCIT:C169798` to non-obsolete `Avoparcin` with exact synonym
  `Avoparcin` and NCIT CAS annotation `37332-99-3`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Avidin.yaml data/ingredients/mapped/Avocadene.yaml data/ingredients/mapped/Avocadyne.yaml data/ingredients/mapped/Avocatin_B.yaml data/ingredients/mapped/Avoparcin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Avoparcin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `NCIT:C169798` and
  `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` both
  resolve the exact NCIT term.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 505 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv`,
  `mappings/ingredient_mappings_unknown_term_triage.tsv`, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` all agree that
  `NCIT:C169798` is an exact resolvable NCIT target.
- The 2026-05-23 curation event records the `ontology_source` correction from
  the stale CHEBI value to NCIT, matching the current `NCIT:` identifier.

## Completeness

- The exact identifier, ontology source, label, SSSOM row, aggregate copy, and
  ingredient type are populated.
- The 0/0 occurrence count is correct for a kg-microbe placeholder-derived
  record with no CultureMech recipe membership.
- No chemical structure fields, roles, components, or literature references are
  required for this exact NCIT registry record.

## Recommended Edits

- None.
