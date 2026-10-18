# `data/ingredients/mapped/Fusidate.yaml`

## Verdict

Pass. The MicrobeDecoder fusidate record maps to the exact active ChEBI anion,
its ChEBI-backed structure fields agree with the ontology term, and the final
SSSOM row does not publish any unsafe synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Fusidate.yaml`.
- Identifier and grounding: `identifier: CHEBI:71321` with matching
  `ontology_mapping.ontology_id`, canonical label `fusidate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:71321` as active ChEBI term `fusidate`, the conjugate
  base of fusidic acid, with formula `C31H47O6`, charge `-1`, the same InChI
  and SMILES recorded under `chemical_properties`, and related synonyms
  `fusidine` and `ramycin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Furazolidone.yaml data/ingredients/mapped/Furfuryl_Alcohol.yaml data/ingredients/mapped/Fusaric_Acid.yaml data/ingredients/mapped/Fusidate.yaml data/ingredients/mapped/Fusidic_Acid_Sodium_Salt.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Furazolidone.yaml data/ingredients/mapped/Furfuryl_Alcohol.yaml data/ingredients/mapped/Fusaric_Acid.yaml data/ingredients/mapped/Fusidate.yaml data/ingredients/mapped/Fusidic_Acid_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, MicrobeDecoder source, source-occurrence count, structure
  fields, and ingredient type as the per-record YAML.
- `mappings/microbedecoder_auto_mapped_review.tsv` explicitly approved this
  exact ChEBI row after OAK resolved the identifier and matched the canonical
  label.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Fusidate`
  to `CHEBI:71321` with `skos:exactMatch` and leaves `other` empty.
- The record has no inferred nutritional, physicochemical, component, synonym,
  or environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, MicrobeDecoder approval row, and MicrobeDecoder source rows.

## Completeness

- The exact fusidate identity, single-ingredient type, structure fields,
  MicrobeDecoder provenance, and final SSSOM row are populated.
- I found no consequential missing CAS, role, component, environment, or
  synonym payload.

## Recommended Edits

- None.
