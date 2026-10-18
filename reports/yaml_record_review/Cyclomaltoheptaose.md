# `data/ingredients/mapped/Cyclomaltoheptaose.yaml`

## Verdict

Needs curation; major. The exact `CHEBI:495055` beta-cyclodextrin identity, CAS
RN, structure fields, 3/3 CultureMech count, and final SSSOM synonyms pass, but
the `CARBON_SOURCE` role is still only inferred from CHEBI carbohydrate
ancestry.

## Identity

- Reviewed record: `data/ingredients/mapped/Cyclomaltoheptaose.yaml`.
- Current identifier and grounding: `identifier: CHEBI:495055`,
  `ontology_mapping.ontology_id: CHEBI:495055`,
  `ontology_label: beta-cyclodextrin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live exact OLS search for `Cyclomaltoheptaose` returns active
  `CHEBI:495055`, labelled `beta-cyclodextrin`, with `cyclomaltoheptaose` as
  an exact synonym.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:495055` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cycloheximid.yaml data/ingredients/mapped/Cyclomaltoheptaose.yaml data/ingredients/mapped/Cyclopamine.yaml data/ingredients/mapped/CyclopentanolCO2.yaml data/ingredients/mapped/Cycloviracin_B1.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cycloheximid.yaml data/ingredients/mapped/Cyclomaltoheptaose.yaml data/ingredients/mapped/Cyclopamine.yaml data/ingredients/mapped/Cycloviracin_B1.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI exact records in this batch.
  `CyclopentanolCO2` was intentionally skipped because its primary identifier
  is a local `kgmicrobe.ingredient` fallback rather than an OBO-backed CHEBI
  term.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- The record's formula, InChI, and SMILES encode beta-cyclodextrin and the
  stored CAS RN `7585-39-9` matches beta-cyclodextrin.
- `mappings/culturemech_recipe_membership.tsv` contains 3 distinct recipes and
  3 total occurrences for `CHEBI:495055`, matching
  `occurrence_statistics.media_count` and `.total_occurrences`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no curation action required.
- The final SSSOM row publishes `MIM:Cyclomaltoheptaose skos:exactMatch
  CHEBI:495055` and exports only beta-cyclodextrin synonyms or `CAS:7585-39-9`
  in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` still cites only
  `COMPUTATIONAL_PREDICTION` from CHEBI carbohydrate ancestry, so there is no
  source-backed evidence that beta-cyclodextrin functions as a carbon source in
  the represented media.

## Completeness

- The active identity and graph-facing SSSOM row are coherent; the remaining
  curation gap is the unsupported carbon-source role.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found only alpha-, beta-, gamma-, and
  generic cyclodextrin siblings with distinct CHEBI identifiers; none conflict
  with this beta-cyclodextrin row.

## Recommended Edits

- Major: either replace the provisional `CARBON_SOURCE` role evidence with a
  source-backed database or literature reference, or remove the role until the
  carbon-source use is curated directly.
- Regenerate synchronized products and rerun strict validation, LinkML term
  validation, SSSOM QC, aggregate roundtrip, and `git diff --check`.
