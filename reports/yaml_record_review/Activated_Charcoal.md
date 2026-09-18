# `data/ingredients/mapped/Activated_Charcoal.yaml`

## Verdict

Pass with minor issues. The exact NCIT identity, occurrence count, SSSOM row,
and aggregate copy pass; only stale row-review output still reflects the
pre-fix NCIT prefix-dispatch gap.

## Identity

- Reviewed record: `data/ingredients/mapped/Activated_Charcoal.yaml`.
- Identifier and grounding: `identifier: NCIT:C77524` with
  `ontology_mapping.ontology_id: NCIT:C77524`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `NCIT:C77524` to `Activated Charcoal` and exact synonyms
  including `Activated Carbon`, `Activated Coal`, and `Medicinal Carbon`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` also
  resolves `NCIT:C77524` as the exact obo_id for `Activated Charcoal`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Actinomycin_D.yaml data/ingredients/mapped/Actinomycin_X.yaml data/ingredients/mapped/Actinotiocin.yaml data/ingredients/mapped/Activated_Charcoal.yaml data/ingredients/mapped/Adenine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Activated_Charcoal.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:ncit aliases NCIT:C77524`: returned the
  expected NCIT label and exact synonyms.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The mim-queue import preserved `source_id=mediadive.ingredient:582`, and the
  later occurrence refresh populated `13` distinct CultureMech recipes.
- `mappings/culturemech_recipe_membership.tsv` contains 13 rows for
  `NCIT:C77524`, matching `occurrence_statistics`.
- `mappings/ingredient_mappings.sssom.tsv` row 342 maps
  `MIM:Activated_Charcoal` to `NCIT:C77524` with `skos:exactMatch`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` explains that the old
  `UNKNOWN_TERM` trailer came from missing prefix coverage in the earlier
  synonym-review dispatcher, not from a mapping defect.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, prefix-validation row, occurrence rows, unknown-term triage
  row, generated indexes, ignored aggregate backups, and stale advisory batch
  rows.

## Completeness

- The occurrence statistics, NCIT grounding, curation history, and
  `ingredient_type` are populated.
- No role, component, chemical structure, environmental context, discussion, or
  dataset entry is required.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None for this record; the stale row-review `UNKNOWN_TERM` output should be
  refreshed through the maintained SSSOM review reports if those are reused.
