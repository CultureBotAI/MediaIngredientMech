# `data/ingredients/mapped/Dynemicin.yaml`

## Verdict

Needs curation. The old kg-microbe placeholder exact-matches active
`NCIT:C1928` Dynemicin through prefix-specific OLS, but the `SELECTIVE_AGENT`
role is still a provisional name-list inference and the final SSSOM row still
carries a stale `UNKNOWN_TERM` validation stamp.

## Identity

- Reviewed record: `data/ingredients/mapped/Dynemicin.yaml`.
- Identifier and grounding: `identifier: NCIT:C1928` with
  `ontology_mapping.ontology_id: NCIT:C1928`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Prefix-specific EBI OLS search resolves `NCIT:C1928` to active `Dynemicin`,
  an enediyne antitumor antibiotic class with exact synonym `Dynemicin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dry_Cow-manure.yaml data/ingredients/mapped/Duartin.yaml data/ingredients/mapped/Durhamycin.yaml data/ingredients/mapped/Dynemicin.yaml data/ingredients/mapped/Dyv_Metal_Solution.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dry_Cow-manure.yaml data/ingredients/mapped/Dynemicin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the ENVO and NCIT files. Duartin, Durhamycin, and DYV Metal Solution
  were skipped because they use `mesh:`, `cas:`, or local `kgmicrobe.*`
  identifiers outside this subset.
- Prefix-specific `curl -L 'https://www.ebi.ac.uk/ols4/api/search?q=NCIT:C1928&ontology=ncit'`:
  returned the current NCIT `Dynemicin` term.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `NCIT:C1928` found the active Dynemicin YAML, external-prefix
  OLS validation, expected stale `UNKNOWN_TERM` review rows, and the final SSSOM
  row.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  `NCIT:C1928` as `RESOLVED_EXACT_CURIE` with exact label `Dynemicin`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Dynemicin`
  to `NCIT:C1928` with `skos:exactMatch`, canonical object label `Dynemicin`,
  NCIT object source, and no `other` tokens.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists` and a
  provisional curator note. It is not source-backed.
- Minor: the final SSSOM row still has `validation_method` of
  `none|UNKNOWN_TERM|2026-07-07`, inherited from the older synonym-review
  dispatcher that lacked full prefix coverage.

## Completeness

- NCIT exact-match provenance is populated.
- CAS RN, structure fields, occurrences, supplied forms, mixture components,
  nutritional roles, biological roles, and environmental contexts are correctly
  empty.

## Recommended Edits

- Major: replace the `SELECTIVE_AGENT` computational role in
  `data/ingredients/mapped/Dynemicin.yaml` with source-backed role evidence
  scoped to dynemicin, or remove the role if no support is available; then
  synchronize `data/curated/mapped_ingredients.yaml`.
- Minor: refresh the Dynemicin SSSOM validation metadata from
  `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` so the final
  NCIT row no longer reports `UNKNOWN_TERM`.
