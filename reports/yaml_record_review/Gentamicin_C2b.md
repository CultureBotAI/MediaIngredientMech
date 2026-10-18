# `data/ingredients/mapped/Gentamicin_C2b.yaml`

## Verdict

Pass. The MicrobeDecoder exact match to active `CHEBI:81283` Gentamicin C2b
is structurally consistent, the record has no unsupported roles, and the final
SSSOM row exports no `other` synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Gentamicin_C2b.yaml`.
- Identifier and grounding: `identifier: CHEBI:81283` with matching
  `ontology_mapping.ontology_id`, canonical label `Gentamicin C2b`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:81283` as active Gentamicin C2b with formula
  `C20H41N5O7`, mass `463.576`, and InChI/SMILES matching the YAML.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Geneticin_G418.yaml data/ingredients/mapped/Gentamicin.yaml data/ingredients/mapped/Gentamicin_C2b.yaml data/ingredients/mapped/Gentamicin_Sulfate_Salt.yaml data/ingredients/mapped/Gentibiose.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Geneticin_G418.yaml data/ingredients/mapped/Gentamicin.yaml data/ingredients/mapped/Gentamicin_C2b.yaml data/ingredients/mapped/Gentamicin_Sulfate_Salt.yaml data/ingredients/mapped/Gentibiose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact mapping, one MicrobeDecoder source occurrence, structure
  fields, single-ingredient type, and empty synonym set as the per-record YAML.
- `mappings/microbedecoder_auto_mapped_review.tsv` explicitly approved
  `Gentamicin_C2b.yaml` after the local OAK id resolved and its canonical label
  exact-matched the stored `ontology_label` case-insensitively.
- The final SSSOM row maps `MIM:Gentamicin_C2b` to `CHEBI:81283` by
  `skos:exactMatch`, keeps object label `Gentamicin C2b`, records the manual
  MicrobeDecoder approval, and leaves the `other` field empty.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM row, the MicrobeDecoder review row, generated indexes, old batch
  validation reports, and ignored aggregate backups.

## Completeness

- The exact Gentamicin C2b identity, structure fields, MicrobeDecoder source
  occurrence, ingredient type, and final SSSOM row are populated.

## Recommended Edits

- None.
