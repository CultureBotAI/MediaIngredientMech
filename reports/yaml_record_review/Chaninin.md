# `data/ingredients/mapped/Chaninin.yaml`

## Verdict

Pass. `Chaninin` is intentionally retained as the local
`kgmicrobe.compound:chaninin` placeholder while no exact CHEBI or NCIT identity
is available, and the placeholder record, SSSOM row, zero occurrence count,
aggregate copy, and no-hit review artifacts agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Chaninin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:chaninin`,
  `ontology_mapping.ontology_id: kgmicrobe.compound:chaninin`,
  `ontology_label: Chaninin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Current exact OLS search for `Chaninin` in CHEBI and NCIT returns no results,
  matching the prior no-hit placeholder review.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chaninin.yaml data/ingredients/mapped/Charcoal.yaml data/ingredients/mapped/Chartreusin.yaml data/ingredients/mapped/Chaulmoogric_Acid.yaml data/ingredients/mapped/Chelated_Iron_Solution.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for `Charcoal`, `Chartreusin`, and `Chaulmoogric_Acid`. `Chaninin`
  and `Chelated_Iron_Solution` were intentionally skipped because their
  kg-microbe CURIEs are local registry IDs outside Engine A's OBO prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Chaninin` SSSOM row, the
  `expected_registry_identifier` row-review disposition, the
  `NO_LOCAL_DUPLICATE_NO_OLS_CANDIDATE` review, the `NO_EXACT_CANDIDATE`
  OLS-candidate review, and matching aggregate and docs rows for
  `kgmicrobe.compound:chaninin`.
- `reports/yaml_record_review_batch/validation_report.md` still says
  `kgmicrobe.compound:chaninin` is invalid and does not exist, but that
  advisory batch report is stale: the active row review explicitly keeps this
  local registry identifier pending promotion to an exact external ontology
  term.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no
  `kgmicrobe.compound:chaninin` rows, matching the explicit 0/0
  `occurrence_statistics`.
- The record carries no synonym, role, chemical property, component, or
  environment claims.

## Completeness

- The local kg-microbe placeholder identifier, no-hit review note, exact local
  SSSOM row, aggregate copy, docs row, and zero occurrence count are populated
  and agree.
- No local alternate label, rejected label, or additional lookup key is
  currently required for this local identity.

## Recommended Edits

- None for this record.
