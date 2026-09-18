# `data/ingredients/mapped/Brazilein.yaml`

## Verdict

Pass. The exact `CHEBI:69196` brazilein identity, CAS, ChEBI synonym, structure
fields, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Brazilein.yaml`.
- Identifier and grounding: `identifier: CHEBI:69196` with
  `ontology_mapping.ontology_id: CHEBI:69196`,
  `ontology_label: brazilein`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Brazilein` returns `CHEBI:69196`, whose formula,
  InChI, SMILES, and IUPAC synonym match the fields stored locally.
- PubChem resolves CAS `600-76-0` to the same formula. Its name lookup omits
  the stereochemical InChI layer, so the ChEBI term remains the structure
  source for this exact record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Brain_Heart_Infusion_Broth.yaml data/ingredients/mapped/Brainheart_infusion_agar.yaml data/ingredients/mapped/Brazilein.yaml data/ingredients/mapped/Bromocresol_Purple.yaml data/ingredients/mapped/Bromophenol_blue.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Brazilein.yaml data/ingredients/mapped/Bromocresol_Purple.yaml data/ingredients/mapped/Bromophenol_blue.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the OAK/OLS confirmation row in
  `mappings/ingredient_mappings_row_review_manifest.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 630, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Brazilein` to `CHEBI:69196` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, ChEBI synonym, single-ingredient
  classification, formula, InChI, SMILES, SSSOM row, and aggregate copy are
  populated.

## Recommended Edits

- None.
