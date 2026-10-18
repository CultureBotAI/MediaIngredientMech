# `data/ingredients/mapped/2-bromo-2-nitro-13-propanediol.yaml`

## Verdict

Pass with minor issues. The record denotes Bronopol exactly through a
CAS-backed `CHEBI:31306` mapping; only stale advisory rows still describe
pre-verification uncertainty.

## Identity

- Reviewed record: `data/ingredients/mapped/2-bromo-2-nitro-13-propanediol.yaml`.
- Identifier and grounding: `identifier: CHEBI:31306` with
  `ontology_mapping.ontology_id: CHEBI:31306`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:31306`
  resolves to `Bronopol` and lists the `2-bromo-2-nitro...` synonym, CAS
  `52-51-7`, and formula `C3H6BrNO4`.
- The 2026-08-24 regrade correctly preserves the explicit CAS lookup
  provenance and leaves the own-identifier SSSOM row as `skos:exactMatch`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-bromo-2-nitro-13-propanediol.yaml data/ingredients/mapped/2-butanolCO2.yaml data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml data/ingredients/mapped/2-dehydro-D-gluconate.yaml data/ingredients/mapped/2-deoxyadenosine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-bromo-2-nitro-13-propanediol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-bromo-2-nitro-13-propanediol` to `CHEBI:31306` row with `CAS:52-51-7`.

## Evidence

- The active ChEBI target confirms the mapped identity, preferred target label,
  CAS RN, and formula for Bronopol.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` already determined
  that the proposed `2-bromo-2-nitro-1,3-propanediol` surface form is represented
  by `preferred_term`.
- Stale: `mappings/record_research_validation.tsv` still contains old rows that
  asked for direct ChEBI verification before trusting `CHEBI:31306`; the current
  ChEBI page resolves the term and confirms the CAS-grounded structure.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `reports`
  found the active YAML/aggregate/SSSOM rows and stale advisory rows, with no
  live contradiction of the active `CHEBI:31306` identity.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, InChI, and SMILES are populated for the active chemical form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale `CHEBI:31306` uncertainty no longer implies pending
   work.
2. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   `2-bromo-2-nitro-13-propanediol` record.
