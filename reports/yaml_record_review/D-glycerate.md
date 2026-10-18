# `data/ingredients/mapped/D-glycerate.yaml`

## Verdict

Pass with minor issues. The record is an exact active ChEBI match for
D-glycerate, the BacDive count is traceable, no unsupported role or SSSOM
synonym payload is present, and only the stale top-level import note should be
cleaned up.

## Identity

- Reviewed record: `data/ingredients/mapped/D-glycerate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16659` with
  `ontology_mapping.ontology_id: CHEBI:16659`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:16659` to `D-glycerate`, charge `-1`, formula
  `C3H5O4`, and structure metadata matching the record's stored formula,
  InChI, SMILES, and mass.
- The MicrobeDecoder source label is exactly `D-glycerate`; the record denotes
  the D glycerate anion and does not collapse L-glycerate or glyceric acid.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-glucose_6-phosphate.yaml data/ingredients/mapped/D-glucuronate.yaml data/ingredients/mapped/D-glucuronic_Acid.yaml data/ingredients/mapped/D-glutamine.yaml data/ingredients/mapped/D-glycerate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucose_6-phosphate.yaml data/ingredients/mapped/D-glucuronate.yaml data/ingredients/mapped/D-glucuronic_Acid.yaml data/ingredients/mapped/D-glutamine.yaml data/ingredients/mapped/D-glycerate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:14314 CHEBI:15748 CHEBI:4178 CHEBI:17061 CHEBI:16659`:
  returned the expected `D-glycerate` label for `CHEBI:16659`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:14314 CHEBI:15748 CHEBI:4178 CHEBI:17061 CHEBI:16659`:
  returned formula, charge, InChI, SMILES, mass, synonyms, and xrefs for
  `CHEBI:16659`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/ingredient_candidates.tsv` and
  `data/custom/microbedecoder/unmapped_labels.tsv` both contain the exact
  `D-glycerate` label with 2 BacDive utilization mentions, matching
  `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:16659`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-glycerate` to `CHEBI:16659` with `skos:exactMatch`, canonical object
  label `D-glycerate`, CHEBI object source, and an empty `other` column.
- The record does not assert nutritional roles, environmental contexts, or
  mixture components, so there are no unsupported claim-specific evidence
  objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record or parent-mapping record for
  `CHEBI:16659`.
- The chemical-property block is complete for the active CHEBI small-molecule
  anion.
- The top-level `notes` string still says no CAS-RN or CHEBI/NCIT match was
  found and curator review was needed even though the record is now mapped to
  `CHEBI:16659`.

## Recommended Edits

- In `data/ingredients/mapped/D-glycerate.yaml`, remove or refresh the stale
  top-level `notes` field.
- Regenerate synchronized curated products afterward, then rerun
  `uv run --frozen python scripts/validate_strict.py` and
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glycerate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`.
