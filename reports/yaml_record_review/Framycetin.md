# `data/ingredients/mapped/Framycetin.yaml`

## Verdict

Pass. The MicrobeDecoder import maps framycetin to the exact ChEBI chemical,
its ChEBI/PubChem structure fields agree with PubChem, and the final SSSOM row
publishes no unsafe synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Framycetin.yaml`.
- Identifier and grounding: `identifier: CHEBI:7508` with matching
  `ontology_mapping.ontology_id`, canonical label `framycetin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by the name `Framycetin` resolved to CID 8378 titled
  `Neomycin` with formula `C23H46N6O13` and the same InChI recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fradicin.yaml data/ingredients/mapped/Framycetin.yaml data/ingredients/mapped/Fraxetin.yaml data/ingredients/mapped/Fructooligosaccharides_Fos.yaml data/ingredients/mapped/Fructose-6-phosphate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fradicin.yaml data/ingredients/mapped/Framycetin.yaml data/ingredients/mapped/Fraxetin.yaml data/ingredients/mapped/Fructose-6-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four OBO/external-prefix records in the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28645 CHEBI:15946 CHEBI:7508 CHEBI:5169`:
  returned the active ChEBI label, formula, InChI, SMILES, mass, and synonyms
  for `CHEBI:7508`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, structure-derived formula, SMILES, InChI, molecular weight,
  MicrobeDecoder source occurrence, and ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Framycetin` to `CHEBI:7508` with `skos:exactMatch` and an empty `other`
  column.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the row by exact
  local OAK label review, and the record has no inferred nutritional,
  physicochemical, component, or environment claim that would need independent
  support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, MicrobeDecoder source rows, and MicrobeDecoder approval row.

## Completeness

- The exact framycetin identity, structure fields, MicrobeDecoder source
  occurrence, ingredient type, and final SSSOM identity row are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
