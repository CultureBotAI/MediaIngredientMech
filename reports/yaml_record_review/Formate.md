# `data/ingredients/mapped/Formate.yaml`

## Verdict

Pass. The MicrobeDecoder import maps formate to the exact ChEBI anion, its
ChEBI/PubChem structure fields are populated, and the final SSSOM row publishes
no unsafe synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Formate.yaml`.
- Identifier and grounding: `identifier: CHEBI:15740` with matching
  `ontology_mapping.ontology_id`, canonical label `formate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The structure fields describe the formate anion with formula `CHO2`, SMILES
  `[H]C(=O)[O-]`, and a deprotonated formic-acid InChI, matching the ChEBI
  identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Formate.yaml data/ingredients/mapped/Formate3-methyl_Mercaptopropionate.yaml data/ingredients/mapped/Formatedimethylsulfide.yaml data/ingredients/mapped/Formatemethanol.yaml data/ingredients/mapped/Formatetetramethylammonium.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Formate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed with
  2,951 records, 83 decompositions, 505 components, and 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, structure-derived formula, SMILES, InChI, molecular weight,
  MicrobeDecoder source occurrence, and ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Formate` to
  `CHEBI:15740` with `skos:exactMatch` and an empty `other` column.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the row by exact
  local OAK label review, and the record has no inferred nutritional,
  physicochemical, component, or environment claim that would need independent
  support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, MicrobeDecoder approval row, and downstream formate-containing
  component decompositions.

## Completeness

- The exact formate identity, structure fields, MicrobeDecoder source
  occurrence, ingredient type, and final SSSOM identity row are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
