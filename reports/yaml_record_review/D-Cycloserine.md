# `data/ingredients/mapped/D-Cycloserine.yaml`

## Verdict

Pass. The CultureBotHT row maps exactly to active `CHEBI:40009`, keeps matching
D-cycloserine structure fields, has a refreshed 1/1 CultureMech occurrence
count, and exports a clean final SSSOM row with only a real exact synonym and
its own CAS alias in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/D-Cycloserine.yaml`.
- Current identifier and grounding: `identifier: CHEBI:40009`,
  `ontology_mapping.ontology_id: CHEBI:40009`,
  `ontology_label: D-cycloserine`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:40009` returns active `CHEBI:40009` labelled
  `D-cycloserine` with formula `C3H6N2O2` and matching InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:40009` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-2-Aminobutyric_Acid.yaml data/ingredients/mapped/D-Alanine.yaml data/ingredients/mapped/D-Aspartic_Acid.yaml data/ingredients/mapped/D-Cycloserine.yaml data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-2-Aminobutyric_Acid.yaml data/ingredients/mapped/D-Alanine.yaml data/ingredients/mapped/D-Aspartic_Acid.yaml data/ingredients/mapped/D-Cycloserine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-primary exact records in this batch.
  `D-Fructose_6-phosphate_Disodium_Salt_Hydrate` was intentionally skipped
  because its primary identifier is `cas:26177-86-6`.
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
  `CHEBI:40009`.
- `mappings/culturemech_recipe_membership.tsv` contains one row for
  `CHEBI:40009`, matching the record's refreshed 1/1
  `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no mapping action required.
- The final SSSOM row publishes `MIM:D-Cycloserine skos:exactMatch
  CHEBI:40009` and carries only `(4R)-4-aminoisoxazolidin-3-one` plus
  `CAS:68-41-7` in `other`.

## Completeness

- No roles, parent mappings, supplied-form assertions, or mixture components
  are asserted, so there are no unsupported secondary claims to adjudicate.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected row-review confirmations and no
  conflicting primary record for `CHEBI:40009`.

## Recommended Edits

- None for this record.
