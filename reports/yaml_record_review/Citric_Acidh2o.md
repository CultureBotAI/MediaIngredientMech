# `data/ingredients/mapped/Citric_Acidh2o.yaml`

## Verdict

Needs curation; minor. The old duplicate source record is correctly rejected
into `data/ingredients/mapped/Citric_Acid_X_H2o.yaml`, has 0/0 occurrences, and
does not publish a live SSSOM row. It still carries two stale provisional
nutritional roles on the rejected tombstone.

## Identity

- Reviewed record: `data/ingredients/mapped/Citric_Acidh2o.yaml`.
- Tombstone state: `mapping_status: REJECTED`, `identifier: CHEBI:31404`,
  `ontology_mapping.ontology_id: CHEBI:31404`, and
  `ontology_label: Citric acid monohydrate`.
- The 2026-09-12 `MERGED_INTO` event records that this duplicate was merged into
  the surviving `CHEBI:31404` `Citric acid x H2O` monohydrate record and had its
  occurrences zeroed.
- Live exact OLS lookup for `Citric acid monohydrate` returns one active
  `CHEBI:31404` term labelled `Citric acid monohydrate`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Citric_Acid_X_H2o.yaml data/ingredients/mapped/Citric_Acidh2o.yaml data/ingredients/mapped/Cl.yaml data/ingredients/mapped/Cladomycin.yaml data/ingredients/mapped/Clarified_rumen_fluid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Citric_Acid_X_H2o.yaml data/ingredients/mapped/Citric_Acidh2o.yaml data/ingredients/mapped/Cl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-scoped records in this batch. `Cladomycin` and
  `Clarified_rumen_fluid` were skipped because local `kgmicrobe.compound:` and
  `MICRO:` terms are outside the focused Engine A CHEBI/OBO validation scope.
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
  `reports` found no active `MIM:Citric_Acidh2o` SSSOM row, found the accepted
  hydrate-review merge into `Citric_Acid_X_H2o`, and found the old source label
  preserved as a synonym on that surviving active monohydrate record.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:31404` only on this rejected tombstone and on the surviving active
  `Citric_Acid_X_H2o` record.
- The two anhydrous or non-resolving synonym rows on the tombstone are typed
  `REJECTED_LABEL`, so they are correctly omitted from final SSSOM `other`.
- `nutritional_roles.CARBON_SOURCE` and `nutritional_roles.ENERGY_SOURCE` remain
  on the rejected tombstone even though they are live-record claims with only
  provisional computational evidence.

## Completeness

- The rejected status, duplicate-merge history, zero occurrence count, and
  absence of an active SSSOM row are synchronized.
- The only active cleanup gap is the stale pair of nutritional roles.

## Recommended Edits

- Minor: remove the stale `nutritional_roles` block from
  `data/ingredients/mapped/Citric_Acidh2o.yaml`; the rejected tombstone should
  retain only the provenance needed to explain the merge into
  `Citric_Acid_X_H2o`.
