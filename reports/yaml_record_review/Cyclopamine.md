# `data/ingredients/mapped/Cyclopamine.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed row maps exactly to active `CHEBI:4021`,
keeps matching structure fields, has the expected 0/0 CultureMech count, and
exports a clean final SSSOM row with only `CAS:4449-51-8` in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Cyclopamine.yaml`.
- Current identifier and grounding: `identifier: CHEBI:4021`,
  `ontology_mapping.ontology_id: CHEBI:4021`,
  `ontology_label: Cyclopamine`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:4021` returns active `CHEBI:4021` labelled
  `Cyclopamine` with CAS `4449-51-8`, formula `C27H41NO2`, and matching
  InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:4021` as its primary
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

- The record's CAS RN, formula, InChI, and SMILES match live `CHEBI:4021`.
- `mappings/culturemech_recipe_membership.tsv` contains no `CHEBI:4021` rows,
  matching the record's 0/0 `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no curation action required.
- The final SSSOM row publishes `MIM:Cyclopamine skos:exactMatch CHEBI:4021`
  with `CAS:4449-51-8` as the only `other` token.

## Completeness

- No roles, parent mappings, or source synonyms are asserted, so there are no
  unsupported secondary claims to adjudicate.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the expected CultureBotHT-derived
  generated rows and no stale conflicting identifier for this term.

## Recommended Edits

- None for this record.
