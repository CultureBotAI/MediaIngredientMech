# `data/ingredients/mapped/D-Glucaric_Acid.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The CultureBotHT row maps
exactly to active `CHEBI:16002`, keeps matching D-glucaric-acid structure
fields, has the expected 0/0 count, and exports only real synonyms in final
SSSOM, but `CARBON_SOURCE` is asserted only from a provisional CHEBI-ancestry
computation.

## Identity

- Reviewed record: `data/ingredients/mapped/D-Glucaric_Acid.yaml`.
- Current identifier and grounding: `identifier: CHEBI:16002`,
  `ontology_mapping.ontology_id: CHEBI:16002`,
  `ontology_label: D-glucaric acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:16002` returns active `CHEBI:16002` labelled
  `D-glucaric acid` with formula `C6H10O8` and matching InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:16002` as its primary
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

- The record's formula, InChI, SMILES, and CAS RN agree with active
  `CHEBI:16002`.
- `mappings/culturemech_recipe_membership.tsv` contains no `CHEBI:16002` rows,
  matching the record's 0/0 `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no mapping action required.
- The final SSSOM row publishes
  `MIM:D-Glucaric_Acid skos:exactMatch CHEBI:16002` and carries only
  `(2R,3S,4S,5S)-2,3,4,5-tetrahydroxyhexanedioic acid` plus `CAS:87-73-0` in
  `other`.
- The `CARBON_SOURCE` facet is supported only by `COMPUTATIONAL_PREDICTION`
  from CHEBI ancestry and its own `curator_note` calls it provisional; that is
  not direct source evidence that this record was used or curated as a carbon
  source.

## Completeness

- No parent mappings, supplied-form assertions, or mixture components are
  asserted, so there are no unsupported secondary claims beyond the provisional
  nutritional role.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found only the expected row-review confirmations and
  no conflicting primary record for `CHEBI:16002`.

## Recommended Edits

- In `data/ingredients/mapped/D-Glucaric_Acid.yaml`, either replace the
  computational `CARBON_SOURCE` evidence with direct source-backed media-role
  evidence for this ingredient, or remove the role facet; then rerun strict
  validation and the final SSSOM build.
