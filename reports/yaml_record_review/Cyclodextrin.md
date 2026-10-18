# `data/ingredients/mapped/Cyclodextrin.yaml`

## Verdict

Pass. The MicrobeDecoder `cyclodextrin` trait maps exactly to active
`CHEBI:23456`, carries the reviewed import provenance and the expected 4
MicrobeDecoder source occurrences, and exports a clean final SSSOM row with no
unsafe `other` labels.

## Identity

- Reviewed record: `data/ingredients/mapped/Cyclodextrin.yaml`.
- Current identifier and grounding: `identifier: CHEBI:23456`,
  `ontology_mapping.ontology_id: CHEBI:23456`,
  `ontology_label: cyclodextrin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:23456` returns active `CHEBI:23456` labelled
  `cyclodextrin`, a generic class for D-glucopyranose macrocycles.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:23456` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cuso4_X_5_H2o.yaml data/ingredients/mapped/Cuso4_X_6_H2o.yaml data/ingredients/mapped/Cyanocobalamin.yaml data/ingredients/mapped/Cyanuric_acid.yaml data/ingredients/mapped/Cyclodextrin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cuso4_X_5_H2o.yaml data/ingredients/mapped/Cuso4_X_6_H2o.yaml data/ingredients/mapped/Cyanocobalamin.yaml data/ingredients/mapped/Cyanuric_acid.yaml data/ingredients/mapped/Cyclodextrin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI exact records in this batch.
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

- `data/custom/microbedecoder/ingredient_candidates.tsv` records
  `cyclodextrin` with count 4 from
  `BacDive_Antibiotic_resistance|BacDive_Metabolite_utilization`, matching
  the record's `source_occurrences` entry.
- `mappings/microbedecoder_auto_mapped_review.tsv` marks
  `Cyclodextrin.yaml` approved after local OAK resolution and case-insensitive
  exact label review.
- The final SSSOM row publishes `MIM:Cyclodextrin skos:exactMatch
  CHEBI:23456`, cites MicrobeDecoder and the review-ingredients promotion, and
  has an empty `other` column.
- `occurrence_statistics` correctly stays at 0/0 for CultureMech and keeps the
  four BacDive-derived MicrobeDecoder mentions under `source_occurrences`.

## Completeness

- The active record makes no role, CAS, formula, InChI, SMILES, or synonym
  claims beyond the exact CHEBI grounding.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found alpha-, beta-, and
  gamma-cyclodextrin sibling records, but no row that conflicts with the
  generic `CHEBI:23456` mapping for plain `cyclodextrin`.

## Recommended Edits

- None for this record.
