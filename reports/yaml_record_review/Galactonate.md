# `data/ingredients/mapped/Galactonate.yaml`

## Verdict

Pass. The MicrobeDecoder galactonate record maps to the exact active ChEBI
class, the formula and source occurrence agree, and the final SSSOM row carries
no unsafe synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Galactonate.yaml`.
- Identifier and grounding: `identifier: CHEBI:24148` with matching
  `ontology_mapping.ontology_id`, canonical label `galactonate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:24148` as active ChEBI term `galactonate`, a monoanion
  class with formula `C6H11O7`, charge `-1`, and mass `195.147`, agreeing with
  the recorded `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Galactomannan_From_Guar.yaml data/ingredients/mapped/Galactonate.yaml data/ingredients/mapped/Galactose.yaml data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml data/ingredients/mapped/Galacturonate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Galactonate.yaml data/ingredients/mapped/Galactose.yaml data/ingredients/mapped/Galacturonate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, MicrobeDecoder source occurrence, structure fields, and
  ingredient type as the per-record YAML.
- `mappings/microbedecoder_auto_mapped_review.tsv` explicitly approved this
  exact ChEBI row after OAK resolved the identifier and matched the canonical
  label.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Galactonate` to `CHEBI:24148` with `skos:exactMatch` and leaves `other`
  empty.
- The record has no inferred nutritional, physicochemical, component, synonym,
  or environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, MicrobeDecoder approval row, generated indexes, and ignored aggregate
  backups.

## Completeness

- The exact galactonate identity, class-level formula and mass, MicrobeDecoder
  source occurrence, and final SSSOM row are populated.
- I found no consequential missing CAS, role, component, environment, or
  synonym payload.

## Recommended Edits

- None.
