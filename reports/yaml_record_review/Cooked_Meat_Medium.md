# `data/ingredients/mapped/Cooked_Meat_Medium.yaml`

## Verdict

Needs curation; major. The record represents cooked meat medium, including an
Oxoid catalog variant, but is grounded to `FOODON:03305103` `meat (cooked)`.
Live OLS confirms the FoodOn target is cooked meat itself, not a cooked-meat
microbiology medium or medium base, and a quoted OLS search found no exact
`Cooked meat medium` class.

## Identity

- Reviewed record: `data/ingredients/mapped/Cooked_Meat_Medium.yaml`.
- Identifier and grounding: `identifier: FOODON:03305103`,
  `ontology_mapping.ontology_id: FOODON:03305103`,
  `ontology_label: meat (cooked)`, `ontology_source: FOODON`,
  `mapping_quality: LEXICAL_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Live OLS lookup by `FOODON:03305103` returns active `FOODON:03305103`
  labelled `meat (cooked)` and describes meat which has been cooked.
- Quoted OLS search for `Cooked meat medium` returned no exact class, agreeing
  that the current FoodOn mapping came from a fuzzy top hit rather than an
  exact medium identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Congocidin.yaml data/ingredients/mapped/Coniferyl_Alcohol.yaml data/ingredients/mapped/Coniferyl_Aldehyde.yaml data/ingredients/mapped/Cooked_Meat_Medium.yaml data/ingredients/mapped/Copper.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Coniferyl_Alcohol.yaml data/ingredients/mapped/Coniferyl_Aldehyde.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two CHEBI-identified records in this batch. `Congocidin`,
  `Cooked_Meat_Medium`, and `Copper` were intentionally skipped because their
  local `kgmicrobe.compound` and FOODON identifiers are outside this
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
  `reports` found the active `MIM:Cooked_Meat_Medium` final SSSOM row, the row
  review that only recommended synonym enrichment, a separate
  `Modified_Cooked_Meat_Medium` local medium record, and matching generated docs
  rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `FOODON:03305103`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 2 rows for
  `FOODON:03305103` whose occurrence weights sum to 2, matching the explicit
  2/2 `occurrence_statistics`.
- The final SSSOM `other` column exports `Cooked meat medium (Oxoid)`, a
  catalog variant of the medium label; the issue is the primary FoodOn
  grounding, not that `other` value.

## Completeness

- The occurrence count, undefined-mixture classification, Oxoid surface form,
  SSSOM row, aggregate copy, and docs row are synchronized.
- The major gap is that the ontology target denotes cooked meat rather than the
  cooked-meat medium or medium base.

## Recommended Edits

- Major: replace `FOODON:03305103` with an exact external medium term if one is
  found; otherwise move the record to a local `kgmicrobe.ingredient` or
  equivalent registry identity for cooked meat medium. Preserve `Cooked meat
  medium (Oxoid)` only as a catalog variant for this medium identity.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
