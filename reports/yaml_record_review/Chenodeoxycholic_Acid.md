# `data/ingredients/mapped/Chenodeoxycholic_Acid.yaml`

## Verdict

Pass. The CultureBotHT chenodeoxycholic-acid record is exactly grounded to
active `CHEBI:16755`, and its CAS, formula, InChI, SMILES, exact synonym, zero
occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Chenodeoxycholic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16755`,
  `ontology_mapping.ontology_id: CHEBI:16755`,
  `ontology_label: chenodeoxycholic acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:16755` returns one active ChEBI term labelled
  `chenodeoxycholic acid` with CAS `474-25-9`, formula `C24H40O4`, exact synonym
  `3alpha,7alpha-dihydroxy-5beta-cholan-24-oic acid`, and the same InChI and
  SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chenodeoxycholic_Acid.yaml data/ingredients/mapped/Chitin.yaml data/ingredients/mapped/Chitosan.yaml data/ingredients/mapped/Chloramphenicol.yaml data/ingredients/mapped/Chlorhexidine_Diacetate_Salt_Hydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chenodeoxycholic_Acid.yaml data/ingredients/mapped/Chitin.yaml data/ingredients/mapped/Chitosan.yaml data/ingredients/mapped/Chloramphenicol.yaml data/ingredients/mapped/Chlorhexidine_Diacetate_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Chenodeoxycholic_Acid` SSSOM row, the
  `CONFIRMED` row-review disposition, and matching aggregate and docs rows for
  `CHEBI:16755`.
- The active SSSOM row includes CAS `474-25-9` and the ChEBI-reviewed exact
  synonym already present in YAML.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:16755` rows,
  matching the explicit 0/0 `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, exact synonym, SSSOM
  row, aggregate copy, docs row, and zero occurrence count are populated and
  agree.
- No component, environment, or dataset entry is required for this concrete
  bile acid record.

## Recommended Edits

- None for this record.
