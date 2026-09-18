# `data/ingredients/mapped/Cholic_Acid.yaml`

## Verdict

Pass. The CultureBotHT record is exactly grounded to active `CHEBI:16359`
`cholic acid`; its CAS, formula, InChI, SMILES, exact synonym, SSSOM row, zero
CultureMech occurrence count, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cholic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16359`,
  `ontology_mapping.ontology_id: CHEBI:16359`,
  `ontology_label: cholic acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct exact OLS lookup for `Cholic acid` returns active `CHEBI:16359`
  labelled `cholic acid` with the exact synonym
  `3alpha,7alpha,12alpha-trihydroxy-5beta-cholan-24-oic acid`.
- PubChem lookup of CAS `81-25-4` resolves to the same formula and standard
  InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chocolate_agar.yaml data/ingredients/mapped/Cholesterol_Lipid_Concentrate.yaml data/ingredients/mapped/Cholic_Acid.yaml data/ingredients/mapped/Cholin_Acetate.yaml data/ingredients/mapped/Choline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cholesterol_Lipid_Concentrate.yaml data/ingredients/mapped/Cholic_Acid.yaml data/ingredients/mapped/Choline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three CHEBI-scoped records in this narrowed run.
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
  `reports` found the active exact `MIM:Cholic_Acid` SSSOM row, the OAK/OLS
  row-review confirmation, matching aggregate/docs rows, and no QC report entry
  that flags this record.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:16359` or
  `MIM:Cholic_Acid` rows, matching the explicit 0/0 media-recipe
  `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, exact synonym, SSSOM
  row, zero occurrence count, aggregate copy, and docs row are populated and
  agree.

## Recommended Edits

- None for this record.
