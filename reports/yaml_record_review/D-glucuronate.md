# `data/ingredients/mapped/D-glucuronate.yaml`

## Verdict

Pass. The record is an exact active ChEBI match for D-glucuronate, the BacDive
source count is traceable, the CultureMech count is correctly zero, and the
published SSSOM row carries no stray synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/D-glucuronate.yaml`.
- Identifier and grounding: `identifier: CHEBI:15748` with
  `ontology_mapping.ontology_id: CHEBI:15748`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:15748` to `D-glucuronate` with formula `C6H9O7`,
  charge `-1`, and the KEGG xref `C00191`.
- The MicrobeDecoder source label is exactly `D-glucuronate`, so this record
  denotes the anion rather than the neutral acid or a salt formulation.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-glucose_6-phosphate.yaml data/ingredients/mapped/D-glucuronate.yaml data/ingredients/mapped/D-glucuronic_Acid.yaml data/ingredients/mapped/D-glutamine.yaml data/ingredients/mapped/D-glycerate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucose_6-phosphate.yaml data/ingredients/mapped/D-glucuronate.yaml data/ingredients/mapped/D-glucuronic_Acid.yaml data/ingredients/mapped/D-glutamine.yaml data/ingredients/mapped/D-glycerate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:14314 CHEBI:15748 CHEBI:4178 CHEBI:17061 CHEBI:16659`:
  returned the expected `D-glucuronate` label for `CHEBI:15748`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:14314 CHEBI:15748 CHEBI:4178 CHEBI:17061 CHEBI:16659`:
  returned formula, charge, mass, synonyms, and xrefs for `CHEBI:15748`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/ingredient_candidates.tsv` and
  `data/custom/microbedecoder/unmapped_labels.tsv` both contain the exact
  `D-glucuronate` label with 89 BacDive utilization mentions, matching
  `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:15748`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-glucuronate` to `CHEBI:15748` with `skos:exactMatch`, canonical object
  label `D-glucuronate`, CHEBI object source, and an empty `other` column.
- The record does not assert nutritional roles, environmental contexts,
  synonyms, or mixture components, so there are no unsupported claim-specific
  evidence objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record or parent-mapping record for
  `CHEBI:15748`.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
