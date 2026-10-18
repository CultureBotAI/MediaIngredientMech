# `data/ingredients/mapped/Fleroxacin.yaml`

## Verdict

Pass. The MicrobeDecoder import maps fleroxacin to the exact ChEBI chemical,
its ChEBI/PubChem structure fields agree with PubChem, and the final SSSOM row
publishes no unsafe synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Fleroxacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:31810` with matching
  `ontology_mapping.ontology_id`, canonical label `fleroxacin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by name resolved CID 3357 titled `Fleroxacin` with formula
  `C17H18F3N3O3` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fleroxacin.yaml data/ingredients/mapped/Flucloxacillin.yaml data/ingredients/mapped/Fluoranthene.yaml data/ingredients/mapped/Fluorene.yaml data/ingredients/mapped/Fluorescein.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fleroxacin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, structure-derived formula, SMILES, InChI, molecular weight,
  MicrobeDecoder source occurrence, and ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fleroxacin` to `CHEBI:31810` with `skos:exactMatch` and an empty
  `other` column.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the row by exact
  local OAK label review, and the record has no inferred selective-agent,
  nutritional, physicochemical, component, or environment claim that would need
  independent support.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, MicrobeDecoder approval row, and ignored
  historical batch reports.

## Completeness

- The exact fleroxacin identity, structure fields, MicrobeDecoder source
  occurrence, ingredient type, and final SSSOM identity row are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
