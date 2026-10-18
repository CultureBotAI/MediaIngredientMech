# `data/ingredients/mapped/Fusaric_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed fusaric acid row maps to the exact active
ChEBI chemical, the stored structure agrees with ChEBI and PubChem, and the
final SSSOM row publishes only the valid CAS alias.

## Identity

- Reviewed record: `data/ingredients/mapped/Fusaric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:5199` with matching
  `ontology_mapping.ontology_id`, canonical label `Fusaric acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:5199` as an active ChEBI term with formula
  `C10H13NO2`, InChI
  `InChI=1S/C10H13NO2/c1-2-3-4-8-5-6-9(10(12)13)11-7-8/h5-7H,2-4H2,1H3,(H,12,13)`,
  SMILES `CCCCc1ccc(C(=O)O)nc1`, and CAS xref `536-69-6`.
- PubChem lookup by CAS RN `536-69-6` resolved to CID 3442 with formula
  `C10H13NO2` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Furazolidone.yaml data/ingredients/mapped/Furfuryl_Alcohol.yaml data/ingredients/mapped/Fusaric_Acid.yaml data/ingredients/mapped/Fusidate.yaml data/ingredients/mapped/Fusidic_Acid_Sodium_Salt.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Furazolidone.yaml data/ingredients/mapped/Furfuryl_Alcohol.yaml data/ingredients/mapped/Fusaric_Acid.yaml data/ingredients/mapped/Fusidate.yaml data/ingredients/mapped/Fusidic_Acid_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CultureBotHT source, structure fields, CAS RN, and
  ingredient type as the per-record YAML.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the exact ChEBI
  row, and the row-review manifest marks it `CONFIRMED_NO_ACTION`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fusaric_Acid` to `CHEBI:5199` with `skos:exactMatch` and exports only
  `CAS:536-69-6` in `other`.
- The record has no inferred nutritional, physicochemical, component, synonym,
  source-occurrence, or environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, and OAK/OLS row-review provenance.

## Completeness

- The exact fusaric acid identity, single-ingredient type, structure fields, CAS
  RN, CultureBotHT provenance, and final SSSOM row are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
