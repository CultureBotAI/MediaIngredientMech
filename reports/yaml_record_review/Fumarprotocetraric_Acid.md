# `data/ingredients/mapped/Fumarprotocetraric_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed fumarprotocetraric acid row maps to the exact
ChEBI chemical, its PubChem identity agrees with the recorded structure fields,
and the final SSSOM row publishes only the valid CAS alias.

## Identity

- Reviewed record: `data/ingredients/mapped/Fumarprotocetraric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:144157` with matching
  `ontology_mapping.ontology_id`, canonical label `Fumarprotocetraric acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `489-50-9` resolved to CID 5317419 titled
  `Fumarprotocetraric Acid` with formula `C22H16O12` and the same InChI
  recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fumaric_Acid.yaml data/ingredients/mapped/Fumarprotocetraric_Acid.yaml data/ingredients/mapped/Fungichromin.yaml data/ingredients/mapped/Furaltadone_Hydrochloride.yaml data/ingredients/mapped/Furaxone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fumaric_Acid.yaml data/ingredients/mapped/Fumarprotocetraric_Acid.yaml data/ingredients/mapped/Fungichromin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary records in the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18012 CHEBI:144157 CHEBI:31639`:
  returned the active ChEBI label, formula, InChI, SMILES, and mass for
  `CHEBI:144157`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CultureBotHT source, structure fields, CAS RN, and
  ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fumarprotocetraric_Acid` to `CHEBI:144157` with `skos:exactMatch` and
  exports only `CAS:489-50-9` in `other`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the ChEBI row,
  and the row-review manifest marks it `CONFIRMED_NO_ACTION`.
- The record has no inferred nutritional, physicochemical, component, synonym,
  source-occurrence, or environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, and OAK/OLS row-review provenance.

## Completeness

- The exact fumarprotocetraric acid identity, single-ingredient type, structure
  fields, CAS RN, CultureBotHT provenance, and final SSSOM row are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
