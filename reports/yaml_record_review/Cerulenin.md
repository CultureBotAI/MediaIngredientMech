# `data/ingredients/mapped/Cerulenin.yaml`

## Verdict

Pass. The cerulenin record is exactly grounded to active `CHEBI:171741`, and
its CAS, formula, InChI, SMILES, zero occurrence count, exact ChEBI synonym,
SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cerulenin.yaml`.
- Identifier and grounding: `identifier: CHEBI:171741`,
  `ontology_mapping.ontology_id: CHEBI:171741`,
  `ontology_label: cerulenin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:171741` returns one active ChEBI term labelled
  `cerulenin` with formula `C12H17NO3`, molecular mass `223.272`, and the same
  InChI and SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cephalothin_Sodium_Salt.yaml data/ingredients/mapped/Cephamycin_A.yaml data/ingredients/mapped/Cephradine.yaml data/ingredients/mapped/Cerulenin.yaml data/ingredients/mapped/Cesium_Chloride.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cephalothin_Sodium_Salt.yaml data/ingredients/mapped/Cephamycin_A.yaml data/ingredients/mapped/Cephradine.yaml data/ingredients/mapped/Cerulenin.yaml data/ingredients/mapped/Cesium_Chloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 external-ontology records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active exact `MIM:Cerulenin` SSSOM row, the `CONFIRMED`
  row-review disposition, and matching aggregate/docs rows for `CHEBI:171741`.
- The active SSSOM row includes `CAS:17397-89-6` and the ChEBI-reviewed exact
  synonym already present in YAML.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:171741` rows,
  which matches the explicit 0/0 `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, exact synonym, SSSOM
  row, aggregate copy, docs row, and zero occurrence count are populated and
  agree.
- No additional exact synonym or rejected label is needed for this record.

## Recommended Edits

- None for this record.
