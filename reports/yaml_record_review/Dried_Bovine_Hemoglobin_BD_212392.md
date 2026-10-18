# `data/ingredients/mapped/Dried_Bovine_Hemoglobin_BD_212392.yaml`

## Verdict

Pass with minor issues. The CultureMech residual surface was correctly restored
as an exact synonym of `MICRO:0001599` dried bovine hemoglobin, the structured
mapping evidence now feeds the final SSSOM row, and the MICRO target resolves
through OLS. A stale residual-triage row still describes the old no-local-record
state.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Dried_Bovine_Hemoglobin_BD_212392.yaml`.
- Identifier and grounding: `identifier: MICRO:0001599` with
  `ontology_mapping.ontology_id: MICRO:0001599`, source `MICRO`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and 2
  CultureMech source occurrences.
- Prefix-specific EBI OLS search resolves `MICRO:0001599` to active
  `dried bovine hemoglobin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Doxorubicin.yaml data/ingredients/mapped/Doxorubicin_Hydrochloride.yaml data/ingredients/mapped/Doxycycline.yaml data/ingredients/mapped/Doxycycline_Hyclate.yaml data/ingredients/mapped/Dried_Bovine_Hemoglobin_BD_212392.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Doxorubicin.yaml data/ingredients/mapped/Doxorubicin_Hydrochloride.yaml data/ingredients/mapped/Doxycycline.yaml data/ingredients/mapped/Doxycycline_Hyclate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4 CHEBI files; `Dried_Bovine_Hemoglobin_BD_212392.yaml` was
  skipped because `MICRO:` identifiers are outside this CHEBI/OBO-focused
  batch.
- Prefix-specific `curl -L 'https://www.ebi.ac.uk/ols4/api/search?q=MICRO:0001599&ontology=micro'`:
  resolved `MICRO:0001599` to active `dried bovine hemoglobin`.
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
  `mappings` for `MICRO:0001599` and
  `Dried_Bovine_Hemoglobin_BD_212392` found the active per-record YAML, the
  maintained residual grounding row that created it, the stale residual-triage
  row, and the final SSSOM row.
- `mappings/culturemech_residual_groundings.tsv` records the BD 212392 surface
  as a new record grounded to `MICRO:0001599` by the exact
  `dried bovine hemoglobin` label.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dried_Bovine_Hemoglobin_BD_212392` to `MICRO:0001599` with
  `skos:exactMatch`, canonical object label `dried bovine hemoglobin`, MICRO
  object source, and structured CultureMech occurrence-table provenance.
- Minor: `mappings/culturemech_residual_triage.tsv` still contains the older
  triage row that described this surface as absent from the pinned MIM index.

## Completeness

- CultureMech source occurrence provenance and the 2/2 occurrence count are
  populated.
- CAS RN, structure fields, supplied forms, mixture components, nutritional
  roles, physicochemical roles, biological roles, and environmental contexts
  are correctly empty.

## Recommended Edits

- Minor: remove or refresh the stale
  `mappings/culturemech_residual_triage.tsv` row for
  `Dried Bovine Hemoglobin (BD 212392)` so it no longer describes this resolved
  residual as having no usable local identity.
