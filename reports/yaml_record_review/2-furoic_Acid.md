# `data/ingredients/mapped/2-furoic_Acid.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:30845` identity, chemistry, occurrence
count, SSSOM row, aggregate row, and docs all pass; only stale advisory rows
remain outside the record.

## Identity

- Reviewed record: `data/ingredients/mapped/2-furoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30845` with
  `ontology_mapping.ontology_id: CHEBI:30845`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:30845`
  resolves to `2-furoic acid`, lists CAS RN `88-14-2`, and lists formula
  `C5H4O3`.
- Formula, InChI, SMILES, and exact synonyms are populated for the active acid.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-fucosyllactose.yaml data/ingredients/mapped/2-furoic_Acid.yaml data/ingredients/mapped/2-hydroxybutyrate.yaml data/ingredients/mapped/2-mercaptoethanesulfonate.yaml data/ingredients/mapped/2-mercaptoethanol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-furoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`
  and the synchronized `MIM:2-furoic_Acid` to `CHEBI:30845` SSSOM row passed.

## Evidence

- The official ChEBI record supports the current identifier, exact label, CAS
  RN, formula, InChI, and SMILES.
- `mappings/culturemech_recipe_membership.tsv` has two membership rows for
  `CHEBI:30845`, matching the active `total_media: 2` and
  `total_recipes: 2`.
- Stale: `mappings/record_research_validation.tsv` still contains advisory rows
  from before the active ChEBI grounding and chemistry were populated.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found only the active YAML,
  aggregate, SSSOM, CultureMech membership, and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- Empty component slots are acceptable for this single chemical.

## Recommended Edits

1. No curation edit is required for `data/ingredients/mapped/2-furoic_Acid.yaml`.
2. When stale advisory TSVs are next regenerated, confirm the obsolete
   `record_research_validation.tsv` rows drop out for this record.
