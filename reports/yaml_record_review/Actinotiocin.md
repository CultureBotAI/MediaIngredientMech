# `data/ingredients/mapped/Actinotiocin.yaml`

## Verdict

Pass with minor issues. The exact MeSH grounding, external-prefix OLS
validation, SSSOM row, and aggregate copy pass; one retained placeholder
evidence row and the old SSSOM trailer still reflect pre-upgrade unknown-term
state.

## Identity

- Reviewed record: `data/ingredients/mapped/Actinotiocin.yaml`.
- Identifier and grounding: `identifier: mesh:C006403` with
  `ontology_mapping.ontology_id: mesh:C006403`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `mesh:C006403` as the exact obo_id for `actinotiocin`.
- The record was auto-upgraded from the kg-microbe placeholder after an exact
  MeSH label match.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Actinomycin_D.yaml data/ingredients/mapped/Actinomycin_X.yaml data/ingredients/mapped/Actinotiocin.yaml data/ingredients/mapped/Activated_Charcoal.yaml data/ingredients/mapped/Adenine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Actinotiocin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:mesh aliases mesh:C041783 mesh:C006403`:
  reached the local MeSH adapter, but the adapter returned only stub `None`
  labels for both SCR terms.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` verifies
  the MeSH exact CURIE through prefix-specific EBI OLS validation.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` explains that the old
  `UNKNOWN_TERM` trailer came from missing prefix coverage in the earlier
  synonym-review dispatcher, not from a mapping defect.
- `mappings/ingredient_mappings.sssom.tsv` row 341 maps `MIM:Actinotiocin` to
  `mesh:C006403` with `skos:exactMatch`.
- The first `ontology_mapping.evidence` row is stale placeholder provenance: it
  still says the imported kg-microbe namespace was pending promotion after the
  record had already been upgraded to MeSH.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, prefix-validation row, unknown-term triage row, generated
  indexes, ignored aggregate backups, and stale advisory batch rows.

## Completeness

- No role, component, environmental context, discussion, or dataset entry is
  required.
- `chemical_properties` is correctly empty for a MeSH identity with no curated
  exact structure.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Actinotiocin.yaml`, either move the stale
  kg-microbe placeholder text out of `ontology_mapping.evidence` or rewrite it
  so the mapping evidence only describes the exact MeSH upgrade.
