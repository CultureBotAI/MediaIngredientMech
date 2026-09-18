# `data/ingredients/mapped/Gluconate.yaml`

## Verdict

Pass. The MicrobeDecoder exact match to active `CHEBI:24265` gluconate is
structurally consistent, the record has no unsupported roles, and the final
SSSOM row exports no `other` synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Gluconate.yaml`.
- Identifier and grounding: `identifier: CHEBI:24265` with matching
  `ontology_mapping.ontology_id`, canonical label `gluconate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:24265` as active gluconate with formula `C6H11O7`,
  charge `-1`, and mass `195.147`, matching the YAML.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ginkgolide_A.yaml data/ingredients/mapped/Ginkgotoxin.yaml data/ingredients/mapped/Glebomycin.yaml data/ingredients/mapped/Glucomannan_Konjac.yaml data/ingredients/mapped/Gluconate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ginkgolide_A.yaml data/ingredients/mapped/Ginkgotoxin.yaml data/ingredients/mapped/Glebomycin.yaml data/ingredients/mapped/Gluconate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI/NCIT-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact mapping, MicrobeDecoder source occurrence, formula,
  mass, single-ingredient type, and empty synonym set as the per-record YAML.
- `mappings/microbedecoder_auto_mapped_review.tsv` explicitly approved
  `Gluconate.yaml` after the local OAK id resolved and its canonical label
  exact-matched the stored `ontology_label` case-insensitively.
- The final SSSOM row maps `MIM:Gluconate` to `CHEBI:24265` by
  `skos:exactMatch`, keeps object label `gluconate`, records the manual
  MicrobeDecoder approval, and leaves the `other` field empty.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM row, the MicrobeDecoder review row, sibling sodium/potassium gluconate
  records, the generated Yeast Extract + Gluconate local record, generated
  indexes, old batch validation reports, and ignored aggregate backups.

## Completeness

- The exact gluconate identity, formula, mass, MicrobeDecoder source occurrence,
  ingredient type, and final SSSOM row are populated.

## Recommended Edits

- None.
