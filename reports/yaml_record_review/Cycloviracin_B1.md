# `data/ingredients/mapped/Cycloviracin_B1.yaml`

## Verdict

Pass. The MicrobeDecoder label maps exactly to active `CHEBI:200226`, keeps
matching Cycloviracin B1 structure fields, carries the reviewed one-count
BacDive production provenance, and exports a clean final SSSOM row with no
unsafe `other` labels.

## Identity

- Reviewed record: `data/ingredients/mapped/Cycloviracin_B1.yaml`.
- Current identifier and grounding: `identifier: CHEBI:200226`,
  `ontology_mapping.ontology_id: CHEBI:200226`,
  `ontology_label: Cycloviracin B1`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:200226` returns active `CHEBI:200226` labelled
  `Cycloviracin B1` with formula `C83H152O33` and matching InChI/SMILES
  strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:200226` as its primary
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

- The record's formula, InChI, SMILES, and molecular weight match live
  `CHEBI:200226`.
- `data/custom/microbedecoder/ingredient_candidates.tsv` records
  `cycloviracin B1` with count 1 from `BacDive_Metabolite_production`, matching
  the record's `source_occurrences` entry.
- `mappings/microbedecoder_auto_mapped_review.tsv` marks
  `Cycloviracin_B1.yaml` approved after local OAK resolution and
  case-insensitive exact label review.
- The final SSSOM row publishes `MIM:Cycloviracin_B1 skos:exactMatch
  CHEBI:200226`, cites MicrobeDecoder and the review-ingredients promotion, and
  has an empty `other` column.

## Completeness

- No roles, parent mappings, CAS RN, or synonyms are asserted, so there are no
  unsupported secondary claims to adjudicate.
- `occurrence_statistics` correctly stays at 0/0 for CultureMech and keeps the
  BacDive-derived MicrobeDecoder mention under `source_occurrences`.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the expected Cycloviracin B2 sibling
  import, but no row that conflicts with this Cycloviracin B1 mapping.

## Recommended Edits

- None for this record.
