# `data/ingredients/mapped/2-mercaptoethanesulfonate.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:17905` coenzyme M identity and
occurrence count pass, but the record still contains non-label raw synonyms and
asserts `COFACTOR_PROVIDER` from unsupported in-session LLM evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/2-mercaptoethanesulfonate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17905` with
  `ontology_mapping.ontology_id: CHEBI:17905`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:17905`
  resolves to `coenzyme M`, lists CAS RN `3375-50-6`, and lists formula
  `C2H6O3S2`.
- Formula, InChI, and SMILES are populated for the active ChEBI-backed
  ingredient.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-fucosyllactose.yaml data/ingredients/mapped/2-furoic_Acid.yaml data/ingredients/mapped/2-hydroxybutyrate.yaml data/ingredients/mapped/2-mercaptoethanesulfonate.yaml data/ingredients/mapped/2-mercaptoethanol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-mercaptoethanesulfonate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`
  and the synchronized `MIM:2-mercaptoethanesulfonate` to `CHEBI:17905` SSSOM
  row passed.

## Evidence

- The official ChEBI record supports the current coenzyme M identity and
  structure fields.
- `mappings/culturemech_recipe_membership.tsv` has 79 membership rows for
  `CHEBI:17905`, matching the active occurrence count.
- Major: the `exact_synonyms` list contains raw source text that is not an
  ingredient label, including `Cross-references: KEGG:com`,
  `Role: Growth factor; Properties: Organic compound, Defined component, Simple component`,
  and `(sodium salt)`.
- Major: the `nutritional_roles` slot asserts `COFACTOR_PROVIDER` at confidence
  `0.6` from only `COMPUTATIONAL_PREDICTION` evidence whose summary is
  `Assigned by in-session Claude reasoning (no external API)`.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, and CultureMech membership rows. It also found
  `mappings/record_research_validation.tsv` already flagging the non-label
  synonym strings as stale raw text.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- The two residual issues are consequential because generated synonym outputs
  now include non-synonym text and the nutritional-role assertion is not backed
  by an inspected medium formulation.

## Recommended Edits

1. Remove non-label strings from
   `data/ingredients/mapped/2-mercaptoethanesulfonate.yaml` `exact_synonyms`;
   keep only true lexical variants such as `2-Mercaptoethanesulfonic acid
   (Coenzyme M)` if they are supported by source labels.
2. Either remove `COFACTOR_PROVIDER` or replace it with inspected
   formulation-specific evidence that directly supports this exact ingredient
   as a cofactor source.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
4. Re-run the focused strict/LinkML validators, synonym review, role/evidence
   checks, `just qc-sssom`, and `just qc-flat-coverage` after those edits.
