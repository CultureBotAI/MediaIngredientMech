# `data/ingredients/mapped/Formamicin.yaml`

## Verdict

Pass. The MicrobeDecoder formamicin import maps to the exact ChEBI metabolite,
the ChEBI/PubChem structure fields agree with PubChem, and the final SSSOM row
publishes no unsafe synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Formamicin.yaml`.
- Identifier and grounding: `identifier: CHEBI:203275` with matching
  `ontology_mapping.ontology_id`, canonical label `Formamicin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by name resolved CID 6474935 with formula `C44H72O13` and the
  same InChI recorded under `chemical_properties`.

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
  ChEBI identifier, structure-derived formula, SMILES, InChI, molecular weight,
  MicrobeDecoder source occurrence, and ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Formamicin` to `CHEBI:203275` with `skos:exactMatch` and an empty
  `other` column.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the row by exact
  local OAK label review, and the record has no inferred nutritional,
  physicochemical, component, or environment claim that would need independent
  support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports, found
  the active YAML, aggregate copy, final SSSOM row, MicrobeDecoder approval row,
  and ignored historical aggregate backups.

## Completeness

- The exact formamicin identity, structure fields, MicrobeDecoder source
  occurrence, ingredient type, and final SSSOM identity row are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
