# `data/ingredients/mapped/3-Hydroxypropanal.yaml`

## Verdict

Needs curation, minor. The restored CultureMech residual grounding to
`CHEBI:17871` passes and exports, but the record has not been post-processed
with `ingredient_type` or ChEBI chemistry.

## Identity

- Reviewed record: `data/ingredients/mapped/3-Hydroxypropanal.yaml`.
- Identifier and grounding: `identifier: CHEBI:17871` with
  `ontology_mapping.ontology_id: CHEBI:17871`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:17871`
  resolves to `3-hydroxypropanal` and lists formula `C3H6O2`.
- The structured evidence points back to the CultureMech occurrence table and
  the creation history documents an exact match against the ChEBI ontology
  label.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Hydroxypropanal.yaml data/ingredients/mapped/3-Hydroxypropionate.yaml data/ingredients/mapped/3-Methyl-2-Oxobutanoic_Acid.yaml data/ingredients/mapped/3-Methyl-2-oxobutanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/3-Methylcatechol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-Hydroxypropanal.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-Hydroxypropanal` to `CHEBI:17871` row.

## Evidence

- The active ChEBI page verifies that `CHEBI:17871` is current for the exact
  aldehyde named by the record.
- `occurrence_statistics` reports one CultureMech occurrence in one medium.
- `mappings/culturemech_residual_groundings.tsv` and
  `mappings/culturemech_residual_triage.tsv` record the source residual and
  target `CHEBI:17871` decision.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, CultureMech residual grounding, residual-triage, and batch
  advisory rows.

## Completeness

- Minor: `ingredient_type` is absent.
- Minor: ChEBI-backed formula, InChI, and SMILES have not been backfilled.
- There is no evidence that the active exact mapping itself is stale or
  over-broad.

## Recommended Edits

1. Set `ingredient_type: SINGLE_INGREDIENT`.
2. Backfill formula `C3H6O2`, InChI, and SMILES from ChEBI.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
4. Re-run the focused strict/LinkML validators, `just qc-sssom`, and
   `just qc-flat-coverage` after those edits.
