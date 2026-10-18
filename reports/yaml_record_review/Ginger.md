# `data/ingredients/mapped/Ginger.yaml`

## Verdict

Needs curation, with a major ingredient-type issue. The exact `NCIT:C66725`
Ginger grounding and final SSSOM row pass, but the record classifies the
fresh, dried, or processed plant rhizome as `SINGLE_INGREDIENT`.

## Identity

- Reviewed record: `data/ingredients/mapped/Ginger.yaml`.
- Identifier and grounding: `identifier: NCIT:C66725` with matching
  `ontology_mapping.ontology_id`, canonical label `Ginger`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS4 resolved `NCIT:C66725` as active Ginger, with synonyms `Ginger Rhizome`
  and `Ginger Root`, Semantic Type `Food`, UNII code `C5529G5JPQ`, and CAS
  Registry `84696-15-1`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gentisic_Acid.yaml data/ingredients/mapped/Geomycin.yaml data/ingredients/mapped/Gepotidacin.yaml data/ingredients/mapped/Geraniol.yaml data/ingredients/mapped/Ginger.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gentisic_Acid.yaml data/ingredients/mapped/Gepotidacin.yaml data/ingredients/mapped/Geraniol.yaml data/ingredients/mapped/Ginger.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI/NCIT-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same NCIT exact mapping, 3 CultureMech occurrences, empty synonym set,
  and `SINGLE_INGREDIENT` type as the per-record YAML.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `NCIT:C66725` exactly to Ginger, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records that the older
  `UNKNOWN_TERM` row was only a missing-prefix-validator-coverage issue.
- The final SSSOM row maps `MIM:Ginger` to `NCIT:C66725` by `skos:exactMatch`,
  with object label `Ginger` and empty `other`.
- Major: `ingredient_type: SINGLE_INGREDIENT` came from an older broad
  `NCIT primary (pharmaceutical)` heuristic. The resolved NCIT term is a fresh,
  dried, or processed ginger rhizome and not a single chemically defined
  ingredient.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM row, external-prefix OLS validation, generated indexes, stale batch
  validation reports from before prefix-specific OLS handling, and ignored
  aggregate backups.

## Completeness

- The exact Ginger identity, occurrence count, and final SSSOM row are
  populated.
- The ingredient type needs curator review.

## Recommended Edits

- Major: replace `ingredient_type: SINGLE_INGREDIENT` with a mixture/botanical
  type appropriate for processed ginger rhizome, then rerun strict validation.
