# `data/ingredients/mapped/Collinomycin.yaml`

## Verdict

Needs curation; major. The active `kgmicrobe.compound:collinomycin` placeholder
is intentional: the row-review artifacts keep it pending curator promotion, and
a fresh exact OLS search still finds no `Collinomycin` class. The material gap
is that `SELECTIVE_AGENT` is supported solely by a provisional computational
name-pattern role.

## Identity

- Reviewed record: `data/ingredients/mapped/Collinomycin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:collinomycin`,
  `ontology_mapping.ontology_id: kgmicrobe.compound:collinomycin`,
  `ontology_label: Collinomycin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The record notes a 2026-05-09 placeholder review that retained the
  `kgmicrobe.compound` primary identifier because OLS had no exact candidate
  and no normalized local duplicate was found.
- A fresh exact OLS search for `Collinomycin` returned no class hits, agreeing
  with `mappings/ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Collagen.yaml data/ingredients/mapped/Collinomycin.yaml data/ingredients/mapped/Columbia_Agar_Base.yaml data/ingredients/mapped/Conessine.yaml data/ingredients/mapped/Congo_Red.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Collagen.yaml data/ingredients/mapped/Conessine.yaml data/ingredients/mapped/Congo_Red.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-identified records in this batch.
  `Collinomycin` and `Columbia_Agar_Base` were intentionally skipped because
  their local `kgmicrobe.compound` and MICRO identifiers are outside this
  CHEBI-focused LinkML term-validation pass.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the expected active local-registry `MIM:Collinomycin` SSSOM
  row and the unknown-term triage rows marking this as
  `expected_registry_identifier` pending promotion to an external ontology term.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `kgmicrobe.compound:collinomycin`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no
  `kgmicrobe.compound:collinomycin` rows, matching the explicit 0/0
  `occurrence_statistics`.
- The final SSSOM row has no `other` tokens to review.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked as a provisional
  name-pattern role.

## Completeness

- The local placeholder identifier, row-review triage, no-hit external search,
  SSSOM row, aggregate copy, docs row, and zero occurrence count are populated
  and agree.
- The only consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Collinomycin.yaml`, either replace
  `physicochemical_roles.SELECTIVE_AGENT` with inspected evidence for
  collinomycin as a selective agent in this media scope, or remove the role.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
