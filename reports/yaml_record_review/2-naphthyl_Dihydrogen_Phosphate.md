# `data/ingredients/mapped/2-naphthyl_Dihydrogen_Phosphate.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:91043` identity, chemistry,
microbedecoder occurrence count, SSSOM row, aggregate row, and docs pass; only
optional synonym enrichment and stale advisory rows remain.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-naphthyl_Dihydrogen_Phosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:91043` with
  `ontology_mapping.ontology_id: CHEBI:91043`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:91043`
  resolves to `2-naphthyl dihydrogen phosphate` and lists formula `C10H9O4P`.
- Formula, InChI, SMILES, and molecular weight are populated and exactly match
  the ChEBI structure fields.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-methyl-1-butanol.yaml data/ingredients/mapped/2-methyl-4-isothizaolin-3-one.yaml data/ingredients/mapped/2-n-Heptyl-4-hydroxyquinoline_N-oxide.yaml data/ingredients/mapped/2-naphthyl_Dihydrogen_Phosphate.yaml data/ingredients/mapped/2-naphthyl_Tetradecanoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-naphthyl_Dihydrogen_Phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-naphthyl_Dihydrogen_Phosphate` to `CHEBI:91043` row.

## Evidence

- The active ChEBI target confirms the exact naphthyl phosphate identity that
  older research rows treated as insufficiently verified.
- `data/custom/microbedecoder/unmapped_labels.tsv` has three occurrences for
  `kgmicrobe.trait:2_naphthyl_dihydrogen_phosphate`, matching the active
  `source_occurrences` entry.
- Stale: `mappings/record_research_validation.tsv` still contains old P1/P2/P3
  rows asking to demote the record or set `ingredient_type`; direct ChEBI
  verification now passes, `ingredient_type` is populated, and the non-media
  microbedecoder count is internally consistent.
- Non-blocking audit nit: `curation_history` is not timestamp-monotonic; the
  2026-08-04T00:00 review promotion follows later 2026-08-04 import and
  flag-for-review events.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the source
  microbedecoder row, active YAML/aggregate/SSSOM rows, and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- Official ChEBI synonyms such as `2-naphthyl phosphate` and
  `beta-naphthyl phosphate` could be added, but are optional enrichment.

## Recommended Edits

1. No required curation edit was found for
   `data/ingredients/mapped/2-naphthyl_Dihydrogen_Phosphate.yaml`.
2. Optionally add official ChEBI synonyms such as `2-naphthyl phosphate` and
   `beta-naphthyl phosphate` in a synonym-enrichment pass.
3. When stale advisory TSVs are next regenerated, confirm the obsolete
   `record_research_validation.tsv` rows drop out for this record.
