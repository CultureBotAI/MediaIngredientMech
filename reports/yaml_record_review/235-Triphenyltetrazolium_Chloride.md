# `data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:78019`
`2,3,5-triphenyltetrazolium chloride` identity, chemistry, CultureBotHT
occurrence count, SSSOM row, and aggregate row pass, but `REDOX_INDICATOR` is
only supported by provisional in-session LLM evidence.

## Identity

- Reviewed record:
  `data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:78019` with
  `ontology_mapping.ontology_id: CHEBI:78019`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:78019`
  resolves to `2,3,5-triphenyltetrazolium chloride`, lists formula
  `C19H15N4.Cl`, and carries CAS `298-96-4`.
- Formula, InChI, SMILES, and CAS RN are populated for the active
  ChEBI-backed chloride salt.
- The absorbed `Triphenyltetrazolium Chloride` source label is retained as
  `RAW_TEXT` with #213 provenance because it is the same common TTC label with
  omitted locants, not a distinct ingredient.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/23-butanediol.yaml data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml data/ingredients/mapped/24-Dichlorophenoxyacetic_acid.yaml data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:235-Triphenyltetrazolium_Chloride` to `CHEBI:78019` row, with
  `2,3,5-triphenyl-2H-tetrazol-3-ium chloride`, the absorbed raw label, and CAS
  `298-96-4` represented in the SSSOM `other` field.

## Evidence

- The active ChEBI page and OAK/OLS review both confirm the exact chloride-salt
  identity.
- `occurrence_statistics` reports all 10 CultureBotHT occurrences that seeded
  this record.
- Major: the `physicochemical_roles` slot asserts `REDOX_INDICATOR` at
  confidence `0.6` from only `COMPUTATIONAL_PREDICTION` evidence whose
  reference text is `Assigned by in-session Claude reasoning (no external API)`.
- Stale: `mappings/record_research_validation.tsv` still contains a P1 row
  asking for direct `CHEBI:78019` verification; the direct ChEBI refresh now
  verifies the active term, formula, and counterion scope.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, and advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- The residual issue is limited to the unsupported physicochemical-role
  assertion.

## Recommended Edits

1. Either remove `REDOX_INDICATOR` or replace it with inspected
   formulation-specific evidence that directly supports this exact ingredient
   as a redox indicator.
2. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
3. Re-run the focused strict/LinkML validators, role/evidence checks,
   `just qc-sssom`, and `just qc-flat-coverage` after those edits.
