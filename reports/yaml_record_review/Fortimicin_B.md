# `data/ingredients/mapped/Fortimicin_B.yaml`

## Verdict

Pass. The MicrobeDecoder import maps fortimicin B to the exact ChEBI chemical,
its ChEBI/PubChem structure fields agree with PubChem, and the final SSSOM row
publishes no unsafe synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Fortimicin_B.yaml`.
- Identifier and grounding: `identifier: CHEBI:81284` with matching
  `ontology_mapping.ontology_id`, canonical label `Fortimicin B`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by name resolved CID 5284518 titled `Fortimicin B` with
  formula `C15H32N4O5` and the same InChI recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Formatetrimethylamine.yaml data/ingredients/mapped/Formic_Acid.yaml data/ingredients/mapped/Fortimicin_B.yaml data/ingredients/mapped/Fosfomycin.yaml data/ingredients/mapped/Fosmidomycin_Sodium_Salt_Hydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Formic_Acid.yaml data/ingredients/mapped/Fortimicin_B.yaml data/ingredients/mapped/Fosfomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, structure-derived formula, SMILES, InChI, molecular weight,
  MicrobeDecoder source occurrence, and ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fortimicin_B` to `CHEBI:81284` with `skos:exactMatch` and an empty
  `other` column.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the row by exact
  local OAK label review, and the record has no inferred nutritional,
  physicochemical, component, or environment claim that would need independent
  support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, MicrobeDecoder source row, and MicrobeDecoder approval row.

## Completeness

- The exact fortimicin B identity, structure fields, MicrobeDecoder source
  occurrence, ingredient type, and final SSSOM identity row are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
