# `data/ingredients/mapped/Flavensomycin.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The local
`kgmicrobe.compound:` placeholder is still justified because no exact external
OLS candidate or local duplicate is available, but `physicochemical_roles`
contains a provisional `SELECTIVE_AGENT` assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Flavensomycin.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:flavensomycin` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The 2026-05-10 placeholder review retained the local placeholder because the
  UNKNOWN_TERM no-hit review found no exact OLS candidate and no normalized
  local duplicate.
- A fresh exact EBI OLS search for `Flavensomycin` returned zero hits across
  indexed ontologies.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Flavensomycin.yaml data/ingredients/mapped/Flavin_Adenine_Dinucleotide.yaml data/ingredients/mapped/Flavofungin.yaml data/ingredients/mapped/Flavomycin.yaml data/ingredients/mapped/Flavone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Flavensomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed because the local placeholder `kgmicrobe.compound:flavensomycin` is
  intentionally outside the OAK/OLS ontology validation scope.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local placeholder identifier, empty synonyms, occurrence counts, ingredient
  type, review note, and provisional role evidence as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Flavensomycin` to `kgmicrobe.compound:flavensomycin` with
  `skos:exactMatch` and an empty `other` column.
- `mappings/ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv`
  records `NO_EXACT_CANDIDATE`, and
  `mappings/ingredient_mappings_unknown_term_nohit_review.tsv` records
  `NO_LOCAL_DUPLICATE_NO_OLS_CANDIDATE`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` was created by
  `infer_roles_from_name_lists` and has only `COMPUTATIONAL_PREDICTION`
  evidence with a curator note calling the name-pattern rule provisional.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, local-registry row-review provenance, placeholder
  no-hit review rows, and ignored historical batch reports.

## Completeness

- The local placeholder identity, occurrence counts, ingredient type, and empty
  final SSSOM synonym payload are populated.
- The record still needs source-backed evidence for the selective-agent role or
  removal of that role.

## Recommended Edits

- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` in
  `data/ingredients/mapped/Flavensomycin.yaml` with source-backed role evidence
  or remove the role, sync `data/curated/mapped_ingredients.yaml`, and rerun
  strict validation plus the final SSSOM invariant gates.
