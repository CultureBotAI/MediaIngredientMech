# `data/ingredients/mapped/Avocadene.yaml`

## Verdict

Pass. The CultureBotHT record exact-maps to `CHEBI:172520` `Avocadene`, and the
CAS, formula, structure, IUPAC synonym, SSSOM row, and aggregate copy all
represent the heptadec-16-ene-1,2,4-triol member of the avocado lipid cluster.

## Identity

- Reviewed record: `data/ingredients/mapped/Avocadene.yaml`.
- Identifier and grounding: `identifier: CHEBI:172520` with
  `ontology_mapping.ontology_id: CHEBI:172520`,
  `ontology_label: Avocadene`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search for `Avocadene` in ChEBI returned `CHEBI:172520`.
- PubChem resolves CAS `24607-08-7` to a heptadecene triol with formula
  `C17H34O3`, matching the saturated count and connectivity of the local
  ChEBI-derived formula and structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Avidin.yaml data/ingredients/mapped/Avocadene.yaml data/ingredients/mapped/Avocadyne.yaml data/ingredients/mapped/Avocatin_B.yaml data/ingredients/mapped/Avoparcin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Avocadene.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS exact search for `Avocadene` found `CHEBI:172520`.
- PubChem lookup for CAS `24607-08-7` resolved a formula-compatible
  heptadecene triol.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 502 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` already record
  `CHEBI:172520` as confirmed with no curation action.
- The single exact synonym in YAML and SSSOM is the ChEBI IUPAC name for
  Avocadene.

## Completeness

- The exact identifier, CAS RN, formula, InChI, SMILES, IUPAC synonym, SSSOM
  row, and aggregate copy are populated.
- The 0/0 occurrence count is correct for a CultureBotHT-only compound not
  present in CultureMech recipe memberships.
- No roles, components, or literature references are required for this
  single-ingredient CultureBotHT import.

## Recommended Edits

- None.
