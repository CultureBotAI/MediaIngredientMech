# `data/ingredients/mapped/Formamide.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed formamide row maps to the exact ChEBI
chemical, its PubChem identity agrees with the recorded structure fields, and
the final SSSOM row publishes only the valid CAS alias.

## Identity

- Reviewed record: `data/ingredients/mapped/Formamide.yaml`.
- Identifier and grounding: `identifier: CHEBI:16397` with matching
  `ontology_mapping.ontology_id`, canonical label `formamide`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `75-12-7` resolved to CID 713 titled `Formamide`
  with formula `CH3NO` and the same InChI recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Folic_Acid.yaml data/ingredients/mapped/Folinic_Acid.yaml data/ingredients/mapped/Formaldehyde.yaml data/ingredients/mapped/Formamicin.yaml data/ingredients/mapped/Formamide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Folic_Acid.yaml data/ingredients/mapped/Folinic_Acid.yaml data/ingredients/mapped/Formaldehyde.yaml data/ingredients/mapped/Formamicin.yaml data/ingredients/mapped/Formamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed with no diagnostics for the 5-file batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CultureBotHT source, structure fields, CAS RN, and
  ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Formamide`
  to `CHEBI:16397` with `skos:exactMatch` and exports only `CAS:75-12-7` in
  `other`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the ChEBI row,
  and the row-review manifest marks it `CONFIRMED_NO_ACTION`.
- The record has no inferred nutritional, physicochemical, component, synonym,
  source-occurrence, or environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports, found
  the active YAML, aggregate copy, final SSSOM row, OAK/OLS row review, and
  ignored historical aggregate backups.

## Completeness

- The exact formamide identity, single-ingredient type, structure fields, CAS
  RN, CultureBotHT provenance, and final SSSOM row are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
