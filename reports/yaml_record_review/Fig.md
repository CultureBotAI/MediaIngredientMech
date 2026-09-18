# `data/ingredients/mapped/Fig.yaml`

## Verdict

Needs curation, with a major ingredient-type issue. The record maps the whole
fig material to the exact NCIT food term and has a clean final SSSOM row, but
an older NCIT-primary classifier marked the complex food as
`SINGLE_INGREDIENT`.

## Identity

- Reviewed record: `data/ingredients/mapped/Fig.yaml`.
- Identifier and grounding: `identifier: NCIT:C71971` with matching
  `ontology_mapping.ontology_id`, label `Fig`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- EBI OLS for NCIT resolves `NCIT:C71971` as `Fig`, marks it non-obsolete, and
  records semantic type `Food`.
- `scripts/demote_alphabet_letter_mapping.py` explicitly treats the `Fig`
  grounding as plausible, so this is not one of the alphabet-letter false
  positives the repository demoted elsewhere.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Feso4_X_H2o.yaml data/ingredients/mapped/Fetal_Bovine_Serum.yaml data/ingredients/mapped/Fibrin.yaml data/ingredients/mapped/Fidaxomicin.yaml data/ingredients/mapped/Fig.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fig.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  NCIT identifier, empty synonym list, occurrence counts, and stale
  `SINGLE_INGREDIENT` type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Fig` to
  `NCIT:C71971` with `skos:exactMatch` and an empty `other` column.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `NCIT:C71971` exactly through prefix-specific EBI OLS; the older
  `UNKNOWN_TERM` row in `mappings/ingredient_mappings_oak_ols_review.tsv` was
  a validator-prefix coverage gap, not a bad identifier.
- Major: `ingredient_type: SINGLE_INGREDIENT` came from the retired
  `auto_classify_ingredient_type` NCIT-primary heuristic. The current
  `scripts/classify_ingredient_type.py` no longer infers an ingredient type
  from NCIT alone, and a whole fig food is a complex material rather than a pure
  chemical-style single ingredient.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, NCIT OLS validation rows, row-review provenance,
  occurrence membership, the alphabet-letter false-positive guard, and ignored
  historical batch reports.

## Completeness

- The exact NCIT identity, occurrence counts, empty final SSSOM synonym payload,
  and lack of asserted roles are appropriate.
- The stale ingredient-type value is the consequential gap.

## Recommended Edits

- Major: change `ingredient_type` in `data/ingredients/mapped/Fig.yaml` from
  `SINGLE_INGREDIENT` to the curator-confirmed type for a complex food material,
  likely `UNDEFINED_MIXTURE`, sync `data/curated/mapped_ingredients.yaml`, and
  rerun strict validation plus the final SSSOM invariant gates.
