# `data/ingredients/mapped/D-Glucosamine_6-phosphate.yaml`

## Verdict

Pass. The CultureBotHT row maps exactly to active `CHEBI:12962`, keeps matching
D-glucosamine 6-phosphate chemistry, has the expected 0/0 CultureMech count,
and exports a clean final SSSOM row with only a real exact synonym and its own
CAS alias in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/D-Glucosamine_6-phosphate.yaml`.
- Current identifier and grounding: `identifier: CHEBI:12962`,
  `ontology_mapping.ontology_id: CHEBI:12962`,
  `ontology_label: D-glucosamine 6-phosphate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:12962` returns active `CHEBI:12962` labelled
  `D-glucosamine 6-phosphate` with formula `C6H14NO8P` and matching InChI.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:12962` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Galacturonic_Acid_Monohydrate.yaml data/ingredients/mapped/D-Glucaric_Acid.yaml data/ingredients/mapped/D-Gluconic_acid.yaml data/ingredients/mapped/D-Glucosamine_6-phosphate.yaml data/ingredients/mapped/D-Glucosamine_Hydrochloride.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Glucaric_Acid.yaml data/ingredients/mapped/D-Gluconic_acid.yaml data/ingredients/mapped/D-Glucosamine_6-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary exact records in this batch.
  `D-Galacturonic_Acid_Monohydrate` and `D-Glucosamine_Hydrochloride` were
  intentionally skipped because their primary identifiers are CAS registry
  CURIEs.
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

- The record's formula and CAS RN agree with the active `CHEBI:12962` identity;
  live OLS exposes the same formula and an InChI for the same compound.
- `mappings/culturemech_recipe_membership.tsv` contains no `CHEBI:12962` rows,
  matching the record's 0/0 `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no mapping action required.
- The final SSSOM row publishes
  `MIM:D-Glucosamine_6-phosphate skos:exactMatch CHEBI:12962` and carries only
  `2-amino-2-deoxy-D-glucose 6-(dihydrogen phosphate)` plus `CAS:3616-42-0` in
  `other`.

## Completeness

- No roles, parent mappings, supplied-form assertions, or mixture components
  are asserted, so there are no unsupported secondary claims to adjudicate.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected row-review confirmations and no
  conflicting primary record for `CHEBI:12962`.

## Recommended Edits

- None for this record.
