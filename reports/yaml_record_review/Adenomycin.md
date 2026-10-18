# `data/ingredients/mapped/Adenomycin.yaml`

## Verdict

Needs curation. The exact `NCIT:C221830` grounding is supported, but the
`SELECTIVE_AGENT` role is still only a provisional name-pattern assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Adenomycin.yaml`.
- Identifier and grounding: `identifier: NCIT:C221830` with
  `ontology_mapping.ontology_id: NCIT:C221830`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `NCIT:C221830` to `Adenomycin`, and
  `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` also
  resolves the exact NCIT CURIE.
- The 2026-05-23 source correction aligned `ontology_source: NCIT` with the
  NCIT CURIE.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml data/ingredients/mapped/Adenomycin.yaml data/ingredients/mapped/Adenosine.yaml data/ingredients/mapped/Adenosine_35-Cyclic_Monophosphate.yaml data/ingredients/mapped/Adenosine_5-monophosphate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Adenomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:ncit aliases NCIT:C221830`: returned the
  expected NCIT label and exact synonyms.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The local OAK NCIT adapter and prefix-specific OLS validation support the
  exact Adenomycin identity.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` explains that the old
  SSSOM `UNKNOWN_TERM` trailer came from missing NCIT prefix coverage in the
  earlier synonym-review dispatcher, not from a mapping defect.
- `mappings/ingredient_mappings.sssom.tsv` row 346 maps `MIM:Adenomycin` to
  `NCIT:C221830` with `skos:exactMatch`.
- The `physicochemical_roles.SELECTIVE_AGENT` row is only a name-pattern
  prediction; no inspected source supports adenomycin as a selective medium
  agent.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, prefix-validation row, unknown-term triage row, generated
  indexes, ignored aggregate backups, and stale advisory batch rows.

## Completeness

- No component, chemical structure, environmental context, discussion, or
  dataset entry is required for the NCIT identity.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Adenomycin.yaml`, remove or evidence the
  provisional `physicochemical_roles.SELECTIVE_AGENT` assertion, then run
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen python scripts/validate_component_partonomy.py`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
