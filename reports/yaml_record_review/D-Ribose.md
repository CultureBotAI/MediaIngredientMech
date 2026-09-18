# `data/ingredients/mapped/D-Ribose.yaml`

## Verdict

Needs curation, with major synonym and role-evidence issues. The exact active
`CHEBI:16988` identity, formula, 1/1 occurrence count, and canonical
`D-ribo-pentose` synonym pass, but the YAML and final SSSOM publish two
rhamnose labels as raw synonyms for D-ribose, and both nutritional roles are
only provisional computations.

## Identity

- Reviewed record: `data/ingredients/mapped/D-Ribose.yaml`.
- Current identifier and grounding: `identifier: CHEBI:16988`,
  `ontology_mapping.ontology_id: CHEBI:16988`,
  `ontology_label: D-ribose`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:16988` returns active `CHEBI:16988` labelled
  `D-ribose`, formula `C5H10O5`, and exact synonym `D-ribo-pentose`.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:16988` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Proline.yaml data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml data/ingredients/mapped/D-Ribose.yaml data/ingredients/mapped/D-Saccharic_Acid_Potassium_Salt.yaml data/ingredients/mapped/D-Serine.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Proline.yaml data/ingredients/mapped/D-Ribose.yaml data/ingredients/mapped/D-Serine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary exact records in this batch.
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

- The record's formula agrees with active `CHEBI:16988`, and the OAK/OLS row
  review confirmed the CHEBI mapping with no ontology action required.
- `mappings/culturemech_recipe_membership.tsv` contains one row for
  `CHEBI:16988`, matching the record's 1/1 `occurrence_statistics`.
- The final SSSOM row publishes `MIM:D-Ribose skos:exactMatch CHEBI:16988`.
- `D-ribo-pentose` is an exact `CHEBI:16988` synonym and is safe in SSSOM
  `other`.
- `(+)-l-rhamnose` and `(-)-d-rhamnose` are not synonyms of D-ribose. A
  hidden/ignored-inclusive search over `data`, `mappings`, `scripts`, `tests`,
  and `reports` found them only in this record, its generated final SSSOM row,
  and ignored aggregate backups.
- `CARBON_SOURCE` is supported only by a provisional CHEBI-ancestry
  `COMPUTATIONAL_PREDICTION`; `ENERGY_SOURCE` is supported only by a
  provisional canonical-substrate `COMPUTATIONAL_PREDICTION`.

## Completeness

- No parent mappings, supplied-form assertions, or mixture components are
  asserted, so there are no unsupported secondary claims beyond the two bad raw
  synonyms and two provisional nutritional roles.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry, including the two wrong rhamnose
  synonyms.

## Recommended Edits

- In `data/ingredients/mapped/D-Ribose.yaml`, remove the two
  `sssom_other_backfill` raw synonyms `(+)-l-rhamnose` and `(-)-d-rhamnose`;
  then synchronize `data/curated/mapped_ingredients.yaml` and regenerate final
  SSSOM so both labels leave the `other` column.
- Either replace the computational `CARBON_SOURCE` and `ENERGY_SOURCE`
  evidence with direct CultureBotHT or source-backed media-role evidence for
  this ingredient, or remove the role facets; then rerun strict validation and
  the final SSSOM build.
