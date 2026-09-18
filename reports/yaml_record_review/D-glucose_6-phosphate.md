# `data/ingredients/mapped/D-glucose_6-phosphate.yaml`

## Verdict

Pass. The record is an exact active ChEBI match for D-glucose 6-phosphate, its
BacDive and CultureMech occurrence counts are traceable, it has no unsupported
roles, and the final SSSOM row has an empty `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/D-glucose_6-phosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:14314` with
  `ontology_mapping.ontology_id: CHEBI:14314`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:14314` to `D-glucose 6-phosphate` with formula
  `C6H13O9P`, charge `0`, and related synonyms
  `6-O-phosphono-D-glucose` and `D-glucose 6-(dihydrogen phosphate)`.
- The MicrobeDecoder source label is exactly `D-glucose 6-phosphate`, so the
  lexical match does not erase an alpha/beta ring form or a sodium salt.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-glucose_6-phosphate.yaml data/ingredients/mapped/D-glucuronate.yaml data/ingredients/mapped/D-glucuronic_Acid.yaml data/ingredients/mapped/D-glutamine.yaml data/ingredients/mapped/D-glycerate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucose_6-phosphate.yaml data/ingredients/mapped/D-glucuronate.yaml data/ingredients/mapped/D-glucuronic_Acid.yaml data/ingredients/mapped/D-glutamine.yaml data/ingredients/mapped/D-glycerate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:14314 CHEBI:15748 CHEBI:4178 CHEBI:17061 CHEBI:16659`:
  returned the expected `D-glucose 6-phosphate` label for `CHEBI:14314`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:14314 CHEBI:15748 CHEBI:4178 CHEBI:17061 CHEBI:16659`:
  returned formula, charge, mass, and related synonyms for `CHEBI:14314`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/ingredient_candidates.tsv` and
  `data/custom/microbedecoder/unmapped_labels.tsv` both contain the exact
  `D-glucose 6-phosphate` label with 68 BacDive utilization mentions, matching
  `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` contains one row for
  `CHEBI:14314`, matching `occurrence_statistics.media_count: 1` and
  `total_occurrences: 1`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-glucose_6-phosphate` to `CHEBI:14314` with `skos:exactMatch`,
  canonical object label `D-glucose 6-phosphate`, CHEBI object source, and an
  empty `other` column.
- The record does not assert nutritional roles, environmental contexts,
  synonyms, or mixture components, so there are no unsupported claim-specific
  evidence objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record for `CHEBI:14314`.
  `D-Glucose-6-Phosphate_Sodium_Salt` separately maps its CAS identity to
  `CHEBI:14314` with `NARROW_MATCH`, which preserves the salt as a distinct
  MIM subject rather than duplicating this record.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
