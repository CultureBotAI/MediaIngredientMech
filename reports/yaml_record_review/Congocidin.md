# `data/ingredients/mapped/Congocidin.yaml`

## Verdict

Needs curation; major. The record still carries the
`kgmicrobe.compound:congocidin` placeholder that was retained after the May 2026
no-hit review, but a fresh OLS search for `Congocidin` now returns a plausible
MeSH `Netropsin` candidate through the related synonym `Congocidine`. That
candidate needs curator review for promotion or explicit rejection.

## Identity

- Reviewed record: `data/ingredients/mapped/Congocidin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:congocidin`,
  `ontology_mapping.ontology_id: kgmicrobe.compound:congocidin`,
  `ontology_label: Congocidin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The record notes a 2026-05-09 placeholder review that retained the
  `kgmicrobe.compound` primary identifier because OLS had no exact candidate
  and no normalized local duplicate was found.
- A fresh OLS search for `Congocidin` returned `mesh:D009429` `Netropsin` with
  related synonym `Congocidine`, so the stale placeholder assumption is no
  longer strong enough to publish without a targeted curator decision.

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
  `reports` found the active local-registry `MIM:Congocidin` final SSSOM row,
  the May 2026 unknown-term triage rows, and matching generated docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `kgmicrobe.compound:congocidin`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no
  `kgmicrobe.compound:congocidin` rows, matching the explicit 0/0
  `occurrence_statistics`.
- The final SSSOM row has no `other` tokens to review.

## Completeness

- The local placeholder identifier, SSSOM row, aggregate copy, docs row, and
  zero occurrence count are populated and agree.
- The gap is that the no-hit OLS rationale predates a now-visible plausible
  MeSH candidate for the same label.

## Recommended Edits

- Major: in `data/ingredients/mapped/Congocidin.yaml`, review whether MeSH
  `D009429` `Netropsin` is an exact grounding for Congocidin. Promote to that
  or another external identifier if exact; otherwise record an explicit
  rejection of the MeSH candidate and keep the local placeholder.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
