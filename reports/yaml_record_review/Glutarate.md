# `data/ingredients/mapped/Glutarate.yaml`

## Verdict

Pass with minor completeness gaps. The MicrobeDecoder exact match to active
`CHEBI:24329` glutarate and the final SSSOM row pass, but the record lacks the
single-ingredient classification and any structure snapshot for the chosen
ChEBI term.

## Identity

- Reviewed record: `data/ingredients/mapped/Glutarate.yaml`.
- Identifier and grounding: `identifier: CHEBI:24329` with matching
  `ontology_mapping.ontology_id`, canonical label `glutarate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glutamate.yaml data/ingredients/mapped/Glutamic_Acid.yaml data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml data/ingredients/mapped/Glutaraldehyde.yaml data/ingredients/mapped/Glutarate.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Glutamate.yaml data/ingredients/mapped/Glutamic_Acid.yaml data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml data/ingredients/mapped/Glutaraldehyde.yaml data/ingredients/mapped/Glutarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five ChEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact mapping, MicrobeDecoder source occurrence, and missing
  type and structure fields as the per-record YAML.
- OLS4 resolves `CHEBI:24329` as `glutarate`, matching the YAML
  `ontology_mapping`.
- `mappings/microbedecoder_auto_mapped_review.tsv` explicitly approved
  `Glutarate.yaml` after the local OAK id resolved and its canonical label
  exact-matched the stored `ontology_label` case-insensitively.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Glutarate`
  to `CHEBI:24329` by `skos:exactMatch`, keeps object label `glutarate`,
  records the manual MicrobeDecoder approval, and leaves `other` empty.
- Minor: `ingredient_type` is absent despite the exact ChEBI small-molecule
  identity.
- Minor: `chemical_properties` is absent, so the record has no local formula,
  mass, SMILES, or InChI snapshot for the chosen ChEBI term.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, the MicrobeDecoder review row, generated indexes, old batch validation
  reports, and ignored aggregate backups.

## Completeness

- The exact glutarate identity, MicrobeDecoder source occurrence, and final
  SSSOM row are populated.
- Ingredient type and structure properties need backfill.

## Recommended Edits

- Minor: add `ingredient_type: SINGLE_INGREDIENT` to
  `data/ingredients/mapped/Glutarate.yaml`.
- Minor: backfill `chemical_properties` from `CHEBI:24329` if ChEBI exposes a
  structure for the exact term.
