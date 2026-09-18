# `data/ingredients/mapped/Champamycin_B.yaml`

## Verdict

Needs curation; major issue. `Champamycin B` is intentionally retained as a
local `kgmicrobe.compound:champamycin_b` placeholder while no exact external
ontology identity is available, and the placeholder record, SSSOM row, zero
occurrence count, aggregate copy, and no-hit review artifacts agree. The only
material gap is that `SELECTIVE_AGENT` is supported solely by a provisional
name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Champamycin_B.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:champamycin_b`,
  `ontology_mapping.ontology_id: kgmicrobe.compound:champamycin_b`,
  `ontology_label: Champamycin B`,
  `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Current exact OLS search for `Champamycin B` in CHEBI and NCIT returns no
  results. That agrees with the prior hidden/ignored-inclusive review artifacts
  saying the 2026-05-06 search across CHEBI, MeSH, NCIT, MICRO, BTO, and FOODON
  found no exact label or synonym candidate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cetocycline.yaml data/ingredients/mapped/Cetomacrogol_1000.yaml data/ingredients/mapped/Cetrimonium_Bromide.yaml data/ingredients/mapped/Chalcopyrite.yaml data/ingredients/mapped/Champamycin_B.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for `Cetocycline`, `Cetomacrogol_1000`, `Cetrimonium_Bromide`, and
  `Chalcopyrite`. `Champamycin_B` was intentionally skipped because
  `kgmicrobe.compound:champamycin_b` is a local registry CURIE outside Engine
  A's OAK/OLS prefix scope.
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
  `reports` found the active exact `MIM:Champamycin_B` SSSOM row, the
  `expected_registry_identifier` row-review disposition, the
  `NO_EXACT_CANDIDATE` OLS-candidate review, the manual
  `NO_IDENTITY_PROMOTION` candidate review, and matching aggregate and docs
  rows for `kgmicrobe.compound:champamycin_b`.
- `reports/yaml_record_review_batch/validation_report.md` still says
  `kgmicrobe.compound:champamycin_b` is invalid and does not exist, but that
  advisory batch report is stale: the active row review explicitly keeps this
  local registry identifier pending promotion to an exact external ontology
  term.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no
  `kgmicrobe.compound:champamycin_b` rows, matching the explicit 0/0
  `occurrence_statistics`.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The local kg-microbe placeholder identifier, no-hit review note, exact local
  SSSOM row, aggregate copy, docs row, and zero occurrence count are populated
  and agree.
- The record has no synonym, component, chemical property, or environment
  claims that need additional evidence.
- The only consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Champamycin_B.yaml`, either replace
  `physicochemical_roles.SELECTIVE_AGENT` with inspected evidence for
  Champamycin B as a selective agent in this media scope, or remove the role.
- Regenerate synchronized outputs and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
