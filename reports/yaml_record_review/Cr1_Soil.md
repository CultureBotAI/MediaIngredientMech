# `data/ingredients/mapped/Cr1_Soil.yaml`

## Verdict

Needs curation; major. `CR1 Soil` is a site-specific soil sample, but it still
uses generic `ENVO:00001998` soil as its primary identifier and final SSSOM
subject target. That collides with the generic `Soil` record and differs from
the already-fixed `Green_House_Soil` and `Vermont_Soil` pattern, where the
site-specific rows use local `kgmicrobe.ingredient` identifiers and keep
`ENVO:00001998` only as a narrow parent.

## Identity

- Reviewed record: `data/ingredients/mapped/Cr1_Soil.yaml`.
- Identifier and grounding: `identifier: ENVO:00001998`,
  `ontology_mapping.ontology_id: ENVO:00001998`, `ontology_label: soil`,
  `ontology_source: ENVO`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- Live OLS lookup by `ENVO:00001998` returns active `ENVO:00001998` labelled
  `soil`, a generic environmental material class.
- The record's own curation history states the intended semantics:
  site-specific CR1 soil should use `ENVO:00001998` as the closest applicable
  parent, not as an exact own identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cotarnine_Chloride.yaml data/ingredients/mapped/Coumarate.yaml data/ingredients/mapped/Cows_Milk.yaml data/ingredients/mapped/Cr1_Soil.yaml data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Coumarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the only CHEBI-identified record in this batch.
  `Cotarnine_Chloride`, `Cows_Milk`, `Cr1_Soil`, and
  `Cr2_So43_X_N_H2o` were intentionally skipped because their CAS, FOODON,
  ENVO, and local `kgmicrobe.compound` identifiers are outside this
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
  `reports` found the active `MIM:Cr1_Soil` final SSSOM row, the exact generic
  `MIM:Soil` row, local `Green_House_Soil` and `Vermont_Soil` narrow-parent
  rows, the duplicate-identifier reports for `ENVO:00001998`, and matching docs
  rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  `ENVO:00001998` as the primary identifier for both `Cr1_Soil.yaml` and
  `Soil.yaml`, while `Green_House_Soil.yaml` and `Vermont_Soil.yaml` use
  `ENVO:00001998` only as a parent.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 46 rows for
  `ENVO:00001998` whose occurrence weights sum to 46, matching the current
  shared ENVO occurrence count.
- The raw duplicate `CR1 Soil` synonym is filtered from the final SSSOM `other`
  column, leaving no exported synonym residue to triage.

## Completeness

- The occurrence count, undefined-mixture classification, SSSOM row, aggregate
  copy, and docs row are synchronized under the current generic ENVO target.
- The major gap is the missing local identity for this site-specific soil
  sample.

## Recommended Edits

- Major: mint a local identity such as `kgmicrobe.ingredient:cr1_soil`, move it
  into `identifier` and an exact kg-microbe registry row, retain
  `ENVO:00001998` as a `NARROW_MATCH` parent, and migrate the SSSOM and
  occurrence rows to match the existing `Green_House_Soil` and `Vermont_Soil`
  pattern.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
