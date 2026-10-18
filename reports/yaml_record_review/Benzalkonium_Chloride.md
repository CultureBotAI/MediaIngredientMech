# `data/ingredients/mapped/Benzalkonium_Chloride.yaml`

## Verdict

Pass. The exact `CHEBI:3020` identity, CultureBotHT CAS value,
variable-alkyl ChEBI formula, surfactant role, SSSOM row, and aggregate copy all
describe generic benzalkonium chloride.

## Identity

- Reviewed record: `data/ingredients/mapped/Benzalkonium_Chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:3020` with
  `ontology_mapping.ontology_id: CHEBI:3020`,
  `ontology_label: benzalkonium chloride`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `chebi` resolves `CHEBI:3020` to
  `benzalkonium chloride`.
- The ChEBI term is a class of quaternary ammonium chlorides with a variable
  alkyl chain; the stored `C9H13ClNR` formula and `*` SMILES wildcard follow
  that generic class, rather than over-specifying a single chain length.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beef_Heart.yaml data/ingredients/mapped/Beef_Heart_Infusion.yaml data/ingredients/mapped/Beijerincks_Solution.yaml data/ingredients/mapped/Benzaldehyde.yaml data/ingredients/mapped/Benzalkonium_Chloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Benzalkonium_Chloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 552 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 381 marked the
  `CHEBI:3020` mapping `CONFIRMED`; the fresh Engine A and OLS checks still
  agree with that verdict.
- PubChem did not resolve the generic CultureBotHT CAS `63449-41-2` to a
  single CID during this review, but the record does not assert a PubChem CID
  or a fixed-chain PubChem structure.
- The provisional `SURFACTANT` role is explicitly marked as a
  `COMPUTATIONAL_PREDICTION` from ChEBI ancestry with review recommended; it is
  not presented as literature-backed evidence.

## Completeness

- The exact CHEBI identifier, variable-chain CAS/formula/SMILES, provisional
  role, SSSOM row, and aggregate copy are populated.
- No source occurrence, component list, or fixed-chain supplied-form split is
  required for this generic ChEBI class record.

## Recommended Edits

- None.
