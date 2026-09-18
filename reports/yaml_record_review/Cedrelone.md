# `data/ingredients/mapped/Cedrelone.yaml`

## Verdict

Pass. The CultureBotHT cedrelone record is exactly grounded to active
`CHEBI:197237`, and its CAS, formula, InChI, SMILES, synonym, zero occurrence
count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cedrelone.yaml`.
- Identifier and grounding: `identifier: CHEBI:197237`,
  `ontology_mapping.ontology_id: CHEBI:197237`,
  `ontology_label: CEDRELONE`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:197237` returns one active ChEBI term labelled
  `CEDRELONE` with formula `C26H30O5` and the same InChI and SMILES stored in
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cecl3.yaml data/ingredients/mapped/Cecl3_X_7_H2o.yaml data/ingredients/mapped/Cecropin_A.yaml data/ingredients/mapped/Cecropin_B.yaml data/ingredients/mapped/Cedrelone.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cecl3.yaml data/ingredients/mapped/Cecl3_X_7_H2o.yaml data/ingredients/mapped/Cecropin_A.yaml data/ingredients/mapped/Cecropin_B.yaml data/ingredients/mapped/Cedrelone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  backups, found the active exact `MIM:Cedrelone` SSSOM row and matching
  aggregate/docs rows.
- Hidden/ignored-inclusive membership search found no
  `CHEBI:197237` rows in `mappings/culturemech_recipe_membership.tsv`, which
  matches the explicit 0/0 `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, IUPAC synonym,
  SSSOM row, aggregate copy, docs row, and zero occurrence count are populated
  and agree.

## Recommended Edits

- None for this record.
