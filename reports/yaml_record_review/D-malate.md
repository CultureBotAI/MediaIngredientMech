# `data/ingredients/mapped/D-malate.yaml`

## Verdict

Pass with minor issues. The record intentionally maps D-malate to the fully
deprotonated active ChEBI dianion, its BacDive count is traceable, the final
SSSOM row is clean, and only the stale top-level import note should be removed.

## Identity

- Reviewed record: `data/ingredients/mapped/D-malate.yaml`.
- Identifier and grounding: `identifier: CHEBI:15588` with
  `ontology_mapping.ontology_id: CHEBI:15588`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:15588` to `(R)-malate(2-)` with formula `C4H4O5`,
  charge `-2`, and `D-malate` as a related synonym.
- The stored formula, InChI, SMILES, and mass describe the same
  fully-deprotonated anion selected by #213.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-histidine.yaml data/ingredients/mapped/D-limonene.yaml data/ingredients/mapped/D-malate.yaml data/ingredients/mapped/D-mannitol.yaml data/ingredients/mapped/D-mannose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-histidine.yaml data/ingredients/mapped/D-malate.yaml data/ingredients/mapped/D-mannitol.yaml data/ingredients/mapped/D-mannose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-file CHEBI subset. `D-limonene` was skipped because its `cas:`
  fallback crashes the OAK SQL label lookup with
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27947 CHEBI:15588 CHEBI:16899 CHEBI:16024`:
  returned formula, charge, InChI, SMILES, mass, synonyms, and xrefs for
  `CHEBI:15588`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/ingredient_candidates.tsv` and
  `data/custom/microbedecoder/unmapped_labels.tsv` both contain the exact
  `D-malate` label with 33 BacDive utilization mentions, matching
  `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:15588`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:D-malate`
  to `CHEBI:15588` with `skos:exactMatch`, canonical object label
  `(R)-malate(2-)`, CHEBI object source, and an empty `other` column.
- The record does not assert nutritional roles, environmental contexts, or
  mixture components, so there are no unsupported claim-specific evidence
  objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record or parent-mapping record for
  `CHEBI:15588`.
- The chemical-property block is complete for the active CHEBI small-molecule
  anion.
- The top-level `notes` string still says no CAS-RN or CHEBI/NCIT match was
  found and curator review was needed even though the record is now mapped to
  `CHEBI:15588`.

## Recommended Edits

- In `data/ingredients/mapped/D-malate.yaml`, remove or refresh the stale
  top-level `notes` field.
- Regenerate synchronized curated products afterward, then rerun
  `uv run --frozen python scripts/validate_strict.py` and
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-malate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`.
