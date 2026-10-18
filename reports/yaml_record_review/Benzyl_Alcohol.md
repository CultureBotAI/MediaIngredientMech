# `data/ingredients/mapped/Benzyl_Alcohol.yaml`

## Verdict

Pass. The exact `CHEBI:17987` benzyl-alcohol identity, microbedecoder
provenance, refreshed 2/2 CultureMech occurrence count, formula, InChI, SMILES,
SSSOM row, and aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Benzyl_Alcohol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17987` with
  `ontology_mapping.ontology_id: CHEBI:17987`,
  `ontology_label: benzyl alcohol`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS search in `chebi` returns `CHEBI:17987` as the `benzyl alcohol` class.
- PubChem resolves benzyl alcohol to formula `C7H8O` and the same standard
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
  `mappings/ingredient_mappings.sssom.tsv` row 560 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/microbedecoder_auto_mapped_review.tsv` row 79 approved the
  `CHEBI:17987` mapping after local OAK resolution and case-insensitive
  canonical-label agreement.
- `mappings/culturemech_recipe_membership.tsv` has two rows for
  `CHEBI:17987`, matching `occurrence_statistics: 2/2`.
- The current OLS and PubChem checks agree with the exact CHEBI grounding and
  the stored `ChEBI+PubChem` structure fields.

## Completeness

- The exact CHEBI identifier, single-ingredient classification, formula, InChI,
  SMILES, occurrence count, SSSOM row, and aggregate copy are populated.
- No role, component list, or supplied-form split is required for this
  single-compound record.

## Recommended Edits

- None.
