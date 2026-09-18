# `data/ingredients/mapped/Flavone.yaml`

## Verdict

Pass. The record denotes flavone exactly, its CAS RN and structure fields agree
with PubChem, and the final SSSOM row carries only true same-substance synonym
payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Flavone.yaml`.
- Identifier and grounding: `identifier: CHEBI:42491` with matching
  `ontology_mapping.ontology_id`, canonical label `flavone`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `525-82-6` resolved to CID 10680 titled `Flavone`
  with formula `C15H10O2` and the same InChI recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Flavensomycin.yaml data/ingredients/mapped/Flavin_Adenine_Dinucleotide.yaml data/ingredients/mapped/Flavofungin.yaml data/ingredients/mapped/Flavomycin.yaml data/ingredients/mapped/Flavone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Flavone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, synonym, and ingredient
  type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Flavone` to
  `CHEBI:42491` with `skos:exactMatch`.
- The final SSSOM `other` column contains `2-PHENYL-4H-CHROMEN-4-ONE` and
  `CAS:525-82-6`, matching the curated exact synonym and
  `chemical_properties.cas_rn`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the ChEBI row
  as `CONFIRMED_NO_ACTION`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, OAK/OLS confirmation, and ignored historical
  batch reports.

## Completeness

- The exact ChEBI identity, CAS RN, structure fields, ingredient type, and final
  SSSOM synonym payload are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
