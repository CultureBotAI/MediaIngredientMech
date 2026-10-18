# `data/ingredients/mapped/22-Dipyridyl.yaml`

## Verdict

Needs curation, major. The CAS-backed `CHEBI:30351` identity and chemistry pass,
but the `CHELATOR` role is still backed only by provisional ChEBI-ancestry
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/22-Dipyridyl.yaml`.
- Identifier and grounding: `identifier: CHEBI:30351` with
  `ontology_mapping.ontology_id: CHEBI:30351`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:30351`
  resolves to `2,2'-bipyridine`, lists formula `C10H8N2`, and contains the
  same structure represented in the YAML.
- Formula, InChI, and SMILES are populated and exactly match the ChEBI
  structure fields.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-undecanol.yaml data/ingredients/mapped/20AA_mix.yaml data/ingredients/mapped/22-Dipyridyl.yaml data/ingredients/mapped/22-dibromo-2-cyanoacetamide.yaml data/ingredients/mapped/2244688-heptamethylnonane.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/22-Dipyridyl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:22-Dipyridyl` to `CHEBI:30351` row, with `CAS:366-18-7` represented in
  the SSSOM `other` field.

## Evidence

- The active ChEBI term confirms the current CAS-backed identity.
- The July OAK/OLS row independently confirmed the same `CHEBI:30351` mapping.
- Major: the `physicochemical_roles` slot asserts `CHELATOR` at confidence
  `0.7` from only `COMPUTATIONAL_PREDICTION` evidence inferred from ChEBI
  ancestry, with a curator note that explicitly calls the role provisional and
  review-recommended.
- Stale: `mappings/record_research_validation.tsv` still contains an old P1 row
  asking to inspect `CHEBI:30351` directly before exporting the exact SSSOM row;
  direct ChEBI verification now passes.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, row-review manifest, and stale advisory
  rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- The role assertion remains consequential because generated users could read
  it as evidence-backed support for how this ingredient functions in a medium.

## Recommended Edits

1. In `data/ingredients/mapped/22-Dipyridyl.yaml`, either remove the provisional
   `CHELATOR` role or replace it with inspected formulation-specific evidence
   that directly supports the role for this exact ingredient.
2. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
3. Re-run the focused strict/LinkML validators and full role/evidence checks
   after the role edit.
