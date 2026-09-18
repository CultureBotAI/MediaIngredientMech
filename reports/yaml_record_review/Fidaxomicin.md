# `data/ingredients/mapped/Fidaxomicin.yaml`

## Verdict

Pass. The record denotes fidaxomicin exactly, the ChEBI and PubChem structure
fields agree, and the final SSSOM row publishes only the identity mapping with
no unsafe synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Fidaxomicin.yaml`.
- Identifier and grounding: `identifier: CHEBI:68590` with matching
  `ontology_mapping.ontology_id`, canonical label `fidaxomicin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:68590` as `fidaxomicin`.
- PubChem lookup by name resolved CID 10034073 with formula `C52H74Cl2O18` and
  the same fidaxomicin InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Feso4_X_H2o.yaml data/ingredients/mapped/Fetal_Bovine_Serum.yaml data/ingredients/mapped/Fibrin.yaml data/ingredients/mapped/Fidaxomicin.yaml data/ingredients/mapped/Fig.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fidaxomicin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, structure-derived formula, SMILES, InChI, molecular weight,
  MicrobeDecoder source occurrence, and ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fidaxomicin` to `CHEBI:68590` with `skos:exactMatch` and an empty
  `other` column.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the row by exact
  local OAK label review, and the record has no inferred selective-agent,
  nutritional, physicochemical, component, or environment claim that would need
  independent support.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, MicrobeDecoder approval row, occurrence
  membership surfaces, and ignored historical batch reports.

## Completeness

- The exact fidaxomicin identity, structure fields, MicrobeDecoder source
  occurrence, ingredient type, and final SSSOM identity row are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
