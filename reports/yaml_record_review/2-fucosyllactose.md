# `data/ingredients/mapped/2-fucosyllactose.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:147155` identity passes, but the
record still asserts `CARBON_SOURCE` from only a provisional ChEBI-ancestry
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/2-fucosyllactose.yaml`.
- Identifier and grounding: `identifier: CHEBI:147155` with
  `ontology_mapping.ontology_id: CHEBI:147155`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:147155`
  resolves to `2'-fucosyllactose` and lists formula `C18H32O15`.
- CAS RN, formula, InChI, and SMILES are populated for the active ChEBI-backed
  ingredient.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-fucosyllactose.yaml data/ingredients/mapped/2-furoic_Acid.yaml data/ingredients/mapped/2-hydroxybutyrate.yaml data/ingredients/mapped/2-mercaptoethanesulfonate.yaml data/ingredients/mapped/2-mercaptoethanol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-fucosyllactose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`
  and the synchronized `MIM:2-fucosyllactose` to `CHEBI:147155` SSSOM row
  passed.

## Evidence

- The active ChEBI target confirms the exact oligosaccharide identity denoted
  by the record label.
- Major: the `nutritional_roles` slot asserts `CARBON_SOURCE` at confidence
  `0.7` from only `COMPUTATIONAL_PREDICTION` evidence inferred from the ChEBI
  carbohydrate hierarchy, with a curator note that explicitly calls the role
  provisional and review-recommended.
- A ChEBI class/has-role closure can identify this ingredient as a carbohydrate
  but does not prove that `2'-fucosyllactose` was intentionally supplied as a
  carbon source in a curated medium.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, and SSSOM rows plus stale advisory files; it did not find
  independent formulation evidence supporting the asserted nutritional role.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- The role assertion is the only consequential issue found in this pass.

## Recommended Edits

1. In `data/ingredients/mapped/2-fucosyllactose.yaml`, either remove the
   provisional `CARBON_SOURCE` role or replace it with inspected
   formulation-specific evidence that directly supports this exact ingredient
   as a carbon source.
2. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
3. Re-run the focused strict/LinkML validators and the full role/evidence
   checks after the role edit.
