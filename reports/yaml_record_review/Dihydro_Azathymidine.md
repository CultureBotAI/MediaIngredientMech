# `data/ingredients/mapped/Dihydro_Azathymidine.yaml`

## Verdict

Pass with minor issues. The local `kgmicrobe.compound:` placeholder remains
the documented identity for `Dihydro Azathymidine`, row review classifies it
as an expected registry identifier, and a fresh exact OLS search did not find
an external replacement. A separate 5,6-dihydro-5-azathymidine record still
mentions the same kg-microbe source ID in provenance and should be reviewed
for source-stream overlap.

## Identity

- Reviewed record: `data/ingredients/mapped/Dihydro_Azathymidine.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:dihydro_azathymidine` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Live EBI OLS exact search for `Dihydro Azathymidine` returned zero rows, so
  the local placeholder still has no exact OLS promotion target by that
  bounded check.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Digitonin.yaml data/ingredients/mapped/Digoxigenin.yaml data/ingredients/mapped/Dihydro_Azathymidine.yaml data/ingredients/mapped/Dihydrocelastrol.yaml data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Digitonin.yaml data/ingredients/mapped/Digoxigenin.yaml data/ingredients/mapped/Dihydrocelastrol.yaml data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 4-record CHEBI subset; this local
  `kgmicrobe.compound:` placeholder is outside Engine A's OBO prefix scope.
- `curl -L -sS --max-time 20 "https://www.ebi.ac.uk/ols/api/search?q=Dihydro%20Azathymidine&exact=true"`:
  returned 0 rows.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus
  plausibility warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected active local placeholder, generated/indexed copies,
  expected-registry row-review rows, and a provenance-only mention in
  `data/ingredients/mapped/56-dihydro-5-azathymidine.yaml`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` classify
  `kgmicrobe.compound:dihydro_azathymidine` as
  `expected_registry_identifier` and keep the local registry row pending exact
  external promotion.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dihydro_Azathymidine` to
  `kgmicrobe.compound:dihydro_azathymidine` with `skos:exactMatch`,
  kg-microbe compound object source, and no `other` tokens.

## Completeness

- The low-confidence CHEBI/NCIT candidate review, local placeholder
  rationale, 0/0 occurrence statistics, and manual no-promotion history are
  populated.
- Chemical properties, supplied forms, mixture components, ingredient roles,
  and environmental contexts are correctly empty while the exact identity
  remains local.

## Recommended Edits

- Minor: review whether
  `data/ingredients/mapped/56-dihydro-5-azathymidine.yaml` and
  `data/ingredients/mapped/Dihydro_Azathymidine.yaml` are intentionally
  separate despite sharing the `kgmicrobe.compound:dihydro_azathymidine`
  source ID in import provenance; if they came from the same upstream
  compound, merge or cross-reference through the maintained YAML and
  regenerated SSSOM surfaces.
