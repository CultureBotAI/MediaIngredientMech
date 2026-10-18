# `data/ingredients/mapped/D-fucose.yaml`

## Verdict

Pass. The MicrobeDecoder label exact-matches active `CHEBI:28847` `D-fucose`,
the neutral formula and structure fields agree, the 200 BacDive source
occurrences are preserved separately from the 0/0 CultureMech count, and the
final SSSOM row carries no unsafe `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/D-fucose.yaml`.
- Current identifier and grounding: `identifier: CHEBI:28847`,
  `ontology_mapping.ontology_id: CHEBI:28847`,
  `ontology_label: D-fucose`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:28847` returns active `CHEBI:28847` labelled
  `D-fucose`, neutral formula `C6H12O5`, and exact synonyms including
  `6-deoxy-D-galactose` and `D-Fuc`.
- A hidden/ignored-inclusive exact `^identifier:` search under `data` found
  only this current record using `CHEBI:28847`.

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

- The hidden/ignored-inclusive MicrobeDecoder search found the original
  `kgmicrobe.trait:d_fucose` import row and its 200
  `BacDive_Metabolite_utilization` count under `data/custom/microbedecoder`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the local OAK
  review that promoted this exact-label ChEBI import to `MAPPED`.
- `mappings/culturemech_recipe_membership.tsv` contains 0 rows for
  `CHEBI:28847`, matching the record's 0/0 CultureMech `occurrence_statistics`;
  the 200 BacDive mentions are correctly kept under `source_occurrences`.
- The final SSSOM row publishes `MIM:D-fucose skos:exactMatch CHEBI:28847`.
  Its `other` field is empty.
- No nutritional, physicochemical, cellular-metabolic, environmental, or
  component claims are asserted.

## Completeness

- No parent mappings, supplied-form assertions, CultureMech recipe occurrences,
  or raw synonyms are asserted, so there are no unsupported secondary claims.
- The aggregate record in `data/curated/mapped_ingredients.yaml` round-trips
  with the per-record YAML.

## Recommended Edits

- No curation edits are needed.
