# `data/ingredients/mapped/2-naphthyl_Tetradecanoate.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:90249` identity, chemistry,
microbedecoder occurrence count, SSSOM row, aggregate row, and docs pass; only
optional `2-Naphthyl myristate` synonym enrichment and stale advisory rows
remain.

## Identity

- Reviewed record: `data/ingredients/mapped/2-naphthyl_Tetradecanoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:90249` with
  `ontology_mapping.ontology_id: CHEBI:90249`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:90249`
  resolves to `2-naphthyl tetradecanoate`, lists formula `C24H34O2`, and lists
  `2-Naphthyl myristate` as an exact synonym.
- Formula, InChI, SMILES, and molecular weight are populated and exactly match
  the ChEBI structure fields.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-methyl-1-butanol.yaml data/ingredients/mapped/2-methyl-4-isothizaolin-3-one.yaml data/ingredients/mapped/2-n-Heptyl-4-hydroxyquinoline_N-oxide.yaml data/ingredients/mapped/2-naphthyl_Dihydrogen_Phosphate.yaml data/ingredients/mapped/2-naphthyl_Tetradecanoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-naphthyl_Tetradecanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-naphthyl_Tetradecanoate` to `CHEBI:90249` row.

## Evidence

- The active ChEBI target confirms the exact neutral naphthyl tetradecanoate
  ester identity that older research rows treated as insufficiently verified.
- `data/custom/microbedecoder/unmapped_labels.tsv` has one occurrence for
  `kgmicrobe.trait:2_naphthyl_tetradecanoate`, matching the active
  `source_occurrences` entry.
- Minor: the official ChEBI page lists `2-Naphthyl myristate` and
  `2-Naphthylmyristate`, but the active YAML has no exact-synonym entries. The
  hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found no local representation
  of those labels outside a stale `record_research_validation.tsv` suggestion.
- Stale: `mappings/record_research_validation.tsv` still contains old P1/P2/P3
  rows asking to demote the record or set `ingredient_type`; direct ChEBI
  verification now passes and `ingredient_type` is populated.
- Non-blocking audit nit: `curation_history` is not timestamp-monotonic; the
  2026-08-04T00:00 review promotion follows later 2026-08-04 import and
  flag-for-review events.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- The missing `2-Naphthyl myristate` labels are optional ChEBI synonym
  enrichment, not an identity defect.

## Recommended Edits

1. No identity or structural curation edit is required for
   `data/ingredients/mapped/2-naphthyl_Tetradecanoate.yaml`.
2. Optionally add `2-Naphthyl myristate` and `2-Naphthylmyristate` as exact
   synonyms from ChEBI.
3. When stale advisory TSVs are next regenerated, confirm the obsolete
   identity and ingredient-type `record_research_validation.tsv` rows drop out
   for this record.
