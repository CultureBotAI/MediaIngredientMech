# `data/ingredients/mapped/Fructose-6-phosphate.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The exact
fructose-6-phosphate identity, CAS-backed structure fields, ChEBI synonyms, and
final SSSOM payload pass, but `CARBON_SOURCE` is still only a provisional
computational prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Fructose-6-phosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:15946` with matching
  `ontology_mapping.ontology_id`, canonical label
  `keto-D-fructose 6-phosphate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `643-13-0` resolved to CID 69507 titled
  `Fructose 6-phosphate` with formula `C6H13O9P` and the same InChI recorded
  under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fradicin.yaml data/ingredients/mapped/Framycetin.yaml data/ingredients/mapped/Fraxetin.yaml data/ingredients/mapped/Fructooligosaccharides_Fos.yaml data/ingredients/mapped/Fructose-6-phosphate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fradicin.yaml data/ingredients/mapped/Framycetin.yaml data/ingredients/mapped/Fraxetin.yaml data/ingredients/mapped/Fructose-6-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four OBO/external-prefix records in the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28645 CHEBI:15946 CHEBI:7508 CHEBI:5169`:
  returned the active ChEBI label, formula, InChI, SMILES, mass, and synonyms
  for `CHEBI:15946`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, exact CultureBotHT CAS mapping, structure fields, exact
  ChEBI synonyms, CAS RN, ingredient type, and provisional carbon-source role
  as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fructose-6-phosphate` to `CHEBI:15946` with `skos:exactMatch` and
  exports the exact ChEBI synonyms plus `CAS:643-13-0` in `other`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the ChEBI row,
  and the row-review manifest marks it `CONFIRMED_NO_ACTION`.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from the curated media-role name pattern
  and the evidence note explicitly says the role is provisional.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, and OAK/OLS row-review provenance.

## Completeness

- The exact fructose-6-phosphate identity, single-ingredient type, PubChem
  structure, CAS RN, and final SSSOM identity row are populated.
- No component, environment, unsafe final synonym, or missing structure gap
  remains for the current ChEBI identity.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/Fructose-6-phosphate.yaml` with inspected
  source-backed evidence for this phosphorylated sugar in media, or remove the
  unsupported role; then sync `data/curated/mapped_ingredients.yaml` and rerun
  strict validation.
