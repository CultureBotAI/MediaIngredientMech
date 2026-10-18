# `data/ingredients/mapped/Dopsisamine.yaml`

## Verdict

Pass with minor issues. The kg-microbe placeholder was correctly upgraded to the
exact MeSH `mesh:C048266` dopsisamine term through prefix-specific OLS, and the
final SSSOM row is an exact MeSH row with no noisy synonyms. The only residual
is a stale `UNKNOWN_TERM` validation stamp caused by the older
CHEBI-focused review dispatcher.

## Identity

- Reviewed record: `data/ingredients/mapped/Dopsisamine.yaml`.
- Identifier and grounding: `identifier: mesh:C048266` with
  `ontology_mapping.ontology_id: mesh:C048266`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Prefix-specific EBI OLS search resolves `mesh:C048266` to active
  `dopsisamine`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dodecanol.yaml data/ingredients/mapped/Dopamine_Hydrochloride.yaml data/ingredients/mapped/Dopsisamine.yaml data/ingredients/mapped/Doripenem.yaml data/ingredients/mapped/Dotriacontane.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dodecanol.yaml data/ingredients/mapped/Dopamine_Hydrochloride.yaml data/ingredients/mapped/Doripenem.yaml data/ingredients/mapped/Dotriacontane.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4 CHEBI files; `Dopsisamine.yaml` was skipped because `mesh:`
  identifiers are outside this CHEBI/OBO-focused batch.
- Prefix-specific `curl -L 'https://www.ebi.ac.uk/ols4/api/search?q=mesh:C048266&ontology=mesh'`:
  resolved `mesh:C048266` to `dopsisamine`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `mesh:C048266` found the active Dopsisamine YAML, the
  generated SSSOM row, the stale `UNKNOWN_TERM` row review, and the later
  external-prefix OLS validation row proving the exact MeSH resolution.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  `mesh:C048266` as `RESOLVED_EXACT_CURIE` with exact label `dopsisamine`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dopsisamine` to `mesh:C048266` with `skos:exactMatch`, MeSH object
  source, canonical object label `dopsisamine`, and no `other` tokens.
- Minor: the final SSSOM row still has `validation_method` of
  `none|UNKNOWN_TERM|2026-07-07`, inherited from the older synonym-review
  dispatcher that lacked full prefix coverage.

## Completeness

- The MeSH exact identity and its upgrade provenance from
  `kgmicrobe.compound:dopsisamine` are populated.
- CAS RN, structure fields, occurrences, supplied forms, mixture components,
  nutritional roles, physicochemical roles, biological roles, and environmental
  contexts are correctly empty.

## Recommended Edits

- Minor: refresh the Dopsisamine SSSOM validation metadata from
  `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` so the final
  row no longer reports `UNKNOWN_TERM`.
