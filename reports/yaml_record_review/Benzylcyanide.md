# `data/ingredients/mapped/Benzylcyanide.yaml`

## Verdict

Pass. The `Benzylcyanide` raw label maps exactly to `CHEBI:25979`
phenylacetonitrile through the `Benzyl cyanide` CHEBI synonym, and the
occurrence count, InChI, SSSOM row, `kg_microbe_node_id`, and aggregate copy all
agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Benzylcyanide.yaml`.
- Identifier and grounding: `identifier: CHEBI:25979` with
  `ontology_mapping.ontology_id: CHEBI:25979`,
  `ontology_label: phenylacetonitrile`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS search in `chebi` returns `CHEBI:25979` for both `phenylacetonitrile`
  and `Benzyl cyanide`; the latter is listed as a CHEBI synonym for the former.
- PubChem resolves phenylacetonitrile to formula `C8H7N` and the same standard
  InChI stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Benzoin.yaml data/ingredients/mapped/Benzothiazole.yaml data/ingredients/mapped/Benzyl_Alcohol.yaml data/ingredients/mapped/Benzyl_Isothiocyanate.yaml data/ingredients/mapped/Benzylcyanide.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Benzoin.yaml data/ingredients/mapped/Benzothiazole.yaml data/ingredients/mapped/Benzyl_Alcohol.yaml data/ingredients/mapped/Benzyl_Isothiocyanate.yaml data/ingredients/mapped/Benzylcyanide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 562 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/unmapped_ingredients_ols_exact_audit.tsv` still has a stale
  pre-curation `NO_EXACT_OLS_HIT` row for the old unmapped copy, but the
  2026-05-11 curation event superseded that earlier OLS miss by using local
  CHEBI exact-alias evidence for `Benzyl cyanide`.
- `mappings/culturemech_recipe_membership.tsv` has two rows for
  `CHEBI:25979`, matching `occurrence_statistics: 2/2`.
- The SSSOM row publishes `skos:exactMatch CHEBI:25979`, carries
  `Benzyl cyanide` in `other`, and has the same primary
  `kg_microbe_node_id: CHEBI:25979` as the YAML.

## Completeness

- The exact CHEBI identifier, raw label synonym, exact CHEBI synonyms, InChI,
  occurrence count, SSSOM row, and aggregate copy are populated.
- PubChem can additionally provide formula and SMILES for this compound, but
  their absence is not consequential because the exact identifier and InChI
  already identify the structure.
- No role, component list, or supplied-form split is required for this
  single-compound record.

## Recommended Edits

- None.
