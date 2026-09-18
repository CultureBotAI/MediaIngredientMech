# `data/ingredients/mapped/D-Leucine.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The exact active
`CHEBI:28225` identity, structure fields, 0/0 count, and final SSSOM CAS alias
pass, but `AMINO_ACID_SOURCE` is asserted only from a provisional
CHEBI-ancestry computation and needs direct media-use evidence or removal.

## Identity

- Reviewed record: `data/ingredients/mapped/D-Leucine.yaml`.
- Current identifier and grounding: `identifier: CHEBI:28225`,
  `ontology_mapping.ontology_id: CHEBI:28225`,
  `ontology_label: D-leucine`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:28225` returns active `CHEBI:28225` labelled
  `D-leucine` with formula `C6H13NO2` and matching InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:28225` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml data/ingredients/mapped/D-Glucuronic_Acid_Gamma_Lactone.yaml data/ingredients/mapped/D-Glucuronic_Acid_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/D-Glutamic_Acid.yaml data/ingredients/mapped/D-Leucine.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Glucuronic_Acid_Gamma_Lactone.yaml data/ingredients/mapped/D-Glutamic_Acid.yaml data/ingredients/mapped/D-Leucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary exact records in this batch.
  `D-Glucose-6-Phosphate_Sodium_Salt` and
  `D-Glucuronic_Acid_Sodium_Salt_Monohydrate` were intentionally skipped
  because their primary identifiers are CAS registry CURIEs.
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

- The record's formula, InChI, SMILES, and CAS RN agree with active
  `CHEBI:28225`.
- `mappings/culturemech_recipe_membership.tsv` contains no `CHEBI:28225` rows,
  matching the record's 0/0 `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no mapping action required.
- The final SSSOM row publishes `MIM:D-Leucine skos:exactMatch CHEBI:28225`
  and carries only `CAS:328-38-1` in `other`.
- The `AMINO_ACID_SOURCE` facet is supported only by
  `COMPUTATIONAL_PREDICTION` from CHEBI ancestry and its own `curator_note`
  calls it provisional; that is not direct source evidence that this record was
  used or curated as an amino-acid source.

## Completeness

- No parent mappings, supplied-form assertions, or mixture components are
  asserted, so there are no unsupported secondary claims beyond the provisional
  nutritional role.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found only the expected row-review confirmations and
  no conflicting primary record for `CHEBI:28225`.

## Recommended Edits

- In `data/ingredients/mapped/D-Leucine.yaml`, either replace the computational
  `AMINO_ACID_SOURCE` evidence with direct CultureBotHT or source-backed
  media-role evidence for this ingredient, or remove the role facet; then rerun
  strict validation and the final SSSOM build.
