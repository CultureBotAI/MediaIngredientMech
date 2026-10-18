# `data/ingredients/mapped/Butyl_Vinyl_Ether.yaml`

## Verdict

Needs curation, minor. The exact `mesh:C521980` butyl vinyl ether identity,
MeSH prefix validation, occurrence count, SSSOM row, and aggregate copy agree,
but the top-level notes still say curator review is needed after the record was
promoted to the MeSH term.

## Identity

- Reviewed record: `data/ingredients/mapped/Butyl_Vinyl_Ether.yaml`.
- Identifier and grounding: `identifier: mesh:C521980` with
  `ontology_mapping.ontology_id: mesh:C521980`,
  `ontology_label: butyl vinyl ether`, `ontology_source: MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS exact search for `Butyl vinyl ether` returns `mesh:C521980`, and
  the prefix-specific OLS validation table resolves the same exact CURIE.
- PubChem resolves `Butyl vinyl ether` to CID 8108 with the expected
  `C6H12O` vinyl-ether formula.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Butan-1-amine.yaml data/ingredients/mapped/Butane-14-diol.yaml data/ingredients/mapped/Butanol.yaml data/ingredients/mapped/Butyl_Stearate.yaml data/ingredients/mapped/Butyl_Vinyl_Ether.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Butan-1-amine.yaml data/ingredients/mapped/Butane-14-diol.yaml data/ingredients/mapped/Butanol.yaml data/ingredients/mapped/Butyl_Stearate.yaml data/ingredients/mapped/Butyl_Vinyl_Ether.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the prefix-specific MeSH OLS validation row, the
  authoritative exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv`
  row 641, all four current `mappings/culturemech_recipe_membership.tsv` rows
  for `mesh:C521980`, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Butyl_Vinyl_Ether` to `mesh:C521980` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact MeSH identifier, raw imported label, 4/4 occurrence count, SSSOM
  row, and aggregate copy are populated.
- Minor gap: top-level `notes` still preserve the original import text saying
  no CAS/CHEBI/NCIT match was found and curator review was needed, which is
  stale after the record was upgraded to `mesh:C521980`.
- No roles, components, or environmental contexts are required for this
  single-compound record.

## Recommended Edits

- Minor: update the maintained `notes` in
  `data/ingredients/mapped/Butyl_Vinyl_Ether.yaml` to describe the accepted
  MeSH mapping, then run `just sync-curated` and focused strict/term/SSSOM
  validation.
