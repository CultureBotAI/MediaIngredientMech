# `data/ingredients/mapped/Butyric_Acid.yaml`

## Verdict

Pass. The exact `CHEBI:30772` butyric acid identity, CAS, synonyms,
nutritional roles, occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Butyric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30772` with
  `ontology_mapping.ontology_id: CHEBI:30772`,
  `ontology_label: butyric acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`,
  `kg_microbe_node_id: CHEBI:30772`, and `mapping_status: MAPPED`.
- Live OLS search for `Butyric acid` returns `CHEBI:30772` as the exact neutral
  butanoic-acid term, matching the local neutral structure rather than
  `CHEBI:17968` butyrate.
- PubChem resolves CAS `107-92-6` to CID 264 with formula `C4H8O2` and the
  same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Butyrate.yaml data/ingredients/mapped/Butyric_Acid.yaml data/ingredients/mapped/Butyricin_7423.yaml data/ingredients/mapped/Butyrolactam.yaml data/ingredients/mapped/CCCP.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Butyrate.yaml data/ingredients/mapped/Butyric_Acid.yaml data/ingredients/mapped/Butyricin_7423.yaml data/ingredients/mapped/Butyrolactam.yaml data/ingredients/mapped/CCCP.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the OAK/OLS confirmation row in
  `mappings/ingredient_mappings_row_review_manifest.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 643, all 48
  current `mappings/culturemech_recipe_membership.tsv` rows for
  `CHEBI:30772`, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Butyric_Acid` to `CHEBI:30772` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`; its `other` field includes the ChEBI-backed synonyms and
  `CAS:107-92-6`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, raw CultureMech role surface, ChEBI
  synonyms, carbon-source and energy-source roles, single-ingredient
  classification, formula, InChI, SMILES, 48/48 occurrence count, SSSOM row,
  and aggregate copy are populated.
- No components or environmental contexts are required for this
  single-compound nutrient.

## Recommended Edits

- None.
