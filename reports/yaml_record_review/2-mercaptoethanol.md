# `data/ingredients/mapped/2-mercaptoethanol.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:41218` identity, chemistry, occurrence
count, SSSOM row, aggregate row, and docs pass, but the record still asserts
`REDUCING_AGENT` from only provisional name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/2-mercaptoethanol.yaml`.
- Identifier and grounding: `identifier: CHEBI:41218` with
  `ontology_mapping.ontology_id: CHEBI:41218`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:41218`
  resolves to `mercaptoethanol`, lists CAS RN `60-24-2`, and lists formula
  `C2H6OS`.
- Formula, InChI, and SMILES are populated for the active ChEBI-backed
  ingredient.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-fucosyllactose.yaml data/ingredients/mapped/2-furoic_Acid.yaml data/ingredients/mapped/2-hydroxybutyrate.yaml data/ingredients/mapped/2-mercaptoethanesulfonate.yaml data/ingredients/mapped/2-mercaptoethanol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-mercaptoethanol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`
  and the synchronized `MIM:2-mercaptoethanol` to `CHEBI:41218` SSSOM row
  passed.

## Evidence

- The official ChEBI record supports the current mercaptoethanol identity and
  structure fields.
- `mappings/culturemech_recipe_membership.tsv` has five membership rows for
  `CHEBI:41218`, matching the active `total_media: 5` and `total_recipes: 5`.
- Major: the `physicochemical_roles` slot asserts `REDUCING_AGENT` at
  confidence `0.8` from only `COMPUTATIONAL_PREDICTION` evidence inferred from
  a curated media-role name pattern, with a curator note that explicitly calls
  the role provisional and review-recommended.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, and CultureMech membership rows plus stale advisory rows;
  it did not find independent formulation evidence supporting the asserted
  physicochemical role.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- The role assertion is the only consequential issue found in this pass.

## Recommended Edits

1. In `data/ingredients/mapped/2-mercaptoethanol.yaml`, either remove the
   provisional `REDUCING_AGENT` role or replace it with inspected
   formulation-specific evidence that directly supports this exact ingredient
   as a reducing agent.
2. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
3. Re-run the focused strict/LinkML validators and the full role/evidence
   checks after the role edit.
