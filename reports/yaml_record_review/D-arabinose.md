# `data/ingredients/mapped/D-arabinose.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The active exact
`CHEBI:17108` identity, formula, 6/6 occurrence count, and final SSSOM payload
pass, but the `CARBON_SOURCE` and `ENERGY_SOURCE` facets are asserted only from
provisional computational evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/D-arabinose.yaml`.
- Current identifier and grounding: `identifier: CHEBI:17108`,
  `ontology_mapping.ontology_id: CHEBI:17108`,
  `ontology_label: D-arabinose`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:17108` returns active `CHEBI:17108` labelled
  `D-arabinose`, neutral formula `C5H10O5`, CAS xref `10323-20-3`, and exact
  synonyms including `D-Ara` and `D-arabino-pentose`.
- A hidden/ignored-inclusive exact `^identifier:` search under `data` found
  only this current record using `CHEBI:17108`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-arabinose.yaml data/ingredients/mapped/D-arabitol.yaml data/ingredients/mapped/D-aspartate.yaml data/ingredients/mapped/D-erythrose.yaml data/ingredients/mapped/D-fructose.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- Five `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`
  invocations, one per reviewed CHEBI-primary file in this batch: all exited 0.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with 104 non-blocking plausibility
  warnings across the full corpus.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe transformed ontology files were absent.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1334`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1334`:
  passed; 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.
- `uv run --frozen python scripts/run_shared_evidence_validator.py`: failed
  because the sibling `culturebotai-claw` evidence validator checkout is absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 6 rows for
  `CHEBI:17108`, matching the record's 6/6 `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no mapping action required.
- The final SSSOM row publishes `MIM:D-arabinose skos:exactMatch CHEBI:17108`.
  Its `other` tokens are the live ChEBI synonyms `D-Ara` and
  `D-arabino-pentose` plus `CAS:10323-20-3`; no non-synonym payload is exported.
- `CARBON_SOURCE` is supported only by `COMPUTATIONAL_PREDICTION` from CHEBI
  carbohydrate ancestry, and `ENERGY_SOURCE` is supported only by a
  `COMPUTATIONAL_PREDICTION` that adds energy-source status alongside a carbon
  source. Both evidence rows call themselves provisional.

## Completeness

- No parent mappings, supplied-form assertions, components, or environmental
  contexts are asserted, so there are no unsupported secondary claims beyond
  the provisional nutritional roles.
- The aggregate record in `data/curated/mapped_ingredients.yaml` round-trips
  with the per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/D-arabinose.yaml`, either replace the
  computational `CARBON_SOURCE` and `ENERGY_SOURCE` evidence with direct,
  source-backed media-role evidence for D-arabinose, or remove both role
  facets; then rerun strict validation and the final SSSOM gates.
