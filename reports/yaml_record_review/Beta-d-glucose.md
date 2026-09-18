# `data/ingredients/mapped/Beta-d-glucose.yaml`

## Verdict

Pass. The exact `CHEBI:15903` beta-D-glucose identity, corrected preferred
term, microbedecoder review trail, occurrence statistics, ChEBI structure
fields, SSSOM row, and aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Beta-d-glucose.yaml`.
- Identifier and grounding: `identifier: CHEBI:15903` with
  `ontology_mapping.ontology_id: CHEBI:15903`,
  `ontology_label: beta-D-glucose`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The 2026-09-10 history entry corrected the display-only lowercase
  stereodescriptor artifact from `Beta-d-glucose` to `Beta-D-glucose`; the
  file slug remains historical.
- PubChem resolves beta-D-glucose to formula `C6H12O6` and the same standard
  InChI stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beta-d-glucose.yaml data/ingredients/mapped/Beta-gentiobiose.yaml data/ingredients/mapped/Beta-lactose.yaml data/ingredients/mapped/Beta-nad.yaml data/ingredients/mapped/Betaine_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-d-glucose.yaml data/ingredients/mapped/Beta-gentiobiose.yaml data/ingredients/mapped/Beta-lactose.yaml data/ingredients/mapped/Beta-nad.yaml data/ingredients/mapped/Betaine_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 579 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the
  `CHEBI:15903` mapping after local OAK resolution and case-insensitive
  canonical-label agreement.
- `mappings/culturemech_recipe_membership.tsv` contains 16 rows for
  `CHEBI:15903`, matching the record's refreshed 16/16 medium and total
  occurrence counts.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact CHEBI identifier, corrected preferred label, single-ingredient
  classification, formula, InChI, SMILES, SSSOM row, occurrence statistics, and
  aggregate copy are populated.
- No CAS fallback, component list, role, or supplied-form split is required for
  this exact monosaccharide record.

## Recommended Edits

- None.
