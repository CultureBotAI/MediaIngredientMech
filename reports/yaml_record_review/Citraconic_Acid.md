# `data/ingredients/mapped/Citraconic_Acid.yaml`

## Verdict

Pass. The CultureBotHT citraconic acid record is exactly grounded to active
`CHEBI:17626`; its CAS RN, formula, InChI, SMILES, exact synonym, zero
occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Citraconic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:17626`,
  `ontology_mapping.ontology_id: CHEBI:17626`,
  `ontology_label: citraconic acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS lookup for `citraconic acid` returns active `CHEBI:17626`
  labelled `citraconic acid`; the adjacent `CHEBI:30719` citraconate dianion is
  kept as a separate record.
- PubChem lookup by CAS RN `498-23-7` returns CID 643798, formula `C5H6O4`, and
  the same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Citraconate.yaml data/ingredients/mapped/Citraconic_Acid.yaml data/ingredients/mapped/Citramalate.yaml data/ingredients/mapped/Citrate.yaml data/ingredients/mapped/Citric_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Citraconate.yaml data/ingredients/mapped/Citraconic_Acid.yaml data/ingredients/mapped/Citramalate.yaml data/ingredients/mapped/Citrate.yaml data/ingredients/mapped/Citric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-scoped records in this batch.
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
  `reports` found the active exact `MIM:Citraconic_Acid` SSSOM row, the
  OAK/OLS row-review confirmation, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:17626` only in this active record.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no exact `CHEBI:17626`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The curated synonym `(2Z)-2-methylbut-2-enedioic acid` is a live exact
  synonym for `CHEBI:17626`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  SSSOM row, aggregate copy, and docs row are populated and agree.

## Recommended Edits

- None for this record.
