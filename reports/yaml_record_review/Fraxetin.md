# `data/ingredients/mapped/Fraxetin.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed fraxetin row maps to the exact ChEBI
chemical, its PubChem identity agrees with the recorded structure fields, and
the final SSSOM row publishes only a valid ChEBI synonym plus the valid CAS
alias.

## Identity

- Reviewed record: `data/ingredients/mapped/Fraxetin.yaml`.
- Identifier and grounding: `identifier: CHEBI:5169` with matching
  `ontology_mapping.ontology_id`, canonical label `fraxetin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `574-84-5` resolved to CID 5273569 titled `Fraxetin`
  with formula `C10H8O5` and the same InChI recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fradicin.yaml data/ingredients/mapped/Framycetin.yaml data/ingredients/mapped/Fraxetin.yaml data/ingredients/mapped/Fructooligosaccharides_Fos.yaml data/ingredients/mapped/Fructose-6-phosphate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fradicin.yaml data/ingredients/mapped/Framycetin.yaml data/ingredients/mapped/Fraxetin.yaml data/ingredients/mapped/Fructose-6-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four OBO/external-prefix records in the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28645 CHEBI:15946 CHEBI:7508 CHEBI:5169`:
  returned the active ChEBI label, formula, InChI, SMILES, mass, and synonyms
  for `CHEBI:5169`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CultureBotHT source, structure fields, exact ChEBI synonym,
  CAS RN, and ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Fraxetin` to
  `CHEBI:5169` with `skos:exactMatch` and exports the same exact ChEBI synonym
  plus `CAS:574-84-5` in `other`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the ChEBI row,
  and the row-review manifest marks it `CONFIRMED_NO_ACTION`.
- The record has no inferred nutritional, physicochemical, component, synonym,
  source-occurrence, or environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, and OAK/OLS row-review provenance.

## Completeness

- The exact fraxetin identity, single-ingredient type, structure fields, CAS RN,
  CultureBotHT provenance, and final SSSOM row are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
