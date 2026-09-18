# `data/ingredients/mapped/D-galacturonic_Acid.yaml`

## Verdict

Pass. The exact active `CHEBI:18024` D-galacturonic acid identity, formula,
3/3 CultureMech count, CultureMech-backed `CARBON_SOURCE` role, and final SSSOM
synonym payload all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/D-galacturonic_Acid.yaml`.
- Current identifier and grounding: `identifier: CHEBI:18024`,
  `ontology_mapping.ontology_id: CHEBI:18024`,
  `ontology_label: D-galacturonic acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:18024` returns active `CHEBI:18024` labelled
  `D-galacturonic acid`, neutral formula `C6H10O7`, and exact synonyms
  including `D-galacturonate` and `D-galacturonic acids`.
- A hidden/ignored-inclusive exact `^identifier:` search under `data` found
  only this current record using `CHEBI:18024`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-fucose.yaml data/ingredients/mapped/D-galactonate.yaml data/ingredients/mapped/D-galactonic_Acid_Lactone.yaml data/ingredients/mapped/D-galactose.yaml data/ingredients/mapped/D-galacturonic_Acid.yaml`:
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

- The record's molecular formula agrees with active `CHEBI:18024`.
- `mappings/culturemech_recipe_membership.tsv` contains 3 rows for
  `CHEBI:18024`, matching the record's 3/3 `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no mapping action required.
- The final SSSOM row publishes
  `MIM:D-galacturonic_Acid skos:exactMatch CHEBI:18024`. Its `other` tokens
  are the live ChEBI synonyms `D-galacturonic acids` and `D-galacturonate`.
- The raw `Role: Carbon source; Properties:` string is retained as YAML
  provenance but is filtered from final SSSOM `other`; it does not create a
  current published synonym defect.
- The `CARBON_SOURCE` role has `DATABASE_ENTRY` evidence tied to the
  CultureMech `Original role text: Carbon Source` import and is supportable.

## Completeness

- No parent mappings, supplied-form assertions, components, environmental
  contexts, source occurrences, or unsupported computational roles are asserted.
- The aggregate record in `data/curated/mapped_ingredients.yaml` round-trips
  with the per-record YAML.

## Recommended Edits

- No curation edits are needed.
