# `data/ingredients/mapped/D-galactonate.yaml`

## Verdict

Pass. The MicrobeDecoder label exact-matches active `CHEBI:12931`
`D-galactonate`, the monoanion formula and structure fields agree, the 3 BacDive
source occurrences are preserved separately from the 0/0 CultureMech count, and
the final SSSOM row carries no unsafe `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/D-galactonate.yaml`.
- Current identifier and grounding: `identifier: CHEBI:12931`,
  `ontology_mapping.ontology_id: CHEBI:12931`,
  `ontology_label: D-galactonate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:12931` returns active `CHEBI:12931` labelled
  `D-galactonate`, formula `C6H11O7`, charge -1, and `D-Galactonate` as a
  synonym.
- A hidden/ignored-inclusive exact `^identifier:` search under `data` found
  only this current record using `CHEBI:12931`.

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
  `kgmicrobe.trait:d_galactonate` import row and its 3
  `BacDive_Metabolite_utilization` count under `data/custom/microbedecoder`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the local OAK
  review that promoted this exact-label ChEBI import to `MAPPED`.
- `mappings/culturemech_recipe_membership.tsv` contains 0 rows for
  `CHEBI:12931`, matching the record's 0/0 CultureMech `occurrence_statistics`;
  the 3 BacDive mentions are correctly kept under `source_occurrences`.
- The final SSSOM row publishes
  `MIM:D-galactonate skos:exactMatch CHEBI:12931`. Its `other` field is empty.
- No nutritional, physicochemical, cellular-metabolic, environmental, or
  component claims are asserted.

## Completeness

- No parent mappings, supplied-form assertions, CultureMech recipe occurrences,
  or raw synonyms are asserted, so there are no unsupported secondary claims.
- The aggregate record in `data/curated/mapped_ingredients.yaml` round-trips
  with the per-record YAML.

## Recommended Edits

- No curation edits are needed.
