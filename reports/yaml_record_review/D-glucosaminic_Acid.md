# `data/ingredients/mapped/D-glucosaminic_Acid.yaml`

## Verdict

Pass with minor issues. The source label is a synonym of active
`CHEBI:17784`, its BacDive count is traceable, no unsupported role or SSSOM
synonym payload is present, and only the stale top-level import note should be
cleaned up.

## Identity

- Reviewed record: `data/ingredients/mapped/D-glucosaminic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:17784` with
  `ontology_mapping.ontology_id: CHEBI:17784`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- OLS resolved `CHEBI:17784` as active
  `2-amino-2-deoxy-D-gluconic acid` with formula `C6H13NO6`, charge `0`, and
  D-glucosaminate / D-glucosaminic acid synonyms.
- The stored formula, InChI, SMILES, and mass describe the same neutral
  D-glucosaminic-acid compound.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-glucarate.yaml data/ingredients/mapped/D-gluconate.yaml data/ingredients/mapped/D-glucosamine.yaml data/ingredients/mapped/D-glucosaminic_Acid.yaml data/ingredients/mapped/D-glucose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucosaminic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  `data/custom/microbedecoder/unmapped_labels.tsv` both contain the
  `D-glucosaminic acid` source label with 16 BacDive utilization mentions,
  matching `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:17784`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-glucosaminic_Acid` to `CHEBI:17784` with `skos:exactMatch`, canonical
  object label `2-amino-2-deoxy-D-gluconic acid`, CHEBI object source, and an
  empty `other` column.
- The record does not assert nutritional roles, environmental contexts, or
  mixture components, so there are no unsupported claim-specific evidence
  objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record for `CHEBI:17784`.
- The chemical-property block is complete for the active CHEBI small-molecule
  term.
- The top-level `notes` string still says no CAS-RN or CHEBI/NCIT match was
  found and curator review was needed even though the record is now mapped to
  `CHEBI:17784`.

## Recommended Edits

- In `data/ingredients/mapped/D-glucosaminic_Acid.yaml`, remove or refresh the
  stale top-level `notes` field.
- Regenerate synchronized curated products afterward, then rerun
  `uv run --frozen python scripts/validate_strict.py` and
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucosaminic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`.
