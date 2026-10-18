# `data/ingredients/mapped/Galacturonate.yaml`

## Verdict

Pass. The MicrobeDecoder galacturonate record maps to the exact active ChEBI
class, its source occurrence is retained, and the final SSSOM row carries no
unsafe synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Galacturonate.yaml`.
- Identifier and grounding: `identifier: CHEBI:24175` with matching
  `ontology_mapping.ontology_id`, canonical label `galacturonate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS4 resolved `CHEBI:24175` as an active ChEBI class with related synonym
  `galacturonates`.

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
  ChEBI identifier and MicrobeDecoder source occurrence as the per-record YAML.
- `mappings/microbedecoder_auto_mapped_review.tsv` explicitly approved this
  exact ChEBI row after OAK resolved the identifier and matched the canonical
  label.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Galacturonate` to `CHEBI:24175` with `skos:exactMatch` and leaves
  `other` empty.
- The record has no inferred nutritional, physicochemical, component, synonym,
  or environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, MicrobeDecoder approval row, generated indexes, and ignored aggregate
  backups.

## Completeness

- The exact galacturonate identity, MicrobeDecoder source occurrence, and final
  SSSOM row are populated.
- I found no consequential missing CAS, role, component, environment, or
  synonym payload.

## Recommended Edits

- None.
