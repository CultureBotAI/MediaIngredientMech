# `data/ingredients/mapped/Bleomycin_Sulfate.yaml`

## Verdict

Pass. The exact `CHEBI:34582` bleomycin sulfate identity, CAS, selective-agent
role, generalized ChEBI formula, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bleomycin_Sulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:34582` with
  `ontology_mapping.ontology_id: CHEBI:34582`,
  `ontology_label: bleomycin sulfate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Bleomycin sulfate` returns the single ChEBI hit
  `CHEBI:34582`, whose cross-references include CAS `9041-93-4`.
- PubChem resolves CAS `9041-93-4` to `Bleomycin Sulfate`, supporting the CAS
  assignment even though its CID carries a concrete charged sulfate structure
  while ChEBI stores only the generalized `C50H71N16O21S2R.(H2O4S)n` formula.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bleomycin.yaml data/ingredients/mapped/Bleomycin_Sulfate.yaml data/ingredients/mapped/Blood.yaml data/ingredients/mapped/Bluensomycin.yaml data/ingredients/mapped/Bold_Trace_Stock.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bleomycin.yaml data/ingredients/mapped/Bleomycin_Sulfate.yaml data/ingredients/mapped/Blood.yaml data/ingredients/mapped/Bluensomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four OBO-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the OAK/OLS confirmation row in
  `mappings/ingredient_mappings_row_review_manifest.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 612, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Bleomycin_Sulfate` to `CHEBI:34582` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI salt identifier, CAS, generalized ChEBI formula,
  selective-agent role, SSSOM row, and aggregate copy are populated.

## Recommended Edits

- None.
