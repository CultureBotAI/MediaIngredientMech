# `data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml`

## Verdict

Needs curation, major. The CAS-derived `CHEBI:18026`
`2,3-dihydroxybenzoic acid` identity, chemistry, occurrence count, SSSOM row,
and aggregate row pass, but `CARBON_SOURCE` is only supported by provisional
in-session LLM evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:18026` with
  `ontology_mapping.ontology_id: CHEBI:18026`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:18026`
  resolves to `2,3-dihydroxybenzoic acid`, lists formula `C7H6O4`, and carries
  CAS `303-38-8`.
- Formula, InChI, SMILES, CAS RN, and kg-microbe synonyms such as
  `2-pyrocatechuic acid`, `3-hydroxysalicylic acid`, and
  `catechol-3-carboxylic acid` are populated for the active ChEBI-backed
  ingredient.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/23-butanediol.yaml data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml data/ingredients/mapped/24-Dichlorophenoxyacetic_acid.yaml data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:23-dihydroxybenzoic_Acid` to `CHEBI:18026` row, with CAS `303-38-8`
  represented in the SSSOM `other` field.

## Evidence

- The active ChEBI page confirms that `CHEBI:18026` is current for the neutral
  acid named by the record, and OAK/OLS review independently confirmed the row.
- `mappings/culturemech_recipe_membership.tsv` and `occurrence_statistics` both
  report two CultureMech recipe occurrences.
- Major: the `nutritional_roles` slot asserts `CARBON_SOURCE` at confidence
  `0.6` from only `COMPUTATIONAL_PREDICTION` evidence whose reference text is
  `Assigned by in-session Claude reasoning (no external API)`.
- Stale: `mappings/record_research_validation.tsv` still contains a P1 row
  asking for direct `CHEBI:18026` verification; the direct ChEBI refresh now
  verifies the active term and neutral-acid identity.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, CultureMech membership, OAK/OLS review, and advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- The residual issue is limited to the unsupported nutritional-role assertion.

## Recommended Edits

1. Either remove `CARBON_SOURCE` or replace it with inspected
   formulation-specific evidence that directly supports this exact ingredient
   as a carbon source.
2. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
3. Re-run the focused strict/LinkML validators, role/evidence checks,
   `just qc-sssom`, and `just qc-flat-coverage` after those edits.
