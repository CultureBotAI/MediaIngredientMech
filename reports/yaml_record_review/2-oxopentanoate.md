# `data/ingredients/mapped/2-oxopentanoate.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:28644` anion identity, chemistry,
microbedecoder occurrence count, SSSOM row, aggregate row, and docs pass; only
stale advisory rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/2-oxopentanoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:28644` with
  `ontology_mapping.ontology_id: CHEBI:28644`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:28644`
  resolves to `2-oxopentanoate` and lists formula `C5H7O3`.
- Formula, InChI, SMILES, and molecular weight are populated and exactly match
  the ChEBI structure fields.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-oxobutanoate.yaml data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/2-oxopentanoate.yaml data/ingredients/mapped/2-pentyl-furan.yaml data/ingredients/mapped/2-propanolCO2.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-oxopentanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-oxopentanoate` to `CHEBI:28644` row.

## Evidence

- The active ChEBI target confirms the exact anion identity denoted by the
  source label.
- `data/custom/microbedecoder/unmapped_labels.tsv` has 164 occurrences for
  `kgmicrobe.trait:2_oxopentanoate`, matching the active `source_occurrences`
  entry.
- Stale: `mappings/record_research_validation.tsv` still contains old P1/P2
  rows treating the source trait as charge-state ambiguous and an old P3 row
  asking for `ingredient_type`; the active microbedecoder label is already the
  anion label, and `ingredient_type` is populated.
- Non-blocking audit nit: `curation_history` is not timestamp-monotonic; the
  2026-08-04T00:00 review promotion follows later 2026-08-04 import and
  flag-for-review events.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the source
  microbedecoder row, active YAML/aggregate/SSSOM rows, and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI anion.
- Empty component slots are acceptable for this single chemical.

## Recommended Edits

1. No curation edit is required for
   `data/ingredients/mapped/2-oxopentanoate.yaml`.
2. When stale advisory TSVs are next regenerated, confirm the obsolete
   `record_research_validation.tsv` rows drop out for this record.
