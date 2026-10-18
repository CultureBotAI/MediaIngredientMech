# `data/ingredients/mapped/Columbia_Agar_Base.yaml`

## Verdict

Pass. The mim-queue record is grounded to active `MICRO:0000536` Columbia Agar
Base, classified as an undefined mixture, has a matching 52/52 CultureMech
occurrence count, exports a clean final SSSOM row, and has no unsupported roles
or component claims.

## Identity

- Reviewed record: `data/ingredients/mapped/Columbia_Agar_Base.yaml`.
- Identifier and grounding: `identifier: MICRO:0000536`,
  `ontology_mapping.ontology_id: MICRO:0000536`,
  `ontology_label: Columbia Agar Base`, `ontology_source: MICRO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Live OLS lookup by `MICRO:0000536` returns active `MICRO:0000536` labelled
  `Columbia Agar Base`.
- The record represents a commercial medium base and carries no chemical
  structure, no CAS RN, and no explicit component list, which is consistent with
  `UNDEFINED_MIXTURE`.

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
  `reports` found the active `MIM:Columbia_Agar_Base` final SSSOM row, the
  unknown-term triage row classifying the earlier validator miss as
  `missing_prefix_validator_coverage_issue`, and matching generated docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `MICRO:0000536`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 52 rows for
  `MICRO:0000536` whose occurrence weights sum to 52, matching the explicit
  52/52 `occurrence_statistics`.
- The raw duplicate `Columbia agar base` synonym is filtered from the final
  SSSOM `other` column, leaving no exported synonym residue to triage.

## Completeness

- The MICRO identifier, undefined-mixture classification, SSSOM row, aggregate
  copy, docs row, and occurrence count are populated and agree.
- No recommended edits.

## Recommended Edits

- None.
