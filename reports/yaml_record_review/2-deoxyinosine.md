# `data/ingredients/mapped/2-deoxyinosine.yaml`

## Verdict

Pass with minor issues. The active CAS-backed `CHEBI:28997` identity, chemistry,
FEBA occurrence count, SSSOM row, and aggregate copy pass; only stale advisory
rows still describe unresolved uncertainty.

## Identity

- Reviewed record: `data/ingredients/mapped/2-deoxyinosine.yaml`.
- Identifier and grounding: `identifier: CHEBI:28997` with
  `ontology_mapping.ontology_id: CHEBI:28997`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:28997`
  resolves to `2'-deoxyinosine`, lists `Deoxyinosine`, CAS `890-38-0`, and
  formula `C10H12N4O4`.
- The four FEBA media occurrences are represented in
  `occurrence_statistics`, and `mappings/culturemech_recipe_membership.tsv`
  lists four `CHEBI:28997` CultureMech recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-deoxyinosine.yaml data/ingredients/mapped/2-deoxythymidine-5-4-nitrophenyl_Phosphate.yaml data/ingredients/mapped/2-deoxyuridine.yaml data/ingredients/mapped/2-dichloroethane.yaml data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-deoxyinosine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-deoxyinosine` to `CHEBI:28997` row with the three curated synonyms and
  `CAS:890-38-0`.

## Evidence

- The active ChEBI target confirms the mapped identity, CAS RN, formula, exact
  synonyms, InChI, and SMILES.
- `mappings/ingredient_mappings_oak_ols_review.tsv` already records this row as
  `CONFIRMED`.
- Stale: `mappings/record_research_validation.tsv` still has an old Edison row
  recommending `UNMAPPED`; the current ChEBI page resolves and confirms
  `CHEBI:28997`.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `reports`
  found the active YAML/aggregate/SSSOM rows and stale advisory rows, with no
  live contradiction of the active `CHEBI:28997` identity.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, InChI, SMILES, and exact synonyms are populated for the active
  chemical form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale `CHEBI:28997` uncertainty no longer implies pending
   work.
2. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   `2-deoxyinosine` record.
