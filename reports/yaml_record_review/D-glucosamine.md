# `data/ingredients/mapped/D-glucosamine.yaml`

## Verdict

Pass. The record is an exact active ChEBI match for D-glucosamine, the BacDive
source count is traceable, there are no over-scoped roles or synonyms, and the
final SSSOM row is empty in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/D-glucosamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17315` with
  `ontology_mapping.ontology_id: CHEBI:17315`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolved `CHEBI:17315` as active `D-glucosamine` with formula `C6H13NO5`
  and charge `0`; the OLS synonyms include `2-amino-2-deoxy-D-glucose`,
  `D-GlcN`, and `D-glucosamine`.
- The MicrobeDecoder source label is exactly `D-glucosamine`, so the lexical
  mapping does not collapse an acetylated, phosphorylated, or salt form.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-glucarate.yaml data/ingredients/mapped/D-gluconate.yaml data/ingredients/mapped/D-glucosamine.yaml data/ingredients/mapped/D-glucosaminic_Acid.yaml data/ingredients/mapped/D-glucose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucosamine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  `D-glucosamine` label with 13 BacDive utilization mentions, matching
  `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:17315`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-glucosamine` to `CHEBI:17315` with `skos:exactMatch`, canonical object
  label `D-glucosamine`, CHEBI object source, and an empty `other` column.
- The record does not assert nutritional roles, environmental contexts,
  mixture components, or synonyms, so there are no unsupported claim-specific
  evidence objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record for `CHEBI:17315`.
- The chemical-property block carries the expected formula, InChI, mass,
  ChEBI+PubChem provenance, and retrieval date for the grounded ChEBI term.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
