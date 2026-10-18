# `data/ingredients/mapped/Glucuronate.yaml`

## Verdict

Pass. The MicrobeDecoder exact match to active `CHEBI:24297` glucuronate is
structurally consistent, the D-glucuronate stereospecific sibling remains a
separate record, the record has no unsupported roles, and the final SSSOM row
exports no `other` synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Glucuronate.yaml`.
- Identifier and grounding: `identifier: CHEBI:24297` with matching
  `ontology_mapping.ontology_id`, canonical label `glucuronate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C6H9O7` and molecular weight `193.132`,
  retrieved from ChEBI on 2026-08-13.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml data/ingredients/mapped/Glucose_Xylose.yaml data/ingredients/mapped/Glucose_Yeast_Extract.yaml data/ingredients/mapped/Glucuronamide.yaml data/ingredients/mapped/Glucuronate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Glucuronamide.yaml data/ingredients/mapped/Glucuronate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two ChEBI-primary records in this batch. Engine A was skipped
  for the three `kgmicrobe.ingredient` local fallback records because that
  private prefix is outside the OBO-only term validator.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact mapping, MicrobeDecoder source occurrence, formula,
  molecular weight, single-ingredient type, and empty synonym set as the
  per-record YAML.
- OLS4 resolves `CHEBI:24297` as `glucuronate`, matching the YAML
  `ontology_mapping`.
- `mappings/microbedecoder_auto_mapped_review.tsv` explicitly approved
  `Glucuronate.yaml` after the local OAK id resolved and its canonical label
  exact-matched the stored `ontology_label` case-insensitively.
- The sibling `data/ingredients/mapped/D-glucuronate.yaml` preserves the
  stereospecific `CHEBI:15748` D-glucuronate record separately; this generic
  glucuronate record is not being used for that D-form.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glucuronate` to `CHEBI:24297` by `skos:exactMatch`, keeps object label
  `glucuronate`, records the manual MicrobeDecoder approval, and leaves
  `other` empty.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, the MicrobeDecoder review row, the separate D-glucuronate sibling,
  generated indexes, old batch validation reports, and ignored aggregate
  backups.

## Completeness

- The exact glucuronate identity, formula, molecular weight, MicrobeDecoder
  source occurrence, ingredient type, and final SSSOM row are populated.

## Recommended Edits

- None.
