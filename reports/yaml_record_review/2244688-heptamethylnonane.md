# `data/ingredients/mapped/2244688-heptamethylnonane.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:131383` heptamethylnonane identity,
chemistry, occurrence count, SSSOM row, and aggregate row pass, but a role
description remains in `synonyms` and `CARBON_SOURCE` is only supported by
in-session LLM evidence.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2244688-heptamethylnonane.yaml`.
- Identifier and grounding: `identifier: CHEBI:131383` with
  `ontology_mapping.ontology_id: CHEBI:131383`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:131383`
  resolves to `2,2,4,4,6,8,8-heptamethylnonane` and lists formula `C16H34`.
- Formula, InChI, SMILES, CAS RN, and `heptamethylnonane`/`isocetane` synonyms
  are populated for the active ChEBI-backed ingredient.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-undecanol.yaml data/ingredients/mapped/20AA_mix.yaml data/ingredients/mapped/22-Dipyridyl.yaml data/ingredients/mapped/22-dibromo-2-cyanoacetamide.yaml data/ingredients/mapped/2244688-heptamethylnonane.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2244688-heptamethylnonane.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2244688-heptamethylnonane` to `CHEBI:131383` row, with
  `heptamethylnonane`, `isocetane`, and `CAS:4390-04-9` represented in the
  SSSOM `other` field.

## Evidence

- The active ChEBI term confirms the current exact identity and exact SSSOM row.
- `mappings/culturemech_recipe_membership.tsv` and the refreshed
  `occurrence_statistics` both report 12 CultureMech recipe occurrences.
- Major: `exact_synonyms` still contains the raw text `Role: Solvating media`,
  which is a role annotation rather than an ingredient label.
- Major: the `nutritional_roles` slot asserts `CARBON_SOURCE` at confidence
  `0.6` from only `COMPUTATIONAL_PREDICTION` evidence whose reference text is
  `Assigned by in-session Claude reasoning (no external API)`.
- Stale: `mappings/record_research_validation.tsv` still contains old P1/P2
  rows asking for direct `CHEBI:131383` verification before exporting an exact
  row; direct ChEBI verification now passes. The same TSV correctly flags the
  non-label raw synonym.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, CultureMech membership, OAK/OLS review, and advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- The residual issues are consequential because generated synonym outputs now
  include non-label role text and the nutritional-role assertion is not backed
  by inspected formulation evidence.

## Recommended Edits

1. Remove `Role: Solvating media` from
   `data/ingredients/mapped/2244688-heptamethylnonane.yaml` `exact_synonyms`.
2. Either remove `CARBON_SOURCE` or replace it with inspected
   formulation-specific evidence that directly supports this exact ingredient
   as a carbon source.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
4. Re-run the focused strict/LinkML validators, synonym review, role/evidence
   checks, `just qc-sssom`, and `just qc-flat-coverage` after those edits.
