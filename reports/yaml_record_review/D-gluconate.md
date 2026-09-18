# `data/ingredients/mapped/D-gluconate.yaml`

## Verdict

Pass. The record is an exact active ChEBI match for D-gluconate, its BacDive
source count is traceable, it has no unsupported role or synonym payloads, and
the final SSSOM row exports no stray `other` values.

## Identity

- Reviewed record: `data/ingredients/mapped/D-gluconate.yaml`.
- Identifier and grounding: `identifier: CHEBI:18391` with
  `ontology_mapping.ontology_id: CHEBI:18391`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolved `CHEBI:18391` as active `D-gluconate` with formula `C6H11O7`,
  charge `-1`, and D-gluconate synonyms; the stored formula, InChI, SMILES, and
  mass describe the same monoanion.
- The MicrobeDecoder source label is exactly `D-gluconate`, so the lexical
  mapping does not cross stereo, acid/anion, or salt boundaries.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-glucarate.yaml data/ingredients/mapped/D-gluconate.yaml data/ingredients/mapped/D-glucosamine.yaml data/ingredients/mapped/D-glucosaminic_Acid.yaml data/ingredients/mapped/D-glucose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-gluconate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/run_shared_evidence_validator.py`: unavailable
  because the sibling `culturebotai-claw` checkout was absent.

## Evidence

- `data/custom/microbedecoder/ingredient_candidates.tsv` and
  `data/custom/microbedecoder/unmapped_labels.tsv` both contain the exact
  `D-gluconate` label with 143 BacDive production/utilization mentions,
  matching `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:18391`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-gluconate` to `CHEBI:18391` with `skos:exactMatch`, canonical object
  label `D-gluconate`, CHEBI object source, and an empty `other` column.
- The record does not assert nutritional roles, environmental contexts,
  mixture components, or synonyms, so there are no unsupported claim-specific
  evidence objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found `CHEBI:18391` only as this record's primary mapping and as a
  component of `Yeast_Extract_Gluconate`; no second active primary record
  asserts the same identifier.
- The chemical-property block is complete for the ChEBI small-molecule anion
  fields used by this corpus.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
