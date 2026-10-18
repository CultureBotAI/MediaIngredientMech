# `data/ingredients/mapped/2-oxobutanoate.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:16763` anion identity, chemistry,
microbedecoder occurrence count, SSSOM row, aggregate row, and docs pass; only
optional synonym enrichment and stale advisory rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/2-oxobutanoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16763` with
  `ontology_mapping.ontology_id: CHEBI:16763`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:16763`
  resolves to `2-oxobutanoate` and lists formula `C4H5O3`.
- Formula, InChI, SMILES, and molecular weight are populated and exactly match
  the ChEBI structure fields.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-oxobutanoate.yaml data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/2-oxopentanoate.yaml data/ingredients/mapped/2-pentyl-furan.yaml data/ingredients/mapped/2-propanolCO2.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-oxobutanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-oxobutanoate` to `CHEBI:16763` row.

## Evidence

- The active ChEBI target confirms the exact anion identity denoted by the
  source label.
- `data/custom/microbedecoder/unmapped_labels.tsv` has 146 occurrences for
  `kgmicrobe.trait:2_oxobutanoate`, matching the active `source_occurrences`
  entry.
- Stale: `mappings/record_research_validation.tsv` still contains old P3 rows
  requesting `ingredient_type` and chemical properties; both are now populated.
- Non-blocking audit nit: `curation_history` is not timestamp-monotonic; the
  2026-08-04T00:00 review promotion follows later 2026-08-04 import and
  flag-for-review events.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the source
  microbedecoder row, active YAML/aggregate/SSSOM rows, sibling sodium-salt
  parent mappings that intentionally point to the same anion, and stale
  advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI anion.
- Official or literature-backed aliases such as `alpha-ketobutyrate` and `AKB`
  would be optional synonym enrichment.

## Recommended Edits

1. No required curation edit was found for
   `data/ingredients/mapped/2-oxobutanoate.yaml`.
2. Optionally add exact aliases such as `alpha-ketobutyrate` in a
   synonym-enrichment pass after confirming they denote the anion here.
3. When stale advisory TSVs are next regenerated, confirm the obsolete
   `record_research_validation.tsv` rows drop out for this record.
