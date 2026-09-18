# `data/ingredients/mapped/DNA_From_Salmon.yaml`

## Verdict

Pass. `DNA from Salmon` is represented as a CAS fallback because no exact OLS
term or PubChem CID currently resolves for the label or CAS value, it has no
unsupported role assertions, and the final SSSOM row publishes only the
structured CAS token.

## Identity

- Reviewed record: `data/ingredients/mapped/DNA_From_Salmon.yaml`.
- Identifier and grounding: `identifier: cas:438545-06-3` with
  `ontology_mapping.ontology_id: cas:438545-06-3`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- Live OLS exact search for `DNA from Salmon` returned zero hits.
- PubChem returned `No CID found` for `438545-06-3`, so there is no active
  PubChem structure to promote over the CultureBotHT CAS fallback.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/DL_Vitamins.yaml data/ingredients/mapped/DNA_From_Salmon.yaml data/ingredients/mapped/D_-carvone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/DL_Vitamins.yaml data/ingredients/mapped/DNA_From_Salmon.yaml data/ingredients/mapped/D_-carvone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed when non-OBO fallback targets were included.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/D_-carvone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 3-file ChEBI subset after skipping this `cas:` fallback and the
  `DL_Vitamins` kg-microbe fallback.
- `curl -L ... q=DNA%20from%20Salmon&exact=true`: live OLS returned zero exact
  hits.
- `curl -L ... /compound/name/438545-06-3/property/.../JSON`: PubChem returned
  no CID for the CAS value.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `cas:438545-06-3`, matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the CAS
  object as `expected_registry_identifier`, matching the current local fallback
  identity.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:DNA_From_Salmon` to `cas:438545-06-3` with `skos:exactMatch`, object
  source `registry:cas`, and only `CAS:438545-06-3` in `other`.
- The record does not assert synonyms, nutritional roles, environmental
  contexts, or mixture components, so there are no unsupported claim-specific
  evidence objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `cas:438545-06-3`.
- The PubChem negative result is bounded to the registry value and supports
  leaving formula, InChI, SMILES, and PubChem CID empty.
- No parent mapping is required because the live OLS exact label search did not
  find an ontology term for salmon DNA.

## Recommended Edits

- None.
