# `data/ingredients/mapped/2-hydroxybutyrate.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:64552` anion identity, chemistry,
SSSOM row, and aggregate row pass, but `source_occurrences` omits the absorbed
`Alpha-hydroxybutyrate` microbedecoder count.

## Identity

- Reviewed record: `data/ingredients/mapped/2-hydroxybutyrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:64552` with
  `ontology_mapping.ontology_id: CHEBI:64552`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:64552`
  resolves to `2-hydroxybutyrate` and lists formula `C4H7O3`.
- Formula, InChI, SMILES, and molecular weight are populated for the active
  anion form.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-fucosyllactose.yaml data/ingredients/mapped/2-furoic_Acid.yaml data/ingredients/mapped/2-hydroxybutyrate.yaml data/ingredients/mapped/2-mercaptoethanesulfonate.yaml data/ingredients/mapped/2-mercaptoethanol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-hydroxybutyrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed on a serial retry.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`
  and the synchronized `MIM:2-hydroxybutyrate` to `CHEBI:64552` SSSOM row
  passed.

## Evidence

- The active ChEBI target confirms the anion identity denoted by the record
  label.
- `data/custom/microbedecoder/unmapped_labels.tsv` has 150 occurrences for the
  direct `2_hydroxybutyrate` source row and 24 occurrences for the absorbed
  `alpha_hydroxybutyrate` source row. The active record only reports the 150
  direct-label occurrences.
- `mappings/ingredient_mappings.sssom.tsv` preserves `Alpha-hydroxybutyrate` in
  the `other` field, so the absorbed source label is represented as vocabulary
  but not in `occurrence_statistics`.
- `mappings/microbedecoder_residual_research_proposed.tsv` confirms
  `Alpha-hydroxybutyrate` should be merged as an already-mapped synonym.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the direct and absorbed
  microbedecoder rows, the active YAML/aggregate/SSSOM rows, and stale advisory
  rows about missing ChEBI and chemistry that are no longer live.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI anion.
- The missing absorbed-label occurrence count is consequential because
  `alpha_hydroxybutyrate` was a real source row, not optional ChEBI synonym
  vocabulary.

## Recommended Edits

1. In `data/ingredients/mapped/2-hydroxybutyrate.yaml`, update
   `occurrence_statistics.source_occurrences` so the microbedecoder count
   includes the absorbed 24-count `alpha_hydroxybutyrate` row in addition to
   the direct 150-count `2_hydroxybutyrate` row.
2. Run `just sync-curated`, `just validate-strict
   data/ingredients/mapped/2-hydroxybutyrate.yaml`, `just validate-terms
   data/ingredients/mapped/2-hydroxybutyrate.yaml`, `just qc-sssom`, and
   `just qc-flat-coverage` after that curation edit.
