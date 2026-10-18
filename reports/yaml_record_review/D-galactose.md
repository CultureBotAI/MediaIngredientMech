# `data/ingredients/mapped/D-galactose.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The exact active
`CHEBI:12936` D-galactose identity, formula/CAS fields, 7/7 occurrence count,
final SSSOM payload, and CultureMech-backed `CARBON_SOURCE` role pass, but
`ENERGY_SOURCE` is asserted only from provisional computational evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/D-galactose.yaml`.
- Current identifier and grounding: `identifier: CHEBI:12936`,
  `ontology_mapping.ontology_id: CHEBI:12936`,
  `ontology_label: D-galactose`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:12936` returns active `CHEBI:12936` labelled
  `D-galactose`, neutral formula `C6H12O6`, and exact synonyms including
  `D-Gal` and `D-galacto-hexose`.
- A hidden/ignored-inclusive exact `^identifier:` search under `data` found
  only this current record using `CHEBI:12936`.

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

- `mappings/culturemech_recipe_membership.tsv` contains 7 rows for
  `CHEBI:12936`, matching the record's 7/7 `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no mapping action required.
- The final SSSOM row publishes `MIM:D-galactose skos:exactMatch CHEBI:12936`.
  Its `other` tokens are the live ChEBI synonyms `D-Gal` and
  `D-galacto-hexose` plus `CAS:59-23-4`; no non-synonym payload is exported.
- The raw `Cross-references: KEGG:gal` and `Role: Carbon source; Properties:`
  strings are retained as YAML provenance but are filtered from final SSSOM
  `other`; they do not create a current published synonym defect.
- The `CARBON_SOURCE` role has `DATABASE_ENTRY` evidence tied to the
  CultureMech `Original role text: Carbon Source` import and is supportable.
  `ENERGY_SOURCE` is supported only by a `COMPUTATIONAL_PREDICTION` that adds
  energy-source status alongside carbon-source status and calls itself
  provisional.

## Completeness

- No parent mappings, supplied-form assertions, components, environmental
  contexts, or source occurrences are asserted.
- The aggregate record in `data/curated/mapped_ingredients.yaml` round-trips
  with the per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/D-galactose.yaml`, either replace the
  computational `ENERGY_SOURCE` evidence with direct, source-backed evidence
  for D-galactose as an energy source or remove that role facet; then rerun
  strict validation and the final SSSOM gates.
