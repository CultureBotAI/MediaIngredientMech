# `data/ingredients/mapped/Cloxacillin_Sodium_Salt_Monohydrate.yaml`

## Verdict

Needs curation; major. The CAS-derived cloxacillin sodium monohydrate record is
grounded to active `CHEBI:34978`; its CAS RN, hydrate-specific formula, InChI,
SMILES, ChEBI exact synonym, zero occurrence count, SSSOM row, and aggregate
copy agree. The material gap is that `SELECTIVE_AGENT` is supported solely by a
provisional name-pattern prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Cloxacillin_Sodium_Salt_Monohydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:34978`,
  `ontology_mapping.ontology_id: CHEBI:34978`,
  `ontology_label: cloxacillin sodium monohydrate`,
  `ontology_source: CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:34978` returns active `CHEBI:34978` labelled
  `cloxacillin sodium monohydrate` with CAS RN `7081-44-9`, formula
  `C19H17ClN3O5S.H2O.Na`, and the same InChI and SMILES stored in
  `chemical_properties`.
- The `reports/hydrate_grounding.tsv` and `mappings/hydrate_review.tsv`
  hydrate audits both classify this record as a correct monohydrate-specific
  `CHEBI:34978` grounding.
- `sodium 2,2-dimethyl-6beta-({[5-methyl-3-(2-chlorophenyl)isoxazol-4-yl]carbonyl}amino)penam-3alpha-carboxylate hydrate`
  is a ChEBI exact synonym for `CHEBI:34978`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cloxacillin.yaml data/ingredients/mapped/Cloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Co-trimoxazole.yaml data/ingredients/mapped/Co_No32.yaml data/ingredients/mapped/Co_No32_X_6_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cloxacillin.yaml data/ingredients/mapped/Cloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Co-trimoxazole.yaml data/ingredients/mapped/Co_No32.yaml data/ingredients/mapped/Co_No32_X_6_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-scoped records in this batch.
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
  `reports` found the active exact
  `MIM:Cloxacillin_Sodium_Salt_Monohydrate` SSSOM row, the synonym-enrich row
  review, the hydrate audits, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  `CHEBI:34978` only as this record's `identifier` and `ontology_id`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no exact `CHEBI:34978`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The final SSSOM `other` column contains the exact ChEBI synonym and the
  matching `CAS:7081-44-9` value.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The CAS-derived ChEBI identifier, CAS RN, formula, InChI, SMILES, exact
  synonym, SSSOM row, aggregate copy, docs row, hydrate audits, and zero
  occurrence count are populated and agree.
- The only consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: in
  `data/ingredients/mapped/Cloxacillin_Sodium_Salt_Monohydrate.yaml`, either
  replace `physicochemical_roles.SELECTIVE_AGENT` with inspected evidence for
  cloxacillin sodium monohydrate as a selective agent in this media scope, or
  remove the role.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
