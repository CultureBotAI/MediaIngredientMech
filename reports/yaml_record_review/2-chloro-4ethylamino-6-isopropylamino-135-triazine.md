# `data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml`

## Verdict

Pass with minor issues. The record denotes atrazine exactly through an exact
ChEBI synonym; remaining findings are stale advisory rows and optional chemistry
enrichment.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml`.
- Identifier and grounding: `identifier: CHEBI:15930` with
  `ontology_mapping.ontology_id: CHEBI:15930`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:15930`
  resolves to `atrazine` and lists formula `C8H14ClN5`, CAS `1912-24-9`, and
  ethylamino/isopropylamino triazine synonyms matching the source labels.
- The one CultureMech alias occurrence is represented as a raw synonym and the
  record's `occurrence_statistics` reports 1 occurrence in 1 medium.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-bromo-2-nitro-13-propanediol.yaml data/ingredients/mapped/2-butanolCO2.yaml data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml data/ingredients/mapped/2-dehydro-D-gluconate.yaml data/ingredients/mapped/2-deoxyadenosine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-chloro-4ethylamino-6-isopropylamino-135-triazine` to `CHEBI:15930`
  row with all three curated surface forms in `other`.

## Evidence

- The active ChEBI target confirms the atrazine identity, formula, CAS RN, and
  the synonym family used for the original mim-queue label and CultureMech alias.
- `mappings/culturemech_recipe_membership.tsv` lists exactly one
  `CHEBI:15930` CultureMech recipe, matching the active occurrence count.
- Stale: `mappings/record_research_validation.tsv` still contains old rows that
  requested direct current-CURIE validation and chemistry enrichment; ChEBI now
  confirms the target and formula.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `reports`
  found the active YAML/aggregate/SSSOM rows, the CultureMech alias triage row,
  and stale advisory rows, with no live contradiction of the active
  `CHEBI:15930` identity.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- InChI and molecular weight are populated; the ChEBI formula, SMILES, and CAS
  RN could be added later but are not required to understand the grounding.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. Optionally enrich `chemical_properties` with the active ChEBI formula,
   SMILES, and CAS RN in
   `data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml`.
2. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale `CHEBI:15930` uncertainty no longer implies pending
   work.
3. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   atrazine record.
