# `data/ingredients/mapped/24-Dichlorophenoxyacetic_acid.yaml`

## Verdict

Needs curation, minor. The restored CultureMech residual grounding to
`CHEBI:28854` passes and exports, but the record has not been post-processed
with `ingredient_type` or ChEBI chemistry.

## Identity

- Reviewed record:
  `data/ingredients/mapped/24-Dichlorophenoxyacetic_acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:28854` with
  `ontology_mapping.ontology_id: CHEBI:28854`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:28854`
  resolves to `2,4-D`, lists formula `C8H6Cl2O3`, carries IUPAC
  `(2,4-dichlorophenoxy)acetic acid`, and carries CAS `94-75-7`.
- The structured evidence points back to the CultureMech occurrence table and
  the creation history documents an exact match against a ChEBI exact synonym.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/23-butanediol.yaml data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml data/ingredients/mapped/24-Dichlorophenoxyacetic_acid.yaml data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/24-Dichlorophenoxyacetic_acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:24-Dichlorophenoxyacetic_acid` to `CHEBI:28854` row.

## Evidence

- The active ChEBI page verifies that `2,4-Dichlorophenoxyacetic acid` is an
  exact name for the ChEBI `2,4-D` term.
- `occurrence_statistics` reports one CultureMech occurrence in one medium,
  matching the post-#337 refresh.
- `mappings/culturemech_residual_groundings.tsv` and
  `mappings/culturemech_residual_triage.tsv` record the source residual and
  target `CHEBI:28854` decision.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, CultureMech residual grounding, and residual-triage rows.

## Completeness

- Minor: `ingredient_type` is absent.
- Minor: ChEBI-backed CAS RN, formula, InChI, and SMILES have not been
  backfilled.
- There is no evidence that the active exact mapping itself is stale or
  over-broad.

## Recommended Edits

1. Set `ingredient_type: SINGLE_INGREDIENT`.
2. Backfill CAS RN `94-75-7`, formula `C8H6Cl2O3`, InChI, and SMILES from
   ChEBI.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
4. Re-run the focused strict/LinkML validators, `just qc-sssom`, and
   `just qc-flat-coverage` after those edits.
