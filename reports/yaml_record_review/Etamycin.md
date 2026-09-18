# `data/ingredients/mapped/Etamycin.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The MeSH identity and
`Viridogrisein` synonym resolve to `mesh:C004910`, but the `SELECTIVE_AGENT`
role is supported only by a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Etamycin.yaml`.
- Identifier and grounding: `identifier: mesh:C004910` with matching
  `ontology_mapping.ontology_id`, canonical label `etamycin`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Fresh exact OLS4 queries against MeSH resolved both `Etamycin` and
  `Viridogrisein` to `mesh:C004910`; `Viridogrisein` appears as a related
  synonym on that same term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Etabetacin.yaml data/ingredients/mapped/Etamycin.yaml data/ingredients/mapped/Ethambutol.yaml data/ingredients/mapped/Ethambutol_Dihydrochloride.yaml data/ingredients/mapped/Ethanol.yaml --out /tmp/mim_eta_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Etamycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  MeSH identifier, `Viridogrisein` exact synonym, placeholder-upgrade history,
  and role facet as the per-record YAML.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `mesh:C004910` exactly to `etamycin`, and
  `mappings/ingredient_mappings_unknown_term_triage.tsv` records that the old
  UNKNOWN_TERM row was caused by missing prefix coverage in the earlier
  synonym-review OLS dispatcher.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Etamycin`
  to `mesh:C004910` with `skos:exactMatch`; its only `other` token is
  `Viridogrisein`, which is a MeSH synonym for the same object.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is asserted only from
  `COMPUTATIONAL_PREDICTION` with `reference_text: Inferred from curated
  media-role name pattern` and a provisional curator note. That evidence does
  not by itself establish that this ingredient was used as a selective agent in
  a reviewed medium.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Etamycin`,
  `mesh:C004910`, `MESH:C004910`, and `Viridogrisein` found the active YAML,
  aggregate copy, final SSSOM row, MeSH external-prefix validation, and
  expected UNKNOWN_TERM triage rows; it did not expose a contradictory active
  mapping.

## Completeness

- The exact MeSH identity, active synonym, and final SSSOM payload are
  populated.
- CAS RN, components, source occurrences, and environmental contexts are
  correctly empty.

## Recommended Edits

- Major: in `data/ingredients/mapped/Etamycin.yaml`, either replace the
  computational `SELECTIVE_AGENT` evidence with direct, source-backed role
  evidence for etamycin, or remove the role facet; then sync
  `data/curated/mapped_ingredients.yaml` and rerun strict validation plus the
  final SSSOM gates.
