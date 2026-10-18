# `data/ingredients/mapped/3-Aminophenol.yaml`

## Verdict

Needs curation, minor. The restored CultureMech residual grounding to
`CHEBI:28924` passes and exports, but the record has not been post-processed
with `ingredient_type` or ChEBI chemistry.

## Identity

- Reviewed record: `data/ingredients/mapped/3-Aminophenol.yaml`.
- Identifier and grounding: `identifier: CHEBI:28924` with
  `ontology_mapping.ontology_id: CHEBI:28924`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:28924`
  resolves to `3-aminophenol`, lists formula `C6H7NO`, carries CAS `591-27-5`,
  and has InChI/SMILES for the exact aminophenol isomer.
- The structured evidence points back to the CultureMech occurrence table and
  the creation history documents an exact match against the ChEBI ontology
  label.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/24-Dinitrophenol.yaml data/ingredients/mapped/24-diamino-67-di-iso-propylpteridine_phosphate.yaml data/ingredients/mapped/25-Dihydroxy-4-Methoxychalcone.yaml data/ingredients/mapped/3-Aminophenol.yaml data/ingredients/mapped/3-Aminopropionitrile_Fumarate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-Aminophenol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-Aminophenol` to `CHEBI:28924` row.

## Evidence

- The active ChEBI page verifies that `CHEBI:28924` is current for the exact
  3-aminophenol isomer named by the record.
- `occurrence_statistics` reports one CultureMech occurrence in one medium,
  matching the post-#337 refresh.
- `mappings/culturemech_residual_groundings.tsv` and
  `mappings/culturemech_residual_triage.tsv` record the source residual and
  target `CHEBI:28924` decision.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, CultureMech residual grounding, residual-triage, and batch
  advisory rows.

## Completeness

- Minor: `ingredient_type` is absent.
- Minor: ChEBI-backed CAS RN, formula, InChI, and SMILES have not been
  backfilled.
- There is no evidence that the active exact mapping itself is stale or
  over-broad.

## Recommended Edits

1. Set `ingredient_type: SINGLE_INGREDIENT`.
2. Backfill CAS RN `591-27-5`, formula `C6H7NO`, InChI, and SMILES from ChEBI.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
4. Re-run the focused strict/LinkML validators, `just qc-sssom`, and
   `just qc-flat-coverage` after those edits.
